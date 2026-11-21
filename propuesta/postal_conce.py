"""Postal pixel de Concepción para el encabezado: el puente sobre el Biobío, Eduardo y Dallana de la mano
y Alejandro en la baranda. Tres versiones según la hora (mañana, tarde, noche).
Uso: python propuesta/postal_conce.py assets/pixel   -> postal-manana.png, postal-tarde.png, postal-noche.png
     (añade una ruta más para guardar una vista previa ampliada de las tres)
"""
import sys, os, math, random
from PIL import Image, ImageDraw

W, H = 160, 104
HORIZONTE = 58          # donde el río toca los cerros
PUENTE = 66             # altura del tablero del puente

PALETAS = {
    'manana': dict(cielo=[(150, 200, 245), (205, 228, 250), (255, 236, 200)], astro=(255, 232, 140), astro_y=18, astro_x=124,
                   cerro1=(120, 170, 110), cerro2=(86, 140, 90), ciudad=(190, 200, 215), ventana=(225, 232, 242),
                   rio=[(110, 165, 215), (90, 145, 200)], brillo=(235, 245, 255), puente=(205, 196, 185), sombra=(150, 140, 135),
                   farol=(120, 110, 105), luz=None, estrellas=False, nubes=(255, 255, 255)),
    'tarde': dict(cielo=[(110, 90, 170), (240, 130, 120), (255, 196, 120)], astro=(255, 214, 110), astro_y=44, astro_x=34,
                  cerro1=(150, 100, 120), cerro2=(110, 70, 100), ciudad=(170, 110, 130), ventana=(255, 214, 140),
                  rio=[(200, 120, 130), (150, 90, 130)], brillo=(255, 210, 140), puente=(220, 170, 150), sombra=(140, 90, 110),
                  farol=(110, 70, 90), luz=(255, 220, 140), estrellas=False, nubes=(255, 190, 170)),
    'noche': dict(cielo=[(20, 24, 60), (36, 42, 90), (60, 60, 120)], astro=(250, 245, 220), astro_y=16, astro_x=128,
                  cerro1=(38, 50, 80), cerro2=(28, 36, 64), ciudad=(44, 50, 90), ventana=(255, 214, 120),
                  rio=[(34, 44, 96), (24, 32, 76)], brillo=(255, 230, 160), puente=(80, 84, 120), sombra=(50, 52, 86),
                  farol=(60, 60, 96), luz=(255, 220, 130), estrellas=True, nubes=None),
}

ROJO, CORAZON = (214, 52, 63), (255, 92, 110)


def degradado(d, colores, y0, y1):
    n = len(colores) - 1
    for y in range(y0, y1):
        t = (y - y0) / max(1, (y1 - y0 - 1))
        k = min(n - 1, int(t * n))
        u = t * n - k
        c = tuple(int(colores[k][i] + (colores[k + 1][i] - colores[k][i]) * u) for i in range(3))
        d.line([0, y, W, y], fill=c)


