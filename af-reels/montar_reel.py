#!/usr/bin/env python3
"""Monta um reel vertical (1080x1920) da série A.F a partir de videos/vNN/.

Uso:
  python3 montar_reel.py 1            # monta videos/v01/final.mp4

Depois, sempre: python3 ../ferramentas/qa_video.py videos/vNN/final.mp4 --duracao 33 --tolerancia 3

Espera em videos/vNN/:
  clipes/cena1.mp4 .. cena6.mp4   (9:16, ~5s cada)
  voz/f01.mp3 .. f06.mp3          (uma frase por cena)
  trilha.mp3                      (instrumental)
A narração (para legenda) vem de serie.json. A marca vem de marca/.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).parent
W, H = 1080, 1920
FPS = 30
FADE = 0.4            # transição entre cenas (s)
RESPIRO = 0.9         # folga mínima: voz + respiro dentro de cada cena (s)
CENA_MIN = 5.0        # duração nativa dos clipes Kling
HOLD_FIM = 3.6        # segundos congelados no último quadro com o cartão de CTA
CARD_APARECE = 2.2    # s depois do início da última fala em que o cartão entra

COBRE = (182, 114, 45)
AREIA = (244, 236, 227)
TERRA = (36, 26, 18)


def dur(arq):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(arq)],
        capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def fonte(tam, peso=800, largura=100):
    f = ImageFont.truetype(str(RAIZ / "marca" / "archivo.ttf"), tam)
    try:
        f.set_variation_by_axes([peso, largura])
    except Exception:
        pass
    return f


def quebrar(texto, f, max_w, draw):
    linhas, atual = [], ""
    for palavra in texto.split():
        teste = (atual + " " + palavra).strip()
        if draw.textlength(teste, font=f) <= max_w:
            atual = teste
        else:
            linhas.append(atual)
            atual = palavra
    if atual:
        linhas.append(atual)
    return linhas


def segmentos(frase):
    """Divide a frase em trechos curtos de legenda (por pontuação), mínimo ~14 caracteres."""
    frase = frase.replace("A.F", "A\u2024F")  # protege o ponto de "A.F" da divisão
    partes = [p.strip() for p in re.findall(r"[^.?!:,]+[.?!:,]?", frase) if p.strip()]
    saida = []
    for p in partes:
        if saida and len(saida[-1]) < 14:
            saida[-1] += " " + p
        else:
            saida.append(p)
    if len(saida) > 1 and len(saida[-1]) < 14:
        saida[-2] += " " + saida.pop()
    return [x.replace("A\u2024F", "A.F")[:1].upper() + x.replace("A\u2024F", "A.F")[1:] for x in saida]


def png_legenda(texto, destino):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = fonte(70, 800, 92)
    linhas = quebrar(texto.rstrip(".,:"), f, 880, d)
    alt = 86
    bloco = alt * len(linhas)
    y0 = 1330
    larg = max(d.textlength(l, font=f) for l in linhas)
    d.rounded_rectangle([(W - larg) / 2 - 36, y0 - 22, (W + larg) / 2 + 36, y0 + bloco + 8],
                        radius=26, fill=TERRA + (150,))
    for i, l in enumerate(linhas):
        d.text((W / 2, y0 + i * alt), l, font=f, fill=AREIA + (255,), anchor="mt")
    img.save(destino)


def png_marca_dagua(destino):
    logo = Image.open(RAIZ / "marca" / "logo-branco.png").convert("RGBA")
    larg = 420
    logo = logo.resize((larg, int(logo.height * larg / logo.width)), Image.LANCZOS)
    alfa = logo.getchannel("A").point(lambda v: int(v * 0.85))
    logo.putalpha(alfa)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    img.alpha_composite(logo, (48, 140))
    img.save(destino)


def png_cartao(destino, marca):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # degradê escuro de baixo para cima (legibilidade do CTA)
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    topo = 620
    for y in range(topo, H):
        a = int(235 * min(1, (y - topo) / 420))
        gd.line([(0, y), (W, y)], fill=TERRA + (a,))
    img.alpha_composite(grad)
    d = ImageDraw.Draw(img)

    logo = Image.open(RAIZ / "marca" / "logo-branco.png").convert("RGBA")
    larg = 760
    logo = logo.resize((larg, int(logo.height * larg / logo.width)), Image.LANCZOS)
    img.alpha_composite(logo, ((W - larg) // 2, 800))

    d.line([(W / 2 - 90, 1060), (W / 2 + 90, 1060)], fill=COBRE + (255,), width=4)
    f_tag = fonte(44, 600, 100)
    y = 1100
    for l in quebrar(marca["tagline"], f_tag, 860, d):
        d.text((W / 2, y), l, font=f_tag, fill=AREIA + (255,), anchor="mt")
        y += 58

    # botão de CTA
    f_btn = fonte(50, 800, 100)
    txt = marca["cta_site"].upper()
    bw = d.textlength(txt, font=f_btn) + 110
    bx0, by0 = (W - bw) / 2, 1290
    d.rounded_rectangle([bx0, by0, bx0 + bw, by0 + 104], radius=52, fill=COBRE + (255,))
    d.text((W / 2, by0 + 52), txt, font=f_btn, fill=(255, 255, 255, 255), anchor="mm")

    f_num = fonte(60, 800, 100)
    d.text((W / 2, 1450), "WhatsApp  " + marca["whatsapp"], font=f_num, fill=AREIA + (255,), anchor="mt")
    f_site = fonte(34, 500, 100)
    d.text((W / 2, 1535), marca["site"], font=f_site, fill=AREIA + (210,), anchor="mt")
    img.save(destino)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    n = int(sys.argv[1])
    serie = json.loads((RAIZ / "serie.json").read_text())
    video = next(v for v in serie["videos"] if v["id"] == n)
    marca = serie["marca"]
    pasta = RAIZ / "videos" / f"v{n:02d}"
    tmp = pasta / "_overlays"
    tmp.mkdir(exist_ok=True)

    nc = len(video["narracao"])
    clipes = [pasta / "clipes" / f"cena{i + 1}.mp4" for i in range(nc)]
    vozes = [pasta / "voz" / f"f{i + 1:02d}.mp3" for i in range(nc)]
    trilha = pasta / "trilha.mp3"
    faltam = [str(p) for p in clipes + vozes + [trilha] if not p.exists()]
    if faltam:
        sys.exit("Faltam arquivos:\n  " + "\n  ".join(faltam))

    vd = [dur(v) for v in vozes]
    D = [max(CENA_MIN, v + RESPIRO) for v in vd]                 # duração de cada cena na timeline
    t = [sum(D[j] - FADE for j in range(i)) for i in range(nc)]   # início de cada cena
    voz_ini = [t[i] + (0.45 if i else 0.5) for i in range(nc)]
    corpo = t[-1] + D[-1]
    total = corpo + HOLD_FIM
    card_t = voz_ini[-1] + CARD_APARECE

    # ---- overlays PNG ----
    png_marca_dagua(tmp / "marca.png")
    png_cartao(tmp / "cartao.png", marca)
    legendas = []  # (png, ini, fim)
    k = 0
    for i, frase in enumerate(video["narracao"]):
        segs = segmentos(frase)
        if i == nc - 1:
            segs = segs[:1]           # a última fala vira cartão de CTA
        pesos = [len(s) for s in segs]
        if i == nc - 1:
            fim_fala = card_t
            ini = voz_ini[i]
            partes = [(ini, fim_fala)]
        else:
            cursor = voz_ini[i]
            partes = []
            for p in pesos:
                d_seg = vd[i] * p / sum(pesos)
                partes.append((cursor, cursor + d_seg))
                cursor += d_seg
        for s, (ini, fim) in zip(segs, partes):
            arq = tmp / f"leg{k:02d}.png"
            png_legenda(s, arq)
            legendas.append((arq, ini, fim + 0.08))
            k += 1

    # ---- grafo ffmpeg ----
    entradas, f = [], []
    for i, c in enumerate(clipes):
        entradas += ["-i", str(c)]
        vel = CENA_MIN / D[i]  # <1 = câmera lenta para a cena caber na fala
        lento = f",setpts=PTS/{vel:.4f},minterpolate=fps={FPS}:mi_mode=blend" if vel < 0.999 else ""
        fim = f",tpad=stop_mode=clone:stop_duration={HOLD_FIM + 0.5:.2f}" if i == nc - 1 else ""
        f.append(f"[{i}:v]fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,"
                 f"crop={W}:{H},setsar=1{lento}{fim},format=yuv420p[v{i}]")
    atual = "v0"
    for i in range(1, nc):
        f.append(f"[{atual}][v{i}]xfade=transition=fade:duration={FADE}:offset={t[i]:.3f}[x{i}]")
        atual = f"x{i}"

    idx = nc
    entradas += ["-loop", "1", "-framerate", str(FPS), "-t", f"{total:.2f}", "-i", str(tmp / "marca.png")]
    f.append(f"[{idx}:v]format=rgba,fade=t=in:st=0.6:d=0.8:alpha=1,"
             f"fade=t=out:st={card_t:.2f}:d=0.5:alpha=1[marca]")
    f.append(f"[{atual}][marca]overlay=0:0:format=auto[b0]")
    atual = "b0"
    idx += 1
    for j, (arq, ini, fim) in enumerate(legendas):
        entradas += ["-loop", "1", "-framerate", str(FPS), "-t", f"{total:.2f}", "-i", str(arq)]
        f.append(f"[{atual}][{idx}:v]overlay=0:0:format=auto:enable='between(t,{ini:.2f},{fim:.2f})'[b{j + 1}]")
        atual = f"b{j + 1}"
        idx += 1
    entradas += ["-loop", "1", "-framerate", str(FPS), "-t", f"{total:.2f}", "-i", str(tmp / "cartao.png")]
    f.append(f"[{idx}:v]format=rgba,fade=t=in:st={card_t:.2f}:d=0.6:alpha=1[cartao]")
    f.append(f"[{atual}][cartao]overlay=0:0:format=auto,fade=t=in:st=0:d=0.4,"
             f"fade=t=out:st={total - 0.5:.2f}:d=0.5,format=yuv420p[vout]")
    idx += 1

    # ---- áudio: voz + trilha com ducking ----
    rotulos = []
    for j, v in enumerate(vozes):
        entradas += ["-i", str(v)]
        ms = int(voz_ini[j] * 1000)
        f.append(f"[{idx}:a]aresample=44100,aformat=channel_layouts=stereo,"
                 f"highpass=f=70,adelay={ms}|{ms}[n{j}]")
        rotulos.append(f"[n{j}]")
        idx += 1
    f.append("".join(rotulos) + f"amix=inputs={nc}:normalize=0,"
             f"acompressor=threshold=-18dB:ratio=3:attack=5:release=120,volume=1.5,"
             f"apad,atrim=0:{total:.2f},asplit=2[voz][chave]")
    entradas += ["-i", str(trilha)]
    f.append(f"[{idx}:a]aresample=44100,aformat=channel_layouts=stereo,apad,atrim=0:{total:.2f},volume=0.55,"
             f"afade=t=in:st=0:d=0.8,afade=t=out:st={total - 2.0:.2f}:d=2.0[mus]")
    f.append("[mus][chave]sidechaincompress=threshold=0.03:ratio=6:attack=15:release=400[musduck]")
    f.append("[musduck][voz]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]")

    destino = pasta / "final.mp4"
    cmd = (["ffmpeg", "-y", "-v", "error", "-stats"] + entradas +
           ["-filter_complex", ";".join(f), "-map", "[vout]", "-map", "[aout]",
            "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-t", f"{total:.2f}", str(destino)])
    print(f"Montando v{n:02d}: {nc} cenas, {len(legendas)} legendas, {total:.1f}s ...")
    subprocess.run(cmd, check=True)
    print(f"pronto: {destino.relative_to(RAIZ)} ({total:.1f}s, {W}x{H})")


if __name__ == "__main__":
    main()
