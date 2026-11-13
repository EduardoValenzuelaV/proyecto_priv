/* ============================================================
   CONFIGURACIÓN
   ============================================================ */
const URL_BACKEND = 'https://tu-api-en-render.onrender.com';
const FECHA_INICIO = '2026-10-17';
const MENSAJES_PARA_CARTA = 10;
const CARTA_LOCAL = 'Dallana, gracias por cada paseo, cada conversación y cada risa. Me haces muy feliz. Te elegiría una y mil veces. Con todo mi cariño, siempre.';
const API_DISPONIBLE = (
  (URL_BACKEND.startsWith('https://') && !URL_BACKEND.includes('tu-api-en-render')) ||
  URL_BACKEND.startsWith('http://localhost') ||
  URL_BACKEND.startsWith('http://127.0.0.1')
);

/* ============================================================
   CONTENIDO LOCAL
   ============================================================ */
const CONTENIDO_LOCAL = {
  autoestima: [
    {categoria:'Su personalidad',icono:'✿',mensaje:'Tu forma de ser tiene algo que te hace única.'},
    {categoria:'Su personalidad',icono:'♡',mensaje:'No necesitas cambiar tu esencia para ser suficiente.'},
    {categoria:'Su personalidad',icono:'❀',mensaje:'Tu manera de ver el mundo es algo muy bonito.'},
    {categoria:'Su personalidad',icono:'☼',mensaje:'Tienes una forma especial de hacer sentir bien a quienes te rodean.'},
    {categoria:'Su belleza',icono:'✧',mensaje:'Ojalá pudieras verte con los ojos de quienes te admiran.'},
    {categoria:'Su belleza',icono:'❀',mensaje:'No necesitas cumplir ningún estándar para ser hermosa.'},
    {categoria:'Su belleza',icono:'♡',mensaje:'Hay belleza en tu sonrisa, pero también en tu manera de ser.'},
    {categoria:'Su belleza',icono:'✿',mensaje:'Eres mucho más que lo que ves frente al espejo.'},
    {categoria:'Su inteligencia',icono:'✦',mensaje:'Tienes una mente que merece ser valorada.'},
    {categoria:'Su inteligencia',icono:'☼',mensaje:'No saber algo todavía no significa que no seas capaz.'},
    {categoria:'Su inteligencia',icono:'✧',mensaje:'Tu curiosidad y tus ideas también son parte de lo maravillosa que eres.'},
    {categoria:'Su inteligencia',icono:'❀',mensaje:'Nunca minimices lo que puedes lograr.'},
    {categoria:'Su valentía',icono:'♡',mensaje:'Has superado días que quizá nadie conoce.'},
    {categoria:'Su valentía',icono:'✿',mensaje:'Seguir intentándolo también es una forma de valentía.'},
    {categoria:'Su valentía',icono:'☼',mensaje:'Está bien descansar, no tienes que poder con todo.'},
    {categoria:'Su valentía',icono:'✦',mensaje:'No eres menos fuerte por tener días difíciles.'},
    {categoria:'Su valor personal',icono:'❀',mensaje:'No tienes que demostrar nada para merecer cariño.'},
    {categoria:'Su valor personal',icono:'♡',mensaje:'Tu valor no depende de la opinión de otras personas.'},
    {categoria:'Su valor personal',icono:'✧',mensaje:'Mereces cosas bonitas, incluso en tus días más complicados.'},
    {categoria:'Su valor personal',icono:'✿',mensaje:'Eres suficiente, incluso cuando tú misma lo dudas.'}
  ],
  cartas: [
    {titulo:'Ábreme cuando estés triste',mensaje:'No tienes que arreglarlo todo ahora. Si puedes, respira despacio y date permiso para sentir. Este momento difícil no cuenta toda tu historia; también hay días más amables esperándote.'},
    {titulo:'Ábreme cuando no te sientas bonita',mensaje:'No hay una sola forma correcta de ser bonita. Tu cuerpo no tiene que cumplir ninguna medida para merecer respeto y ternura.'},
    {titulo:'Ábreme cuando dudes de ti misma',mensaje:'No necesitas tener todas las respuestas para seguir siendo capaz. Puedes aprender, cambiar de idea y avanzar a tu ritmo.'},
    {titulo:'Ábreme cuando tengas un mal día',mensaje:'Un día pesado no convierte tu vida en una vida pesada. Haz lo que puedas, deja lo demás para después y recuerda que descansar también cuenta como cuidarte.'},
    {titulo:'Ábreme cuando sientas que no puedes más',mensaje:'No tienes que resolver todo de una vez. Busca un paso pequeño, una pausa o a alguien de confianza con quien compartir el peso.'},
    {titulo:'Ábreme cuando estés orgullosa de ti',mensaje:'Detente un momento y reconoce lo que hiciste. No hace falta que sea algo enorme para que importe. Tu esfuerzo merece ser celebrado.'},
    {titulo:'Ábreme cuando necesites recordar cuánto vales',mensaje:'Tu valor no se gana con logros, aprobación ni días perfectos. Estás aquí, siendo tú, y eso basta para merecer cuidado, respeto y cosas buenas.'},
    {titulo:'Ábreme cuando simplemente quieras sonreír',mensaje:'Ojalá encuentres una canción que te guste, algo rico para comer y un ratito sin apuro. No necesitas una razón grande para regalarte un momento bonito.'}
  ],
  frasco: [
    'No tienes que ganarte el descanso.',
    'Tu voz y tus ideas merecen espacio.',
    'Un paso pequeño también es avanzar.',
    'Puedes sentir mucho y seguir siendo capaz.',
    'Hoy mereces tratarte con cariño.',
    'Tu valor no depende de cómo salió el día.',
    'Está bien pedir apoyo cuando lo necesitas.',
    'Ojalá notes una cosa bonita de ti hoy.'
  ],
  museo: [
    {titulo:'Tu vocación',descripcion:'Tu curiosidad por la geología y la dedicación que pones en tu carrera me inspiran.',mensaje:'Mi geóloga favorita.',foto:''},
    {titulo:'Tu sonrisa',descripcion:'Me encanta tu sonrisa; puede hacer más amable hasta un día común.',mensaje:'Una de mis cosas favoritas de ti.',foto:''},
    {titulo:'Tus gustos',descripcion:'Sushi, un helado en Sweet Cream y esos momentos simples que disfrutamos juntos.',mensaje:'Me gusta aprender qué cosas te hacen feliz.',foto:''},
    {titulo:'Nuestros paseos',descripcion:'Caminar contigo por Paicaví siempre es un buen plan.',mensaje:'A tu lado, cualquier camino se vuelve mi favorito.',foto:''}
  ],
  suenos: ['Conocer un lugar nuevo','Ver una película juntos','Salir a caminar sin apuro','Compartir una comida rica','Tomarnos fotografías','Vivir una pequeña aventura']
    .map((titulo,i)=>({id:`sueno-${i+1}`,titulo,descripcion:'',hecho:false}))
};

