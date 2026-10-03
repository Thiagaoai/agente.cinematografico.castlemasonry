#!/usr/bin/env python3
"""Checa o ambiente ANTES de gastar crédito. Sai com código 1 se faltar algo essencial.

Uso:
  python3 ferramentas/preflight.py
"""
import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
FILTROS_ESSENCIAIS = ["loudnorm", "ebur128", "xfade", "sidechaincompress", "amix", "alimiter", "overlay", "concat"]
FILTROS_OPCIONAIS = ["subtitles", "drawtext"]


def main():
    falhas, avisos = [], []

    for prog in ("ffmpeg", "ffprobe"):
        if not shutil.which(prog):
            falhas.append(f"{prog} não instalado (brew install ffmpeg)")

    if shutil.which("ffmpeg"):
        lista = subprocess.run(["ffmpeg", "-hide_banner", "-filters"], capture_output=True, text=True).stdout
        nomes = {linha.split()[1] for linha in lista.splitlines() if len(linha.split()) > 2}
        for f in FILTROS_ESSENCIAIS:
            if f not in nomes:
                falhas.append(f"filtro ffmpeg ausente: {f}")
        for f in FILTROS_OPCIONAIS:
            if f not in nomes:
                avisos.append(f"filtro ffmpeg opcional ausente: {f} (legendas são rasterizadas com PIL)")
        enc = subprocess.run(["ffmpeg", "-hide_banner", "-encoders"], capture_output=True, text=True).stdout
        for e in ("libx264", "aac"):
            if f" {e} " not in enc:
                falhas.append(f"encoder ausente: {e}")

    if importlib.util.find_spec("PIL") is None:
        falhas.append("Pillow não instalado (python3 -m pip install -r requirements.txt)")

    for arq in ("af-reels/marca/archivo.ttf", "af-reels/marca/logo-branco.png", "af-reels/marca/logo-cobre.png",
                "af-reels/serie.json", "af-reels/marca/fatos.md"):
        if not (RAIZ / arq).is_file():
            falhas.append(f"arquivo de marca/dados ausente: {arq}")

    env = RAIZ / ".env"
    tem_chave = env.is_file() and any(
        l.startswith("MAGNIFIC_API_KEY=") and l.split("=", 1)[1].strip() not in ("", "cole_sua_chave_aqui")
        for l in env.read_text().splitlines())
    if not tem_chave:
        avisos.append("MAGNIFIC_API_KEY não definida no .env (só necessária para magnific.py; o MCP usa a conta conectada)")

    for a in avisos:
        print(f"AVISO  {a}")
    for f in falhas:
        print(f"FALHA  {f}")
    if falhas:
        print("\nAmbiente NÃO está pronto. Corrija antes de gerar qualquer coisa paga.")
        sys.exit(1)
    print("Ambiente pronto (ferramentas locais). Ferramentas MCP (Magnific, ElevenLabs) são checadas na conversa.")


if __name__ == "__main__":
    main()
