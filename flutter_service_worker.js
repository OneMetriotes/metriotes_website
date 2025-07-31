'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';

const RESOURCES = {"flutter_bootstrap.js": "40e8914b557de773ab658f47d62c0af7",
"version.json": "60c15629866419db489698dc2784dc04",
"index.html": "f48b4bf2ab1746287a2cec8469b56b6d",
"/": "f48b4bf2ab1746287a2cec8469b56b6d",
"metriotes_icon.png": "a36a978c29fa7d862e5b9d901842f843",
"main.dart.js": "b6c76535fdfdb15700b09435e334eea0",
"flutter.js": "83d881c1dbb6d6bcd6b42e274605b69c",
"favicon.png": "5dcef449791fa27946b3d35ad8803796",
"icons/metriotes_icon.png": "aa7f4d23fc9d1a9eda1eb41a719f2320",
"icons/Icon-192.png": "ac9a721a12bbc803b44f645561ecb1e1",
"icons/Icon-maskable-192.png": "c457ef57daa1d16f64b27b786ec2ea3c",
"icons/Icon-maskable-512.png": "301a7604d45b3e739efc881eb04896ea",
"icons/Icon-512.png": "96e752610906ba2a93c65f8abe1645f1",
"manifest.json": "2220b9101ea81b1ea328a2eb5c3e01d9",
"assets/AssetManifest.json": "8ce27ab053888b68c8f24ce080da8eb5",
"assets/NOTICES": "b838260b0d97a68cd82a2e3083336660",
"assets/FontManifest.json": "a29ce8d2e45014327f2588c5d7e72a23",
"assets/AssetManifest.bin.json": "0bfa465ad43917e728710436adac506e",
"assets/icons/keni.jpg": "b63d1d833f3ddcbabc9b3e57ead03f55",
"assets/icons/learnings.gif": "207d37183d0a8332bc3bdc8e7bcfe2f5",
"assets/icons/8.jpg": "4df77fff7e1cd332c356cfe939212a7a",
"assets/icons/who_.gif": "ec4a37b364d3f62d0fa500e7da66944e",
"assets/icons/north.png": "1ef779ecd44c7a22be2deaaf7759e9c2",
"assets/icons/home_background.png": "7c74f0ad57762581e2f01a938a8ac516",
"assets/icons/9.jpg": "c1e0bf34fcfc31590618f6bace061bfb",
"assets/icons/contexts-base.png": "0f156e461f503e64dc89d03d348a9339",
"assets/icons/12.jpg": "2deb06b3f4ab331ad65b1a7cd5ab9932",
"assets/icons/howscreen.png": "dc574f525e9ec72983bf9838ab1511f4",
"assets/icons/11.jpg": "ded5f16c13ab0cb9f6694154bb73abb1",
"assets/icons/insecurities.gif": "7ee4aff46ae141f15c34e4d747e9803d",
"assets/icons/10.jpg": "efcc073e8aea8accd898f7a2f5b7f624",
"assets/icons/beliefs.gif": "4aaade9c445949aeb401a28deff935f1",
"assets/icons/logo.png": "a36a978c29fa7d862e5b9d901842f843",
"assets/icons/keni_loading.gif": "b17497217d465b9795404320e409b580",
"assets/icons/4.jpg": "c2588a99fd68d906c5703c1175c2fb62",
"assets/icons/Norte.png": "c39a26fdacf7f04c74311a6ca561ea9a",
"assets/icons/5.jpg": "e79407fac51dba37fe05925efb7b832d",
"assets/icons/7.jpg": "85bdcd61a052791010bdf60b9272ecce",
"assets/icons/light_background.png": "9baec236eefffdff58ac726460f6696c",
"assets/icons/6.jpg": "ffd1b47598c7f0bbe7fc23030ae1ae33",
"assets/icons/2.jpg": "7044e04bb4393f9d9933cc60a3d1e9a8",
"assets/icons/contexts-base-light.png": "572016f70dc6f1428a44c0fbd02e59e6",
"assets/icons/1.jpg": "6965e9f48ef216d1beb4ad4099135f32",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "d5b09f035d2358c205a365df9be31bdc",
"assets/packages/simple_circular_progress_bar/fonts/Roboto-Regular.ttf": "8a36205bd9b83e03af0591a004bc97f4",
"assets/shaders/ink_sparkle.frag": "ecc85a2e95f5e9f53123dcaf8cb9b6ce",
"assets/AssetManifest.bin": "4426a98a321bdd954120e707c5b08fc3",
"assets/fonts/MaterialIcons-Regular.otf": "b5e5e0d7f827fd7a7a639e24d681c860",
"canvaskit/skwasm.js": "ea559890a088fe28b4ddf70e17e60052",
"canvaskit/skwasm.js.symbols": "e72c79950c8a8483d826a7f0560573a1",
"canvaskit/canvaskit.js.symbols": "bdcd3835edf8586b6d6edfce8749fb77",
"canvaskit/skwasm.wasm": "39dd80367a4e71582d234948adc521c0",
"canvaskit/chromium/canvaskit.js.symbols": "b61b5f4673c9698029fa0a746a9ad581",
"canvaskit/chromium/canvaskit.js": "8191e843020c832c9cf8852a4b909d4c",
"canvaskit/chromium/canvaskit.wasm": "f504de372e31c8031018a9ec0a9ef5f0",
"canvaskit/canvaskit.js": "728b2d477d9b8c14593d4f9b82b484f3",
"canvaskit/canvaskit.wasm": "7a3f4ae7d65fc1de6a6e7ddd3224bc93"};
// The application shell files that are downloaded before a service worker can
// start.
const CORE = ["main.dart.js",
"index.html",
"flutter_bootstrap.js",
"assets/AssetManifest.bin.json",
"assets/FontManifest.json"];

