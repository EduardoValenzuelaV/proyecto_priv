"""Escena pixel: Eduardo y Dallana de espaldas, subiendo la rampa hacia la pasarela (mismo punto de vista de la foto),
tomados de la mano: Dallana (suéter rosado) a la izquierda y Eduardo (polerón crema y mochila) a la derecha, del lado de la calle.
A la izquierda, donde en la foto está el estacionamiento, una mini laguna con la mamá pata y sus patitos;
Dallana gira la cabeza y los apunta. La cámara los sigue: las juntas de la rampa y los barrotes avanzan.
Uso: python propuesta/escena_pasarela.py assets/pixel/pasarela   (genera pasarela.gif y pasarela_f0.png)
"""
import sys, math, random, os
from PIL import Image, ImageDraw

OUT = sys.argv[1] if len(sys.argv) > 1 else 'pasarela'
W, H, K, F = 256, 144, 2, 96
TAU = 2 * math.pi

def lerp(a, b, t):
    t = max(0.0, min(1.0, t))
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def figura(im, forma, x, y, col):
    p = im.load()
    for r, fila in enumerate(forma):
        for c, v in enumerate(fila):
            if v == '1' and 0 <= x + c < W and 0 <= y + r < H:
                p[x + c, y + r] = col

def pegar(im, filas, x0, y0, pal):
    p = im.load()
    for y, fila in enumerate(filas):
        for x, ch in enumerate(fila):
            if ch != '.' and 0 <= x0 + x < W and 0 <= y0 + y < H:
                p[x0 + x, y0 + y] = pal[ch]

def espejo(filas):
    ancho = max(len(f) for f in filas)
    return [f.ljust(ancho, '.')[::-1] for f in filas]

def degradado(im, x0, y0, x1, y1, c0, c1, pasos=7):
    p = im.load()
    for y in range(max(0, y0), min(H, y1)):
        nivel = (y - y0) / max(1, (y1 - y0)) * pasos
        a, b = int(nivel), min(pasos, int(nivel) + 1)
        ca, cb = lerp(c0, c1, a / pasos), lerp(c0, c1, b / pasos)
        for x in range(max(0, x0), min(W, x1)):
            umbral = ((x % 2) * 2 + (y % 2)) / 4 + .125
            p[x, y] = cb if nivel - a > umbral else ca

def contorno(S, col):
    px = S.load()
    con = S.copy(); pc = con.load()
    for y in range(S.height):
        for x in range(S.width):
            if px[x, y][3] == 0:
                for (a, b) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    xx, yy = x + a, y + b
                    if 0 <= xx < S.width and 0 <= yy < S.height and px[xx, yy][3] > 0 and px[xx, yy][:3] != col:
                        pc[x, y] = col + (255,)
                        break
    return con

CORAZON = ["0110110", "1111111", "1111111", "0111110", "0011100", "0001000"]

# ---------- paletas ----------
CIELO_A, CIELO_B = (48, 128, 230), (190, 226, 252)
PASTO = [(66, 132, 52), (88, 162, 64), (114, 186, 80), (150, 206, 102)]
CONC = [(128, 128, 136), (164, 164, 172), (196, 196, 202), (226, 226, 230)]
METAL = [(120, 126, 138), (164, 170, 180), (214, 220, 228)]
AGUA = [(46, 116, 184), (70, 150, 214), (104, 182, 234), (156, 214, 246)]
OUTL = (40, 26, 32)
PIEL, PIEL_S = (236, 186, 146), (204, 146, 110)

# ---------- perspectiva (como la foto: la rampa sube derecho hacia la pasarela) ----------
VPY = 60                     # horizonte / punto de fuga
def y_de(z):                 # z = distancia en metros desde la cámara (z=1 al pie de la imagen)
    return VPY + 84 / z
def borde_rampa(y, lado):    # x del borde izquierdo (-1) o derecho (1) de la rampa a la altura y
    t = (y - 62) / (144 - 62)
    return (121 + (82 - 121) * t) if lado < 0 else (135 + (174 - 135) * t)

# ---------- fondo fijo ----------
def cielo(im):
    degradado(im, 0, 0, W, VPY + 4, CIELO_A, CIELO_B)

def fondo_lejano(im):
    d = ImageDraw.Draw(im)
    # edificio blanco con letrero rojo y edificio bajo a la derecha
    d.rectangle([224, 44, W, 64], fill=(246, 246, 248))
    d.rectangle([224, 44, 226, 64], fill=(214, 214, 222))
    d.rectangle([232, 40, W, 50], fill=(212, 44, 56))
    d.rectangle([236, 43, 252, 47], fill=(255, 255, 255))
    for x in range(230, W, 6):
        d.rectangle([x, 54, x + 3, 58], fill=(170, 200, 224))
    d.rectangle([150, 54, 172, 64], fill=(240, 238, 236))
    d.rectangle([174, 56, 196, 64], fill=(226, 228, 232))
    d.rectangle([150, 52, 162, 54], fill=(214, 120, 84))
    # cerros muy lejanos
    pts = [(0, 62)] + [(x, 56 + int(3 * math.sin(x * .05) + 2 * math.sin(x * .13))) for x in range(0, W + 8, 8)] + [(W, 64), (0, 64)]
    d.polygon(pts, fill=(160, 192, 220))
    # palmeras lejanas
    for (x, y, alto) in ((236, 30, 34), (248, 36, 28), (214, 40, 24)):
        for k in range(alto):
            d.point((x + int(1.5 * math.sin(k * .1)), y + k), fill=(120, 96, 70))
        for (dx, dy) in ((-8, 2), (-6, -4), (0, -6), (6, -4), (8, 2), (4, 5), (-4, 5)):
            d.line([x, y, x + dx, y + dy], fill=(48, 112, 56))
            d.point((x + dx, y + dy), fill=(84, 150, 70))

