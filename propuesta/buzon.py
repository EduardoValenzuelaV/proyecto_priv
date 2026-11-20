"""Buzón pixel para la sección «Buzón de papá».
Uso: python propuesta/buzon.py assets/pixel/buzon.png
Genera una tira de 2 cuadros de 48x44: 0 = sin cartas (bandera abajo), 1 = con carta (bandera arriba y sobre asomando).
"""
import sys, os
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from alejandro2 import contorno

OUT = sys.argv[1] if len(sys.argv) > 1 else 'buzon.png'
W, H = 48, 44
ROJO, ROJO_OSC, ROJO_CLARO = (214, 58, 70), (170, 36, 52), (246, 118, 120)
MADERA, MADERA_OSC = (150, 100, 62), (112, 72, 42)
ORO = (244, 196, 64)
BLANCO = (255, 252, 246)

def buzon(con_carta):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    # poste
    d.rectangle([21, 29, 26, 42], fill=MADERA)
    d.line([25, 30, 25, 42], fill=MADERA_OSC)
    d.rectangle([17, 41, 30, 42], fill=MADERA_OSC)
    # cuerpo con techo redondo
    d.rectangle([6, 14, 40, 30], fill=ROJO)
    d.ellipse([6, 5, 40, 23], fill=ROJO)
    d.rectangle([6, 27, 40, 30], fill=ROJO_OSC)
    d.arc([9, 7, 37, 21], 200, 320, fill=ROJO_CLARO)
    # corazón al costado
    for (x, y) in ((22, 17), (23, 16), (25, 16), (26, 17), (22, 18), (23, 18), (24, 18), (25, 18), (26, 18), (23, 19), (24, 19), (25, 19), (24, 20), (24, 17)):
        d.point((x, y), fill=BLANCO)
    # puerta (al frente, a la izquierda)
    d.rounded_rectangle([3, 9, 9, 30], radius=3, fill=ROJO_CLARO)
    d.line([5, 12, 5, 27], fill=(255, 160, 158))
    d.rectangle([8, 18, 10, 20], fill=ORO)
    if con_carta:
        # sobre asomando por la puerta, con corazoncito
        d.rectangle([0, 13, 10, 20], fill=BLANCO)
        d.line([0, 13, 5, 17, 10, 13], fill=(226, 200, 196))
        d.point([(3, 17), (5, 17), (2, 18), (3, 18), (4, 18), (5, 18), (6, 18), (3, 19), (4, 19), (5, 19), (4, 20)], fill=(220, 40, 70))
        # bandera arriba
        d.rectangle([41, 4, 42, 24], fill=(120, 120, 130))
        d.rectangle([43, 4, 47, 10], fill=ORO)
        d.line([43, 10, 47, 10], fill=(200, 150, 40))
    else:
        # bandera abajo
        d.rectangle([41, 16, 42, 25], fill=(120, 120, 130))
        d.rectangle([41, 24, 47, 25], fill=(120, 120, 130))
        d.rectangle([43, 25, 47, 29], fill=ORO)
    im = contorno(im)
    sombra = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sombra).ellipse([12, 41, 35, 43], fill=(0, 0, 0, 50))
    sombra.alpha_composite(im)
    return sombra

tira = Image.new('RGBA', (W * 2, H), (0, 0, 0, 0))
tira.alpha_composite(buzon(False), (0, 0))
tira.alpha_composite(buzon(True), (W, 0))
tira.save(OUT, optimize=True)
print('ok')
