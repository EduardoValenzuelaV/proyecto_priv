"""Escena pixel: Eduardo y Dallana durmiendo abrazados en la cama, de noche.
Uso: python propuesta/escena_dormir.py assets/pixel/dormir   (genera dormir.gif y dormir_f0.png)
"""
import sys, math, random
from PIL import Image, ImageDraw

OUT = sys.argv[1] if len(sys.argv) > 1 else 'dormir'
W, H, K, F = 256, 144, 2, 24

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

PAL = {
    'O': (34, 22, 26),
    'H': (44, 30, 30), 'h': (78, 52, 46), 'c': (130, 90, 72),
    'S': (236, 186, 146), 's': (204, 146, 110), 'K': (244, 138, 140), 'M': (206, 88, 98),
}

# cabezas de frente, con los ojos cerrados
EL_CARA = [
    "....OOOOOOOO",
    "..OOHHhHHHHHOO",
    ".OHHHHHhHHHHHHO",
    ".OHHhHHHHHHHhHO",
    "OHHHHHHHHHHHHHHO",
    "OHHSHHHSHHHHSHHO",
    "OHSSSSSSSSSSSSHO",
    "OsSSSSSSSSSSSSsO",
    "OsSOOSSSSSSOOSsO",
    "OSSSSSSSSSSSSSSO",
    ".OSKSSSSSSSSKSO",
    ".OSSSSSOOSSSSSO",
    "..OSSSSSSSSSSO",
    "...OOSSSSSSOO",
]
ELLA_CARA = [
    "...OO.OOOO.OO",
    ".OOccOHHHHOccOO",
    "OHHHHHHhHHHHHHHO",
    "OHcHHHHHHHHHHcHO",
    "OHHHHHHHHHHHHHHO",
    "OHHSHHSHHSHHSHHO",
    "OHSSSSSSSSSSSSHO",
    "OHSSSSSSSSSSSSHO",
    "OHSOOSSSSSSOOSHO",
    "OcSSSSSSSSSSSScO",
    "OHSKSSSSSSSSKSHO",
    "OHHSSSSSMMSSSSHO",
    "OcHOSSSSSSSSSOHcO",
    "OHHHOOSSSSOOHHHO",
    "OcHHHHHHHHHHHHcO",
    ".OHHcHHHHHHcHHO",
    "..OOOOOOOOOOOO",
]

def pegar(im, filas, x0, y0):
    p = im.load()
    for y, fila in enumerate(filas):
        for x, ch in enumerate(fila):
            if ch != '.' and 0 <= x0 + x < W and 0 <= y0 + y < H:
                p[x0 + x, y0 + y] = PAL[ch]

CORAZON = ["0110110", "1111111", "1111111", "0111110", "0011100", "0001000"]
Z = ["111", "001", "010", "100", "111"]
def figura(im, forma, x, y, col):
    p = im.load()
    for r, fila in enumerate(forma):
        for c, v in enumerate(fila):
            if v == '1' and 0 <= x + c < W and 0 <= y + r < H:
                p[x + c, y + r] = col

PARED_A, PARED_B = (226, 206, 176), (206, 184, 152)

