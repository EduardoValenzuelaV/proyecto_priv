"""Escena pixel (segunda): Eduardo y Dallana de espaldas, ya más arriba en la rampa, con la pasarela más cerca.
Eduardo (polerón blanco, blue jeans y zapatillas blancas) a la derecha, del lado de la calle;
Dallana (blusa celeste y pantalón crema) a la izquierda. Por la vereda de la izquierda camina gente.
Eduardo le pregunta: "¿Las parejas deberían parecerse o ser distintas para que la relación funcione?" y ella lo mira con corazones.
Uso: python propuesta/escena_pasarela2.py assets/pixel/pasarela2   (genera pasarela2.gif y pasarela2_f0.png)
"""
import sys, math, random, os
from PIL import Image, ImageDraw

OUT = sys.argv[1] if len(sys.argv) > 1 else 'pasarela'
W, H, K, F = 256, 144, 2, 120
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

class _Escala:
    """Envuelve ImageDraw y agranda todo `s` veces alrededor de (ox, oy): la pasarela se ve más cerca."""
    def __init__(self, d, s, ox, oy):
        self.d, self.s, self.ox, self.oy = d, s, ox, oy
    def p(self, x, y):
        return (round(self.ox + (x - self.ox) * self.s), round(self.oy + (y - self.oy) * self.s))
    def _m(self, xy):
        if xy and isinstance(xy[0], (tuple, list)):
            return [self.p(x, y) for (x, y) in xy]
        out = []
        for k in range(0, len(xy), 2):
            out += self.p(xy[k], xy[k + 1])
        return out
    def __getattr__(self, nombre):
        f = getattr(self.d, nombre)
        return lambda xy, *a, **k: f(self._m(list(xy)), *a, **k)

def figura2(im, forma, x, y, col):
    p = im.load()
    for r, fila in enumerate(forma):
        for c, v in enumerate(fila):
            if v == '1':
                for a in (0, 1):
                    for b in (0, 1):
                        if 0 <= x + 2 * c + a < W and 0 <= y + 2 * r + b < H:
                            p[x + 2 * c + a, y + 2 * r + b] = col

def pasarela(im):
    """La pasarela ya cerca: vidrios con reflejo, enrejado grueso, letrero con corazón y la caseta de ladrillo."""
    d = _Escala(ImageDraw.Draw(im), 1.5, 128, 64)
    top, deck = 40, 58
    for px in (150, 196):
        d.rectangle([px - 2, deck + 4, px + 2, 68], fill=CONC[1])
        d.line([px - 2, deck + 4, px - 2, 68], fill=CONC[3])
        d.line([px + 2, deck + 4, px + 2, 68], fill=CONC[0])
    d.rectangle([126, top - 2, 214, top + 1], fill=(126, 134, 146))
    d.line([126, top - 2, 214, top - 2], fill=(176, 184, 196))
    d.rectangle([126, top + 2, 214, deck - 1], fill=(200, 224, 240))
    d.rectangle([126, top + 2, 214, top + 5], fill=(216, 236, 250))
    for x in range(126, 214, 10):
        d.line([x + 2, top + 3, x + 6, deck - 2], fill=(238, 247, 254), width=2)
    for x in range(126, 214, 10):
        d.line([x, top + 2, x + 10, deck - 1], fill=(132, 142, 156), width=2)
        d.line([x + 10, top + 2, x, deck - 1], fill=(132, 142, 156), width=2)
        d.line([x, top + 2, x, deck - 1], fill=(108, 116, 128), width=2)
    d.rectangle([126, deck - 1, 214, deck + 4], fill=CONC[1])
    d.line([126, deck - 1, 214, deck - 1], fill=CONC[3])
    d.line([126, deck + 4, 214, deck + 4], fill=CONC[0])
    d.rectangle([176, top + 3, 206, deck - 3], fill=(253, 248, 249), outline=(196, 58, 78))
    hx, hy = d.p(186, top + 6)
    figura2(im, CORAZON, hx, hy, (224, 48, 70))
    for (a, b) in ((179, top + 7), (201, top + 5)):
        sx, sy = d.p(a, b)
        figura(im, ["010", "111", "010"], sx, sy, (255, 196, 80))
    # caseta de ladrillo donde termina la rampa
    d.rectangle([118, top - 4, 128, 64], fill=(160, 96, 70))
    for yy in range(top - 2, 64, 3):
        d.line([118, yy, 128, yy], fill=(146, 86, 62))
    d.line([127, top - 4, 127, 64], fill=(126, 74, 52))
    d.rectangle([117, top - 6, 129, top - 4], fill=(128, 74, 52))
    d.rectangle([120, 50, 126, 63], fill=(70, 60, 64))
    d.rectangle([121, 51, 125, 54], fill=(120, 150, 180))
    # torre de ladrillo al otro lado (se asoma)
    d.rectangle([212, 30, 226, 68], fill=(180, 96, 68))

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
    return False

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

