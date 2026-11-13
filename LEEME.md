# Un rincón para Dallana

## Abrir y publicar

Abre `Dallana.html` directamente o publica el proyecto con GitHub Pages:

`https://eduardovalenzuelav.github.io/proyecto_priv/Dallana.html`

La página carga sus estilos desde `Dallana.css` y su lógica desde `Dallana.js`; conserva los tres archivos juntos en la misma carpeta. «Cosas bonitas sobre ti» reúne afirmaciones y notas sorpresa del antiguo frasco. El mensaje de bienvenida cambia una vez al día. Las cartas «Ábreme cuando…», «Hoy necesito…», el museo de Dallana y las aventuras usan contenido local aunque la API no esté configurada. La carta final se puede abrir cuando quieras; las aventuras marcadas se guardan en el navegador de cada visitante.

Para habilitar la API, asigna la URL HTTPS del servicio a `URL_BACKEND` en `Dallana.js` (sin una ruta final; por ejemplo `https://nombre-del-servicio.onrender.com`). Actualmente está vacía a propósito, así que no hay un backend remoto configurado.

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

En otra terminal, sirve los archivos estáticos desde la carpeta del proyecto:

```powershell
python -m http.server 5500
```

Configura `URL_BACKEND` en `Dallana.js` como `http://127.0.0.1:8000` para desarrollo local (la página acepta HTTP solo en localhost). Para publicar, usa HTTPS y configura los valores del servidor mediante variables de entorno. No subas `DALLANA_ADMIN_TOKEN` al repositorio ni lo incluyas en el HTML o JavaScript.

## Despliegue en Render

Crea un Web Service conectado al repositorio con:

- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn Dallana_main:app --host 0.0.0.0 --port $PORT`
- `DALLANA_ADMIN_TOKEN`: una clave larga y privada.
- `DALLANA_ALLOWED_ORIGINS`: origen del sitio, por ejemplo `https://eduardovalenzuelav.github.io`.
- `DALLANA_DATA_FILE`: archivo de datos en un disco persistente, por ejemplo `/var/data/cumplidos.json`.
- `DALLANA_MEDIA_DIR`: carpeta de fotos en ese disco, por ejemplo `/var/data/fotos`.

Después configura en `Dallana.js` la URL HTTPS asignada al servicio. Sin disco persistente, el proveedor puede reiniciar y perder los datos y fotos guardados.

El panel protegido permite administrar recuerdos, carta final, saludos y colecciones de autoestima, cartas «Ábreme cuando», notas sorpresa, museo y aventuras. El museo muestra detalles de Dallana, separados de las afirmaciones y notas sorpresa. Las fotos PNG, JPG, WebP y GIF pueden pesar hasta 8 MB; el servidor contrasta el tipo declarado con la firma del archivo.

Cada cambio de datos conserva la versión anterior en `DALLANA_DATA_FILE.bak`. Si el JSON principal queda ilegible, la API se detiene con un error para evitar reemplazarlo con valores iniciales. Revisa el archivo `.bak` y restáuralo como `DALLANA_DATA_FILE` antes de volver a iniciar el servicio.

## Contenido y recursos

El editor de colecciones trabaja con JSON y valida la estructura antes de enviar cambios al backend. Agrega solo recuerdos, gustos y logros reales. Las imágenes seleccionadas desde el panel se guardan en `DALLANA_MEDIA_DIR`; los recursos estáticos deben estar en `assets/` y se publican junto con el repositorio.

Los archivos de `assets/fotos/` no se borran automáticamente si dejan de aparecer enlazados en el HTML: el backend puede referenciarlos desde datos administrados y pueden ser originales o respaldos. Antes de eliminarlos, revisa también el JSON de datos y las imágenes administradas. Los archivos versionados en GitHub Pages son públicos.

Agrega stickers SVG o PNG transparentes en `assets/stickers/` y usa rutas relativas desde el HTML.
