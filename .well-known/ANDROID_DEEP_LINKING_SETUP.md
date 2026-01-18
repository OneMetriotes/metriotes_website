# Configuración de Deep Linking para Android

## Instrucciones para completar assetlinks.json

El archivo `assetlinks.json` necesita los SHA-256 fingerprints de tus keystores.

### 1. Obtener SHA-256 del keystore de DEBUG

```bash
keytool -list -v -keystore ~/.android/debug.keystore -alias androiddebugkey -storepass android -keypass android | grep "SHA256"
```

El output será algo como:
```
SHA256: AA:BB:CC:DD:EE:FF:00:11:22:33:44:55:66:77:88:99:AA:BB:CC:DD:EE:FF:00:11:22:33:44:55:66:77:88:99
```

### 2. Obtener SHA-256 del keystore de RELEASE

Si tienes un keystore de release (producción), usa:

```bash
keytool -list -v -keystore /path/to/your/release.keystore -alias your-alias | grep "SHA256"
```

**Nota importante**: Actualmente tu `build.gradle` usa el keystore de debug también para release. Necesitarás:
- Crear un keystore de producción real para la Play Store
- Actualizar `android/app/build.gradle` con la configuración de signing de release

### 3. Actualizar assetlinks.json

Reemplaza los placeholders en `assetlinks.json` con los fingerprints obtenidos (sin los dos puntos):

```json
[
  {
    "relation": ["delegate_permission/common.handle_all_urls"],
    "target": {
      "namespace": "android_app",
      "package_name": "com.metriotes.metriotes_front",
      "sha256_cert_fingerprints": [
        "AA:BB:CC:DD:EE:FF:00:11:22:33:44:55:66:77:88:99:AA:BB:CC:DD:EE:FF:00:11:22:33:44:55:66:77:88:99",
        "11:22:33:44:55:66:77:88:99:AA:BB:CC:DD:EE:FF:00:11:22:33:44:55:66:77:88:99:AA:BB:CC:DD:EE:FF"
      ]
    }
  }
]
```

### 4. Subir y verificar

1. Sube el archivo a tu servidor web
2. Verifica que sea accesible en: `https://metriotes.com/.well-known/assetlinks.json`
3. Verifica el archivo en: https://developers.google.com/digital-asset-links/tools/generator
4. En el dispositivo Android, ejecuta:
   ```bash
   adb shell pm verify-app-links --re-verify com.metriotes.metriotes_front
   ```

### 5. Configurar keystore de producción (recomendado)

Para producción, debes crear un keystore seguro:

```bash
keytool -genkey -v -keystore ~/metriotes-release.keystore -alias metriotes -keyalg RSA -keysize 2048 -validity 10000
```

Luego actualiza `android/app/build.gradle`:

```gradle
android {
    signingConfigs {
        release {
            storeFile file("path/to/metriotes-release.keystore")
            storePassword System.getenv("KEYSTORE_PASSWORD")
            keyAlias "metriotes"
            keyPassword System.getenv("KEY_PASSWORD")
        }
    }
    
    buildTypes {
        release {
            signingConfig signingConfigs.release
        }
    }
}
```

## Testing

Después de configurar todo:

1. Compila y instala la app en un dispositivo Android
2. Envía un link de template (ej: `https://metriotes.com/goals/15`)
3. Al tocar el link, Android debería preguntar si quieres abrir con Metriotes
4. La app debería abrirse directamente en la pantalla del template
