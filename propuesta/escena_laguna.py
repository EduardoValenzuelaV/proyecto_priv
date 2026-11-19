"""Escena pixel: Eduardo y Dallana de pie en la glorieta de madera, mirando la laguna (los vemos de espalda).
Uso: python propuesta/escena_laguna.py assets/pixel/laguna   (genera laguna.gif y laguna_f0.png)
"""
import sys, math, random
from PIL import Image, ImageDraw

OUT = sys.argv[1] if len(sys.argv) > 1 else 'laguna'
W, H, K, F = 256, 144, 2, 96
VUELTA = 288  # ancho del recorrido que se repite: 3 px por cuadro x 96 cuadros

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

PAL = {
    'O': (34, 22, 26),
    'H': (44, 30, 30), 'h': (78, 52, 46), 'c': (130, 90, 72),
    'S': (236, 186, 146), 's': (204, 146, 110),
    'R': (200, 32, 50),
    # Eduardo: polerón café y pantalón negro
    'B': (140, 92, 58), 'b': (104, 66, 40), 'u': (176, 124, 82), 'N': (30, 30, 34), 'n': (52, 52, 60),
    # Dallana: suéter rojo y jeans
    'X': (204, 44, 60), 'x': (150, 28, 44), 'y': (238, 100, 110),
    'P': (68, 88, 130), 'p': (46, 58, 92),
    'W': (248, 246, 242),
}

# ---------- de espalda ----------
EL_ESPALDA = [
    ".....OOOOOO",
    "...OOHHHHHHOO",
    "..OHHhHHHHhHHO",
    ".OHHHHHHHHHHHHO",
    ".OHHhHHHHHHhHHO",
    ".OHHHHHHHHHHHHO",
    ".OHHHHHhHHHHHHO",
    ".OsHHHHHHHHHHsO",
    ".OsHHHHHHHHHHsO",
    "..OHHHHHHHHHHO",
    "...OSSSSSSSSO",
    "..ObbbbbbbbbbO",
    ".ObbBBBBBBBBbbO",
    "OBBbBBBBBBBBbBBO",
    "OBBBBBBBBBBBBBBO",
    "OBBBBBBBBBBBBBBO",
    "OBBBBBBBBBBBBBBO",
    "OSBBBBBBBBBBBBBO",
    "OSBBBBBBBBBBBBSO",
    ".OBBBBBBBBBBBBO",
    ".ObbbbbbbbbbbbO",
    "..ONNNNNNNNNNO",
    "..ONNNnOONnNNO",
    "..ONNNnOONnNNO",
    "..ONNNnOONnNNO",
    "..ONNNNOONNNNO",
    "..OWWWWOOWWWWO",
    "..OOOOOOOOOOOO",
]
ELLA_ESPALDA = [
    "....OO.OOO.OO",
    "..OOccOHHcOHHO",
    ".OHHHHhHHHHHhHO",
    "OHHcHHHHHhHHHHHO",
    "OHHHHHhcHHHHcHHO",
    "OHhHHcHHHHHHHHHO",
    "ORHHHHHHhHHcHHRO",
    "OHcHhHHHHHHHHhHO",
    "OHHHHHcHHHhHHHHO",
    "OHhHHHHHHHHHcHHO",
    "OHHHcHHhHHHHHHHO",
    "OXHHHHHHHHcHHHXO",
    "OXHhHHcHHHHHhHXO",
    "OXXHHHHHHHHHHXXO",
    "OXXXHHcHHhHHXXXO",
    "OSXXXHHHHHHXXXSO",
    "OSXXXXXXXXXXXXSO",
    ".OXXXXXyXXXXXXO",
    ".OxxxxxxxxxxxxO",
    "..OPPPPPPPPPPO",
    "..OPPPpOOpPPPO",
    "..OPPPpOOpPPPO",
    "..OPPPPOOPPPPO",
    "..OWWWWOOWWWWO",
    "..OOOOOOOOOOOO",
]

def pegar(im, filas, x0, y0):
    p = im.load()
    for y, fila in enumerate(filas):
        for x, ch in enumerate(fila):
            if ch != '.' and 0 <= x0 + x < W and 0 <= y0 + y < H:
                p[x0 + x, y0 + y] = PAL[ch]

