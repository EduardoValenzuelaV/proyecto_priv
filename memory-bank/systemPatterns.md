# System patterns

Document **architecture** and **recurring patterns** so Copilot stays aligned.

- **High-level layout** (modules, services, boundaries):
- **Data flow**:
- **Patterns to follow** (naming, error handling, testing style):
- **Patterns to avoid**:

_Link to key files or packages when it saves repetition._

## Estilos (v3)

- Colores solo vía tokens de `:root` en `Dallana.css`; no añadir hex sueltos.
- Stickers: `<img class="sticker sticker--tl|tr">` como hijo directo de la sección; la sección reserva la franja superior con `:has(>.sticker)`. Máximo dos por sección.
- Al cambiar CSS/JS, subir `?v=` en `Dallana.html` y `CACHE_NAME` en `sw.js`.

## Pixel art

- Todo el pixel art se genera con Python + PIL en `propuesta/` (sprites como formas o grillas, contorno con `contorno()`, escalado NEAREST). No editar los PNG a mano.
- Alejandro: `propuesta/alejandro2.py` → `assets/pixel/alejandro.png` (6 filas: salta, aplaude, baila, duerme, bosteza, camina; celdas 72×86). Disfraces: `propuesta/disfraces2.py --hojas assets/pixel/disfraces`.
- En CSS el sprite se escala ×1,75 (escritorio) o ×1 (teléfono, 72×86) con `steps(12)` e `image-rendering:pixelated`.

## Alejandro (Dallana.js)

- Estado en `data-estado` del `<aside>`; prioridad: reacción > música > hablando > caminando > hora.
- Movimiento con la propiedad CSS `translate` (no `transform`, que se usa para agacharse al hacer scroll). En su esquina no lleva `translate` (ni siquiera 0): crearía un marco para los globos `position:fixed` del teléfono.
- Antes de hablar (globo, frase, carta) vuelve a su esquina con `volverACasa()`. No habla si hay un `<dialog>` abierto.

## Alejandro: mapa de estados (Dallana.js)

- **Filas del sprite** (`alejandro.png` y cada disfraz, 72×86, 12 cuadros, 11 filas): 0 salto · 1 aplaudir · 2 bailar · 3 dormir · 4 bostezar · 5 caminar · 6 saludar · 7 llorar · 8 enamorado · 9 enojado · 10 mareado. Si se agregan filas: `propuesta/alejandro2.py` y luego `disfraces2.py --hojas assets/pixel/disfraces`; actualizar `background-size` en CSS (sprite, portada, carga, estampilla) y subir `?v=` de las hojas.
- **Estado visible** (`estadoAlejandro`): reacción (`alejandroReacciona(tipo, ms)`) > música > globo abierto > caminando > hora (`dormir` 23–7 salvo `despiertoDeNoche`). Caminar borra la reacción del momento.
- **Moverse**: `caminarA` marca `alejandroMoviendo`; `enCasa()` solo es true cuando llegó (sin `translate`). Los globos solo se abren en casa (si no, los `position:fixed` del teléfono se angostan).
- **Hablar**: `alejandroDice(texto, titulo, accion, importante)` devuelve si habló. No habla con globo grande, diálogo abierto o portada visible; lo `importante` queda en `dichosPendientes` y se dice al cerrar (`decirPendientes`).
- **Disfraz**: `ponerDisfraz`; rotación cada 2–4 min (`programarDisfraz`); de noche pijama; fecha especial (`FECHAS_ALEJANDRO`, `disfrazDelDia`) manda todo el día; `guia-de-museo` (máximo 2 min, `GUIA_MAX`) y `cartero` fuera de la rotación.
- **Rutinas** (`RUTINAS`, una vez al día en `dallanaRutinas`): mañana 7–12, almuerzo 13–15, tarde 17–20, noche 21–23; se revisan al saludar y cada minuto. `CUMPLE_DALLANA` = 12 de agosto (disfraz de cumpleaños, llora de emoción y confeti).
- **Reacciones**: 6 toques en 2,5 s → enojado; scroll muy rápido → mareado (cada 5 min); carta principal leída >30 s → llora; 10 corazones → enamorado; ≥2 días sin entrar → llora «te extrañé»; pestaña oculta >20 min → saluda; carta nueva → «!» y corre al buzón; mensaje a papá → disfraz de cartero mientras entrega.
- **Comandos de papá** por ntfy: `/borrar`, `/editar`, `/buzon`, `/alejandro <frase>`, `/disfraz <nombre>`.

## Animaciones

- Todas respetan `prefers-reduced-motion` (`animarMucho()`).
- Nada que dependa solo de IntersectionObserver para mostrar contenido: siempre hay respaldo (scroll/tiempo).
- Web Audio solo en PC con mouse; en teléfonos se usa la onda animada (bloquear la pantalla podría cortar la música).
