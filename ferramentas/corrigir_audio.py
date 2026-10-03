#!/usr/bin/env python3
"""Ajusta loudness e true peak do áudio de um vídeo pronto, sem re-encodar a imagem.

Uso:
  python3 ferramentas/corrigir_audio.py entrada.mp4 saida.mp4

Faz loudnorm em duas passagens (mede, depois aplica com os valores medidos),
mira -14,5 LUFS e -2,0 dBTP (margem para o encoder AAC) e copia o vídeo como está.
Nunca sobrescreve a entrada. Depois rode qa_video.py na saída: o que vale é a medição.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ALVO_I, ALVO_TP, ALVO_LRA = -14.5, -2.0, 11


def medir(entrada):
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(entrada), "-vn",
         "-af", f"loudnorm=I={ALVO_I}:TP={ALVO_TP}:LRA={ALVO_LRA}:print_format=json", "-f", "null", "-"],
        capture_output=True, text=True, check=True,
    )
    return json.loads(re.findall(r"\{[^{}]*\}", r.stderr)[-1])


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    entrada, saida = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    if not entrada.is_file():
        sys.exit(f"Não encontrado: {entrada}")
    if entrada == saida:
        sys.exit("A saída precisa ser outro arquivo (a entrada é preservada).")

    m = medir(entrada)
    print(f"antes: {m['input_i']} LUFS, true peak {m['input_tp']} dBTP")
    filtro = (f"loudnorm=I={ALVO_I}:TP={ALVO_TP}:LRA={ALVO_LRA}"
              f":measured_I={m['input_i']}:measured_TP={m['input_tp']}"
              f":measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}"
              f":offset={m['target_offset']}:linear=true,aresample=48000")
    temporario = saida.with_name(saida.stem + ".parcial" + saida.suffix)
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(entrada),
                    "-map", "0:v:0", "-map", "0:a:0", "-c:v", "copy", "-af", filtro,
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(temporario)], check=True)
    temporario.replace(saida)
    print(f"salvo: {saida}")
    print("Agora meça de verdade: python3 ferramentas/qa_video.py", saida, "--duracao <alvo>")


if __name__ == "__main__":
    main()
