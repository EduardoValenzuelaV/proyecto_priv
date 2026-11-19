"""Personaje pixel: cangrejo rojo feliz bajo el mar (mismo estilo que Eduardo y Dallana).
Uso: python propuesta/cangrejo.py assets/pixel/cangrejo   (genera cangrejo.gif y cangrejo_f0.png)
"""
import sys, math, random
from PIL import Image, ImageDraw

OUT = sys.argv[1] if len(sys.argv) > 1 else 'cangrejo'
W, H, K, F = 128, 96, 4, 12

OUTL = (64, 14, 22)
R = (226, 52, 50)
r = (176, 30, 38)
L = (252, 120, 104)
BL = (255, 255, 255)
NE = (24, 16, 20)
BOCA = (96, 18, 32)
LENGUA = (242, 120, 150)

def sprite(garra, parpadeo):
    """garra: 0 arriba, 1 abajo. Se dibuja con formas y luego se le pone contorno."""
    S = Image.new('RGBA', (44, 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(S)
    cx = 22
    # patas (3 por lado)
    for i, dy in enumerate((24, 27, 30)):
        d.line([cx - 9, dy, cx - 15, dy + 2, cx - 18, dy + 5], fill=r, width=2)
        d.line([cx + 9, dy, cx + 15, dy + 2, cx + 18, dy + 5], fill=r, width=2)
    # brazos hacia las pinzas
    gy = 3 if garra == 0 else 7
    d.line([cx - 9, 22, cx - 13, 16, cx - 15, gy + 8], fill=R, width=3)
    d.line([cx + 9, 22, cx + 13, 16, cx + 15, gy + 8], fill=R, width=3)
    # pinzas: elipse con una muesca en V
    for sx in (-1, 1):
        x0 = cx + sx * 16
        d.ellipse([x0 - 6, gy - 2, x0 + 6, gy + 9], fill=R)
        d.ellipse([x0 - 4, gy + 3, x0 + 2, gy + 8], fill=L)
        d.polygon([(x0 + sx * 1, gy + 3), (x0 + sx * 7, gy - 3), (x0 + sx * 7, gy + 4)], fill=(0, 0, 0, 0))
    # cuerpo (caparazón)
    d.ellipse([cx - 11, 16, cx + 11, 34], fill=R)
    d.ellipse([cx - 9, 27, cx + 9, 35], fill=r)
    d.ellipse([cx - 7, 18, cx - 2, 22], fill=L)
    # cara
    d.ellipse([cx - 8, 9, cx + 8, 24], fill=R)
    d.ellipse([cx - 6, 10, cx - 1, 13], fill=L)
    # ojos sobre tallos
    for sx in (-1, 1):
        ex = cx + sx * 4
        d.line([ex, 8, ex, 11], fill=R, width=2)
        if parpadeo:
            d.line([ex - 3, 5, ex + 3, 5], fill=NE)
        else:
            d.ellipse([ex - 3, 1, ex + 3, 8], fill=BL)
            px0 = ex - 1 if sx > 0 else ex
            d.rectangle([px0, 4, px0 + 1, 6], fill=NE)
            d.point((px0, 4), fill=BL)
    # boca abierta con dientes y lengua
    d.ellipse([cx - 7, 10, cx + 7, 24], fill=BOCA)
    d.rectangle([cx - 8, 10, cx + 8, 15], fill=R)
    d.rectangle([cx - 6, 16, cx + 6, 17], fill=BL)
    d.ellipse([cx - 4, 19, cx + 4, 24], fill=LENGUA)
    d.line([cx - 3, 23, cx + 3, 23], fill=BL)
    # cejas felices
    d.line([cx - 7, 0, cx - 3, 0], fill=OUTL)
    d.line([cx + 3, 0, cx + 7, 0], fill=OUTL)
    # contorno de 1 px alrededor de todo lo opaco
    px = S.load()
    con = S.copy(); pc = con.load()
    for y in range(S.height):
        for x in range(S.width):
            if px[x, y][3] == 0:
                for (a, b) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    xx, yy = x + a, y + b
                    if 0 <= xx < S.width and 0 <= yy < S.height and px[xx, yy][3] > 0 and px[xx, yy][:3] != OUTL:
                        pc[x, y] = OUTL + (255,)
                        break
    return con

def fondo(f):
    im = Image.new('RGB', (W, H))
    p = im.load()
    for y in range(H):
        for x in range(W):
            t = y / H
            c = (int(60 + 40 * t), int(26 + 20 * t), int(110 + 30 * t))
            # rayos de luz diagonales
            if ((x + y // 2 + f) // 10) % 5 == 0 and y < 70:
                c = tuple(min(255, v + 18) for v in c)
            p[x, y] = c
    d = ImageDraw.Draw(im)
    # arena y algas
    d.rectangle([0, 82, W, H], fill=(196, 160, 120))
    for x in range(0, W, 3):
        d.point((x, 82 + (x * 7) % 3), fill=(220, 186, 144))
    for (ax, alto) in [(10, 22), (16, 14), (110, 20), (117, 12)]:
        for yy in range(alto):
            sx = ax + int(2 * math.sin((yy + f) / 3))
            d.point((sx, 82 - yy), fill=(70, 170, 110))
            d.point((sx + 1, 82 - yy), fill=(50, 130, 90))
    # burbujas que suben (loop exacto)
    random.seed(5)
    for i in range(14):
        bx = random.randint(4, W - 6)
        by0 = random.randint(0, 96)
        tam = random.choice([1, 2, 2, 3])
        by = (by0 - f * 8) % 96
        bx += int(1.5 * math.sin((by + i) / 6))
        d.ellipse([bx, by, bx + tam * 2, by + tam * 2], outline=(200, 190, 255))
        d.point((bx + 1, by + 1), fill=(255, 255, 255))
    return im

frames = []
for f in range(F):
    im = fondo(f)
    garra = 0 if (f // 3) % 2 == 0 else 1
    rebote = [0, 1, 2, 1][f % 4]
    spr = sprite(garra, parpadeo=(f == 9))
    # sombra en la arena
    ImageDraw.Draw(im).ellipse([44, 82, 84, 86], fill=(166, 132, 100))
    im.paste(spr, (W // 2 - 22, 46 - rebote), spr)
    frames.append(im.resize((W * K, H * K), Image.NEAREST))

frames[0].save(OUT + '.gif', save_all=True, append_images=frames[1:], duration=110, loop=0, optimize=True)
frames[0].save(OUT + '_f0.png')
print('ok')

# ---------- Alejandro: hoja de sprites sin fondo para el ayudante de la página ----------
# Genera <OUT>_hoja.png: 12 cuadros de 44x54 en fila (salta, mueve las pinzas y parpadea).
SALTO = [0, 0, 1, 3, 6, 8, 9, 8, 6, 3, 1, 0]
hoja = Image.new('RGBA', (44 * len(SALTO), 54), (0, 0, 0, 0))
for i, alto in enumerate(SALTO):
    spr = sprite(0 if alto >= 3 or i % 2 == 0 else 1, parpadeo=(i == 1))
    hoja.paste(spr, (i * 44, 54 - 40 - alto), spr)
    # sombrita que se achica cuando está en el aire
    ds = ImageDraw.Draw(hoja)
    ancho = 14 - alto
    ds.ellipse([i * 44 + 22 - ancho, 51, i * 44 + 22 + ancho, 53], fill=(0, 0, 0, 60))
hoja.save(OUT + '_hoja.png')
print('hoja ok')
