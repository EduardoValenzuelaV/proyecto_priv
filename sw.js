const CACHE_NAME = 'dallana-v4.14';
// Solo lo básico para abrir sin internet. Lo demás (fotos, GIF de recuerdos, stickers) se guarda
// en la caché cuando ella lo ve, así cada actualización no vuelve a bajar varios MB por adelantado.
const ASSETS_TO_CACHE = [
  './',
  './Dallana.html',
  './Dallana.css?v=10.5',
  './Dallana.js?v=3.93',
  './manifest.json',
  './assets/icons/icon-192.png',
  './assets/pixel/alejandro.png?v=5',
  './assets/pixel/buzon.png?v=1',
  './assets/pixel/adornos.png?v=1',
  './assets/pixel/postal-manana.png?v=1',
  './assets/pixel/postal-tarde.png?v=1',
  './assets/pixel/postal-noche.png?v=1',
  './assets/pixel/dragones.png?v=3',
  './assets/pixel/disfraces/cartero.png?v=2',
  './assets/fotos/portada-polaroid.jpg?v=2',
  './assets/fotos/portada-tira.jpg?v=1'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS_TO_CACHE))
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key)))
    ).then(() => self.clients.claim())
  );
});

// Red primero: así cada publicación se ve al instante; la caché solo cubre el modo sin conexión.
self.addEventListener('fetch', event => {
  const { request } = event;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);
  const mismoOrigen = url.origin === self.location.origin;
  // lo que va a otros sitios (ntfy, el servidor del rincón) no pasa por aquí: va directo a la red
  if (!mismoOrigen) return;
  // La música va directo a la red (y al caché normal del navegador): así funcionan las peticiones
  // por partes (Range) que usa el iPhone para reproducir y adelantar, y no se descargan 33 MB de una vez.
  if (request.headers.has('range') || url.pathname.includes('/assets/musica/')) return;
  event.respondWith(
    fetch(request).then(response => {
      if (mismoOrigen && response.ok && !url.pathname.includes('/api/')) {
        const copia = response.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(request, copia));
      }
      return response;
    }).catch(() =>
      caches.match(request).then(cached => cached || (request.mode === 'navigate' ? caches.match('./Dallana.html') : Response.error()))
    )
  );
});
