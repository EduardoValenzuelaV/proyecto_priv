"""Escena pixel: los dos corriendo de la mano bajo la lluvia en la ciudad.
Uso: python propuesta/escena_lluvia.py assets/pixel/lluvia   (genera lluvia.gif y lluvia_f0.png)
"""
import sys, math, random
from PIL import Image, ImageDraw

OUT = sys.argv[1] if len(sys.argv) > 1 else 'lluvia'
W, H, K, F = 256, 144, 2, 16

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

# ---------- capas que se desplazan (se repiten en un periodo exacto para que el GIF haga loop) ----------
def capa_edificios(periodo, seed, alto_min, alto_max, color, ventana, prob_luz, base_y):
    random.seed(seed)
    ancho = W + periodo
    im = Image.new('RGBA', (ancho, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x = 0
    edificios = []
    while x < periodo:
        w = random.randint(18, 34)
        w = min(w, periodo - x) if periodo - x < 18 + 4 else w
        h = random.randint(alto_min, alto_max)
        edificios.append((x, w, h))
        x += w + random.randint(1, 3)
    for rep in range(0, ancho, periodo):
        for (bx, w, h) in edificios:
            x0 = bx + rep
            d.rectangle([x0, base_y - h, x0 + w - 1, base_y], fill=color)
            d.line([x0, base_y - h, x0 + w - 1, base_y - h], fill=lerp(color, (255, 255, 255), .12))
            rnd = random.Random(bx * 31 + h)
            for wy in range(base_y - h + 4, base_y - 4, 6):
                for wx in range(x0 + 3, x0 + w - 4, 5):
                    if rnd.random() < prob_luz:
                        d.rectangle([wx, wy, wx + 2, wy + 2], fill=ventana)
                    else:
                        d.rectangle([wx, wy, wx + 2, wy + 2], fill=lerp(color, (0, 0, 0), .25))
    return im

cielo = Image.new('RGB', (W, H))
pc = cielo.load()
for y in range(H):
    c = lerp((28, 34, 58), (74, 86, 120), y / 110)
    for x in range(W):
        pc[x, y] = c

lejos = capa_edificios(48 * 2, 3, 30, 62, (52, 62, 92), (150, 140, 110), .25, 108)
cerca = capa_edificios(96 * 2, 9, 40, 84, (34, 40, 64), (246, 208, 120), .4, 108)

# farolas en la capa cercana (periodo 96)
dc = ImageDraw.Draw(cerca)
for rep in range(0, cerca.width, 96):
    fx = rep + 60
    dc.rectangle([fx, 70, fx + 1, 108], fill=(24, 26, 36))
    dc.rectangle([fx - 3, 68, fx + 4, 70], fill=(24, 26, 36))
    dc.rectangle([fx - 2, 71, fx + 3, 72], fill=(255, 236, 170))

def escena_base(f):
    im = cielo.copy()
    # luna borrosa entre nubes
    d = ImageDraw.Draw(im)
    d.ellipse([200, 10, 214, 24], fill=(200, 205, 225))
    for (x, y, w) in [(170, 18, 50), (196, 26, 40), (40, 12, 60), (90, 20, 44)]:
        d.rounded_rectangle([x, y, x + w, y + 7], radius=3, fill=(60, 70, 100))
    im.paste(lejos.crop((f * 6, 0, f * 6 + W, H)), (0, 0), lejos.crop((f * 6, 0, f * 6 + W, H)))
    im.paste(cerca.crop((f * 12, 0, f * 12 + W, H)), (0, 0), cerca.crop((f * 12, 0, f * 12 + W, H)))
    d = ImageDraw.Draw(im)
    # halos de las farolas sobre la vereda
    # vereda y calle
    d.rectangle([0, 108, W, 116], fill=(92, 98, 118))
    for x in range(-(f * 12) % 16 - 16, W, 16):
        d.line([x, 108, x, 116], fill=(78, 84, 102))
    d.line([0, 108, W, 108], fill=(130, 138, 160))
    d.rectangle([0, 117, W, H], fill=(48, 52, 66))
    d.line([0, 117, W, 117], fill=(36, 38, 50))
    for x in range(-(f * 16) % 32 - 32, W, 32):
        d.rectangle([x, 130, x + 14, 131], fill=(220, 210, 150))
    # reflejos de ventanas en el asfalto mojado
    px = im.load()
    for y in range(118, H):
        for x in range(0, W, 1):
            sy = 108 - (y - 117) * 2
            if 0 <= sy < 108 and (x + y) % 3 == 0:
                r, g, b = px[x, sy]
                if r > 200 and g > 170:
                    px[x, y] = lerp(px[x, y], (r, g, b), .45)
    # charcos
    for (cx, w) in [(30, 26), (120, 34), (210, 22)]:
        x0 = (cx - f * 16) % (W + 40) - 20
        d.ellipse([x0, 121, x0 + w, 126], fill=(84, 100, 140))
        d.line([x0 + 4, 123, x0 + w - 6, 123], fill=(130, 150, 190))
    return im

# ---------- personajes (de perfil, mirando a la derecha) ----------
PAL = {
    'O': (34, 22, 26),
    # pelo
    'H': (44, 30, 30), 'h': (78, 52, 46), 'c': (126, 88, 72),
    # piel
    'S': (234, 182, 142), 's': (206, 148, 112), 'K': (242, 140, 140), 'E': (30, 22, 24), 'M': (204, 90, 96),
    # lentes y aro (Dallana)
    'R': (196, 32, 48), 'L': (222, 238, 248), 'G': (230, 230, 236),
    # chaqueta morada (Dallana)
    'V': (128, 78, 190), 'v': (92, 52, 148), 'u': (172, 128, 224),
    'T': (242, 216, 172),
    # chaqueta negra con azul (él)
    'N': (36, 36, 46), 'n': (60, 62, 78), 'A': (52, 112, 214), 'a': (110, 164, 240),
    'W': (248, 246, 242),
    # jeans y zapatillas
    'P': (66, 84, 124), 'p': (46, 58, 90), 'Z': (246, 244, 240), 'z': (196, 192, 200),
}

ELLA_ARRIBA = [
    ".........OOOOOO",
    "......OOOHHhHHHOO",
    ".....OHHcHHHHHhHHO",
    "....OHHHHHHhHHHHHHO",
    "...OHhHHcHHHHHHHhHHO",
    "...OHHHHHHHHHHHHHHHHO",
    "..OHcHHhHHHHHHHHHSSSO",
    "..OHHHHHHHHHHHHSSSSSSO",
    ".OHHcHHHhHHHHHSSSOOOSO",
    ".OHHHHHHHHHRRRRRRRRRSO",
    ".OHcHHHhHHHHSSSRLEERSSO",
    ".OHHHHHHHHHHGSSRLLLRSSSO",
    "OHHcHHHhHHHGSGSRRRRRSSO",
    "OHHHHHHHHHHHGSSSSSKKSSO",
    "OHcHHHhHHHHHHSSSSSSMMO",
    "OHHHHHHcHHHHHOSSSSSSO",
    ".OHHcHHHHhHHHHOSSSSO",
    ".OHHHHHHHHHHOVVuSSuVO",
    "OHHcHHHhHHHOVVVuTTuVVO",
    "OHHHHHHHHHOVVVVuTTTuVVO",
    "OHcHHhHHHOVVVVVuTTTuVVVO",
    ".OHHcHHHOVVVvVVuTTTuVVVVOOOO",
    ".OHHHHHOVVVVvVVuTTTuVVVVVVSSO",
    "..OHHcOVVVVvVVVuTTTuVVOOOOOO",
    "...OOOVVVVVvVVVuTTTuVO",
    "....OvvvvvvvvvvvvvvvvO",
]
ELLA_PIERNAS = [
    [
        "......OPPPPPPPPPPPO",
        ".....OPPPPPOOOPPPPPO",
        "....OPPPPO....OPPPPO",
        "...OPPPPO......OPPPO",
        "..OPPPO.........OPPPO",
        ".OZZZO..........OPPPO",
        ".OZZZZO.........OZZZZO",
        "..OOOOO.........OOOOOO",
    ],
    [
        "......OPPPPPPPPPPPO",
        "......OPPPPPPPPPPO",
        ".......OPPPOOPPPO",
        ".......OPPPOOPPPO",
        ".......OPPPOOPPPO",
        "......OZZZOOOPPPO",
        "......OZZZZOOZZZZO",
        ".......OOOOOOOOOOO",
    ],
]

EL_ARRIBA = [
    ".......OOOOOOO",
    ".....OOHHHHHHHOO",
    "....OHHhHHHHHHHHO",
    "...OHHHHHHHhHHHHHO",
    "...OHHHHHHHHHHHHHHO",
    "...OHhHHHHHHHHHSSHO",
    "...OHHHHHHHHHSSSSSO",
    "....OHHHHHHSSSSSSSO",
    "....OHHHHHHSSSOOOSSO",
    "....OHHHSSSSSSSESSSO",
    "....OHSSsSSSSSSSSSSSO",
    "....OSSssSSSSSSKSSSO",
    ".....OSSSSSSSSSSMMO",
    "......OSSSSSSSSSSO",
    ".......OOSSSSSOO",
    "......ONnASSSANnO",
    ".....ONNNAWWWANNNO",
    "....ONNNNAWWWANNNNO",
    "OOOONNNNNAWWWANNNNO",
    "SSONNNnNNAWWWANNNNO",
    "OOONNNnNNAWWWANNNNO",
    "....ONNnNAWWWANNNNO",
    "....ONNNNAWWWANNNNO",
    ".....OAAAAAAAAAAAAO",
]
EL_PIERNAS = [
    [
        "......OPPPPPPPPPO",
        ".....OPPPPOOPPPPPO",
        "....OPPPPO..OPPPPO",
        "...OPPPPO....OPPPO",
        "..OPPPO.......OPPPO",
        ".ONNNO........OPPPO",
        ".ONAAAO.......ONAAAO",
        "..OOOOO.......OOOOOO",
    ],
    [
        "......OPPPPPPPPPO",
        "......OPPPPPPPPO",
        ".......OPPPOPPPO",
        ".......OPPPOPPPO",
        ".......OPPPOPPPO",
        "......ONNNOOPPPO",
        "......ONAAAOONAAAO",
        ".......OOOOOOOOOOO",
    ],
]

def pegar(im, filas, x0, y0):
    p = im.load()
    for y, fila in enumerate(filas):
        for x, ch in enumerate(fila):
            if ch != '.' and 0 <= x0 + x < W and 0 <= y0 + y < H:
                p[x0 + x, y0 + y] = PAL[ch]

CORAZON = ["0110110", "1111111", "1111111", "0111110", "0011100", "0001000"]

frames = []
random.seed(21)
gotas = [(random.randint(0, W), random.randint(0, H), random.choice([5, 6, 7])) for _ in range(150)]
for f in range(F):
    im = escena_base(f)
    paso = (f // 2) % 2
    rebote = 1 if paso == 1 else 0
    ex, ey = 88, 74 - rebote
    hx0, hy0 = ex + 28, 76 - (1 - rebote)
    pegar(im, ELLA_ARRIBA + ELLA_PIERNAS[paso], ex, ey)
    pegar(im, EL_ARRIBA + EL_PIERNAS[1 - paso], hx0, hy0)
    # manos tomadas: une la mano de ella con la de él
    pm = im.load()
    for yy in sorted({ey + 22, hy0 + 19}):
        for xx in range(ex + 26, hx0 + 2):
            pm[xx, yy] = PAL['S']
    # salpicaduras en los pies
    d = ImageDraw.Draw(im)
    if paso == 0:
        for (sx, sy) in [(ex + 3, 108), (ex + 46, 108)]:
            d.point([(sx - 2, sy - 2), (sx + 3, sy - 3), (sx, sy - 4), (sx + 5, sy - 1)], fill=(170, 200, 240))
    # lluvia: cae 8 px por frame (loop exacto en 16 frames con alto 128)
    for (gx, gy, largo) in gotas:
        y = (gy + f * 9) % (H + 0)
        x = (gx - f * 3) % W
        d.line([x, y, x - 2, y + largo], fill=(170, 196, 236))
    # gotas que rebotan en la calle
    for j in range(10):
        if (f + j) % 4 == 0:
            rx = (j * 47 + f * 13) % W
            ry = 119 + (j * 7) % 22
            d.point([(rx - 1, ry), (rx + 1, ry), (rx, ry - 1)], fill=(190, 210, 245))
    # corazoncito que sube entre los dos
    t = (f % 8) / 8
    hx, hy = ex + 25 + int(2 * math.sin(t * 6.28)), int(ey - 4 - t * 18)
    p = im.load()
    for r, fila in enumerate(CORAZON):
        for c, v in enumerate(fila):
            if v == '1':
                p[hx + c, hy + r] = (255, 110, 140)
    frames.append(im.resize((W * K, H * K), Image.NEAREST))

frames[0].save(OUT + '.gif', save_all=True, append_images=frames[1:], duration=90, loop=0, optimize=True)
frames[0].save(OUT + '_f0.png')
print('ok')