def seto(im):
    """Seto con florcitas abajo a la izquierda: la gente de la vereda se pierde detrás."""
    d = ImageDraw.Draw(im)
    tonos = [(34, 84, 40), (52, 112, 48), (74, 142, 60), (112, 176, 80)]
    d.rectangle([0, 130, 74, H - 1], fill=tonos[0])
    random.seed(41)
    matas = [(x, 127 + int(3 * math.sin(x * .3)) + x // 24, 7 + (x * 7) % 4) for x in range(-4, 74, 6)]
    for (x, y, r) in matas:
        d.ellipse([x - r, y - r, x + r, y + r], fill=tonos[0])
    for (x, y, r) in matas:
        d.ellipse([x - r + 1, y - r + 1, x + r - 2, y + r - 3], fill=tonos[1])
        d.ellipse([x - r + 2, y - r + 1, x + 1, y - 1], fill=tonos[2])
        d.point((x - r + 4, y - r + 3), fill=tonos[3])
    for _ in range(26):
        x, y = random.randint(2, 70), random.randint(124, H - 3)
        c = random.choice([(255, 255, 255), (255, 190, 210), (255, 236, 120)])
        d.point([(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)], fill=c)
        d.point((x, y), fill=(255, 206, 60))

BASE = Image.new('RGB', (W, H))
cielo(BASE)
fondo_lejano(BASE)
suelo(BASE)
pasarela(BASE)
arbol(BASE, 92, 44, 15, 2, 68)
flores(BASE)
rampa_base(BASE)

def capa(dibujar):
    """Dibuja sobre un fondo clave y devuelve (imagen, máscara) para pegarla encima en cada cuadro."""
    im = Image.new('RGB', (W, H), CLAVE)
    dibujar(im)
    m = Image.new('L', (W, H), 0)
    ip, mp = im.load(), m.load()
    for y in range(H):
        for x in range(W):
            if ip[x, y] != CLAVE:
                mp[x, y] = 255
    return im, m

CLAVE = (255, 0, 255)
# la pasarela va delante de las nubes y los autos
PUENTE, MASCARA_PUENTE = capa(pasarela)
# el árbol grande, el poste y el seto van al frente
FRENTE, MASCARA_FRENTE = capa(lambda im: (arbol(im, 14, 46, 30, 1, 124), poste(im), seto(im)))
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
DENIM, DENIM_S, DENIM_L, PESPUNTE = (82, 124, 184), (58, 92, 146), (124, 162, 214), (222, 170, 96)
CHIPORRO, CHIPORRO_S = (244, 236, 218), (212, 200, 176)
NEGRO_P, NEGRO_PS = (46, 46, 56), (32, 32, 40)
CUERO, CUERO_S = (150, 98, 60), (112, 72, 44)
PELO_E, PELO_E2, PELO_E3 = (40, 28, 26), (68, 48, 40), (110, 80, 62)
LILA, LILA_S, LILA_L, LILA_O = (192, 158, 228), (156, 120, 198), (224, 204, 246), (128, 94, 170)
FALDA, FALDA_S = (240, 218, 166), (204, 176, 124)
AMARILLO, AMARILLO_S = (255, 214, 96), (222, 172, 56)

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

BLANCO, BLANCO_S, BLANCO_L, BLANCO_P = (244, 244, 248), (206, 208, 220), (255, 255, 255), (188, 190, 206)
JEAN_E, JEAN_ES, JEAN_EL = (70, 106, 172), (50, 78, 136), (100, 136, 200)
PELO_E4 = (80, 60, 52)
CELESTE, CELESTE_S, CELESTE_L = (150, 198, 238), (110, 160, 214), (198, 228, 252)
CREMA_P, CREMA_PS = (238, 230, 212), (206, 194, 168)

PIEL_E, PIEL_ES, BARBA = (214, 160, 118), (180, 126, 90), (150, 112, 92)
PLATA = (206, 210, 220)

def eduardo(paso, gira):
    """Eduardo de espaldas (a la derecha), según su foto: tez morena, pelo negro corto a los lados con la nuca
    rebajada (degradado) y arriba más largo, con volumen y peinado hacia un lado; cadenita de plata.
    Polerón blanco de cuello redondo (sin capucha) con costuras raglán, pliegues y puños tejidos,
    blue jeans y zapatillas blancas. Si `gira`, voltea hacia Dallana: mejilla con barba corta, sin lentes."""
    S = Image.new('RGBA', (38, 61), (0, 0, 0, 0))
    DY = 9
    d = _Desplazado(ImageDraw.Draw(S), DY)
    cx = 18
    # blue jeans y zapatillas blancas
    for lado, x0 in ((-1, cx - 7), (1, cx + 1)):
        arriba = (paso == 0 and lado < 0) or (paso == 1 and lado > 0)
        y_fin = 45 if arriba else 48
        d.rectangle([x0, 34, x0 + 6, y_fin], fill=JEAN_E)
        d.line([x0 + (6 if lado < 0 else 0), 35, x0 + (6 if lado < 0 else 0), y_fin], fill=JEAN_ES)
        d.line([x0 + 2, 37, x0 + 2, y_fin - 3], fill=JEAN_EL)
        d.point([(x0 + 4, 40), (x0 + 3, 43)], fill=JEAN_ES)
        d.rectangle([x0 - 1, y_fin - 2, x0 + 7, y_fin + 1], fill=(250, 250, 252))
        d.line([x0 - 1, y_fin + 1, x0 + 7, y_fin + 1], fill=(196, 198, 208))
        d.point((x0 + 3, y_fin - 1), fill=(214, 216, 226))
        if arriba:
            d.line([x0 - 1, y_fin, x0 + 7, y_fin], fill=(170, 172, 182))
    # polerón blanco de cuello redondo
    d.polygon([(cx - 12, 19), (cx - 6, 13), (cx + 6, 13), (cx + 12, 19), (cx + 11, 37), (cx - 11, 37)], fill=BLANCO)
    d.polygon([(cx + 5, 14), (cx + 6, 13), (cx + 12, 19), (cx + 11, 35), (cx + 6, 35), (cx + 7, 24)], fill=BLANCO_S)
    d.polygon([(cx - 11, 20), (cx - 6, 14), (cx - 5, 15), (cx - 9, 21), (cx - 9, 33), (cx - 11, 33)], fill=BLANCO_L)
    d.line([(cx - 5, 14), (cx - 11, 21)], fill=BLANCO_P)                 # costuras raglán
    d.line([(cx + 5, 14), (cx + 11, 21)], fill=(176, 178, 196))
    d.line([(cx - 2, 18), (cx - 4, 26)], fill=(228, 230, 238))           # pliegues suaves de la tela
    d.line([(cx + 1, 25), (cx + 4, 32)], fill=(226, 228, 236))
    d.line([(cx - 6, 28), (cx - 3, 33)], fill=(230, 232, 240))
    d.line([(cx + 2, 17), (cx + 3, 21)], fill=(230, 232, 240))
    d.rectangle([cx - 11, 34, cx + 11, 37], fill=BLANCO_S)               # pretina tejida
    for x in range(cx - 10, cx + 11, 2):
        d.line([x, 35, x, 36], fill=BLANCO_P)
    # brazo derecho colgando, con puño tejido
    d.polygon([(cx + 11, 18), (cx + 14, 21), (cx + 14, 33), (cx + 11, 33)], fill=BLANCO_S)
    d.line([cx + 12, 21, cx + 12, 30], fill=BLANCO)
    d.line([cx + 13, 25, cx + 12, 27], fill=(186, 188, 204))
    d.rectangle([cx + 11, 31, cx + 14, 33], fill=BLANCO_P)
    d.point([(cx + 12, 32), (cx + 14, 32)], fill=(176, 178, 196))
    d.rounded_rectangle([cx + 11, 33, cx + 14, 37], radius=1, fill=PIEL_E)
    d.point((cx + 14, 36), fill=PIEL_ES)
    # brazo izquierdo hacia Dallana
    d.line([(cx - 10, 18), (cx - 15, 30)], fill=BLANCO, width=5)
    d.line([(cx - 11, 18), (cx - 16, 28)], fill=BLANCO_L)
    d.line([(cx - 12, 21), (cx - 14, 25)], fill=(226, 228, 236))
    d.line([(cx - 17, 30), (cx - 13, 30)], fill=BLANCO_P, width=2)
    d.rounded_rectangle([cx - 19, 31, cx - 15, 34], radius=1, fill=PIEL_E)
    # cuello con la cadenita y cuello redondo tejido
    d.rectangle([cx - 3, 7, cx + 3, 13], fill=PIEL_E)
    d.line([cx + 2, 8, cx + 3, 12], fill=PIEL_ES)
    d.arc([cx - 4, 6, cx + 4, 13], 15, 165, fill=PLATA)
    d.rounded_rectangle([cx - 6, 12, cx + 6, 15], radius=2, fill=BLANCO_S)
    for x in range(cx - 5, cx + 6, 2):
        d.point((x, 13), fill=BLANCO_P)
    d.line([cx - 4, 12, cx + 4, 12], fill=BLANCO)
    # cabeza: nuca y costados con degradado (de negro a piel), arriba largo con volumen hacia la izquierda
    g = 1 if gira else 0
    hx = cx + g
    NP, NP2, NP3, NPF = (26, 20, 20), (50, 38, 36), (92, 78, 78), (58, 46, 42)
    d.ellipse([hx - 7, -4, hx + 7, 11], fill=PIEL_E)
    px = S.load()
    for y in range(-4, 11):
        for x in range(hx - 7, hx + 8):
            if ((x - hx) / 7.5) ** 2 + ((y - 3.5) / 7.5) ** 2 > 1 or px[x, y + DY][3] == 0:
                continue
            if y <= 4:
                col = NP
            elif y <= 6:
                col = NP if (x + y) % 3 else NPF
            elif y <= 8:
                col = NPF if (x + y) % 2 else lerp(NPF, PIEL_E, .5)
            elif y <= 9:
                col = lerp(NPF, PIEL_E, .6) if (x + y) % 2 else lerp(NPF, PIEL_E, .85)
            else:
                continue
            px[x, y + DY] = col + (255,)
    # el largo de arriba: copete con volumen, barrido hacia la izquierda; borde de abajo desigual
    d.polygon([(hx + 8, 2), (hx + 8, -3), (hx + 5, -7), (hx, -8), (hx - 5, -8), (hx - 9, -6), (hx - 11, -2), (hx - 10, 2),
               (hx - 7, 4), (hx - 4, 3), (hx - 1, 5), (hx + 2, 3), (hx + 5, 4)], fill=NP)
    for (x0, y0, x1, y1) in ((hx + 5, -6, hx + 1, -7), (hx + 2, -4, hx - 3, -6), (hx - 1, -1, hx - 6, -3), (hx + 6, -1, hx + 2, -2),
                             (hx - 4, 2, hx - 9, 0), (hx + 3, 1, hx, 0), (hx - 6, -6, hx - 9, -4)):
        d.line([x0, y0, x1, y1], fill=NP2)                              # mechones cortos barridos
    d.line([hx - 3, -7, hx - 8, -5], fill=NP3)                          # brillo arriba a la izquierda
    d.point([(hx - 9, -3), (hx - 1, -7)], fill=NP3)
    d.point([(hx - 1, -8), (hx + 2, -8), (hx - 6, -8)], fill=NP)        # puntitas
    d.point([(hx - 11, 0), (hx - 12, -1)], fill=NP)
    # orejas: los costados van cortos, así que se ven
    for ox in (-1, 1):
        x0 = hx + ox * 8
        d.rectangle([x0 - 1, 3, x0 + 1, 7], fill=PIEL_E)
        d.point([(x0 + ox, 4), (x0 + ox, 5), (x0 + ox, 6)], fill=PIEL_E)
        d.line([x0, 4, x0, 6], fill=PIEL_ES)
        d.point((x0 - ox, 2), fill=NPF)
    if gira:                                                          # mira a Dallana: mejilla y barba corta, sin lentes
        d.ellipse([cx - 12, 1, cx - 6, 11], fill=PIEL_E)
        d.point([(cx - 13, 5), (cx - 13, 6)], fill=PIEL_E)            # nariz
        for (x, y) in ((cx - 11, 9), (cx - 10, 10), (cx - 9, 10), (cx - 8, 10), (cx - 12, 8), (cx - 7, 9), (cx - 9, 8)):
            d.point((x, y), fill=BARBA)
        d.point((cx - 11, 4), fill=(50, 36, 32))                      # pestaña
        d.line([cx - 12, 2, cx - 10, 2], fill=PELO_E)                 # ceja
        d.rectangle([cx - 8, 0, cx - 7, 4], fill=(58, 46, 42))        # patilla corta
        d.polygon([(cx - 13, -1), (cx - 6, -4), (cx - 5, 1), (cx - 10, 1)], fill=(26, 20, 20))
        d.line([cx - 12, -1, cx - 8, -3], fill=(92, 78, 78))
    return contorno(S, OUTL)

def dallana(paso, mira):
    """Dallana de espaldas (a la izquierda): blusa celeste con mangas abullonadas, pantalón crema,
    zapatillas blancas, carterita amarilla con una margarita y moñito blanco en su pelo crespo.
    Si `mira`, gira la cabeza a la derecha para mirar a Eduardo."""
    S = Image.new('RGBA', (38, 50), (0, 0, 0, 0))
    d = ImageDraw.Draw(S)
    cx = 19
    piernas(d, cx, paso, CREMA_P, CREMA_PS, (250, 250, 252), (196, 198, 208))
    # blusa celeste: un poco suelta abajo, costura al centro y mangas abullonadas
    d.polygon([(cx - 9, 17), (cx - 6, 15), (cx + 6, 15), (cx + 9, 17), (cx + 10, 33), (cx - 10, 33)], fill=CELESTE)
    d.polygon([(cx + 4, 16), (cx + 6, 15), (cx + 9, 17), (cx + 10, 33), (cx + 5, 33)], fill=CELESTE_S)
    d.rectangle([cx - 8, 18, cx - 7, 30], fill=CELESTE_L)
    for x in (cx - 4, cx, cx + 3):
        d.line([x, 23, x + (1 if x > cx else 0), 32], fill=CELESTE_S)     # pliegues
    d.line([cx - 10, 33, cx + 10, 33], fill=CELESTE_S)
    for x in range(cx - 9, cx + 10, 3):
        d.point((x, 32), fill=CELESTE_L)
    # carterita amarilla con margarita, colgando cruzada
    d.line([(cx - 6, 16), (cx + 9, 28)], fill=AMARILLO_S)
    d.ellipse([cx + 7, 27, cx + 14, 34], fill=AMARILLO)
    d.arc([cx + 7, 27, cx + 14, 34], 300, 90, fill=AMARILLO_S)
    d.point([(cx + 10, 29), (cx + 12, 31), (cx + 10, 32), (cx + 9, 31), (cx + 11, 30)], fill=(255, 255, 255))
    d.point((cx + 10, 31), fill=(240, 150, 40))
    # brazo derecho hacia Eduardo (manos juntas), con manga abullonada
    d.ellipse([cx + 5, 15, cx + 11, 21], fill=CELESTE_S)
    d.line([(cx + 8, 19), (cx + 13, 28)], fill=CELESTE_S, width=3)
    d.line([(cx + 12, 27), (cx + 15, 27)], fill=CELESTE_L)
    d.rectangle([cx + 12, 28, cx + 16, 31], fill=PIEL)
    # brazo izquierdo colgando
    d.ellipse([cx - 12, 15, cx - 6, 21], fill=CELESTE)
    d.point((cx - 10, 17), fill=CELESTE_L)
    d.rectangle([cx - 12, 19, cx - 9, 29], fill=CELESTE)
    d.line([cx - 11, 20, cx - 11, 28], fill=CELESTE_L)
    d.line([cx - 12, 29, cx - 9, 29], fill=CELESTE_S)
    d.rectangle([cx - 12, 30, cx - 9, 33], fill=PIEL)
    # pelo crespo largo
    g = 1 if mira else 0
    d.ellipse([cx - 10 + g, -1, cx + 10 + g, 27], fill=PELO)
    for (x, y, r) in ((cx - 10, 5, 3), (cx - 11, 12, 3), (cx - 11, 19, 3), (cx - 8, 25, 3), (cx + 10, 5, 3), (cx + 11, 12, 3),
                      (cx + 11, 19, 3), (cx + 8, 25, 3), (cx - 5, -1, 3), (cx + 4, -1, 3), (cx, 27, 3), (cx - 4, 27, 2), (cx + 4, 27, 2)):
        d.ellipse([x - r + g, y - r, x + r + g, y + r], fill=PELO)
    for gy in range(1, 27, 3):
        for gx in range(cx - 9, cx + 10, 3):
            x = gx + (gy // 3) % 2 + g
            claro = (x - cx) + (gy - 8) < -6
            d.arc([x - 1, gy - 1, x + 1, gy + 1], 160, 380, fill=PELO3 if claro else PELO2)
    bx = cx - 6 + g                                              # moñito blanco
    d.polygon([(bx - 3, 1), (bx, 3), (bx - 3, 5)], fill=(252, 252, 252))
    d.polygon([(bx + 3, 1), (bx, 3), (bx + 3, 5)], fill=(252, 252, 252))
    d.point([(bx - 2, 3), (bx + 2, 3)], fill=(214, 222, 236))
    d.point((bx, 3), fill=CELESTE_S)
    if mira:                                                     # mira a Eduardo: mejilla, lentes rojos, rubor
        d.ellipse([cx + 5, 4, cx + 13, 13], fill=PIEL)
        d.point((cx + 14, 9), fill=PIEL)
        d.rectangle([cx + 8, 7, cx + 13, 9], fill=(200, 32, 50))
        d.rectangle([cx + 10, 8, cx + 12, 8], fill=(226, 240, 250))
        d.point([(cx + 9, 11), (cx + 10, 11)], fill=(244, 138, 140))
        d.ellipse([cx + 2, 0, cx + 8, 11], fill=PELO)
        d.arc([cx + 3, 2, cx + 7, 6], 160, 380, fill=PELO2)
    else:
        d.point([(cx - 11, 8), (cx + 10, 8)], fill=(200, 32, 50))
    return contorno(S, OUTL)

def pareja(im, f):
    t = f % F
    paso = (f // 6) % 2
    bob = 1 if f % 6 in (2, 3) else 0
    gira = 6 <= t < 116                 # Eduardo le habla y la mira
    mira = 58 <= t < 116                # ella se da vuelta a mirarlo
    dx, dy = 92, 92 - bob               # Dallana a la izquierda
    ex, ey = dx + 33, 79 - bob          # Eduardo a la derecha (del lado de la calle)
    d = ImageDraw.Draw(im)
    p = im.load()
    for (sx, sy, an) in ((dx + 19, 140, 10), (ex + 18, 139, 11)):
        for yy in range(sy - 2, sy + 2):
            for xx in range(sx - an, sx + an):
                if ((xx - sx) / an) ** 2 + ((yy - sy) / 2) ** 2 <= 1 and (xx + yy) % 2 == 0:
                    p[xx, yy] = lerp(p[xx, yy], CONC[0], .7)
    se = eduardo(1 - paso, gira)
    sd = dallana(paso, mira)
    im.paste(se, (ex, ey), se)
    im.paste(sd, (dx, dy), sd)
    # la respuesta de Dallana: un globito con corazones
    if 94 <= t < 116:
        bx, by = dx + 2, dy - 22
        d.rounded_rectangle([bx, by, bx + 24, by + 13], radius=4, fill=(255, 255, 255), outline=(70, 70, 80))
        d.polygon([(bx + 15, by + 13), (bx + 20, by + 13), (bx + 21, by + 18)], fill=(255, 255, 255))
        d.line([bx + 15, by + 13, bx + 21, by + 18], fill=(70, 70, 80)); d.line([bx + 21, by + 18, bx + 20, by + 13], fill=(70, 70, 80))
        late = (f // 4) % 2
        figura(im, CORAZON, bx + 4, by + 4 - late, (224, 48, 70))
        figura(im, CORAZON, bx + 13, by + 3 + late, (240, 110, 150))
    # corazones que suben desde las manos juntas
    for k in range(2):
        u = ((f + k * 12) % 24) / 24
        hx = dx + 29 + k * 4 + int(2 * math.sin(u * TAU + k))
        hy = int(dy + 26 - u * 30)
        if u < .8:
            figura(im, CORAZON, hx, hy, (255, 110, 140) if k == 0 else (255, 160, 190))

# ---------- la pregunta de Eduardo, en letras pixel ----------
FUENTE = {
    'B': ["110", "101", "110", "101", "110"], 'F': ["111", "100", "110", "100", "100"],
    'A': ["010", "101", "111", "101", "101"], 'C': ["011", "100", "100", "100", "011"], 'D': ["110", "101", "101", "101", "110"],
    'E': ["111", "100", "110", "100", "111"], 'I': ["111", "010", "010", "010", "111"], 'J': ["001", "001", "001", "101", "010"],
    'L': ["100", "100", "100", "100", "111"], 'M': ["10001", "11011", "10101", "10001", "10001"], 'N': ["1001", "1101", "1011", "1001", "1001"],
    'O': ["010", "101", "101", "101", "010"], 'P': ["110", "101", "110", "100", "100"], 'Q': ["010", "101", "101", "110", "011"],
    'R': ["110", "101", "110", "101", "101"], 'S': ["011", "100", "010", "001", "110"], 'T': ["111", "010", "010", "010", "010"],
    'U': ["101", "101", "101", "101", "111"], '?': ["110", "001", "010", "000", "010"], '¿': ["010", "000", "010", "100", "011"],
}
SIN_TILDE = {'Ú': 'U', 'É': 'E', 'Í': 'I', 'Ó': 'O'}
PREGUNTA = ["¿LAS PAREJAS DEBERÍAN", "PARECERSE O SER", "DISTINTAS PARA QUE", "LA RELACIÓN FUNCIONE?"]

def ancho_linea(txt):
    return sum(3 if ch == ' ' else len(FUENTE[SIN_TILDE.get(ch, ch)][0]) + 1 for ch in txt) - 1

def escribir(im, txt, x, y, col, n):
    p = im.load()
    for ch in txt[:max(0, n)]:
        if ch == ' ':
            x += 3
            continue
        g = FUENTE[SIN_TILDE.get(ch, ch)]
        figura(im, g, x, y, col)
        if ch in SIN_TILDE:
            p[x + 1, y - 2] = col
            p[x + 2, y - 3] = col
        x += len(g[0]) + 1

def dialogo(im, f):
    t = f % F
    if not 8 <= t < 92:
        return
    d = ImageDraw.Draw(im)
    ancho = max(ancho_linea(l) for l in PREGUNTA)
    bw, bh = ancho + 10, len(PREGUNTA) * 8 + 4
    bx, by = 128 - bw // 2, 75 - bh + (2 if t < 10 else 0)
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=4, fill=(255, 255, 255), outline=(70, 70, 80))
    tx = 141                                         # colita hacia la cabeza de Eduardo
    d.polygon([(tx - 5, by + bh), (tx, by + bh), (tx + 2, by + bh + 5)], fill=(255, 255, 255))
    d.line([tx - 5, by + bh, tx + 2, by + bh + 5], fill=(70, 70, 80)); d.line([tx + 2, by + bh + 5, tx, by + bh], fill=(70, 70, 80))
    quedan = int((t - 10) * 2.2)                     # se escribe letra por letra
    y = by + 5
    for linea in PREGUNTA:
        escribir(im, linea, 128 - ancho_linea(linea) // 2, y, (64, 52, 76), quedan)
        quedan -= len(linea)
        y += 8

# ---------- vida alrededor ----------
def nubes(im, f):
    p = im.load()
    desp = f * 96 // F
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

def persona(im, x, y, h, cfg, paso, frente):
    """Una persona de pie con (x, y) = pies; `frente` = viene hacia la cámara. Devuelve la mano derecha."""
    h = int(round(h))
    if h < 5:
        return None
    w = max(3, int(h * .36))
    S = Image.new('RGBA', (w + 12, h + 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(S)
    c, top = (w + 12) // 2, 2
    r = max(1, round(h * .09))
    hombro = top + 2 * r + 1
    cadera = top + int(h * .56)
    pie = top + h - 1
    lw = max(1, w // 3)
    piel = cfg.get('piel', PIEL)
    ropa, ropa_s = cfg['ropa']
    sep = 1 if w > 5 else 0
    for k, x0 in enumerate((c - lw - sep, c + sep)):
        y1 = pie - (max(1, h // 14) if (paso == k and h >= 9) else 0)
        d.rectangle([x0, cadera, x0 + lw - 1, y1], fill=cfg['pant'])
        d.line([x0, y1, x0 + lw - 1, y1], fill=cfg.get('zap', (64, 58, 62)))
    if 'falda' in cfg:
        fy = cadera + max(2, int(h * .16))
        d.polygon([(c - w // 2, cadera - 1), (c + w // 2, cadera - 1), (c + w // 2 + 1, fy), (c - w // 2 - 1, fy)], fill=cfg['falda'])
    if cfg.get('largo') and frente:
        d.rectangle([c - r - 1, top + r, c + r + 1, hombro + int(h * .14)], fill=cfg['pelo'])
    d.rounded_rectangle([c - w // 2, hombro, c + w // 2, cadera + 1], radius=max(0, w // 4), fill=ropa)
    if w >= 6:
        d.rectangle([c + w // 4, hombro + 1, c + w // 2 - 1, cadera], fill=ropa_s)
    br = max(1, w // 5)
    vaiven = max(0, h // 20)
    for k, xa in enumerate((c - w // 2 - br, c + w // 2 + 1)):
        sv = vaiven if paso == k else -vaiven
        d.rectangle([xa, hombro + 1, xa + br - 1, max(hombro + 1, cadera - 1 + sv)], fill=ropa_s if k else ropa)
        d.rectangle([xa, cadera + sv, xa + br - 1, cadera + sv + max(0, br - 1)], fill=piel)
    if 'mochila' in cfg and not frente:
        d.rounded_rectangle([c - w // 3, hombro + 1, c + w // 3, hombro + max(2, int(h * .26))], radius=1, fill=cfg['mochila'])
    elif 'mochila' in cfg:
        for xm in (c - w // 3, c + w // 3):
            d.line([xm, hombro, xm, hombro + int(h * .2)], fill=cfg['mochila'])
    if 'bolsa' in cfg:
        xb, tb = c + w // 2 + 1 + br, max(2, w // 3)
        d.rectangle([xb - 1, cadera - 2, xb + tb - 1, cadera - 2 + tb], fill=cfg['bolsa'])
    d.ellipse([c - r, top, c + r, top + 2 * r], fill=piel)
    if frente:
        d.chord([c - r, top, c + r, top + 2 * r], 180, 360, fill=cfg['pelo'])
        if r >= 2:
            d.point([(c - 1, top + r + 1), (c + 1, top + r + 1)], fill=(50, 40, 44))
    else:
        d.ellipse([c - r, top, c + r, top + 2 * r], fill=cfg['pelo'])
        if cfg.get('largo'):
            d.rectangle([c - r, top + r, c + r, hombro + int(h * .14)], fill=cfg['pelo'])
    if h >= 14:
        S = contorno(S, OUTL)
    im.paste(S, (int(x) - c, int(y) - pie), S)
    return (int(x) + w // 2 + 1, int(y) - pie + cadera)

def perro(im, x, y, h, paso, f):
    """Perrito café que va al lado de su dueño, moviendo la cola."""
    d = ImageDraw.Draw(im)
    hp = max(3, int(h * .24))
    largo = int(hp * 1.6)
    col, cs = (198, 142, 82), (150, 100, 58)
    for k, xx in enumerate((x + 1, x + largo - 1)):
        d.line([xx, y - hp // 2, xx, y - (1 if (paso + k) % 2 else 0)], fill=cs)
    d.rounded_rectangle([x, y - hp, x + largo, y - hp // 2], radius=1, fill=col)
    d.rounded_rectangle([x + largo - 1, y - hp - hp // 2, x + largo + hp // 2 + 1, y - hp // 2 - 1], radius=1, fill=col)
    d.point((x + largo, y - hp - hp // 2), fill=cs)
    d.point((x + largo + hp // 2, y - hp), fill=(40, 30, 30))
    d.line([x, y - hp, x - 2, y - hp - 2 - (f // 2) % 2], fill=col)
    return (x + largo + 1, y - hp - 1)

GENTE = [  # (ropa, sube = de espaldas alejándose, carril en la vereda, fase, vueltas por ciclo, tamaño)
    ({'ropa': ((150, 64, 86), (116, 46, 66)), 'pant': (64, 62, 84), 'pelo': (206, 206, 212), 'bolsa': (230, 190, 90)}, True, .3, 0, 1, .95),
    ({'ropa': ((64, 150, 118), (44, 116, 90)), 'pant': (70, 90, 140), 'pelo': (36, 30, 30), 'mochila': (240, 140, 50)}, False, .72, .3, 1, 1),
    ({'ropa': ((206, 176, 104), (170, 140, 78)), 'pant': (84, 70, 58), 'pelo': (70, 56, 46), 'perro': True}, True, .62, .55, 1, 1.02),
    ({'ropa': ((246, 208, 96), (214, 170, 64)), 'pant': PIEL, 'pelo': (110, 70, 44), 'largo': True, 'falda': (90, 110, 170)}, False, .36, .78, 1, .92),
    ({'ropa': ((230, 70, 70), (186, 48, 52)), 'pant': (60, 80, 130), 'pelo': (60, 40, 30), 'globo': (90, 170, 240)}, True, .5, .12, 2, .62),
]

def gente(im, f):
    d = ImageDraw.Draw(im)
    # alguien cruza por dentro de la pasarela
    t = (f % F) / F
    persona(im, 134 + t * 116, 53, 12, {'ropa': ((90, 100, 140), (66, 74, 108)), 'pant': (50, 56, 80), 'pelo': (50, 40, 36)}, (f // 3) % 2, False)
    # la vereda de la izquierda: unos suben, otros bajan; cerca de la cámara salen por el borde
    def borde_izq(y): return (132 - y) * 101 / 68
    def borde_der(y): return 52 + (144 - y) * 54 / 80
    lista = []
    for (cfg, sube, carril, fase, vueltas, tam) in GENTE:
        u = (f / F * vueltas + fase) % 1
        z = 1 + u * 8 if sube else 9 - u * 8
        lista.append((z, cfg, sube, carril, vueltas, tam))
    for (z, cfg, sube, carril, vueltas, tam) in sorted(lista, key=lambda e: -e[0]):
        y = y_de(z)
        x = borde_izq(y) + (borde_der(y) - borde_izq(y)) * carril - max(0, 2 - z) * 55
        h = 52 / z * tam
        paso = (f // (2 if vueltas > 1 else 4)) % 2
        if cfg.get('perro'):
            cuello = perro(im, int(x - h * .62), int(y), h, paso, f)
        mano = persona(im, x, y, h, cfg, paso, not sube)
        if mano and cfg.get('perro'):
            d.line([(mano[0] - int(h * .4), mano[1]), cuello], fill=(200, 60, 60))
        if mano and cfg.get('globo'):
            gx, gy = mano[0] + 1, mano[1] - int(h * .7)
            rg = max(1, int(h * .13))
            d.line([mano, (gx, gy + rg)], fill=(230, 230, 230))
            d.ellipse([gx - rg, gy - rg, gx + rg, gy + rg + 1], fill=cfg['globo'])
            d.point((gx - rg // 2, gy - rg // 2), fill=(200, 230, 255))

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
    im.paste(PUENTE, (0, 0), MASCARA_PUENTE)
    gente(im, f)
    juntas_y_barandas(im, f)
    pareja(im, f)
    im.paste(FRENTE, (0, 0), MASCARA_FRENTE)
    hojas_que_caen(im, f)
    mariposas(im, f)
    destellos(im, f)
    dialogo(im, f)
    frames.append(im.resize((W * K, H * K), Image.NEAREST))

# paleta común de 128 colores para todos los cuadros: el GIF pesa la mitad sin perder calidad
muestra = Image.new('RGB', (frames[0].width, frames[0].height * 4))
for k, i in enumerate((0, 40, 70, 100)):
    muestra.paste(frames[i], (0, frames[0].height * k))
paleta = muestra.quantize(colors=128, method=Image.Quantize.MEDIANCUT)
cuadros = [fr.quantize(palette=paleta, dither=Image.Dither.NONE) for fr in frames]
cuadros[0].save(OUT + '.gif', save_all=True, append_images=cuadros[1:], duration=90, loop=0, optimize=True, disposal=1)
frames[0].save(OUT + '_f0.png')
print('ok')