def suelo(im):
    d = ImageDraw.Draw(im)
    degradado(im, 0, VPY + 2, W, H, PASTO[3], PASTO[1], 6)
    p = im.load()
    for y in range(VPY + 2, H):
        for x in range(W):
            ang = math.atan2(y - VPY, x - 128)
            if int(ang * 18) % 2 == 0 and (x + y) % 2 == 0:
                p[x, y] = lerp(p[x, y], PASTO[0], .18)
    # calle a la derecha que se pierde hacia la pasarela
    d.polygon([(150, 63), (W, 70), (W, 86), (146, 64)], fill=(118, 122, 130))
    d.line([(146, 64), (W, 86)], fill=(150, 154, 160))
    for k in range(6):
        t = k / 6
        x0 = 156 + t * 90
        d.line([x0, 66 + t * 10, x0 + 6 + t * 6, 67 + t * 10], fill=(236, 236, 236))
    # reja baja entre el pasto y la calle
    for x in range(146, W, 3):
        y = 64 + (x - 146) * .2
        d.line([x, y + 1, x, y + 3 + (x - 146) * .03], fill=(150, 152, 160))
    # vereda de la izquierda que sube en paralelo a la rampa
    d.polygon([(0, 132), (52, 144), (106, 64), (101, 64)], fill=(214, 200, 176))
    d.line([(52, 144), (106, 64)], fill=(190, 176, 152))
    d.line([(0, 132), (101, 64)], fill=(196, 182, 158))

def arbol(im, x, y, r, semilla, tronco_hasta):
    d = ImageDraw.Draw(im)
    tono = [(32, 78, 38), (48, 106, 48), (68, 136, 58), (100, 166, 74), (144, 198, 98)]
    d.polygon([(x - 4, tronco_hasta), (x + 4, tronco_hasta), (x + 2, y), (x - 2, y)], fill=(104, 78, 56))
    d.line([x + 2, y + 6, x + 3, tronco_hasta], fill=(76, 56, 40))
    d.line([x - 2, y + 10, x - 2, tronco_hasta], fill=(132, 100, 72))
    d.line([x - 1, y + 4, x - 12, y - 10], fill=(104, 78, 56), width=2)
    d.line([x + 1, y + 2, x + 12, y - 8], fill=(104, 78, 56), width=2)
    rx, ry = r, int(r * .8)
    cy = y - ry // 2
    d.ellipse([x - rx, cy - ry, x + rx, cy + ry], fill=tono[0])
    random.seed(semilla)
    racimos = []
    for _ in range(int(r * 2.4)):
        a, rr = random.uniform(0, TAU), random.uniform(0, 1) ** .6
        racimos.append((cy + math.sin(a) * ry * rr * .9, x + math.cos(a) * rx * rr * .9, random.randint(4, 8)))
    for (py, px, rr) in sorted(racimos, reverse=True):
        luz = ((x - px) / rx + (cy - py) / ry) / 2
        k = 1 if luz < -.35 else 2 if luz < .05 else 3
        d.ellipse([px - rr, py - rr + 1, px + rr, py + rr + 1], fill=tono[k - 1])
        d.ellipse([px - rr, py - rr, px + rr, py + rr - 1], fill=tono[k])
        if k == 3:
            d.ellipse([px - rr + 1, py - rr, px + 1, py - 1], fill=tono[4])
    p = im.load()
    for _ in range(int(r * .9)):
        a, rr = random.uniform(0, TAU), random.uniform(.3, .85)
        hx, hy = int(x + math.cos(a) * rx * rr), int(cy + math.sin(a) * ry * rr)
        if 0 <= hx < W and 0 <= hy < H:
            p[hx, hy] = lerp(CIELO_B, (120, 170, 220), .4)

def pasarela(im):
    d = ImageDraw.Draw(im)
    top, deck = 40, 58
    # pilares
    for px in (150, 196):
        d.rectangle([px - 2, deck + 4, px + 2, 68], fill=CONC[1])
        d.line([px - 2, deck + 4, px - 2, 68], fill=CONC[3])
    d.rectangle([126, top - 2, 214, top + 1], fill=(126, 134, 146))
    d.rectangle([126, top + 2, 214, deck - 1], fill=(200, 224, 240))
    for x in range(126, 214, 10):
        d.line([x + 2, top + 3, x + 7, deck - 2], fill=(228, 242, 252))
    for x in range(126, 214, 10):
        d.line([x, top + 2, x + 10, deck - 1], fill=(132, 142, 156))
        d.line([x + 10, top + 2, x, deck - 1], fill=(132, 142, 156))
        d.line([x, top + 2, x, deck - 1], fill=(116, 124, 136))
    d.rectangle([126, deck - 1, 214, deck + 4], fill=CONC[1])
    d.line([126, deck - 1, 214, deck - 1], fill=CONC[3])
    # letrero con corazón
    d.rectangle([176, top + 3, 206, deck - 3], fill=(253, 248, 249), outline=(196, 58, 78))
    figura(im, CORAZON, 188, top + 6, (224, 48, 70))
    figura(im, ["010", "111", "010"], 180, top + 8, (255, 196, 80))
    figura(im, ["010", "111", "010"], 199, top + 6, (255, 196, 80))
    # caseta de entrada (donde termina la rampa) y torre de ladrillo al otro lado
    d.rectangle([118, top - 4, 128, 64], fill=(160, 96, 70))
    d.rectangle([118, top - 6, 128, top - 4], fill=(128, 74, 52))
    d.rectangle([121, 52, 125, 62], fill=(70, 60, 64))
    d.rectangle([212, 30, 226, 68], fill=(180, 96, 68))
    d.rectangle([222, 30, 226, 68], fill=(146, 76, 54))
    for yy in range(33, 68, 3):
        d.line([212, yy, 226, yy], fill=(158, 84, 60))
    d.rectangle([214, 36, 219, 52], fill=(126, 138, 158))
    # escalera de la torre (diagonal)
    d.line([(214, 68), (226, 58)], fill=METAL[0], width=2)

def poste(im):
    d = ImageDraw.Draw(im)
    x = 76
    d.rectangle([x, 0, x + 3, 120], fill=(222, 224, 228))
    d.line([x + 3, 0, x + 3, 120], fill=(176, 178, 184))
    d.line([x, 0, x, 120], fill=(244, 244, 246))
    for yy in (40, 41, 80, 81):
        d.line([x, yy, x + 3, yy], fill=(190, 192, 198))
    d.rectangle([x - 1, 118, x + 4, 122], fill=(170, 172, 178))

