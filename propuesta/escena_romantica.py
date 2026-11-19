"""Escena pixel: Eduardo (polerón café) y Dallana (suéter rojo y perlas) sentados cenando hamburguesas
con papas fritas y conversando. Afuera es de día y llueve; hay dos ventanas y una tele.
Uso: python propuesta/escena_romantica.py assets/pixel/cena   (genera cena.gif y cena_f0.png)
"""
import sys, math, random
from PIL import Image, ImageDraw

OUT = sys.argv[1] if len(sys.argv) > 1 else 'cena'
W, H, K, F = 256, 144, 2, 16

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

PAL = {
    'O': (34, 22, 26),
    'H': (44, 30, 30), 'h': (78, 52, 46), 'c': (130, 90, 72),
    'S': (236, 186, 146), 's': (204, 146, 110), 'K': (244, 138, 140), 'E': (30, 22, 24), 'M': (206, 88, 98),
    'R': (200, 32, 50), 'L': (226, 240, 250), 'G': (232, 232, 238), 'W': (248, 246, 242),
    # suéter rojo y perlas (Dallana)
    'X': (204, 44, 60), 'x': (150, 28, 44), 'y': (238, 100, 110), 'Q': (252, 250, 244), 'q': (200, 196, 210),
    # polerón café (Eduardo)
    'B': (140, 92, 58), 'b': (104, 66, 40), 'u': (176, 124, 82),
    'P': (68, 88, 130), 'p': (46, 58, 92),
}

# ---------- Dallana (dibujada mirando a la derecha; se espeja para que mire a Eduardo) ----------
ELLA = [
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
    "OHHHHHHHHHHHOXXQqQXXO",
    "OHcHHcHHhHHOXXQXXXQXXO",
    "OHHHHHHHHHOXXXXQqQXXXXO",
    ".OHcHHhHHOXXXXXXXXXyXXXO",
    ".OHHHcHHOXXXxXXXXXXyXXXXOOO",
    "..OHHHHOXXXxXXXXXXyyXXXXXSSO",
    "..OcHHOXXXXxXXXXXXXXXXXXOOO",
    "...OOOXXXXXxXXXXXXXXXXO",
    "....OXXXXXxXXXXXXXXXXO",
    "....OXXXXXxXXXXXXXXXXO",
    "....OXXXXXxXXXXXXXXXXO",
    "....OXXXXXxXXXXXXXXXXO",
]
ELLA_BOCA = 14
ELLA_HABLA = "OHHHHhHHHHHHHsSSSSOMMO"

# ---------- Eduardo con polerón café (mira a la derecha) ----------
EL = [
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
    "..ObbbOsSSSSSSSSSSO",
    "..ObbbbOOssSSSSSOO",
    "..ObbbBBBBsssBBO",
    "...ObBBBBBBBBBBBO",
    "...ObBBBBBBWBBBBBO",
    "...ObBBBBBBWBBBBBBO",
    "...ObBBuBBBWBBBBBBO",
    "...ObBBuBBBBBBBBBBBOOO",
    "...ObBBuBBBBBBBBBBBBSSO",
    "...ObBBBBBBBBBBBBBBOOO",
    "...ObBBBBBBBBBBBBBO",
    "...ObBBBBBBBBBBBBBO",
    "...ObBBBBBBBBBBBBBO",
    "...ObBBBBBBBBBBBBBO",
    "...ObbbbbbbbbbbbbbO",
]
EL_BOCA = 12
EL_HABLA = ".....OSSSSSSSSSSSOMO"

def espejo(filas):
    ancho = max(len(f) for f in filas)
    return [f.ljust(ancho, '.')[::-1] for f in filas]

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

# ---------- comida ----------
def hamburguesa(d, x, y):
    d.rounded_rectangle([x, y, x + 9, y + 3], radius=2, fill=(214, 148, 62))       # pan de arriba
    d.point([(x + 2, y + 1), (x + 5, y + 1), (x + 7, y + 2)], fill=(252, 238, 200))
    d.line([x - 1, y + 4, x + 10, y + 4], fill=(110, 190, 70))                        # lechuga
    d.line([x, y + 5, x + 9, y + 5], fill=(250, 200, 40))                              # queso
    d.rectangle([x, y + 6, x + 9, y + 7], fill=(110, 62, 36))                          # carne
    d.rectangle([x, y + 8, x + 9, y + 9], fill=(200, 134, 56))                         # pan de abajo

def papas(d, x, y):
    for k, (dx, alto) in enumerate([(1, 4), (3, 5), (4, 4), (6, 6), (7, 4)]):
        d.line([x + dx, y + 5 - alto, x + dx, y + 5], fill=(252, 214, 70))
        d.point((x + dx, y + 5 - alto), fill=(232, 176, 40))
    d.polygon([(x, y + 4), (x + 8, y + 4), (x + 7, y + 10), (x + 1, y + 10)], fill=(220, 40, 50))
    d.line([x + 2, y + 6, x + 6, y + 6], fill=(255, 220, 90))

