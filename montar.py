#!/usr/bin/env python3
"""Monta o vídeo final: cenas escolhidas + transições + trilha + encerramento."""
import subprocess
from pathlib import Path

S = Path(__file__).parent / "saida"
FADE = 0.6          # duração de cada transição (s)
SEGURA_FIM = 1.8    # segundos extras congelados no último quadro, para o encerramento

# (arquivo, início, duração) — cena 5 cortada antes de o céu ficar rosa demais
CENAS = [
    ("cena1.mp4", 0, 5.0),
    ("cena2.mp4", 0, 5.0),
    ("cena3_v2.mp4", 0, 5.0),
    ("cena4.mp4", 0, 5.0),
    ("cena5.mp4", 0, 3.6),
    ("cena6_v2.mp4", 0, 5.0),
    ("cena7.mp4", 0, 5.0),
]

entradas, filtros = [], []
for i, (arq, ini, dur) in enumerate(CENAS):
    entradas += ["-ss", str(ini), "-t", str(dur), "-i", str(S / arq)]
    extra = f",tpad=stop_mode=clone:stop_duration={SEGURA_FIM}" if i == len(CENAS) - 1 else ""
    filtros.append(
        f"[{i}:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
        f"fps=24,format=yuv420p,setsar=1{extra}[v{i}]"
    )

atual, offset = "v0", 0.0
for i in range(1, len(CENAS)):
    offset += CENAS[i - 1][2] - FADE
    filtros.append(f"[{atual}][v{i}]xfade=transition=fade:duration={FADE}:offset={offset:.3f}[x{i}]")
    atual = f"x{i}"

total = sum(d for _, _, d in CENAS) - FADE * (len(CENAS) - 1) + SEGURA_FIM
inicio_marca = total - SEGURA_FIM - 2.6

n = len(CENAS)
filtros.append(
    f"[{n}:v]format=rgba,scale=1920:1080,fade=t=in:st={inicio_marca:.2f}:d=1.2:alpha=1[marca]"
)
filtros.append(f"[{atual}][marca]overlay=0:0,fade=t=in:st=0:d=0.6[vout]")
filtros.append(
    f"[{n + 1}:a]atrim=0:{total:.2f},afade=t=in:st=0:d=0.8,"
    f"afade=t=out:st={total - 2.5:.2f}:d=2.5[aout]"
)

cmd = (
    ["ffmpeg", "-y", "-v", "error"] + entradas
    + ["-loop", "1", "-t", f"{total:.2f}", "-i", str(S / "encerramento.png")]
    + ["-i", str(S / "trilha.wav")]
    + ["-filter_complex", ";".join(filtros), "-map", "[vout]", "-map", "[aout]",
       "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
       "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
       str(S.parent / "castle-masonry-quintal-cape-cod.mp4")]
)
subprocess.run(cmd, check=True)
print(f"pronto: castle-masonry-quintal-cape-cod.mp4 ({total:.1f}s)")
