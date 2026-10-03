#!/usr/bin/env python3
"""Monta a versão vertical a partir de voz transcrita e cenas verificadas."""
import json
import subprocess
from fractions import Fraction
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
BRAND = ROOT.parents[1] / 'marca'
OUT = ROOT / 'entrega'
OUT.mkdir(exist_ok=True)
W, H, TOTAL, VOICE_OFFSET = 1080, 1920, 30.0, 0.35
FONT = BRAND / 'archivo.ttf'


def probe(path):
    return json.loads(subprocess.check_output([
        'ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(path)
    ]))


def centered(draw, text, y, size, color, max_width=850):
    font = ImageFont.truetype(str(FONT), size)
    while draw.textbbox((0, 0), text, font=font)[2] > max_width:
        size -= 1
        if size < 24:
            raise ValueError('Texto excede a largura segura: ' + text)
        font = ImageFont.truetype(str(FONT), size)
    draw.text((W / 2, y), text, font=font, fill=color, anchor='mm')


def time_ass(seconds):
    centiseconds = round(seconds * 100)
    hours, rem = divmod(centiseconds, 360000)
    minutes, rem = divmod(rem, 6000)
    sec, cs = divmod(rem, 100)
    return f'{hours}:{minutes:02d}:{sec:02d}.{cs:02d}'


def time_srt(seconds):
    ms = round(seconds * 1000)
    hours, rem = divmod(ms, 3600000)
    minutes, rem = divmod(rem, 60000)
    sec, mil = divmod(rem, 1000)
    return f'{hours:02d}:{minutes:02d}:{sec:02d},{mil:03d}'


