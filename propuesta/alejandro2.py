"""Alejandro 2.0: cangrejito chibi más adorable (ojos grandes con brillo, cachetitos, cuerpo de mochi).
Uso:
  python propuesta/alejandro2.py salida      -> salida_hoja.png (hoja de 6 filas x 12 cuadros de 44x54)
                                              -> salida_vista.png (vista grande para revisar)
Filas de la hoja: 0 salta, 1 aplaude, 2 baila, 3 duerme (Zzz), 4 bosteza, 5 camina de lado.
"""
import sys
from PIL import Image, ImageDraw

# ---------------- paleta ----------------
OUTL = (98, 28, 40)        # contorno suave (no negro)
R = (240, 76, 70)          # coral
r = (206, 58, 62)          # sombra
RR = (176, 40, 52)         # sombra profunda (patas)
L = (255, 152, 132)        # brillo
BRI = (255, 226, 214)      # punto de brillo
BELLY = (255, 206, 178)    # pancita
EYE = (40, 24, 36)
BL = (255, 255, 255)
BLUSH = (255, 128, 150)
BOCA = (122, 30, 46)
LENGUA = (255, 122, 140)

T = 10                      # margen arriba para gorros y pinzas sobre la cabeza
SW, SH = 44, 40 + T
cx = 22
def Y(v):
    return v + T

def contorno(S, col=OUTL):
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

def pinza(d, x0, gy, sx):
    """Pinza redondita tipo manito, con una muesca chiquita arriba y brillo."""
    d.ellipse([x0 - 5, Y(gy), x0 + 5, Y(gy + 10)], fill=r)
    d.ellipse([x0 - 5, Y(gy), x0 + 5, Y(gy + 8)], fill=R)
    d.ellipse([x0 - 3, Y(gy + 2), x0, Y(gy + 4)], fill=L)
    d.point((x0 - 2, Y(gy + 2)), fill=BRI)
    # muesca en V (la "boquita" de la pinza)
    d.polygon([(x0 + sx * 2, Y(gy + 4)), (x0 + sx * 1, Y(gy - 1)), (x0 + sx * 5, Y(gy - 1)), (x0 + sx * 6, Y(gy + 2))], fill=(0, 0, 0, 0))

