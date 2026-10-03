#!/usr/bin/env python3
"""Gera o encerramento institucional transparente para a A.F Consultoria."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SAIDA = Path(__file__).parent / "saida" / "encerramento_af.png"
W, H = 1920, 1080

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Cores oficiais da A.F Consultoria
COBRE = (182, 114, 45, 255)       # #b6722d
AREIA = (244, 236, 227, 255)      # #f4ece3
AREIA_SUAVE = (244, 236, 227, 210)
LINHA = (221, 210, 198, 180)

# Card elegante centralizado / terço superior
card_w, card_h = 920, 340
cx, cy = W // 2, H // 2 - 40
x0 = cx - card_w // 2
y0 = cy - card_h // 2
x1 = cx + card_w // 2
y1 = cy + card_h // 2

# Fundo translúcido refinado (vidro escurecido cinematográfico)
draw.rounded_rectangle([x0, y0, x1, y1], radius=16, fill=(36, 26, 18, 190), outline=COBRE, width=2)

# Linha de destaque em cobre
draw.line([x0 + 40, y0 + 130, x1 - 40, y0 + 130], fill=COBRE, width=2)

# Textos institucionais
try:
    font_titulo = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 44)
    font_sub = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 22)
    font_tagline = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 26)
    font_contato = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", 20)
except Exception:
    font_titulo = font_sub = font_tagline = font_contato = ImageFont.load_default()

# Desenhar textos centralizados
draw.text((cx, y0 + 40), "A.F  C O N S U L T O R I A", font=font_titulo, fill=AREIA, anchor="mm")
draw.text((cx, y0 + 95), "ASSESSORIA EM ENGENHARIA", font=font_sub, fill=COBRE, anchor="mm")
draw.text((cx, y0 + 195), "Antes de construir, enxergue o que vem pela frente.", font=font_tagline, fill=AREIA, anchor="mm")
draw.text((cx, y0 + 265), "araujoferrazconsultoria.com.br  ·  Goiânia - GO  ·  (62) 99338-0808", font=font_contato, fill=AREIA_SUAVE, anchor="mm")

img.save(SAIDA, "PNG")
print(f"Salvo: {SAIDA}")
