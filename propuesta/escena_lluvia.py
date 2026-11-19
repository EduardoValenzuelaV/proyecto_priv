"""Escena pixel: los dos corriendo de la mano bajo la lluvia en la ciudad.
Uso: python propuesta/escena_lluvia.py assets/pixel/lluvia   (genera lluvia.gif y lluvia_f0.png)
"""
import sys, math, random
from PIL import Image, ImageDraw

OUT = sys.argv[1] if len(sys.argv) > 1 else 'lluvia'
W, H, K, F = 256, 144, 2, 24

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
        edificios.append((x, w, h, random.choice(color) if isinstance(color, list) else color))
        x += w + random.randint(1, 3)
    for rep in range(0, ancho, periodo):
        for (bx, w, h, color_e) in edificios:
            x0 = bx + rep
            d.rectangle([x0, base_y - h, x0 + w - 1, base_y], fill=color_e)
            d.line([x0, base_y - h, x0 + w - 1, base_y - h], fill=lerp(color_e, (255, 255, 255), .2))
            rnd = random.Random(bx * 31 + h)
            for wy in range(base_y - h + 4, base_y - 4, 6):
                for wx in range(x0 + 3, x0 + w - 4, 5):
                    if rnd.random() < prob_luz:
                        d.rectangle([wx, wy, wx + 2, wy + 2], fill=ventana)
                    else:
                        d.rectangle([wx, wy, wx + 2, wy + 2], fill=lerp(color_e, (0, 0, 0), .2))
    return im

cielo = Image.new('RGB', (W, H))
pc = cielo.load()
for y in range(H):
    c = lerp((156, 176, 200), (206, 218, 230), y / 110)
    for x in range(W):
        pc[x, y] = c

lejos = capa_edificios(48 * 2, 3, 30, 62, (160, 172, 192), (196, 208, 224), .5, 108)
cerca = capa_edificios(96 * 2, 9, 40, 84, [(120, 134, 160), (184, 142, 118), (206, 178, 140), (140, 160, 140), (196, 150, 160)], (214, 228, 242), .55, 108)

# farolas en la capa cercana (periodo 96)
dc = ImageDraw.Draw(cerca)
for rep in range(0, cerca.width, 96):
    fx = rep + 60
    dc.rectangle([fx, 70, fx + 1, 108], fill=(70, 78, 94))
    dc.rectangle([fx - 3, 68, fx + 4, 70], fill=(70, 78, 94))
    dc.rectangle([fx - 2, 71, fx + 3, 72], fill=(226, 230, 236))

def escena_base(f):
    im = cielo.copy()
    # luna borrosa entre nubes
    d = ImageDraw.Draw(im)
    for (x, y, w) in [(160, 10, 70), (196, 22, 50), (20, 8, 80), (90, 18, 56), (230, 4, 40)]:
        d.rounded_rectangle([x, y, x + w, y + 10], radius=5, fill=(222, 228, 236))
        d.rounded_rectangle([x + 6, y - 4, x + w - 10, y + 4], radius=4, fill=(232, 236, 242))
        d.line([x + 3, y + 10, x + w - 3, y + 10], fill=(196, 206, 220))
    im.paste(lejos.crop((f * 4, 0, f * 4 + W, H)), (0, 0), lejos.crop((f * 4, 0, f * 4 + W, H)))
    im.paste(cerca.crop((f * 8, 0, f * 8 + W, H)), (0, 0), cerca.crop((f * 8, 0, f * 8 + W, H)))
    d = ImageDraw.Draw(im)
    # halos de las farolas sobre la vereda
    # vereda y calle
    d.rectangle([0, 108, W, 116], fill=(170, 174, 184))
    for x in range(-(f * 8) % 16 - 16, W, 16):
        d.line([x, 108, x, 116], fill=(150, 154, 166))
    d.line([0, 108, W, 108], fill=(200, 204, 212))
    d.rectangle([0, 117, W, H], fill=(104, 110, 124))
    d.line([0, 117, W, 117], fill=(86, 90, 104))
    for x in range(-(f * 8) % 32 - 32, W, 32):
        d.rectangle([x, 130, x + 14, 131], fill=(236, 226, 170))
    # reflejos de ventanas en el asfalto mojado
    px = im.load()
    for y in range(118, H):
        for x in range(0, W, 1):
            sy = 108 - (y - 117) * 2
            if 0 <= sy < 108 and (x + y) % 3 == 0:
                r, g, b = px[x, sy]
                px[x, y] = lerp(px[x, y], (r, g, b), .22)
    # charcos
    for (cx, w) in [(30, 26), (120, 34), (210, 22)]:
        x0 = (cx - f * 8) % (W + 128) - 20
        d.ellipse([x0, 121, x0 + w, 126], fill=(150, 168, 196))
        d.line([x0 + 4, 123, x0 + w - 6, 123], fill=(206, 220, 238))
    return im

