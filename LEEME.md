# Un rincón para Dallana

## Publicar la página estática

`Dallana.html` se puede abrir directamente o publicar en GitHub Pages. La dirección publicada de este repositorio es:

`https://eduardovalenzuelav.github.io/proyecto_priv/Dallana.html`

La experiencia romántica, las cartas, las notas del frasco, el selector de ánimo, los recordatorios y las actividades funcionan sin servidor. Los recuerdos, el contenido administrable y la carta usan contenido de respaldo cuando la API no está conectada. Favoritos, elementos descubiertos y actividades marcadas se guardan localmente en el navegador de cada visitante.

Para habilitar la API, asigna la URL HTTPS real de tu servicio a `URL_BACKEND` en `Dallana.html` (sin una ruta final; por ejemplo `https://nombre-del-servicio.onrender.com`). Actualmente está vacía a propósito: no hay un backend remoto configurado para este proyecto.

## Ejecutar la API

Requiere Python 3.9 o posterior.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:DALLANA_ADMIN_TOKEN = "una-clave-larga-y-privada"
$env:DALLANA_ALLOWED_ORIGINS = "http://localhost:5500,http://127.0.0.1:5500,https://eduardovalenzuelav.github.io"
uvicorn Dallana_main:app --reload --port 8000
```

Abre otra terminal para servir los archivos estáticos desde la carpeta del proyecto:

```powershell
python -m http.server 5500
```

En local, actualiza `URL_BACKEND` a `http://127.0.0.1:8000` (la página acepta HTTP solo en localhost). Para publicar, configura los mismos valores desde las variables del proveedor y usa la URL HTTPS del servicio. No subas `DALLANA_ADMIN_TOKEN` al repositorio ni lo pongas en el HTML.

## Despliegue en Render

Crea un Web Service conectado al repositorio con:

- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn Dallana_main:app --host 0.0.0.0 --port $PORT`
- `DALLANA_ADMIN_TOKEN`: una clave larga y privada.
- `DALLANA_ALLOWED_ORIGINS`: origen del sitio, por ejemplo `https://eduardovalenzuelav.github.io`.
- `DALLANA_DATA_FILE`: archivo de datos en un disco persistente, por ejemplo `/var/data/cumplidos.json`.
- `DALLANA_MEDIA_DIR`: carpeta de fotos en ese disco, por ejemplo `/var/data/fotos`.

Después configura en `Dallana.html` la URL HTTPS que Render asignó al servicio. Sin disco persistente, el sistema de archivos del proveedor puede reiniciarse y perder datos/fotos.

El panel valida `DALLANA_ADMIN_TOKEN` en cada operación privada del servidor. Permite gestionar recuerdos, fotos, carta final, saludos y las colecciones de autoestima, cartas «Ábreme cuando», frasco, museo y aventuras. Las fotos PNG, JPG, WebP y GIF pueden pesar hasta 8 MB.

## Contenido y recursos

El editor de las nuevas colecciones presenta el contenido completo como JSON y valida su estructura antes de enviarlo al backend; eso permite agregar, editar y eliminar entradas sin inventar recuerdos, gustos ni logros. Las vitrinas del museo empiezan sin detalles personales y pueden completarse con información real. El panel permite subir una imagen para la vitrina elegida; queda pendiente hasta guardar el contenido. Las imágenes locales se guardan en `assets/fotos/`; las que se suban desde el panel quedan en `DALLANA_MEDIA_DIR`.

Agrega stickers SVG o PNG transparentes en `assets/stickers/`. Las rutas se escriben desde el HTML, por ejemplo `assets/fotos/paseo-paicavi.jpg`. Todo archivo subido al repositorio público será visible en Internet.
