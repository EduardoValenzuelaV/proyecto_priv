"""Íconos pixel de «Lo que admiro de ti» (Museo de ti): una «obra» de 32×32 por cualidad.
Uso: python propuesta/obras.py assets/pixel/obras.png [vista_previa.png]
Genera una tira horizontal (32×32 por obra) en el mismo orden que OBRAS; Dallana.js elige la obra por su id (`icono`).
"""
import sys, os, math
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from alejandro2 import contorno

T = 32
NEGRO = (40, 34, 46)
BLANCO = (252, 252, 250)
ORO = (244, 196, 64)
ORO_OSC = (196, 140, 40)
ROJO = (214, 52, 63)
ROJO_OSC = (165, 34, 46)
ROSA = (255, 150, 160)
MADERA = (130, 84, 48)
PLATA = (196, 204, 216)
PLATA_OSC = (140, 148, 164)


def lienzo():
    return Image.new('RGBA', (T, T), (0, 0, 0, 0))


def corazon(d, x, y, col, grande=False):
    forma = (["0110110", "1111111", "1111111", "0111110", "0011100", "0001000"] if grande
             else ["01010", "11111", "01110", "00100"])
    for rr, fila in enumerate(forma):
        for c, v in enumerate(fila):
            if v == '1':
                d.point((x + c, y + rr), fill=col)


def chispa(d, x, y, col=(255, 236, 140)):
    d.point([(x, y - 1), (x - 1, y), (x, y), (x + 1, y), (x, y + 1)], fill=col)


def con_contorno(dibujar, detalle=None):
    im = lienzo()
    dibujar(ImageDraw.Draw(im))
    im = contorno(im)
    if detalle:
        detalle(ImageDraw.Draw(im))
    return im


# ---------------- las obras ----------------
def geologa():
    """Geoda partida con cristales y martillo de geóloga."""
    def dib(d):
        d.ellipse([4, 9, 25, 28], fill=(150, 120, 100))
        d.ellipse([7, 12, 22, 25], fill=(120, 80, 170))
        d.polygon([(11, 23), (13, 14), (15, 23)], fill=(196, 160, 240))
        d.polygon([(15, 23), (18, 16), (20, 23)], fill=(170, 130, 225))
        d.polygon([(8, 22), (10, 17), (12, 22)], fill=(170, 130, 225))
        d.line([22, 27, 28, 9], fill=MADERA, width=2)
        d.rectangle([23, 5, 30, 9], fill=PLATA)
    def det(d):
        d.line([24, 6, 29, 6], fill=BLANCO)
        d.point([(12, 16), (17, 18), (9, 19)], fill=BLANCO)
        d.line([5, 15, 6, 13], fill=(184, 156, 134))
        chispa(d, 5, 5); chispa(d, 18, 4)
    return con_contorno(dib, det)


def sonrisa():
    """Un solcito que sonríe."""
    def dib(d):
        for k in range(8):
            a = k * math.pi / 4
            x, y = 16 + 12 * math.cos(a), 16 + 12 * math.sin(a)
            d.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(255, 176, 60))
        d.ellipse([7, 7, 25, 25], fill=(255, 214, 80))
    def det(d):
        d.rectangle([12, 13, 13, 15], fill=NEGRO); d.rectangle([19, 13, 20, 15], fill=NEGRO)
        d.point([(12, 13), (19, 13)], fill=BLANCO)
        d.arc([11, 15, 21, 22], 20, 160, fill=NEGRO)
        d.rectangle([9, 18, 10, 19], fill=ROSA); d.rectangle([22, 18, 23, 19], fill=ROSA)
        d.line([10, 9, 12, 8], fill=(255, 240, 170))
    return con_contorno(dib, det)


def gustos():
    """Nigiri de salmón y un trocito de pizza."""
    def dib(d):
        d.rounded_rectangle([3, 18, 17, 25], radius=3, fill=BLANCO)
        d.rounded_rectangle([2, 14, 18, 19], radius=3, fill=(255, 140, 90))
        d.rectangle([9, 13, 11, 25], fill=(40, 70, 50))
        d.polygon([(18, 6), (30, 10), (21, 28)], fill=(244, 196, 100))
        d.polygon([(18, 6), (30, 10), (29, 13), (17, 9)], fill=(200, 130, 60))
    def det(d):
        d.line([4, 16, 16, 16], fill=(255, 196, 160))
        for (x, y) in ((22, 13), (25, 16), (22, 19)):
            d.ellipse([x - 1, y - 1, x + 1, y + 1], fill=ROJO)
        d.point([(24, 12), (21, 16)], fill=(90, 160, 70))
    return con_contorno(dib, det)


