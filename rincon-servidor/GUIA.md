# Servidor del rincón (Cloudflare, gratis)

Con este servidor:

- **El buzón queda privado.** Los temas de ntfy ya no aparecen en la página. Para leer o mandar mensajes hay que conocer la clave (PIN) que solo sabe Dallana.
- **Las cartas no se pierden.** Cada 15 minutos, y cada vez que Dallana entra, el servidor copia tus cartas de ntfy y las guarda para siempre, aunque ntfy las borre a las 12 horas.
- **Puedes programar cartas.** Escribe en ntfy `/programar 2026-12-17 Tu carta…` y aparecerá en el buzón ese día (hora de Chile).
- **El progreso de Dallana se respalda.** Si cambia de teléfono o borra los datos, al escribir la clave recupera su buzón, sus corazones, su récord y lo demás.

Mientras `URL_RINCON` esté vacío en `Dallana.js`, la página funciona como siempre, directo con ntfy.

## 1. Crear la cuenta (lo haces tú)

1. Entra a <https://dash.cloudflare.com/sign-up> y crea una cuenta gratis.
2. Instala Node.js LTS desde <https://nodejs.org> (necesario para `npx wrangler`).

## 2. Elegir los secretos

Anota estas cuatro cosas en un lugar seguro (no en el repositorio):

| Secreto | Qué es | Ejemplo |
|---|---|---|
| `PIN` | La clave que escribirá Dallana | `1710` (una fecha de ustedes) |
| `CLAVE` | Una frase larga al azar (nadie necesita recordarla) | `tortuga-luna-87-arauco-talca-...` |
| `NTFY_CARTAS` | **Tema nuevo** de ntfy donde escribirás las cartas | `rincon-cartas-` + 12 letras al azar |
| `NTFY_AVISOS` | **Tema nuevo** de ntfy donde te llegarán los avisos | `rincon-avisos-` + 12 letras al azar |

Los temas viejos (`dallana-aviso-…` y `dallana-cartas-…`) están a la vista en el historial público del repositorio, así que usa temas nuevos. En la app ntfy, suscríbete a `NTFY_AVISOS` y desuscríbete de los viejos.

## 3. Publicar el servidor

En una terminal, dentro de la carpeta `rincon-servidor`:

```bash
npx wrangler login
```

```bash
npx wrangler kv namespace create RINCON
```

Copia el `id` que muestra este último comando y pégalo en `wrangler.toml`, en vez de `PEGA_AQUI_EL_ID_DEL_KV`. Luego guarda los cuatro secretos (cada comando te pide el valor):

```bash
npx wrangler secret put PIN
```

```bash
npx wrangler secret put CLAVE
```

```bash
npx wrangler secret put NTFY_CARTAS
```

```bash
npx wrangler secret put NTFY_AVISOS
```

Y publica:

```bash
npx wrangler deploy
```

Al terminar te muestra la dirección del servidor, por ejemplo `https://rincon-dallana.tu-usuario.workers.dev`.

## 4. Conectar la página

En `Dallana.js`, en la línea `const URL_RINCON = '';`, pon la dirección (sin `/` al final):

```js
const URL_RINCON = 'https://rincon-dallana.tu-usuario.workers.dev';
```

Sube las versiones (`?v=` en `Dallana.html` y `sw.js`, y `CACHE_NAME`), haz commit y push. La próxima vez que Dallana entre, Alejandro le pedirá la clave una sola vez.

## 5. Cómo escribirle desde ahora

- **Cartas:** publica en tu tema `NTFY_CARTAS`, o responde en `NTFY_AVISOS`, igual que antes.
- **Comandos:** siguen funcionando `/borrar`, `/editar`, `/buzon`, `/alejandro` y `/disfraz`. Además, `/programar AAAA-MM-DD texto` deja una carta lista para ese día.

## Límites del plan gratis

El plan gratis de Cloudflare Workers permite 100.000 peticiones al día y 1.000 escrituras diarias en KV. El servidor solo escribe cuando llega una carta nueva o cuando cambia el progreso de Dallana (como máximo una vez por minuto mientras ella usa la página), así que no se acerca a esos límites.
