"""Dragoncitos pixel que vuelan detrás de la página: 10 dragones distintos, 3 cuadros de aleteo (arriba, medio, abajo).
Uso: python propuesta/dragones.py assets/pixel/dragones.png [vista_previa.png]
Hoja: 10 columnas (un dragón cada una) × 3 filas (cuadros), celdas de 68×48, mirando a la derecha.
Orden: 0 cereza · 1 serpentina jade · 2 bebé azul · 3 gordito mantequilla · 4 rosa de plumas · 5 lila dormilón
       6 arcoíris · 7 bebé menta con cascarón · 8 estrellado de noche · 9 durazno con flores
"""
import sys, os, math
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from alejandro2 import contorno

CW, CH = 68, 48
OFF = 2   # margen a la izquierda para que las colas no toquen el borde
BL, OJO, CACHETE, BORDE = (255, 255, 255), (36, 26, 40), (255, 150, 172), (68, 34, 52)
ARCOIRIS = [(240, 90, 100), (250, 160, 80), (250, 215, 90), (120, 200, 120), (110, 160, 235), (170, 130, 220)]


def tono(c, k):
    return tuple(max(0, min(255, int(v * k))) for v in c)


def capa():
    return Image.new('RGBA', (CW, CH), (0, 0, 0, 0))


def bezier(p0, p1, p2, n):
    out = []
    for i in range(n):
        t = i / (n - 1)
        out.append(((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
                    (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]))
    return out


# ---------------- alas ----------------
def ala(hx, hy, col, pose, escala=1.0, estilo='membrana', colores=None):
    """Capa con un ala: membrana con borde festoneado, nervaduras y borde más claro.
    estilo: membrana · plumas · hojas · estrellas. pose 0 arriba, 1 medio, 2 abajo."""
    im = capa(); d = ImageDraw.Draw(im)
    s = escala
    codo = {0: (-3, -9), 1: (-6, -4), 2: (-4, 5)}[pose]
    puntas = {0: [(-12, -18), (-3, -22), (6, -17)],
              1: [(-19, -8), (-11, -12), (-1, -11)],
              2: [(-14, 10), (-5, 14), (4, 10)]}[pose]
    ex, ey = hx + codo[0] * s, hy + codo[1] * s
    P = [(hx + px * s, hy + py * s) for px, py in puntas]
    atras = (hx - 7 * s, hy + (2 if pose != 2 else -1))
    if estilo == 'hojas':
        for p in P:
            d.polygon([(round(hx), round(hy)), (round(p[0] - 3), round(p[1] + 2)), (round(p[0]), round(p[1])), (round(p[0] + 3), round(p[1] + 2))], fill=col)
            d.line([round(hx), round(hy), round(p[0]), round(p[1])], fill=tono(col, .72))
        return im
    secciones = colores or [col, col, col]
    tris = [[(hx + 2, hy), P[2], P[1]], [(hx + 2, hy), P[1], P[0]], [(hx + 2, hy), P[0], atras]]
    for tri, c in zip(tris, secciones):
        d.polygon([(round(x), round(y)) for x, y in tri], fill=c)
    for a, b, c in ((P[2], P[1], secciones[0]), (P[1], P[0], secciones[1]), (P[0], atras, secciones[2])):
        d.line([round(a[0]), round(a[1]), round(b[0]), round(b[1])], fill=tono(c, 1.18), width=2)
    # festón: se recorta un semicírculo entre cada punta
    for a, b in ((P[2], P[1]), (P[1], P[0])):
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        vx, vy = hx - mx, hy - my
        L = math.hypot(vx, vy) or 1
        cx, cy = mx + vx / L * 1.5, my + vy / L * 1.5
        r = 2.4 * s
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0, 0))
    hueso = tono(secciones[1], .62)
    d.line([round(hx), round(hy), round(ex), round(ey)], fill=hueso, width=2)
    for p in P:
        d.line([round(ex), round(ey), round(p[0]), round(p[1])], fill=hueso)
        if estilo == 'plumas':
            d.ellipse([p[0] - 2.5, p[1] - 2.5, p[0] + 2.5, p[1] + 2.5], fill=tono(col, 1.15))
        if estilo == 'estrellas':
            x, y = round(p[0]), round(p[1])
            d.point([(x, y - 1), (x - 1, y), (x, y), (x + 1, y), (x, y + 1)], fill=(255, 236, 150))
    d.point((round(ex), round(ey) - 1), fill=tono(hueso, 1.4))
    return im