def postal(nombre):
    P = PALETAS[nombre]
    rnd = random.Random(17)
    im = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(im)
    degradado(d, P['cielo'], 0, HORIZONTE)
    # estrellas o nubes
    if P['estrellas']:
        for _ in range(38):
            x, y = rnd.randrange(W), rnd.randrange(HORIZONTE - 14)
            d.point((x, y), fill=(255, 250, 220) if rnd.random() < .7 else (180, 200, 255))
        for (x, y) in ((22, 10), (70, 6), (98, 22)):
            d.point([(x, y - 1), (x - 1, y), (x, y), (x + 1, y), (x, y + 1)], fill=(255, 245, 200))
    elif P['nubes']:
        for (x, y, w) in ((14, 12, 22), (64, 20, 16), (96, 9, 18)):
            d.ellipse([x, y, x + w, y + 6], fill=P['nubes'])
            d.ellipse([x + w // 4, y - 3, x + w * 3 // 4, y + 4], fill=P['nubes'])
    # sol o luna
    ax, ay = P['astro_x'], P['astro_y']
    d.ellipse([ax - 8, ay - 8, ax + 8, ay + 8], fill=P['astro'])
    if nombre == 'noche':
        d.ellipse([ax - 4, ay - 9, ax + 11, ay + 6], fill=P['cielo'][0])   # luna creciente
    # cerros (el de atrás más claro)
    for x in range(W):
        y1 = int(HORIZONTE - 14 - 8 * math.sin(x / 26) - 5 * math.sin(x / 9 + 1))
        d.line([x, y1, x, HORIZONTE], fill=P['cerro1'])
    for x in range(W):
        y2 = int(HORIZONTE - 6 - 6 * math.sin(x / 18 + 2) - 2 * math.sin(x / 5))
        d.line([x, y2, x, HORIZONTE], fill=P['cerro2'])
    # ciudad en la otra orilla
    x = 2
    while x < W - 4:
        w, h = rnd.randint(4, 8), rnd.randint(5, 13)
        d.rectangle([x, HORIZONTE - h, x + w, HORIZONTE], fill=P['ciudad'])
        for wy in range(HORIZONTE - h + 2, HORIZONTE - 1, 3):
            for wx in range(x + 1, x + w, 2):
                if rnd.random() < (.55 if nombre == 'noche' else .3):
                    d.point((wx, wy), fill=P['ventana'])
        x += w + rnd.randint(1, 4)
    # río Biobío
    degradado(d, P['rio'], HORIZONTE, H)
    for y in range(HORIZONTE + 3, H, 4):
        for x in range(rnd.randrange(6), W, rnd.randint(10, 18)):
            d.line([x, y, x + rnd.randint(2, 5), y], fill=tuple(min(255, c + 22) for c in P['rio'][0]))
    # reflejo del sol o la luna en el agua
    for k, y in enumerate(range(HORIZONTE + 2, H - 2, 3)):
        ancho = max(1, 6 - k // 2)
        d.line([ax - ancho + (k % 2), y, ax + ancho - (k % 2), y], fill=P['brillo'])
    # el puente: tablero, pilares, baranda y faroles
    d.rectangle([0, PUENTE, W, PUENTE + 3], fill=P['puente'])
    d.line([0, PUENTE + 4, W, PUENTE + 4], fill=P['sombra'])
    for x in range(6, W, 22):
        d.rectangle([x, PUENTE + 5, x + 3, H], fill=P['sombra'])
        d.rectangle([x, PUENTE + 5, x, H], fill=P['puente'])
    d.line([0, PUENTE - 4, W, PUENTE - 4], fill=P['puente'])
    for x in range(0, W, 4):
        d.line([x, PUENTE - 4, x, PUENTE], fill=P['puente'])
    for x in range(16, W, 32):
        d.line([x, PUENTE - 13, x, PUENTE - 1], fill=P['farol'])
        d.rectangle([x - 1, PUENTE - 15, x + 1, PUENTE - 13], fill=P['luz'] or P['farol'])
        if P['luz']:
            for r in range(1, 4):
                for a in range(0, 360, 45):
                    px, py = x + round(r * 1.3 * math.cos(math.radians(a))), PUENTE - 14 + round(r * math.sin(math.radians(a)))
                    if 0 <= px < W and rnd.random() < .45 / r:
                        d.point((px, py), fill=P['luz'])
    # Eduardo y Dallana de la mano en el centro del puente
    bx, by = 74, PUENTE - 1
    # él: pelo oscuro, polera blanca, pantalón azul
    d.rectangle([bx, by - 11, bx + 2, by - 9], fill=(60, 40, 35))            # pelo
    d.rectangle([bx, by - 9, bx + 2, by - 8], fill=(232, 190, 160))          # cara
    d.rectangle([bx - 1, by - 7, bx + 3, by - 4], fill=(245, 245, 245))      # polera
    d.rectangle([bx, by - 3, bx + 2, by], fill=(60, 80, 140))                # piernas
    # ella: pelo largo y crespo, polera roja, falda
    gx = bx + 6
    d.rectangle([gx - 1, by - 11, gx + 3, by - 5], fill=(45, 30, 30))        # pelo largo
    d.rectangle([gx, by - 9, gx + 2, by - 8], fill=(225, 180, 150))          # cara
    d.point([(gx, by - 9), (gx + 2, by - 9)], fill=(150, 40, 50))            # lentes
    d.rectangle([gx - 1, by - 7, gx + 3, by - 4], fill=ROJO)                 # polera
    d.rectangle([gx, by - 3, gx + 2, by], fill=(70, 60, 80))
    d.line([bx + 3, by - 5, gx - 1, by - 5], fill=(232, 190, 160))           # las manos tomadas
    # corazoncito sobre ellos
    for (cx, cy) in ((bx + 3, by - 16), (bx + 5, by - 16)):
        d.point([(cx, cy), (cx + 1, cy)], fill=CORAZON)
    d.line([bx + 3, by - 15, bx + 7, by - 15], fill=CORAZON)
    d.line([bx + 4, by - 14, bx + 6, by - 14], fill=CORAZON)
    d.point((bx + 5, by - 13), fill=CORAZON)
    # Alejandro en la baranda
    ax2, ay2 = 104, PUENTE - 6
    d.rectangle([ax2, ay2, ax2 + 4, ay2 + 2], fill=(240, 76, 70))
    d.point([(ax2 - 1, ay2 - 1), (ax2 + 5, ay2 - 1)], fill=(240, 76, 70))   # pinzas arriba (saluda)
    d.point([(ax2 + 1, ay2 - 1), (ax2 + 3, ay2 - 1)], fill=(255, 255, 255))  # ojitos
    d.point([(ax2 + 1, ay2 + 3), (ax2 + 3, ay2 + 3)], fill=(176, 40, 52))
    return im


if __name__ == '__main__':
    carpeta = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(carpeta, exist_ok=True)
    ims = []
    for nombre in PALETAS:
        im = postal(nombre)
        im.save(os.path.join(carpeta, f'postal-{nombre}.png'), optimize=True)
        ims.append(im)
    if len(sys.argv) > 2:
        E = 4
        vista = Image.new('RGB', (W * E * 3 + 20, H * E), (240, 236, 226))
        for k, im in enumerate(ims):
            vista.paste(im.resize((W * E, H * E), Image.NEAREST), (k * (W * E + 10), 0))
        vista.save(sys.argv[2])
    print('ok')
