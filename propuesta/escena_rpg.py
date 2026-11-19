import sys, math, random
from PIL import Image, ImageDraw

OUT = sys.argv[1]
W, H = 256, 144
K = 4

C = {
    'sea': (56, 196, 222), 'sea2': (88, 214, 236), 'spark': (235, 252, 255),
    'g1': (108, 194, 74), 'g2': (88, 170, 60), 'g3': (140, 214, 92), 'gedge': (70, 140, 52),
    'rock': (150, 160, 172), 'rock2': (110, 120, 134), 'rock3': (190, 198, 208), 'rockd': (78, 86, 98),
    'wood': (156, 104, 60), 'wood2': (112, 72, 38), 'wood3': (190, 136, 84),
    'path': (226, 192, 140), 'path2': (206, 168, 116), 'pathe': (184, 132, 84),
    'roof': (58, 50, 66), 'roof2': (84, 74, 94), 'red': (204, 52, 60), 'red2': (160, 34, 44), 'redl': (234, 96, 96),
    'win': (240, 232, 214), 'door': (120, 70, 40),
    'tg': (96, 176, 62), 'tg2': (70, 140, 46), 'ty': (232, 220, 70), 'to': (226, 124, 52), 'to2': (180, 84, 30),
    'fl1': (255, 255, 255), 'fl2': (255, 140, 170), 'fl3': (120, 160, 255),
    'out': (42, 28, 30),
}

img0 = Image.new('RGB', (W, H), C['sea'])
d = ImageDraw.Draw(img0)
px = img0.load()

def rect(x0, y0, x1, y1, c):
    d.rectangle([x0, y0, x1, y1], fill=C[c] if isinstance(c, str) else c)

# mar con ondas
for y in range(H):
    for x in range(W):
        if (x * 3 + y * 7) % 23 == 0 or (x + y * 5) % 37 == 0:
            px[x, y] = C['sea2']

# meseta de pasto
PL, PR, PB = 46, 210, 100
rect(PL, 0, PR, PB, 'g1')
random.seed(7)
for _ in range(900):
    x, y = random.randint(PL, PR), random.randint(0, PB)
    px[x, y] = C['g2'] if random.random() < .6 else C['g3']
rect(PL, PB - 2, PR, PB, 'gedge')
for x in range(PL, PR + 1, 3):
    px[x, PB + 1] = C['gedge']

