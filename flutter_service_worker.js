'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';

const RESOURCES = {"flutter_bootstrap.js": "4aecee8b658291fa011cfbd0a92c86e6",
"version.json": "d43848f52b57d138e7dcf7ea7985d253",
"index.html": "6b9d1fd4961b6c2792de346833835652",
"/": "6b9d1fd4961b6c2792de346833835652",
"metriotes_icon.png": "aa7f4d23fc9d1a9eda1eb41a719f2320",
"main.dart.js": "5c30ad4ddcbfb26ebfa7694cbc1a70b1",
"flutter.js": "83d881c1dbb6d6bcd6b42e274605b69c",
"favicon.png": "5dcef449791fa27946b3d35ad8803796",
"icons/metriotes_icon.png": "aa7f4d23fc9d1a9eda1eb41a719f2320",
"icons/Icon-192.png": "ac9a721a12bbc803b44f645561ecb1e1",
"icons/Icon-maskable-192.png": "c457ef57daa1d16f64b27b786ec2ea3c",
"icons/Icon-maskable-512.png": "301a7604d45b3e739efc881eb04896ea",
"icons/Icon-512.png": "96e752610906ba2a93c65f8abe1645f1",
"manifest.json": "772f3ccae7dbd4ebfed3b2bcd37e4e51",
"assets/AssetManifest.json": "33b61cb3bb2e191552953a12fc420c02",
"assets/NOTICES": "e57b9528187690ae560b195a21a60087",
"assets/FontManifest.json": "c5d980f2ce04dec19b6903f7e594bcc5",
"assets/AssetManifest.bin.json": "6d665647e3c3a7e1fe8c1d77338add73",
"assets/icons/keni.jpg": "b63d1d833f3ddcbabc9b3e57ead03f55",
"assets/icons/learnings.gif": "207d37183d0a8332bc3bdc8e7bcfe2f5",
"assets/icons/8.jpg": "b81439e65e688752044548ece825a3f5",
"assets/icons/who_.gif": "ec4a37b364d3f62d0fa500e7da66944e",
"assets/icons/9.jpg": "9e8aa43799fa7b9dfce6039a9956f19f",
"assets/icons/14.jpg": "7c23b7bb4c392d46339ba1ad352a1448",
"assets/icons/who_back.gif": "d957cfba3104cb4bbdae343717f4f00d",
"assets/icons/15.jpg": "6dd9ab382d3ac05ee38b7d2276841c46",
"assets/icons/how.gif": "6116a8c3e74d1295f19a8307d611774e",
"assets/icons/contexts-base.png": "0f156e461f503e64dc89d03d348a9339",
"assets/icons/12.jpg": "2deb06b3f4ab331ad65b1a7cd5ab9932",
"assets/icons/13.jpg": "e667cf49355e72f2a81455dab65732df",
"assets/icons/11.jpg": "156ea3306ad3c744eaf2eff7c82ebee0",
"assets/icons/insecurities.gif": "7ee4aff46ae141f15c34e4d747e9803d",
"assets/icons/10.jpg": "173d515974bdc89e77898fd75a129d70",
"assets/icons/beliefs.gif": "4aaade9c445949aeb401a28deff935f1",
"assets/icons/fears.gif": "2a94aed3bb4695d5b736a6aa894b8b81",
"assets/icons/keni_loading.gif": "b17497217d465b9795404320e409b580",
"assets/icons/4.jpg": "6d669e392f3f540ce9d0e088ed0e58a8",
"assets/icons/5.jpg": "47b945c7ded4545fc7c42a6802181066",
"assets/icons/7.jpg": "85bdcd61a052791010bdf60b9272ecce",
"assets/icons/who_background.gif": "4af5f8a15c333bcf4ece12e451c30157",
"assets/icons/how_back.gif": "c430a0bbcd60cdaed146adb1ae653a4d",
"assets/icons/6.jpg": "62132878e67a45bfd210b59dc2ca1220",
"assets/icons/2.jpg": "569c5269ff00d7c3be9c86538db7e503",
"assets/icons/desires.gif": "3a6127fcd097c99c2fdadd0505e2fb74",
"assets/icons/contexts-base-light.png": "572016f70dc6f1428a44c0fbd02e59e6",
"assets/icons/why.gif": "896baa5c2fccc02c33545ad9eb970f85",
"assets/icons/3.jpg": "4bab722235d6a2a5f4a08b4571ec91d6",
"assets/icons/1.jpg": "25b4dc8790a0d7306b7a3d51fb0774c2",
"assets/icons/gratitudes.gif": "cc7b76ff4ed79b6c371b71c6c3032f8d",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "eedc71142b3c8b0e2302adc3583bfa49",
"assets/packages/simple_circular_progress_bar/fonts/Roboto-Regular.ttf": "8a36205bd9b83e03af0591a004bc97f4",
"assets/shaders/ink_sparkle.frag": "ecc85a2e95f5e9f53123dcaf8cb9b6ce",
"assets/AssetManifest.bin": "ca3c5fb40d6889830f847a65596c9026",
"assets/fonts/NunitoSans-LightItalic.ttf": "bc3489f6859f9f64e3891908b0a0d46c",
"assets/fonts/NunitoSans-BoldItalic.ttf": "0c17d21db93136847a02b79a9c5acc0d",
"assets/fonts/NunitoSans-ExtraLight.ttf": "58713e07b7ee41bdbdaa72703be0c6c6",
"assets/fonts/NunitoSans-Light.ttf": "3b696c5e8c55321863bfbf03ef0c0ff3",
"assets/fonts/Poppins-ExtraLight.ttf": "6f8391bbdaeaa540388796c858dfd8ca",
"assets/fonts/Poppins-ThinItalic.ttf": "01555d25092b213d2ea3a982123722c9",
"assets/fonts/Poppins-ExtraLightItalic.ttf": "a9bed017984a258097841902b696a7a6",
"assets/fonts/Poppins-BoldItalic.ttf": "19406f767addf00d2ea82cdc9ab104ce",
"assets/fonts/Poppins-Light.ttf": "fcc40ae9a542d001971e53eaed948410",
"assets/fonts/Poppins-Medium.ttf": "bf59c687bc6d3a70204d3944082c5cc0",
"assets/fonts/NunitoSans-BlackItalic.ttf": "c5ef9713df6633c8dd9e42c1a45495de",
"assets/fonts/Poppins-SemiBoldItalic.ttf": "9841f3d906521f7479a5ba70612aa8c8",
"assets/fonts/BodoniModa-Italic-VariableFont_opsz,wght.ttf": "baf1951ce7449c744482ecd5d17b022d",
"assets/fonts/BodoniModa-VariableFont_opsz,wght.ttf": "cef9125c763a35e9ad7585e316a1e286",
"assets/fonts/NunitoSans-ExtraBold.ttf": "1d86790a12f81cc60ab837c979bab63d",
"assets/fonts/Poppins-ExtraBoldItalic.ttf": "8afe4dc13b83b66fec0ea671419954cc",
"assets/fonts/NunitoSans-Regular.ttf": "4dac705158fb1ca226d583b3829f82a0",
"assets/fonts/Poppins-ExtraBold.ttf": "d45bdbc2d4a98c1ecb17821a1dbbd3a4",
"assets/fonts/NunitoSans-SemiBoldItalic.ttf": "b8fb6d82716bef6558b16867a6fa5702",
"assets/fonts/NunitoSans-Italic.ttf": "ceeddfb0cea317042f4c796b72dfd6bf",
"assets/fonts/RozhaOne-Regular.ttf": "b5000551d30dc03efbc274fd6941f45b",
"assets/fonts/Poppins-BlackItalic.ttf": "e9c5c588e39d0765d30bcd6594734102",
"assets/fonts/Poppins-Regular.ttf": "093ee89be9ede30383f39a899c485a82",
"assets/fonts/NunitoSans-Bold.ttf": "ac72fe0f27dd514aa3215e8424842062",
"assets/fonts/Poppins-LightItalic.ttf": "0613c488cf7911af70db821bdd05dfc4",
"assets/fonts/NunitoSans-SemiBold.ttf": "2836528ad13278d88bcc509dc3f8102b",
"assets/fonts/NunitoSans-Black.ttf": "1f8f5740309e62a563b8a5c9d59ece3b",
"assets/fonts/NunitoSans-ExtraBoldItalic.ttf": "fd9f725108ba8d058032c48218522a41",
"assets/fonts/MaterialIcons-Regular.otf": "8bd357cbb3b33567251aa97a05f02f35",
"assets/fonts/Poppins-Bold.ttf": "08c20a487911694291bd8c5de41315ad",
"assets/fonts/NunitoSans-ExtraLightItalic.ttf": "93f8af033d60621442f90c61507d86ad",
"assets/fonts/Poppins-Black.ttf": "14d00dab1f6802e787183ecab5cce85e",
"assets/fonts/Zeyada-Regular.ttf": "ba6dd1f5d34075339dba06c690388c93",
"assets/fonts/Poppins-Thin.ttf": "9ec263601ee3fcd71763941207c9ad0d",
"assets/fonts/Poppins-SemiBold.ttf": "6f1520d107205975713ba09df778f93f",
"assets/fonts/Poppins-Italic.ttf": "c1034239929f4651cc17d09ed3a28c69",
"assets/fonts/Poppins-MediumItalic.ttf": "cf5ba39d9ac24652e25df8c291121506",
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