const moodCopy = {
  'Necesito cariño':'Ojalá puedas recibir el cariño que necesitas, también de ti misma. Si te ayuda, busca a alguien de confianza y dile que te vendría bien compañía.',
  'Estoy triste':'No tienes que justificar tu tristeza. Puedes ir despacio, atender lo básico y dejar que alguien te acompañe si eso te hace bien.',
  'No me siento bonita':'No hay nada que tengas que corregir para merecer ternura. Tu cuerpo merece respeto hoy, tal como es y tal como está.',
  'Dudo de mí misma':'La duda puede aparecer incluso cuando eres capaz. Elige un paso pequeño; no tienes que sentir seguridad completa para intentarlo.',
  'Estoy orgullosa de mí':'Qué lindo que puedas reconocerlo. Guarda este momento: tu esfuerzo y lo que lograste también te pertenecen.',
  'Solo quiero sentirme querida':'Mereces sentirte querida y acompañada. Puedes pedir un abrazo, escribirle a alguien cercano o darte un momento amable.',
  'Necesito motivación':'No tienes que resolverlo entero. Elige el siguiente paso más pequeño y date crédito por empezarlo.'
};
const moodIcons = {'Necesito cariño':'♡','Estoy triste':'☁','No me siento bonita':'❀','Dudo de mí misma':'✧','Estoy orgullosa de mí':'✦','Solo quiero sentirme querida':'♡','Necesito motivación':'☀'};
const moodSteps = {
  'Necesito cariño':'Si te nace, escribe a alguien de confianza: «¿Me acompañas un ratito?»',
  'Estoy triste':'Toma un poco de agua y elige solo una cosa amable para hacer por ti ahora.',
  'No me siento bonita':'Aléjate un momento del espejo y ponte algo cómodo que te haga sentir cuidada.',
  'Dudo de mí misma':'Piensa en algo difícil que ya aprendiste y da solo el siguiente paso pequeño.',
  'Estoy orgullosa de mí':'Anota qué hiciste para llegar aquí; puedes celebrar el esfuerzo, además del resultado.',
  'Solo quiero sentirme querida':'Pide compañía de forma sencilla, aunque sea compartir un mensaje o un rato en silencio.',
  'Necesito motivación':'Pon un temporizador de cinco minutos y empieza por la parte más fácil.'
};

const RESPALDO = [
  'Me encanta tu sonrisa; ilumina cualquier día.',
  'Eres mi persona favorita para contarle todo.',
  'Te elegiría otra vez, y otra vez, y otra vez. ❤️',
  'Caminar contigo convierte cualquier camino en mi favorito.',
  'Admiro tu inteligencia, tu ternura y todo lo que te esfuerzas.',
  'Tu risa es de mis sonidos favoritos.',
  'Gracias por hacer que los días comunes se sientan especiales.',
  'Contigo hasta esperar la micro se vuelve una aventura.',
  'Me gusta lo tranquilo que se siente todo cuando estoy contigo.',
  'Eres una de las casualidades más bonitas de mi vida.',
  'Me encanta cómo empezamos a hablar; es un recuerdo que atesoro.',
  'Gracias por ser tú, tal como eres.',
  'Vale por una invitación a tu sushi favorito. Yo invito.',
  'Vale por un helado juntos y una conversación sin apuro.',
  'Me brillan los días cuando recibo un mensaje tuyo.',
  'Eres increíblemente valiente, incluso cuando no te das cuenta.',
  'Me encanta escucharte hablar de lo que te apasiona.',
  'Vale por una tarde de película y manta; tú eliges.',
  'Mi lugar favorito es a tu lado.',
  'Contigo hasta el silencio se siente cómodo.',
  'Me haces querer ser una mejor versión de mí.',
  'Vale por un abrazo largo, de esos que arreglan el día.',
  'Gracias por cada paseo, cada conversación y cada risa.',
  'Eres la razón por la que reviso el celular con una sonrisa.',
  'Me encanta que a tu lado siempre puedo ser yo.',
  'Ojalá tengamos muchos paseos, helados y recuerdos por delante.',
  'Te quiero un poquito más con cada recuerdo que sumamos.',
  'Gracias por hacerme feliz de tantas formas pequeñas.',
  'Si pudiera repetir un día, elegiría uno de los que pasé contigo.',
  'Este es solo el comienzo de muchas cosas bonitas juntos.'
].map((mensaje,i)=>({id:`offline-${i+1}`,mensaje,foto:''}));

const MELODIAS = [
  {nombre:'Una melodía para ti',notas:[261.63,329.63,392,329.63,293.66,349.23,440,392]},
  {nombre:'Paseo al atardecer',notas:[293.66,369.99,440,392,349.23,293.66,261.63,329.63]},
  {nombre:'Un baile tranquilo',notas:[220,261.63,329.63,293.66,246.94,293.66,349.23,329.63]},
  {nombre:'Un recuerdo bonito',notas:[392,440,392,329.63,349.23,392,293.66,329.63]}
];

const FRASES_DE_ENTRADA = [
  'Un recordatorio amable para hoy: no tienes que hacerlo todo de una vez.',
  'Que hoy encuentres un momento para tratarte con la misma ternura que das.',
  'Tu historia también merece pausas, cambios y comienzos nuevos.',
  'No necesitas sentirte perfecta para merecer un día bonito.',
  'Ojalá hoy puedas reconocer una cosa que te guste de ti.'
];
const FRASES_DE_CIERRE = [
  'Gracias por regalarte este ratito. Ojalá te lleves contigo una palabra amable.',
  'Antes de irte, recuerda: también mereces estar de tu propio lado.',
  'Que lo bonito que encontraste aquí te acompañe un poquito más.'
];

/* ============================================================
   HELPERS
   ============================================================ */
