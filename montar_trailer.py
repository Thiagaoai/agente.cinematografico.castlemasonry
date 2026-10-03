#!/usr/bin/env python3
"""Versão trailer: narração em inglês sincronizada por cena + música de ação + CTA."""
import subprocess
from pathlib import Path

S = Path(__file__).parent / "saida"
V = S / "voz"
FADE = 0.5
SAIDA = S.parent / "castle-masonry-trailer-en.mp4"

# (arquivo, corte em segundos, velocidade) — velocidade < 1 deixa a cena mais lenta
CENAS = [
    ("cena1.mp4", 5.0, 0.84),     # chegada pelo telhado — "On Cape Cod..."
    ("cena2.mp4", 5.0, 1.0),      # pátio — "And home..." / "A stone patio."
    ("cena3_v2.mp4", 5.0, 1.0),   # piscina — "A pool that glows..."
    ("cena4.mp4", 5.0, 1.0),      # golfe — "A putting green."
    ("cena5.mp4", 3.6, 1.0),      # lareira — "A fireplace..."
    ("cena6_v2.mp4", 5.0, 1.0),   # fire pit — "Every stone... While you rest..."
    ("cena7.mp4", 5.0, 0.6),      # aéreo final — marca + CTA
]
SEGURA_FIM = 4.9

duracoes = [corte / vel for _, corte, vel in CENAS]
inicios, t = [], 0.0
for d in duracoes:
    inicios.append(t)
    t += d - FADE
total = inicios[-1] + duracoes[-1] + SEGURA_FIM
marca = inicios[-1] + 2.8

# (frase, instante no vídeo)
VOZ = [
    ("f01.wav", 0.8),
    ("f02.wav", inicios[1] + 0.4),
    ("f03.wav", inicios[1] + 3.7),
    ("f04.wav", inicios[2] + 0.5),
    ("f05.wav", inicios[3] + 0.7),
    ("f06.wav", inicios[4] + 0.4),
    ("f07.wav", inicios[5] + 0.3),
    ("f08.wav", marca + 0.4),
]

entradas, f = [], []
for i, (arq, corte, vel) in enumerate(CENAS):
    entradas += ["-t", str(corte), "-i", str(S / arq)]
    lento = f",setpts=PTS/{vel},minterpolate=fps=24:mi_mode=blend" if vel != 1.0 else ""
    fim = f",tpad=stop_mode=clone:stop_duration={SEGURA_FIM}" if i == len(CENAS) - 1 else ""
    f.append(f"[{i}:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
             f"fps=24{lento},format=yuv420p,setsar=1{fim}[v{i}]")
atual = "v0"
for i in range(1, len(CENAS)):
    f.append(f"[{atual}][v{i}]xfade=transition=fade:duration={FADE}:offset={inicios[i]:.3f}[x{i}]")
    atual = f"x{i}"

n = len(CENAS)
entradas += ["-loop", "1", "-t", f"{total:.2f}", "-i", str(S / "encerramento_trailer.png")]
f.append(f"[{n}:v]format=rgba,fade=t=in:st={marca:.2f}:d=1.0:alpha=1[marca]")
f.append(f"[{atual}][marca]overlay=0:0,fade=t=in:st=0:d=0.5,fade=t=out:st={total - 0.6:.2f}:d=0.6[vout]")

# narração: cada frase atrasada até seu instante e somada
voz_labels = []
for j, (arq, quando) in enumerate(VOZ):
    k = n + 1 + j
    entradas += ["-i", str(V / arq)]
    ms = int(quando * 1000)
    f.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms}[n{j}]")
    voz_labels.append(f"[n{j}]")
f.append("".join(voz_labels) + f"amix=inputs={len(VOZ)}:normalize=0,"
         "highpass=f=70,acompressor=threshold=-18dB:ratio=3:attack=5:release=120,"
         f"volume=1.6,apad,atrim=0:{total:.2f},asplit=2[voz][chave]")

m = n + 1 + len(VOZ)
entradas += ["-i", str(S / "trilha_trailer.mp3")]
f.append(f"[{m}:a]aresample=44100,aformat=channel_layouts=stereo,atrim=0:{total:.2f},volume=0.75,"
         f"afade=t=out:st={total - 1.5:.2f}:d=1.5[mus]")
f.append("[mus][chave]sidechaincompress=threshold=0.03:ratio=8:attack=15:release=400[musduck]")
f.append("[musduck][voz]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]")

cmd = (["ffmpeg", "-y", "-v", "error"] + entradas +
       ["-filter_complex", ";".join(f), "-map", "[vout]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-t", f"{total:.2f}", str(SAIDA)])
subprocess.run(cmd, check=True)
print(f"pronto: {SAIDA.name} ({total:.1f}s)")
for (arq, q) in VOZ:
    print(f"  {arq} em {q:.1f}s")