# acantilado de piedra
rect(PL, PB + 1, PR, H - 1, 'rock2')
for yy in range(PB + 2, H, 6):
    off = 0 if (yy // 6) % 2 else 4
    for xx in range(PL + off, PR, 8):
        d.ellipse([xx, yy, xx + 6, yy + 4], fill=C['rock'])
        d.point([(xx + 2, yy + 1), (xx + 3, yy + 1)], fill=C['rock3'])
        d.line([xx + 1, yy + 4, xx + 5, yy + 4], fill=C['rockd'])
d.line([PL, PB + 1, PL, H], fill=C['rockd']); d.line([PR, PB + 1, PR, H], fill=C['rockd'])

# islas laterales abajo
for (x0, x1) in [(0, 40), (216, 255)]:
    rect(x0, 112, x1, H - 1, 'g1')
    for _ in range(80):
        px[random.randint(x0, x1), random.randint(112, H - 1)] = C['g2']
    d.line([x0, 112, x1, 112], fill=C['gedge'])

# camino
for y in range(30, PB + 1):
    wob = int(1.5 * math.sin(y / 6))
    xl, xr = 114 + wob, 142 + wob
    d.line([xl, y, xr, y], fill=C['path'])
    px[xl, y] = C['pathe']; px[xr, y] = C['pathe']
for _ in range(60):
    x, y = random.randint(117, 139), random.randint(32, PB)
    px[x, y] = C['path2']

# escalera de madera
SX0, SX1 = 110, 146
rect(SX0, PB - 4, SX1, H - 1, 'wood')
for y in range(PB - 2, H, 4):
    d.line([SX0 + 3, y, SX1 - 3, y], fill=C['wood2'])
    d.line([SX0 + 3, y - 1, SX1 - 3, y - 1], fill=C['wood3'])
rect(SX0, PB - 6, SX0 + 3, H - 1, 'wood2'); rect(SX1 - 3, PB - 6, SX1, H - 1, 'wood2')
for (x0) in (SX0, SX1 - 3):
    rect(x0, PB - 8, x0 + 3, PB - 6, 'wood3')

# casita (techo, paredes, puerta, ventanas, baranda)
HX0, HX1 = 94, 162
rect(HX0 + 8, 0, HX1 - 8, 4, 'roof')
rect(HX0, 4, HX1, 14, 'roof')
for x in range(HX0, HX1 + 1, 4):
    d.line([x, 5, x + 2, 5], fill=C['roof2'])
d.line([HX0 - 2, 14, HX1 + 2, 14], fill=C['red']); d.line([HX0 - 2, 15, HX1 + 2, 15], fill=C['red2'])
# corazón en el frontón
for (x, y) in [(127, 7), (129, 7), (126, 8), (127, 8), (128, 8), (129, 8), (130, 8), (127, 9), (128, 9), (129, 9), (128, 10)]:
    px[x, y] = C['redl']
rect(HX0 + 4, 16, HX1 - 4, 34, 'red')
d.line([HX0 + 4, 16, HX1 - 4, 16], fill=C['red2'])
for wx in (HX0 + 9, HX1 - 21):
    rect(wx, 19, wx + 12, 27, 'win'); d.rectangle([wx, 19, wx + 12, 27], outline=C['red2'])
    for k in range(wx + 3, wx + 12, 3):
        d.line([k, 20, k, 26], fill=C['wood2'])
rect(122, 20, 134, 34, 'door'); d.rectangle([122, 20, 134, 34], outline=C['wood2'])
d.line([128, 21, 128, 33], fill=C['wood2']); px[126, 28] = C['ty']; px[130, 28] = C['ty']
rect(HX0 + 2, 30, HX1 - 2, 36, 'red2')
for x in range(HX0 + 4, HX1 - 2, 4):
    d.line([x, 31, x, 35], fill=C['redl'])
rect(118, 35, 138, 38, 'red2')

# árboles (pinos por capas con punta amarilla y base naranja)
def arbol(cx, cy):
    rect(cx - 3, cy + 14, cx + 3, cy + 18, 'to2')
    d.polygon([(cx - 8, cy + 18), (cx, cy + 12), (cx + 8, cy + 18)], fill=C['to'])
    for i, (w, y) in enumerate([(12, 12), (10, 6), (7, 0)]):
        d.polygon([(cx - w, cy + y + 8), (cx, cy + y - 2), (cx + w, cy + y + 8)], fill=C['tg2'])
        d.polygon([(cx - w + 2, cy + y + 6), (cx, cy + y - 1), (cx + w - 2, cy + y + 6)], fill=C['tg'])
    d.polygon([(cx - 3, cy + 2), (cx, cy - 3), (cx + 3, cy + 2)], fill=C['ty'])
    d.point([(cx - 5, cy + 9), (cx + 6, cy + 15), (cx - 8, cy + 19)], fill=C['ty'])

for (x, y) in [(60, 2), (82, 4), (174, 4), (196, 2), (58, 30), (198, 30), (66, 58), (190, 58), (16, 112), (36, 118), (222, 112), (242, 118)]:
    arbol(x, y)

# flores
FLORES = [(90, 50), (100, 72), (160, 46), (170, 80), (84, 88), (178, 64), (152, 92), (96, 92), (74, 76), (184, 90)]
for i, (x, y) in enumerate(FLORES):
    c = ['fl1', 'fl2', 'fl3'][i % 3]
    for (a, b) in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
        px[x + a, y + b] = C[c]
    px[x, y] = C['ty']

base = img0

# ---------- personajes ----------
PAL = {
    'O': (42, 28, 30), 'H': (43, 33, 32), 'h': (82, 62, 56), 'S': (236, 186, 148), 's': (204, 146, 112),
    'E': (30, 22, 24), 'M': (190, 90, 84), 'W': (246, 243, 238), 'w': (206, 200, 216),
    'P': (64, 78, 112), 'p': (44, 54, 82), 'B': (60, 42, 40), 'R': (178, 30, 44), 'T': (236, 210, 168), 't': (206, 174, 128),
    'G': (222, 222, 226), 'K': (250, 150, 150),
}
EL = [
    "....OOOOOO....",
    "...OHHHHHHO...",
    "..OHHhhHHHHO..",
    "..OHHHHHHHHO..",
    "..OHHSHHSHHO..",
    "..OHSSSSSSHO..",
    "..OSSESSESSO..",
    "..OSKSSSSKSO..",
    "...OSSMMSSO...",
    "....OOSSOO....",
    "...OWWWWWWO...",
    "..OWWWWWWWWO..",
    ".OSOWWWWWWOSO.",
    ".OSOWWWWWWOSO.",
    "..OOwwwwwwOO..",
    "...OPPPPPPO...",
    "...OPPOOPPO...",
    "...OPpOOpPO...",
    "...OBBOOBBO...",
    "...OOOOOOOO...",
]
ELLA = [
    "....OOOOOO....",
    "...OHHHHHHO...",
    "..OHHhhHHHHO..",
    ".OHHHHHHHHhHO.",
    ".OHhSHSSHSHHO.",
    ".OHSSSSSSSSHO.",
    ".OHRRRSSRRRHO.",
    ".OhRESRRSERhO.",
    ".OHSRRSSRRSHO.",
    ".OHSKSSSSKSHO.",
    "OHhGSSMMSSGhHO",
    "OHHHOOSSOOHHHO",
    "OhHOTTTTTTOHhO",
    "OHHTTTTTTTTHHO",
    "OHhSTTTTTTShHO",
    "OHHOttttttOHHO",
    ".OhOPPPPPPOhO.",
    "..OOPPOOPPOO..",
    "...OPpOOpPO...",
    "...OBBOOBBO...",
    "...OOOOOOOO...",
]
for spr in (EL, ELLA):
    assert all(len(r) == 14 for r in spr), [len(r) for r in spr]

def pegar(im, spr, x0, y0):
    p = im.load()
    for y, row in enumerate(spr):
        for x, ch in enumerate(row):
            if ch != '.':
                p[x0 + x, y0 + y] = PAL[ch]

def sombra(im, cx, cy):
    p = im.load()
    for x in range(cx - 6, cx + 7):
        for y in (cy, cy + 1):
            r, g, b = p[x, y]
            p[x, y] = (int(r * .8), int(g * .8), int(b * .8))

CORAZON = ["0110110", "1111111", "1111111", "0111110", "0011100", "0001000"]

def burbuja(im, x0, y0):
    dd = ImageDraw.Draw(im)
    dd.rounded_rectangle([x0, y0, x0 + 14, y0 + 11], radius=4, fill=(250, 250, 252), outline=PAL['O'])
    dd.polygon([(x0 + 5, y0 + 11), (x0 + 7, y0 + 14), (x0 + 9, y0 + 11)], fill=(250, 250, 252))
    dd.line([x0 + 5, y0 + 11, x0 + 7, y0 + 14], fill=PAL['O']); dd.line([x0 + 7, y0 + 14, x0 + 9, y0 + 11], fill=PAL['O'])
    p = im.load()
    for r, row in enumerate(CORAZON):
        for c, v in enumerate(row):
            if v == '1':
                p[x0 + 4 + c, y0 + 3 + r] = (224, 48, 63)

frames = []
F = 12
for f in range(F):
    im = base.copy()
    p = im.load()
    # destellos del mar
    for j in range(14):
        sx = (j * 53 + 11) % W
        if PL - 2 < sx < PR + 2:
            sx = (sx + 170) % W
        sy = (j * 29 + 7) % 108
        if (f + j) % 4 == 0:
            for (a, b) in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= sx + a < W and 0 <= sy + b < H:
                    p[sx + a, sy + b] = C['spark']
        elif (f + j) % 4 == 1:
            p[sx, sy] = C['spark']
    # personajes: respiran en contrafase
    b1 = 1 if f % 6 < 3 else 0
    b2 = 1 if (f + 3) % 6 < 3 else 0
    sombra(im, 121, 79); sombra(im, 137, 79)
    pegar(im, EL, 114, 60 + b1)
    pegar(im, ELLA, 130, 59 + b2)
    # manos tomadas
    for x in range(126, 134):
        p[x, 73] = PAL['S']; p[x, 74] = PAL['O']
    # burbuja con corazón que flota
    by = 40 + (0 if f % 4 < 2 else -1)
    burbuja(im, 122, by)
    # corazoncito que sube
    t = f / F
    hy = int(38 - t * 24); hx = 140 + int(2 * math.sin(t * 6.28))
    if t < .9:
        for (a, b) in [(0, 0), (2, 0), (-1, 1), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (1, 3)]:
            p[hx + a, hy + b] = (255, 120, 150)
    frames.append(im.resize((W * K, H * K), Image.NEAREST))

frames[0].save(OUT + '.gif', save_all=True, append_images=frames[1:], duration=140, loop=0, optimize=True)
frames[0].save(OUT + '_f0.png')
print('ok')