const $ = id => document.getElementById(id);
const leerJSON = (key, fallback) => { try { return JSON.parse(localStorage.getItem(key) || 'null') || fallback; } catch { return fallback; } };
const leerSet = key => { try { return new Set(JSON.parse(localStorage.getItem(key) || '[]').map(String)); } catch { return new Set(); } };
const guardarSet = (key, set) => { try { localStorage.setItem(key, JSON.stringify([...set])); } catch {} };
const escogerIndice = (total, anterior) => { if (total < 2) return 0; let n; do { n = Math.floor(Math.random() * total); } while (n === anterior); return n; };
const vibrar = () => { if (navigator.vibrate) navigator.vibrate([30, 20, 42]); };

/* ============================================================
   ESTADO
   ============================================================ */
let contenido = CONTENIDO_LOCAL;
let currentId = null;
let affirmationIndex = -1;
let lastJarIndex = -1;
let token = '';
let mensajes = [];
let seen = leerSet('dallanaSeen');
let favorites = leerSet('dallanaFavorites');
let cartaTimer = null;
let toquesSecretos = 0;

/* ============================================================
   POLYFILL dialog
   ============================================================ */
if (!HTMLDialogElement.prototype.showModal) {
  HTMLDialogElement.prototype.showModal = function () { this.setAttribute('open', ''); };
  HTMLDialogElement.prototype.close = function () { this.removeAttribute('open'); };
}

/* ============================================================
   CORAZONES FLOTANTES
   ============================================================ */
const heartDrift = $('heartDrift');
if (heartDrift && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const heartColors = ['#d71945', '#2878d0', '#269b68'];
  function lanzarCorazon() {
    const heart = document.createElement('span');
    heart.className = 'drift-heart';
    heart.textContent = '♥';
    heart.style.setProperty('--side', Math.random() < .5 ? `${3 + Math.random() * 10}vw` : `${87 + Math.random() * 10}vw`);
    heart.style.setProperty('--heart-color', heartColors[Math.floor(Math.random() * heartColors.length)]);
    heart.style.setProperty('--heart-size', `${16 + Math.random() * 18}px`);
    heart.style.setProperty('--heart-duration', `${7 + Math.random() * 5}s`);
    heart.style.setProperty('--heart-opacity', `${.42 + Math.random() * .28}`);
    heart.style.setProperty('--heart-drift', `${-24 + Math.random() * 48}px`);
    if (heartDrift.childElementCount >= 18) heartDrift.firstElementChild.remove();
    heartDrift.append(heart);
    heart.addEventListener('animationend', () => heart.remove(), { once: true });
    setTimeout(() => heart.remove(), 13000);
  }
  for (let i = 0; i < 7; i++) setTimeout(lanzarCorazon, i * 650);
  setInterval(lanzarCorazon, 850);
}

/* ============================================================
   FECHA / CONTADOR
   ============================================================ */
function actualizarContador() {
  const [anio, mes, dia] = FECHA_INICIO.split('-').map(Number);
  const ahora = new Date();
  const inicio = Date.UTC(anio, mes - 1, dia);
  const hoy = Date.UTC(ahora.getFullYear(), ahora.getMonth(), ahora.getDate());
  const diferencia = Math.round((hoy - inicio) / 864e5);
  const el = $('counter'); if (!el) return;
  el.textContent = diferencia < 0
    ? `Faltan ${Math.abs(diferencia)} días para comenzar 💕`
    : `${diferencia + 1} ${diferencia === 0 ? 'día' : 'días'} juntos 💕`;
}

/* ============================================================
   PROGRESO Y CELEBRACIÓN
   ============================================================ */
function lanzarCelebracion() {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const container = $('celebrationContainer');
  if (!container) return;
  const simbolos = ['♥', '❀', '✿', '✧', '♡'];
  const colores = ['#d82148', '#e94560', '#f2789f', '#ff9494', '#f6b8b8'];
  for (let i = 0; i < 40; i++) {
    const el = document.createElement('span');
    el.className = 'celebration-petal';
    el.textContent = simbolos[Math.floor(Math.random() * simbolos.length)];
    el.style.left = `${Math.random() * 100}vw`;
    el.style.color = colores[Math.floor(Math.random() * colores.length)];
    el.style.fontSize = `${14 + Math.random() * 22}px`;
    el.style.setProperty('--fall-duration', `${2.8 + Math.random() * 2.4}s`);
    el.style.setProperty('--drift-x', `${-60 + Math.random() * 120}px`);
    el.style.setProperty('--rot', `${-180 + Math.random() * 360}deg`);
    setTimeout(() => {
      container.append(el);
      setTimeout(() => el.remove(), 5500);
    }, i * 75);
  }
}

function actualizarProgreso(abrirSiNuevo = false) {
  const cantidad = Math.min(seen.size, MENSAJES_PARA_CARTA);
  const porcentaje = cantidad / MENSAJES_PARA_CARTA * 100;
  const count = $('progressCount'); if (count) count.textContent = `${cantidad} / ${MENSAJES_PARA_CARTA}`;
  const fill = $('progressFill'); if (fill) fill.style.width = `${porcentaje}%`;
  const boton = $('openLetter');
  if (cantidad >= MENSAJES_PARA_CARTA) {
    const label = $('progressLabel'); if (label) label.textContent = 'Tu carta ya está lista, Dallana';
    if (boton) boton.classList.add('show');
    let desbloqueada = false;
    try { desbloqueada = localStorage.getItem('dallanaLetterUnlocked') === 'true'; } catch {}
    if (abrirSiNuevo && !desbloqueada) {
      try { localStorage.setItem('dallanaLetterUnlocked', 'true'); } catch {}
      lanzarCelebracion();
      cargarCarta();
      const dlg = $('letterDialog'); if (dlg) dlg.showModal();
    }
  } else {
    const label = $('progressLabel'); if (label) label.textContent = 'Descubre recuerdos para abrir tu carta';
    if (boton) boton.classList.remove('show');
  }
}

/* ============================================================
   MEMORIAS
   ============================================================ */
function urlFoto(foto) {
  if (!foto) return '';
  try { return new URL(foto, `${URL_BACKEND}/`).href; } catch { return foto; }
}

