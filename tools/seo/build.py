#!/usr/bin/env python3
"""Generador de páginas SEO estáticas de metriotes.com.

Qué genera (todo HTML estático, indexable, con datos estructurados):
  /blog/                         índice + un artículo por archivo de tools/seo/articles/*.md
  /profesionales/                hub del directorio
  /profesionales/<categoria>/    una página por oficio (pilates, yoga, idiomas...)
  /profesionales/<cat>/<ciudad>/ sólo donde hay profesionales reales (nada de páginas vacías)
  /perfil/<slug>/                ficha pública de cada profesional visible
  /eventos/<slug>/               eventos y clases públicos
  /sitemap.xml  /robots.txt  /llms.txt

Los datos de profesionales y eventos salen de la API pública (sin credenciales).
Sólo se publican perfiles con `is_visible=True` (el backend ya filtra). Nunca se
publican email, teléfono ni WhatsApp: el contacto pasa por la app.

Uso:
    python3 tools/seo/build.py            # con datos en vivo
    python3 tools/seo/build.py --offline  # sólo artículos y categorías
"""
import argparse
import html
import json
import re
import shutil
import sys
import unicodedata
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from categories import CATEGORIES, by_slug  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SITE = "https://metriotes.com"
API = "https://metriotes-22732fa1f31f.herokuapp.com"
APP_STORE = "https://apple.co/3LX7yom"
PLAY_STORE = "https://play.google.com/store/apps/details?id=com.metriotes.metriotes_front"
TODAY = date.today().isoformat()

# Directorios que este script regenera por completo en cada corrida.
GENERATED_DIRS = ["blog", "profesionales", "perfil", "eventos"]

# Alias en inglés para que las profesiones en `en` también caigan en su página.
EXTRA_MATCH = {
    "meditacion-mindfulness": ["meditation"],
    "idiomas": ["language teacher"],
    "psicologos": ["psycholog", "therapist", "counsel"],
    "coaching": ["career coach", "life coach"],
    "nutricion": ["nutrition", "dietitian"],
    "entrenadores": ["trainer", "fitness"],
    "fisioterapia": ["physio", "osteopath", "chiropract"],
    "musica-arte-danza": ["music", "dance", "chess"],
}

COUNTRIES = {
    "ES": "España", "AR": "Argentina", "MX": "México", "CO": "Colombia", "CL": "Chile",
    "PE": "Perú", "UY": "Uruguay", "IT": "Italia", "US": "Estados Unidos", "FR": "Francia",
    "PT": "Portugal", "BR": "Brasil", "DE": "Alemania", "GB": "Reino Unido",
}
MONTHS = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
          "septiembre", "octubre", "noviembre", "diciembre"]
WEEKDAYS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábados", "domingos"]
WEEKDAYS_PL = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábados", "Domingos"]

esc = html.escape


# ─── utilidades ──────────────────────────────────────────────────────────────
def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def slugify(s):
    s = re.sub(r"['’`]", "", norm(s))
    s = re.sub(r"^(lic|dr|dra|lcdo|lcda)\.?\s+", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "x"


_B62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
_OFFSET = 10 * (62 ** 5)


def share_hash(n):
    """Port de core.utils.base62.encode_share_hash (links /app/professional/<hash>)."""
    n += _OFFSET
    out = []
    while n:
        n, r = divmod(n, 62)
        out.append(_B62[r])
    return "".join(reversed(out))


def fetch(path):
    try:
        req = urllib.request.Request(API + path, headers={"Accept": "application/json", "User-Agent": "metriotes-seo-build"})
        with urllib.request.urlopen(req, timeout=40) as r:
            return json.load(r)
    except Exception as e:  # noqa: BLE001
        print(f"  ! no se pudo leer {path}: {e}", file=sys.stderr)
        return None


def fmt_date(iso):
    d = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return f"{d.day} de {MONTHS[d.month - 1]} de {d.year}", d


def short(text, n=155):
    t = re.sub(r"\s+", " ", text or "").strip()
    if len(t) <= n:
        return t
    return t[: n - 1].rsplit(" ", 1)[0].rstrip(",.;:") + "…"


def with_brand(t):
    """Agrega " | Metriotes" sólo si el título sigue entrando en ~65 caracteres."""
    t = t.replace(" | Metriotes", "")
    return t + " | Metriotes" if len(t) + 12 <= 65 else t


def strip_dashes(t):
    """Regla de copy de la casa: sin guiones largos."""
    return (t or "").replace("—", ",").replace("–", "-")


# ─── markdown mínimo ─────────────────────────────────────────────────────────
def inline(t):
    t = esc(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
    return t


def md_to_html(md):
    out, para, items, kind = [], [], [], None

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def flush_list():
        nonlocal kind
        if items:
            tag = "ol" if kind == "ol" else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{i}</li>" for i in items) + f"</{tag}>")
            items.clear()
            kind = None

    for raw in md.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            flush_para(); flush_list(); continue
        m = re.match(r"^(#{2,3})\s+(.*)$", line)
        if m:
            flush_para(); flush_list()
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            continue
        m = re.match(r"^\s*-\s+(?:\[( |x)\]\s+)?(.*)$", line)
        if m:
            flush_para()
            if kind == "ol":
                flush_list()
            kind = "ul"
            box = "" if m.group(1) is None else ("☑ " if m.group(1) == "x" else "☐ ")
            items.append(box + inline(m.group(2)))
            continue
        m = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if m:
            flush_para()
            if kind == "ul":
                flush_list()
            kind = "ol"
            items.append(inline(m.group(1)))
            continue
        flush_list()
        para.append(line.strip())
    flush_para(); flush_list()
    return "\n".join(out)


def parse_article(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError(f"{path.name}: falta front matter")
    meta = {}
    for ln in m.group(1).split("\n"):
        k, _, v = ln.partition(":")
        meta[k.strip()] = v.strip()
    body = strip_dashes(m.group(2).strip())
    meta["slug"] = path.stem
    meta["body"] = body
    meta["title"] = strip_dashes(meta["title"])
    meta["description"] = strip_dashes(meta["description"])
    words = len(re.findall(r"\w+", body))
    meta["minutes"] = max(1, round(words / 200))
    return meta


# ─── layout ──────────────────────────────────────────────────────────────────
def jsonld(objs):
    return "\n".join(
        '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False, separators=(",", ":")) + "</script>"
        for o in objs
    )


def breadcrumbs(trail):
    """trail = [(nombre, url_relativa)] → (HTML, JSON-LD)."""
    parts = []
    for i, (name, url) in enumerate(trail):
        if i < len(trail) - 1:
            parts.append(f'<a href="{url}">{esc(name)}</a>')
        else:
            parts.append(f"<span style='margin:0'>{esc(name)}</span>")
    h = '<nav class="s-crumbs" aria-label="Migas de pan">' + "<span>›</span>".join(parts) + "</nav>"
    ld = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u}
            for i, (n, u) in enumerate(trail)
        ],
    }
    return h, ld


