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