# ---------------- piezas del cuerpo ----------------
def cola(d, pts, col, grosor, punta, col_punta, puas_col=None):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        r = grosor * (1 - i / n) + .7
        d.ellipse([x - r, y - r, x + r, y + r], fill=col)
        if i % 3 == 0 and r > 1.4:
            d.ellipse([x - r * .6, y - r, x + r * .4, y - r * .3], fill=tono(col, 1.15))
    if puas_col:
        for i in range(2, n - 2, 3):
            x, y = pts[i]
            r = grosor * (1 - i / n) + .7
            h = max(1.5, r)
            c = puas_col[i % len(puas_col)] if isinstance(puas_col, list) else puas_col
            d.polygon([(round(x - 1.5), round(y - r + 1)), (round(x), round(y - r - h)), (round(x + 1.5), round(y - r + 1))], fill=c)
    tx, ty = pts[-1]
    if punta == 'corazon':
        for rr, fila in enumerate(["0110110", "1111111", "0111110", "0011100", "0001000"]):
            for c, v in enumerate(fila):
                if v == '1':
                    d.point((tx - 6 + c, ty - 3 + rr), fill=col_punta)
    elif punta == 'pica':
        d.polygon([(tx - 6, ty), (tx - 2, ty - 4), (tx + 1, ty), (tx - 2, ty + 4)], fill=col_punta)
    elif punta == 'estrella':
        pts5 = []
        for k in range(10):
            a = -math.pi / 2 + k * math.pi / 5
            rr = 4.5 if k % 2 == 0 else 2
            pts5.append((tx - 3 + rr * math.cos(a), ty + rr * math.sin(a)))
        d.polygon(pts5, fill=col_punta)
    elif punta == 'llama':
        d.polygon([(tx, ty - 1), (tx - 6, ty - 4), (tx - 4, ty), (tx - 7, ty + 3), (tx, ty + 2)], fill=col_punta)
        d.polygon([(tx - 1, ty), (tx - 4, ty - 2), (tx - 3, ty + 1)], fill=(255, 230, 140))
    elif punta == 'hoja':
        d.polygon([(tx, ty), (tx - 4, ty - 3), (tx - 8, ty), (tx - 4, ty + 3)], fill=col_punta)
        d.line([tx, ty, tx - 7, ty], fill=tono(col_punta, .7))


def cuerpo(d, cx, cy, rx, ry, col, panza, pecas=None):
    d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=tono(col, .8))
    d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry - 2], fill=col)
    d.ellipse([cx - rx + 2, cy - ry + 1, cx + rx * .3, cy - ry * .2], fill=tono(col, 1.1))
    d.ellipse([cx - rx + 4, cy - ry + 2, cx - rx + 8, cy - ry + 4], fill=tono(col, 1.28))
    d.ellipse([cx - rx * .35, cy - ry * .1, cx + rx * .95, cy + ry], fill=panza)
    for k in range(4):
        yy = cy + 1 + k * 2
        d.arc([cx - rx * .25, yy - 3, cx + rx * .85, yy + 1], 20, 160, fill=tono(panza, .82))
    if pecas:
        for (px, py) in ((-6, -4), (-2, -6), (-8, 0), (2, -4)):
            x, y = cx + px, cy + py
            d.point([(x, y - 1), (x - 1, y), (x, y), (x + 1, y), (x, y + 1)], fill=pecas)


def cuello(d, a, b, col, grosor):
    for (x, y) in bezier(a, ((a[0] + b[0]) / 2 + 2, a[1]), b, 9):
        d.ellipse([x - grosor, y - grosor, x + grosor, y + grosor], fill=col)


def pata(d, x, y, col, adelante=True):
    d.ellipse([x - 2, y - 2, x + 3, y + 2], fill=tono(col, .9))
    d.line([x, y + 1, x + (1 if adelante else -1), y + 4], fill=tono(col, .78), width=2)
    for k in range(3):
        d.point((x - 1 + k + (1 if adelante else -1), y + 5), fill=(250, 240, 220))


