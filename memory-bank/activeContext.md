# Active context

**Current focus**: Alejandro (cangrejo ayudante) y el sistema de cartas entre Eduardo y Dallana. Última tarea: hacer más visible el «Buzón de papá».

**In progress**:

- [x] Sección «Buzón de papá» en la página (`#buzonSection`, buzón pixel `assets/pixel/buzon.png`) + aviso arriba `#cartaAviso` cuando llega una carta.
- [x] Limpieza de `propuesta/` (scripts viejos borrados).
- [ ] Comprimir canciones a 128 kbps: pendiente, ffmpeg no aparece instalado (winget no lo registra).

**Decisions (recent)**:

- Cartas de papá llegan por ntfy (tema `NTFY_CARTAS` en `Dallana.js`); los mensajes de Dallana van al tema de avisos `NTFY_TEMA`. ntfy.sh guarda solo 12 h.
- Alejandro vive en la capa superior (`popover="manual"`) para seguir visible sobre los diálogos de cartas; nunca camina sobre el texto (`zonasCarta()`).
- Disfraces: 39 hojas en `assets/pixel/disfraces/`, cambio aleatorio cada 3–6 min; de noche pijama.
- De noche (23–7 h) duerme, pero cualquier actividad (toque, tecla, scroll) lo despierta y actúa como de día; tras 90 s sin actividad vuelve a dormir (`actividadUsuario`, `INACTIVIDAD_DORMIR`).

**Open questions**:

- Los temas ntfy son públicos (están en el JS): evaluar temas reservados con ntfy Pro.
- Precarga de 46 MB de música en `sw.js` al instalar: pasar a caché bajo demanda.

_Update when the task or branch focus changes._
