"""Adornitos pixel para el reverso de las obras del Museo de ti (14×14 cada uno, con contorno).
Uso: python propuesta/adornos.py assets/pixel/adornos.png [vista_previa.png]
Orden de la tira: corazón, estrella, flor, chispa, nota, nube, gema, hongo, cangrejito, sobre.
"""
import sys, os
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from alejandro2 import contorno

T = 14
ROJO, ROSA, ORO, AZUL, VERDE, LILA, BLANCO = (214, 52, 63), (255, 150, 170), (247, 200, 70), (90, 140, 220), (90, 170, 90), (180, 140, 230), (252, 252, 250)


def grilla(filas, paleta):
    im = Image.new('RGBA', (T, T), (0, 0, 0, 0))
    p = im.load()
    oy = (T - len(filas)) // 2
    for y, fila in enumerate(filas):
        ox = (T - len(fila)) // 2
        for x, c in enumerate(fila):
            if c in paleta:
                p[ox + x, oy + y] = paleta[c] + (255,)
    return contorno(im)


ADORNOS = [
    (["0110110", "1211111", "1111111", "0111110", "0011100", "0001000"], {'1': ROJO, '2': ROSA}),
    (["0001000", "0011100", "1111111", "0111110", "0110110", "0100010"], {'1': ORO}),
    (["0110110", "1111111", "0112110", "1111111", "0110110", "0003000", "0033000"], {'1': ROSA, '2': ORO, '3': VERDE}),
    (["00100", "00100", "11211", "00100", "00100"], {'1': ORO, '2': BLANCO}),
    (["0001111", "0001001", "0001001", "0111011", "1111111", "0110110"], {'1': AZUL}),
    (["00111000", "01222100", "12222210", "12222221", "01111110"], {'1': (190, 210, 240), '2': BLANCO}),
    (["0111110", "1222221", "0122210", "0012100", "0001000"], {'1': (120, 80, 190), '2': LILA}),
    (["0111110", "1121211", "1111111", "0033300", "0033300"], {'1': ROJO, '2': BLANCO, '3': (250, 230, 200)}),
    (["1000001", "1100011", "0111110", "1212121", "0111110", "1010101"], {'1': (240, 90, 80), '2': BLANCO}),
    (["11111111", "12000021", "10200201", "10022001", "11111111"], {'1': (240, 200, 160), '2': ROJO, '0': (255, 244, 230)}),
]

if __name__ == '__main__':
    salida = sys.argv[1] if len(sys.argv) > 1 else 'adornos.png'
    tira = Image.new('RGBA', (T * len(ADORNOS), T), (0, 0, 0, 0))
    for i, (filas, pal) in enumerate(ADORNOS):
        tira.alpha_composite(grilla(filas, pal), (i * T, 0))
    tira.save(salida, optimize=True)
    if len(sys.argv) > 2:
        tira.resize((tira.width * 10, T * 10), Image.NEAREST).save(sys.argv[2])
    print('adornos:', len(ADORNOS))
