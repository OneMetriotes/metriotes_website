# Metriotes Website

Landing page y configuración de deep linking para Metriotes.

## 📁 Estructura

```
metriotes_website/
├── index.html                      # Landing page bilingüe (ES/EN)
├── apple-app-site-association      # Configuración Universal Links (iOS)
├── .well-known/
│   └── assetlinks.json            # Configuración App Links (Android)
└── README.md
```

## 🔗 Configuración de Deep Linking

### iOS - Universal Links

1. **Obtener tu Team ID de Apple Developer:**
   - Ve a [developer.apple.com](https://developer.apple.com/account)
   - Tu Team ID está en la esquina superior derecha
   - Ejemplo: `ABCDE12345`

2. **Editar `apple-app-site-association`:**
   ```json
   {
     "applinks": {
       "apps": [],
       "details": [
         {
           "appID": "TU_TEAM_ID.com.metriotes.metriotesFront",
           "paths": ["/template/*"]
         }
       ]
     }
   }
   ```
   Reemplaza `YOUR_TEAM_ID` con tu Team ID real.

3. **Subir el archivo:**
   - Debe estar en la raíz: `https://metriotes.com/apple-app-site-association`
   - **Sin extensión de archivo**
   - Content-Type: `application/json`
   - Debe ser accesible sin autenticación

4. **Verificar configuración:**
   ```bash
   curl -I https://metriotes.com/apple-app-site-association
   ```
   Debe devolver `Content-Type: application/json`

### Android - App Links

1. **Obtener el SHA-256 de tu certificado de firma:**
   
   Para debug (desarrollo):
   ```bash
   keytool -list -v -keystore ~/.android/debug.keystore -alias androiddebugkey -storepass android -keypass android
   ```
   
   Para release (producción):
   ```bash
   keytool -list -v -keystore tu-keystore.jks -alias tu-alias
   ```
   
   Busca la línea `SHA256:` y copia el valor (con dos puntos, ejemplo: `AA:BB:CC:...`).

2. **Editar `.well-known/assetlinks.json`:**
   ```json
   [
     {
       "relation": ["delegate_permission/common.handle_all_urls"],
       "target": {
         "namespace": "android_app",
         "package_name": "com.metriotes.Metriotes",
         "sha256_cert_fingerprints": [
           "TU_SHA256_AQUI"
         ]
       }
     }
   ]
   ```
   Reemplaza `YOUR_SHA256_FINGERPRINT_HERE` con tu SHA-256 real.

3. **Subir el archivo:**
   - Debe estar en: `https://metriotes.com/.well-known/assetlinks.json`
   - Content-Type: `application/json`

4. **Verificar configuración:**
   ```bash
   curl https://metriotes.com/.well-known/assetlinks.json
   ```

### Configuración del servidor web

Asegúrate de que tu servidor sirva estos archivos con el Content-Type correcto:

**Nginx:**
```nginx
location /apple-app-site-association {
    default_type application/json;
    add_header Access-Control-Allow-Origin *;
}

location /.well-known/assetlinks.json {
    default_type application/json;
    add_header Access-Control-Allow-Origin *;
}
```

**Apache (.htaccess):**
```apache
<Files "apple-app-site-association">
    Header set Content-Type "application/json"
    Header set Access-Control-Allow-Origin "*"
</Files>

<Files "assetlinks.json">
    Header set Content-Type "application/json"
    Header set Access-Control-Allow-Origin "*"
</Files>
```

## 🌐 Landing Page

La landing page (`index.html`) incluye:

- ✅ Diseño responsive y mobile-first
- ✅ Soporte bilingüe (Español/Inglés)
- ✅ Detección automática del idioma del navegador
- ✅ Botones para App Store y Google Play (con badge "Próximamente")
- ✅ Secciones de características
- ✅ Manejo de deep links a templates

### Actualizar enlaces de descarga

Cuando publiques la app, actualiza los enlaces en `index.html`:

```html
<!-- Reemplaza href="#" con los enlaces reales -->
<a href="https://apps.apple.com/app/metriotes/idXXXXXXXX" class="store-btn">
    <!-- App Store -->
</a>

<a href="https://play.google.com/store/apps/details?id=com.metriotes.Metriotes" class="store-btn">
    <!-- Google Play -->
</a>

<!-- Y elimina la clase "disabled" y el badge "coming-soon" -->
```

## 🧪 Probar Deep Links

### En desarrollo (Simulador iOS):

```bash
xcrun simctl openurl booted "metriotes://template/3"
```

### En desarrollo (Emulador Android):

```bash
adb shell am start -W -a android.intent.action.VIEW -d "metriotes://template/3" com.metriotes.Metriotes
```

### Con URLs HTTPS (después de publicar):

```bash
# iOS
xcrun simctl openurl booted "https://metriotes.com/template/3"

# Android
adb shell am start -W -a android.intent.action.VIEW -d "https://metriotes.com/template/3"
```

## 📝 Notas Importantes

1. **iOS Universal Links** solo funcionan después de instalar la app desde el App Store o TestFlight. No funcionan con builds locales.

2. **Android App Links** requieren que el dominio y el SHA-256 coincidan exactamente.

3. Los archivos de configuración deben ser accesibles públicamente (sin autenticación).

4. Los cambios en los archivos de configuración pueden tardar hasta 24 horas en propagarse.

5. Para probar en desarrollo, usa el custom URL scheme: `metriotes://template/ID`

## 🚀 Deployment

1. Sube todos los archivos a tu servidor web
2. Verifica que los archivos de configuración sean accesibles
3. Prueba los deep links en dispositivos reales
4. Publica la app en las tiendas
5. Actualiza los enlaces de descarga en `index.html`

## 🔍 Herramientas de Debug

**iOS:**
- [Apple App Site Association Validator](https://branch.io/resources/aasa-validator/)
- Console.app (para ver logs de Universal Links)

**Android:**
- [Digital Asset Links Tester](https://developers.google.com/digital-asset-links/tools/generator)
- `adb logcat` (para ver logs de App Links)

## 📧 Soporte

Para más información sobre deep linking:
- [Apple Universal Links](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app)
- [Android App Links](https://developer.android.com/training/app-links)
