const CACHE_NAME = 'djangopwa-v1';

const urlsToCache = [
  '/',
  '/static/site/icons/192x192.png',
  '/static/site/icons/512x512.png',
  '/static/site/css/style.css',
  '/static/site/js/main.js'
];

self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function (cache) {
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener('fetch', function (event) {
  event.respondWith(
    caches.match(event.request).then(function (response) {
      return response || fetch(event.request);
    }).catch(() => {
      return caches.match('/');
    })
  );
});
