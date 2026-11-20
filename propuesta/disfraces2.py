"""Disfraces de Alejandro 2.0 (vista previa para elegir).
Uso: python propuesta/disfraces2.py carpeta_salida
Genera una imagen por categoría: disfraces_<categoria>.png
Cada disfraz se arma en capas: lo de atrás (capas, alas), Alejandro, y lo de adelante (gorros, objetos),
con contorno automático para que todo tenga el mismo estilo pixel.
"""
import sys, os, math
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import alejandro2 as A
from alejandro2 import pose, R, r, RR, L, BRI, BELLY, OUTL, EYE, BL, BLUSH, BOCA, T

CW, CH, OX, OY = 72, 86, 14, 26
cx = 22 + OX
def y(v):
    return v + T + OY

NEGRO = (40, 34, 46)
BLANCO = (252, 252, 250)
ORO = (244, 196, 64)
ORO_OSC = (196, 140, 40)
PLATA = (196, 204, 216)
PLATA_OSC = (140, 148, 164)
MADERA = (130, 84, 48)

def lienzo():
    return Image.new('RGBA', (CW, CH), (0, 0, 0, 0))

def armar(atras=None, adelante=None, detalle=None, tenir=None, ojos_encima=True, **kw):
    im = lienzo()
    if atras:
        capa_ = lienzo(); atras(ImageDraw.Draw(capa_)); im.alpha_composite(A.contorno(capa_))
    cang = pose(**kw)
    im.alpha_composite(cang, (OX, OY))
    if tenir:
        tenir(im)
    if adelante:
        capa_ = lienzo(); adelante(ImageDraw.Draw(capa_)); im.alpha_composite(A.contorno(capa_))
        if ojos_encima:
            # los ojitos quedan delante del gorro (están en sus tallos, más adelante)
            ojos = im.crop((cx - 11, y(-1), cx + 12, y(11)))
            limpio = lienzo(); limpio.alpha_composite(cang, (OX, OY))
            if tenir:
                tenir(limpio)
            ojos = limpio.crop((cx - 11, y(-1), cx + 12, y(11)))
            im.alpha_composite(ojos, (cx - 11, y(-1)))
    if detalle:
        detalle(ImageDraw.Draw(im))
    return im

# ---------------- ayudantes de dibujo ----------------
def teñir(im, mapa, y0=0, y1=CH, x0=0, x1=CW):
    p = im.load()
    for yy in range(max(0, y0), min(CH, y1)):
        for xx in range(max(0, x0), min(CW, x1)):
            c = p[xx, yy]
            if c[3] and c[:3] in mapa:
                p[xx, yy] = mapa[c[:3]] + (255,)

def tono(col, k):
    return tuple(max(0, min(255, int(v * k))) for v in col)

def cuerpo_color(col, panza=None, patas=None):
    mapa = {R: col, r: tono(col, .82), L: tono(col, 1.18), BRI: tono(col, 1.35)}
    if panza: mapa[BELLY] = panza; mapa[(236, 170, 150)] = tono(panza, .85)
    if patas: mapa[RR] = patas
    return lambda im: teñir(im, mapa)

def capa(d, col, forro=None, ancho=19, alto=38):
    d.polygon([(cx - 14, y(13)), (cx + 14, y(13)), (cx + ancho + 1, y(alto)), (cx - ancho - 1, y(alto))], fill=col)
    d.ellipse([cx - 16, y(11), cx + 16, y(19)], fill=col)
    if forro:
        d.polygon([(cx - ancho + 3, y(alto - 2)), (cx + ancho - 3, y(alto - 2)), (cx + ancho, y(alto)), (cx - ancho, y(alto))], fill=forro)