def cabeza(d, x, y, col, panza, acento, cuernos, ojo='abierto', g=1.0, pestanas=False, aleta=True):
    if aleta:
        d.polygon([(x - 5 * g, y - 1), (x - 11 * g, y - 4 * g), (x - 9 * g, y + 1), (x - 11 * g, y + 4 * g), (x - 4 * g, y + 3)], fill=acento)
    for (bx, by, lx, ly) in ((x - 3 * g, y - 4 * g, -7, -6), (x + 1 * g, y - 5 * g, -4, -8)):
        d.line([bx, by, bx + lx * g * .6, by + ly * g * .6, bx + lx * g, by + ly * g], fill=cuernos, width=2)
        d.point((round(bx + lx * g), round(by + ly * g)), fill=tono(cuernos, .75))
    d.ellipse([x - 6 * g, y - 6 * g, x + 6 * g, y + 5 * g], fill=col)
    d.ellipse([x - 4 * g, y - 5 * g, x + 1 * g, y - 2 * g], fill=tono(col, 1.15))
    d.ellipse([x + 1 * g, y - 2.5 * g, x + 11 * g, y + 4.5 * g], fill=col)
    d.ellipse([x + 3 * g, y + 1.5 * g, x + 10 * g, y + 4.5 * g], fill=panza)
    d.point((round(x + 9 * g), round(y - 1 * g)), fill=tono(col, .45))
    d.line([round(x + 5 * g), round(y + 2.5 * g), round(x + 8 * g), round(y + 2 * g)], fill=tono(col, .55))
    d.ellipse([x - 3 * g, y + 1 * g, x + 1 * g, y + 3.5 * g], fill=CACHETE)
    ex, ey = round(x + 1.5 * g), round(y - 2 * g)
    if ojo == 'abierto':
        d.ellipse([ex - 2, ey - 3, ex + 2, ey + 2], fill=OJO)
        d.rectangle([ex - 1, ey - 2, ex, ey - 1], fill=BL)
        d.point((ex + 1, ey + 1), fill=(150, 140, 190))
        if pestanas:
            d.line([ex + 2, ey - 3, ex + 4, ey - 5], fill=OJO)
    else:
        d.arc([ex - 3, ey - 2, ex + 2, ey + 2], 0, 180, fill=OJO)


# ---------------- dragones alados ----------------
def dragon(pose, col, panza, acento, cuernos, punta, col_punta, estilo='membrana', ala_col=None, ala_colores=None,
           gordo=0, cabeza_g=1.0, ala_g=1.0, ojo='abierto', pestanas=False, pecas=None, puas_cola=None, extras=()):
    im = capa(); d = ImageDraw.Draw(im)
    bx, by = 31 + OFF, 31
    rx, ry = 11 + gordo, 8 + gordo // 2
    hombro = (bx + 3, by - ry + 3)
    alac = ala_col or tono(col, .8)
    lejos = ala(hombro[0] - 4, hombro[1] + 1, tono(alac, .7), pose, escala=ala_g * .78, estilo=estilo,
                colores=[tono(c, .7) for c in ala_colores] if ala_colores else None)
    im.alpha_composite(lejos)
    d = ImageDraw.Draw(im)
    pts = bezier((bx - rx + 3, by + 1), (bx - rx - 8, by + 9 - pose * 2), (bx - rx - 11, by - 3 + pose), 12)
    cola(d, pts, col, 4.2, punta, col_punta, puas_col=puas_cola or acento)
    cerca = ala(hombro[0], hombro[1], alac, pose, escala=ala_g, estilo=estilo, colores=ala_colores)
    if pose < 2:
        im.alpha_composite(cerca)
        d = ImageDraw.Draw(im)
    pata(d, bx + 5, by + ry - 1, col, adelante=False)
    cuello(d, (bx + 6, by - 2), (bx + 15, by - 13), col, 3.6)
    cuerpo(d, bx, by, rx, ry, col, panza, pecas=pecas)
    for i, (px, py) in enumerate([(bx - 7, by - ry + 1), (bx - 2, by - ry), (bx + 3, by - ry), (bx + 9, by - 7), (bx + 12, by - 11)]):
        c = acento[i % len(acento)] if isinstance(acento, list) else acento
        d.polygon([(px - 2, py + 1), (px, py - 3), (px + 2, py + 1)], fill=c)
        d.point((px, py - 2), fill=tono(c, 1.2))
    pata(d, bx - 4, by + ry - 1, col)
    cabeza(d, bx + 18, by - 16, col, panza, acento[0] if isinstance(acento, list) else acento, cuernos,
           ojo=ojo, g=cabeza_g, pestanas=pestanas)
    if pose == 2:
        im.alpha_composite(cerca)
        d = ImageDraw.Draw(im)
    for extra in extras:
        extra(d, pose, bx, by)
    return im


