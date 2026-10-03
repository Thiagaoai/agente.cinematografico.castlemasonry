#!/usr/bin/env python3
"""QA técnico de um vídeo final. Mede o arquivo real; não confia no que foi planejado.

Uso:
  python3 ferramentas/qa_video.py caminho/do/video.mp4 --duracao 30
  python3 ferramentas/qa_video.py video.mp4 --duracao 30 --largura 1080 --altura 1920

Grava ao lado do vídeo:
  <video>.qa.json      checagens (esperado x medido), hash do arquivo e estado
  <video>.quadros.jpg  folha com 8 quadros para revisão visual

Estados possíveis gravados aqui:
  reprovado-tecnico     alguma checagem falhou: não entregar
  aguardando-escuta     todas as checagens técnicas passaram; falta revisão humana
A aprovação final só acontece com `ferramentas/estado.py aprovar` (pessoa ouviu e viu).

Sai com código 1 se reprovar.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Alvos do projeto (critério nosso, não regra do Instagram).
LUFS_MIN, LUFS_MAX = -16.0, -14.0
TRUE_PEAK_MAX = -1.5


def sha256(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def probe(caminho):
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(caminho)
    ]))


def loudness(caminho):
    """Loudness integrado (LUFS), true peak (dBTP) e LRA do arquivo, via ebur128."""
    r = subprocess.run(
        ["ffmpeg", "-nostats", "-hide_banner", "-i", str(caminho),
         "-filter_complex", "ebur128=peak=true", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    resumo = r.stderr[r.stderr.rfind("Summary:"):]
    i = re.search(r"I:\s+(-?[\d.]+|-inf) LUFS", resumo)
    lra = re.search(r"LRA:\s+(-?[\d.]+) LU", resumo)
    tp = re.search(r"True peak:\s+Peak:\s+(-?[\d.]+|-inf) dBFS", resumo)
    paraf = lambda m: float(m.group(1)) if m and m.group(1) != "-inf" else None
    return paraf(i), paraf(tp), paraf(lra)


def decodifica_inteiro(caminho):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(caminho), "-f", "null", "-"],
                       capture_output=True, text=True)
    return r.returncode == 0 and not r.stderr.strip(), r.stderr.strip()[:500]


def folha_de_quadros(caminho, duracao, destino):
    """8 quadros espaçados (do início ao fim) em grade 4x2, com o tempo de cada um."""
    import tempfile
    from PIL import Image, ImageDraw
    n, larg = 8, 270
    tempos = [min(duracao - 0.05, max(0.05, duracao * k / (n - 1))) for k in range(n)]
    quadros = []
    with tempfile.TemporaryDirectory() as tmp:
        for k, t in enumerate(tempos):
            arq = Path(tmp) / f"q{k}.png"
            r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", str(caminho),
                                "-frames:v", "1", "-vf", f"scale={larg}:-2", str(arq)],
                               capture_output=True)
            if r.returncode != 0 or not arq.exists():
                return False, tempos
            quadros.append(Image.open(arq).convert("RGB"))
        alt = quadros[0].height
        folha = Image.new("RGB", (larg * 4, alt * 2), "black")
        for k, (q, t) in enumerate(zip(quadros, tempos)):
            x, y = (k % 4) * larg, (k // 4) * alt
            folha.paste(q, (x, y))
            d = ImageDraw.Draw(folha)
            d.rectangle((x, y, x + 70, y + 24), fill="black")
            d.text((x + 6, y + 5), f"{t:.1f}s", fill="white")
        folha.save(destino, quality=88)
    return True, tempos


def checar(nome, esperado, medido, ok):
    return {"checagem": nome, "esperado": esperado, "medido": medido, "ok": bool(ok)}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video")
    p.add_argument("--duracao", type=float, required=True, help="duração alvo em segundos")
    p.add_argument("--tolerancia", type=float, default=None, help="tolerância da duração (padrão: 1 quadro)")
    p.add_argument("--largura", type=int, default=1080)
    p.add_argument("--altura", type=int, default=1920)
    p.add_argument("--sem-audio", action="store_true", help="vídeo propositalmente mudo")
    a = p.parse_args()

    video = Path(a.video).resolve()
    if not video.is_file():
        sys.exit(f"Arquivo não encontrado: {video}")

    d = probe(video)
    v = next((s for s in d["streams"] if s["codec_type"] == "video"), None)
    au = next((s for s in d["streams"] if s["codec_type"] == "audio"), None)
    dur = float(d["format"].get("duration", 0))
    checagens = []

    if v is None:
        checagens.append(checar("stream de vídeo", "presente", "ausente", False))
        fps = 0.0
    else:
        num, den = (int(x) for x in v["r_frame_rate"].split("/"))
        fps = num / den if den else 0.0
        checagens += [
            checar("resolução", f"{a.largura}x{a.altura}", f"{v['width']}x{v['height']}",
                   (v["width"], v["height"]) == (a.largura, a.altura)),
            checar("codec de vídeo", "h264", v["codec_name"], v["codec_name"] == "h264"),
            checar("pixel format", "yuv420p", v.get("pix_fmt"), v.get("pix_fmt") == "yuv420p"),
            checar("fps", "23.976 a 60", round(fps, 3), 23.9 <= fps <= 60),
        ]

    tol = a.tolerancia if a.tolerancia is not None else (1 / fps + 0.02 if fps else 0.1)
    checagens.append(checar("duração (s)", f"{a.duracao} ± {tol:.3f}", round(dur, 3),
                            abs(dur - a.duracao) <= tol))

    lufs = tp = lra = None
    if a.sem_audio:
        checagens.append(checar("áudio", "ausente (declarado)", "presente" if au else "ausente", au is None))
    elif au is None:
        checagens.append(checar("stream de áudio", "presente", "ausente", False))
    else:
        checagens += [
            checar("codec de áudio", "aac", au["codec_name"], au["codec_name"] == "aac"),
            checar("taxa de amostragem", "44100 ou 48000", int(au["sample_rate"]),
                   int(au["sample_rate"]) in (44100, 48000)),
            checar("canais", "1 ou 2", au.get("channels"), au.get("channels") in (1, 2)),
        ]
        lufs, tp, lra = loudness(video)
        checagens += [
            checar("loudness integrado (LUFS)", f"{LUFS_MIN} a {LUFS_MAX}", lufs,
                   lufs is not None and LUFS_MIN <= lufs <= LUFS_MAX),
            checar("true peak (dBTP)", f"<= {TRUE_PEAK_MAX}", tp, tp is not None and tp <= TRUE_PEAK_MAX),
        ]

    ok_decode, erro_decode = decodifica_inteiro(video)
    checagens.append(checar("decodificação completa", "sem erros", erro_decode or "sem erros", ok_decode))

    folha = video.with_suffix(".quadros.jpg")
    ok_folha, tempos = folha_de_quadros(video, dur, folha)
    checagens.append(checar("folha de quadros gerada", str(folha.name), "ok" if ok_folha else "falhou", ok_folha))

    passou = all(c["ok"] for c in checagens)
    resultado = {
        "arquivo": video.name,
        "sha256": sha256(video),
        "medido_em": datetime.now().isoformat(timespec="seconds"),
        "estado": "aguardando-escuta" if passou else "reprovado-tecnico",
        "checagens": checagens,
        "audio": {"lufs_integrado": lufs, "true_peak_dbtp": tp, "lra_lu": lra},
        "folha_de_quadros": folha.name if ok_folha else None,
        "quadros_em_s": [round(t, 2) for t in tempos],
        "nao_verificado_por_este_script": [
            "pronúncia, sotaque e naturalidade da voz (exige escuta humana)",
            "conteúdo visual: deformações, texto ilegível, rosto, coerência entre cenas (olhar a folha de quadros)",
            "movimento entre os quadros amostrados e transições",
            "veracidade das afirmações do roteiro (conferir af-reels/marca/fatos.md)",
        ],
    }
    if not passou:
        resultado["motivos_reprovacao"] = [c["checagem"] for c in checagens if not c["ok"]]

    saida = video.with_suffix(".qa.json")
    # preserva histórico de aprovação apenas se o arquivo não mudou
    if saida.exists():
        antigo = json.loads(saida.read_text())
        if antigo.get("sha256") == resultado["sha256"] and antigo.get("aprovacao"):
            resultado["aprovacao"] = antigo["aprovacao"]
            resultado["estado"] = antigo["estado"] if passou else "reprovado-tecnico"
    saida.write_text(json.dumps(resultado, ensure_ascii=False, indent=2))

    print(f"\n{video.name}")
    for c in checagens:
        print(f"  {'OK  ' if c['ok'] else 'FALHA'} {c['checagem']}: medido {c['medido']} (esperado {c['esperado']})")
    print(f"\nEstado: {resultado['estado']}")
    print(f"Relatório: {saida}")
    if ok_folha:
        print(f"Folha de quadros (olhar antes de aprovar): {folha}")
    print("Não verificado aqui: " + "; ".join(resultado["nao_verificado_por_este_script"]))
    sys.exit(0 if passou else 1)


if __name__ == "__main__":
    main()