def bufanda(d, c1, c2, cola=True):
    for xx in range(cx - 13, cx + 14):
        d.line([xx, y(24), xx, y(26)], fill=c1 if ((xx - cx) // 2) % 2 else c2)
    if cola:
        for yy in range(y(26), y(34)):
            d.line([cx + 5, yy, cx + 8, yy], fill=c1 if (yy // 2) % 2 else c2)

def estrella5(d, x, yy, rad, col):
    pts = []
    for k in range(10):
        a = -math.pi / 2 + k * math.pi / 5
        rr = rad if k % 2 == 0 else rad * .45
        pts.append((x + rr * math.cos(a), yy + rr * math.sin(a)))
    d.polygon(pts, fill=col)

def corazon(d, x, yy, col, grande=False):
    forma = (["0110110", "1111111", "1111111", "0111110", "0011100", "0001000"] if grande
             else ["01010", "11111", "01110", "00100"])
    for rr, fila in enumerate(forma):
        for c, v in enumerate(fila):
            if v == '1':
                d.point((x + c, yy + rr), fill=col)

def chispa(d, x, yy, col=(255, 236, 140)):
    d.point([(x, yy - 1), (x - 1, yy), (x, yy), (x + 1, yy), (x, yy + 1)], fill=col)

def rayo(d, x, yy, col, e=1):
    d.polygon([(x + 2 * e, yy), (x - 1 * e, yy + 4 * e), (x + 1 * e, yy + 4 * e), (x - 2 * e, yy + 9 * e), (x + 3 * e, yy + 3 * e), (x + 1 * e, yy + 3 * e), (x + 3 * e, yy)], fill=col)

def gorro_cono(d, col, banda, alto=14, caida=6, pompon=None, ancho=10):
    """Gorro puntudo que se dobla hacia un lado (mago, navidad, dormir)."""
    d.polygon([(cx - ancho, y(0)), (cx + ancho, y(0)), (cx + 5, y(-alto + 4)), (cx + 5 + caida, y(-alto + 2 + caida // 2)), (cx - 1, y(-alto))], fill=col)
    if banda:
        d.rectangle([cx - ancho - 1, y(-2), cx + ancho + 1, y(1)], fill=banda)
    if pompon:
        px, py = cx + 5 + caida, y(-alto + 2 + caida // 2)
        d.ellipse([px - 3, py - 2, px + 3, py + 4], fill=pompon)

def ala_ancha(d, col, banda=None, copa=7):
    d.ellipse([cx - 16, y(-3), cx + 16, y(2)], fill=col)
    d.rounded_rectangle([cx - 9, y(-3 - copa), cx + 9, y(0)], radius=3, fill=col)
    if banda:
        d.rectangle([cx - 9, y(-4), cx + 9, y(-2)], fill=banda)

def en_pinza_der(gy=3):
    return cx + 17, y(gy + 3)

# ---------------- MAGIA ----------------
def aprendiz_mago():
    def atras(d): capa(d, (44, 40, 58), (150, 26, 40))
    def adel(d):
        bufanda(d, (150, 26, 40), ORO)
        d.line([(cx + 18, y(6)), (cx + 25, y(-8))], fill=(92, 58, 34), width=2)
    def det(d):
        for sx in (-1, 1):
            ex = cx + sx * 6
            d.ellipse([ex - 5, y(-1), ex + 5, y(10)], outline=(34, 28, 36))
        d.line([cx - 1, y(4), cx + 1, y(4)], fill=(34, 28, 36))
        d.line([(cx + 1, y(13)), (cx - 1, y(15)), (cx + 1, y(15)), (cx - 1, y(17))], fill=(150, 24, 40))
        for (x, yy) in ((cx + 27, y(-11)), (cx + 22, y(-14)), (cx + 29, y(-5))):
            chispa(d, x, yy)
        d.point((cx + 25, y(-9)), fill=(255, 255, 255))
    return armar(atras, adel, det)

def sombrero_seleccionador():
    def atras(d): capa(d, (44, 40, 58), (40, 110, 70))
    def adel(d):
        d.ellipse([cx - 15, y(-3), cx + 15, y(2)], fill=(116, 80, 48))
        d.polygon([(cx - 9, y(-1)), (cx + 9, y(-1)), (cx + 6, y(-9)), (cx + 1, y(-14)), (cx + 8, y(-20)), (cx - 3, y(-15)), (cx - 7, y(-8))], fill=(138, 98, 60))
        d.rectangle([cx + 2, y(-12), cx + 6, y(-9)], fill=(160, 120, 76))
    def det(d):
        d.line([cx - 5, y(-7), cx - 2, y(-6)], fill=(70, 44, 26)); d.line([cx + 1, y(-6), cx + 4, y(-7)], fill=(70, 44, 26))
        d.line([cx - 4, y(-3), cx - 1, y(-2), cx + 2, y(-2), cx + 4, y(-3)], fill=(70, 44, 26))
        d.line([cx + 2, y(-12), cx + 6, y(-9)], fill=(96, 64, 38))
    return armar(atras, adel, det, mira=-1, ojos_encima=False)

def buscador_escoba():
    def atras(d):
        for k in range(5):
            col = (150, 26, 40) if k % 2 else ORO
            d.line([cx - 10 - k * 3, y(22 + k), cx - 13 - k * 3, y(22 + k)], fill=col, width=2)
    def adel(d):
        d.line([cx - 24, y(35), cx + 26, y(31)], fill=MADERA, width=2)
        d.polygon([(cx - 22, y(32)), (cx - 33, y(28)), (cx - 34, y(40)), (cx - 22, y(37))], fill=(214, 170, 96))
        d.rectangle([cx - 23, y(32), cx - 21, y(37)], fill=(150, 26, 40))
        bx, by = cx + 26, y(-8)
        d.ellipse([bx - 7, by - 3, bx - 2, by + 1], fill=BLANCO); d.ellipse([bx + 2, by - 3, bx + 7, by + 1], fill=BLANCO)
        d.ellipse([bx - 3, by - 2, bx + 3, by + 4], fill=ORO)
    def det(d):
        d.line([cx - 33, y(31), cx - 24, y(33)], fill=(176, 130, 66)); d.line([cx - 33, y(36), cx - 24, y(35)], fill=(176, 130, 66))
        d.point((cx + 25, y(-7)), fill=(255, 250, 210))
        for k in range(3):
            d.line([2, y(14 + k * 5), 9 + k * 2, y(14 + k * 5)], fill=(200, 190, 220))
    return armar(atras, adel, det, gr=(19, -5), ojos='abiertos', mira=1)

def bruja_pociones():
    def adel(d):
        d.ellipse([cx - 16, y(-3), cx + 16, y(2)], fill=(96, 52, 150))
        d.polygon([(cx - 8, y(-1)), (cx + 8, y(-1)), (cx + 3, y(-12)), (cx + 11, y(-21)), (cx - 2, y(-14))], fill=(118, 66, 176))
        d.rectangle([cx - 8, y(-3), cx + 8, y(-1)], fill=ORO)
        fx, fy = cx + 20, y(-4)
        d.rectangle([fx - 1, fy - 6, fx + 1, fy - 2], fill=(220, 236, 240))
        d.ellipse([fx - 5, fy - 3, fx + 5, fy + 7], fill=(220, 236, 240))
        d.chord([fx - 5, fy - 3, fx + 5, fy + 7], 10, 170, fill=(110, 220, 120))
        d.rectangle([fx - 2, fy - 8, fx + 2, fy - 6], fill=MADERA)
    def det(d):
        chispa(d, cx + 1, y(-8), (255, 236, 120)); d.point((cx + 6, y(-14)), fill=(255, 236, 120))
        for (bx, by) in ((cx + 19, y(-14)), (cx + 23, y(-17)), (cx + 20, y(-20))):
            d.ellipse([bx - 1, by - 1, bx + 1, by + 1], outline=(140, 230, 150))
        d.point((cx + 18, y(-1)), fill=BLANCO)
    return armar(None, adel, det, gr=(19, 2), ojos='felices')

# ---------------- TIERRA MEDIA ----------------
def hobbit():
    def atras(d): capa(d, (70, 116, 62), (100, 150, 84))
    def adel(d):
        for hx, hy in ((cx - 8, y(-3)), (cx - 3, y(-5)), (cx + 3, y(-5)), (cx + 8, y(-3))):
            d.ellipse([hx - 3, hy - 3, hx + 3, hy + 3], fill=(140, 88, 48))
        d.polygon([(cx - 3, y(23)), (cx + 3, y(23)), (cx, y(28))], fill=(120, 180, 96))
        d.polygon([(cx - 8, y(27)), (cx - 3, y(27)), (cx - 4, y(36)), (cx - 7, y(35))], fill=(206, 166, 88))
        d.polygon([(cx + 3, y(27)), (cx + 8, y(27)), (cx + 7, y(35)), (cx + 4, y(36))], fill=(206, 166, 88))
    def det(d):
        for hx, hy in ((cx - 8, y(-3)), (cx - 3, y(-5)), (cx + 3, y(-5)), (cx + 8, y(-3))):
            d.arc([hx - 2, hy - 2, hx + 2, hy + 2], 200, 520, fill=(186, 128, 76))
        d.line([cx, y(24), cx, y(27)], fill=(70, 120, 60)); d.point((cx, y(23)), fill=PLATA)
        for k in range(3):
            d.point((cx - 4, y(29) + k * 2), fill=ORO); d.point((cx + 4, y(29) + k * 2), fill=ORO)
        rx, ry = cx - 17, y(-3)
        d.ellipse([rx - 7, ry - 7, rx + 7, ry + 7], outline=(255, 236, 150))
        d.ellipse([rx - 3, ry - 3, rx + 3, ry + 3], outline=ORO)
        d.ellipse([rx - 2, ry - 2, rx + 2, ry + 2], outline=ORO_OSC)
        d.point((rx - 2, ry - 2), fill=(255, 252, 220))
        chispa(d, rx + 8, ry - 6); chispa(d, rx - 8, ry + 4)
    return armar(atras, adel, det, gl=(17, 2))

def mago_gris():
    def atras(d):
        capa(d, (128, 130, 142), (98, 100, 114))
        d.line([(cx - 18, y(-16)), (cx - 18, y(40))], fill=MADERA, width=3)
        d.ellipse([cx - 22, y(-21), cx - 14, y(-13)], fill=(255, 255, 236))
    def adel(d):
        d.polygon([(cx - 9, y(-1)), (cx + 9, y(-1)), (cx + 7, y(-12)), (cx + 3, y(-23)), (cx - 3, y(-11))], fill=(146, 148, 162))
        d.ellipse([cx - 16, y(-3), cx + 16, y(2)], fill=(156, 158, 172))
        d.polygon([(cx - 10, y(20)), (cx + 10, y(20)), (cx + 9, y(26)), (cx + 6, y(31)), (cx + 3, y(36)), (cx, y(40)), (cx - 3, y(36)), (cx - 6, y(31)), (cx - 9, y(26))], fill=(240, 240, 244))
        d.ellipse([cx - 7, y(17), cx, y(21)], fill=(240, 240, 244)); d.ellipse([cx, y(17), cx + 7, y(21)], fill=(240, 240, 244))
    def det(d):
        d.line([cx - 8, y(-3), cx + 8, y(-3)], fill=(110, 112, 126))
        for k in (-6, -3, 0, 3, 6):
            d.line([cx + k, y(23), cx + k * 2 // 3, y(36) - abs(k)], fill=(208, 208, 220))
        d.line([cx - 1, y(19), cx + 1, y(19)], fill=(200, 200, 212))
        for rr, a in ((9, 50), (6, 100)):
            d.ellipse([cx - 18 - rr, y(-17) - rr, cx - 18 + rr, y(-17) + rr], outline=(255, 255, 220, a))
        chispa(d, cx - 18, y(-17), BLANCO)
    return armar(atras, adel, det, gl=(16, 8), boca='sonrisa')

def elfo_arquero():
    def atras(d):
        capa(d, (60, 110, 72), (44, 86, 56))
        for sx in (-1, 1):
            d.polygon([(cx + sx * 4, y(-2)), (cx + sx * 13, y(0)), (cx + sx * 15, y(26)), (cx + sx * 10, y(28)), (cx + sx * 9, y(8))], fill=(246, 222, 128))
    def adel(d):
        d.arc([cx + 13, y(-14), cx + 27, y(18)], 270, 90, fill=MADERA, width=2)
        d.line([cx + 20, y(-14), cx + 20, y(18)], fill=(236, 236, 236))
        d.ellipse([cx - 3, y(22), cx + 3, y(27)], fill=(120, 190, 110))
    def det(d):
        d.arc([cx - 11, y(-3), cx + 11, y(5)], 200, 340, fill=PLATA)
        d.point((cx, y(-3)), fill=(140, 220, 255))
        d.line([cx, y(23), cx, y(26)], fill=(70, 130, 70)); d.point((cx, y(22)), fill=PLATA)
        for sx in (-1, 1):
            d.line([cx + sx * 11, y(4), cx + sx * 13, y(20)], fill=(222, 190, 96))
    return armar(atras, adel, det, gr=(19, 1))

# ---------------- GALAXIA ----------------
def caballero_espacial():
    def atras(d):
        d.ellipse([cx - 15, y(-6), cx + 15, y(22)], fill=(132, 90, 58))
        d.ellipse([cx - 11, y(-3), cx + 11, y(20)], fill=(70, 46, 30))
        capa(d, (132, 90, 58), (104, 68, 42))
    def adel(d):
        d.line([cx - 13, y(28), cx + 13, y(28)], fill=(92, 58, 36), width=2)
        d.rectangle([cx - 2, y(27), cx + 2, y(29)], fill=PLATA)
        bx, by = cx + 19, y(2)
        d.line([(bx, by + 9), (bx + 2, by + 1)], fill=PLATA_OSC, width=3)
        d.line([(bx + 2, by), (bx + 8, by - 26)], fill=(110, 196, 255), width=3)
    def det(d):
        bx, by = cx + 19, y(2)
        d.line([(bx + 2, by), (bx + 8, by - 26)], fill=(236, 250, 255))
        d.point((bx + 1, by + 5), fill=NEGRO)
    return armar(atras, adel, det, gr=(19, 4), mira=1)

def lado_oscuro():
    def atras(d): capa(d, (30, 28, 36), (60, 56, 70), ancho=21)
    def adel(d):
        d.ellipse([cx - 12, y(-6), cx + 12, y(12)], fill=(34, 32, 42))
        d.polygon([(cx - 13, y(6)), (cx + 13, y(6)), (cx + 15, y(14)), (cx - 15, y(14))], fill=(34, 32, 42))
        d.polygon([(cx - 9, y(2)), (cx - 1, y(3)), (cx - 2, y(7)), (cx - 8, y(6))], fill=(70, 76, 92))
        d.polygon([(cx + 9, y(2)), (cx + 1, y(3)), (cx + 2, y(7)), (cx + 8, y(6))], fill=(70, 76, 92))
        d.polygon([(cx - 3, y(8)), (cx + 3, y(8)), (cx + 4, y(14)), (cx - 4, y(14))], fill=(120, 124, 136))
        d.rectangle([cx - 5, y(25), cx + 5, y(30)], fill=(52, 52, 62))
        bx, by = cx + 19, y(2)
        d.line([(bx, by + 9), (bx + 2, by + 1)], fill=(60, 60, 68), width=3)
        d.line([(bx + 2, by), (bx + 8, by - 26)], fill=(255, 70, 70), width=3)
    def det(d):
        d.line([(cx + 21, y(2)), (cx + 27, y(-24))], fill=(255, 220, 220))
        for k, col in enumerate(((255, 70, 70), (90, 220, 120), (90, 160, 255))):
            d.point((cx - 3 + k * 2, y(27)), fill=col)
        for k in range(3):
            d.line([cx - 2, y(10 + k * 1), cx + 2, y(10 + k * 1)], fill=(60, 62, 72))
        d.point([(cx - 7, y(3)), (cx + 5, y(3))], fill=(150, 160, 190))
    return armar(atras, adel, det, gr=(19, 4), ojos_encima=False)

def maestro_verde():
    def atras(d):
        capa(d, (150, 112, 74), (120, 88, 56))
        for sx in (-1, 1):
            d.polygon([(cx + sx * 8, y(3)), (cx + sx * 27, y(-3)), (cx + sx * 24, y(1)), (cx + sx * 9, y(10))], fill=(140, 180, 100))
    def adel(d):
        d.line([(cx - 17, y(12)), (cx - 19, y(40))], fill=(96, 70, 44), width=2)
    def det(d):
        for sx in (-1, 1):
            d.line([cx + sx * 11, y(4), cx + sx * 23, y(-1)], fill=(176, 120, 120))
        for k in range(4):
            d.point((cx - 3 + k * 2, y(-1) - (k % 2)), fill=(236, 236, 236))
    return armar(atras, adel, det, gl=(17, 9), gr=(17, 9), boca='sonrisa')

def princesa_galactica():
    def atras(d):
        capa(d, (244, 244, 246), (220, 222, 230))
        for sx in (-1, 1):
            d.ellipse([cx + sx * 14 - 6, y(-1), cx + sx * 14 + 6, y(11)], fill=(118, 76, 46))
    def adel(d):
        d.line([cx - 12, y(28), cx + 12, y(28)], fill=PLATA, width=2)
    def det(d):
        for sx in (-1, 1):
            hx = cx + sx * 14
            d.arc([hx - 4, y(1), hx + 4, y(9)], 0, 300, fill=(150, 100, 64))
            d.arc([hx - 2, y(3), hx + 2, y(7)], 0, 300, fill=(150, 100, 64))
        for k in range(4):
            d.point((cx - 6 + k * 4, y(28)), fill=(120, 200, 255))
    return armar(atras, adel, det, gl=(18, 10), gr=(18, 10))

# ---------------- MARVEL (inspirados) ----------------
def hombre_arana():
    def tenir(im):
        azul = (52, 96, 206)
        teñir(im, {R: azul, r: tono(azul, .8), L: tono(azul, 1.25), BELLY: azul, (236, 170, 150): tono(azul, .8), RR: (34, 64, 150)}, y0=y(28))
    def adel(d):
        d.ellipse([cx - 11, y(-1), cx + 11, y(11)], fill=(214, 40, 50))
        for sx in (-1, 1):
            ex = cx + sx * 5
            d.polygon([(ex - sx * 3, y(1)), (ex + sx * 1, y(2)), (ex + sx * 4, y(5)), (ex + sx * 4, y(8)), (ex, y(8)), (ex - sx * 3, y(6))], fill=BLANCO)
    def det(d):
        tela = (140, 20, 32)
        for sx in (-1, 1):
            d.polygon([(cx + sx * 5 - sx * 3, y(1)), (cx + sx * 5 + sx * 1, y(2)), (cx + sx * 5 + sx * 4, y(5)), (cx + sx * 5 + sx * 4, y(8)), (cx + sx * 5, y(8)), (cx + sx * 5 - sx * 3, y(6))], outline=NEGRO)
        d.line([cx, y(-1), cx, y(11)], fill=tela)
        d.arc([cx - 8, y(-4), cx + 8, y(14)], 180, 360, fill=tela)
        for ang in (215, 250, 290, 325):
            a = math.radians(ang)
            d.line([cx, y(30), cx + 15 * math.cos(a), y(30) + 15 * math.sin(a)], fill=tela)
        d.arc([cx - 9, y(21), cx + 9, y(39)], 200, 340, fill=tela)
        d.point([(cx, y(24)), (cx - 1, y(25)), (cx + 1, y(25)), (cx, y(26)), (cx - 2, y(24)), (cx + 2, y(24)), (cx - 2, y(27)), (cx + 2, y(27))], fill=NEGRO)
        for sx in (-1, 1):
            d.line([(cx + sx * 17, y(3)), (cx + sx * 24, y(-12))], fill=BLANCO)
    return armar(None, adel, det, tenir=tenir, ojos='parpadeo', boca='sonrisa', gl=(17, 0), gr=(17, 0), ojos_encima=False)

def capitan_escudo():
    def tenir(im):
        teñir(im, {BELLY: (50, 86, 176), (236, 170, 150): (40, 68, 150)})
    def adel(d):
        sx_, sy_ = cx + 19, y(4)
        for rad, col in ((10, (210, 40, 50)), (8, BLANCO), (6, (210, 40, 50)), (4, (50, 86, 176))):
            d.ellipse([sx_ - rad, sy_ - rad, sx_ + rad, sy_ + rad], fill=col)
        d.rounded_rectangle([cx - 10, y(-4), cx + 10, y(1)], radius=2, fill=(50, 86, 176))
    def det(d):
        estrella5(d, cx + 19, y(4), 4, BLANCO)
        estrella5(d, cx, y(30), 4, BLANCO)
        for sx in (-1, 1):
            d.polygon([(cx + sx * 10, y(-3)), (cx + sx * 15, y(-6)), (cx + sx * 13, y(-1))], fill=BLANCO)
        estrella5(d, cx, y(-2), 2, BLANCO)
    return armar(None, adel, det, tenir=tenir, gr=(19, 4))

def dios_trueno():
    def atras(d): capa(d, (196, 32, 44), (150, 22, 34), ancho=21)
    def adel(d):
        d.chord([cx - 8, y(-6), cx + 8, y(4)], 180, 360, fill=PLATA)
        for sx in (-1, 1):
            d.polygon([(cx + sx * 7, y(-2)), (cx + sx * 16, y(-9)), (cx + sx * 13, y(-3)), (cx + sx * 16, y(-4)), (cx + sx * 9, y(1))], fill=BLANCO)
        d.line([cx + 18, y(10), cx + 18, y(-3)], fill=MADERA, width=2)
        d.rectangle([cx + 12, y(-11), cx + 24, y(-3)], fill=(150, 156, 168))
        d.line([cx - 12, y(29), cx + 12, y(29)], fill=(70, 70, 84), width=2)
    def det(d):
        d.line([cx + 12, y(-11), cx + 24, y(-11)], fill=(190, 196, 206))
        rayo(d, cx + 26, y(-20), (255, 230, 90))
        rayo(d, cx + 6, y(-18), (255, 240, 150))
    return armar(atras, adel, det, gr=(18, 6), ojos='abiertos')

def armadura_hierro():
    def tenir(im):
        cuerpo_color((196, 34, 44), panza=(244, 190, 70), patas=(200, 150, 50))(im)
    def adel(d):
        for sx in (-1, 1):
            d.polygon([(cx + sx * 12, y(40)), (cx + sx * 16, y(40)), (cx + sx * 14, y(47))], fill=(255, 170, 60))
    def det(d):
        d.ellipse([cx - 3, y(26), cx + 3, y(32)], fill=(150, 230, 255))
        d.ellipse([cx - 1, y(28), cx + 1, y(30)], fill=BLANCO)
        d.arc([cx - 5, y(24), cx + 5, y(34)], 0, 360, fill=(110, 180, 230))
        for sx in (-1, 1):
            d.point((cx + sx * 14, y(44)), fill=(255, 230, 120))
    return armar(None, adel, det, tenir=tenir)

def gigante_verde():
    def tenir(im):
        cuerpo_color((110, 186, 82), panza=(160, 214, 120), patas=(70, 130, 54))(im)
    def adel(d):
        d.polygon([(cx - 13, y(30)), (cx + 13, y(30)), (cx + 12, y(36)), (cx + 8, y(34)), (cx + 4, y(37)), (cx, y(34)), (cx - 4, y(37)), (cx - 8, y(34)), (cx - 12, y(36))], fill=(120, 66, 160))
    def det(d):
        for sx in (-1, 1):
            ex = cx + sx * 6
            d.line([ex - sx * 4, y(-2), ex + sx * 3, y(0)], fill=(40, 70, 30))
        d.line([cx - 2, y(9), cx - 1, y(11)], fill=(60, 110, 46))
    return armar(None, adel, det, tenir=tenir, gl=(18, 6), gr=(18, 6))

def hechicero_supremo():
    def atras(d):
        capa(d, (186, 36, 48), (150, 26, 38), ancho=21)
        for sx in (-1, 1):
            d.polygon([(cx + sx * 9, y(16)), (cx + sx * 16, y(2)), (cx + sx * 15, y(18))], fill=(186, 36, 48))
    def adel(d):
        d.ellipse([cx - 4, y(23), cx + 4, y(31)], fill=ORO)
    def det(d):
        d.ellipse([cx - 2, y(25), cx + 2, y(29)], fill=(90, 220, 120))
        d.point((cx, y(27)), fill=(20, 80, 40))
        mx, my = cx + 23, y(-2)
        for rad, col in ((9, (255, 170, 60)), (6, (255, 210, 110))):
            d.ellipse([mx - rad, my - rad, mx + rad, my + rad], outline=col)
        for k in range(8):
            a = k * math.pi / 4
            d.point((mx + 8 * math.cos(a), my + 8 * math.sin(a)), fill=(255, 240, 180))
        estrella5(d, mx, my, 3, (255, 200, 90))
    return armar(atras, adel, det, gr=(19, 1), ojos='abiertos', mira=1)

# ---------------- DC (inspirados) ----------------
def murcielago():
    def atras(d):
        capa(d, (40, 40, 54), None, ancho=22, alto=39)
        for k in range(4):
            d.ellipse([cx - 22 + k * 11, y(37), cx - 11 + k * 11, y(42)], fill=(0, 0, 0, 0))
    def adel(d):
        d.ellipse([cx - 12, y(-3), cx + 12, y(14)], fill=(48, 48, 62))
        for sx in (-1, 1):
            d.polygon([(cx + sx * 10, y(1)), (cx + sx * 9, y(-9)), (cx + sx * 5, y(-2))], fill=(48, 48, 62))
        d.line([cx - 12, y(29), cx + 12, y(29)], fill=ORO, width=2)
        d.ellipse([cx - 6, y(19), cx + 6, y(25)], fill=ORO)
    def det(d):
        for sx in (-1, 1):
            ex = cx + sx * 5
            d.polygon([(ex - sx * 3, y(4)), (ex + sx * 3, y(6)), (ex - sx * 2, y(7))], fill=BLANCO)
        d.polygon([(cx - 5, y(22)), (cx - 2, y(20)), (cx, y(21)), (cx + 2, y(20)), (cx + 5, y(22)), (cx, y(24))], fill=NEGRO)
        d.line([cx - 2, y(11), cx + 2, y(11)], fill=(30, 30, 40))
    return armar(atras, adel, det, boca='sonrisa', ojos_encima=False)

def kriptoniano():
    def atras(d): capa(d, (210, 34, 44), (170, 24, 36), ancho=21)
    def tenir(im):
        cuerpo_color((58, 104, 214), panza=(80, 126, 228), patas=(200, 30, 44))(im)
    def adel(d):
        d.polygon([(cx - 7, y(23)), (cx + 7, y(23)), (cx + 9, y(26)), (cx, y(33)), (cx - 9, y(26))], fill=(250, 214, 70))
    def det(d):
        d.polygon([(cx - 5, y(25)), (cx + 5, y(25)), (cx + 6, y(26)), (cx, y(31)), (cx - 6, y(26))], fill=(210, 34, 44))
        d.line([cx - 3, y(27), cx + 3, y(27)], fill=(250, 214, 70)); d.line([cx - 2, y(29), cx + 2, y(29)], fill=(250, 214, 70))
        d.arc([cx - 2, y(10), cx + 2, y(14)], 90, 360, fill=(30, 26, 40))
    return armar(atras, adel, det, tenir=tenir, gl=(17, -2), gr=(18, 8))

def amazona():
    def atras(d):
        for sx in (-1, 1):
            d.polygon([(cx + sx * 3, y(-2)), (cx + sx * 13, y(0)), (cx + sx * 16, y(24)), (cx + sx * 10, y(26)), (cx + sx * 9, y(8))], fill=(44, 32, 40))
    def adel(d):
        d.chord([cx - 12, y(-4), cx + 12, y(6)], 190, 350, fill=ORO)
        for sx in (-1, 1):
            d.rectangle([cx + sx * 15 - 2, y(13), cx + sx * 15 + 2, y(16)], fill=PLATA)
        d.line([cx - 12, y(27), cx + 12, y(27)], fill=ORO, width=2)
        lx, ly = cx - 20, y(-2)
        for rad in (6, 4):
            d.ellipse([lx - rad, ly - rad, lx + rad, ly + rad], outline=(250, 210, 80))
    def det(d):
        estrella5(d, cx, y(-2), 3, (220, 40, 50))
        d.polygon([(cx - 6, y(23)), (cx, y(26)), (cx + 6, y(23)), (cx + 3, y(25)), (cx, y(27)), (cx - 3, y(25))], fill=ORO)
        d.line([cx - 20, y(4), cx - 22, y(12)], fill=(250, 210, 80))
        chispa(d, cx - 26, y(-6))
    return armar(atras, adel, det, gl=(18, -1))

def velocista():
    def adel(d):
        d.ellipse([cx - 6, y(22), cx + 6, y(32)], fill=BLANCO)
        for sx in (-1, 1):
            d.polygon([(cx + sx * 9, y(3)), (cx + sx * 16, y(-3)), (cx + sx * 13, y(2)), (cx + sx * 17, y(1)), (cx + sx * 10, y(8))], fill=(250, 210, 60))
    def det(d):
        rayo(d, cx - 1, y(22), (250, 200, 50))
        for k, ln in enumerate((10, 14, 8, 12)):
            d.line([1, y(8 + k * 7), 1 + ln, y(8 + k * 7)], fill=(250, 210, 80))
        rayo(d, 4, y(-12), (255, 230, 120))
    return armar(None, adel, det, gl=(15, 10), gr=(19, -1), mira=1)

def rey_del_mar():
    def tenir(im):
        teñir(im, {BELLY: (240, 166, 64), (236, 170, 150): (210, 130, 44), RR: (60, 150, 100)})
    def adel(d):
        d.polygon([(cx - 9, y(1)), (cx - 9, y(-6)), (cx - 5, y(-3)), (cx, y(-9)), (cx + 5, y(-3)), (cx + 9, y(-6)), (cx + 9, y(1))], fill=ORO)
        tx = cx + 20
        d.line([tx, y(36), tx, y(-10)], fill=ORO_OSC, width=2)
        d.line([tx - 5, y(-10), tx + 5, y(-10)], fill=ORO, width=2)
        for dx in (-5, 0, 5):
            d.polygon([(tx + dx - 1, y(-10)), (tx + dx + 1, y(-10)), (tx + dx, y(-17) + abs(dx) // 2)], fill=ORO)
    def det(d):
        for rr in range(3):
            for k in range(-2, 3):
                d.arc([cx + k * 4 - 2 + (rr % 2) * 2, y(27 + rr * 3), cx + k * 4 + 2 + (rr % 2) * 2, y(30 + rr * 3)], 0, 180, fill=(200, 120, 40))
        d.point([(cx - 5, y(-3)), (cx, y(-6)), (cx + 5, y(-3))], fill=(110, 220, 220))
        for (bx, by) in ((cx - 24, y(-4)), (cx - 20, y(-12)), (cx - 26, y(6))):
            d.ellipse([bx - 1, by - 1, bx + 2, by + 2], outline=(150, 210, 250))
    return armar(None, adel, det, tenir=tenir, gr=(20, 8))

def anillo_verde():
    def tenir(im):
        teñir(im, {BELLY: (70, 170, 90), (236, 170, 150): (50, 130, 70)})
    def atras(d):
        d.rounded_rectangle([cx - 13, y(2), cx + 13, y(7)], radius=3, fill=(60, 170, 80))
    def adel(d):
        d.ellipse([cx - 4, y(23), cx + 4, y(31)], fill=(30, 30, 40))
    def det(d):
        d.ellipse([cx - 3, y(24), cx + 3, y(30)], outline=(120, 240, 140))
        d.line([cx - 4, y(25), cx + 4, y(25)], fill=(30, 30, 40)); d.line([cx - 4, y(29), cx + 4, y(29)], fill=(30, 30, 40))
        rx, ry = cx + 18, y(2)
        for rad, a in ((10, 60), (7, 110)):
            d.ellipse([rx - rad, ry - rad, rx + rad, ry + rad], outline=(130, 255, 150, a))
        d.ellipse([rx - 2, ry - 2, rx + 2, ry + 2], fill=(120, 240, 140))
        chispa(d, rx + 9, ry - 8, (200, 255, 210))
    return armar(atras, adel, det, tenir=tenir, gr=(18, -1))

# ---------------- FECHAS ESPECIALES ----------------
def san_valentin():
    def atras(d):
        for sx in (-1, 1):
            for k, (w, h) in enumerate(((15, 11), (12, 8))):
                x0 = cx + sx * 8
                d.ellipse([min(x0, x0 + sx * w), y(14 + k * 7), max(x0, x0 + sx * w), y(14 + k * 7 + h)], fill=(252, 250, 255))
    def adel(d):
        d.arc([cx - 11, y(-5), cx + 11, y(7)], 190, 350, fill=(226, 50, 80), width=2)
        for sx in (-1, 1):
            d.line([(cx + sx * 8, y(-3)), (cx + sx * 10, y(-9))], fill=(226, 50, 80))
        d.arc([cx + 13, y(-10), cx + 25, y(14)], 270, 90, fill=ORO, width=2)
        d.line([cx + 19, y(-10), cx + 19, y(14)], fill=(255, 220, 230))
        d.line([cx + 6, y(2), cx + 28, y(2)], fill=MADERA)
    def det(d):
        for sx in (-1, 1):
            corazon(d, cx + sx * 10 - 3, y(-14), (236, 40, 80), True)
            for k in range(3):
                d.line([cx + sx * (11 + k * 3), y(18), cx + sx * (11 + k * 3), y(23)], fill=(218, 210, 236))
        corazon(d, cx + 27, y(0), (236, 40, 80))
        for sx in (-1, 1):
            d.ellipse([cx + sx * 9 - 3, y(19), cx + sx * 9 + 3, y(22)], fill=(255, 110, 140))
        corazon(d, cx - 26, y(-6), (255, 140, 170)); corazon(d, cx - 22, y(-16), (255, 170, 190))
    return armar(atras, adel, det, ojos='felices', gr=(19, 4))

def pijama():
    def tenir(im):
        p = im.load()
        for yy in range(y(25), y(38)):
            for xx in range(cx - 15, cx + 16):
                c = p[xx, yy]
                if c[3] and c[:3] in (R, r, L, BELLY, (236, 170, 150), BRI):
                    p[xx, yy] = ((240, 244, 255, 255) if (xx // 2) % 2 else (128, 158, 228, 255))
    def adel(d):
        gorro_cono(d, (96, 128, 210), (240, 244, 255), alto=13, caida=9, pompon=BLANCO)
        ox, oy = cx - 24, y(2)
        d.ellipse([ox, oy + 4, ox + 9, oy + 13], fill=(186, 130, 82))
        d.ellipse([ox + 1, oy - 3, ox + 8, oy + 5], fill=(186, 130, 82))
        d.ellipse([ox, oy - 4, ox + 3, oy - 1], fill=(186, 130, 82)); d.ellipse([ox + 6, oy - 4, ox + 9, oy - 1], fill=(186, 130, 82))
    def det(d):
        for (sx_, sy_) in ((cx - 4, y(-6)), (cx + 3, y(-9)), (cx + 8, y(-5))):
            d.point((sx_, sy_), fill=(255, 240, 150))
        ox, oy = cx - 24, y(2)
        d.point([(ox + 3, oy), (ox + 6, oy)], fill=(40, 26, 26)); d.point((ox + 4, oy + 2), fill=(90, 50, 40))
        d.ellipse([ox + 3, oy + 6, ox + 6, oy + 10], fill=(222, 180, 130))
        chispa(d, cx + 24, y(-14)); d.point((cx + 20, y(-20)), fill=(255, 240, 160))
    return armar(None, adel, det, tenir=tenir, ojos='cerrados', boca='dormido', gl=(14, 9))

def navidad():
    def adel(d):
        gorro_cono(d, (214, 40, 50), BLANCO, alto=14, caida=10, pompon=BLANCO)
        bufanda(d, (40, 140, 80), (40, 140, 80))
        bx, by = cx + 19, y(4)
        d.rectangle([bx - 1, by - 10, bx + 1, by + 6], fill=BLANCO)
        d.arc([bx - 1, by - 16, bx + 9, by - 6], 180, 360, fill=BLANCO, width=3)
    def det(d):
        bx, by = cx + 19, y(4)
        for k in range(0, 16, 3):
            d.line([bx - 1, by + 6 - k, bx + 1, by + 4 - k], fill=(220, 40, 50))
        d.point([(bx + 1, by - 14), (bx + 5, by - 16), (bx + 8, by - 13)], fill=(220, 40, 50))
        for xx in range(cx - 12, cx + 13, 4):
            d.point((xx, y(25)), fill=BLANCO)
        for (sx_, sy_) in ((cx - 24, y(-10)), (cx - 18, y(-18)), (cx + 26, y(-18)), (cx - 27, y(8))):
            d.point([(sx_, sy_ - 1), (sx_, sy_ + 1), (sx_ - 1, sy_), (sx_ + 1, sy_), (sx_, sy_)], fill=(220, 236, 255))
    return armar(None, adel, det, gr=(19, 4))

def cumpleanos():
    def adel(d):
        d.polygon([(cx - 7, y(0)), (cx + 7, y(0)), (cx + 2, y(-16))], fill=(120, 176, 244))
        d.ellipse([cx, y(-20), cx + 5, y(-15)], fill=(255, 120, 160))
        px, py = cx + 18, y(-2)
        d.rectangle([px - 6, py, px + 6, py + 7], fill=(250, 214, 170))
        d.rectangle([px - 6, py, px + 6, py + 2], fill=(255, 150, 190))
        d.rectangle([px - 1, py - 5, px + 1, py - 1], fill=(120, 176, 244))
    def det(d):
        for k in range(3):
            y0 = y(-3) - k * 4
            d.line([(cx - 6 + k * 2, y0), (cx + 6 - k * 2, y0)], fill=(255, 226, 100))
        d.point((cx + 18, y(-8)), fill=(255, 200, 60)); d.point((cx + 18, y(-9)), fill=(255, 120, 60))
        d.point((cx + 18, y(-10)), fill=(255, 240, 160))
        for (x, yy, c) in ((cx - 22, y(-12), (255, 120, 160)), (cx - 15, y(-19), (120, 200, 120)), (cx + 12, y(-17), (255, 200, 60)),
                           (cx + 26, y(-12), (120, 176, 244)), (cx - 26, y(-1), (255, 200, 60)), (cx - 8, y(-23), (190, 120, 240))):
            d.rectangle([x, yy, x + 1, yy + 1], fill=c)
        d.point([(cx + 14, y(0)), (cx + 17, y(1)), (cx + 21, y(0))], fill=(255, 255, 255))
    return armar(None, adel, det, ojos='felices', gr=(18, 6))

def fantasmita():
    def adel(d):
        pts = [(cx - 15, y(4))]
        for k in range(7):
            pts.append((cx - 15 + k * 5, y(40) if k % 2 == 0 else y(36)))
        pts += [(cx + 15, y(40)), (cx + 15, y(4))]
        d.polygon(pts, fill=(250, 250, 252))
        d.ellipse([cx - 15, y(-10), cx + 15, y(16)], fill=(250, 250, 252))
        bx, by = cx + 21, y(14)
        d.chord([bx - 6, by - 4, bx + 6, by + 8], 0, 180, fill=(250, 140, 40))
        d.rectangle([bx - 6, by + 1, bx + 6, by + 2], fill=(250, 140, 40))
    def det(d):
        for sx in (-1, 1):
            d.ellipse([cx + sx * 6 - 3, y(-1), cx + sx * 6 + 3, y(7)], fill=NEGRO)
            d.point((cx + sx * 6 - 1, y(1)), fill=BLANCO)
            d.ellipse([cx + sx * 10 - 2, y(9), cx + sx * 10 + 2, y(11)], fill=(255, 170, 190))
        d.ellipse([cx - 2, y(9), cx + 2, y(13)], fill=NEGRO)
        bx, by = cx + 21, y(14)
        d.arc([bx - 5, by - 9, bx + 5, by + 1], 180, 360, fill=(60, 50, 50))
        d.point([(bx - 2, by + 3), (bx + 2, by + 3)], fill=(60, 30, 10)); d.line([bx - 2, by + 5, bx + 2, by + 5], fill=(60, 30, 10))
    return armar(None, adel, det, gr=(20, 10), ojos_encima=False)

def anio_nuevo():
    def adel(d):
        d.ellipse([cx - 13, y(-3), cx + 13, y(1)], fill=(36, 34, 44))
        d.rectangle([cx - 8, y(-15), cx + 8, y(-1)], fill=(36, 34, 44))
        d.rectangle([cx - 8, y(-5), cx + 8, y(-3)], fill=ORO)
        d.polygon([(cx + 17, y(4)), (cx + 21, y(-6)), (cx + 26, y(-4))], fill=(240, 120, 200))
    def det(d):
        for (fx, fy, col) in ((cx - 20, y(-14), (255, 120, 160)), (cx + 20, y(-18), (255, 220, 90)), (cx - 6, y(-24), (120, 200, 255))):
            for k in range(8):
                a = k * math.pi / 4
                d.point((fx + 5 * math.cos(a), fy + 5 * math.sin(a)), fill=col)
                d.point((fx + 3 * math.cos(a), fy + 3 * math.sin(a)), fill=col)
        for (x, yy, c) in ((cx + 25, y(-10), (255, 220, 90)), (cx + 28, y(-6), (120, 220, 160)), (cx + 23, y(-13), (255, 120, 160))):
            d.line([cx + 23, y(-5), x, yy], fill=c)
    return armar(None, adel, det, ojos='felices', gr=(18, 6))

def conejito():
    def adel(d):
        for sx, inc in ((-1, -3), (1, 4)):
            bx = cx + sx * 5
            d.ellipse([bx - 3 + inc, y(-22), bx + 3 + inc, y(-1)], fill=BLANCO)
        d.arc([cx - 10, y(-4), cx + 10, y(6)], 190, 350, fill=(250, 170, 200), width=2)
        ex, ey = cx + 19, y(1)
        d.ellipse([ex - 5, ey - 6, ex + 5, ey + 7], fill=(180, 220, 250))
    def det(d):
        for sx, inc in ((-1, -3), (1, 4)):
            bx = cx + sx * 5
            d.ellipse([bx - 1 + inc, y(-19), bx + 1 + inc, y(-4)], fill=(255, 180, 200))
        ex, ey = cx + 19, y(1)
        d.line([ex - 5, ey, ex + 5, ey], fill=(250, 150, 190))
        d.line([ex - 4, ey + 3, ex - 2, ey + 2, ex, ey + 3, ex + 2, ey + 2, ex + 4, ey + 3], fill=(250, 210, 90))
        d.point([(ex - 2, ey - 3), (ex + 2, ey - 3)], fill=(140, 200, 120))
    return armar(None, adel, det, gr=(19, 4), ojos='felices')

# ---------------- OTROS ----------------
def chef():
    def adel(d):
        d.rectangle([cx - 8, y(-9), cx + 8, y(0)], fill=BLANCO)
        for k, dx in enumerate((-7, 0, 7)):
            d.ellipse([cx + dx - 6, y(-18) + (k % 2), cx + dx + 6, y(-7)], fill=BLANCO)
        d.polygon([(cx - 8, y(23)), (cx + 8, y(23)), (cx, y(29))], fill=(220, 50, 60))
        sx_, sy_ = cx + 18, y(4)
        d.line([sx_, sy_ + 6, sx_ + 3, sy_ - 6], fill=MADERA, width=2)
        d.rectangle([sx_ + 1, sy_ - 12, sx_ + 9, sy_ - 7], fill=PLATA)
        d.ellipse([sx_ + 1, sy_ - 17, sx_ + 10, sy_ - 12], fill=(232, 176, 96))
    def det(d):
        d.line([cx - 8, y(-2), cx + 8, y(-2)], fill=(226, 226, 230))
        d.line([cx + 21, y(-12), cx + 26, y(-12)], fill=(196, 130, 56))
        d.ellipse([cx + 24, y(-17), cx + 27, y(-15)], fill=(255, 236, 140))
        for k in range(3):
            d.point((cx + 20 + k * 3, y(-21) - (k % 2)), fill=(230, 230, 240))
    return armar(None, adel, det, gr=(18, 4), ojos='felices')

def pirata():
    def tenir(im):
        p = im.load()
        for yy in range(y(26), y(37)):
            for xx in range(cx - 9, cx + 10):
                if p[xx, yy][3] and p[xx, yy][:3] in (BELLY, (236, 170, 150)):
                    p[xx, yy] = ((246, 246, 248, 255) if (yy // 2) % 2 else (220, 50, 60, 255))
    def adel(d):
        d.polygon([(cx - 16, y(0)), (cx - 10, y(-10)), (cx, y(-6)), (cx + 10, y(-10)), (cx + 16, y(0)), (cx, y(2))], fill=(40, 34, 44))
        sx_, sy_ = cx + 18, y(4)
        d.line([sx_, sy_ + 5, sx_ + 6, sy_ - 18], fill=PLATA, width=2)
        d.line([sx_ - 3, sy_ + 2, sx_ + 3, sy_ + 4], fill=ORO, width=2)
    def det(d):
        d.ellipse([cx - 11, y(0), cx - 1, y(9)], fill=(30, 26, 34), outline=OUTL)
        d.line([cx - 1, y(2), cx + 12, y(-1)], fill=(30, 26, 34))
        d.point([(cx - 1, y(-5)), (cx + 1, y(-5)), (cx, y(-4)), (cx - 1, y(-3)), (cx + 1, y(-3))], fill=BLANCO)
        d.line([cx - 14, y(-1), cx + 14, y(-1)], fill=ORO)
        d.line([cx + 19, y(1), cx + 24, y(-17)], fill=(240, 244, 250))
    return armar(None, adel, det, tenir=tenir, gr=(18, 4), boca='sonrisa')

def astronauta():
    def tenir(im):
        teñir(im, {BELLY: (236, 238, 244), (236, 170, 150): (200, 204, 214)})
    def adel(d):
        d.rectangle([cx - 5, y(26), cx + 5, y(31)], fill=(90, 100, 120))
        d.line([cx + 9, y(-14), cx + 9, y(-6)], fill=PLATA)
    def det(d):
        casco = Image.new('RGBA', (CW, CH), (0, 0, 0, 0)); dc = ImageDraw.Draw(casco)
        dc.ellipse([cx - 16, y(-11), cx + 16, y(22)], fill=(190, 230, 255, 70), outline=(150, 190, 220, 255))
        dc.arc([cx - 13, y(-8), cx + 3, y(10)], 190, 260, fill=(255, 255, 255, 220), width=2)
        d._image.alpha_composite(casco)
        d.ellipse([cx + 7, y(-17), cx + 11, y(-13)], fill=(255, 90, 90))
        for k, col in enumerate(((255, 80, 80), (90, 220, 120), (255, 210, 80))):
            d.point((cx - 3 + k * 3, y(28)), fill=col)
        for (sx_, sy_) in ((cx - 26, y(-14)), (cx + 26, y(-6)), (cx - 22, y(28)), (cx + 24, y(-20))):
            chispa(d, sx_, sy_, (255, 250, 200))
    return armar(None, adel, det, tenir=tenir, gl=(18, 12), gr=(18, 12))

def graduado():
    def adel(d):
        d.rectangle([cx - 8, y(-5), cx + 8, y(0)], fill=(36, 34, 44))
        d.polygon([(cx - 16, y(-6)), (cx, y(-11)), (cx + 16, y(-6)), (cx, y(-2))], fill=(44, 42, 54))
        rx, ry = cx + 19, y(3)
        d.rounded_rectangle([rx - 3, ry - 10, rx + 3, ry + 8], radius=2, fill=(250, 244, 226))
    def det(d):
        d.line([cx, y(-7), cx + 12, y(-5), cx + 12, y(4)], fill=ORO)
        d.rectangle([cx + 11, y(4), cx + 13, y(7)], fill=ORO)
        rx, ry = cx + 19, y(3)
        d.rectangle([rx - 3, ry - 1, rx + 3, ry + 1], fill=(210, 40, 50))
        d.point((rx + 4, ry + 2), fill=(210, 40, 50))
        chispa(d, cx - 22, y(-10)); chispa(d, cx + 26, y(-14))
    return armar(None, adel, det, gr=(19, 5), ojos='felices')

def vaquero():
    def adel(d):
        d.chord([cx - 18, y(-6), cx + 18, y(4)], 0, 180, fill=(170, 110, 60))
        d.rounded_rectangle([cx - 9, y(-11), cx + 9, y(0)], radius=4, fill=(170, 110, 60))
        d.polygon([(cx - 12, y(23)), (cx + 12, y(23)), (cx, y(31))], fill=(214, 44, 54))
    def det(d):
        d.rectangle([cx - 9, y(-3), cx + 9, y(-2)], fill=(110, 66, 36))
        d.line([cx, y(-11), cx, y(-7)], fill=(140, 88, 46))
        for (x, yy) in ((cx - 6, y(24)), (cx + 5, y(24)), (cx, y(27))):
            d.point((x, yy), fill=BLANCO)
        estrella5(d, cx - 6, y(32), 3, ORO)
    return armar(None, adel, det, boca='sonrisa')

def rey():
    def atras(d):
        capa(d, (176, 30, 56), None, ancho=21)
        d.rectangle([cx - 21, y(35), cx + 21, y(38)], fill=BLANCO)
    def adel(d):
        d.polygon([(cx - 10, y(1)), (cx - 10, y(-7)), (cx - 6, y(-3)), (cx - 3, y(-10)), (cx, y(-4)), (cx + 3, y(-10)), (cx + 6, y(-3)), (cx + 10, y(-7)), (cx + 10, y(1))], fill=ORO)
        d.rectangle([cx - 13, y(14), cx + 13, y(18)], fill=BLANCO)
        d.line([cx + 19, y(14), cx + 19, y(-6)], fill=ORO_OSC, width=2)
        d.ellipse([cx + 16, y(-11), cx + 22, y(-5)], fill=(220, 50, 80))
    def det(d):
        d.point([(cx - 6, y(-1)), (cx, y(-1)), (cx + 6, y(-1))], fill=(90, 160, 240)); d.point((cx, y(-1)), fill=(220, 50, 80))
        for xx in range(cx - 11, cx + 12, 4):
            d.point((xx, y(16)), fill=NEGRO)
        for xx in range(cx - 19, cx + 20, 5):
            d.point((xx, y(36)), fill=NEGRO)
        d.point((cx + 18, y(-10)), fill=(255, 200, 210))
    return armar(atras, adel, det, gr=(19, 6))

def hada():
    def atras(d):
        for sx in (-1, 1):
            d.ellipse([cx + sx * 6 - (13 if sx < 0 else 0), y(8), cx + sx * 6 + (13 if sx > 0 else 0), y(22)], fill=(250, 210, 236))
            d.ellipse([cx + sx * 6 - (10 if sx < 0 else 0), y(20), cx + sx * 6 + (10 if sx > 0 else 0), y(30)], fill=(236, 210, 250))
    def adel(d):
        d.polygon([(cx - 6, y(0)), (cx - 4, y(-5)), (cx - 2, y(-2)), (cx, y(-7)), (cx + 2, y(-2)), (cx + 4, y(-5)), (cx + 6, y(0))], fill=(255, 200, 230))
        d.line([cx + 18, y(8), cx + 22, y(-8)], fill=ORO, width=1)
    def det(d):
        estrella5(d, cx + 23, y(-11), 5, (255, 226, 90))
        d.point((cx, y(-4)), fill=(140, 220, 255))
        for (sx_, sy_) in ((cx + 28, y(-18)), (cx + 17, y(-17)), (cx - 24, y(-6)), (cx - 18, y(-14))):
            chispa(d, sx_, sy_, (255, 236, 250))
    return armar(atras, adel, det, ojos='felices', gr=(18, 6))

def abejita():
    def atras(d):
        for sx in (-1, 1):
            d.ellipse([cx + sx * 8 - (12 if sx < 0 else 0), y(8), cx + sx * 8 + (12 if sx > 0 else 0), y(20)], fill=(226, 244, 255, 230))
    def tenir(im):
        cuerpo_color((250, 200, 50), panza=(255, 228, 120), patas=(60, 50, 50))(im)
        p = im.load()
        for yy in list(range(y(25), y(27))) + list(range(y(31), y(33))):
            for xx in range(CW):
                if p[xx, yy][3] and p[xx, yy][:3] != OUTL and abs(xx - cx) < 15:
                    p[xx, yy] = (50, 40, 46, 255)
    def adel(d):
        d.polygon([(cx - 1, y(38)), (cx + 1, y(38)), (cx, y(42))], fill=(60, 50, 50))
    def det(d):
        for sx in (-1, 1):
            d.line([cx + sx * 2, y(12), cx + sx * 4, y(-6)], fill=(50, 40, 46))
            d.ellipse([cx + sx * 4 - 2, y(-9), cx + sx * 4 + 2, y(-5)], fill=(50, 40, 46))
        corazon(d, cx + 22, y(-12), (255, 140, 170))
    return armar(atras, adel, det, tenir=tenir)

def marinero():
    def adel(d):
        d.ellipse([cx - 12, y(-6), cx + 12, y(2)], fill=BLANCO)
        d.rectangle([cx - 10, y(-3), cx + 10, y(0)], fill=(50, 90, 180))
        d.polygon([(cx - 13, y(22)), (cx + 13, y(22)), (cx + 10, y(28)), (cx, y(25)), (cx - 10, y(28))], fill=(50, 90, 180))
        d.polygon([(cx - 3, y(25)), (cx + 3, y(25)), (cx, y(31))], fill=(220, 50, 60))
    def det(d):
        d.line([cx - 12, y(23), cx + 12, y(23)], fill=BLANCO)
        d.line([cx - 1, y(31), cx - 1, y(35)], fill=(50, 90, 180)); d.line([cx - 3, y(33), cx + 1, y(33)], fill=(50, 90, 180))
        d.arc([cx - 4, y(32), cx + 2, y(36)], 0, 180, fill=(50, 90, 180))
        for k in range(3):
            d.arc([cx - 30 + k * 6, y(36), cx - 24 + k * 6, y(40)], 180, 360, fill=(120, 180, 240))
    return armar(None, adel, det, ojos='abiertos')

CATEGORIAS = [
    ('Magia', [('Aprendiz de mago', aprendiz_mago), ('Sombrero que habla', sombrero_seleccionador),
               ('Buscador en escoba', buscador_escoba), ('Brujita de pociones', bruja_pociones)]),
    ('Tierra Media', [('Hobbit con el anillo', hobbit), ('El mago gris', mago_gris), ('Elfo arquero', elfo_arquero)]),
    ('Galaxia', [('Caballero espacial', caballero_espacial), ('El lado oscuro', lado_oscuro),
                 ('Maestro verde', maestro_verde), ('Princesa galáctica', princesa_galactica)]),
    ('Marvel', [('Hombre araña', hombre_arana), ('Capitán del escudo', capitan_escudo), ('Dios del trueno', dios_trueno),
                ('Armadura de hierro', armadura_hierro), ('Gigante verde', gigante_verde), ('Hechicero supremo', hechicero_supremo)]),
    ('DC', [('Murciélago', murcielago), ('Kriptoniano', kriptoniano), ('Amazona', amazona),
            ('Velocista', velocista), ('Rey del mar', rey_del_mar), ('Anillo verde', anillo_verde)]),
    ('Fechas especiales', [('San Valentín', san_valentin), ('Pijama', pijama), ('Navidad', navidad), ('Cumpleaños', cumpleanos),
                           ('Fantasmita', fantasmita), ('Año Nuevo', anio_nuevo), ('Conejito de Pascua', conejito)]),
    ('Otros', [('Chef', chef), ('Pirata', pirata), ('Astronauta', astronauta), ('Graduado', graduado),
               ('Vaquero', vaquero), ('Rey', rey), ('Hada', hada), ('Abejita', abejita), ('Marinero', marinero)]),
]

if __name__ == '__main__':
    carpeta = sys.argv[1] if len(sys.argv) > 1 else '.'
    E, COLS = 4, 5
    try:
        f_tit = ImageFont.truetype('arialbd.ttf', 30); f_nom = ImageFont.truetype('arialbd.ttf', 17)
    except OSError:
        f_tit = f_nom = ImageFont.load_default()
    n = 0
    for cat, lista in CATEGORIAS:
        filas = (len(lista) + COLS - 1) // COLS
        cw, ch = CW * E, CH * E + 30
        hoja = Image.new('RGB', (cw * min(COLS, len(lista)), 54 + ch * filas), (250, 242, 232))
        dh = ImageDraw.Draw(hoja)
        dh.text((14, 10), cat, fill=(120, 30, 50), font=f_tit)
        for i, (nombre, fn) in enumerate(lista):
            n += 1
            x0, y0 = (i % COLS) * cw, 54 + (i // COLS) * ch
            dh.rounded_rectangle([x0 + 5, y0 + 2, x0 + cw - 5, y0 + ch - 6], radius=14, fill=(255, 251, 246), outline=(232, 214, 204))
            im = fn().resize((CW * E, CH * E), Image.NEAREST)
            hoja.paste(im, (x0, y0), im)
            et = f'{n}. {nombre}'
            w = dh.textlength(et, font=f_nom)
            dh.text((x0 + (cw - w) / 2, y0 + CH * E - 2), et, fill=(120, 30, 50), font=f_nom)
        nombre_arch = cat.lower().replace(' ', '_').replace('á', 'a').replace('é', 'e').replace('í', 'i')
        hoja.save(os.path.join(carpeta, f'disfraces_{nombre_arch}.png'))
    print('ok', n)