# ---------------- adornos ----------------
def corazones(d, pose, bx, by):
    x, y = [(58 + OFF, 12), (59 + OFF, 7), (60 + OFF, 2)][pose]
    for rr, fila in enumerate(["0101", "1111", "0110"]):
        for c, v in enumerate(fila):
            if v == '1':
                d.point((x + c - 3, y + rr), fill=(230, 70, 90) if pose != 1 else (255, 140, 160))


def zzz(d, pose, bx, by):
    for k, (x, y) in enumerate(((54 + OFF, 6), (57 + OFF, 2))):
        if (pose + k) % 2 == 0:
            for (a, b) in ((0, 0), (1, 0), (2, 0), (1, 1), (0, 2), (1, 2), (2, 2)):
                d.point((x + a, y + b), fill=(110, 100, 180))


def esponja(d, pose, bx, by):
    for (x, y) in ((bx - 7, by - 8), (bx - 1, by - 10), (bx + 5, by - 8)):
        d.ellipse([x - 4, y - 3, x + 4, y + 3], fill=(196, 176, 236))


def cascaron(d, pose, bx, by):
    hx, hy = bx + 18 * 1.15, by - 16
    d.chord([hx - 8, hy - 12, hx + 7, hy + 1], 180, 360, fill=(252, 250, 240))
    for k in range(5):
        x = hx - 8 + k * 3
        d.polygon([(x, hy - 6), (x + 1.5, hy - 3), (x + 3, hy - 6)], fill=(252, 250, 240))
    d.point([(round(hx - 3), round(hy - 9)), (round(hx + 2), round(hy - 10))], fill=(150, 210, 180))


def corona(d, pose, bx, by):
    hx, hy = bx + 18, by - 16
    d.line([hx - 7, hy - 5, hx + 6, hy - 5], fill=(110, 170, 90))
    for k, c in enumerate(((255, 160, 190), (255, 255, 255), (255, 200, 120), (255, 160, 190))):
        x, y = hx - 6 + k * 3.5, hy - 7 - (1 if k in (1, 2) else 0)
        d.ellipse([x - 1.8, y - 1.8, x + 1.8, y + 1.8], fill=c)
        d.point((round(x), round(y)), fill=(250, 210, 80))


def llamita(d, pose, bx, by):
    if pose == 1:
        return
    x, y = 58 + OFF, 18
    d.polygon([(x, y), (x + 4, y - 3), (x + 3, y), (x + 5, y + 1), (x + 2, y + 2)], fill=(250, 140, 70))
    d.point((x + 2, y), fill=(255, 230, 140))