function mostrar(d, label = 'Un mensaje para ti') {
  if (!d) return;
  currentId = String(d.id);
  const tag = $('tag'); if (tag) tag.textContent = label;
  const msg = $('message'); if (msg) msg.textContent = d.mensaje || '';
  const image = $('memory');
  const url = urlFoto(d.foto);
  if (image) {
    image.classList.remove('show');
    const note = $('memoryNote'); if (note) note.classList.remove('show');
    image.removeAttribute('src');
    if (url) {
      image.onload = () => { image.classList.add('show'); if (note) note.classList.add('show'); };
      image.onerror = () => { image.classList.remove('show'); if (note) note.classList.remove('show'); };
      image.src = url;
    }
  }
  seen.add(currentId); guardarSet('dallanaSeen', seen);
  const fav = $('favorite');
  if (fav) {
    fav.textContent = favorites.has(currentId) ? '♥' : '♡';
    fav.classList.toggle('favorite', favorites.has(currentId));
  }
  const paper = $('paper');
  if (paper) {
    paper.classList.toggle('surprise', Boolean(d.sorpresa));
    paper.classList.add('new');
    setTimeout(() => paper.classList.remove('new'), 500);
  }
  actualizarProgreso(true);
}

async function pedir(url, label = 'Un mensaje para ti') {
  const foot = $('foot'); if (foot) foot.textContent = 'Buscando un recuerdo bonito…';
  let wakeTimer = null;
  if (API_DISPONIBLE) {
    wakeTimer = setTimeout(() => {
      if (foot) foot.textContent = 'Despertando nuestro rincón en el servidor... 💌';
    }, 1400);
    try {
      const r = await fetch(url);
      clearTimeout(wakeTimer);
      if (!r.ok) throw new Error();
      const data = await r.json();
      mostrar(data, data.tipo || label);
      if (foot) foot.textContent = `${seen.size} recuerdos descubiertos · ${favorites.size} favoritos ♥`;
      return;
    } catch {
      clearTimeout(wakeTimer);
    }
  }
  const opciones = RESPALDO.filter(item => item.id !== currentId);
  const item = opciones[Math.floor(Math.random() * opciones.length)] || RESPALDO[0];
  mostrar(item, label);
  if (foot) foot.textContent = `${seen.size} recuerdos descubiertos · ${favorites.size} favoritos ♥`;
}

/* ============================================================
   RECORDATORIO POSITIVO
   ============================================================ */
function renderAffirmation(frase) {
  const card = $('affirmationCard'); if (!card) return;
  const icon = $('affirmationIcon'); if (icon) icon.textContent = frase.icono || '✿';
  const text = $('affirmationText'); if (text) text.textContent = frase.mensaje || '';
  const cat = $('affirmationCategory'); if (cat) cat.textContent = frase.categoria || '';
  card.classList.remove('is-beauty', 'is-mind', 'is-brave', 'is-worth');
  const c = (frase.categoria || '').toLowerCase();
  if (c.includes('belleza')) card.classList.add('is-beauty');
  else if (c.includes('inteligencia')) card.classList.add('is-mind');
  else if (c.includes('valent')) card.classList.add('is-brave');
  else if (c.includes('valor')) card.classList.add('is-worth');
}

function mostrarRecordatorioPositivo() {
  const frases = [
    ...(contenido.autoestima || []).map((item, i) => ({ id: `autoestima-${i}`, mensaje: item.mensaje || '', categoria: item.categoria || '', icono: item.icono || '✿', tipo: item.categoria || 'Cosas bonitas sobre ti' })),
    ...(contenido.frasco || []).map((m, i) => ({ id: `frasco-${i}`, mensaje: m, categoria: 'Una sorpresa para ti', icono: '✨', tipo: 'Una sorpresa para ti', sorpresa: true }))
  ].filter(f => f.mensaje);
  if (!frases.length) return;
  affirmationIndex = escogerIndice(frases.length, affirmationIndex);
  const frase = frases[affirmationIndex];
  renderAffirmation(frase);
  mostrar({ ...frase, foto: '' }, frase.tipo);
  const foot = $('foot');
  if (foot) foot.textContent = frase.sorpresa ? 'Sacaste una notita sorpresa ♥' : 'Cosas bonitas sobre ti ♥';
}

/* ============================================================
   FRASCO
   ============================================================ */
function sacarNotaDelFrasco() {
  const frases = (contenido.frasco || []).filter(Boolean);
  if (!frases.length) return;
  lastJarIndex = escogerIndice(frases.length, lastJarIndex);
  const note = $('jarNote'); if (!note) return;
  const btn = $('jarButton');
  if (btn) { btn.classList.add('is-drawing'); setTimeout(() => btn.classList.remove('is-drawing'), 850); }
  note.textContent = frases[lastJarIndex];
  note.classList.remove('new'); void note.offsetWidth; note.classList.add('new');
}

/* ============================================================
   CARTAS "ÁBREME CUANDO..."
   ============================================================ */
function abrirCartaDeAnimo(carta) {
  const scene = $('letterScene');
  const dlg = $('openWhenDialog');
  if (!scene || !dlg) return;
  scene.classList.remove('is-opening', 'is-open');
  const t1 = $('openWhenNoteTitle'); if (t1) t1.textContent = carta.titulo || 'Una carta para ti';
  const m = $('openWhenMessage'); if (m) m.textContent = carta.mensaje || 'Aquí tienes unas palabras para este momento.';
  const t2 = $('openWhenDialogTitle'); if (t2) t2.textContent = carta.titulo || 'Una carta para ti';
  dlg.showModal();
  requestAnimationFrame(() => scene.classList.add('is-opening'));
  const delay = matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 620;
  setTimeout(() => { if (dlg.open) scene.classList.add('is-open'); }, delay);
}

function renderCartas() {
  const host = $('letterCards'); if (!host) return;
  host.replaceChildren();
  (contenido.cartas || []).forEach((c, i) => {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'open-card';
    b.textContent = c.titulo || `Carta ${i + 1}`;
    b.setAttribute('aria-haspopup', 'dialog');
    b.onclick = () => abrirCartaDeAnimo(c);
    host.append(b);
  });
}

/* ============================================================
   SUEÑOS
   ============================================================ */