def pose(gl=(17, 3), gr=(17, 3), ojos='abiertos', boca='feliz', patas=0, mira=0):
    """gl/gr: (distancia al centro, altura de arriba) de cada pinza.
    ojos: abiertos / parpadeo / cerrados (durmiendo) / felices (^ ^).
    boca: feliz / dormido / sonrisa / ('bostezo', n). patas: 0 quietas, 1-2 paso. mira: -1/0/1 pupilas."""
    S = Image.new('RGBA', (SW, SH), (0, 0, 0, 0))
    d = ImageDraw.Draw(S)
    # patitas cortas (3 por lado)
    for i, dy in enumerate((27, 30, 33)):
        if patas:
            alt = (i + patas) % 2
            pi, pd = (2 if alt else 4), (4 if alt else 2)
        else:
            pi = pd = 4
        d.line([cx - 10, Y(dy), cx - 15, Y(dy + 1), cx - 17, Y(dy + pi)], fill=RR, width=2)
        d.line([cx + 10, Y(dy), cx + 15, Y(dy + 1), cx + 17, Y(dy + pd)], fill=RR, width=2)
    # bracitos y pinzas
    for sx, (dx, gy) in ((-1, gl), (1, gr)):
        d.line([cx + sx * 11, Y(24), cx + sx * (dx - 1), Y(gy + 6)], fill=r, width=3)
        pinza(d, cx + sx * dx, gy, sx)
    # cuerpo de mochi: sombra abajo, color, brillo y pancita
    d.ellipse([cx - 14, Y(12), cx + 14, Y(37)], fill=r)
    d.ellipse([cx - 14, Y(12), cx + 14, Y(35)], fill=R)
    d.ellipse([cx - 8, Y(26), cx + 8, Y(36)], fill=BELLY)
    d.ellipse([cx - 8, Y(26), cx + 8, Y(32)], fill=BELLY)
    d.line([cx - 4, Y(36), cx + 4, Y(36)], fill=(236, 170, 150))
    d.ellipse([cx - 11, Y(14), cx - 5, Y(19)], fill=L)
    d.point([(cx - 9, Y(15)), (cx - 8, Y(15))], fill=BRI)
    # tallos de los ojos
    for sx in (-1, 1):
        ex = cx + sx * 6
        d.line([ex, Y(8), ex, Y(14)], fill=R, width=3)
        d.line([ex + sx, Y(9), ex + sx, Y(14)], fill=r)
    # ojos grandes y brillantes
    for sx in (-1, 1):
        ex = cx + sx * 6
        if ojos in ('abiertos',):
            d.ellipse([ex - 4, Y(0), ex + 4, Y(9)], fill=BL)
            px0 = ex + mira
            d.ellipse([px0 - 3, Y(1), px0 + 3, Y(9)], fill=EYE)
            d.rectangle([px0 - 2, Y(2), px0 - 1, Y(3)], fill=BL)
            d.point((px0 + 1, Y(7)), fill=BL)
            d.point((px0 - 2, Y(8)), fill=(90, 70, 110))
        else:
            d.ellipse([ex - 4, Y(1), ex + 4, Y(9)], fill=R)
            d.ellipse([ex - 3, Y(2), ex + 1, Y(4)], fill=L)
            if ojos == 'cerrados':      # ∪ dormido, con pestañita
                d.line([ex - 2, Y(6), ex + 2, Y(6)], fill=EYE)
                d.point([(ex - 3, Y(5)), (ex + 3, Y(5))], fill=EYE)
                d.point((ex + sx * 4, Y(4)), fill=EYE)
            elif ojos == 'felices':     # ^ ^
                d.line([ex - 3, Y(6), ex, Y(3), ex + 3, Y(6)], fill=EYE)
            else:                       # parpadeo
                d.line([ex - 3, Y(5), ex + 3, Y(5)], fill=EYE)
    # cachetitos
    for sx in (-1, 1):
        d.ellipse([cx + sx * 9 - 2, Y(19), cx + sx * 9 + 2, Y(21)], fill=BLUSH)
    # boca
    if boca == 'feliz':
        d.chord([cx - 3, Y(16), cx + 3, Y(24)], 0, 180, fill=BOCA)
        d.chord([cx - 2, Y(20), cx + 2, Y(24)], 0, 180, fill=LENGUA)
    elif boca == 'sonrisa':
        d.line([cx - 3, Y(19), cx - 1, Y(21), cx + 1, Y(21), cx + 3, Y(19)], fill=BOCA)
    elif boca == 'dormido':
        d.point([(cx - 2, Y(20)), (cx - 1, Y(21)), (cx, Y(20)), (cx + 1, Y(21)), (cx + 2, Y(20))], fill=BOCA)
    else:
        n = boca[1]
        if n == 0:
            d.line([cx - 2, Y(20), cx + 2, Y(20)], fill=BOCA)
        else:
            d.ellipse([cx - 1 - n // 2, Y(18), cx + 1 + n // 2, Y(19 + n)], fill=BOCA)
            if n >= 3:
                d.ellipse([cx - 1, Y(17 + n), cx + 1, Y(19 + n)], fill=LENGUA)
    return contorno(S)

# ---------------- hoja de sprites ----------------
FW, FH, N, FILAS = 44, 54, 12, 6
Z = ["111", "001", "010", "100", "111"]
ESTRELLA = ["010", "111", "010"]
CORA = ["0101", "1111", "0110"]

def hacer_hoja(pose_fn=pose):
    hoja = Image.new('RGBA', (FW * N, FH * FILAS), (0, 0, 0, 0))
    ds = ImageDraw.Draw(hoja)

    def poner(spr, i, fila, alto=0, dx=0, sombra=13):
        x0, y0 = i * FW + dx, fila * FH + FH - spr.height - alto
        if y0 < fila * FH:
            spr = spr.crop((0, fila * FH - y0, spr.width, spr.height)); y0 = fila * FH
        ancho = max(4, sombra - alto)
        ds.ellipse([i * FW + 22 - ancho, fila * FH + 51, i * FW + 22 + ancho, fila * FH + 53], fill=(0, 0, 0, 55))
        hoja.alpha_composite(spr, (x0, y0))

    def fig(forma, x, y, col):
        for rr, fila in enumerate(forma):
            for c, v in enumerate(fila):
                if v == '1' and 0 <= y + rr < hoja.height:
                    hoja.putpixel((x + c, y + rr), col + (255,))

    # 0. salta y saluda
    SALTO = [0, 0, 1, 3, 6, 8, 9, 8, 6, 3, 1, 0]
    for i, alto in enumerate(SALTO):
        gy = 2 if (alto >= 3 or i % 2 == 0) else 6
        poner(pose_fn((17, gy), (17, gy), 'parpadeo' if i == 1 else 'abiertos'), i, 0, alto)
    # 1. aplaude feliz con estrellitas
    for i in range(N):
        junta = i % 4 in (1, 2)
        pz = (6, -8) if junta else (14, -5)
        poner(pose_fn(pz, pz, 'felices'), i, 1, [0, 1, 1, 0][i % 4])
        if i % 4 == 2:
            fig(ESTRELLA, i * FW + 21, FH + 0, (255, 214, 80))
            fig(ESTRELLA, i * FW + 5, FH + 6, (255, 240, 160))
            fig(ESTRELLA, i * FW + 36, FH + 4, (255, 240, 160))
    # 2. baila meciéndose
    MECE = [0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 0, -1]
    for i in range(N):
        arriba, abajo = (15, -3), (16, 8)
        izq = (i // 3) % 2 == 0
        poner(pose_fn(arriba if izq else abajo, abajo if izq else arriba, 'felices' if i % 6 >= 4 else 'abiertos', mira=MECE[i]),
              i, 2, [0, 2, 3, 2][i % 4], MECE[i])
    # 3. duerme con Zzz
    for i in range(N):
        respira = 1 if (i // 3) % 2 else 0
        poner(pose_fn((15, 10), (15, 10), 'cerrados', 'dormido'), i, 3, respira, sombra=14)
        for n in range(2):
            t = ((i + n * 6) % N) / N
            fig(Z, i * FW + 31 + int(t * 7), 3 * FH + 11 - int(t * 11), (110, 120, 200) if t < .6 else (170, 180, 230))
    # 4. bosteza estirándose
    BOCA_B = [0, 1, 2, 4, 5, 6, 6, 6, 5, 3, 1, 0]
    for i, n in enumerate(BOCA_B):
        estira = n >= 4
        pz = (17, -3) if estira else (16, 6)
        ojos = 'cerrados' if 2 <= i <= 9 else ('parpadeo' if i in (1, 10) else 'abiertos')
        poner(pose_fn(pz, pz, ojos, ('bostezo', n) if 1 <= i <= 10 else 'feliz'), i, 4, 1 if estira else 0)
    # 5. camina de lado
    for i in range(N):
        gy = 3 if (i // 2) % 2 == 0 else 5
        poner(pose_fn((17, gy), (17, gy), 'parpadeo' if i == 7 else 'abiertos', patas=1 + i % 2, mira=1), i, 5, i % 2)
    return hoja

if __name__ == '__main__':
    OUT = sys.argv[1] if len(sys.argv) > 1 else 'alejandro2'
    hoja = hacer_hoja()
    hoja.save(OUT + '_hoja.png')
    # vista: primer cuadro de cada fila en grande + la hoja completa
    E = 6
    vista = Image.new('RGBA', (FW * 6 * E, FH * E), (250, 242, 232, 255))
    for k in range(6):
        cuadro = hoja.crop(([0, 2, 0, 5, 6, 0][k] * FW, k * FH, ([0, 2, 0, 5, 6, 0][k] + 1) * FW, (k + 1) * FH))
        vista.alpha_composite(cuadro.resize((FW * E, FH * E), Image.NEAREST), (k * FW * E, 0))
    vista.save(OUT + '_vista.png')
    print('ok')