# ---------- personajes (de perfil, mirando a la derecha) ----------
PAL = {
    'O': (34, 22, 26),
    # pelo
    'H': (44, 30, 30), 'h': (78, 52, 46), 'c': (130, 90, 72),
    # piel
    'S': (236, 186, 146), 's': (204, 146, 110), 'K': (244, 138, 140), 'E': (30, 22, 24), 'M': (206, 88, 98),
    # lentes y aro (Dallana)
    'R': (200, 32, 50), 'L': (226, 240, 250), 'G': (232, 232, 238),
    # chaqueta morada (Dallana)
    'V': (128, 78, 190), 'v': (92, 52, 148), 'u': (176, 132, 228),
    'T': (244, 218, 176),
    # chaqueta negra con azul (Eduardo)
    'N': (36, 36, 46), 'n': (64, 66, 84), 'A': (52, 112, 214), 'a': (120, 172, 244),
    'W': (248, 246, 242),
    # jeans y zapatillas
    'P': (68, 88, 130), 'p': (46, 58, 92), 'Z': (248, 246, 242), 'z': (192, 188, 200),
}

ELLA_ARRIBA = [
    "..........OO.OOO",
    "........OOccOHHcOO",
    "......OOHHHHhHHHHhOO",
    ".....OHHcHHHHHhHHHHHO",
    "....OHHHHHhcHHHHHHhHHO",
    "...OHhHHcHHHHHHHHHHHHO",
    "...OHHHHHHHhHHHHHHHSSO",
    "..OHcHHhHHHHHHHHSSSSSO",
    "..OHHHHHHHHHHHHSSOOOSSO",
    ".OHHcHHHhHHHRRRRRRRRRSO",
    ".OHcHHHhHHHHHsSRLLERSSO",
    "OHHHHHHHHHHHGsSRLLERSSSO",
    "OHHcHHHhHHHGSGSRRRRRSSO",
    "OHcHHHHHHHHHGSSSSSKKSSO",
    "OHHHHhHHHHHHHsSSSSSMMO",
    "OHcHHHHHcHHHHOsSSSSSO",
    ".OHHcHHHHhHHHHOssSSO",
    "OHHHHHHHHHHHOVVussuVO",
    "OHcHHcHHhHHOVVVuTTuVVO",
    "OHHHHHHHHHOVVVVuTTTuVVO",
    ".OHcHHhHHOVVVvVuTTTuVVVO",
    ".OHHHcHHOVVVvVVuTTTuVVVVOOOO",
    "..OHHHHOVVVvVVVuTTTuVVVuuVSSO",
    "..OcHHOVVVVvVVVuTTTuVVOOOOOO",
    "...OOOVVVVVvVVVuTTTuVO",
    "....OvvvvvvvvvvvvvvvvO",
]
ELLA_PIERNAS = [
    [
        "......OPPPPPPPPPPPO",
        ".....OpppPPOOOPPPPPO",
        "....OpppPO....OPPPPO",
        "...OpppPO......OPPPO",
        "..OpppO.........OPPPO",
        ".OZZZO..........OPPPO",
        ".OZZzZO.........OZZzZO",
        "..OOOOO.........OOOOOO",
    ],
    [
        "......OPPPPPPPPPPPO",
        "......OpPPPPPPPPPO",
        ".......OpppOOPPPO",
        ".......OpppOOPPPO",
        ".......OpppOOPPPO",
        "......OZZZOOOPPPO",
        "......OZZzZOOZZzZO",
        ".......OOOOOOOOOOO",
    ],
]