function renderSuenos() {
  const host = $('dreamGrid'); if (!host) return;
  host.replaceChildren();
  const done = leerSet('dallanaDreamsDone');
  const dreams = contenido.suenos || [];
  dreams.forEach((item, i) => {
    const id = String(item.id || `sueno-${i}`);
    const label = document.createElement('label');
    label.className = 'dream-card' + (done.has(id) ? ' done' : '');
    const input = document.createElement('input');
    input.type = 'checkbox'; input.checked = done.has(id);
    input.setAttribute('aria-label', `Marcar como realizada: ${item.titulo || 'actividad'}`);
    input.onchange = () => {
      const next = leerSet('dallanaDreamsDone');
      input.checked ? next.add(id) : next.delete(id);
      guardarSet('dallanaDreamsDone', next);
      renderSuenos();
    };
    const text = document.createElement('span');
    text.textContent = item.titulo || '';
    label.append(input, text);
    if (item.descripcion) { const d = document.createElement('small'); d.textContent = item.descripcion; label.append(d); }
    host.append(label);
  });
  const prog = $('dreamProgress');
  if (prog) {
    const activos = dreams.filter((it, i) => done.has(String(it.id || `sueno-${i}`))).length;
    prog.textContent = `${activos} de ${dreams.length} pequeñas aventuras marcadas como realizadas.`;
  }
}

/* ============================================================
   MUSEO
   ============================================================ */
function renderMuseo() {
  const host = $('museumGrid'); const section = $('museumSection');
  if (!host || !section) return;
  host.replaceChildren();
  const items = (contenido.museo || []).filter(it => it && it.titulo && (it.descripcion || it.mensaje));
  section.hidden = items.length === 0;
  items.forEach((item, i) => {
    const card = document.createElement('article'); card.className = 'museum-card';
    const icon = document.createElement('span'); icon.className = 'museum-icon';
    icon.setAttribute('aria-hidden', 'true'); icon.textContent = ['✿', '♡', '✧', '☼'][i % 4];
    const title = document.createElement('h3'); title.textContent = item.titulo;
    const desc = document.createElement('p'); desc.textContent = item.descripcion || item.mensaje;
    card.append(icon, title, desc);
    if (item.descripcion && item.mensaje) { const s = document.createElement('small'); s.textContent = item.mensaje; card.append(s); }
    host.append(card);
  });
}

/* ============================================================
   MOODS
   ============================================================ */
function limpiarAnimo() {
  document.querySelectorAll('.mood-options button').forEach(b => {
    b.setAttribute('aria-pressed', 'false'); b.classList.remove('selected');
  });
  const resp = $('moodResponse'); if (!resp) return;
  resp.replaceChildren();
  const p = document.createElement('p'); p.className = 'mood-prompt';
  p.textContent = 'Elige lo que necesitas ahora. No tienes que explicarlo ni resolverlo todo.';
  resp.append(p);
}

function renderMoods() {
  const host = $('moodOptions'); if (!host) return;
  host.replaceChildren();
  Object.keys(moodCopy).forEach(label => {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'mood-option';
    b.setAttribute('aria-pressed', 'false'); b.setAttribute('aria-label', label);
    b.textContent = `${moodIcons[label] || '♡'} ${label}`;
    b.onclick = () => {
      host.querySelectorAll('button').forEach(o => {
        o.setAttribute('aria-pressed', String(o === b));
        o.classList.toggle('selected', o === b);
      });
      const resp = $('moodResponse'); if (!resp) return;
      resp.replaceChildren();
      const k = document.createElement('span'); k.className = 'mood-response-kicker'; k.textContent = 'PARA ESTE MOMENTO';
      const h = document.createElement('h3'); h.textContent = label;
      const m = document.createElement('p'); m.className = 'mood-message'; m.textContent = moodCopy[label];
      const s = document.createElement('p'); s.className = 'mood-next-step';
      const strong = document.createElement('strong'); strong.textContent = 'Si te sirve: ';
      s.append(strong, document.createTextNode(moodSteps[label] || 'Puedes ir a tu ritmo.'));
      const reset = document.createElement('button');
      reset.type = 'button'; reset.className = 'mood-reset'; reset.textContent = 'Elegir otra opción';
      reset.onclick = limpiarAnimo;
      resp.append(k, h, m, s, reset);
    };
    host.append(b);
  });
  limpiarAnimo();
}

/* ============================================================
   RENDER GLOBAL
   ============================================================ */
function renderContenido() { renderCartas(); renderSuenos(); renderMuseo(); renderMoods(); }

/* ============================================================
   CARTA FINAL
   ============================================================ */
function animarCarta(texto) {
  const destino = $('letterText'); if (!destino) return;
  if (cartaTimer) clearInterval(cartaTimer);
  destino.replaceChildren();
  destino.setAttribute('aria-label', texto);
  const visual = document.createElement('span');
  visual.setAttribute('aria-hidden', 'true');
  destino.append(visual);
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) { visual.textContent = texto; return; }
  const letras = Array.from(texto);
  let indice = 0;
  cartaTimer = setInterval(() => {
    visual.textContent += letras[indice++] || '';
    if (indice >= letras.length) { clearInterval(cartaTimer); cartaTimer = null; }
  }, 18);
}

async function cargarCarta() {
  animarCarta(CARTA_LOCAL);
  if (API_DISPONIBLE) {
    try {
      const r = await fetch(`${URL_BACKEND}/api/carta`);
      if (r.ok) {
        const d = await r.json();
        animarCarta(d.carta || CARTA_LOCAL);
      }
    } catch {}
  }
}

/* ============================================================
   ENVELOPE / RANDOM / DAILY / FAVORITE
   ============================================================ */
const openEnvelopeBtn = $('openEnvelope');
if (openEnvelopeBtn) openEnvelopeBtn.onclick = () => {
  const cover = $('welcome');
  const env = $('env');
  if (cover && cover.classList.contains('opening')) return;
  if (cover) cover.classList.add('opening');
  if (env) env.classList.add('open');
  const delay = matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 780;
  setTimeout(() => {
    if (cover) { cover.classList.add('closed'); cover.classList.remove('opening'); }
    pedir(`${URL_BACKEND}/api/momento`, 'Un mensaje para ti');
  }, delay);
};

const randomBtn = $('random');
if (randomBtn) randomBtn.onclick = () => {
  vibrar();
  const q = currentId ? `?ultimo=${encodeURIComponent(currentId)}` : '';
  pedir(`${URL_BACKEND}/api/cumplido${q}`);
};

