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

T = 10  # margen arriba para que las pinzas puedan subir sobre la cabeza (aplaudir)

def contorno(S):
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

def pose(gl=(16, 3), gr=(16, 3), ojos='abiertos', boca='feliz', patas=0):
    """Cangrejo de 44x50 (con T px de margen arriba).
    gl/gr: (distancia al centro, altura) de cada pinza. ojos: abiertos/parpadeo/cerrados.
    boca: feliz/dormido/('bostezo', n). patas: 0 quietas, 1 o 2 = paso al caminar."""
    S = Image.new('RGBA', (44, 40 + T), (0, 0, 0, 0))
    d = ImageDraw.Draw(S)
    cx = 22
    Y = lambda v: v + T
    # patas (3 por lado); al caminar se alternan arriba y abajo
    for i, dy in enumerate((24, 27, 30)):
        if patas:
            alt = (i + patas) % 2
            pi, pd = dy + (3 if alt else 5), dy + (5 if alt else 3)
        else:
            pi = pd = dy + 5
        d.line([cx - 9, Y(dy), cx - 15, Y(dy + 2), cx - 18, Y(pi)], fill=r, width=2)
        d.line([cx + 9, Y(dy), cx + 15, Y(dy + 2), cx + 18, Y(pd)], fill=r, width=2)
    # brazos y pinzas
    for sx, (dx, gy) in ((-1, gl), (1, gr)):
        d.line([cx + sx * 9, Y(22), cx + sx * 13, Y(16), cx + sx * dx, Y(gy + 8)], fill=R, width=3)
        x0 = cx + sx * dx
        d.ellipse([x0 - 6, Y(gy - 2), x0 + 6, Y(gy + 9)], fill=R)
        d.ellipse([x0 - 4, Y(gy + 3), x0 + 2, Y(gy + 8)], fill=L)
        d.polygon([(x0 + sx * 1, Y(gy + 3)), (x0 + sx * 7, Y(gy - 3)), (x0 + sx * 7, Y(gy + 4))], fill=(0, 0, 0, 0))
    # cuerpo (caparazón)
    d.ellipse([cx - 11, Y(16), cx + 11, Y(34)], fill=R)
    d.ellipse([cx - 9, Y(27), cx + 9, Y(35)], fill=r)
    d.ellipse([cx - 7, Y(18), cx - 2, Y(22)], fill=L)
    # cara
    d.ellipse([cx - 8, Y(9), cx + 8, Y(24)], fill=R)
    d.ellipse([cx - 6, Y(10), cx - 1, Y(13)], fill=L)
    # ojos sobre tallos
    for sx in (-1, 1):
        ex = cx + sx * 4
        d.line([ex, Y(8), ex, Y(11)], fill=R, width=2)
        if ojos == 'parpadeo':
            d.line([ex - 3, Y(5), ex + 3, Y(5)], fill=NE)
        elif ojos == 'cerrados':
            # ojito cerrado en curva, como durmiendo
            d.ellipse([ex - 3, Y(2), ex + 3, Y(8)], fill=L)
            d.line([ex - 2, Y(6), ex + 2, Y(6)], fill=NE)
            d.point([(ex - 3, Y(5)), (ex + 3, Y(5))], fill=NE)
        else:
            d.ellipse([ex - 3, Y(1), ex + 3, Y(8)], fill=BL)
            px0 = ex - 1 if sx > 0 else ex
            d.rectangle([px0, Y(4), px0 + 1, Y(6)], fill=NE)
            d.point((px0, Y(4)), fill=BL)
    # boca
    if boca == 'feliz':
        d.ellipse([cx - 7, Y(10), cx + 7, Y(24)], fill=BOCA)
        d.rectangle([cx - 8, Y(10), cx + 8, Y(15)], fill=R)
        d.rectangle([cx - 6, Y(16), cx + 6, Y(17)], fill=BL)
        d.ellipse([cx - 4, Y(19), cx + 4, Y(24)], fill=LENGUA)
        d.line([cx - 3, Y(23), cx + 3, Y(23)], fill=BL)
    elif boca == 'dormido':
        d.line([cx - 3, Y(18), cx - 1, Y(19), cx + 1, Y(19), cx + 3, Y(18)], fill=BOCA)
    else:
        n = boca[1]  # 0..6: qué tan abierta está la boca del bostezo
        if n == 0:
            d.line([cx - 3, Y(18), cx + 3, Y(18)], fill=BOCA)
        else:
            d.ellipse([cx - 2 - n // 2, Y(16), cx + 2 + n // 2, Y(18 + n)], fill=BOCA)
            if n >= 3:
                d.ellipse([cx - 2, Y(15 + n), cx + 2, Y(18 + n)], fill=LENGUA)
    # cejas
    if ojos == 'cerrados':
        d.line([cx - 7, Y(0), cx - 3, Y(1)], fill=OUTL)
        d.line([cx + 3, Y(1), cx + 7, Y(0)], fill=OUTL)
    else:
        d.line([cx - 7, Y(0), cx - 3, Y(0)], fill=OUTL)
        d.line([cx + 3, Y(0), cx + 7, Y(0)], fill=OUTL)
    return contorno(S)

def sprite(garra, parpadeo):
    gy = 3 if garra == 0 else 7
    return pose((16, gy), (16, gy), 'parpadeo' if parpadeo else 'abiertos').crop((0, T, 44, 40 + T))

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
# Genera <OUT>_hoja.png: 6 filas de 12 cuadros de 44x54.
# Filas: 0 salta, 1 aplaude, 2 baila, 3 duerme (Zzz), 4 bosteza, 5 camina de lado.
FW, FH, N, FILAS = 44, 54, 12, 6
hoja = Image.new('RGBA', (FW * N, FH * FILAS), (0, 0, 0, 0))
ds = ImageDraw.Draw(hoja)
Z = ["111", "001", "010", "100", "111"]
ESTRELLA = ["010", "111", "010"]

def poner(spr, i, fila, alto=0, dx=0, sombra=14):
    x0, y0 = i * FW + dx, fila * FH + FH - spr.height - alto
    if y0 < fila * FH:  # recorta el margen vacío de arriba si se sale del cuadro
        spr = spr.crop((0, fila * FH - y0, spr.width, spr.height)); y0 = fila * FH
    ancho = max(4, sombra - alto)
    ds.ellipse([i * FW + 22 - ancho, fila * FH + 51, i * FW + 22 + ancho, fila * FH + 53], fill=(0, 0, 0, 60))
    hoja.alpha_composite(spr, (x0, y0))

def figura_hoja(forma, x, y, col):
    for rr, fila in enumerate(forma):
        for c, v in enumerate(fila):
            if v == '1':
                hoja.putpixel((x + c, y + rr), col + (255,))

# 0. salta (igual que antes)
SALTO = [0, 0, 1, 3, 6, 8, 9, 8, 6, 3, 1, 0]
for i, alto in enumerate(SALTO):
    gy = 3 if (alto >= 3 or i % 2 == 0) else 7
    poner(pose((16, gy), (16, gy), 'parpadeo' if i == 1 else 'abiertos'), i, 0, alto)

# 1. aplaude: pinzas sobre la cabeza que se juntan, con estrellitas
for i in range(N):
    junta = i % 4 in (1, 2)
    pz = (7, -8) if junta else (14, -5)
    poner(pose(pz, pz), i, 1, [0, 1, 1, 0][i % 4])
    if i % 4 == 2:
        figura_hoja(ESTRELLA, i * FW + 21, 1 * FH + 0, (255, 214, 80))
        figura_hoja(ESTRELLA, i * FW + 5, 1 * FH + 6, (255, 240, 160))
        figura_hoja(ESTRELLA, i * FW + 36, 1 * FH + 4, (255, 240, 160))

# 2. baila: se mece de lado a lado y sube una pinza y luego la otra
MECE = [0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 0, -1]
for i in range(N):
    arriba, abajo = (14, -2), (15, 8)
    izq = (i // 3) % 2 == 0
    poner(pose(arriba if izq else abajo, abajo if izq else arriba), i, 2, [0, 2, 3, 2][i % 4], MECE[i])

# 3. duerme: sentadito, ojos cerrados, respira y salen Zzz
for i in range(N):
    respira = 1 if (i // 3) % 2 else 0
    poner(pose((15, 9), (15, 9), 'cerrados', 'dormido'), i, 3, -2 + respira, sombra=15)
    for n in range(2):
        t = ((i + n * 6) % N) / N
        figura_hoja(Z, i * FW + 30 + int(t * 8), 3 * FH + 11 - int(t * 11),
                    (110, 120, 200) if t < .6 else (170, 180, 230))

# 4. bosteza: abre la boca grande, estira las pinzas y vuelve a sonreír
BOCA_B = [0, 1, 2, 4, 5, 6, 6, 6, 5, 3, 1, 0]
for i, n in enumerate(BOCA_B):
    estira = n >= 4
    pz = (17, -3) if estira else (16, 6)
    ojos = 'cerrados' if 2 <= i <= 9 else ('parpadeo' if i in (1, 10) else 'abiertos')
    poner(pose(pz, pz, ojos, ('bostezo', n) if 1 <= i <= 10 else 'feliz'), i, 4, 1 if estira else 0)

# 5. camina de lado: patitas alternadas y un saltito pequeño
for i in range(N):
    gy = 4 if (i // 2) % 2 == 0 else 6
    poner(pose((16, gy), (16, gy), 'parpadeo' if i == 7 else 'abiertos', patas=1 + i % 2), i, 5, i % 2)

hoja.save(OUT + '_hoja.png')
print('hoja ok')
