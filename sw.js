const CACHE_NAME = 'dallana-v3.22';
const ASSETS_TO_CACHE = [
  './',
  './Dallana.html',
  './Dallana.css?v=4.6',
  './Dallana.js?v=3.19',
  './manifest.json',
  './assets/fotos/portada-musica.png',
  './assets/musica/Taylor%20Swift%20-%20Love%20Story.mp3',
  './assets/musica/The%20Weeknd%2C%20Ariana%20Grande%20-%20Die%20For%20You%20(Remix%20Lyric%20Video).mp3',
  './assets/musica/The%20Weeknd%20%26%20Ariana%20Grande%20-%20Save%20Your%20Tears%20(Remix)%20(Official%20Video).mp3',
  './assets/musica/Swedish%20House%20Mafia%20and%20The%20Weeknd%20-%20Moth%20To%20A%20Flame%20(Official%20Video).mp3',
  './assets/musica/Billie%20Eilish%20-%20CHIHIRO%20(Official%20Music%20Video).mp3',
  './assets/musica/Nessa%20Barrett%20-%20die%20first%20(official%20music%20video).mp3',
  './assets/musica/Billie%20Eilish%20-%20BIRDS%20OF%20A%20FEATHER%20(Official%20Music%20Video).mp3',
  './assets/musica/The%20Verve%20-%20Bitter%20Sweet%20Symphony.mp3',
  './assets/fotos/migeo.jpg',
  './assets/stickers/stikers3.png',
  './assets/icons/icon-192.png',
  './assets/icons/icon-512.png'
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
