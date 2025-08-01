self.addEventListener('install', function(e) {
    console.log('Service Worker: Installed');
});

self.addEventListener('activate', function(e) {
    console.log('Service Worker: Activated');
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        fetch(event.request).catch(function() {
            return new Response("Offline Page");
        })
    );
});