const dailyBtn = $('daily');
if (dailyBtn) dailyBtn.onclick = () => {
  vibrar();
  if (API_DISPONIBLE) { pedir(`${URL_BACKEND}/api/del-dia`, 'Tu mensaje de hoy'); return; }
  const ahora = new Date();
  const n = Math.floor(Date.UTC(ahora.getFullYear(), ahora.getMonth(), ahora.getDate()) / 864e5);
  const item = RESPALDO[((n % RESPALDO.length) + RESPALDO.length) % RESPALDO.length];
  mostrar(item, 'Tu mensaje de hoy');
  const foot = $('foot');
  if (foot) foot.textContent = `${seen.size} recuerdos descubiertos · ${favorites.size} favoritos ♥`;
};

const favBtn = $('favorite');
if (favBtn) favBtn.onclick = () => {
  if (!currentId) return;
  favorites.has(currentId) ? favorites.delete(currentId) : favorites.add(currentId);
  guardarSet('dallanaFavorites', favorites);
  favBtn.textContent = favorites.has(currentId) ? '♥' : '♡';
  favBtn.classList.toggle('favorite', favorites.has(currentId));
  actualizarBotonFavoritos();
  const foot = $('foot');
  if (foot) foot.textContent = favorites.has(currentId) ? 'Guardado entre tus favoritos ♥' : 'Quitado de tus favoritos';
};

/* ============================================================
   FAVORITOS
   ============================================================ */
function actualizarBotonFavoritos() {
  const count = $('favCount');
  if (count) count.textContent = String(favorites.size);
}

function encontrarMensajePorId(id) {
  let item = mensajes.find(m => String(m.id) === String(id));
  if (item) return item;
  item = RESPALDO.find(m => String(m.id) === String(id));
  if (item) return item;
  const auto = (contenido.autoestima || []).map((it, i) => ({ id: `autoestima-${i}`, mensaje: it.mensaje }));
  item = auto.find(m => String(m.id) === String(id));
  if (item) return item;
  const fr = (contenido.frasco || []).map((m, i) => ({ id: `frasco-${i}`, mensaje: m }));
  item = fr.find(m => String(m.id) === String(id));
  return item || { id, mensaje: 'Un recuerdo guardado con amor ♥' };
}

function renderFavoritos() {
  const host = $('favoritesList');
  if (!host) return;
  host.replaceChildren();
  if (favorites.size === 0) {
    const p = document.createElement('p');
    p.className = 'favorite-empty';
    p.textContent = 'Aún no has guardado recuerdos favoritos. Toca el corazón ♡ en cualquier recuerdo para guardarlo aquí.';
    host.append(p);
    return;
  }
  favorites.forEach(id => {
    const item = encontrarMensajePorId(id);
    const card = document.createElement('article');
    card.className = 'favorite-item';
    const text = document.createElement('p');
    text.textContent = item.mensaje || '';
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'icon-btn';
    btn.textContent = '✕';
    btn.title = 'Quitar de favoritos';
    btn.setAttribute('aria-label', 'Quitar de favoritos');
    btn.onclick = (e) => {
      e.stopPropagation();
      favorites.delete(String(id));
      guardarSet('dallanaFavorites', favorites);
      actualizarBotonFavoritos();
      const fav = $('favorite');
      if (fav && currentId === String(id)) {
        fav.textContent = '♡';
        fav.classList.remove('favorite');
      }
      renderFavoritos();
    };
    card.onclick = () => {
      mostrar(item, 'Un recuerdo favorito');
      const dlg = $('favoritesDialog');
      if (dlg) dlg.close();
      const paper = $('paper');
      if (paper) paper.scrollIntoView({ behavior: 'smooth', block: 'center' });
    };
    card.style.cursor = 'pointer';
    card.append(text, btn);
    host.append(card);
  });
}

const viewFavoritesBtn = $('viewFavorites');
if (viewFavoritesBtn) viewFavoritesBtn.onclick = () => {
  renderFavoritos();
  const dlg = $('favoritesDialog');
  if (dlg) dlg.showModal();
};

const openLetterBtn = $('openLetter');
if (openLetterBtn) openLetterBtn.onclick = () => {
  lanzarCelebracion();
  cargarCarta();
  const dlg = $('letterDialog'); if (dlg) dlg.showModal();
};

const positiveBtn = $('positiveNote');
if (positiveBtn) positiveBtn.onclick = mostrarRecordatorioPositivo;

const jarBtn = $('jarButton');
if (jarBtn) jarBtn.onclick = sacarNotaDelFrasco;

const resetBtn = $('resetProgress');
if (resetBtn) resetBtn.onclick = () => {
  if (!confirm('¿Quieres reiniciar tu progreso en este rincón?')) return;
  ['dallanaSeen', 'dallanaFavorites', 'dallanaDreamsDone', 'dallanaLetterUnlocked'].forEach(k => { try { localStorage.removeItem(k); } catch {} });
  seen = new Set(); favorites = new Set();
  actualizarBotonFavoritos();
  actualizarProgreso(false);
  location.reload();
};

document.querySelectorAll('[data-close]').forEach(b => b.onclick = () => {
  const el = $(b.dataset.close); if (el) el.close();
});

const openWhenDlg = $('openWhenDialog');
if (openWhenDlg) openWhenDlg.addEventListener('close', () => {
  const scene = $('letterScene'); if (scene) scene.classList.remove('is-opening', 'is-open');
});

const letterDlg = $('letterDialog');
if (letterDlg) letterDlg.addEventListener('close', () => {
  if (cartaTimer) { clearInterval(cartaTimer); cartaTimer = null; }
});

/* ============================================================
   MÚSICA (Cajita de música delicada)
   ============================================================ */
let audioContext, masterGain, melodyTimer, melodyStep = 0, melodyIndex = 0;

function tocarNota() {
  if (!audioContext || !masterGain) return;
  const notas = MELODIAS[melodyIndex].notas;
  const freq = notas[melodyStep++ % notas.length];
  const now = audioContext.currentTime;

  // 1. Tono principal fundamental
  const osc1 = audioContext.createOscillator();
  const gain1 = audioContext.createGain();
  osc1.type = 'sine';
  osc1.frequency.setValueAtTime(freq, now);
  gain1.gain.setValueAtTime(0.0001, now);
  gain1.gain.exponentialRampToValueAtTime(0.048, now + 0.015);
  gain1.gain.exponentialRampToValueAtTime(0.018, now + 0.22);
  gain1.gain.exponentialRampToValueAtTime(0.0001, now + 0.82);
  osc1.connect(gain1);
  gain1.connect(masterGain);
  osc1.start(now);
  osc1.stop(now + 0.85);

  // 2. Armónico metálico sutil (brillo de cajita de música)
  const osc2 = audioContext.createOscillator();
  const gain2 = audioContext.createGain();
  osc2.type = 'triangle';
  osc2.frequency.setValueAtTime(freq * 3, now);
  gain2.gain.setValueAtTime(0.0001, now);
  gain2.gain.exponentialRampToValueAtTime(0.011, now + 0.008);
  gain2.gain.exponentialRampToValueAtTime(0.0001, now + 0.24);
  osc2.connect(gain2);
  gain2.connect(masterGain);
  osc2.start(now);
  osc2.stop(now + 0.26);
}