def fondo(f):
    im = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(im)
    p = im.load()
    # pared beige con rayas suaves (de noche, un poco en penumbra)
    for y in range(128):
        d.line([0, y, W, y], fill=lerp(PARED_A, PARED_B, y / 128))
    for x in range(0, W, 10):
        d.line([x, 0, x, 127], fill=lerp(PARED_A, PARED_B, .7))
    d.rectangle([0, 120, W, 127], fill=(236, 226, 206))
    # ventana a la izquierda con luna y estrellas, y cortinas
    d.rectangle([14, 16, 58, 70], fill=(150, 112, 80))
    d.rectangle([17, 19, 55, 67], fill=(22, 28, 66))
    d.ellipse([38, 24, 50, 36], fill=(250, 244, 206))
    d.ellipse([42, 22, 54, 34], fill=(22, 28, 66))
    random.seed(4)
    for k in range(9):
        sx, sy = random.randint(19, 53), random.randint(22, 64)
        if (f + k * 3) % 8 < 2:
            d.point([(sx, sy), (sx - 1, sy), (sx + 1, sy), (sx, sy - 1), (sx, sy + 1)], fill=(255, 250, 220))
        else:
            d.point((sx, sy), fill=(220, 220, 240))
    d.line([36, 19, 36, 67], fill=(150, 112, 80), width=2)
    for (x0, x1) in ((6, 16), (56, 66)):
        d.rectangle([x0, 12, x1, 82], fill=(176, 140, 120))
        for xx in range(x0 + 2, x1, 3):
            d.line([xx, 14, xx, 82], fill=(156, 120, 100))
    d.rectangle([2, 10, 70, 13], fill=(120, 90, 66))
    # luz de luna entrando desde la ventana hacia la cama
    for y in range(70, 128):
        for x in range(40 + (y - 70) // 2, 92 + (y - 70) // 2):
            if 0 <= x < W and (x + y) % 2 == 0:
                p[x, y] = lerp(p[x, y], (200, 210, 240), .22)
    # cuadro con corazón sobre la cama
    d.rectangle([116, 14, 138, 32], fill=(196, 160, 90))
    d.rectangle([119, 17, 135, 29], fill=(250, 242, 230))
    figura(im, CORAZON, 124, 20, (220, 60, 80))
    # piso
    d.rectangle([0, 128, W, H], fill=(150, 108, 76))
    for y in range(131, H, 5):
        d.line([0, y, W, y], fill=(128, 90, 62))
    # velador a la derecha con lámpara encendida y los lentes de Dallana
    vx = 204
    brillo = .30 if f % 12 else .24
    for r in range(24, 0, -2):
        d.ellipse([vx + 15 - r, 76 - r, vx + 15 + r, 76 + r], fill=lerp(lerp(PARED_A, PARED_B, .55), (255, 214, 140), brillo * (1 - r / 26)))
    d.rectangle([vx, 92, vx + 30, 128], fill=(170, 124, 86))
    d.rectangle([vx, 92, vx + 30, 95], fill=(196, 146, 102))
    d.rectangle([vx + 4, 104, vx + 26, 106], fill=(140, 100, 68))
    d.ellipse([vx + 13, 104, vx + 17, 107], fill=(236, 210, 130))
    d.rectangle([vx + 12, 80, vx + 18, 91], fill=(236, 226, 206))
    d.polygon([(vx + 6, 80), (vx + 24, 80), (vx + 20, 68), (vx + 10, 68)], fill=(252, 220, 160))
    d.line([vx + 6, 80, vx + 24, 80], fill=(226, 184, 116))
    # lentes rojos sobre el velador
    d.rectangle([vx + 20, 89, vx + 24, 91], outline=(200, 32, 50))
    d.rectangle([vx + 13, 89, vx + 17, 91], outline=(200, 32, 50))
    d.line([vx + 18, 90, vx + 19, 90], fill=(200, 32, 50))
    return im

# ropa de cama verde azulada
TEAL = (96, 168, 164)
TEAL_OSC = (74, 140, 138)
TEAL_CLARO = (150, 206, 198)

def cama(im, f):
    d = ImageDraw.Draw(im)
    # respaldo de madera clara
    d.rounded_rectangle([78, 38, 176, 80], radius=10, fill=(176, 130, 90))
    d.rounded_rectangle([82, 42, 172, 80], radius=8, fill=(200, 154, 108))
    for x in range(90, 170, 10):
        d.line([x, 46, x, 78], fill=(182, 136, 94))
    # almohadas verde agua clarito
    d.rounded_rectangle([86, 58, 125, 76], radius=6, fill=(214, 236, 232))
    d.rounded_rectangle([128, 58, 166, 76], radius=6, fill=(214, 236, 232))
    d.line([90, 74, 121, 74], fill=(184, 214, 208)); d.line([132, 74, 162, 74], fill=(184, 214, 208))

def frazada(im, f, respira):
    d = ImageDraw.Draw(im)
    top = 72 - respira
    d.rectangle([76, 120, 178, 130], fill=(176, 130, 90))
    d.rectangle([78, 128, 82, 136], fill=(150, 108, 72)); d.rectangle([172, 128, 176, 136], fill=(150, 108, 72))
    # frazada verde azulada con corazoncitos y doblez claro
    d.rounded_rectangle([74, top, 180, 122], radius=6, fill=TEAL)
    # los dos cuerpos juntitos bajo la frazada (él de lado abrazándola)
    d.ellipse([86, top + 10, 128, top + 38], fill=TEAL_OSC)
    d.ellipse([108, top + 12, 152, top + 40], fill=TEAL_OSC)
    d.ellipse([86, top + 7, 128, top + 35], fill=TEAL)
    d.ellipse([108, top + 9, 152, top + 37], fill=TEAL)
    for yy in range(top + 14, 120, 10):
        for xx in range(80 + (yy // 10) % 2 * 8, 176, 16):
            figura(im, ["101", "111", "010"], xx, yy, TEAL_CLARO)
    d.rounded_rectangle([74, top, 180, top + 6], radius=3, fill=(232, 244, 240))
    d.line([74, top + 6, 180, top + 6], fill=(190, 216, 210))
    # brazo de Eduardo que la rodea: sale de su hombro, pasa por encima de ella y su mano queda en su hombro
    d.rounded_rectangle([106, top + 2, 134, top + 7], radius=2, fill=(170, 186, 214))
    d.line([106, top + 7, 134, top + 7], fill=(134, 150, 186))
    d.line([132, top + 2, 134, top + 1], fill=(170, 186, 214))
    d.rounded_rectangle([132, top - 1, 138, top + 5], radius=2, fill=(236, 186, 146))
    d.point((137, top + 2), fill=(204, 146, 110))
    # mano de Dallana sobre el pecho de él
    d.rounded_rectangle([98, top + 8, 116, top + 12], radius=2, fill=(240, 170, 190))
    d.rounded_rectangle([95, top + 7, 100, top + 12], radius=2, fill=(236, 186, 146))

frames = []
for f in range(F):
    im = fondo(f)
    cama(im, f)
    respira = 1 if (f // 6) % 2 else 0
    # cabezas sobre las almohadas: ella apoyada en el hombro de él
    pegar(im, EL_CARA, 100, 55 + respira)
    pegar(im, ELLA_CARA, 112, 60 + respira)
    frazada(im, f, respira)
    # Zzz que suben de cada uno
    for k, (x0, fase) in enumerate(((104, 0), (128, 12))):
        t = ((f + fase) % 24) / 24
        for n in range(2):
            tt = t - n * .25
            if 0 <= tt < .7:
                col = lerp((120, 130, 190), PARED_A, tt / .9)
                figura(im, Z, x0 + int(tt * 10) + n * 4, int(50 - tt * 34), col)
    # corazoncito que sube entre los dos
    t = (f % 24) / 24
    if t < .8:
        figura(im, CORAZON, 118 + int(2 * math.sin(t * 6.28)), int(48 - t * 30), (255, 130, 160))
    frames.append(im.resize((W * K, H * K), Image.NEAREST))

frames[0].save(OUT + '.gif', save_all=True, append_images=frames[1:], duration=150, loop=0, optimize=True)
frames[0].save(OUT + '_f0.png')
print('ok')
