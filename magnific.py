#!/usr/bin/env python3
"""Gera as cenas de um projeto pela API do Magnific, sem pagar duas vezes pela mesma coisa.

Uso:
  python3 magnific.py imagens --projeto cenas-cape-cod.json --cena 7          # só a cena 7 (âncora)
  python3 magnific.py imagens --projeto cenas-cape-cod.json --ref saida-cape-cod/cena7.png
  python3 magnific.py videos  --projeto cenas-cape-cod.json
  python3 magnific.py imagens --projeto cenas.json --simular                  # mostra o que faria, sem gastar
  python3 magnific.py status  --projeto cenas.json                            # estado de cada cena

Proteções:
  - O pedido pago (POST) NUNCA é repetido automaticamente. Se a conexão cair no envio,
    a tarefa vira "ambígua" e o script para: confira no painel do Magnific antes de reenviar
    (--reenviar-ambiguas assume o risco de pagar de novo).
  - Todo task_id é gravado em <saida>/tarefas.json ANTES de esperar. Se o script cair,
    rodar de novo retoma a mesma tarefa em vez de criar outra.
  - Uma cena só é reaproveitada se foi gerada com os MESMOS prompt, modelo, referência e
    parâmetros (hash). Se o roteiro mudou, a cena aparece como "desatualizada" e só é
    regerada com --regerar-desatualizadas (ou --cena N).
  - Download vai para arquivo temporário, é validado e só então substitui o destino.

Configuração no JSON do projeto (opcionais, com padrão):
  "saida": "saida", "aspect_ratio": "widescreen_16_9", "duracao_video": "5",
  "modelo_imagem": "realism", "resolucao_imagem": "2k"

A chave vem de MAGNIFIC_API_KEY (ambiente ou .env nesta pasta).
"""
import argparse
import base64
import hashlib
import json
import os
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

BASE = "https://api.magnific.com"
PASTA = Path(__file__).resolve().parent
ROTA_IMAGEM = "/v1/ai/mystic"
ROTA_VIDEO_POST = "/v1/ai/image-to-video/kling-v2-6-pro"
ROTA_VIDEO_GET = "/v1/ai/image-to-video/kling-v2-6"


class SubmissaoAmbigua(Exception):
    """A conexão caiu depois de enviar um pedido pago: não sabemos se ele foi aceito."""


def chave():
    k = os.environ.get("MAGNIFIC_API_KEY")
    env = PASTA / ".env"
    if not k and env.exists():
        for linha in env.read_text().splitlines():
            if linha.startswith("MAGNIFIC_API_KEY="):
                k = linha.split("=", 1)[1].strip().strip('"')
    if not k:
        sys.exit("Defina MAGNIFIC_API_KEY no arquivo .env ou no ambiente.")
    return k


def req(metodo, caminho, corpo=None):
    """GET é repetido em falha de rede (é só leitura). POST nunca é repetido."""
    dados = json.dumps(corpo).encode() if corpo else None
    r = urllib.request.Request(
        BASE + caminho, data=dados, method=metodo,
        headers={"x-magnific-api-key": chave(), "Content-Type": "application/json"},
    )
    tentativas = 3 if metodo == "GET" else 1
    for tentativa in range(tentativas):
        try:
            with urllib.request.urlopen(r, timeout=120) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            # o servidor respondeu: o estado é conhecido (recusado), não houve cobrança ambígua
            sys.exit(f"Erro {e.code} em {metodo} {caminho}: {e.read().decode()[:500]}")
        except (urllib.error.URLError, socket.timeout, ConnectionError) as e:
            if metodo != "GET":
                raise SubmissaoAmbigua(f"conexão caiu no envio de {caminho}: {e}")
            print(f"  falha de conexão na consulta ({e}), tentando de novo...")
            time.sleep(5 * (tentativa + 1))
    sys.exit(f"Sem conexão com {caminho} (consulta). Rode de novo: a tarefa será retomada.")


# ---------- registro persistente ----------

class Registro:
    """tarefas.json: uma entrada por cena/tipo, com hash do pedido, task_id e estado."""

    def __init__(self, saida):
        self.arq = saida / "tarefas.json"
        self.dados = json.loads(self.arq.read_text()) if self.arq.exists() else {}

    def get(self, chave):
        return self.dados.get(chave)

    def set(self, chave, **campos):
        entrada = self.dados.setdefault(chave, {})
        entrada.update(campos, atualizado_em=datetime.now().isoformat(timespec="seconds"))
        tmp = self.arq.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.dados, ensure_ascii=False, indent=2))
        tmp.replace(self.arq)  # gravação atômica