def layout(*, title, description, path, body, ld=(), robots="index,follow,max-image-preview:large", image=None, og_type="website", wide=False):
    image = image or f"{SITE}/assets/og-image.png"
    url = SITE + path
    cats = "".join(f'<a href="/profesionales/{c["slug"]}/">{esc(c["name"])}</a>' for c in CATEGORIES[:6])
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#5B7A94">
<link rel="canonical" href="{url}">
<link rel="icon" href="/app/favicon.png">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Metriotes">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{esc(image)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@metrioteslife">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{esc(image)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Kalnia:wght@400;600;700&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/seo.css">
{jsonld(ld)}
</head>
<body>
<header class="s-nav">
  <div class="s-nav-inner">
    <a class="s-logo" href="/">Metriotes</a>
    <nav class="s-links" aria-label="Principal">
      <a href="/profesionales/">Profesionales</a>
      <a href="/blog/">Blog</a>
      <a href="/#profesionales">Para profesionales</a>
      <a class="s-cta" href="/#descarga">Descargar</a>
    </nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="s-foot">
  <div class="s-foot-inner">
    <div><h4>Encuentra</h4>{cats}<a href="/profesionales/">Ver todos los oficios</a></div>
    <div><h4>Aprende</h4><a href="/blog/">Blog y guías</a><a href="/blog/como-crear-habitos-que-duran/">Cómo crear hábitos</a><a href="/blog/como-definir-objetivos-con-proposito/">Cómo definir objetivos</a></div>
    <div><h4>Para profesionales</h4><a href="/#profesionales">Crea tu perfil</a><a href="/blog/como-conseguir-alumnos-instructor-independiente/">Consigue alumnos</a><a href="/blog/app-para-gestionar-clases-y-reservas/">Gestiona tus clases</a></div>
    <div><h4>Metriotes</h4><a href="/">Inicio</a><a href="/privacy.html">Privacidad</a><a href="/terms.html">Términos</a><a href="https://www.instagram.com/metrioteslife" rel="noopener">Instagram</a></div>
    <p class="s-copy">© {date.today().year} Metriotes. La persona que quieres ser.</p>
  </div>
</footer>
</body>
</html>
"""


def write(path, content):
    p = ROOT / path.lstrip("/")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def app_cta(extra=""):
    return f"""<div class="s-box">
<h2>Descarga Metriotes y empieza hoy</h2>
<p>Define tu Norte, convierte tus objetivos en hábitos y encuentra profesionales de tu ciudad. Gratis para empezar.{extra}</p>
<div class="s-btns"><a class="s-btn" href="{APP_STORE}" rel="noopener">App Store</a><a class="s-btn s-btn-ghost" href="{PLAY_STORE}" rel="noopener">Google Play</a><a class="s-btn s-btn-ghost" href="/app/">Abrir en el navegador</a></div>
</div>"""


# ─── profesionales ───────────────────────────────────────────────────────────
def pro_slug(p):
    return f'{slugify(p.get("display_name") or p.get("profile_name") or "profesional")}-{p["id"]}'


def pro_url(p):
    return f"/perfil/{pro_slug(p)}/"


def pro_name(p):
    return strip_dashes((p.get("display_name") or p.get("profile_name") or "Profesional").strip())


def pro_country(p):
    return COUNTRIES.get((p.get("country") or "").upper(), p.get("country") or "")


def pro_location(p):
    return ", ".join(x for x in [p.get("city"), pro_country(p)] if x)


def pro_modality(p):
    m = []
    if p.get("attends_in_person"):
        m.append("presencial")
    if p.get("attends_online"):
        m.append("online")
    return " y ".join(m)


def prof_names(p):
    """Nombres de profesión en español si existen (se evitan duplicados en inglés)."""
    pr = p.get("professions") or []
    es = [x["name"] for x in pr if x.get("language") == "es"]
    return es or [x["name"] for x in pr]


def pro_in_category(p, cat):
    tokens = cat["match"] + EXTRA_MATCH.get(cat["slug"], [])
    for pr in p.get("professions") or []:
        n = norm(pr["name"])
        for t in tokens:
            if re.search(r"\b" + re.escape(norm(t)), n):
                return True
    return False


def pro_indexable(p):
    return len((p.get("bio") or "").strip()) >= 80


def stars(r):
    try:
        r = float(r)
    except (TypeError, ValueError):
        return ""
    full = int(round(r))
    return "★" * full + "☆" * (5 - full)


def pro_card(p):
    avatar = p.get("avatar_url")
    img = f'<img class="s-avatar" src="{esc(avatar)}" alt="{esc(pro_name(p))}" loading="lazy" width="64" height="64">' if avatar else '<span class="s-avatar"></span>'
    rating = ""
    if p.get("ratings_count"):
        rating = f'<div class="s-stars" aria-label="Valoración {p["average_rating"]} de 5">{stars(p["average_rating"])} <span style="color:var(--ink-3)">{p["average_rating"]} ({p["ratings_count"]})</span></div>'
    meta = " · ".join(x for x in [", ".join(prof_names(p)[:2]), pro_location(p), pro_modality(p).capitalize()] if x)
    link = pro_url(p) if pro_indexable(p) else f'/app/professional/{share_hash(p["id"])}'
    return f'<a class="s-card" href="{link}"><div class="s-pro">{img}<div><h3>{esc(pro_name(p))}</h3>{rating}</div></div><p style="margin-top:10px">{esc(meta)}</p></a>'


def build_pro_page(p, cats_for_pro):
    name = pro_name(p)
    profs = prof_names(p)
    prof_txt = profs[0] if profs else "Profesional"
    loc = pro_location(p)
    h = share_hash(p["id"])
    title = f"{name}: {prof_txt}{' en ' + p['city'] if p.get('city') else ''} | Metriotes"
    bio = strip_dashes((p.get("bio") or "").strip())
    desc = short(f"{name}, {prof_txt.lower()}{' en ' + loc if loc else ''}. {bio}", 158)
    trail = [("Inicio", "/"), ("Profesionales", "/profesionales/")]
    if cats_for_pro:
        trail.append((cats_for_pro[0]["name"], f"/profesionales/{cats_for_pro[0]['slug']}/"))
    trail.append((name, pro_url(p)))
    bc_html, bc_ld = breadcrumbs(trail)

    person = {
        "@context": "https://schema.org", "@type": "Person", "name": name,
        "jobTitle": prof_txt, "description": short(bio, 300), "url": SITE + pro_url(p),
    }
    if p.get("avatar_url"):
        person["image"] = p["avatar_url"]
    if p.get("city"):
        person["workLocation"] = {"@type": "Place", "address": {"@type": "PostalAddress", "addressLocality": p["city"], "addressCountry": (p.get("country") or "").upper()}}
    same = []
    if p.get("website_url"):
        same.append(p["website_url"])
    if p.get("linkedin_url"):
        same.append(p["linkedin_url"])
    if p.get("instagram_handle"):
        same.append("https://instagram.com/" + p["instagram_handle"].lstrip("@"))
    if same:
        person["sameAs"] = same
    if p.get("ratings_count"):
        person["aggregateRating"] = {"@type": "AggregateRating", "ratingValue": str(p["average_rating"]), "reviewCount": p["ratings_count"], "bestRating": "5"}

    paras = "".join(f"<p>{esc(x.strip())}</p>" for x in bio.split("\n") if x.strip())
    avatar = f'<img class="s-avatar s-avatar-lg" src="{esc(p["avatar_url"])}" alt="{esc(name)}" width="120" height="120">' if p.get("avatar_url") else ""
    rating = ""
    if p.get("ratings_count"):
        rating = f'<p class="s-stars">{stars(p["average_rating"])} <span style="color:var(--ink-3)">{p["average_rating"]} de 5 · {p["ratings_count"]} valoraciones</span></p>'
    chips = "".join(f'<span class="s-chip">{esc(x)}</span>' for x in profs)
    mod = pro_modality(p)
    facts = []
    if loc:
        facts.append(f"<li><strong>Ubicación:</strong> {esc(loc)}</li>")
    if mod:
        facts.append(f"<li><strong>Modalidad:</strong> {esc(mod.capitalize())}</li>")
    if p.get("specializations"):
        facts.append("<li><strong>Áreas de trabajo:</strong> " + esc(", ".join(s["name"] for s in p["specializations"])) + "</li>")

    related = "".join(f'<a class="s-chip" href="/profesionales/{c["slug"]}/">Más {esc(c["plural"])}</a>' for c in cats_for_pro)
    body = f"""<div class="s-wrap">
{bc_html}
<div class="s-pro" style="margin-bottom:22px">{avatar}<div><h1 style="margin:0 0 6px">{esc(name)}</h1><p class="s-lead" style="margin:0">{esc(prof_txt)}{' en ' + esc(loc) if loc else ''}</p>{rating}</div></div>
<div class="s-chips">{chips}</div>
<div class="s-prose" style="margin-top:22px">
<h2>Sobre {esc(name)}</h2>
{paras}
<ul>{''.join(facts)}</ul>
</div>
<div class="s-box">
<h2>Reserva con {esc(name.split()[0])}</h2>
<p>Mira servicios, horarios, eventos y valoraciones, y reserva directamente en Metriotes.</p>
<div class="s-btns"><a class="s-btn" href="/app/professional/{h}">Ver perfil completo y reservar</a><a class="s-btn s-btn-ghost" href="{APP_STORE}" rel="noopener">Descargar la app</a></div>
</div>
<div class="s-chips">{related}</div>
</div>"""
    return layout(title=title, description=desc, path=pro_url(p), body=body, ld=[person, bc_ld], image=p.get("avatar_url"), og_type="profile")


def build_category_page(cat, pros, articles, city=None):
    plural = cat["plural"]
    if city:
        city_name, city_pros = city
        path = f"/profesionales/{cat['slug']}/{slugify(city_name)}/"
        title = with_brand(f"{cat['plural'].capitalize()} en {city_name}")
        desc = short(f"Encuentra {plural} en {city_name}. Perfiles verificados, reseñas y reserva desde la app de Metriotes.", 158)
        h1 = f"{cat['plural'].capitalize()} en {city_name}"
        lead = f"{len(city_pros)} {'profesional' if len(city_pros) == 1 else 'profesionales'} de {cat['name'].lower()} en {city_name} que puedes contactar y reservar desde Metriotes."
        shown = city_pros
        trail = [("Inicio", "/"), ("Profesionales", "/profesionales/"), (cat["name"], f"/profesionales/{cat['slug']}/"), (city_name, path)]
    else:
        path = f"/profesionales/{cat['slug']}/"
        title = with_brand(strip_dashes(cat["title"]))
        desc = strip_dashes(cat["description"])
        h1 = cat["h1"]
        lead = strip_dashes(cat["lead"])
        shown = pros
        trail = [("Inicio", "/"), ("Profesionales", "/profesionales/"), (cat["name"], path)]
    bc_html, bc_ld = breadcrumbs(trail)

    if shown:
        listing = '<div class="s-grid">' + "".join(pro_card(p) for p in shown) + "</div>"
        listing_h = f"<h2>{esc(cat['plural'].capitalize())} en Metriotes</h2>"
    else:
        listing = (
            '<div class="s-box"><h2>Estamos sumando profesionales</h2>'
            f"<p>Todavía no hay perfiles publicados de {esc(plural)} en esta categoría. Descarga la app para ver los que se vayan sumando en tu ciudad, o si ofreces este servicio, crea tu perfil gratis.</p>"
            '<div class="s-btns"><a class="s-btn" href="/#profesionales">Soy profesional</a><a class="s-btn s-btn-ghost" href="/#descarga">Descargar la app</a></div></div>'
        )
        listing_h = ""

    cities = {}
    for p in pros:
        if p.get("city"):
            cities.setdefault(p["city"].strip(), []).append(p)
    city_chips = ""
    if not city and cities:
        city_chips = '<h2>Por ciudad</h2><div class="s-chips">' + "".join(
            f'<a class="s-chip" href="/profesionales/{cat["slug"]}/{slugify(c)}/">{esc(c)} ({len(v)})</a>' for c, v in sorted(cities.items())
        ) + "</div>"

    secs = ""
    if not city:
        for h2, blocks in cat["sections"]:
            secs += f"<h2>{esc(strip_dashes(h2))}</h2>" + md_to_html(strip_dashes("\n\n".join(blocks)))
    faqs = cat["faqs"]
    faq_html = '<h2>Preguntas frecuentes</h2><div class="s-faq">' + "".join(
        f"<details><summary>{esc(strip_dashes(q))}</summary><p>{esc(strip_dashes(a))}</p></details>" for q, a in faqs
    ) + "</div>"
    faq_ld = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": strip_dashes(q), "acceptedAnswer": {"@type": "Answer", "text": strip_dashes(a)}} for q, a in faqs],
    }
    ld = [bc_ld, faq_ld]
    if shown:
        ld.append({
            "@context": "https://schema.org", "@type": "ItemList", "name": h1,
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "url": SITE + (pro_url(p) if pro_indexable(p) else path), "name": pro_name(p)}
                for i, p in enumerate(shown)
            ],
        })
    arts = [a for a in articles if a["slug"] in cat["articles"]]
    art_html = ""
    if arts:
        art_html = "<h2>Guías para elegir bien</h2><div class='s-grid'>" + "".join(
            f'<a class="s-card" href="/blog/{a["slug"]}/"><span class="s-tag">{esc(a["tag"])}</span><h3>{esc(a["title"])}</h3><p>{esc(short(a["description"], 110))}</p></a>' for a in arts
        ) + "</div>"
    others = "".join(f'<a class="s-chip" href="/profesionales/{c["slug"]}/">{esc(c["name"])}</a>' for c in CATEGORIES if c["slug"] != cat["slug"])

    body = f"""<div class="s-wrap s-wide">
{bc_html}
<h1>{esc(h1)}</h1>
<p class="s-lead">{esc(lead)}</p>
{listing_h}{listing}
{city_chips}
<div class="s-prose" style="max-width:760px">{secs}</div>
{art_html}
<div style="max-width:760px">{faq_html}</div>
{app_cta()}
<h2>Otros profesionales</h2><div class="s-chips">{others}</div>
</div>"""
    # Una página de ciudad con una sola persona y sin texto propio es fina: la dejamos
    # indexable sólo si hay al menos 1 perfil (siempre cierto, se genera sólo en ese caso).
    return path, layout(title=title, description=desc, path=path, body=body, ld=ld)


def build_hub(pros, articles):
    path = "/profesionales/"
    bc_html, bc_ld = breadcrumbs([("Inicio", "/"), ("Profesionales", path)])
    cards = ""
    for c in CATEGORIES:
        n = len([p for p in pros if pro_in_category(p, c)])
        count = f"{n} {'perfil' if n == 1 else 'perfiles'}" if n else "Próximamente"
        cards += f'<a class="s-card" href="/profesionales/{c["slug"]}/"><span class="s-tag">{count}</span><h3>{esc(c["name"])}</h3><p>{esc(short(strip_dashes(c["lead"]), 110))}</p></a>'
    cities = {}
    for p in pros:
        if p.get("city"):
            cities.setdefault(p["city"].strip(), 0)
            cities[p["city"].strip()] += 1
    city_html = ""
    if cities:
        city_html = "<h2>Ciudades con profesionales</h2><div class='s-chips'>" + "".join(
            f'<span class="s-chip">{esc(c)} ({n})</span>' for c, n in sorted(cities.items())) + "</div>"
    body = f"""<div class="s-wrap s-wide">
{bc_html}
<h1>Encuentra al profesional que te acompaña</h1>
<p class="s-lead">Psicólogos, coaches, instructores de pilates y yoga, profesores de idiomas, nutricionistas y más. Perfiles reales, reseñas verificadas y reserva desde la app.</p>
<div class="s-grid">{cards}</div>
{city_html}
<div class="s-box"><h2>¿Eres profesional?</h2><p>Crea tu perfil gratis, publica tus servicios, clases y eventos, y recibe reservas de clientes de tu ciudad.</p><div class="s-btns"><a class="s-btn" href="/#profesionales">Crear mi perfil profesional</a><a class="s-btn s-btn-ghost" href="/blog/como-conseguir-alumnos-instructor-independiente/">Cómo conseguir alumnos</a></div></div>
{app_cta()}
</div>"""
    ld = [bc_ld, {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Directorio de profesionales de Metriotes", "url": SITE + path}]
    return layout(
        title="Directorio de profesionales de bienestar | Metriotes",
        description="Encuentra psicólogos, coaches, instructores de pilates y yoga, profesores de idiomas y nutricionistas. Perfiles reales, reseñas y reserva desde la app.",
        path=path, body=body, ld=ld)


# ─── eventos ─────────────────────────────────────────────────────────────────
def ev_slug(e):
    return f'{slugify(e["title"])}-{e["id"]}'


def ev_url(e):
    return f"/eventos/{ev_slug(e)}/"


def event_publishable(e):
    if not e.get("is_active") or e.get("cancelled") or e.get("visibility", "public") != "public":
        return False
    if e.get("parent_event_id"):
        return False  # sólo la cabeza de cada serie
    if e.get("is_series_finished"):
        return False
    try:
        start = datetime.fromisoformat(e["start_date"].replace("Z", "+00:00"))
    except Exception:  # noqa: BLE001
        return False
    if start < datetime.now(timezone.utc) and not (e.get("is_recurring") or e.get("weekday_schedule")):
        return False
    return True


def build_event_page(e, pro):
    title_raw = strip_dashes(e["title"])
    h = share_hash(e["id"])
    desc_txt = strip_dashes((e.get("description") or "").strip())
    start_txt, start_dt = fmt_date(e["start_date"])
    is_series = bool(e.get("weekday_schedule"))
    sched = ""
    if is_series:
        sched = "; ".join(f"{WEEKDAYS_PL[s['weekday']]} de {s['start_time']} a {s['end_time']}" for s in e["weekday_schedule"])
    where = "Online" if e.get("is_online") else (e.get("location") or "")
    kind = "Clases" if e.get("event_type") == "classes" else "Evento"
    pname = pro_name(pro) if pro else None
    title = f"{title_raw}{' en ' + e['location'] if e.get('location') and not e.get('is_online') else ''} | {kind} en Metriotes"
    desc = short(f"{title_raw}. {desc_txt}", 158)
    trail = [("Inicio", "/"), ("Eventos y clases", "/eventos/"), (title_raw, ev_url(e))]
    bc_html, bc_ld = breadcrumbs(trail)

    ev = {
        "@context": "https://schema.org", "@type": "Event", "name": title_raw,
        "description": short(desc_txt, 300), "startDate": e["start_date"],
        "eventStatus": "https://schema.org/EventScheduled",
        "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode" if e.get("is_online") else "https://schema.org/OfflineEventAttendanceMode",
        "url": SITE + ev_url(e),
    }
    if e.get("end_date"):
        ev["endDate"] = e["end_date"]
    if e.get("cover_image_url"):
        ev["image"] = [e["cover_image_url"]]
    if e.get("is_online"):
        ev["location"] = {"@type": "VirtualLocation", "url": SITE + ev_url(e)}
    elif e.get("location"):
        ev["location"] = {"@type": "Place", "name": e["location"], "address": e["location"]}
    if pro:
        ev["organizer"] = {"@type": "Person", "name": pname, "url": SITE + pro_url(pro)}
    price = e.get("effective_price")
    if price not in (None, ""):
        ev["offers"] = {"@type": "Offer", "price": str(price), "priceCurrency": e.get("currency") or "EUR", "availability": "https://schema.org/InStock", "url": SITE + ev_url(e)}
    else:
        ev["isAccessibleForFree"] = True

    cover = f'<img src="{esc(e["cover_image_url"])}" alt="{esc(title_raw)}" style="border-radius:20px;margin:6px 0 22px;width:100%;max-height:380px;object-fit:cover" loading="lazy">' if e.get("cover_image_url") else ""
    facts = [f"<li><strong>{'Primera fecha' if is_series else 'Fecha'}:</strong> {start_txt}</li>"]
    if sched:
        facts.append(f"<li><strong>Horario:</strong> {esc(sched)}</li>")
    if where:
        facts.append(f"<li><strong>Lugar:</strong> {esc(where)}</li>")
    if price not in (None, ""):
        facts.append(f"<li><strong>Precio:</strong> {esc(str(price))} {esc(e.get('currency') or 'EUR')}</li>")
    else:
        facts.append("<li><strong>Precio:</strong> consulta en la app</li>")
    if e.get("max_participants"):
        facts.append(f"<li><strong>Cupos:</strong> {e['max_participants']}</li>")
    maps = f'<a class="s-btn s-btn-ghost" href="{esc(e["maps_url"])}" rel="noopener nofollow">Ver en el mapa</a>' if e.get("maps_url") else ""
    host = f'<p>Organiza <a href="{pro_url(pro)}">{esc(pname)}</a>.</p>' if pro and pro_indexable(pro) else (f"<p>Organiza {esc(pname)}.</p>" if pname else "")
    paras = "".join(f"<p>{esc(x.strip())}</p>" for x in desc_txt.split("\n") if x.strip())
    body = f"""<div class="s-wrap">
{bc_html}
<span class="s-tag">{kind}</span>
<h1>{esc(title_raw)}</h1>
{cover}
<div class="s-prose">{paras}<ul>{''.join(facts)}</ul>{host}</div>
<div class="s-box"><h2>Reserva tu lugar</h2><p>Inscríbete en Metriotes y recibe tu entrada con código QR.</p><div class="s-btns"><a class="s-btn" href="/app/event/{h}">Inscribirme</a>{maps}</div></div>
</div>"""
    return layout(title=title, description=desc, path=ev_url(e), body=body, ld=[ev, bc_ld], image=e.get("cover_image_url"), og_type="article")


def build_events_index(events, pros_by_id):
    path = "/eventos/"
    bc_html, bc_ld = breadcrumbs([("Inicio", "/"), ("Eventos y clases", path)])
    if events:
        cards = ""
        for e in events:
            pro = pros_by_id.get(e["professional_profile"])
            when = fmt_date(e["start_date"])[0]
            sub = " · ".join(x for x in [when, "Online" if e.get("is_online") else e.get("location"), pro_name(pro) if pro else None] if x)
            cards += f'<a class="s-card" href="{ev_url(e)}"><span class="s-tag">{"Clases" if e.get("event_type") == "classes" else "Evento"}</span><h3>{esc(strip_dashes(e["title"]))}</h3><p>{esc(sub)}</p></a>'
        listing = f'<div class="s-grid">{cards}</div>'
    else:
        listing = '<div class="s-box"><h2>Pronto, más clases y eventos</h2><p>Descarga la app para enterarte de las nuevas clases abiertas, talleres y eventos de tu ciudad.</p></div>'
    body = f"""<div class="s-wrap s-wide">{bc_html}<h1>Eventos y clases abiertas</h1>
<p class="s-lead">Clases de pilates, yoga, idiomas, talleres y encuentros organizados por profesionales de Metriotes.</p>
{listing}{app_cta()}</div>"""
    return layout(title="Eventos y clases abiertas cerca de ti | Metriotes", description="Descubre clases abiertas, talleres y eventos de profesionales de Metriotes: pilates, yoga, idiomas, bienestar y más.", path=path, body=body, ld=[bc_ld])


# ─── blog ────────────────────────────────────────────────────────────────────
def build_article(a, articles):
    path = f"/blog/{a['slug']}/"
    bc_html, bc_ld = breadcrumbs([("Inicio", "/"), ("Blog", "/blog/"), (a["title"], path)])
    d = datetime.fromisoformat(a["date"])
    ld = {
        "@context": "https://schema.org", "@type": "BlogPosting", "headline": a["title"],
        "description": a["description"], "datePublished": a["date"], "dateModified": a.get("updated", a["date"]),
        "inLanguage": "es", "mainEntityOfPage": SITE + path,
        "image": SITE + "/assets/og-image.png",
        "author": {"@type": "Organization", "name": "Metriotes", "url": SITE + "/"},
        "publisher": {"@type": "Organization", "name": "Metriotes", "logo": {"@type": "ImageObject", "url": SITE + "/assets/logo.png"}},
    }
    cat = by_slug(a.get("related", ""))
    cta = ""
    if cat:
        cta = f'<div class="s-box"><h2>Encuentra {esc(cat["plural"])} en Metriotes</h2><p>Compara perfiles, mira reseñas y reserva desde la app.</p><div class="s-btns"><a class="s-btn" href="/profesionales/{cat["slug"]}/">Ver {esc(cat["plural"])}</a></div></div>'
    more = [x for x in articles if x["slug"] != a["slug"]]
    more.sort(key=lambda x: (x.get("related") != a.get("related"), x["slug"]))
    more_html = "<h2>Sigue leyendo</h2><div class='s-grid'>" + "".join(
        f'<a class="s-card" href="/blog/{x["slug"]}/"><span class="s-tag">{esc(x["tag"])}</span><h3>{esc(x["title"])}</h3></a>' for x in more[:3]) + "</div>"
    body = f"""<article class="s-wrap">
{bc_html}
<span class="s-tag">{esc(a["tag"])}</span>
<h1>{esc(a["title"])}</h1>
<p class="s-meta">Por el equipo de Metriotes · {d.day} de {MONTHS[d.month - 1]} de {d.year} · {a["minutes"]} min de lectura</p>
<div class="s-prose">{md_to_html(a["body"])}</div>
{cta}{app_cta()}{more_html}
</article>"""
    return path, layout(title=with_brand(a['title']), description=a["description"], path=path, body=body, ld=[ld, bc_ld], og_type="article")


def build_blog_index(articles):
    path = "/blog/"
    bc_html, bc_ld = breadcrumbs([("Inicio", "/"), ("Blog", path)])
    cards = "".join(
        f'<a class="s-card" href="/blog/{a["slug"]}/"><span class="s-tag">{esc(a["tag"])}</span><h3>{esc(a["title"])}</h3><p>{esc(short(a["description"], 120))}</p></a>'
        for a in sorted(articles, key=lambda x: x["date"], reverse=True))
    body = f"""<div class="s-wrap s-wide">{bc_html}<h1>Blog de Metriotes</h1>
<p class="s-lead">Guías prácticas para elegir profesionales, crear hábitos que duran y vivir con más dirección.</p>
<div class="s-grid">{cards}</div>{app_cta()}</div>"""
    return layout(title="Blog de bienestar y desarrollo personal | Metriotes", description="Guías para elegir profesor de pilates, yoga o idiomas, psicólogo o coach, crear hábitos que duran y definir objetivos con propósito.", path=path, body=body, ld=[bc_ld, {"@context": "https://schema.org", "@type": "Blog", "name": "Blog de Metriotes", "url": SITE + path, "inLanguage": "es"}])


# ─── sitemap / robots / llms ─────────────────────────────────────────────────
def build_sitemap(urls):
    rows = "".join(
        f"<url><loc>{SITE}{u}</loc><lastmod>{lm}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority></url>\n"
        for u, lm, cf, pr in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}</urlset>\n'


ROBOTS = f"""User-agent: *
Allow: /
# /app/ (la web app de Flutter, un lienzo sin texto indexable) NO se bloquea acá a
# propósito: lleva <meta name="robots" content="noindex"> y para que Google lo lea
# tiene que poder rastrearla. Sus equivalentes públicos viven en /perfil/,
# /eventos/ y /profesionales/.
Disallow: /design-system/
Disallow: /dashboard.html
Disallow: /tournament-results.html

# Rastreadores de IA y buscadores conversacionales: permitidos.
User-agent: GPTBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: {SITE}/sitemap.xml
"""


def build_llms(articles, cats_with_pros):
    lines = [
        "# Metriotes",
        "",
        "> Metriotes es una app para convertir tus valores en objetivos y hábitos, y encontrar profesionales de bienestar (psicólogos, coaches, instructores de pilates y yoga, profesores de idiomas, nutricionistas, entrenadores) en tu ciudad. Disponible en iOS, Android y web. Gratis para empezar.",
        "",
        "## Directorio de profesionales",
    ]
    for c in CATEGORIES:
        lines.append(f"- [{c['name']}]({SITE}/profesionales/{c['slug']}/): {strip_dashes(c['lead'])}")
    lines += ["", "## Guías"]
    for a in sorted(articles, key=lambda x: x["date"], reverse=True):
        lines.append(f"- [{a['title']}]({SITE}/blog/{a['slug']}/): {a['description']}")
    lines += ["", "## Más", f"- [Inicio]({SITE}/)", f"- [Eventos y clases]({SITE}/eventos/)", ""]
    return "\n".join(lines)


# ─── main ────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()

    for d in GENERATED_DIRS:
        shutil.rmtree(ROOT / d, ignore_errors=True)

    articles = [parse_article(p) for p in sorted((Path(__file__).parent / "articles").glob("*.md"))]
    pros, events = [], []
    if not args.offline:
        print("Leyendo profesionales y eventos de la API pública…")
        pros = fetch("/coaches/professional-profiles/") or []
        events = fetch("/coaches/events/") or []
        print(f"  {len(pros)} profesionales visibles, {len(events)} eventos")
    pros_by_id = {p["id"]: p for p in pros}

    # lastmod estable: sólo cambia cuando cambian los datos (así el job diario
    # no genera commits vacíos). Sin datos, cae a la fecha del último artículo.
    stamps = [(x.get("updated_at") or "")[:10] for x in pros + events if x.get("updated_at")]
    LAST = max(stamps + [a.get("updated", a["date"]) for a in articles])

    urls = [("/", LAST, "weekly", "1.0"), ("/blog/", LAST, "weekly", "0.8"),
            ("/profesionales/", LAST, "daily", "0.9"), ("/eventos/", LAST, "daily", "0.6")]

    # Blog
    for a in articles:
        path, content = build_article(a, articles)
        write(path + "index.html", content)
        urls.append((path, a["date"], "monthly", "0.7"))
    write("/blog/index.html", build_blog_index(articles))

    # Categorías + ciudades
    write("/profesionales/index.html", build_hub(pros, articles))
    for cat in CATEGORIES:
        cat_pros = [p for p in pros if pro_in_category(p, cat)]
        path, content = build_category_page(cat, cat_pros, articles)
        write(path + "index.html", content)
        urls.append((path, LAST, "weekly", "0.9"))
        by_city = {}
        for p in cat_pros:
            if p.get("city"):
                by_city.setdefault(p["city"].strip(), []).append(p)
        for city_name, cp in by_city.items():
            cpath, ccontent = build_category_page(cat, cat_pros, articles, city=(city_name, cp))
            write(cpath + "index.html", ccontent)
            urls.append((cpath, LAST, "weekly", "0.8"))

    # Fichas de profesionales
    n_pro = 0
    for p in pros:
        if not pro_indexable(p):
            continue
        cats_for_pro = [c for c in CATEGORIES if pro_in_category(p, c)]
        write(pro_url(p) + "index.html", build_pro_page(p, cats_for_pro))
        urls.append((pro_url(p), (p.get("updated_at") or LAST)[:10], "weekly", "0.7"))
        n_pro += 1

    # Eventos
    pub_events = [e for e in events if event_publishable(e)]
    for e in pub_events:
        write(ev_url(e) + "index.html", build_event_page(e, pros_by_id.get(e["professional_profile"])))
        urls.append((ev_url(e), (e.get("updated_at") or LAST)[:10], "daily", "0.6"))
    write("/eventos/index.html", build_events_index(pub_events, pros_by_id))

    write("/sitemap.xml", build_sitemap(urls))
    write("/robots.txt", ROBOTS)
    write("/llms.txt", build_llms(articles, None))
    print(f"OK · {len(articles)} artículos · {len(CATEGORIES)} categorías · {n_pro} fichas · {len(pub_events)} eventos · {len(urls)} URLs en el sitemap")


if __name__ == "__main__":
    main()