function seleccionarMelodia(indice) {
  melodyIndex = (indice + MELODIAS.length) % MELODIAS.length;
  melodyStep = 0;
  const h = document.querySelector('.track-heading h2'); if (h) h.textContent = MELODIAS[melodyIndex].nombre;
  const p = document.querySelector('.track-heading p'); if (p) p.textContent = `Melodía ${melodyIndex + 1} de ${MELODIAS.length}`;
  if (melodyTimer) { clearInterval(melodyTimer); tocarNota(); melodyTimer = setInterval(tocarNota, 700); }
}

const musicPrev = $('musicPrev');
if (musicPrev) musicPrev.onclick = () => seleccionarMelodia(melodyIndex - 1);

const musicNext = $('musicNext');
if (musicNext) musicNext.onclick = () => seleccionarMelodia(melodyIndex + 1);

const musicVolume = $('musicVolume');
if (musicVolume) musicVolume.oninput = () => {
  const valor = Number(musicVolume.value);
  const out = $('musicVolumeValue'); if (out) out.value = `${Math.round(valor * 100)}%`;
  if (masterGain && audioContext) masterGain.gain.setTargetAtTime(valor, audioContext.currentTime, .04);
};

const musicPlay = $('musicPlay');
if (musicPlay) musicPlay.onclick = async () => {
  if (melodyTimer) {
    clearInterval(melodyTimer); melodyTimer = null;
    musicPlay.textContent = '▶';
    musicPlay.setAttribute('aria-label', 'Reproducir música');
    musicPlay.setAttribute('aria-pressed', 'false');
    const hint = $('musicHint'); if (hint) hint.textContent = 'Melodía en pausa';
    return;
  }
  const AudioContextClass = window.AudioContext || window.webkitAudioContext;
  if (!AudioContextClass) {
    const hint = $('musicHint'); if (hint) hint.textContent = 'Tu navegador no admite estas melodías.';
    return;
  }
  audioContext ??= new AudioContextClass();
  if (!masterGain) {
    masterGain = audioContext.createGain();
    masterGain.gain.value = Number(musicVolume ? musicVolume.value : 0.35);
    masterGain.connect(audioContext.destination);
  }
  await audioContext.resume();
  tocarNota();
  melodyTimer = setInterval(tocarNota, 700);
  musicPlay.textContent = 'Ⅱ';
  musicPlay.setAttribute('aria-label', 'Pausar música');
  musicPlay.setAttribute('aria-pressed', 'true');
  const hint = $('musicHint'); if (hint) hint.textContent = `Reproduciendo: ${MELODIAS[melodyIndex].nombre}`;
};

/* ============================================================
   CORAZÓN SECRETO
   ============================================================ */
const secretHeart = $('secretHeart');
if (secretHeart) secretHeart.onclick = () => {
  toquesSecretos++;
  if (toquesSecretos >= 5) {
    const sm = $('secretMessage'); if (sm) sm.hidden = false;
    const aa = $('albumArt'); if (aa) aa.classList.add('secret-found');
    const hint = $('musicHint'); if (hint) hint.textContent = 'Encontraste un detalle escondido.';
    toquesSecretos = 0;
  }
};

/* ============================================================
   ADMIN
   ============================================================ */
function estadoAdmin(texto, error = false) {
  const el = $('adminStatus'); if (!el) return;
  el.textContent = texto;
  el.classList.toggle('error', error);
}

async function adminFetch(path, options = {}) {
  if (!API_DISPONIBLE) throw new Error('El panel privado necesita que primero conectes y despliegues la API en Render.');
  const headers = { 'X-Admin-Token': token, ...options.headers };
  if (!(options.body instanceof FormData)) headers['Content-Type'] = 'application/json';
  return fetch(`${URL_BACKEND}${path}`, { ...options, headers });
}

function seleccionarMensaje() {
  const id = $('editSelect')?.value;
  const item = mensajes.find(m => String(m.id) === id);
  if (!item) return;
  $('editMessage').value = item.mensaje;
  $('editPhoto').value = item.foto || '';
  $('editPhotoFile').value = '';
}

function renderMensajes() {
  const select = $('editSelect'); if (!select) return;
  select.replaceChildren();
  mensajes.forEach((m, i) => {
    const option = document.createElement('option');
    option.value = String(m.id);
    option.textContent = `${i + 1}. ${m.mensaje.slice(0, 68)}`;
    select.append(option);
  });
  if (mensajes.length) seleccionarMensaje();
}

function previewContenido() {
  try {
    const data = {
      autoestima: JSON.parse($('adminAffirmations').value),
      cartas: JSON.parse($('adminCards').value),
      frasco: JSON.parse($('adminJar').value),
      museo: JSON.parse($('adminMuseum').value),
      suenos: JSON.parse($('adminDreams').value)
    };
    if (!Object.values(data).every(Array.isArray)) throw new Error();
    const prev = $('contentPreview');
    if (prev) prev.textContent = `${data.autoestima.length} recordatorios · ${data.cartas.length} cartas · ${data.frasco.length} sorpresas · ${data.museo.length} vitrinas · ${data.suenos.length} actividades`;
    return data;
  } catch {
    const prev = $('contentPreview');
    if (prev) prev.textContent = 'Revisa el JSON de cada colección antes de guardar.';
    return null;
  }
}