def rampa_base(im):
    d = ImageDraw.Draw(im)
    pts = [(borde_rampa(62, -1), 62), (borde_rampa(62, 1), 62), (borde_rampa(144, 1), 144), (borde_rampa(144, -1), 144)]
    d.polygon(pts, fill=CONC[2])
    # más clara al centro (gastada) y luz del sol
    p = im.load()
    for y in range(62, H):
        xl, xr = borde_rampa(y, -1), borde_rampa(y, 1)
        for x in range(int(xl) + 1, int(xr)):
            t = (x - xl) / max(1, xr - xl)
            if .3 < t < .62 and (x + y) % 2 == 0:
                p[x, y] = CONC[3]
            elif t > .85:
                p[x, y] = lerp(CONC[2], CONC[1], .6)
    # sombra de la baranda izquierda en diagonal sobre la rampa (sol desde la izquierda)
    for y in range(66, H):
        xl = borde_rampa(y, -1)
        ancho = (y - 60) * .22
        for x in range(int(xl) + 1, int(xl + ancho)):
            if (x + y) % 2 == 0:
                p[x, y] = lerp(p[x, y], CONC[0], .5)
    # muros laterales del terraplén
    d.polygon([(borde_rampa(62, -1), 62), (borde_rampa(144, -1), 144), (borde_rampa(144, -1) - 6, 144), (borde_rampa(62, -1) - 1, 63)], fill=CONC[1])
    d.polygon([(borde_rampa(62, 1), 62), (borde_rampa(144, 1), 144), (borde_rampa(144, 1) + 8, 144), (borde_rampa(62, 1) + 1, 63)], fill=CONC[0])

def laguna_base(im):
    d = ImageDraw.Draw(im)
    cx, cy, rx, ry = LAG
    d.ellipse([cx - rx - 6, cy - ry - 3, cx + rx + 6, cy + ry + 5], fill=(198, 184, 150))
    d.ellipse([cx - rx - 2, cy - ry - 1, cx + rx + 2, cy + ry + 2], fill=PASTO[0])
    random.seed(8)
    for k in range(18):
        a = k / 18 * TAU
        sx, sy = cx + int(math.cos(a) * (rx + 4)), cy + int(math.sin(a) * (ry + 2))
        c = random.choice([(168, 168, 176), (192, 192, 198), (150, 152, 160)])
        d.ellipse([sx - 3, sy - 2, sx + 3, sy + 2], fill=c)
        d.point((sx - 1, sy - 1), fill=(222, 222, 228))

LAG = (36, 78, 30, 8)      # mini laguna a la izquierda, donde estaba el estacionamiento
def dentro(x, y):
    cx, cy, rx, ry = LAG
    return ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1

def flores(im):
    d = ImageDraw.Draw(im)
    random.seed(21)
    for _ in range(40):
        x = random.randint(0, W - 1)
        y = random.randint(76, H - 2)
        if borde_rampa(y, -1) - 8 < x < borde_rampa(y, 1) + 10 or dentro(x, y):
            continue
        tam = 1 if y < 100 else 2
        c = random.choice([(255, 255, 255), (255, 236, 110), (255, 190, 210)])
        if tam == 1:
            d.point((x, y), fill=c)
        else:
            d.point([(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)], fill=c)
            d.point((x, y), fill=(255, 206, 60))
    for _ in range(60):
        x, y = random.randint(0, W - 3), random.randint(80, H - 2)
        if borde_rampa(y, -1) - 8 < x < borde_rampa(y, 1) + 10 or dentro(x, y):
            continue
        d.point([(x, y), (x + 1, y - 1), (x + 2, y)], fill=PASTO[0])

BASE = Image.new('RGB', (W, H))
cielo(BASE)
fondo_lejano(BASE)
suelo(BASE)
pasarela(BASE)
laguna_base(BASE)
arbol(BASE, 92, 44, 15, 2, 68)
flores(BASE)
rampa_base(BASE)
# el árbol grande y el poste van en una capa aparte: se pegan al final, delante de la laguna y los patos
CLAVE = (255, 0, 255)
FRENTE = Image.new('RGB', (W, H), CLAVE)
arbol(FRENTE, 18, 46, 30, 1, 118)
poste(FRENTE)
MASCARA_FRENTE = Image.new('L', (W, H), 0)
_fp, _mp = FRENTE.load(), MASCARA_FRENTE.load()
for _y in range(H):
    for _x in range(W):
        if _fp[_x, _y] != CLAVE:
            _mp[_x, _y] = 255
BASE.paste(FRENTE, (0, 0), MASCARA_FRENTE)

# ---------- patitos ----------
PAT = {'W': (252, 252, 246), 'w': (214, 218, 226), 'g': (186, 192, 204), 'O': (255, 150, 40), 'E': (30, 24, 28),
       'Y': (255, 224, 72), 'y': (232, 182, 38), 'o': (86, 68, 60), 'b': (255, 255, 255)}
MAMA = [
    ".......ooo...",
    "......oWWWo..",
    "......oWbEWOO",
    ".o....oWWWOOo",
    "oWo...oWWWo..",
    "oWWo..oWWWo..",
    "oWWWooWWWWWo.",
    ".oWWWWWgWWWWo",
    ".owWWggWWWWwo",
    "..owwwwwwwwo.",
    "...ooooooo...",
]
MAMA_ALETEA = MAMA[:4] + ["oWo.oWWWWWo..", "oWWoWWwWWWo..", "oWWWWwwWWWWo."] + MAMA[7:]
PATITO = [
    "...ooo.",
    "..oYYYo",
    "..oYbEOO",
    "o.oYYYo.",
    "YooYYYYo",
    "oYYYYYYo",
    ".oyyyyo.",
    "..oooo..",
]
PATITO_BUCEA = ["........", "........", "...o....", "..oYo...", "..oYYo..", ".oYYYYo.", ".oyyyyo.", "..oooo.."]
RANA = {'G': (96, 178, 72), 'g': (62, 134, 52), 'E': (30, 30, 30), 'w': (240, 250, 230)}
RANA_SPR = [".wE..Ew.", ".GGGGGG.", "GGgGGgGG", "gGGGGGGg", ".g....g."]
HOJA = ["..1111..", ".111111.", "11111111", "1111.111", ".11..11."]
PAJARO = [["1...1", ".1.1.", "..1.."], [".....", "11111", "..1.."]]
MARIPOSA = [["1.1", "111", "1.1"], [".1.", "111", ".1."]]
LETRAS = {'C': ["111", "100", "100", "100", "111"], 'U': ["101", "101", "101", "101", "111"],
          'A': ["010", "101", "111", "101", "101"], '!': ["1", "1", "1", "0", "1"]}