def vaso(d, x, y):
    d.polygon([(x, y), (x + 5, y), (x + 4, y + 8), (x + 1, y + 8)], fill=(240, 240, 246))
    d.rectangle([x + 1, y + 2, x + 4, y + 5], fill=(220, 50, 70))
    d.line([x + 3, y - 4, x + 2, y], fill=(250, 120, 140))

# ---------- fondo ----------
def ventana_lluvia(im, x0, y0, x1, y1, f, seed, arco=False):
    d = ImageDraw.Draw(im)
    MARCO = (232, 234, 236)
    d.rectangle([x0 - 3, y0 - 3, x1 + 3, y1 + 3], fill=(98, 104, 110))
    d.rectangle([x0 - 2, y0 - 2, x1 + 2, y1 + 2], fill=MARCO)
    p = im.load()
    for y in range(y0, y1 + 1):
        c = lerp((170, 190, 214), (214, 226, 236), (y - y0) / (y1 - y0))
        for x in range(x0, x1 + 1):
            p[x, y] = c
    # edificios lejanos y árbol
    rnd = random.Random(seed)
    x = x0
    while x < x1:
        w = rnd.randint(7, 12); h = rnd.randint(10, 22)
        d.rectangle([x, y1 - h, min(x + w, x1), y1], fill=(176, 186, 204))
        x += w + 2
    d.ellipse([x0 + 4, y1 - 16, x0 + 18, y1 - 4], fill=(120, 170, 120))
    d.rectangle([x0 + 10, y1 - 5, x0 + 12, y1], fill=(110, 80, 60))
    # nubes
    for (cx, cy, w) in [(x0 + 6, y0 + 4, 18), (x0 + 22, y0 + 8, 20)]:
        d.rounded_rectangle([cx, cy, min(cx + w, x1), cy + 5], radius=3, fill=(232, 236, 242))
    # lluvia suave (loop exacto: 3 px x 16 = 48)
    for i in range(18):
        gx = x0 + rnd.randint(0, x1 - x0)
        gy0 = rnd.randint(0, 47)
        gy = y0 + (gy0 + f * 3) % 48
        if gy + 3 <= y1:
            d.line([gx, gy, gx, gy + 3], fill=(240, 246, 252))
    # gotas en el vidrio
    for i in range(4):
        d.point((x0 + rnd.randint(2, x1 - x0 - 2), y0 + rnd.randint(2, y1 - y0 - 2)), fill=(236, 244, 255))
    # marco en cruz y alféizar
    d.line([(x0 + x1) // 2, y0, (x0 + x1) // 2, y1], fill=MARCO, width=2)
    d.line([x0, y0 + (y1 - y0) // 3, x1, y0 + (y1 - y0) // 3], fill=MARCO, width=1)
    d.rectangle([x0 - 5, y1 + 3, x1 + 5, y1 + 5], fill=(132, 138, 144))
    if arco:
        # recorta las esquinas de arriba para que la ventana sea en arco
        pa = im.load()
        r = (x1 - x0) // 2 + 3
        cx, cy = (x0 + x1) // 2, y0 - 3 + r
        for yy in range(y0 - 3, cy):
            for xx in range(x0 - 3, x1 + 4):
                dist = ((xx - cx) ** 2 + (yy - cy) ** 2) ** .5
                if dist > r:
                    pa[xx, yy] = PARED
                elif dist > r - 1:
                    pa[xx, yy] = (98, 104, 110)
                elif dist > r - 2:
                    pa[xx, yy] = MARCO

PARED = (116, 124, 128)

def ampolleta(im, x, y_fin, f, fase):
    d = ImageDraw.Draw(im)
    d.line([x, 0, x, y_fin], fill=(40, 40, 44))
    brillo = 1 if (f + fase) % 6 else 0
    halo = (196, 170, 120) if brillo else (176, 156, 116)
    d.ellipse([x - 7, y_fin - 1, x + 7, y_fin + 13], fill=lerp(PARED, halo, .35))
    d.ellipse([x - 4, y_fin + 2, x + 4, y_fin + 10], fill=lerp(PARED, halo, .7))
    d.rectangle([x - 1, y_fin, x + 1, y_fin + 2], fill=(150, 120, 60))
    d.ellipse([x - 2, y_fin + 3, x + 2, y_fin + 9], fill=(255, 206, 110) if brillo else (240, 180, 90))
    d.point((x, y_fin + 5), fill=(255, 250, 220))

def espejo_dorado(im, x0, y0, x1, y1):
    d = ImageDraw.Draw(im)
    d.rectangle([x0, y0, x1, y1], fill=(200, 160, 80))
    d.rectangle([x0 + 1, y0 + 1, x1 - 1, y1 - 1], fill=(224, 188, 104))
    d.rectangle([x0 + 3, y0 + 3, x1 - 3, y1 - 3], fill=(150, 160, 166))
    d.rectangle([x0 + 3, y1 - 12, x1 - 3, y1 - 3], fill=(120, 96, 76))
    d.line([x0 + 5, y0 + 5, x0 + 10, y0 + 12], fill=(196, 204, 210))
    d.rectangle([x0 + 8, y0 + 16, x0 + 13, y0 + 22], fill=(220, 190, 90))

def planta(im, x, y):
    d = ImageDraw.Draw(im)
    for (dx, dy, w) in [(-8, -20, 5), (-3, -26, 5), (3, -24, 5), (8, -18, 4), (-12, -12, 4), (11, -10, 4), (0, -16, 4)]:
        d.ellipse([x + dx - w // 2, y + dy, x + dx + w // 2, y + dy + 12], fill=(64, 140, 70))
        d.line([x + dx, y + dy + 3, x + dx, y + dy + 10], fill=(110, 186, 100))
        d.line([x, y, x + dx, y + dy + 10], fill=(70, 120, 60))
    d.polygon([(x - 10, y), (x + 10, y), (x + 8, y + 18), (x - 8, y + 18)], fill=(232, 222, 200))
    d.line([x - 10, y, x + 10, y], fill=(200, 188, 164))
    d.line([x - 9, y + 2, x + 9, y + 2], fill=(60, 44, 36))

def fondo(f):
    im = Image.new('RGB', (W, H), PARED)
    d = ImageDraw.Draw(im)
    p = im.load()
    # pared gris con un poco de textura
    for y in range(112):
        for x in range(0, W, 7):
            if (x * 3 + y * 5) % 11 == 0:
                p[x, y] = lerp(PARED, (0, 0, 0), .05)
    # techo: moldura y vigas de madera en el centro
    d.rectangle([0, 0, W, 7], fill=(146, 152, 154))
    d.line([0, 8, W, 8], fill=(200, 204, 206))
    d.polygon([(96, 0), (176, 0), (170, 10), (102, 10)], fill=(236, 230, 214))
    for k in range(5):
        x = 100 + k * 17
        d.line([x, 0, x + 6, 10], fill=(150, 96, 56), width=2)
    d.rectangle([94, 10, 178, 12], fill=(120, 126, 130))
    # ventana en arco y ventanal, con lluvia de día
    ventana_lluvia(im, 12, 22, 46, 72, f, 1, arco=True)
    ventana_lluvia(im, 60, 30, 96, 72, f, 2)
    # espejo dorado y cuadro
    espejo_dorado(im, 184, 32, 206, 66)
    d.rectangle([166, 36, 176, 52], fill=(40, 40, 44)); d.rectangle([168, 38, 174, 50], fill=(230, 226, 214))
    d.line([169, 46, 173, 41], fill=(80, 80, 90))
    # muro de tablas de madera a la derecha
    d.rectangle([222, 0, W, 112], fill=(206, 196, 178))
    for x in range(222, W, 6):
        d.line([x, 0, x, 112], fill=(180, 168, 148))
        for y in range((x * 13) % 30, 112, 30):
            d.line([x + 1, y, x + 4, y], fill=(190, 178, 158))
    d.line([221, 0, 221, 112], fill=(92, 98, 102))
    # ampolletas colgantes sobre la mesa
    ampolleta(im, 118, 22, f, 0)
    ampolleta(im, 140, 18, f, 3)
    # piso de madera oscura
    d.rectangle([0, 112, W, H], fill=(112, 70, 52))
    for y in range(114, H, 5):
        d.line([0, y, W, y], fill=(92, 56, 42))
        for x in range((y * 11) % 34, W, 34):
            d.line([x, y, x, y + 4], fill=(92, 56, 42))
    d.line([0, 112, W, 112], fill=(70, 74, 78))
    # planta en macetero
    planta(im, 234, 100)
    return im

def globo(im, x0, y0, f, cola_derecha, contenido):
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([x0, y0, x0 + 22, y0 + 13], radius=5, fill=(255, 252, 248), outline=PAL['O'])
    cx = x0 + (16 if cola_derecha else 6)
    d.polygon([(cx - 2, y0 + 13), (cx + 2, y0 + 13), (cx + (3 if cola_derecha else -3), y0 + 18)], fill=(255, 252, 248))
    d.line([cx - 2, y0 + 13, cx + (3 if cola_derecha else -3), y0 + 18], fill=PAL['O'])
    d.line([cx + (3 if cola_derecha else -3), y0 + 18, cx + 2, y0 + 13], fill=PAL['O'])
    if contenido == 'corazon':
        corazon(im, x0 + 8, y0 + 4 - (1 if f % 2 else 0), (224, 48, 63))
    elif contenido == 'puntos':
        for k in range(3):
            if k <= f % 4:
                d.rectangle([x0 + 5 + k * 5, y0 + 6, x0 + 6 + k * 5, y0 + 7], fill=PAL['O'])
    else:  # hamburguesita
        hamburguesa(d, x0 + 5, y0 + 1)

NEGRO = (38, 38, 42)
def silla_respaldo(d, x0, x1):
    """Respaldo negro con la X, como las sillas de la foto."""
    d.rectangle([x0, 66, x0 + 1, 112], fill=NEGRO)
    d.rectangle([x1 - 1, 66, x1, 112], fill=NEGRO)
    d.rectangle([x0, 66, x1, 68], fill=NEGRO)
    d.line([x0 + 1, 69, x1 - 1, 92], fill=NEGRO)
    d.line([x1 - 1, 69, x0 + 1, 92], fill=NEGRO)

def piernas_sentado(d, x_cadera, x_rodilla, mira_derecha, tela=None, sombra=None):
    """Muslos y piernas de alguien sentado (jeans y zapatillas)."""
    tela = tela or PAL['P']; sombra = sombra or PAL['p']
    a, b = sorted((x_cadera, x_rodilla))
    d.rectangle([a, 92, b, 97], fill=tela)
    d.line([a, 97, b, 97], fill=sombra)
    xr = x_rodilla - 4 if mira_derecha else x_rodilla
    d.rectangle([xr, 97, xr + 4, 110], fill=tela)
    d.rectangle([xr + (0 if mira_derecha else -2), 110, xr + 6 + (0 if mira_derecha else -2), 112], fill=(248, 246, 242))
    # asiento negro
    d.rectangle([a - 2, 98, b - 4 if mira_derecha else b + 2, 99], fill=NEGRO)

frames = []
for f in range(F):
    im = fondo(f)
    d = ImageDraw.Draw(im)
    habla_el = f < 8
    # sillas negras con X detrás de cada uno, y sus piernas sentadas
    silla_respaldo(d, 78, 88)
    silla_respaldo(d, 172, 182)
    piernas_sentado(d, 86, 108, True, (30, 30, 34), (52, 52, 60))
    piernas_sentado(d, 174, 150, False)
    # Eduardo
    el = list(EL)
    if habla_el and f % 2 == 0:
        el[EL_BOCA] = EL_HABLA
    rebote_el = 1 if habla_el and f % 4 < 2 else 0
    pegar(im, el, 82, 63 - rebote_el)
    # Dallana (espejada)
    ella = list(ELLA)
    if not habla_el and f % 2 == 0:
        ella[ELLA_BOCA] = ELLA_HABLA
    rebote_ella = 1 if not habla_el and f % 4 < 2 else 0
    filas = espejo(ella)
    pegar(im, filas, 148, 61 - rebote_ella)
    # mesa (tapa a los cuerpos desde la cintura)
    d.rectangle([92, 91, 166, 95], fill=(196, 140, 84))
    d.line([92, 91, 166, 91], fill=(226, 176, 116))
    d.line([92, 95, 166, 95], fill=(150, 98, 58))
    d.rectangle([126, 96, 131, 110], fill=NEGRO)
    d.rectangle([116, 110, 141, 112], fill=NEGRO)
    # servilletero y cartita amarilla
    d.polygon([(118, 90), (124, 90), (121, 85)], fill=(246, 244, 238))
    d.rectangle([133, 84, 137, 90], fill=(240, 200, 60)); d.line([134, 86, 136, 86], fill=(120, 90, 30))
    # platos, hamburguesas, papas y bebidas
    for px0 in (102, 138):
        d.ellipse([px0, 89, px0 + 16, 93], fill=(244, 244, 248))
        hamburguesa(d, px0 + 3, 81)
    papas(d, 122, 82)
    vaso(d, 96, 83)
    vaso(d, 157, 83)
    # globos de diálogo: conversan por turnos
    if habla_el:
        globo(im, 98, 37 - rebote_el, f, False, 'puntos' if f < 4 else 'corazon')
    else:
        globo(im, 136, 35 - rebote_ella, f, True, 'corazon' if f >= 12 else 'puntos')
    # corazoncitos flotando sobre la mesa
    t = (f % 16) / 16
    if t < .8:
        corazon(im, 125 + int(2 * math.sin(t * 6.28)), int(72 - t * 30), (255, 130, 160))
    frames.append(im.resize((W * K, H * K), Image.NEAREST))

frames[0].save(OUT + '.gif', save_all=True, append_images=frames[1:], duration=140, loop=0, optimize=True)
frames[0].save(OUT + '_f0.png')
print('ok')