def hash_pedido(rota, corpo):
    """Hash estável do que define o resultado (imagens em base64 entram pelo próprio hash)."""
    canon = json.dumps({"rota": rota, "corpo": corpo}, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(canon.encode()).hexdigest()[:16]


def esperar(caminho_status, task_id, intervalo=8, limite=1800):
    inicio = time.time()
    while time.time() - inicio < limite:
        d = req("GET", f"{caminho_status}/{task_id}")["data"]
        if d["status"] == "COMPLETED":
            return d["generated"]
        if d["status"] == "FAILED":
            return None
        time.sleep(intervalo)
    sys.exit(f"Tempo esgotado esperando {task_id}. Rode de novo para continuar esperando a mesma tarefa.")


def validar_midia(caminho):
    if not caminho.exists() or caminho.stat().st_size < 1024:
        return False
    if caminho.suffix == ".png":
        try:
            from PIL import Image
            with Image.open(caminho) as im:
                im.verify()
            return True
        except Exception:
            return False
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=width,height", "-of", "json", str(caminho)], capture_output=True, text=True)
    return r.returncode == 0 and bool(json.loads(r.stdout or "{}").get("streams"))


def baixar(url, destino):
    destino.parent.mkdir(parents=True, exist_ok=True)
    tmp = destino.with_name(destino.stem + ".parcial" + destino.suffix)
    urllib.request.urlretrieve(url, tmp)
    if not validar_midia(tmp):
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"download inválido para {destino.name}")
    tmp.replace(destino)
    print(f"  salvo: {destino.relative_to(PASTA) if destino.is_relative_to(PASTA) else destino}")


def b64(caminho):
    return base64.b64encode(Path(caminho).read_bytes()).decode()


# ---------- núcleo: gerar uma cena com segurança ----------

def processar(reg, chave_reg, rota_post, rota_get, corpo, destino, explicita, opcoes, intervalo=8):
    """Decide entre reaproveitar, retomar, recusar ou submeter. Retorna o estado final."""
    h = hash_pedido(rota_post, corpo)
    atual = reg.get(chave_reg) or {}

    # 1) já existe e foi gerado exatamente com este pedido
    if destino.exists() and atual.get("hash") == h and atual.get("estado") == "concluida" and not explicita:
        print(f"{chave_reg}: em dia (mesmo pedido), reaproveitando")
        return "em-dia"

    # 2) existe mas veio de outro pedido (roteiro mudou) ou de versão sem registro
    if destino.exists() and atual.get("hash") != h and not explicita and not opcoes.regerar_desatualizadas:
        origem = "sem registro de origem" if not atual else "pedido diferente do atual"
        print(f"{chave_reg}: DESATUALIZADA ({origem}). Não regerei para não gastar sem você pedir. "
              f"Use --regerar-desatualizadas ou --cena.")
        return "desatualizada"

    # 3) submissão anterior ambígua com este mesmo pedido
    if atual.get("hash") == h and atual.get("estado") == "ambigua" and not opcoes.reenviar_ambiguas:
        print(f"{chave_reg}: envio anterior AMBÍGUO ({atual.get('erro')}). Confira no painel do Magnific se "
              f"a tarefa existe. Para reenviar mesmo assim: --reenviar-ambiguas (pode cobrar 2x).")
        return "ambigua"

    # 4) tarefa já submetida com este pedido: retoma em vez de pagar de novo
    if atual.get("hash") == h and atual.get("task_id") and atual.get("estado") in ("submetida", "baixando"):
        task = atual["task_id"]
        print(f"{chave_reg}: retomando tarefa já paga {task}")
    else:
        if opcoes.simular:
            print(f"{chave_reg}: [simulação] enviaria POST {rota_post} (hash {h})")
            return "simulada"
        reg.set(chave_reg, hash=h, estado="enviando", destino=str(destino.name), task_id=None, erro=None)
        try:
            task = req("POST", rota_post, corpo)["data"]["task_id"]
        except SubmissaoAmbigua as e:
            reg.set(chave_reg, estado="ambigua", erro=str(e))
            print(f"{chave_reg}: {e}. NÃO reenviei. Confira no painel antes de tentar de novo.")
            return "ambigua"
        reg.set(chave_reg, estado="submetida", task_id=task)
        print(f"{chave_reg}: tarefa {task} registrada, aguardando...")

    urls = esperar(rota_get, task, intervalo=intervalo)
    if not urls:
        reg.set(chave_reg, estado="falhou", erro="Magnific retornou FAILED")
        print(f"{chave_reg}: tarefa {task} FALHOU no Magnific (consulte o painel sobre cobrança).")
        return "falhou"
    reg.set(chave_reg, estado="baixando", url=urls[0])
    baixar(urls[0], destino)
    reg.set(chave_reg, estado="concluida", arquivo=destino.name)
    return "concluida"