CORAZON = ["0110110", "1111111", "1111111", "0111110", "0011100", "0001000"]
def corazon(im, x, y, col):
    p = im.load()
    for r, fila in enumerate(CORAZON):
        for c, v in enumerate(fila):
            if v == '1' and 0 <= x + c < W and 0 <= y + r < H:
                p[x + c, y + r] = col

def copa(d, cx, cy, r, base, claro, osc, rnd):
    """Copa de árbol hecha de varias manchas."""
    for _ in range(14):
        dx, dy = rnd.randint(-r, r), rnd.randint(-r // 2, r // 2)
        rr = rnd.randint(r // 3, r // 2 + 2)
        d.ellipse([cx + dx - rr, cy + dy - rr, cx + dx + rr, cy + dy + rr], fill=base)
    for _ in range(10):
        dx, dy = rnd.randint(-r, r), rnd.randint(-r // 2, 0)
        d.ellipse([cx + dx - 2, cy + dy - 2, cx + dx + 2, cy + dy + 2], fill=claro)
    for _ in range(8):
        dx, dy = rnd.randint(-r, r), rnd.randint(0, r // 2)
        d.ellipse([cx + dx - 2, cy + dy - 1, cx + dx + 2, cy + dy + 2], fill=osc)

def laguna_fauna(d, p, f):
    """Patitos en fila, tortuguitas nadando y pececitos que saltan."""
    def punto(x, y, col):
        if 0 <= x < W and 56 <= y < 100:
            p[x, y] = col
    # mamá pata con tres patitos (nadan a la derecha)
    mx = (f * 3) % VUELTA - 30
    bob = 1 if (f // 3) % 2 else 0
    d.ellipse([mx, 86 + bob, mx + 8, 90 + bob], fill=(250, 250, 244))
    d.ellipse([mx + 6, 83 + bob, mx + 10, 87 + bob], fill=(250, 250, 244))
    punto(mx + 11, 85 + bob, (240, 160, 40)); punto(mx + 8, 84 + bob, (30, 30, 30))
    d.line([mx - 3, 91, mx + 8, 91], fill=(170, 206, 186))
    for n in range(3):
        cx = mx - 7 - n * 6
        cb = 1 if (f // 3 + n) % 2 else 0
        d.rectangle([cx, 88 + cb, cx + 3, 90 + cb], fill=(250, 214, 70))
        d.rectangle([cx + 2, 86 + cb, cx + 4, 88 + cb], fill=(250, 214, 70))
        punto(cx + 5, 87 + cb, (240, 140, 40)); punto(cx + 3, 87 + cb, (30, 30, 30))
    # dos tortuguitas (nadan a la izquierda)
    for n, (off, y) in enumerate(((40, 77), (190, 93))):
        tx = W - ((f * 3 + off) % VUELTA) + 16
        d.ellipse([tx, y, tx + 6, y + 3], fill=(70, 128, 66))
        punto(tx + 2, y + 1, (120, 176, 100)); punto(tx + 4, y + 1, (120, 176, 100))
        punto(tx - 1, y + 2, (150, 190, 110)); punto(tx - 2, y + 2, (150, 190, 110))
        pata = 1 if (f // 2 + n) % 2 else 0
        punto(tx + pata, y + 4, (150, 190, 110)); punto(tx + 5 - pata, y + 4, (150, 190, 110))
        d.line([tx + 7, y + 3, tx + 12, y + 3], fill=(160, 200, 180))
    # pececitos que saltan haciendo un arco y salpican al caer
    for n, (x0, base, fase, col) in enumerate(((30, 82, 0, (240, 130, 60)), (200, 80, 32, (210, 220, 230)), (100, 92, 64, (240, 150, 70)), (60, 70, 48, (210, 220, 230)))):
        t = (f + fase) % 32
        if t < 10:
            u = t / 9
            fx = x0 + int(u * 12)
            fy = base - int(14 * 4 * u * (1 - u))
            sube = u < .5
            for (a, b) in ((0, 0), (1, 0), (2, 0), (1, -1 if sube else 1)):
                if 0 <= fx + a < W and 0 <= fy + b < H:
                    p[fx + a, fy + b] = col
            cola = (fx - 1, fy + (1 if sube else -1))
            if 0 <= cola[0] < W and 0 <= cola[1] < H:
                p[cola] = col
            if t < 2:
                for (a, b) in ((-1, 1), (2, 1), (0, 2)):
                    punto(x0 + a, base + b, (240, 250, 250))
        elif t < 14:
            r = t - 9
            sx = x0 + 12
            for (a, b) in ((-r, 0), (r, 0), (0, -1), (-r + 1, -1), (r - 1, -1)):
                punto(sx + a, base + b, (240, 250, 250))

def fondo(f):
    im = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(im)
    p = im.load()
    # cielo
    for y in range(60):
        c = lerp((150, 200, 240), (206, 230, 246), y / 60)
        d.line([0, y, W, y], fill=c)
    for (x, y, w) in [(30, 10, 34), (120, 6, 40), (180, 16, 28)]:
        xx = (x + f) % VUELTA - 20
        d.rounded_rectangle([xx, y, xx + w, y + 6], radius=3, fill=(246, 250, 255))
        d.rounded_rectangle([xx + 6, y - 3, xx + w - 8, y + 3], radius=3, fill=(250, 252, 255))
    # árboles de la otra orilla
    rnd = random.Random(7)
    for x in range(-10, W + 10, 14):
        copa(d, x, 50, 10, (84, 140, 70), (120, 176, 90), (60, 110, 56), rnd)
    # laguna
    for y in range(56, 100):
        c = lerp((96, 150, 120), (126, 170, 140), (y - 56) / 44)
        d.line([0, y, W, y], fill=c)
    for y in range(56, 64):
        for x in range(0, W, 2):
            if (x + y) % 4 == 0:
                p[x, y] = lerp(p[x, y], (60, 110, 56), .5)
    # ondas que se desplazan y destellos de sol
    for k in range(14):
        wx = (k * 37 + f * 3) % VUELTA - 16
        wy = 66 + (k * 11) % 30
        d.line([wx, wy, wx + 6, wy], fill=(170, 206, 186))
        if (f + k) % 5 == 0:
            d.point([(wx + 3, wy - 1), (wx + 2, wy - 1), (wx + 4, wy - 1)], fill=(250, 255, 250))
    # fauna de la laguna
    laguna_fauna(d, p, f)
    # pájaros en el cielo
    for k in range(2):
        bx = (40 + k * 90 + f * 3) % VUELTA - 16
        by = 22 + k * 8 + (1 if (f + k) % 4 < 2 else 0)
        ala = 1 if (f + k) % 2 else -1
        d.line([bx - 3, by + ala, bx, by, bx + 3, by + ala], fill=(70, 70, 80))
    # pasto
    d.rectangle([0, 96, W, H], fill=(120, 172, 72))
    for _ in range(260):
        x, y = rnd.randint(0, W), rnd.randint(98, H)
        d.line([x, y, x, y - 2], fill=(96, 148, 60) if rnd.random() < .6 else (150, 196, 90))
    d.line([0, 96, W, 96], fill=(100, 150, 66))
    # árbol grande a la izquierda (tronco) y follaje arriba
    d.rectangle([0, 0, 14, 118], fill=(120, 96, 76))
    for y in range(0, 118, 5):
        d.line([2, y, 6, y + 3], fill=(96, 76, 60))
        d.line([9, y + 2, 12, y + 4], fill=(150, 124, 100))
    rnd2 = random.Random(11)
    copa(d, 18, 6, 18, (70, 130, 60), (110, 170, 80), (50, 100, 46), rnd2)
    # árbol grande a la derecha
    d.rectangle([222, 30, 228, 98], fill=(96, 76, 60))
    d.line([224, 60, 236, 86], fill=(96, 76, 60), width=2)
    copa(d, 232, 26, 26, (70, 130, 60), (110, 170, 80), (50, 100, 46), rnd2)
    # letrero informativo a la izquierda
    d.rectangle([2, 96, 14, 128], fill=(246, 246, 250))
    d.rectangle([2, 96, 14, 102], fill=(40, 90, 170))
    for yy in range(105, 126, 3):
        d.line([4, yy, 12, yy], fill=(150, 170, 200))
    # poste oscuro delgado
    d.line([60, 30, 58, 144], fill=(50, 50, 56), width=2)
    return im

MADERA = (204, 150, 92)
MADERA_OSC = (160, 108, 62)
MADERA_CLARA = (226, 178, 118)

def glorieta_atras(d):
    """Lo que queda detrás de los personajes: piso, postes de atrás y baranda del fondo."""
    # piso de tablas
    d.polygon([(70, 106), (190, 106), (196, 114), (64, 114)], fill=(160, 152, 140))
    for x in range(70, 192, 6):
        d.line([x, 106, x - 3 + (x - 70) // 20, 114], fill=(138, 130, 120))
    d.rectangle([64, 114, 196, 118], fill=MADERA_OSC)
    # postes del fondo (más delgados)
    for x in (82, 174):
        d.rectangle([x, 46, x + 2, 106], fill=MADERA_OSC)
    # baranda del fondo
    d.rectangle([82, 84, 176, 85], fill=MADERA_OSC)

def glorieta_delante(d, im):
    """Postes de adelante, barandas laterales, techo, letrero y rampa."""
    # rampa de cemento a la derecha
    d.polygon([(190, 112), (204, 112), (238, 138), (214, 140)], fill=(196, 196, 192))
    d.line([190, 112, 214, 140], fill=(170, 170, 166))
    # barandas laterales con travesaños
    for (x0, x1) in ((68, 96), (162, 192)):
        d.rectangle([x0, 82, x1, 84], fill=MADERA)
        d.line([x0, 85, x1, 85], fill=MADERA_OSC)
        d.rectangle([x0, 96, x1, 97], fill=MADERA_OSC)
    # postes de adelante
    for x in (66, 96, 160, 190):
        d.rectangle([x, 40, x + 4, 114], fill=MADERA)
        d.line([x + 4, 40, x + 4, 114], fill=MADERA_OSC)
        d.line([x, 40, x, 114], fill=MADERA_CLARA)
    # viga y diagonales bajo el techo
    d.rectangle([62, 38, 198, 41], fill=MADERA)
    d.line([62, 41, 198, 41], fill=MADERA_OSC)
    for (xa, xb) in ((70, 80), (100, 110), (156, 146), (186, 176)):
        d.line([xa, 50, xb, 42], fill=MADERA, width=2)
    # letrero blanco en la viga
    d.rectangle([116, 42, 144, 48], fill=(250, 250, 248))
    d.rectangle([116, 42, 144, 48], outline=(120, 110, 100))
    for xx in range(119, 142, 3):
        d.point((xx, 45), fill=(80, 90, 120))
    # techo de calamina roja
    d.polygon([(54, 38), (206, 38), (184, 22), (76, 22)], fill=(150, 62, 52))
    for x in range(58, 204, 4):
        xt = 76 + (x - 54) * (184 - 76) / (206 - 54)
        d.line([x, 37, xt, 23], fill=(124, 48, 42))
    d.line([76, 22, 184, 22], fill=(180, 84, 70))
    d.line([54, 38, 206, 38], fill=(110, 40, 36))

frames = []
for f in range(F):
    im = fondo(f)
    d = ImageDraw.Draw(im)
    glorieta_atras(d)
    # los dos, de espalda, mirando la laguna (respiran en contrafase)
    r1 = 1 if (f // 4) % 2 else 0
    r2 = 0 if (f // 4) % 2 else 1
    ex, ey = 110, 113 - len(EL_ESPALDA) - r1 + 1
    dx, dy = 125, 113 - len(ELLA_ESPALDA) - r2 + 1
    pegar(im, EL_ESPALDA, ex, ey)
    pegar(im, ELLA_ESPALDA, dx, dy)
    # manos tomadas
    pm = im.load()
    for xx in range(ex + 14, dx + 2):
        pm[xx, ey + 18] = PAL['S']
    glorieta_delante(d, im)
    # corazones que suben sobre ellos hacia la laguna
    for k in range(2):
        t = ((f + k * 8) % 16) / 16
        if t < .85:
            corazon(im, 120 + k * 5 + int(2 * math.sin(t * 6.28 + k)), int(78 - t * 26), (255, 110, 140) if k == 0 else (255, 170, 190))
    frames.append(im.resize((W * K, H * K), Image.NEAREST))

frames[0].save(OUT + '.gif', save_all=True, append_images=frames[1:], duration=110, loop=0, optimize=True)
frames[0].save(OUT + '_f0.png')
print('ok')
