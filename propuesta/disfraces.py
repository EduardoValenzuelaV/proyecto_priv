"""Disfraces de Alejandro (vista previa para elegir).
Uso: python propuesta/disfraces.py salida.png
Reutiliza pose() de cangrejo.py y dibuja encima los accesorios de cada disfraz.
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont

# toma solo las definiciones del cangrejo (sin generar sus GIF)
_src = open(os.path.join(os.path.dirname(__file__), 'cangrejo.py'), encoding='utf-8').read()
exec(_src[:_src.index('def fondo(f):')])

OUT = sys.argv[1] if len(sys.argv) > 1 else 'disfraces.png'
CW, CH = 64, 72          # lienzo de cada disfraz
OX, OY = 10, 18          # dónde va el cangrejo dentro del lienzo
cx = 22 + OX
def P(x, y):             # coordenadas del cangrejo (pose) -> lienzo
    return (x + OX, y + OY)
Y = lambda v: v + T + OY  # misma Y() que usa pose(), ya desplazada

OSC = OUTL

def corazon(d, x, y, col, borde=OSC):
    forma = ["0110110", "1111111", "1111111", "0111110", "0011100", "0001000"]
    for r_, fila in enumerate(forma):
        for c, v in enumerate(fila):
            if v == '1':
                d.point((x + c, y + r_), fill=col)
    d.point((x + 1, y + 1), fill=(255, 220, 220))

def estrella(d, x, y, col):
    d.point([(x, y - 1), (x - 1, y), (x, y), (x + 1, y), (x, y + 1)], fill=col)

def capa(d, col, forro=None):
    d.polygon([(cx - 10, Y(18)), (cx + 10, Y(18)), (cx + 17, Y(37)), (cx - 17, Y(37))], fill=col, outline=OSC)
    if forro:
        d.line([(cx - 16, Y(36)), (cx + 16, Y(36))], fill=forro)

def base(ojos='abiertos', boca='feliz', gl=(16, 3), gr=(16, 3)):
    return pose(gl, gr, ojos, boca)

def lienzo():
    return Image.new('RGBA', (CW, CH), (0, 0, 0, 0))

def pegar(im, spr):
    im.alpha_composite(spr, (OX, OY))

def pijama_cuerpo(im):
    """Recolorea la parte de abajo del caparazón como un pijama a rayas."""
    p = im.load()
    for y in range(Y(26), Y(36)):
        for x in range(cx - 11, cx + 12):
            if p[x, y][:3] in (R, r, L):
                p[x, y] = ((236, 240, 252, 255) if (x // 2) % 2 else (120, 150, 220, 255))

# ---------------- disfraces ----------------
def mago():  # aprendiz de mago: lentes redondos, cicatriz, bufanda roja y dorada, varita
    im = lienzo(); d = ImageDraw.Draw(im)
    capa(d, (34, 32, 44), (150, 26, 36))
    pegar(im, base())
    d = ImageDraw.Draw(im)
    for ex in (cx - 4, cx + 4):
        d.ellipse([ex - 5, Y(-1), ex + 5, Y(10)], outline=(28, 24, 28), width=2)
    # cicatriz de rayo entre los ojos
    d.line([(cx + 1, Y(10)), (cx - 1, Y(12)), (cx + 1, Y(12)), (cx - 1, Y(14))], fill=(120, 16, 28))
    for x in range(cx - 10, cx + 11):
        col = (160, 24, 36) if ((x - cx) // 2) % 2 else (236, 186, 56)
        d.line([x, Y(24), x, Y(26)], fill=col)
    for yy in range(Y(26), Y(33)):
        col = (160, 24, 36) if ((yy) // 2) % 2 else (236, 186, 56)
        d.line([cx + 5, yy, cx + 8, yy], fill=col)
    d.line([(cx + 16, Y(5)), (cx + 22, Y(-6))], fill=(110, 72, 40), width=2)
    estrella(d, cx + 23, Y(-8), (255, 232, 120)); estrella(d, cx + 18, Y(-10), (255, 250, 200))
    return im

def hobbit():  # capa verde con broche de hoja, rulitos y el anillo dorado
    im = lienzo(); d = ImageDraw.Draw(im)
    capa(d, (64, 110, 60), (96, 150, 80))
    pegar(im, base())
    d = ImageDraw.Draw(im)
    for (hx, hy) in ((cx - 6, Y(-2)), (cx - 2, Y(-3)), (cx + 2, Y(-3)), (cx + 6, Y(-2))):
        d.ellipse([hx - 2, hy - 2, hx + 2, hy + 2], fill=(120, 74, 40), outline=(70, 40, 24))
        d.point((hx, hy), fill=(160, 104, 60))
    d.ellipse([cx - 3, Y(24), cx + 3, Y(28)], fill=(120, 180, 96), outline=(200, 210, 220))
    d.line([cx, Y(24) + 1, cx, Y(28) - 1], fill=(70, 120, 60))
    for k in range(3):
        d.point((cx, Y(30) + k * 2), fill=(236, 196, 80))
    rx, ry = cx - 16, Y(-3)
    for rr, a in ((7, 40), (5, 70)):
        d.ellipse([rx - rr, ry - rr, rx + rr, ry + rr], fill=(255, 230, 120, a))
    d.ellipse([rx - 3, ry - 3, rx + 3, ry + 3], outline=(242, 196, 50), width=2)
    d.point((rx - 2, ry - 2), fill=(255, 250, 200))
    return im

def mago_gris():  # el mago gris: sombrero puntiagudo, barba blanca y bastón
    im = lienzo(); d = ImageDraw.Draw(im)
    capa(d, (120, 122, 132), (90, 92, 104))
    d.line([(cx - 16, Y(-14)), (cx - 16, Y(39))], fill=(110, 72, 40), width=2)
    for rr, a in ((6, 50), (4, 110)):
        d.ellipse([cx - 16 - rr, Y(-15) - rr, cx - 16 + rr, Y(-15) + rr], fill=(255, 255, 240, a))
    d.ellipse([cx - 18, Y(-17), cx - 14, Y(-13)], fill=(255, 255, 250))
    pegar(im, base())
    d = ImageDraw.Draw(im)
    d.polygon([(cx - 9, Y(-1)), (cx + 9, Y(-1)), (cx + 7, Y(-14)), (cx + 2, Y(-21)), (cx - 2, Y(-12))], fill=(140, 142, 154), outline=OSC)
    d.line([(cx - 8, Y(-3)), (cx + 8, Y(-3))], fill=(96, 98, 110), width=2)
    d.ellipse([cx - 14, Y(-2), cx + 14, Y(1)], fill=(150, 152, 164), outline=OSC)
    d.polygon([(cx - 8, Y(21)), (cx + 8, Y(21)), (cx + 5, Y(30)), (cx, Y(36)), (cx - 5, Y(30))], fill=(238, 238, 242), outline=(170, 170, 180))
    for k in (-3, 0, 3):
        d.line([cx + k, Y(23), cx + k, Y(31) - abs(k)], fill=(206, 206, 216))
    d.rectangle([cx - 4, Y(19), cx + 4, Y(21)], fill=(238, 238, 242))
    return im

def caballero_espacial():  # túnica con capucha, cinturón y espada de luz
    im = lienzo(); d = ImageDraw.Draw(im)
    d.ellipse([cx - 13, Y(-4), cx + 13, Y(22)], fill=(122, 82, 50), outline=OSC)
    d.ellipse([cx - 10, Y(-2), cx + 10, Y(20)], fill=(70, 46, 30))
    capa(d, (122, 82, 50), (96, 62, 38))
    pegar(im, base())
    d = ImageDraw.Draw(im)
    d.line([(cx - 10, Y(27)), (cx + 10, Y(27))], fill=(92, 60, 36), width=2)
    d.rectangle([cx - 2, Y(26), cx + 2, Y(28)], fill=(200, 200, 210))
    bx, by = cx + 16, Y(4)
    d.line([(bx + 4, by - 3), (bx + 10, by - 28)], fill=(120, 200, 255), width=3)
    d.line([(bx + 4, by - 3), (bx + 10, by - 28)], fill=(235, 250, 255), width=1)
    d.line([(bx + 1, by + 7), (bx + 4, by - 3)], fill=(170, 172, 182), width=3)
    d.point((bx + 2, by + 3), fill=(40, 40, 44))
    return im

def san_valentin():  # alitas de cupido, cintillo con corazones y un corazón en la pinza
    im = lienzo(); d = ImageDraw.Draw(im)
    for sx in (-1, 1):
        x0 = cx + sx * 9
        d.ellipse([min(x0, x0 + sx * 13), Y(18), max(x0, x0 + sx * 13), Y(30)], fill=(252, 250, 255), outline=(190, 180, 210))
        for k in range(3):
            d.line([(x0 + sx * (4 + k * 3), Y(21)), (x0 + sx * (4 + k * 3), Y(28))], fill=(214, 208, 232))
    pegar(im, base())
    d = ImageDraw.Draw(im)
    d.arc([cx - 10, Y(-4), cx + 10, Y(6)], 190, 350, fill=(220, 40, 70), width=1)
    for (hx, tip) in ((cx - 7, -9), (cx + 7, -10)):
        d.line([(hx, Y(-2)), (hx + (2 if hx > cx else -2), Y(tip) + 5)], fill=(220, 40, 70))
        corazon(d, hx - 3 + (2 if hx > cx else -2), Y(tip), (230, 40, 70))
    for ex in (cx - 7, cx + 7):
        d.ellipse([ex - 2, Y(19), ex + 2, Y(21)], fill=(255, 150, 170))
    corazon(d, cx + 13, Y(4), (240, 50, 80))
    return im

def pijama():  # gorro de dormir, pijama a rayas y su osito
    im = lienzo(); d = ImageDraw.Draw(im)
    pegar(im, base('cerrados', 'dormido', gl=(15, 7)))
    pijama_cuerpo(im)
    d = ImageDraw.Draw(im)
    d.polygon([(cx - 9, Y(-1)), (cx + 9, Y(-1)), (cx + 8, Y(-7)), (cx + 14, Y(-9)), (cx + 18, Y(-4)), (cx + 4, Y(-12)), (cx - 6, Y(-8))], fill=(90, 120, 200), outline=OSC)
    for (sx_, sy_) in ((cx - 3, Y(-6)), (cx + 4, Y(-8)), (cx + 10, Y(-6))):
        d.point((sx_, sy_), fill=(255, 240, 150))
    d.rectangle([cx - 10, Y(-2), cx + 10, Y(0)], fill=(236, 240, 252), outline=OSC)
    d.ellipse([cx + 16, Y(-6), cx + 21, Y(-1)], fill=(255, 255, 255), outline=OSC)
    ox_, oy_ = cx - 21, Y(10)
    d.ellipse([ox_, oy_, ox_ + 8, oy_ + 8], fill=(170, 116, 70), outline=OSC)
    d.ellipse([ox_ + 1, oy_ - 6, ox_ + 7, oy_ + 1], fill=(170, 116, 70), outline=OSC)
    d.point([(ox_ + 1, oy_ - 6), (ox_ + 7, oy_ - 6)], fill=(170, 116, 70))
    d.point([(ox_ + 3, oy_ - 3), (ox_ + 5, oy_ - 3)], fill=(30, 20, 20))
    d.point((ox_ + 4, oy_ - 1), fill=(90, 50, 40))
    estrella(d, cx + 22, Y(-14), (255, 232, 120))
    return im

def navidad():  # gorro navideño, bufanda verde y bastón de dulce
    im = lienzo(); d = ImageDraw.Draw(im)
    pegar(im, base())
    d = ImageDraw.Draw(im)
    d.polygon([(cx - 10, Y(-1)), (cx + 10, Y(-1)), (cx + 6, Y(-10)), (cx + 15, Y(-6)), (cx - 2, Y(-14))], fill=(214, 40, 50), outline=OSC)
    d.rectangle([cx - 11, Y(-3), cx + 11, Y(0)], fill=(250, 250, 250), outline=OSC)
    d.ellipse([cx + 13, Y(-9), cx + 18, Y(-4)], fill=(255, 255, 255), outline=OSC)
    for x in range(cx - 10, cx + 11):
        d.line([x, Y(24), x, Y(26)], fill=(40, 140, 80) if ((x - cx) // 3) % 2 else (230, 240, 236))
    d.rectangle([cx - 8, Y(26), cx - 5, Y(32)], fill=(40, 140, 80))
    bx, by = cx + 16, Y(4)
    # bastón de dulce: palo a rayas con su curva arriba
    d.rectangle([bx + 3, by - 12, bx + 6, by + 2], fill=OSC)
    d.arc([bx + 2, by - 19, bx + 13, by - 8], 180, 360, fill=OSC, width=4)
    d.arc([bx + 3, by - 18, bx + 12, by - 9], 180, 360, fill=(255, 255, 255), width=2)
    for k in range(14):
        d.line([bx + 4, by + 1 - k, bx + 5, by + 1 - k], fill=(230, 40, 50) if (k // 2) % 2 else (255, 255, 255))
    for (x, y) in ((bx + 5, by - 17), (bx + 9, by - 17), (bx + 11, by - 14)):
        d.point([(x, y), (x + 1, y)], fill=(230, 40, 50))
    return im

def cumpleanos():  # gorro de fiesta, confeti y un pastelito con vela
    im = lienzo(); d = ImageDraw.Draw(im)
    pegar(im, base())
    d = ImageDraw.Draw(im)
    d.polygon([(cx - 7, Y(-1)), (cx + 7, Y(-1)), (cx + 2, Y(-15))], fill=(110, 170, 240), outline=OSC)
    for k in range(3):
        y0 = Y(-3) - k * 4
        d.line([(cx - 6 + k * 2, y0), (cx + 6 - k * 2, y0)], fill=(255, 220, 90))
    d.ellipse([cx, Y(-18), cx + 4, Y(-14)], fill=(255, 120, 160), outline=OSC)
    for (x, y, c) in ((cx - 20, Y(-10), (255, 120, 160)), (cx - 14, Y(-16), (120, 200, 120)), (cx + 12, Y(-14), (255, 200, 60)), (cx + 20, Y(-8), (110, 170, 240)), (cx - 24, Y(0), (255, 200, 60))):
        d.rectangle([x, y, x + 1, y + 1], fill=c)
    px_, py_ = cx + 12, Y(2)
    d.rectangle([px_, py_, px_ + 10, py_ + 6], fill=(250, 214, 170), outline=OSC)
    d.rectangle([px_ + 1, py_ + 1, px_ + 9, py_ + 2], fill=(255, 150, 190))
    d.line([px_ + 5, py_ - 4, px_ + 5, py_ - 1], fill=(110, 170, 240))
    d.point((px_ + 5, py_ - 5), fill=(255, 200, 60)); d.point((px_ + 5, py_ - 6), fill=(255, 120, 60))
    return im

DISFRACES = [
    ('1. Aprendiz de mago', mago),
    ('2. Hobbit con el anillo', hobbit),
    ('3. El mago gris', mago_gris),
    ('4. Caballero espacial', caballero_espacial),
    ('5. San Valentín', san_valentin),
    ('6. Pijama', pijama),
    ('7. Navidad', navidad),
    ('8. Cumpleaños', cumpleanos),
]

if __name__ == '__main__':
    E = 4
    cols = 4
    filas = (len(DISFRACES) + cols - 1) // cols
    celda_w, celda_h = CW * E, CH * E + 34
    hoja = Image.new('RGB', (celda_w * cols, celda_h * filas), (250, 242, 232))
    try:
        fuente = ImageFont.truetype('arialbd.ttf', 18)
    except OSError:
        fuente = ImageFont.load_default()
    dh = ImageDraw.Draw(hoja)
    for i, (nombre, fn) in enumerate(DISFRACES):
        x0, y0 = (i % cols) * celda_w, (i // cols) * celda_h
        dh.rectangle([x0 + 6, y0 + 6, x0 + celda_w - 6, y0 + celda_h - 6], fill=(255, 250, 244), outline=(226, 206, 196))
        im = fn()
        hoja.paste(im.resize((CW * E, CH * E), Image.NEAREST), (x0, y0 + 6), im.resize((CW * E, CH * E), Image.NEAREST))
        w = dh.textlength(nombre, font=fuente)
        dh.text((x0 + (celda_w - w) / 2, y0 + CH * E + 6), nombre, fill=(120, 30, 50), font=fuente)
    hoja.save(OUT)
    print('ok')