// During install, the TEMP cache is populated with the application shell files.
self.addEventListener("install", (event) => {
  self.skipWaiting();
  return event.waitUntil(
    caches.open(TEMP).then((cache) => {
      return cache.addAll(
        CORE.map((value) => new Request(value, {'cache': 'reload'})));
    })
  );
});
// During activate, the cache is populated with the temp files downloaded in
// install. If this service worker is upgrading from one with a saved
// MANIFEST, then use this to retain unchanged resource files.
self.addEventListener("activate", function(event) {
  return event.waitUntil(async function() {
    try {
      var contentCache = await caches.open(CACHE_NAME);
      var tempCache = await caches.open(TEMP);
      var manifestCache = await caches.open(MANIFEST);
      var manifest = await manifestCache.match('manifest');
      // When there is no prior manifest, clear the entire cache.
      if (!manifest) {
        await caches.delete(CACHE_NAME);
        contentCache = await caches.open(CACHE_NAME);
        for (var request of await tempCache.keys()) {
          var response = await tempCache.match(request);
          await contentCache.put(request, response);
        }
        await caches.delete(TEMP);
        // Save the manifest to make future upgrades efficient.
        await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
        // Claim client to enable caching on first launch
        self.clients.claim();
        return;
      }
      var oldManifest = await manifest.json();
      var origin = self.location.origin;
      for (var request of await contentCache.keys()) {
        var key = request.url.substring(origin.length + 1);
        if (key == "") {
          key = "/";
        }
        // If a resource from the old manifest is not in the new cache, or if
        // the MD5 sum has changed, delete it. Otherwise the resource is left
        // in the cache and can be reused by the new service worker.
        if (!RESOURCES[key] || RESOURCES[key] != oldManifest[key]) {
          await contentCache.delete(request);
        }
      }
      // Populate the cache with the app shell TEMP files, potentially overwriting
      // cache files preserved above.
      for (var request of await tempCache.keys()) {
        var response = await tempCache.match(request);
        await contentCache.put(request, response);
      }
      await caches.delete(TEMP);
      // Save the manifest to make future upgrades efficient.
      await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
      // Claim client to enable caching on first launch
      self.clients.claim();
      return;
    } catch (err) {
      // On an unhandled exception the state of the cache cannot be guaranteed.
      console.error('Failed to upgrade service worker: ' + err);
      await caches.delete(CACHE_NAME);
      await caches.delete(TEMP);
      await caches.delete(MANIFEST);
    }
  }());
});
// The fetch handler redirects requests for RESOURCE files to the service
// worker cache.
self.addEventListener("fetch", (event) => {
  if (event.request.method !== 'GET') {
    return;
  }
  var origin = self.location.origin;
  var key = event.request.url.substring(origin.length + 1);
  // Redirect URLs to the index.html
  if (key.indexOf('?v=') != -1) {
    key = key.split('?v=')[0];
  }
  if (event.request.url == origin || event.request.url.startsWith(origin + '/#') || key == '') {
    key = '/';
  }
  // If the URL is not the RESOURCE list then return to signal that the
  // browser should take over.
  if (!RESOURCES[key]) {
    return;
  }
  // If the URL is the index.html, perform an online-first request.
  if (key == '/') {
    return onlineFirst(event);
  }
  event.respondWith(caches.open(CACHE_NAME)
    .then((cache) =>  {
      return cache.match(event.request).then((response) => {
        // Either respond with the cached resource, or perform a fetch and
        // lazily populate the cache only if the resource was successfully fetched.
        return response || fetch(event.request).then((response) => {
          if (response && Boolean(response.ok)) {
            cache.put(event.request, response.clone());
          }
          return response;
        });
      })
    })
  );
});
self.addEventListener('message', (event) => {
  // SkipWaiting can be used to immediately activate a waiting service worker.
  // This will also require a page refresh triggered by the main worker.
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
    return;
  }
  if (event.data === 'downloadOffline') {
    downloadOffline();
    return;
  }
});
// Download offline will check the RESOURCES for all files not in the cache
// and populate them.
async function downloadOffline() {
  var resources = [];
  var contentCache = await caches.open(CACHE_NAME);
  var currentContent = {};
  for (var request of await contentCache.keys()) {
    var key = request.url.substring(origin.length + 1);
    if (key == "") {
      key = "/";
    }
    currentContent[key] = true;
  }
  for (var resourceKey of Object.keys(RESOURCES)) {
    if (!currentContent[resourceKey]) {
      resources.push(resourceKey);
    }
  }
  return contentCache.addAll(resources);
}
// Attempt to download the resource online before falling back to
// the offline cache.
function onlineFirst(event) {
  return event.respondWith(
    fetch(event.request).then((response) => {
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request, response.clone());
        return response;
      });
    }).catch((error) => {
      return caches.open(CACHE_NAME).then((cache) => {
        return cache.match(event.request).then((response) => {
          if (response != null) {
            return response;
          }
          throw error;
        });
      });
    })
  );
}
