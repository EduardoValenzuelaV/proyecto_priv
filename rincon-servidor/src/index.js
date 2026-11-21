/* Rincón de Dallana · servidor en Cloudflare Workers (gratis)
 *
 * Para qué sirve:
 *  1. Privacidad: los temas de ntfy ya no están en la página pública; solo los conoce este servidor.
 *     Para leer o escribir el buzón, la página necesita la clave (PIN) que solo sabe Dallana.
 *  2. Las cartas no se pierden: cada 15 minutos (y cada vez que ella entra) el servidor copia tus
 *     cartas de ntfy y las guarda para siempre. También puedes programar cartas para un día.
 *  3. Respaldo: guarda el progreso de Dallana (buzón, corazones, récord, etc.) para que no se pierda
 *     si cambia de teléfono o borra los datos del navegador.
 *
 * Secretos (se configuran con `npx wrangler secret put NOMBRE`, nunca en el código):
 *   PIN          la clave que escribe Dallana (por ejemplo, una fecha de ustedes: 1710)
 *   CLAVE        una frase larga y al azar para firmar la sesión
 *   NTFY_CARTAS  tema secreto de ntfy donde tú escribes las cartas
 *   NTFY_AVISOS  tema secreto de ntfy donde te llegan los avisos (y donde también puedes responder)
 * Almacenamiento: KV con el nombre RINCON (ver wrangler.toml).
 *
 * Comandos que puedes escribir en ntfy (además de /borrar, /editar, /buzon, /alejandro y /disfraz, que procesa la página):
 *   /programar 2026-12-17 Tu carta…   la carta aparece en el buzón ese día (hora de Chile)
 */

const TITULOS_DE_LA_PAGINA = ['Actividad en tu pagina', 'Visita en tu pagina', 'Salio de tu pagina', 'Carta leida', 'Mensaje de Dallana 💌', 'Buzon de Dallana'];
const ORIGENES = ['https://eduardovalenzuelav.github.io', 'http://localhost:8765', 'http://127.0.0.1:8765'];
const MAX_CARTAS = 400;
const MAX_PROGRESO = 300 * 1024;

const hoyChile = () => new Date().toLocaleDateString('en-CA', { timeZone: 'America/Santiago' });

function cors(req) {
  const origen = req.headers.get('Origin') || '';
  return {
    'Access-Control-Allow-Origin': ORIGENES.includes(origen) ? origen : ORIGENES[0],
    'Access-Control-Allow-Methods': 'GET, POST, PUT, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Access-Control-Max-Age': '86400',
    'Vary': 'Origin'
  };
}

const json = (req, datos, status = 200) => new Response(JSON.stringify(datos), {
  status, headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', ...cors(req) }
});

async function firmar(env, texto) {
  const k = await crypto.subtle.importKey('raw', new TextEncoder().encode(env.CLAVE), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const firma = await crypto.subtle.sign('HMAC', k, new TextEncoder().encode(texto));
  return btoa(String.fromCharCode(...new Uint8Array(firma))).replace(/[+/=]/g, c => ({ '+': '-', '/': '_', '=': '' }[c]));
}

async function autorizado(req, env) {
  const t = (req.headers.get('Authorization') || '').replace(/^Bearer\s+/i, '');
  return !!t && t === await firmar(env, 'dallana');
}

/* Copia a KV los mensajes nuevos de ntfy (tus cartas y tus respuestas en el tema de avisos) */
async function traerCartas(env) {
  const cartas = JSON.parse(await env.RINCON.get('cartas') || '[]');
  const cursores = JSON.parse(await env.RINCON.get('cursores') || '{}');
  let cambios = false;
  for (const [tema, esDePapa] of [[env.NTFY_CARTAS, () => true], [env.NTFY_AVISOS, m => !TITULOS_DE_LA_PAGINA.includes(m.title || '')]]) {
    if (!tema) continue;
    const r = await fetch(`https://ntfy.sh/${tema}/json?poll=1&since=${cursores[tema] || 'all'}`);
    if (!r.ok) continue;
    for (const linea of (await r.text()).split('\n')) {
      if (!linea.trim()) continue;
      let m; try { m = JSON.parse(linea); } catch { continue; }
      if (m.event !== 'message') continue;
      cursores[tema] = m.id; cambios = true;
      const texto = (m.message || '').trim();
      if (!texto || texto === 'triggered' || !esDePapa(m) || cartas.some(c => c.id === m.id)) continue;
      const carta = { id: m.id, t: (m.time || Date.now() / 1000) * 1000, titulo: m.title || '', texto };
      const prog = texto.match(/^\/programar\s+(\d{4}-\d{2}-\d{2})\s+([\s\S]+)$/i);
      if (prog) { carta.desde = prog[1]; carta.texto = prog[2].trim(); }
      cartas.push(carta);
    }
  }
  if (cambios) {
    cartas.sort((a, b) => a.t - b.t);
    await env.RINCON.put('cartas', JSON.stringify(cartas.slice(-MAX_CARTAS)));
    await env.RINCON.put('cursores', JSON.stringify(cursores));
  }
  return cartas;
}

async function avisar(env, titulo, texto, tags) {
  if (!env.NTFY_AVISOS) return;
  await fetch('https://ntfy.sh/', {
    method: 'POST',
    body: JSON.stringify({ topic: env.NTFY_AVISOS, title: String(titulo || 'Actividad en tu pagina').slice(0, 80), message: String(texto || '').slice(0, 2000), tags: String(tags || 'heart').split(',').slice(0, 4) })
  });
}

export default {
  async fetch(req, env, ctx) {
    if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors(req) });
    const { pathname } = new URL(req.url);

    if (pathname === '/api/entrar' && req.method === 'POST') {
      const { pin } = await req.json().catch(() => ({}));
      if (!env.PIN || String(pin || '').trim() !== String(env.PIN).trim()) {
        await new Promise(r => setTimeout(r, 800));   // frena a quien intente adivinar
        return json(req, { error: 'Esa no es nuestra clave 🙈' }, 401);
      }
      return json(req, { token: await firmar(env, 'dallana') });
    }

    if (!await autorizado(req, env)) return json(req, { error: 'Falta la clave' }, 401);

    if (pathname === '/api/cartas' && req.method === 'GET') {
      const cartas = await traerCartas(env);
      const hoy = hoyChile();
      return json(req, { cartas: cartas.filter(c => !c.desde || c.desde <= hoy) });
    }

    if (pathname === '/api/aviso' && req.method === 'POST') {
      const { titulo, texto, tags } = await req.json().catch(() => ({}));
      ctx.waitUntil(avisar(env, titulo, texto, tags));
      return json(req, { ok: true });
    }

    if (pathname === '/api/progreso') {
      if (req.method === 'GET') return json(req, JSON.parse(await env.RINCON.get('progreso') || '{}'));
      if (req.method === 'PUT') {
        const cuerpo = await req.text();
        if (cuerpo.length > MAX_PROGRESO) return json(req, { error: 'Demasiado grande' }, 413);
        try { JSON.parse(cuerpo); } catch { return json(req, { error: 'JSON inválido' }, 400); }
        await env.RINCON.put('progreso', cuerpo);
        return json(req, { ok: true });
      }
    }

    return json(req, { error: 'No existe' }, 404);
  },

  // cada 15 minutos guarda las cartas nuevas, aunque Dallana no esté conectada
  async scheduled(evento, env, ctx) {
    ctx.waitUntil(traerCartas(env));
  }
};
