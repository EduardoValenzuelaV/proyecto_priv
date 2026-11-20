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
# Celdas de 72x86 para que quepan gorros, espadas y capas de los disfraces.
# El cangrejo (lienzo de 44x50) queda en x=14 y con su base en y=86 (como antes, pero con margen).
FW, FH, N, FILAS = 72, 86, 12, 6
CX0, CY0 = 14, 36            # dónde va el lienzo del cangrejo dentro de la celda (si no salta)
Z = ["111", "001", "010", "100", "111"]
ESTRELLA = ["010", "111", "010"]

def render_base(kw):
    """Dibuja solo a Alejandro. Devuelve (imagen, x del lienzo del cangrejo, y del lienzo)."""
    return pose(**{k: v for k, v in kw.items() if not k.startswith('_')}), 0, 0

def cuadros():
    """Lista de (fila, i, kw, alto, dx). kw['_fijo'] dice qué no puede cambiar un disfraz."""
    out = []
    SALTO = [0, 0, 1, 3, 6, 8, 9, 8, 6, 3, 1, 0]
    for i, alto in enumerate(SALTO):
        gy = 2 if (alto >= 3 or i % 2 == 0) else 6
        out.append((0, i, dict(gl=(17, gy), gr=(17, gy), ojos='parpadeo' if i == 1 else 'abiertos', _fijo=set()), alto, 0))
    for i in range(N):
        junta = i % 4 in (1, 2)
        pz = (6, -8) if junta else (14, -5)
        out.append((1, i, dict(gl=pz, gr=pz, ojos='felices', _fijo={'ojos'}), [0, 1, 1, 0][i % 4], 0))
    MECE = [0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 0, -1]
    for i in range(N):
        arriba, abajo = (15, -3), (16, 8)
        izq = (i // 3) % 2 == 0
        out.append((2, i, dict(gl=arriba if izq else abajo, gr=abajo if izq else arriba,
                               ojos='felices' if i % 6 >= 4 else 'abiertos', mira=MECE[i], _fijo=set()), [0, 2, 3, 2][i % 4], MECE[i]))
    for i in range(N):
        out.append((3, i, dict(gl=(15, 10), gr=(15, 10), ojos='cerrados', boca='dormido', _fijo={'ojos', 'boca'}), 1 if (i // 3) % 2 else 0, 0))
    BOCA_B = [0, 1, 2, 4, 5, 6, 6, 6, 5, 3, 1, 0]
    for i, n in enumerate(BOCA_B):
        estira = n >= 4
        pz = (17, -3) if estira else (16, 6)
        ojos = 'cerrados' if 2 <= i <= 9 else ('parpadeo' if i in (1, 10) else 'abiertos')
        out.append((4, i, dict(gl=pz, gr=pz, ojos=ojos, boca=('bostezo', n) if 1 <= i <= 10 else 'feliz', _fijo={'ojos', 'boca'}), 1 if estira else 0, 0))
    for i in range(N):
        gy = 3 if (i // 2) % 2 == 0 else 5
        out.append((5, i, dict(gl=(17, gy), gr=(17, gy), ojos='parpadeo' if i == 7 else 'abiertos', patas=1 + i % 2, mira=1, _fijo=set()), i % 2, 0))
    return out

def hacer_hoja(render=render_base):
    hoja = Image.new('RGBA', (FW * N, FH * FILAS), (0, 0, 0, 0))
    ds = ImageDraw.Draw(hoja)

    def fig(forma, x, yy, col):
        for rr, fila in enumerate(forma):
            for c, v in enumerate(fila):
                if v == '1' and 0 <= yy + rr < hoja.height:
                    hoja.putpixel((x + c, yy + rr), col + (255,))

    for fila, i, kw, alto, dx in cuadros():
        im, rx, ry = render(kw)
        x0, y0 = i * FW + CX0 - rx + dx, fila * FH + CY0 - ry - alto
        # recorta lo que se saldría de la celda
        cx0, cy0 = max(x0, i * FW), max(y0, fila * FH)
        cx1, cy1 = min(x0 + im.width, (i + 1) * FW), min(y0 + im.height, (fila + 1) * FH)
        trozo = im.crop((cx0 - x0, cy0 - y0, cx1 - x0, cy1 - y0))
        ancho = max(4, (14 if fila == 3 else 13) - alto)
        bx, by = i * FW + CX0 + 22, fila * FH + FH - 3
        ds.ellipse([bx - ancho, by, bx + ancho, by + 2], fill=(0, 0, 0, 55))
        hoja.alpha_composite(trozo, (cx0, cy0))
        # efectos: estrellitas al aplaudir y Zzz al dormir (coordenadas de la celda vieja + desplazamiento)
        ox, oy = i * FW + CX0, fila * FH + CY0 - 4
        if fila == 1 and i % 4 == 2:
            fig(ESTRELLA, ox + 21, oy + 0, (255, 214, 80))
            fig(ESTRELLA, ox + 5, oy + 6, (255, 240, 160))
            fig(ESTRELLA, ox + 36, oy + 4, (255, 240, 160))
        if fila == 3:
            for n in range(2):
                t = ((i + n * 6) % N) / N
                fig(Z, ox + 31 + int(t * 7), oy + 11 - int(t * 11), (110, 120, 200) if t < .6 else (170, 180, 230))
    return hoja

if __name__ == '__main__':
    OUT = sys.argv[1] if len(sys.argv) > 1 else 'alejandro2'
    hoja = hacer_hoja()
    hoja.save(OUT + '_hoja.png')
    # vista: primer cuadro de cada fila en grande + la hoja completa
    E = 4
    vista = Image.new('RGBA', (FW * 6 * E, FH * E), (250, 242, 232, 255))
    for k in range(6):
        c = [0, 2, 0, 5, 6, 0][k]
        cuadro = hoja.crop((c * FW, k * FH, (c + 1) * FW, (k + 1) * FH))
        vista.alpha_composite(cuadro.resize((FW * E, FH * E), Image.NEAREST), (k * FW * E, 0))
    vista.save(OUT + '_vista.png')
    print('ok')
