# Progress

**What works**

- El frontend vuelve a ejecutarse; recuerdos, favoritos y contenido local se verificaron en navegador.
- 2026-11-15: service worker pasa a red primero (las publicaciones se ven al instante), iconos PWA cuadrados en `assets/icons/`, sin bucle de pétalos inactivo, errores de API legibles, login admin dentro de un `<form>`.
- 2026-11-15: rediseño visual v3 (CSS reescrito: paleta de 9 tokens, Fraunces + DM Sans + Caveat, breakpoints 600/900). Stickers en esquinas superiores de cada sección con franja reservada (`.sticker--tl/--tr`); verificado sin solapes a 375, 768 y 1280 px. Capítulos numerados 01–07.
- 2026-11-15: stickers 17–22 recortados a PNG con borde blanco tipo troquel (originales .jpg quedan sin uso). Nuevas variantes `.sticker--bl/--br` (esquinas inferiores, franja reservada), `.sticker-buddy` en portada y `.letter-sticker` al final de la carta. Cartas "Ábreme cuando" rediseñadas como sobres (`.oc-flap/.oc-letter/.oc-seal/.oc-label/.oc-title`, tonos alternos). CSS v3.3, JS v3.7, caché dallana-v3.7.
- 2026-11-15: paleta menos rosada: base crema, acento rojo cereza (`--vino:#d1343f`) y nuevos tokens `--azul/--azul-claro/--verde/--verde-claro/--mantequilla`; secciones alternan azul, verde y mantequilla; sobres en rojo/azul/verde/amarillo; película del álbum azul noche; corazones flotantes y celebración en rojo, azul y verde. CSS v3.4, JS v3.8, caché dallana-v3.8.
- 2026-11-15: nota de "Ábreme cuando" con estilo de carta escrita a mano (papel blanco, Caveat, garabatos SVG en tokens `--doodle-*`, sticker de Snoopy, resaltador en las 2 primeras palabras de cada frase vía `escribirConResaltes`). Sobres con marco cosido y flores en las esquinas (`.oc-deco`). CSS v3.5, JS v3.9, caché dallana-v3.9.
- 2026-11-15: reproductor (sección 01) rediseñado con los tokens del proyecto: polaroid con cinta washi, vinilo que gira (`.vinyl`), onda de 40 barras como barra de progreso con tiempo y seek (`#musicWave`, `pintarProgreso` en `Dallana.js`), iconos SVG en controles, Caveat en dedicatoria y pista. CSS v4.5, JS v3.18, caché dallana-v3.21. Sin verificar en navegador (el servidor local fue denegado).
- Las rutas públicas y administrativas de la API se verificaron con un almacenamiento temporal.
- 2026-11-18/19: avisos ntfy de visitas, actividad y tiempo en la página (`notificar`, `?de=dallana`, `?yo=1` excluye el navegador propio). 10 corazones por día; recuerdo pixel cada 5 sonrisas (5 GIF en `assets/pixel/`, generados con `propuesta/escena_*.py`).
- 2026-11-19: Alejandro, cangrejo ayudante en la esquina: novedades (`NOVEDADES`), aplaude, baila con música, duerme 23–7 h, bosteza, mensaje secreto al mantenerlo presionado.
- 2026-11-20: Alejandro 2.0 (diseño chibi, `propuesta/alejandro2.py`) con hoja de 6 filas × 12 cuadros de 72×86. 39 disfraces animados (`propuesta/disfraces2.py --hojas`) que cambian al azar con frase propia.
- 2026-11-20: Alejandro cartero: cartas de papá por ntfy con buzón guardado en `localStorage` (`dallanaBuzon`), «Dile algo a papá» (ntfy JSON a `NTFY_TEMA`), menú al tocarlo, paseo libre por la pantalla sin pisar el texto de cartas abiertas.
- 2026-11-20: sección «Buzón de papá» con buzón pixel, contador, última carta y aviso superior; `propuesta/` ordenada. CSS v6.1, JS v3.41, caché dallana-v3.50.

**Not started / backlog**

- Configurar `URL_BACKEND` y las variables del servidor cuando se publique la API.
- Comprimir canciones (46 MB) a 128 kbps: requiere instalar ffmpeg.
- `sw.js` precarga todas las canciones al instalar: cambiar a caché bajo demanda.
- Temas ntfy reservados (lectura/escritura protegidas).

**Known issues**

- ntfy.sh guarda las cartas 12 h: si Dallana no entra en ese tiempo, no le llegan.
- Los nombres de los temas ntfy están en el JS público.

_Keep bullets factual and small; link issues or PRs when useful._