def selecionar(cfg, cena):
    cenas = [c for c in cfg["cenas"] if cena is None or c["id"] == cena]
    if cena is not None and not cenas:
        sys.exit(f"Cena {cena} não existe no projeto.")
    return cenas


def imagens(cfg, saida, reg, a):
    estados = {}
    for c in selecionar(cfg, a.cena):
        destino = saida / f"cena{c['id']}{a.sufixo}.png"
        corpo = {
            "prompt": f"{c['imagem']} {cfg['biblia']} {cfg['estilo']}",
            "resolution": cfg.get("resolucao_imagem", "2k"),
            "aspect_ratio": cfg.get("aspect_ratio", "widescreen_16_9"),
            "model": cfg.get("modelo_imagem", "realism"),
        }
        if a.ref and Path(a.ref).resolve() != destino.resolve():
            corpo["style_reference"] = b64(a.ref)
        estados[c["id"]] = processar(reg, f"imagem-cena{c['id']}{a.sufixo}", ROTA_IMAGEM, ROTA_IMAGEM,
                                     corpo, destino, a.cena is not None, a)
    return estados


def videos(cfg, saida, reg, a):
    estados = {}
    for c in selecionar(cfg, a.cena):
        img = saida / f"cena{c['id']}{a.sufixo}.png"
        destino = saida / f"cena{c['id']}{a.sufixo}.mp4"
        if not img.exists():
            print(f"video-cena{c['id']}: sem imagem, pulando")
            estados[c["id"]] = "sem-imagem"
            continue
        img_reg = reg.get(f"imagem-cena{c['id']}{a.sufixo}") or {}
        if img_reg.get("estado") not in (None, "concluida"):
            print(f"video-cena{c['id']}: imagem em estado '{img_reg.get('estado')}', pulando")
            estados[c["id"]] = "imagem-pendente"
            continue
        corpo = {
            "image": b64(img),
            "prompt": c["movimento"],
            "negative_prompt": cfg["negative_video"],
            "duration": str(cfg.get("duracao_video", "5")),
            "aspect_ratio": cfg.get("aspect_ratio", "widescreen_16_9"),
            "cfg_scale": 0.5,
            "generate_audio": False,
        }
        estados[c["id"]] = processar(reg, f"video-cena{c['id']}{a.sufixo}", ROTA_VIDEO_POST, ROTA_VIDEO_GET,
                                     corpo, destino, a.cena is not None, a, intervalo=15)
    return estados


def status(cfg, saida, reg):
    for c in cfg["cenas"]:
        for tipo, ext in (("imagem", "png"), ("video", "mp4")):
            e = reg.get(f"{tipo}-cena{c['id']}") or {}
            existe = (saida / f"cena{c['id']}.{ext}").exists()
            print(f"cena {c['id']:>2} {tipo:6} arquivo={'sim' if existe else 'não'}  "
                  f"registro={e.get('estado', 'sem registro')}  task={e.get('task_id') or '-'}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("etapa", choices=["imagens", "videos", "status"])
    p.add_argument("--projeto", default="cenas.json", help="JSON de cenas (padrão: cenas.json)")
    p.add_argument("--cena", type=int, help="gera só esta cena (regera mesmo se já existir)")
    p.add_argument("--ref", help="imagem usada como style_reference")
    p.add_argument("--sufixo", default="", help="sufixo do arquivo, para variações (ex.: _v2)")
    p.add_argument("--simular", action="store_true", help="não envia nada; mostra o que seria pago")
    p.add_argument("--regerar-desatualizadas", action="store_true",
                   help="regera cenas cujo pedido mudou desde a geração (gasta crédito)")
    p.add_argument("--reenviar-ambiguas", action="store_true",
                   help="reenvia tarefas cujo envio ficou ambíguo (pode cobrar duas vezes)")
    a = p.parse_args()

    proj = (PASTA / a.projeto) if not Path(a.projeto).is_absolute() else Path(a.projeto)
    cfg = json.loads(proj.read_text())
    saida = PASTA / cfg.get("saida", "saida")
    saida.mkdir(parents=True, exist_ok=True)
    reg = Registro(saida)

    if a.etapa == "status":
        status(cfg, saida, reg)
        return
    estados = imagens(cfg, saida, reg, a) if a.etapa == "imagens" else videos(cfg, saida, reg, a)
    resumo = {}
    for e in estados.values():
        resumo[e] = resumo.get(e, 0) + 1
    print("\nResumo: " + ", ".join(f"{k}={v}" for k, v in resumo.items()))
    if any(e in ("ambigua", "falhou") for e in estados.values()):
        sys.exit(1)


if __name__ == "__main__":
    main()
