# Metriotes Website - Guía para Agentes AI

Metriotes es una plataforma de bienestar y desarrollo personal. Este es el sitio web estático (landing page).

**Responder siempre en español al usuario.**

---

## Stack

Sitio estático puro: HTML + CSS + JS inline en cada página. Sin framework, bundler ni `package.json`.

## Hosting

GitHub Pages con `_config.yml` (Jekyll solo para `include` de `.well-known`). Dominio: `www.metriotes.com`.

---

## Internacionalización

- Atributos `data-i18n="key"` en elementos HTML
- Objeto `translations` con keys `es` y `en` en el `<script>` del documento
- Función `setLanguage(lang)` recorre `[data-i18n]` y asigna `textContent`
- Idioma guardado en `localStorage('preferredLang')`
- Detección automática via `navigator.language` con fallback a `es`

Al agregar texto nuevo, siempre incluir ambas traducciones (ES y EN) en el objeto `translations`.

---

## Tipografía

Google Fonts: **Kalnia** + **Poppins** (consistente con la app Flutter).

---

## Deep Linking

- iOS Universal Links: `apple-app-site-association` en raíz y `.well-known/`
- Android App Links: `.well-known/assetlinks.json`
- JS detecta paths como `/goals/<base62>` e intenta abrir `metriotes://template/${id}`

---

## Páginas

- `index.html`: landing con canvas mesh gradient, secciones de features, footer
- `privacy.html`: política de privacidad (bilingüe con toggle)
- `terms.html`: términos de servicio (bilingüe con toggle)

---

## Estilos

- CSS inline en `<style>` dentro de cada HTML
- Variables CSS en `:root` (para privacy/terms)
- Reset universal, layout flex/grid, media queries en 768px y 1024px
- `@supports not (backdrop-filter)` como fallback

---

## Otros repositorios

- Backend Django: `metriotes_django/`
- App Flutter: `metriotes_flutter/`
