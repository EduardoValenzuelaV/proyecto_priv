# Regalo para Dallana

## Backend en Render

1. Sube `Dallana_main.py` y `requirements.txt` al servicio.
2. Usa `pip install -r requirements.txt` para instalar y `uvicorn Dallana_main:app --host 0.0.0.0 --port $PORT` para iniciar.
3. Configura `DALLANA_ADMIN_TOKEN` con una clave larga y privada.
4. Configura `DALLANA_ALLOWED_ORIGINS` con el origen exacto de la página publicada, por ejemplo `https://tupagina.netlify.app`. Para varios orígenes, sepáralos por coma. En desarrollo, el valor predeterminado permite `http://localhost:5500` y `http://127.0.0.1:5500`.
5. Conecta un disco persistente. Define `DALLANA_DATA_FILE=/var/data/cumplidos.json` y `DALLANA_MEDIA_DIR=/var/data/fotos` para conservar tanto mensajes como fotos entre despliegues.

## Página

1. En `Dallana.html`, cambia `URL_BACKEND` por la URL de Render y revisa `FECHA_INICIO` y `MENSAJES_PARA_CARTA`.
2. Publica `Dallana.html` en Netlify o GitHub Pages. Puedes agregar `musica.mp3` a la misma carpeta.
3. Entra al panel con la pequeña estrella de la esquina. La clave es la variable `DALLANA_ADMIN_TOKEN`.
4. Desde el panel puedes añadir, editar y borrar recuerdos, subir imágenes PNG/JPG/WebP/GIF, cambiar la carta y editar los saludos de mañana y noche.
5. Para el paseo de Paicaví, selecciona el recuerdo en el panel, sube una foto real y guarda los cambios.

El mensaje del día y los saludos se calculan según la hora de `America/Santiago`. El progreso y favoritos se guardan en el navegador de Dallana. Al descubrir 10 mensajes distintos se abre la carta una vez; después queda disponible el botón «Leer mi carta».