EL_ARRIBA = [
    ".......OOOOOOO",
    ".....OOhhHHHHHOO",
    "....OHHHhcHHHHHHO",
    "...OHHcHHHhHHHHHHOO",
    "..OHHhHHHHHHHhchHHHO",
    "..OHHHHHHHHHHHHHHHHHO",
    "...OHHHHHHHHHHHHHHHO",
    "...OHHHHHHHHHSSSSSSO",
    "....OHHHHHHSSSOOOSSO",
    "....OHHHssSSSSSSWESSO",
    "....OHHsSssSSSSSEESSSO",
    "....OHSssSSSSSSSKSSSO",
    ".....OSSSSSSSSSSSSMO",
    "......OsSSSSSSSSSSO",
    ".......OOssSSSSSOO",
    "......ONnAsssANnO",
    ".....ONNNAWWWANNNO",
    "....ONNNNAWWWANNNNO",
    "OOOONNNNNAWWWANNNNNOO",
    "SSONNNnNNAWWWANNnNNNNSO",
    "OOONNNnNNAWWWANNNnNNSSO",
    "....ONNnNAWWWANNNOOOOO",
    "....ONNNNAWAWANNNNO",
    ".....OAAAAAAAAAAAAO",
]
EL_PIERNAS = [
    [
        "......OPPPPPPPPPO",
        ".....OpppPOOPPPPPO",
        "....OpppPO..OPPPPO",
        "...OpppPO....OPPPO",
        "..OpppO.......OPPPO",
        ".ONNNO........OPPPO",
        ".ONAaAO.......ONAaAO",
        "..OOOOO.......OOOOOO",
    ],
    [
        "......OPPPPPPPPPO",
        "......OpPPPPPPPO",
        ".......OpppOPPPO",
        ".......OpppOPPPO",
        ".......OpppOPPPO",
        "......ONNNOOPPPO",
        "......ONAaAOONAaAO",
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

def espejo_piernas(filas):
    """La otra zancada: invierte las piernas y cambia cuál va sombreada."""
    ancho = max(len(f) for f in filas)
    swap = {'P': 'p', 'p': 'P'}
    return [''.join(swap.get(c, c) for c in f.ljust(ancho, '.')[::-1]) for f in filas]

# ciclo de carrera de 4 poses: zancada, paso, zancada contraria, paso
CICLO_ELLA = [ELLA_PIERNAS[0], ELLA_PIERNAS[1], espejo_piernas(ELLA_PIERNAS[0]), ELLA_PIERNAS[1]]
CICLO_EL = [espejo_piernas(EL_PIERNAS[0]), EL_PIERNAS[1], EL_PIERNAS[0], EL_PIERNAS[1]]
REBOTE = [0, 2, 0, 2]

def mover_brazo_libre(filas, arriba):
    """El brazo de adelante de Eduardo sube y baja al correr."""
    filas = list(filas)
    if arriba:
        filas[18], filas[19], filas[20] = filas[18][:19] + "NSO", filas[19][:19] + "NSO", filas[20][:19] + "OO"
    return filas

def relampago(im, fuerza):
    px = im.load()
    for y in range(0, 108):
        for x in range(W):
            px[x, y] = lerp(px[x, y], (220, 228, 255), fuerza)

frames = []
random.seed(21)
gotas = [(random.randint(0, W), random.randint(0, H), random.choice([3, 4, 5])) for _ in range(85)]
for f in range(F):
    im = escena_base(f)
    pose = (f // 3) % 4
    sub = f % 3
    rebote = REBOTE[pose] if sub != 1 else REBOTE[pose] // 2 + (1 if REBOTE[pose] == 0 else 0)
    rebote_el = rebote
    ex, ey = 88, 74 - rebote
    hx0, hy0 = ex + 28, 77 - rebote_el
    ds = ImageDraw.Draw(im)
    for (sx0, sx1, r) in [(ex + 2, ex + 22, rebote), (hx0 + 2, hx0 + 20, rebote_el)]:
        ds.ellipse([sx0 + r, 106, sx1 - r, 109], fill=(140, 144, 156))
    # el pelo de Dallana rebota un poco detrás del cuerpo
    arriba_ella = [fila for fila in ELLA_ARRIBA]
    pegar(im, arriba_ella + CICLO_ELLA[pose], ex, ey)
    if rebote:
        pm = im.load()
        for yy in range(ey + 14, ey + 24):
            for xx in range(ex, ex + 3):
                if pm[xx, yy] == PAL['H'] or pm[xx, yy] == PAL['c']:
                    pm[xx, yy + 1] = pm[xx, yy]
    pegar(im, mover_brazo_libre(EL_ARRIBA, pose in (1, 2)) + CICLO_EL[pose], hx0, hy0)
    pm = im.load()
    for yy in sorted({ey + 22, hy0 + 19}):
        for xx in range(ex + 26, hx0 + 2):
            pm[xx, yy] = PAL['S']
    d = ImageDraw.Draw(im)
    # salpicaduras cuando un pie toca el suelo
    if pose in (0, 2) and sub == 0:
        for sx in (ex + 4, ex + 18, hx0 + 4, hx0 + 18):
            d.point([(sx - 2, 105), (sx + 3, 104), (sx, 103), (sx + 5, 106), (sx - 4, 106)], fill=(226, 236, 250))
    # lluvia (loop exacto: 6 px x 24 cuadros = 144)
    for (gx, gy, largo) in gotas:
        y = (gy + f * 6) % H
        x = (gx - (f * 32) // 6) % W
        d.line([x, y, x - 1, y + largo], fill=(232, 240, 250))
    for j in range(6):
        if (f + j) % 4 == 0:
            rx = (j * 47 + f * 13) % W
            ry = 119 + (j * 7) % 22
            d.point([(rx - 1, ry), (rx + 1, ry), (rx, ry - 1)], fill=(226, 236, 250))
    # corazones que suben entre los dos
    p = im.load()
    for k in range(2):
        t = ((f + k * 12) % 24) / 24
        hx = ex + 22 + k * 8 + int(2 * math.sin(t * 6.28 + k))
        hy = int(ey - 2 - t * 30)
        if t < .85:
            col = (255, 110, 140) if k == 0 else (255, 160, 190)
            for r, fila in enumerate(CORAZON):
                for c, v in enumerate(fila):
                    if v == '1' and 0 <= hy + r < H:
                        p[hx + c, hy + r] = col
    frames.append(im.resize((W * K, H * K), Image.NEAREST))

frames[0].save(OUT + '.gif', save_all=True, append_images=frames[1:], duration=80, loop=0, optimize=True)
frames[0].save(OUT + '_f0.png')
print('ok')