def serpentina(pose):
    """Dragón oriental jade: largo y ondulado, escamas, panza dorada, crin naranja, 4 patitas, bigotes y perla."""
    im = capa(); d = ImageDraw.Draw(im)
    col, panza, crin = (64, 160, 112), (240, 214, 130), (245, 130, 80)
    fase = pose * 2.1
    segs = [(8 + OFF + i * 1.65, 28 + 7 * math.sin(i / 3.2 + fase)) for i in range(24)]
    for i, (x, y) in enumerate(segs):
        r = 2.6 + i * .1
        d.ellipse([x - r, y - r, x + r, y + r], fill=col)
    for i, (x, y) in enumerate(segs):
        r = 2.6 + i * .1
        d.point((round(x), round(y + r - 1)), fill=panza)
        if i % 2:
            d.point((round(x), round(y - 1)), fill=tono(col, .82))
        if i % 3 == 1:
            d.polygon([(round(x) - 1, round(y - r + 1)), (round(x) + 1, round(y - r - 4)), (round(x) + 2, round(y - r + 1))], fill=crin)
    for i in (5, 10, 15, 20):
        x, y = segs[i]
        d.line([x, y + 3, x + 1, y + 6], fill=tono(col, .75), width=2)
        d.point([(round(x), round(y + 7)), (round(x + 2), round(y + 7))], fill=(250, 240, 220))
    tx, ty = segs[0]
    for k in range(5):
        d.line([tx, ty, tx - 5, ty - 4 + k * 2], fill=crin)
    hx, hy = segs[-1][0] + 4, segs[-1][1] - 4
    cabeza(d, hx, hy, col, panza, crin, (250, 214, 120), aleta=False)
    for k in range(3):
        d.line([hx - 5, hy - 2 + k * 2, hx - 11, hy - 6 + k * 3], fill=crin)
    d.line([hx + 9, hy + 2, hx + 12, hy + 7 - pose, hx + 10, hy + 10], fill=(250, 220, 120))
    d.line([hx + 8, hy + 3, hx + 9, hy + 9 - pose], fill=(250, 220, 120))
    px, py = segs[20][0] + 3, segs[20][1] + 8
    d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=(255, 190, 210))
    d.point((round(px - 1), round(py - 1)), fill=BL)
    return im


DRAGONES = [
    lambda p: dragon(p, (214, 52, 63), (255, 216, 196), (246, 196, 80), (250, 236, 200), 'corazon', (255, 226, 120), pestanas=True),
    serpentina,
    lambda p: dragon(p, (61, 114, 196), (214, 232, 255), (150, 205, 255), (240, 236, 220), 'pica', (150, 205, 255), cabeza_g=1.2, ala_g=1.2),
    lambda p: dragon(p, (240, 188, 70), (255, 244, 210), (232, 120, 80), (250, 236, 200), 'llama', (240, 120, 70), gordo=3, ala_g=.85, extras=(corazones,)),
    lambda p: dragon(p, (238, 128, 160), (255, 226, 236), (255, 196, 214), (255, 244, 236), 'corazon', (214, 52, 63), estilo='plumas', pestanas=True, ala_g=1.05),
    lambda p: dragon(p, (168, 140, 220), (238, 230, 255), (255, 214, 110), (250, 240, 215), 'estrella', (255, 214, 110), ojo='dormido', ala_g=.8, extras=(esponja, zzz)),
    lambda p: dragon(p, (236, 228, 250), (255, 252, 255), ARCOIRIS, (255, 220, 120), 'estrella', (250, 200, 90),
                     ala_colores=[(255, 170, 180), (255, 220, 140), (170, 215, 250)], puas_cola=ARCOIRIS, pestanas=True),
    lambda p: dragon(p, (120, 200, 170), (226, 250, 238), (90, 170, 140), (250, 245, 225), 'pica', (90, 170, 140), cabeza_g=1.15, ala_g=.75, extras=(cascaron,)),
    lambda p: dragon(p, (60, 70, 138), (190, 200, 240), (255, 214, 110), (255, 236, 170), 'estrella', (255, 214, 110),
                     estilo='estrellas', ala_col=(232, 186, 80), pecas=(255, 226, 140)),
    lambda p: dragon(p, (255, 166, 128), (255, 232, 212), (120, 190, 110), (250, 240, 220), 'hoja', (110, 180, 100),
                     estilo='hojas', ala_col=(126, 196, 112), pestanas=True, extras=(corona, llamita)),
]


def hoja():
    h = Image.new('RGBA', (CW * len(DRAGONES), CH * 3), (0, 0, 0, 0))
    for n, fn in enumerate(DRAGONES):
        for pose in range(3):
            h.alpha_composite(contorno(fn(pose), BORDE), (n * CW, pose * CH))
    return h


if __name__ == '__main__':
    salida = sys.argv[1] if len(sys.argv) > 1 else 'dragones.png'
    H = hoja()
    H.save(salida, optimize=True)
    if len(sys.argv) > 2:
        E = 4
        prev = Image.new('RGB', (H.width * E, H.height * E), (226, 233, 250))
        g = H.resize((H.width * E, H.height * E), Image.NEAREST)
        prev.paste(g, (0, 0), g)
        prev.save(sys.argv[2])
    print('ok', H.size)