def anillo(im, x, y, t):
    if not 0 <= t < 1:
        return
    d = ImageDraw.Draw(im)
    rx, ry = 2 + t * 9, 1 + t * 3
    d.ellipse([x - rx, y - ry, x + rx, y + ry], outline=lerp(AGUA[3], AGUA[2], t))

def agua(im, f):
    cx, cy, rx, ry = LAG
    p = im.load()
    for y in range(cy - ry, cy + ry + 1):
        for x in range(cx - rx, cx + rx + 1):
            if not dentro(x, y):
                continue
            # refleja el cielo: más claro al fondo, más hondo cerca
            t = (y - (cy - ry)) / (2 * ry)
            col = lerp(lerp(CIELO_B, AGUA[2], .55), AGUA[1], t)
            onda = math.sin(x * .35 + y * 1.3 - f / F * TAU * 4)
            if onda > .82:
                col = lerp(col, AGUA[3], .6)
            if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 > .78:
                col = lerp(col, AGUA[0], .35)
            p[x, y] = col
    # reflejo de la pasarela no se ve desde aquí; reflejo de la nube que pasa
    d = ImageDraw.Draw(im)
    random.seed(9)
    for k in range(12):
        bx = cx - rx + 8 + random.randint(0, 2 * rx - 16)
        by = cy - ry + 3 + random.randint(0, 2 * ry - 6)
        if (f // 3 + k * 5) % 8 < 3:
            d.line([bx, by, bx + 2, by], fill=(236, 248, 255))

def nenufares(im):
    d = ImageDraw.Draw(im)
    cx, cy, rx, ry = LAG
    for (dx, dy, flor) in ((-24, -3, True), (-16, 2, False), (18, -4, True), (8, 3, False)):
        x, y = cx + dx, cy + dy
        figura(im, ["..111..", ".11111.", "1111.11", ".11.11."], x, y, (62, 140, 62))
        figura(im, ["11.", ".11"], x + 2, y + 1, (96, 170, 80))
        if flor:
            d.point([(x + 2, y), (x + 3, y - 1), (x + 4, y), (x + 3, y)], fill=(255, 150, 190))
            d.point((x + 3, y), fill=(255, 220, 90))

def juncos(im, f):
    d = ImageDraw.Draw(im)
    cx, cy, rx, ry = LAG
    for k in range(6):
        jx = cx + rx - 3 + k * 3
        alto = 8 + (k * 5) % 6
        sway = round(1.5 * math.sin(f / F * TAU * 2 + k * .7))
        d.line([jx, cy + 2, jx + sway, cy + 2 - alto], fill=(58, 118, 50))
        d.line([jx + 1, cy + 2, jx + 1 + sway // 2, cy + 5 - alto], fill=(84, 150, 64))
        if k % 2 == 0:
            d.rectangle([jx + sway - 1, cy + 2 - alto, jx + sway, cy + 5 - alto], fill=(128, 82, 50))

def rana(im, f):
    x0, y0 = LAG[0] + 16, LAG[1] - 6
    t = (f % F) / F
    salto = int(8 * math.sin((t - .55) / .12 * math.pi)) if .55 < t < .67 else 0
    pegar(im, RANA_SPR, x0, y0 - salto, RANA)
    if .66 <= t < .8:
        anillo(im, x0 + 4, y0 + 5, (t - .66) / .14)

def pez(im, f):
    t = (f % F) / F
    x0, y0 = LAG[0] - 14, LAG[1] + 2
    if .2 <= t < .32:
        u = (t - .2) / .12
        x, y = x0 + int(u * 12), y0 - int(10 * math.sin(u * math.pi))
        figura(im, ["0110", "1111", "0110"] if u < .5 else ["0110", "1111", "1001"], x, y, (255, 128, 40))
    if .2 <= t < .3:
        anillo(im, x0, y0 + 2, (t - .2) / .1)
    if .31 <= t < .45:
        anillo(im, x0 + 12, y0 + 2, (t - .31) / .14)

def patos(im, f):
    cx, cy, rx, ry = LAG
    base = f / F * TAU
    lista = []
    for k in range(4):
        a = base - (k * .55 + (.3 if k else 0))
        lista.append((cy + math.sin(a) * (ry - 3), cx + math.cos(a) * (rx - 10), k, -math.sin(a) > 0))
    d = ImageDraw.Draw(im)
    for (y, x, k, der) in sorted(lista):
        if k == 0:
            spr = MAMA_ALETEA if (f % 48) in (30, 31, 32, 33) else MAMA
        else:
            spr = PATITO_BUCEA if (k == 2 and 60 <= f % F < 70) else PATITO
        spr = spr if der else espejo(spr)
        alto, ancho = len(spr), max(len(r) for r in spr)
        bob = 1 if (f // 4 + k) % 2 else 0
        x0, y0 = int(x - ancho / 2), int(y - alto + 4 + bob)
        s = -1 if der else 1
        cola = x0 + (0 if der else ancho)
        d.line([cola, y0 + alto - 2, cola + s * 6, y0 + alto], fill=AGUA[3])
        d.line([cola, y0 + alto - 1, cola + s * 5, y0 + alto + 2], fill=AGUA[3])
        pegar(im, spr, x0, y0, PAT)
        d.line([x0 + 1, y0 + alto - 2, x0 + ancho - 2, y0 + alto - 2], fill=AGUA[2])
        if k == 2 and 66 <= f % F < 76:
            anillo(im, x0 + ancho // 2, y0 + alto - 1, (f % F - 66) / 10)
    return lista

def cuac(im, f, lista):
    if (f % 48) >= 10:
        return
    y, x, _, _ = [e for e in lista if e[2] == 0][0]
    d = ImageDraw.Draw(im)
    mx = max(2, min(W - 30, int(x) - 12))
    my = int(y) - 22
    d.rounded_rectangle([mx, my - 8, mx + 26, my + 2], radius=3, fill=(255, 255, 255), outline=(70, 70, 80))
    d.polygon([(mx + 11, my + 2), (mx + 15, my + 2), (mx + 13, my + 5)], fill=(255, 255, 255))
    d.line([mx + 11, my + 2, mx + 13, my + 5], fill=(70, 70, 80)); d.line([mx + 13, my + 5, mx + 15, my + 2], fill=(70, 70, 80))
    xx = mx + 3
    for ch in "CUAC!":
        figura(im, LETRAS[ch], xx, my - 6, (70, 70, 80))
        xx += len(LETRAS[ch][0]) + 1

# ---------- lo que se mueve con la cámara: juntas de la rampa y barrotes ----------
def juntas_y_barandas(im, f):
    d = ImageDraw.Draw(im)
    avance = (f % F) / F * 2            # la cámara avanza 2 m por vuelta (múltiplo del paso de las juntas)
    # juntas de dilatación cada 1 m
    for k in range(1, 40):
        z = k - avance % 1
        if z < 1:
            continue
        y = y_de(z)
        if y < 63:
            break
        xl, xr = borde_rampa(y, -1), borde_rampa(y, 1)
        d.line([xl + 1, y, xr - 1, y], fill=lerp(CONC[1], CONC[2], min(1, (z - 1) / 8)))
    # barandas a ambos lados: barrotes cada 0,5 m, pasamanos arriba
    for lado in (-1, 1):
        puntos_arriba = []
        for k in range(1, 80):
            z = k * .5 - (avance % .5)
            if z < .9:
                continue
            y = y_de(z)
            if y < 62:
                break
            x = borde_rampa(y, lado) + (-1 if lado < 0 else 1)
            alto = 40 / z
            col = lerp(METAL[1], METAL[0], .3) if z < 3 else METAL[1]
            d.line([x, y, x, y - alto], fill=col, width=2 if z < 1.6 else 1)
            puntos_arriba.append((x, y - alto))
        # pasamanos y travesaño medio (línea continua hacia el punto de fuga)
        y0 = H + 10
        for (frac, col, ancho) in ((1.0, METAL[2], 3), (1.0, METAL[0], 1), (.5, METAL[1], 2)):
            pts = []
            for z in (0.86, 1, 1.5, 2, 3, 5, 8, 14, 30):
                y = y_de(z)
                x = borde_rampa(min(y, 160), lado) + (-1 if lado < 0 else 1)
                pts.append((x, y - 40 / z * frac))
            d.line(pts, fill=col, width=ancho)

# ---------- Eduardo y Dallana de espaldas ----------
NEGRO, NEGRO2, AZUL, AZUL2 = (36, 36, 46), (60, 62, 80), (52, 112, 214), (120, 172, 244)
MORADO, MORADO2, MORADO3 = (128, 78, 190), (92, 52, 148), (170, 128, 226)
JEAN, JEAN2 = (64, 84, 128), (44, 56, 92)
PELO, PELO2, PELO3 = (44, 30, 30), (78, 52, 46), (118, 82, 64)

def piernas(d, cx, paso, jean, jean2, zapato, zapato2):
    """Dos piernas de espalda; al caminar una sube (el pie se levanta y se acorta)."""
    for lado, x0 in ((-1, cx - 6), (1, cx + 1)):
        arriba = (paso == 0 and lado < 0) or (paso == 1 and lado > 0)
        y_fin = 42 if arriba else 45
        d.rectangle([x0, 31, x0 + 5, y_fin], fill=jean)
        d.line([x0 + (5 if lado < 0 else 0), 32, x0 + (5 if lado < 0 else 0), y_fin], fill=jean2)
        d.rectangle([x0 - 1, y_fin - 1, x0 + 6, y_fin + 1], fill=zapato)
        d.line([x0, y_fin + 1, x0 + 5, y_fin + 1], fill=zapato2)
        if arriba:
            d.line([x0 - 1, y_fin - 1, x0 + 6, y_fin - 1], fill=(150, 150, 160))   # suela se ve al levantar

# ropa nueva
CREMA, CREMA_S, CREMA_L = (238, 226, 202), (206, 190, 160), (250, 244, 228)
MOCHILA, MOCHILA_S, MOCHILA_L = (46, 62, 104), (32, 44, 76), (82, 104, 156)
GRIS, GRIS_S = (64, 66, 78), (46, 48, 58)
ROSA, ROSA_S, ROSA_L = (242, 148, 172), (210, 108, 138), (255, 198, 212)
CELESTE, CELESTE_S = (118, 158, 214), (84, 120, 180)
PELO_E, PELO_E2, PELO_E3, PELO_E4 = (40, 28, 26), (66, 46, 38), (104, 74, 58), (80, 60, 52)

class _Desplazado:
    """Envuelve ImageDraw y suma `dy` a todas las coordenadas y."""
    def __init__(self, d, dy):
        self.d, self.dy = d, dy
    def _m(self, xy):
        if xy and isinstance(xy[0], (tuple, list)):
            return [(x, y + self.dy) for (x, y) in xy]
        return [v + (self.dy if k % 2 else 0) for k, v in enumerate(xy)]
    def __getattr__(self, nombre):
        f = getattr(self.d, nombre)
        return lambda xy, *a, **k: f(self._m(list(xy)), *a, **k)

def eduardo(paso):
    """Eduardo de espaldas (a la derecha): un poco más alto que Dallana, hombros anchos,
    polerón crema en 3 tonos con capucha, mochila azul marino con un llaverito de Alejandro,
    pantalón gris y zapatillas blancas. Pelo con coronilla, mechones con dirección, brillo y nuca rebajada."""
    S = Image.new('RGBA', (36, 59), (0, 0, 0, 0))
    d = _Desplazado(ImageDraw.Draw(S), 6)     # 6 px de margen arriba para la coronilla
    cx = 17
    # piernas (más largas) con el paso
    for lado, x0 in ((-1, cx - 7), (1, cx + 1)):
        arriba = (paso == 0 and lado < 0) or (paso == 1 and lado > 0)
        y_fin = 45 if arriba else 48
        d.rectangle([x0, 34, x0 + 6, y_fin], fill=GRIS)
        d.line([x0 + (6 if lado < 0 else 0), 35, x0 + (6 if lado < 0 else 0), y_fin], fill=GRIS_S)
        d.line([x0 + 2, 38, x0 + 2, y_fin - 2], fill=(84, 86, 98))
        d.rectangle([x0 - 1, y_fin - 1, x0 + 7, y_fin + 1], fill=(250, 250, 250))
        d.line([x0, y_fin + 1, x0 + 6, y_fin + 1], fill=(220, 60, 70))
        if arriba:
            d.line([x0 - 1, y_fin - 1, x0 + 7, y_fin - 1], fill=(150, 150, 160))
    # polerón: hombros anchos, 3 tonos (luz desde la izquierda) y pretina tejida
    d.polygon([(cx - 12, 19), (cx - 7, 14), (cx + 7, 14), (cx + 12, 19), (cx + 11, 37), (cx - 11, 37)], fill=CREMA)
    d.polygon([(cx + 5, 15), (cx + 7, 14), (cx + 12, 19), (cx + 11, 35), (cx + 5, 35)], fill=CREMA_S)
    d.polygon([(cx - 11, 20), (cx - 7, 15), (cx - 5, 15), (cx - 9, 21), (cx - 9, 34), (cx - 11, 34)], fill=CREMA_L)
    d.rectangle([cx - 11, 34, cx + 11, 37], fill=CREMA_S)
    for x in range(cx - 10, cx + 11, 2):
        d.line([x, 35, x, 36], fill=(188, 170, 138))
    # brazo derecho colgando, un poco doblado, con puño tejido
    d.polygon([(cx + 11, 18), (cx + 14, 21), (cx + 14, 33), (cx + 11, 33)], fill=CREMA_S)
    d.line([cx + 12, 21, cx + 12, 31], fill=CREMA)
    d.rectangle([cx + 11, 31, cx + 14, 33], fill=(188, 170, 138))
    d.rounded_rectangle([cx + 11, 33, cx + 14, 37], radius=1, fill=PIEL)
    d.point((cx + 14, 36), fill=PIEL_S)
    # brazo izquierdo hacia Dallana
    d.line([(cx - 10, 18), (cx - 15, 30)], fill=CREMA, width=5)
    d.line([(cx - 11, 18), (cx - 16, 28)], fill=CREMA_L)
    d.line([(cx - 17, 30), (cx - 13, 30)], fill=(188, 170, 138), width=2)
    d.rounded_rectangle([cx - 19, 31, cx - 15, 34], radius=1, fill=PIEL)
    # capucha caída sobre la espalda
    d.rounded_rectangle([cx - 8, 11, cx + 8, 21], radius=5, fill=CREMA_S)
    d.arc([cx - 6, 11, cx + 6, 22], 200, 340, fill=(184, 166, 136))
    d.line([cx - 6, 12, cx + 6, 12], fill=CREMA)
    d.point([(cx - 7, 13), (cx + 7, 13)], fill=CREMA)
    # mochila azul marino: tiras, asa, bolsillo, cierre y llaverito de Alejandro
    d.line([cx - 7, 14, cx - 7, 21], fill=MOCHILA_S, width=2)
    d.line([cx + 7, 14, cx + 7, 21], fill=MOCHILA_S, width=2)
    d.rounded_rectangle([cx - 8, 19, cx + 8, 34], radius=4, fill=MOCHILA)
    d.rectangle([cx + 4, 21, cx + 8, 32], fill=MOCHILA_S)
    d.line([cx - 7, 21, cx - 7, 31], fill=MOCHILA_L)
    d.rounded_rectangle([cx - 6, 26, cx + 6, 33], radius=2, fill=MOCHILA_L)
    d.line([cx - 5, 27, cx + 5, 27], fill=(176, 192, 220))
    d.line([cx - 7, 22, cx + 7, 22], fill=MOCHILA_L)
    d.arc([cx - 3, 16, cx + 3, 22], 180, 360, fill=MOCHILA_S)
    d.point((cx + 5, 28), fill=(234, 204, 96))                         # tirador del cierre
    d.line([cx + 5, 29, cx + 5, 30], fill=(200, 200, 210))
    d.rectangle([cx + 4, 31, cx + 6, 32], fill=(226, 56, 60))          # Alejandro chiquitito
    d.point([(cx + 3, 30), (cx + 7, 30)], fill=(226, 56, 60))
    d.point([(cx + 4, 31), (cx + 6, 31)], fill=(255, 255, 255))
    # cuello, orejas y patillas
    d.rectangle([cx - 3, 8, cx + 3, 12], fill=PIEL)
    d.line([cx + 1, 9, cx + 3, 11], fill=PIEL_S)
    d.ellipse([cx - 10, 3, cx - 6, 9], fill=PIEL); d.line([cx - 8, 5, cx - 8, 7], fill=PIEL_S)
    d.ellipse([cx + 6, 3, cx + 10, 9], fill=PIEL); d.line([cx + 8, 5, cx + 8, 7], fill=PIEL_S)
    # pelo: coronilla redonda, mechones con dirección, brillo y nuca rebajada
    d.ellipse([cx - 8, -5, cx + 8, 10], fill=PELO_E)
    d.polygon([(cx - 7, 5), (cx + 7, 5), (cx + 6, 9), (cx + 3, 11), (cx - 3, 11), (cx - 6, 9)], fill=PELO_E)
    for (x, y) in ((cx - 5, -5), (cx - 1, -6), (cx + 3, -6), (cx + 6, -4)):
        d.polygon([(x - 2, y + 3), (x, y), (x + 3, y + 2)], fill=PELO_E)
    # mechones que caen desde la coronilla hacia la nuca
    for (x0, y0, x1, y1) in ((cx, -2, cx - 4, 8), (cx, -2, cx, 9), (cx, -2, cx + 4, 8), (cx - 3, -1, cx - 7, 6), (cx + 3, -1, cx + 7, 6)):
        d.line([x0, y0, x1, y1], fill=PELO_E2)
    d.point([(cx, -2), (cx + 1, -2)], fill=PELO_E4)                      # remolino de la coronilla
    # brillo de pelo sano: una banda curva arriba a la izquierda
    d.arc([cx - 7, -4, cx + 5, 8], 200, 300, fill=PELO_E3)
    d.arc([cx - 6, -3, cx + 4, 8], 210, 280, fill=PELO_E3)
    # nuca y costados rebajados (se aclara hacia abajo)
    d.line([cx - 5, 10, cx + 5, 10], fill=PELO_E4)
    d.point([(cx - 4, 11), (cx - 1, 11), (cx + 2, 11)], fill=PELO_E4)
    d.rectangle([cx - 8, 4, cx - 7, 8], fill=PELO_E4)
    d.rectangle([cx + 7, 4, cx + 8, 8], fill=PELO_E4)
    return contorno(S, OUTL)

def dallana(paso, mira):
    """Dallana de espaldas (a la izquierda): suéter tejido rosado, jeans celestes, bolsita de tela
    con corazón y su pelo crespo largo. Cuando mira, gira la cabeza a la izquierda y apunta a la laguna."""
    S = Image.new('RGBA', (36, 50), (0, 0, 0, 0))
    d = ImageDraw.Draw(S)
    cx = 19
    piernas(d, cx, paso, CELESTE, CELESTE_S, (250, 250, 250), (255, 150, 180))
    # suéter tejido rosado
    d.rounded_rectangle([cx - 9, 15, cx + 9, 34], radius=4, fill=ROSA)
    d.rectangle([cx + 4, 16, cx + 9, 32], fill=ROSA_S)
    d.rectangle([cx - 8, 17, cx - 7, 31], fill=ROSA_L)
    for x in range(cx - 7, cx + 9, 3):
        for y in range(18, 31, 2):
            d.point((x, y), fill=ROSA_S if x < cx + 4 else (186, 90, 118))
    d.rectangle([cx - 9, 31, cx + 9, 34], fill=ROSA_S)
    for x in range(cx - 8, cx + 9, 2):
        d.point((x, 32), fill=(186, 90, 118))
    # bolsita de tela colgando del hombro derecho, con un corazón
    d.line([(cx + 5, 16), (cx + 10, 25)], fill=(196, 176, 140))
    d.rounded_rectangle([cx + 7, 24, cx + 14, 32], radius=1, fill=(244, 234, 210))
    d.line([cx + 7, 31, cx + 14, 31], fill=(214, 200, 168))
    d.point([(cx + 9, 26), (cx + 11, 26), (cx + 9, 27), (cx + 10, 27), (cx + 11, 27), (cx + 10, 28)], fill=(224, 48, 70))
    # brazo derecho hacia Eduardo (manos juntas)
    d.line([(cx + 7, 18), (cx + 13, 28)], fill=ROSA_S, width=4)
    d.line([(cx + 12, 27), (cx + 15, 27)], fill=ROSA_L)
    d.rectangle([cx + 12, 28, cx + 16, 31], fill=PIEL)
    if not mira:
        d.rectangle([cx - 12, 17, cx - 9, 30], fill=ROSA)
        d.line([cx - 11, 18, cx - 11, 29], fill=ROSA_L)
        d.rectangle([cx - 12, 30, cx - 9, 33], fill=PIEL)
    # pelo crespo largo: volumen, rulitos, brillo arriba a la izquierda
    g = -1 if mira else 0
    d.ellipse([cx - 10 + g, -1, cx + 10 + g, 27], fill=PELO)
    for (x, y, r) in ((cx - 10, 5, 3), (cx - 11, 12, 3), (cx - 11, 19, 3), (cx - 8, 25, 3), (cx + 10, 5, 3), (cx + 11, 12, 3),
                      (cx + 11, 19, 3), (cx + 8, 25, 3), (cx - 5, -1, 3), (cx + 4, -1, 3), (cx, 27, 3), (cx - 4, 27, 2), (cx + 4, 27, 2)):
        d.ellipse([x - r + g, y - r, x + r + g, y + r], fill=PELO)
    for gy in range(1, 27, 3):
        for gx in range(cx - 9, cx + 10, 3):
            x = gx + (gy // 3) % 2 + g
            claro = (x - cx) + (gy - 8) < -6
            d.arc([x - 1, gy - 1, x + 1, gy + 1], 160, 380, fill=PELO3 if claro else PELO2)
    d.rectangle([cx + 4 + g, 3, cx + 7 + g, 4], fill=(255, 120, 160))      # pinche con corazoncito
    d.point((cx + 5 + g, 2), fill=(255, 170, 200))
    if mira:
        d.ellipse([cx - 13, 4, cx - 5, 13], fill=PIEL)
        d.point((cx - 14, 9), fill=PIEL)
        d.rectangle([cx - 13, 7, cx - 8, 9], fill=(200, 32, 50))
        d.rectangle([cx - 12, 8, cx - 10, 8], fill=(226, 240, 250))
        d.point([(cx - 10, 11), (cx - 9, 11)], fill=(244, 138, 140))
        d.ellipse([cx - 8, 0, cx - 2, 11], fill=PELO)
        d.arc([cx - 7, 2, cx - 3, 6], 160, 380, fill=PELO2)
        # brazo estirado apuntando a la laguna (encima del pelo)
        d.line([(cx - 6, 19), (cx - 16, 10)], fill=ROSA_S, width=5)
        d.line([(cx - 6, 18), (cx - 16, 9)], fill=ROSA, width=3)
        d.line([(cx - 7, 17), (cx - 15, 9)], fill=ROSA_L)
        d.line([(cx - 17, 8), (cx - 15, 11)], fill=(186, 90, 118), width=2)
        d.rectangle([cx - 20, 6, cx - 17, 9], fill=PIEL)
        d.line([(cx - 21, 6), (cx - 23, 4)], fill=PIEL)
        d.point((cx - 18, 9), fill=PIEL_S)
    else:
        d.point([(cx - 11, 8), (cx + 10, 8)], fill=(200, 32, 50))
    return contorno(S, OUTL)

def pareja(im, f):
    paso = (f // 6) % 2
    bob = 1 if f % 6 in (2, 3) else 0
    mira = 18 <= f % F < 74
    dx, dy = 92, 92 - bob           # Dallana a la izquierda
    ex, ey = dx + 34, 82 - bob      # Eduardo a la derecha (del lado de la calle), un poco más alto
    d = ImageDraw.Draw(im)
    p = im.load()
    for (sx, sy, an) in ((dx + 19, 140, 10), (ex + 17, 139, 11)):
        for yy in range(sy - 2, sy + 2):
            for xx in range(sx - an, sx + an):
                if ((xx - sx) / an) ** 2 + ((yy - sy) / 2) ** 2 <= 1 and (xx + yy) % 2 == 0:
                    p[xx, yy] = lerp(p[xx, yy], CONC[0], .7)
    se = eduardo(1 - paso)
    sd = dallana(paso, mira)
    im.paste(se, (ex, ey), se)
    im.paste(sd, (dx, dy), sd)
    # globito de Dallana: patito y corazón, hacia la laguna
    if mira and 24 <= f % F < 70:
        bx, by = dx - 14, dy - 24
        d.rounded_rectangle([bx, by, bx + 28, by + 14], radius=4, fill=(255, 255, 255), outline=(70, 70, 80))
        d.polygon([(bx + 19, by + 14), (bx + 24, by + 14), (bx + 25, by + 19)], fill=(255, 255, 255))
        d.line([bx + 19, by + 14, bx + 25, by + 19], fill=(70, 70, 80)); d.line([bx + 25, by + 19, bx + 24, by + 14], fill=(70, 70, 80))
        pegar(im, espejo(PATITO), bx + 3, by + 3, PAT)
        figura(im, CORAZON, bx + 16, by + 4, (224, 48, 70) if (f // 4) % 2 else (240, 90, 110))
    # corazones que suben desde las manos juntas
    for k in range(2):
        t = ((f + k * 12) % 24) / 24
        hx = dx + 29 + k * 4 + int(2 * math.sin(t * TAU + k))
        hy = int(dy + 26 - t * 30)
        if t < .8:
            figura(im, CORAZON, hx, hy, (255, 110, 140) if k == 0 else (255, 160, 190))

# ---------- vida alrededor ----------
def nubes(im, f):
    p = im.load()
    desp = f
    trazos = [(10, 8, 30), (52, 18, 22), (78, 4, 18)]
    for rep in range(-1, W // 96 + 2):
        for (tx, ty, largo) in trazos:
            x0 = rep * 96 + tx + desp
            for i in range(largo):
                x, y = x0 + i, ty + int(1.5 * math.sin(i * .2))
                if 0 <= x < W and 0 <= y < VPY:
                    p[x, y] = lerp(p[x, y], (250, 252, 255), .55 if 3 < i < largo - 3 else .25)
                    if i % 3 and y + 1 < VPY:
                        p[x, y + 1] = lerp(p[x, y + 1], (250, 252, 255), .25)

def pajaros(im, f):
    for k in range(3):
        t = ((f + k * 13) % F) / F
        x = int(W + 10 - t * (W + 40)) + k * 9
        y = 14 + k * 6 + int(3 * math.sin(t * TAU * 3 + k))
        figura(im, PAJARO[(f // 3 + k) % 2], x, y, (70, 80, 100))

def gente(im, f):
    d = ImageDraw.Draw(im)
    # alguien cruza la pasarela por dentro
    x = int(130 + (f % F) / F * 80)
    paso = (f // 3) % 2
    d.rectangle([x, 47, x + 2, 52], fill=(80, 90, 120))
    d.rectangle([x, 45, x + 2, 46], fill=PIEL)
    d.line([x + paso, 53, x + paso, 56], fill=(50, 56, 80)); d.line([x + 2 - paso, 53, x + 2 - paso, 56], fill=(50, 56, 80))
    # dos personas bajan por la vereda a lo lejos
    for k, col in enumerate(((60, 90, 150), (180, 60, 70))):
        t = ((f + k * 48) % F) / F
        z = 7 - t * 3
        y = int(y_de(z))
        xx = int(103 - (y - 64) * .62) - 2 + k * 3
        alto = max(4, int(18 / z))
        d.rectangle([xx, y - alto, xx + max(1, alto // 4), y - alto // 3], fill=col)
        d.point((xx, y - alto - 1), fill=PIEL)
        d.line([xx, y - alto // 3, xx, y], fill=(50, 56, 80))

def autos(im, f):
    d = ImageDraw.Draw(im)
    for k, (col, vel) in enumerate((((244, 244, 248), 1), ((214, 56, 60), 2))):
        t = ((f * vel) % F) / F
        x = int(160 + t * 110)
        y = int(65 + (x - 150) * .1) + k * 3
        largo = 5 + int((x - 150) * .08)
        if x < W:
            d.rounded_rectangle([x, y - 2, x + largo, y + 1], radius=1, fill=col)
            d.line([x + 1, y - 2, x + largo - 1, y - 2], fill=(150, 190, 220))

def hojas_que_caen(im, f):
    for k in range(5):
        t = ((f + k * 19) % F) / F
        x = 6 + k * 12 + int(8 * math.sin(t * TAU * 2 + k))
        y = 30 + int(t * 100)
        figura(im, ["11", "1."] if (f // 4 + k) % 2 else [".1", "11"], x, y, (176, 196, 72) if k % 2 else (226, 170, 60))

def mariposas(im, f):
    for k, (bx, by, col) in enumerate(((52, 70, (255, 236, 120)), (210, 112, (255, 255, 255)))):
        t = f / F * TAU + k
        x = int(bx + 16 * math.sin(t) + 5 * math.sin(t * 3))
        y = int(by + 6 * math.sin(t * 2))
        figura(im, MARIPOSA[(f // 2 + k) % 2], x, y, col)
        figura(im, ["1"], x + 1, y + 1, (90, 70, 50))

def destellos(im, f):
    p = im.load()
    for k in range(7):
        t = ((f + k * 14) % F) / F
        x, y = int(10 + k * 8 + 6 * math.sin(t * TAU + k)), int(20 + t * 60)
        if 0 <= x < W and t < .8:
            p[x, y] = lerp(p[x, y], (255, 250, 220), .85)

frames = []
for f in range(F):
    im = BASE.copy()
    nubes(im, f)
    pajaros(im, f)
    autos(im, f)
    # la pasarela, la torre y los árboles van delante de nubes y autos
    for (x0, y0, x1, y1) in ((116, 26, 228, 70),):
        im.paste(BASE.crop((x0, y0, x1, y1)), (x0, y0))
    gente(im, f)
    agua(im, f)
    nenufares(im)
    pez(im, f)
    lista = patos(im, f)
    rana(im, f)
    juncos(im, f)
    juntas_y_barandas(im, f)
    pareja(im, f)
    # árbol grande y poste en primer plano, delante de la laguna y los patos
    im.paste(FRENTE, (0, 0), MASCARA_FRENTE)
    hojas_que_caen(im, f)
    mariposas(im, f)
    destellos(im, f)
    cuac(im, f, lista)
    frames.append(im.resize((W * K, H * K), Image.NEAREST))

# paleta común de 128 colores para todos los cuadros: el GIF pesa la mitad sin perder calidad
muestra = Image.new('RGB', (frames[0].width, frames[0].height * 4))
for k, i in enumerate((0, 24, 48, 72)):
    muestra.paste(frames[i], (0, frames[0].height * k))
paleta = muestra.quantize(colors=128, method=Image.Quantize.MEDIANCUT)
cuadros = [fr.quantize(palette=paleta, dither=Image.Dither.NONE) for fr in frames]
cuadros[0].save(OUT + '.gif', save_all=True, append_images=cuadros[1:], duration=90, loop=0, optimize=True, disposal=1)
frames[0].save(OUT + '_f0.png')
print('ok')
