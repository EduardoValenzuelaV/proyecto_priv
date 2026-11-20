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
- En CSS el sprite se escala ×2 (escritorio) o ×1,5 (teléfono) con `steps(12)` e `image-rendering:pixelated`.

## Alejandro (Dallana.js)

- Estado en `data-estado` del `<aside>`; prioridad: reacción > música > hablando > caminando > hora.
- Movimiento con la propiedad CSS `translate` (no `transform`, que se usa para agacharse al hacer scroll). En su esquina no lleva `translate` (ni siquiera 0): crearía un marco para los globos `position:fixed` del teléfono.
- Antes de hablar (globo, frase, carta) vuelve a su esquina con `volverACasa()`.
