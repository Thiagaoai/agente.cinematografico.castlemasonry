#!/usr/bin/env python3
"""Gera a locução institucional dramática em voz masculina forte (pt-BR-AntonioNeural)."""
import asyncio
import subprocess
from pathlib import Path
import edge_tts

SAIDA = Path(__file__).parent / "saida"
VOZ_DIR = SAIDA / "voz"
VOZ_DIR.mkdir(parents=True, exist_ok=True)

# Frases sincronizadas com as 6 cenas do vídeo de 30s
FALAS = [
    ("f01.wav", "Cada obra de sucesso começa antes da primeira pedra."),
    ("f02.wav", "Um projeto executivo que antecipa desafios..."),
    ("f03.wav", "...e um orçamento com rigor técnico oficial, item por item."),
    ("f04.wav", "Acompanhamento técnico em campo para a sua obra não parar."),
    ("f05.wav", "Medição precisa do que foi realmente executado."),
    ("f06.wav", "A.F Consultoria em Engenharia. Do projeto à entrega final."),
]

async def sintetizar():
    for arq, texto in FALAS:
        mp3_temp = VOZ_DIR / f"{arq}.mp3"
        wav_final = VOZ_DIR / arq
        print(f"Gerando voz: {arq} -> '{texto}'")
        
        # Voz de locutor forte, tom mais grave (-4Hz) e ritmo firme e pausado (-3%)
        comunicador = edge_tts.Communicate(
            texto,
            voice="pt-BR-AntonioNeural",
            pitch="-4Hz",
            rate="-3%"
        )
        await comunicador.save(str(mp3_temp))
        
        # Converte para WAV estúdio com compressão de rádio/cinema (grave encorpado)
        cmd = [
            "ffmpeg", "-y", "-i", str(mp3_temp),
            "-af", "highpass=f=75,equalizer=f=120:width_type=o:width=1:g=3,acompressor=threshold=-16dB:ratio=4:attack=5:release=100,volume=1.8",
            "-ar", "44100", "-ac", "2",
            str(wav_final)
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        mp3_temp.unlink(missing_ok=True)
        print(f"  salvo: {wav_final.name}")

if __name__ == "__main__":
    asyncio.run(sintetizar())