def main():
    scenes = [ROOT / 'cenas' / f'cena{i}.mp4' for i in (1, 2, 3)]
    voice = ROOT / 'audio' / 'locucao.mp3'
    for file in scenes + [voice, FONT, BRAND / 'logo-cobre.png']:
        if not file.is_file():
            raise FileNotFoundError(file)
    measurements = [probe(file) for file in scenes]
    frame_rates = [next(s['r_frame_rate'] for s in d['streams'] if s['codec_type'] == 'video') for d in measurements]
    fps = Fraction(frame_rates[0])
    if fps <= 0 or fps > 60:
        raise ValueError('Taxa de quadros inválida')
    for d in measurements:
        if float(d['format']['duration']) < 7.95:
            raise ValueError('Cena curta demais para a montagem')
    voice_duration = float(probe(voice)['format']['duration'])
    if voice_duration + VOICE_OFFSET > 24:
        raise ValueError('Reescrever locução: excede a janela de fala')

    # Encerramento com ativo oficial; não recriar o símbolo da marca.
    card = Image.new('RGB', (W, H), '#f4ece3')
    draw = ImageDraw.Draw(card)
    logo = Image.open(BRAND / 'logo-cobre.png').convert('RGBA')
    logo.thumbnail((850, 250), Image.Resampling.LANCZOS)
    card.paste(logo, ((W-logo.width)//2, 555), logo)
    centered(draw, 'Clareza para decidir.', 850, 53, '#241a12')
    draw.line((230, 960, 850, 960), fill='#b6722d', width=3)
    centered(draw, 'Vamos avaliar os', 1085, 58, '#241a12')
    centered(draw, 'próximos passos?', 1160, 58, '#241a12')
    centered(draw, 'CONVERSE PELO WHATSAPP', 1350, 32, '#754414')
    centered(draw, '(62) 99338-0808', 1420, 56, '#241a12')
    centered(draw, 'araujoferrazconsultoria.com.br', 1540, 33, '#754414')
    card_path = OUT / 'encerramento.png'
    card.save(card_path)

    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    # Fundo discreto para assegurar leitura do título sobre o céu.
    for y in range(500):
        od.line((0, y, W, y), fill=(20, 18, 16, round(125 * (1-y/500))))
    centered(od, 'SUA OBRA PAROU.', 245, 69, '#ffffff')
    centered(od, 'POR ONDE COMEÇAR?', 335, 60, '#ffffff')
    overlay_path = OUT / 'abertura.png'
    overlay.save(overlay_path)

    segments = json.loads((ROOT / 'audio' / 'transcricao.json').read_text())
    authored = ('Sua obra parou. Por onde começar? Primeiro, é preciso entender o que já foi feito e o que ainda falta. '
                'A AF confere a obra em campo, compara os serviços com o projeto e organiza o orçamento das etapas restantes. '
                'Assim, você tem informação técnica para avaliar os próximos passos. Converse com a AF sobre a sua obra.')
    import re
    normalize = lambda s: re.sub(r'[^a-z0-9áéíóúâêôãõç]', '', s.lower())
    if normalize(' '.join(s['text'] for s in segments)) != normalize(authored):
        raise ValueError('A transcrição não confere com o texto aprovado para produção')
    chunks = []
    for segment in segments:
        pending = []
        for word in segment['words']:
            if pending and (len(pending) >= 5 or len(' '.join(w['word'].strip() for w in pending + [word])) > 34):
                chunks.append(pending)
                pending = []
            pending.append(word)
            if word['word'].strip().endswith(('.', '?', '!')):
                chunks.append(pending)
                pending = []
        if pending:
            chunks.append(pending)
    header = '''[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Archivo,52,&H00FFFFFF,&H00FFFFFF,&H001A1224,&H80000000,-1,0,0,0,100,100,0,0,1,3,1,2,115,155,445,1
Style: Notice,Archivo,25,&H00FFFFFF,&H00FFFFFF,&H001A1224,&H80000000,0,0,0,0,100,100,0,0,1,2,0,1,90,120,325,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
    events, srt = [], []
    caption_times = []
    previous_end = 0.0
    for i, group in enumerate(chunks, 1):
        start = group[0]['start'] + VOICE_OFFSET
        end = group[-1]['end'] + VOICE_OFFSET
        if start < previous_end - .01 or end <= start:
            raise ValueError('Tempos de legendas inválidos')
        text = ' '.join(w['word'].strip() for w in group).replace('AF', 'A.F')
        events.append(f'Dialogue: 0,{time_ass(start)},{time_ass(end)},Default,,0,0,0,,{text}')
        srt.append(f'{i}\n{time_srt(start)} --> {time_srt(end)}\n{text}\n')
        caption_times.append((start, end, text))
        previous_end = end
    events.append('Dialogue: 0,0:00:00.00,0:00:23.00,Notice,,0,0,0,,Cenas ilustrativas')
    ass = OUT / 'legendas.ass'
    ass.write_text(header + '\n'.join(events) + '\n')
    (OUT / 'legendas.srt').write_text('\n'.join(srt))

    # Legendas rasterizadas preservam a tipografia mesmo sem libass no FFmpeg.
    fps_float = float(fps)
    boundaries = sorted({0, round(TOTAL*fps_float), round(23*fps_float)} |
                        {round(t*fps_float) for a,b,_ in caption_times for t in (a,b)})
    caption_dir = OUT / 'caption_frames'
    caption_dir.mkdir(exist_ok=True)
    concat_lines = []
    for j,(first,last) in enumerate(zip(boundaries,boundaries[1:])):
        canvas = Image.new('RGBA',(W,H),(0,0,0,0))
        cd = ImageDraw.Draw(canvas)
        midpoint = (first+last)/2/fps_float
        for a,b,words in caption_times:
            if a <= midpoint < b:
                font = ImageFont.truetype(str(FONT),52)
                cd.text((W/2,1450),words,font=font,fill='white',stroke_width=3,
                        stroke_fill='#24121a',anchor='mm')
        if midpoint < 23:
            cd.text((90,1590),'Cenas ilustrativas',font=ImageFont.truetype(str(FONT),25),
                    fill='white',stroke_width=2,stroke_fill='#24121a')
        frame = caption_dir / f'{j:03d}.png'
        canvas.save(frame)
        concat_lines += [f"file '{frame}'",f'duration {(last-first)/fps_float:.9f}']
    concat_lines.append(f"file '{frame}'")
    concat_path = OUT / 'captions.concat'
    concat_path.write_text('\n'.join(concat_lines)+'\n')
    captions_movie = OUT / 'captions.mov'
    subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',str(concat_path),
                    '-vf',f'fps={fps}','-t',str(TOTAL),'-c:v','qtrle','-pix_fmt','argb',
                    str(captions_movie)],check=True)

    # Cortes associados às unidades de sentido da locução medida.
    # Não há fades que reduzam a duração nem alteração de velocidade da voz.
    cuts = [(0, 0, 7), (1, 0, 4), (2, 0, 6), (1, 4, 4), (2, 6, 2)]
    filters = []
    filters += ['[1:v]split=2[s2a][s2b]', '[2:v]split=2[s3a][s3b]']
    sources = ['0:v', 's2a', 's3a', 's2b', 's3b']
    for i, ((_, start, duration), source) in enumerate(zip(cuts, sources)):
        filters.append(f'[{source}]trim=start={start}:duration={duration},setpts=PTS-STARTPTS,'
                       f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},'
                       f'fps={fps},setsar=1,format=yuv420p[c{i}]')
    filters.append(f'[3:v]trim=duration=7,setpts=PTS-STARTPTS,fps={fps},setsar=1,format=yuv420p[c5]')
    filters.append(''.join(f'[c{i}]' for i in range(6)) + 'concat=n=6:v=1:a=0[base]')
    filters.append('[base][4:v]overlay=0:0:enable=between(t\\,0\\,3.2)[title]')
    filters.append("[title][6:v]overlay=0:0,fade=t=out:st=29.7:d=0.3[vout]")
    filters.append(f'[5:a]adelay={int(VOICE_OFFSET*1000)}:all=1,apad,atrim=duration={TOTAL},'
                   'loudnorm=I=-16:TP=-1.5:LRA=9,aresample=48000[aout]')
    target = OUT / 'af-obra-parada-vertical-v01.mp4'
    args = ['ffmpeg', '-y', '-hide_banner', '-loglevel', 'error']
    for file in scenes:
        args += ['-i', str(file)]
    args += ['-loop', '1', '-i', str(card_path), '-loop', '1', '-i', str(overlay_path), '-i', str(voice), '-i', str(captions_movie)]
    args += ['-filter_complex', ';'.join(filters), '-map', '[vout]', '-map', '[aout]',
             '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p',
             '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-t', str(TOTAL), str(target)]
    subprocess.run(args, check=True)
    final = probe(target)
    actual = float(final['format']['duration'])
    if abs(actual - TOTAL) > 1/float(fps) + .01:
        raise ValueError(f'Duração final incorreta: {actual}')
    subprocess.run(['ffmpeg', '-v', 'error', '-i', str(target), '-f', 'null', '-'], check=True)
    (OUT / 'verificacao.json').write_text(json.dumps({
        'duration': actual, 'voice_duration': voice_duration, 'voice_offset': VOICE_OFFSET,
        'fps': str(fps), 'source_frame_rates': frame_rates, 'width': W, 'height': H,
        'transcript_matches': True, 'full_decode': True, 'caption_count': len(chunks),
        'human_listening': 'pending: audio input unavailable to this agent',
    }, indent=2))
    print(target)


if __name__ == '__main__':
    main()
