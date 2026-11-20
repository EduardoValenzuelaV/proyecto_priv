# Tech context

**Stack**

- Sitio estático: `Dallana.html`, `Dallana.css`, `Dallana.js`, `sw.js` (service worker red primero), `manifest.json`.
- Publicado en GitHub Pages: https://eduardovalenzuelav.github.io/proyecto_priv/Dallana.html
- Backend opcional en Python (`Dallana_main.py`); el sitio funciona sin él.
- Pixel art: scripts Python + Pillow en `propuesta/`.

**Servicios externos**

- ntfy.sh: `NTFY_TEMA` (avisos y mensajes de Dallana para Eduardo) y `NTFY_CARTAS` (cartas de Eduardo para Dallana, lectura con `/json?poll=1`). Títulos con emoji solo vía publicación JSON (los headers HTTP no aceptan emoji).

**Build & test**

- Sin build. Pruebas: Edge headless (`msedge --headless --dump-dom/--screenshot`) con un script de prueba inyectado; `fetch` simulado para no enviar avisos reales. Edge headless no baja de ~496 px de ancho y las capturas ignoran el scroll.

**Constraints**

- En este equipo no hay Node. ffmpeg está instalado con winget (`Gyan.FFmpeg`, en `%LOCALAPPDATA%\Microsoft\WinGet\Packages`). Servidor local de prueba: `.claude/launch.json` (`python -m http.server 8765`, sin soporte de Range).
- Cada cambio de CSS/JS sube versiones en `Dallana.html` y `sw.js`.