def paseos():
    """Caminito que serpentea con un arbolito y un pin de corazón."""
    def dib(d):
        d.rounded_rectangle([2, 20, 29, 29], radius=3, fill=(130, 200, 110))
        d.polygon([(6, 29), (12, 29), (18, 24), (24, 21), (20, 21), (14, 23)], fill=(240, 220, 170))
        d.rectangle([7, 15, 8, 22], fill=MADERA)
        d.ellipse([3, 6, 13, 16], fill=(80, 160, 80))
        d.ellipse([20, 3, 28, 11], fill=ROJO)
        d.polygon([(21, 9), (27, 9), (24, 16)], fill=ROJO)
    def det(d):
        d.ellipse([22, 5, 26, 9], fill=BLANCO)
        corazon(d, 22, 6, ROJO)
        d.point([(6, 9), (9, 8)], fill=(150, 210, 140))
        d.point([(15, 26), (21, 23)], fill=(210, 186, 130))
    return con_contorno(dib, det)


def voz():
    """Micrófono con notitas musicales."""
    def dib(d):
        d.rounded_rectangle([9, 4, 19, 17], radius=5, fill=PLATA)
        d.rectangle([9, 14, 19, 16], fill=ROJO)
        d.rectangle([13, 17, 15, 25], fill=PLATA_OSC)
        d.rounded_rectangle([8, 25, 20, 28], radius=1, fill=PLATA_OSC)
        d.ellipse([22, 13, 26, 17], fill=(60, 110, 200)); d.rectangle([25, 5, 26, 15], fill=(60, 110, 200))
        d.rectangle([25, 5, 29, 6], fill=(60, 110, 200))
    def det(d):
        for y in range(6, 13, 2):
            d.line([10, y, 18, y], fill=PLATA_OSC)
        d.line([11, 5, 11, 12], fill=BLANCO)
        d.ellipse([2, 6, 5, 9], fill=ROJO); d.line([5, 2, 5, 7], fill=ROJO)
        chispa(d, 4, 16)
    return con_contorno(dib, det)


def cuidar():
    """Tacita calentita con vapor en forma de corazón."""
    def dib(d):
        d.rounded_rectangle([5, 15, 22, 27], radius=4, fill=(130, 180, 240))
        d.ellipse([19, 17, 27, 25], fill=(130, 180, 240))
        d.ellipse([21, 19, 25, 23], fill=(0, 0, 0, 0))
        d.rounded_rectangle([2, 26, 25, 29], radius=2, fill=BLANCO)
    def det(d):
        d.line([7, 16, 20, 16], fill=(180, 120, 70))
        corazon(d, 10, 20, BLANCO)
        corazon(d, 9, 3, ROJO, True)
        d.point([(13, 11), (14, 12), (13, 13)], fill=(220, 220, 230))
        d.line([8, 18, 8, 24], fill=(170, 210, 250))
    return con_contorno(dib, det)


def caracter():
    """Escudo valiente con una estrella."""
    def dib(d):
        d.polygon([(16, 3), (27, 7), (26, 18), (16, 29), (6, 18), (5, 7)], fill=ROJO)
        d.polygon([(16, 6), (24, 9), (23, 17), (16, 25), (9, 17), (8, 9)], fill=(255, 226, 120))
    def det(d):
        pts = []
        for k in range(10):
            a = -math.pi / 2 + k * math.pi / 5
            rr = 6 if k % 2 == 0 else 2.6
            pts.append((16 + rr * math.cos(a), 15 + rr * math.sin(a)))
        d.polygon(pts, fill=ROJO)
        d.line([7, 8, 7, 15], fill=(240, 110, 110))
        chispa(d, 28, 3); chispa(d, 3, 25)
    return con_contorno(dib, det)


