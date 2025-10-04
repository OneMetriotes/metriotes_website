'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';

const RESOURCES = {"flutter_bootstrap.js": "210a5ad2937fcbf1662f5d2aaba434e4",
"version.json": "60c15629866419db489698dc2784dc04",
"index.html": "e7b4145dd4b981d0c361ebf0586848f9",
"/": "e7b4145dd4b981d0c361ebf0586848f9",
"main.dart.js": "82dc2fd25fce296ddaeb05d06ce90eb3",
"Metriotes.png": "05624a56a01aebd78326a51c821fe1da",
"sqlite3.wasm": "33e37e7fcae44dfab4ec6d071f4e301b",
"flutter.js": "888483df48293866f9f41d3d9274a779",
"favicon.png": "5dcef449791fa27946b3d35ad8803796",
"sqflite_sw.js": "442fd04c0d5907b1f7487cba60f4c9ce",
"icons/metriotes_icon.png": "aa7f4d23fc9d1a9eda1eb41a719f2320",
"icons/Icon-192.png": "ac9a721a12bbc803b44f645561ecb1e1",
"icons/Icon-maskable-192.png": "c457ef57daa1d16f64b27b786ec2ea3c",
"icons/Icon-maskable-512.png": "301a7604d45b3e739efc881eb04896ea",
"icons/Icon-512.png": "96e752610906ba2a93c65f8abe1645f1",
"manifest.json": "2220b9101ea81b1ea328a2eb5c3e01d9",
"assets/AssetManifest.json": "7ec939b01ad815fbfdfd20276c541ca4",
"assets/NOTICES": "3a0101fb8dafce21f472ad112e82f73c",
"assets/FontManifest.json": "b405ab34fbd41344c1f995702528b7d2",
"assets/AssetManifest.bin.json": "5400b446be79bf0f8b14e52d1cf56dcc",
"assets/icons/revelations.png": "494a07bd4e63cd6e8d8633ec526c5691",
"assets/icons/trayecto.png": "156416982302fc357382374adf0572d7",
"assets/icons/habits_back.png": "4cceb1d46c9c23924e077c7bf7f44070",
"assets/icons/keni.jpg": "b63d1d833f3ddcbabc9b3e57ead03f55",
"assets/icons/8.jpg": "4df77fff7e1cd332c356cfe939212a7a",
"assets/icons/goals.png": "9499612e1bea131cf50b217bfaf57127",
"assets/icons/north.png": "1ef779ecd44c7a22be2deaaf7759e9c2",
"assets/icons/9.jpg": "c1e0bf34fcfc31590618f6bace061bfb",
"assets/icons/Metriotes.png": "05624a56a01aebd78326a51c821fe1da",
"assets/icons/12.jpg": "2deb06b3f4ab331ad65b1a7cd5ab9932",
"assets/icons/howscreen.png": "dc574f525e9ec72983bf9838ab1511f4",
"assets/icons/11.jpg": "ded5f16c13ab0cb9f6694154bb73abb1",
"assets/icons/10.jpg": "efcc073e8aea8accd898f7a2f5b7f624",
"assets/icons/northlogo.png": "4f69cef38023420cd6a6adf6c4c6accb",
"assets/icons/achievement.png": "c59473af0454e250aa56e7c5753263d9",
"assets/icons/star.svg": "5625d9ff9937f66cd6db92451949761d",
"assets/icons/keni_loading.gif": "b17497217d465b9795404320e409b580",
"assets/icons/profile.png": "bcc674f391785751235114d4e975197c",
"assets/icons/4.jpg": "c2588a99fd68d906c5703c1175c2fb62",
"assets/icons/happening.png": "7154ca1bfe6ec23f61e3ebdd49981bc1",
"assets/icons/problem.png": "b2b9cbc74c72da6437a1f7f400f4ac1c",
"assets/icons/Metriotes_logo.png": "1f2fc133be81316d34d6ee0ae48ed8c7",
"assets/icons/5.jpg": "e79407fac51dba37fe05925efb7b832d",
"assets/icons/7.jpg": "85bdcd61a052791010bdf60b9272ecce",
"assets/icons/light_background.png": "9baec236eefffdff58ac726460f6696c",
"assets/icons/6.jpg": "ffd1b47598c7f0bbe7fc23030ae1ae33",
"assets/icons/2.jpg": "7044e04bb4393f9d9933cc60a3d1e9a8",
"assets/icons/north_back.png": "54ecf01880a7b17f39e5cad19dfafdc9",
"assets/icons/1.jpg": "6965e9f48ef216d1beb4ad4099135f32",
"assets/icons/gratefull.png": "8f5181ca66d39412f2a0b323e5c5601d",
"assets/icons/inspiracion.png": "6bfe4ab3458051061cd54712a5f34f24",
"assets/icons/emotions.png": "9986fe4bf8cd8c3f67243f29bc233949",
"assets/packages/mesh/shaders/omesh.frag": "242b80a0ff93acfab4745ef36f76f6f2",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "33b7d9392238c04c131b6ce224e13711",
"assets/packages/simple_circular_progress_bar/fonts/Roboto-Regular.ttf": "8a36205bd9b83e03af0591a004bc97f4",
"assets/shaders/ink_sparkle.frag": "ecc85a2e95f5e9f53123dcaf8cb9b6ce",
"assets/AssetManifest.bin": "6845da734e7006b3cf65d9749df0c2e1",
"assets/fonts/MaterialIcons-Regular.otf": "68a17af61365e1b8f098f1b2f9d979ee",
"canvaskit/skwasm.js": "1ef3ea3a0fec4569e5d531da25f34095",
"canvaskit/skwasm_heavy.js": "413f5b2b2d9345f37de148e2544f584f",
"canvaskit/skwasm.js.symbols": "0088242d10d7e7d6d2649d1fe1bda7c1",
"canvaskit/canvaskit.js.symbols": "58832fbed59e00d2190aa295c4d70360",
"canvaskit/skwasm_heavy.js.symbols": "3c01ec03b5de6d62c34e17014d1decd3",
"canvaskit/skwasm.wasm": "264db41426307cfc7fa44b95a7772109",
"canvaskit/chromium/canvaskit.js.symbols": "193deaca1a1424049326d4a91ad1d88d",
"canvaskit/chromium/canvaskit.js": "5e27aae346eee469027c80af0751d53d",
"canvaskit/chromium/canvaskit.wasm": "24c77e750a7fa6d474198905249ff506",
"canvaskit/canvaskit.js": "140ccb7d34d0a55065fbd422b843add6",
"canvaskit/canvaskit.wasm": "07b9f5853202304d3b0749d9306573cc",
"canvaskit/skwasm_heavy.wasm": "8034ad26ba2485dab2fd49bdd786837b"};
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
