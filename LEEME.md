# Un rincón para Dallana

## Publicar la página

`Dallana.html` se puede publicar directamente en GitHub Pages. La URL pública del proyecto es:

`https://eduardovalenzuelav.github.io/proyecto_priv/Dallana.html`

La página muestra recuerdos de respaldo y una carta sin necesitar el backend. El contador considera el 17 de octubre de 2026 como el primer día. Los descubrimientos y favoritos se guardan en el navegador de cada visitante. La música ambiental se genera en el navegador al tocar el sobre o el botón de música; no hace falta un archivo MP3.

## Activar el panel privado y sincronizar cambios

Para editar recuerdos, fotos, carta y saludos desde el panel secreto, despliega `Dallana_main.py` como Web Service en Render conectado a este repositorio:

- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn Dallana_main:app --host 0.0.0.0 --port $PORT`
- Variable `DALLANA_ADMIN_TOKEN`: define una clave larga y privada.
- Variable `DALLANA_ALLOWED_ORIGINS`: `https://eduardovalenzuelav.github.io`

Luego reemplaza en `Dallana.html` la constante `URL_BACKEND` por la URL real de tu servicio Render y sube el cambio a `main`. Para conservar los recuerdos y fotos que se administren, conecta un disco persistente y define `DALLANA_DATA_FILE=/var/data/cumplidos.json` y `DALLANA_MEDIA_DIR=/var/data/fotos`.

El panel de administración necesita que la API esté disponible. Las fotos se aceptan en PNG, JPG, WebP y GIF, hasta 8 MB. La página guarda el progreso de descubrimientos y los favoritos localmente en el navegador.