def divertida():
    """Carita muerta de la risa con confeti."""
    def dib(d):
        d.ellipse([5, 6, 27, 28], fill=(255, 214, 80))
    def det(d):
        d.line([10, 13, 13, 15], fill=NEGRO); d.line([10, 17, 13, 15], fill=NEGRO)
        d.line([22, 13, 19, 15], fill=NEGRO); d.line([22, 17, 19, 15], fill=NEGRO)
        d.chord([10, 15, 22, 26], 0, 180, fill=ROJO_OSC)
        d.rectangle([12, 21, 20, 21], fill=BLANCO)
        d.point([(8, 18), (8, 19), (24, 18), (24, 19)], fill=(110, 190, 250))
        for (x, y, c) in ((3, 4, (60, 110, 200)), (28, 5, ROJO), (2, 26, (80, 160, 80)), (29, 24, (200, 110, 220)), (16, 2, ROJO)):
            d.rectangle([x, y, x + 1, y + 1], fill=c)
    return con_contorno(dib, det)


def estilo():
    """Vestidito en su perchero."""
    def dib(d):
        d.line([16, 2, 16, 5], fill=PLATA_OSC)
        d.line([7, 9, 16, 5, 25, 9], fill=PLATA_OSC, width=2)
        d.polygon([(11, 8), (21, 8), (19, 15), (25, 28), (7, 28), (13, 15)], fill=(236, 80, 120))
        d.rectangle([12, 14, 20, 16], fill=(255, 210, 220))
    def det(d):
        d.arc([14, 0, 18, 4], 180, 360, fill=PLATA_OSC)
        for (x, y) in ((13, 21), (18, 24), (16, 19), (11, 25), (21, 22)):
            d.point((x, y), fill=(255, 190, 210))
        corazon(d, 14, 9, BLANCO)
        chispa(d, 4, 18); chispa(d, 28, 15)
    return con_contorno(dib, det)


def ojitos():
    """Ojo con pestañas largas y brillo de estrellas."""
    def dib(d):
        d.ellipse([3, 9, 29, 24], fill=BLANCO)
        d.ellipse([10, 9, 22, 24], fill=(120, 76, 50))
        d.ellipse([13, 12, 19, 21], fill=NEGRO)
    def det(d):
        d.rectangle([13, 12, 15, 14], fill=BLANCO); d.point((18, 19), fill=BLANCO)
        for (x0, y0, x1, y1) in ((6, 10, 4, 6), (11, 8, 10, 4), (16, 7, 16, 3), (21, 8, 22, 4), (26, 10, 28, 6)):
            d.line([x0, y0, x1, y1], fill=NEGRO)
        corazon(d, 25, 25, ROJO)
        chispa(d, 4, 27)
    return con_contorno(dib, det)


def cocinera():
    """Sartén con huevito en forma de corazón."""
    def dib(d):
        d.ellipse([2, 10, 22, 28], fill=(70, 66, 80))
        d.line([20, 18, 30, 12], fill=MADERA, width=3)
        d.ellipse([5, 13, 19, 25], fill=(110, 104, 120))
    def det(d):
        corazon(d, 8, 15, BLANCO, True)
        d.ellipse([10, 17, 13, 20], fill=(255, 196, 40))
        d.point((10, 17), fill=(255, 236, 160))
        for k in range(3):
            d.point((7 + k * 4, 6 - (k % 2)), fill=(220, 220, 230))
            d.point((8 + k * 4, 4 - (k % 2)), fill=(220, 220, 230))
        d.arc([5, 12, 19, 26], 200, 260, fill=(150, 146, 160))
    return con_contorno(dib, det)


OBRAS = [('geologa', geologa), ('sonrisa', sonrisa), ('gustos', gustos), ('paseos', paseos), ('voz', voz),
         ('cuidar', cuidar), ('caracter', caracter), ('divertida', divertida), ('estilo', estilo),
         ('ojitos', ojitos), ('cocinera', cocinera)]

if __name__ == '__main__':
    salida = sys.argv[1] if len(sys.argv) > 1 else 'obras.png'
    tira = Image.new('RGBA', (T * len(OBRAS), T), (0, 0, 0, 0))
    for i, (_, fn) in enumerate(OBRAS):
        tira.alpha_composite(fn(), (i * T, 0))
    tira.save(salida, optimize=True)
    print('obras:', ', '.join(n for n, _ in OBRAS))
    if len(sys.argv) > 2:
        E = 8
        prev = Image.new('RGB', (tira.width * E + 12 * len(OBRAS), T * E + 12), (240, 236, 226))
        for i in range(len(OBRAS)):
            im = tira.crop((i * T, 0, i * T + T, T)).resize((T * E, T * E), Image.NEAREST)
            prev.paste(im, (6 + i * (T * E + 12), 6), im)
        prev.save(sys.argv[2])