async function entradaAdmin() {
  token = $('adminToken').value;
  try {
    const r = await adminFetch('/api/administracion');
    if (!r.ok) throw new Error((await r.json()).detail || 'No pude validar la clave');
    const d = await r.json();
    mensajes = d.cumplidos;
    $('adminLetter').value = d.carta;
    $('greetingMorning').value = d.saludos.manana;
    $('greetingNight').value = d.saludos.noche;
    const c = d.contenido || contenido;
    const setVal = (id, v) => { const el = $(id); if (el) el.value = v; };
    setVal('adminAffirmations', JSON.stringify(c.autoestima, null, 2));
    setVal('adminCards', JSON.stringify(c.cartas, null, 2));
    setVal('adminJar', JSON.stringify(c.frasco, null, 2));
    setVal('adminMuseum', JSON.stringify(c.museo, null, 2));
    setVal('adminDreams', JSON.stringify(c.suenos, null, 2));
    previewContenido();
    $('adminTools').classList.remove('hidden');
    renderMensajes();
    estadoAdmin(`Panel listo · ${mensajes.length} recuerdos guardados.`);
  } catch (e) { estadoAdmin(e.message, true); }
}

async function subirFoto(fileInput, destination) {
  const file = fileInput.files?.[0];
  if (!file) return;
  try {
    const body = new FormData();
    body.append('foto', file);
    const r = await adminFetch('/api/administracion/fotos', { method: 'POST', body });
    if (!r.ok) throw new Error((await r.json()).detail || 'No pude subir la imagen');
    const d = await r.json();
    $(destination).value = `${URL_BACKEND}${d.foto}`;
    estadoAdmin('Foto subida. Guarda el recuerdo para aplicar el cambio.');
  } catch (e) { estadoAdmin(e.message, true); }
}

const loadAdmin = $('loadAdmin');
if (loadAdmin) loadAdmin.onclick = entradaAdmin;

const editSelect = $('editSelect');
if (editSelect) editSelect.onchange = seleccionarMensaje;

['adminAffirmations', 'adminCards', 'adminJar', 'adminMuseum', 'adminDreams'].forEach(id => {
  const el = $(id); if (el) el.oninput = previewContenido;
});

const adminOpenBtn = $('adminOpen');
if (adminOpenBtn) adminOpenBtn.onclick = () => {
  const dlg = $('adminDialog'); if (!dlg) return;
  dlg.showModal();
  const t = $('adminToken'); if (t) t.value = token;
};

const newPhotoFile = $('newPhotoFile');
if (newPhotoFile) newPhotoFile.onchange = () => subirFoto(newPhotoFile, 'newPhoto');

const editPhotoFile = $('editPhotoFile');
if (editPhotoFile) editPhotoFile.onchange = () => subirFoto(editPhotoFile, 'editPhoto');

const saveEdit = $('saveEdit');
if (saveEdit) saveEdit.onclick = async () => {
  const id = $('editSelect')?.value;
  if (!id) return;
  try {
    const r = await adminFetch(`/api/administracion/cumplidos/${encodeURIComponent(id)}`, {
      method: 'PUT', body: JSON.stringify({ mensaje: $('editMessage').value.trim(), foto: $('editPhoto').value.trim() })
    });
    if (!r.ok) throw new Error((await r.json()).detail || 'No pude guardar el recuerdo');
    const actualizado = await r.json();
    mensajes = mensajes.map(m => String(m.id) === String(actualizado.id) ? actualizado : m);
    renderMensajes(); estadoAdmin('Recuerdo actualizado.');
  } catch (e) { estadoAdmin(e.message, true); }
};

const deleteMessage = $('deleteMessage');
if (deleteMessage) deleteMessage.onclick = async () => {
  const id = $('editSelect')?.value;
  if (!id) return;
  try {
    const r = await adminFetch(`/api/administracion/cumplidos/${encodeURIComponent(id)}`, { method: 'DELETE' });
    if (!r.ok) throw new Error((await r.json()).detail || 'No pude eliminar el recuerdo');
    mensajes = mensajes.filter(m => String(m.id) !== String(id));
    renderMensajes(); estadoAdmin('Recuerdo eliminado.');
  } catch (e) { estadoAdmin(e.message, true); }
};

const addMessage = $('addMessage');
if (addMessage) addMessage.onclick = async () => {
  const mensaje = $('newMessage').value.trim();
  if (!mensaje) return estadoAdmin('Escribe un mensaje antes de guardarlo.', true);
  try {
    const r = await adminFetch('/api/administracion/cumplidos', {
      method: 'POST', body: JSON.stringify({ mensaje, foto: $('newPhoto').value.trim() })
    });
    if (!r.ok) throw new Error((await r.json()).detail || 'No pude añadir el recuerdo');
    $('newMessage').value = ''; $('newPhoto').value = ''; $('newPhotoFile').value = '';
    await entradaAdmin(); estadoAdmin('Nuevo recuerdo añadido.');
  } catch (e) { estadoAdmin(e.message, true); }
};

const saveLetter = $('saveLetter');
if (saveLetter) saveLetter.onclick = async () => {
  try {
    const r = await adminFetch('/api/administracion/carta', { method: 'PUT', body: JSON.stringify({ carta: $('adminLetter').value }) });
    if (!r.ok) throw new Error((await r.json()).detail || 'No pude guardar la carta');
    estadoAdmin('Carta guardada.');
  } catch (e) { estadoAdmin(e.message, true); }
};

const saveGreetings = $('saveGreetings');
if (saveGreetings) saveGreetings.onclick = async () => {
  try {
    const r = await adminFetch('/api/administracion/saludos', {
      method: 'PUT', body: JSON.stringify({ manana: $('greetingMorning').value, noche: $('greetingNight').value })
    });
    if (!r.ok) throw new Error((await r.json()).detail || 'No pude guardar los saludos');
    estadoAdmin('Saludos guardados.');
  } catch (e) { estadoAdmin(e.message, true); }
};

const saveContent = $('saveContent');
if (saveContent) saveContent.onclick = async () => {
  const data = previewContenido();
  if (!data) return estadoAdmin('Revisa el JSON antes de guardar.', true);
  try {
    const r = await adminFetch('/api/administracion/contenido', { method: 'PUT', body: JSON.stringify(data) });
    if (!r.ok) throw new Error((await r.json()).detail || 'No pude guardar el contenido');
    contenido = data; estadoAdmin('Contenido guardado.');
  } catch (e) { estadoAdmin(e.message, true); }
};

/* ============================================================
   INICIALIZACIÓN
   ============================================================ */
actualizarContador();
actualizarProgreso(false);
actualizarBotonFavoritos();
renderContenido();
setInterval(actualizarContador, 60000);

if ('serviceWorker' in navigator && (location.protocol === 'https:' || location.hostname === 'localhost' || location.hostname === '127.0.0.1')) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./sw.js').catch(() => {});
  });
}

