#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate hardcoded HTML pages for Mini-słownik matematyki PL-UA."""
from pathlib import Path

from pages_data import PAGES
from ai_prompts import (
    prompt_hero,
    prompt_life,
    prompt_card_media,
)

ROOT = Path(__file__).resolve().parent
PAGES_DIR = ROOT / "pages"
ASSETS = ROOT / "assets"
IMAGES = ASSETS / "images"
ICONS = ASSETS / "icons"
ASSETS.mkdir(exist_ok=True)
IMAGES.mkdir(exist_ok=True)
ICONS.mkdir(exist_ok=True)
PAGES_DIR.mkdir(exist_ok=True)

# Domyślne typy media wg kategorii (zaślepki do podmiany)
CAT_MEDIA = {
    "A": {"hero": "🔢", "life": "🍎", "photo": "📸", "life_pl": "Liczby widzisz w sklepie, na ulicy, w grze.", "life_ua": "Числа бачиш у магазині, на вулиці, в грі."},
    "B": {"hero": "➕", "life": "🧮", "photo": "✏️", "life_pl": "Działania pomagają dzielić się, kupować, liczyć punkty.", "life_ua": "Дії допомагають ділитися, купувати, рахувати очки."},
    "C": {"hero": "🍕", "life": "🍰", "photo": "🧀", "life_pl": "Ułamki to części pizzy, tortu, czekolady.", "life_ua": "Дроби — частини піци, торта, шоколаду."},
    "D": {"hero": "📐", "life": "🏠", "photo": "△", "life_pl": "Figury są w domach, znakach, w przyrodzie.", "life_ua": "Фігури є в будинках, знаках, у природі."},
    "E": {"hero": "📏", "life": "⏱️", "photo": "🪙", "life_pl": "Miary pomagają gotować, podróżować, płacić.", "life_ua": "Величини допомагають готувати, подорожувати, платити."},
    "F": {"hero": "📊", "life": "🎲", "photo": "📈", "life_pl": "Dane pomagają porównywać i podejmować decyzje.", "life_ua": "Дані допомагають порівнювати і приймати рішення."},
}


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def wordwall_stub(url: str = "#") -> str:
    """Link do ćwiczenia na karcie — tylko gdy jest prawdziwy URL."""
    href = (url or "").strip()
    if not href or href == "#":
        return ""
    return (
        "\n          <div class=\"card-task no-print\">\n"
        f'            <a class="wordwall-link" href="{esc(href)}" target="_blank" rel="noopener noreferrer">\n'
        '              <span class="ww-ico" aria-hidden="true">▶</span>\n'
        "              Ćwiczenie · Wordwall\n"
        '              <span class="lab-ua">Вправа</span>\n'
        "            </a>\n"
        "          </div>"
    )


def page_wordwall_block(page: dict) -> str:
    """Wordwall po „Częsty błąd”: live iframe gdy jest embed, inaczej przycisk."""
    from wordwall_embeds import embed_for_page

    n = int(page.get("n") or 0)
    embed = embed_for_page(page)
    href = (page.get("wordwall") or page.get("wordwall_url") or "").strip() or "#"
    if embed:
        href = embed.split("?")[0].replace("/embed/", "/uk/play/").replace("/uk/uk/", "/uk/")
        # keep play link optional; iframe uses embed URL
        iframe = (
            f'<iframe style="max-width:100%" src="{esc(embed)}" '
            f'width="500" height="380" frameborder="0" allowfullscreen loading="lazy"></iframe>'
        )
        return (
            f'\n    <section class="page-wordwall no-print" aria-label="Ćwiczenie Wordwall" '
            f'id="wordwall-s{n:02d}">\n'
            '      <div class="page-wordwall-inner page-wordwall-inner--embed">\n'
            '        <div class="page-wordwall-text">\n'
            '          <h3>Ćwiczenie · Wordwall <span class="ua">Вправа</span></h3>\n'
            "          <p>Sprawdź hasła z tej strony w krótkim quizie.</p>\n"
            '          <p class="ua">Перевір поняття з цієї сторінки в короткому квізі.</p>\n'
            "        </div>\n"
            f"        <div class=\"page-wordwall-embed\">{iframe}</div>\n"
            "      </div>\n"
            "    </section>"
        )

    live = href != "#"
    link_cls = "wordwall-link" + ("" if live else " wordwall-link--pending")
    extra = ' target="_blank" rel="noopener noreferrer"' if live else ""
    return (
        f'\n    <section class="page-wordwall no-print" aria-label="Ćwiczenie Wordwall" id="wordwall-s{n:02d}">\n'
        '      <div class="page-wordwall-inner">\n'
        '        <div class="page-wordwall-text">\n'
        '          <h3>Ćwiczenie · Wordwall <span class="ua">Вправа</span></h3>\n'
        "          <p>Sprawdź hasła z tej strony w krótkim quizie.</p>\n"
        '          <p class="ua">Перевір поняття з цієї сторінки в короткому квізі.</p>\n'
        "        </div>\n"
        f'        <a class="{link_cls}" href="{esc(href)}"{extra}>\n'
        '          <span class="ww-ico" aria-hidden="true">▶</span>\n'
        "          Otwórz ćwiczenie\n"
        '          <span class="lab-ua">Відкрити вправу</span>\n'
        "        </a>\n"
        "      </div>\n"
        "    </section>"
    )


def block_meta(klasa: str) -> str:
    if not klasa:
        return ""
    return (
        "\n          <div class=\"block-meta\">\n"
        f'            <span class="klasa-pill" title="Etap w polskiej szkole podstawowej">{esc(klasa)}</span>\n'
        "          </div>"
    )


def media_block(
    kind: str,
    emoji: str,
    label: str,
    prompt: str,
    *,
    page_n: int,
    slot: str,
    alt: str = "",
    asset_prefix: str = "../",
) -> str:
    """
    Zawsze wstawia gotowy <img> (has-img), wg schematu:
      images/img01_1.png      → hero
      images/img01_2.png      → w życiu
      images/img01_3.png …    → karty (kolejno: karta1 = _3)
      icons/icon01_1.png …    → ikony kart
    """
    if slot.startswith("i") and slot[1:].isdigit():
        n = int(slot[1:])
        rel = f"assets/icons/icon{page_n:02d}_{n}.png"
    elif slot.startswith("c") and slot[1:].isdigit():
        n = int(slot[1:])
        rel = f"assets/images/img{page_n:02d}_{n + 2}.png"
    else:
        rel = f"assets/images/img{page_n:02d}_{slot}.png"

    src = f"{asset_prefix}{rel}"
    return (
        f'        <div class="media media--{kind} has-img">\n'
        f'          <img src="{esc(src)}" alt="{esc(alt or label)}" />\n'
        f"        </div>"
    )


def ph(kind: str, emoji: str, label: str, prompt: str, extra_class: str = "") -> str:
    """Unused legacy — kept for compatibility."""
    return (
        f'        <div class="media media--{kind} is-placeholder {extra_class}" '
        f'data-emoji="{emoji}" data-label="{esc(label)}"></div>'
    )


def card_html(i, c, page=None, asset_prefix="../"):
    from klasa_map import resolve_klasa
    from card_ux import present_card

    page = page or {}
    cat = page.get("cat", "A")
    page_n = int(page.get("asset_n") or page.get("source_n") or page.get("n") or 1)
    meta = CAT_MEDIA.get(cat, CAT_MEDIA["A"])
    media_kind = c.get("media") or "cover"
    term = c.get("pl") or ""
    klasa_n = int(page.get("source_n") or page.get("asset_n") or page.get("n") or page_n)
    klasa = resolve_klasa(klasa_n, term, c)
    ux = present_card(c)

    media_block_html = media_block(
        media_kind,
        meta["photo"],
        f"{media_kind} · {term}",
        prompt_card_media(page, c, media_kind),
        page_n=page_n,
        slot=f"c{i:02d}",
        alt=term,
        asset_prefix=asset_prefix,
    )

    klasa_html = block_meta(klasa)

    # ⚠ Nie pomyl
    np_rows = []
    for a, b in ux["nie_pomyl"]:
        if not a:
            continue
        if b:
            np_rows.append(
                "<li>"
                f'<span class="np-a">{esc(a)}</span>'
                '<span class="np-vs" aria-hidden="true">≠</span>'
                f'<span class="np-b">{esc(b)}</span>'
                "</li>"
            )
        else:
            np_rows.append(f'<li><span class="np-a">{esc(a)}</span></li>')
    if np_rows:
        nie_pomyl_html = (
            f'\n        <div class="ux-block ux-nie-pomyl">\n'
            f'          <span class="ux-label">⚠ Nie pomyl <span class="lab-ua">Не плутай</span></span>\n'
            f'          <ul class="np-list">\n            '
            + "\n            ".join(np_rows)
            + "\n          </ul>\n        </div>"
        )
    else:
        nie_pomyl_html = ""

    # ✅ Przykłady
    ex_items = "\n".join(f"<li>{esc(x)}</li>" for x in ux["przyklady"])
    przyklady_html = (
        f'\n        <div class="ux-block ux-przyklady">\n'
        f'          <span class="ux-label">✅ Przykłady <span class="lab-ua">Приклади</span></span>\n'
        f'          <ul class="ex-list">\n            {ex_items}\n          </ul>\n'
        f"        </div>"
    )

    zap_ua = (
        f'\n          <p class="ux-zap-ua">{esc(ux["zap_ua"])}</p>'
        if ux.get("zap_ua")
        else ""
    )
    co_ua = (
        f'\n          <p class="learn-ua">{esc(ux["co_ua"])}</p>'
        if ux.get("co_ua")
        else ""
    )

    return (
        f'\n      <article class="card card--ux {c.get("wide", "")}">\n'
        f'        <header class="card-head">\n'
        f'          <div class="card-num-row">\n'
        f'            <div class="card-num">{i}</div>\n'
        f"{klasa_html}\n"
        f"          </div>\n"
        f"          <h3>{esc(c['pl'])}</h3>\n"
        f'          <p class="term-ua">{esc(c["ua"])}</p>\n'
        f"        </header>\n\n"
        f'        <div class="card-illu">\n'
        f"{media_block_html}\n"
        f"        </div>\n"
        f'\n        <div class="ux-block ux-co">\n'
        f'          <span class="ux-label">📘 Co to jest? <span class="lab-ua">Що це?</span></span>\n'
        f'          <p class="learn-pl">{esc(ux["co_pl"])}</p>'
        f"{co_ua}\n"
        f"        </div>\n"
        f'\n        <div class="ux-block ux-zap">\n'
        f'          <span class="ux-label">⭐ Zapamiętaj <span class="lab-ua">Запам\'ятай</span></span>\n'
        f'          <div class="ux-zap-core">{esc(ux["zap_pl"])}</div>'
        f"{zap_ua}\n"
        f"        </div>\n"
        f"{nie_pomyl_html}\n"
        f"{przyklady_html}\n"
        f"      </article>"
    )


def chapter_body(p, asset_prefix="../"):
    """Treść jednej tematyki (bez <html>) — używane w pageXX i w book.html."""
    from page_summary_ux import render_cheat_section, render_mistake_section

    meta = CAT_MEDIA.get(p["cat"], CAT_MEDIA["A"])
    page_n = int(p.get("asset_n") or p.get("source_n") or p["n"])
    card_bits = [
        card_html(i + 1, c, p, asset_prefix=asset_prefix)
        for i, c in enumerate(p["cards"])
    ]
    cards = "\n".join(card_bits)

    hero = media_block(
        "hero",
        meta["hero"],
        f"hero · {p['title_pl']}",
        prompt_hero(p),
        page_n=page_n,
        slot="1",
        alt=p["title_pl"],
        asset_prefix=asset_prefix,
    )

    life_media = media_block(
        "photo",
        meta["life"],
        "w życiu · photo",
        prompt_life(p),
        page_n=page_n,
        slot="2",
        alt=f"W życiu — {p['title_pl']}",
        asset_prefix=asset_prefix,
    )

    howto_pl = (p.get("howto_pl") or "").strip()
    howto_ua = (p.get("howto_ua") or "").strip()
    howto_html = ""
    if howto_pl or howto_ua:
        howto_html = ""
        if howto_pl:
            howto_html += f'<p class="howto-mini">{esc(howto_pl)}</p>\n'
        if howto_ua:
            howto_html += f'<p class="howto-mini ua">{esc(howto_ua)}</p>\n'

    mistake_html = render_mistake_section(p)
    wordwall_html = page_wordwall_block(p)
    cheat_html = render_cheat_section(p)

    return f'''
    <header class="page-header">
      <div class="cat-badge">
        <div class="letter">{p["cat"]}</div>
        <div class="label">{esc(p["cat_pl"])}<br/>{esc(p["cat_ua"])}</div>
      </div>
      <div>
        <h1>{esc(p["title_pl"])}</h1>
        <p class="ua">{esc(p["title_ua"])}</p>
        <p class="intro">{esc(p["intro_pl"])}</p>
      </div>
      <aside class="owl-tip">
        <span class="owl-tip-icon" aria-hidden="true">🦉</span>
        <p class="owl-tip-pl">{esc(p["tip_pl"])}</p>
        <span class="owl-tip-ua ua">{esc(p["tip_ua"])}</span>
      </aside>
    </header>

    {hero}

    <section class="topic-lead">
      <span class="label">Na tej stronie / На цій сторінці</span>
      <p>{esc(p["intro_pl"])}</p>
      <p class="ua">{esc(p["intro_ua"])}</p>
      {howto_html}
    </section>

    <section class="life-strip">
      {life_media}
      <div>
        <h3>W życiu / У житті</h3>
        <p>{esc(p.get("life_pl") or meta["life_pl"])}</p>
        <span class="ua">{esc(p.get("life_ua") or meta["life_ua"])}</span>
      </div>
    </section>

    <section class="cards">
      {cards}
    </section>

    {mistake_html}

    {wordwall_html}

    {cheat_html}

    <footer class="page-footer">
      <div class="page-footer-bar">
        <div>{p["cat"]} • {esc(p["cat_pl"])} / {esc(p["cat_ua"])}</div>
        <div class="center">{p["n"]}</div>
        <div class="right">Mini-słownik matematyki PL-UA</div>
      </div>
      <div class="site-copyright">
        <p>© 2026 <strong>EduMost</strong>. Wszelkie prawa zastrzeżone. / Усі права захищені.</p>
        <p class="site-copyright-note">Kopiowanie, udostępnianie i sprzedaż bez pisemnej zgody autora są zabronione. · Копіювання, поширення та продаж без письмової згоди автора заборонені.</p>
        <p class="site-copyright-links"><a href="{asset_prefix}regulamin.html">Regulamin</a> · <a href="{asset_prefix}rodo.html">Polityka prywatności / RODO</a></p>
      </div>
    </footer>
'''


def page_html(p, prev_f, next_f):
    prev = f'<a href="{prev_f}">← Poprzednia</a>' if prev_f else "<span></span>"
    nxt = f'<a href="{next_f}">Następna →</a>' if next_f else "<span></span>"
    body = chapter_body(p, asset_prefix="../")

    return f'''<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <meta name="theme-color" content="#1e4f9c" />
  <title>{esc(p["title_pl"])} — Mini-słownik matematyki PL-UA</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../style.css" />
  <link rel="stylesheet" href="../media.css" />
</head>
<body class="page-body cat-{p["cat"]}">
  <main class="page" id="print-root">
    <div class="page-nav no-print">
      <div class="page-nav-start">
        <a class="site-logo" href="../index.html" aria-label="EduMost">
          <img src="../assets/logo.png" alt="EduMost" width="160" height="36" />
        </a>
        <a href="../index.html">⌂ Spis</a>
      </div>
      <div class="nav-actions">
        <button type="button" class="btn-print" data-print>🖨 PDF</button>
        <a class="btn-book" href="../book.html">📚 Książka</a>
        {prev}{nxt}
      </div>
    </div>
    {body}
  </main>
  <div class="print-hint no-print">Drukuj → <strong>Zapisz jako PDF</strong></div>
  <script src="../script.js"></script>
</body>
</html>
'''


def book_html(pages_list):
    chapters = []
    toc_items = []
    for p in pages_list:
        body = chapter_body(p, asset_prefix="")
        # w książce ścieżki CSS są z roota; media placeholders OK
        # popraw linków w body nie trzeba — brak linków wewnętrznych
        chapters.append(
            f'<article class="book-chapter cat-{p["cat"]}" id="rozdzial-{p["n"]:02d}">\n'
            f'{body}\n</article>'
        )
        toc_items.append(
            f'<li><a href="#rozdzial-{p["n"]:02d}">'
            f'<span class="toc-n">{p["n"]:02d}</span> {esc(p["title_pl"])} '
            f'<em>{esc(p["title_ua"])}</em></a></li>'
        )

    return f'''<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <meta name="theme-color" content="#1e4f9c" />
  <title>Mini-słownik matematyki PL-UA — Książka PDF ({len(pages_list)} tematów)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="style.css" />
  <link rel="stylesheet" href="media.css" />
</head>
<body class="book-body">
  <div class="book-toolbar no-print">
    <div class="page-nav-start">
      <a class="site-logo" href="index.html" aria-label="EduMost">
        <img src="assets/logo.png" alt="EduMost" width="160" height="36" />
      </a>
      <a href="index.html">⌂ Spis treści</a>
    </div>
    <div class="nav-actions">
      <button type="button" class="btn-print btn-print-lg" data-print>
        🖨 PDF — 1 temat = 1 strona
      </button>
      <button type="button" class="btn-print btn-print-lg" data-print="compact" style="background:#0f766e">
        📄 PDF kompaktowy (mniej pustych miejsc)
      </button>
    </div>
  </div>

  <header class="book-cover no-print-keep">
    <div class="book-cover-inner">
      <p class="brand-mark"><span class="star">★</span> EduMost</p>
      <h1>Mini-słownik matematyki</h1>
      <p class="ua-title">Міні-довідник з математики</p>
      <p class="lead">{len(pages_list)} tematów · Polski ↔ Українська · Szkoła podstawowa</p>
      <p class="book-cover-hint no-print">
        <strong>PDF — 1 temat = 1 strona</strong> — czytelna książka (mogą zostać puste doły stron).<br/>
        <strong>PDF kompaktowy</strong> — tematy jeden za drugim, mniej pustego miejsca (zalecane).<br/>
        W oknie druku: <em>Zapisz jako PDF</em> · marginesy domyślne · <em>Grafika tła</em> włączona.
      </p>
      <div class="no-print" style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center">
        <button type="button" class="btn-print btn-print-lg" data-print>
          🖨 PDF — 1 temat = 1 strona
        </button>
        <button type="button" class="btn-print btn-print-lg" data-print="compact" style="background:#0f766e">
          📄 PDF kompaktowy
        </button>
      </div>
    </div>
  </header>

  <nav class="book-toc no-print">
    <h2>Spis rozdziałów</h2>
    <ol class="book-toc-list">
      {"".join(toc_items)}
    </ol>
  </nav>

  <div class="book-pages">
    {"".join(chapters)}
  </div>

  <p class="print-hint no-print">
    Tip: Chrome / Edge → Drukuj → <strong>Zapisz jako PDF</strong>.
    Dla gęstego pliku użyj zielonego przycisku <strong>PDF kompaktowy</strong>.
    Włącz „Grafika tła”, aby zachować kolory.
  </p>
  <script src="script.js"></script>
</body>
</html>
'''


pages = PAGES

for i, p in enumerate(pages):
    prev_f = pages[i - 1]["file"] if i > 0 else None
    next_f = pages[i + 1]["file"] if i < len(pages) - 1 else None
    (PAGES_DIR / p["file"]).write_text(page_html(p, prev_f, next_f), encoding="utf-8")

(ROOT / "book.html").write_text(book_html(pages), encoding="utf-8")

CAT_NAMES = {
    "A": ("LICZBY", "ЧИСЛА", "#1e4f9c"),
    "B": ("DZIAŁANIA", "ДІЇ", "#2e9b57"),
    "C": ("UŁAMKI", "ДРОБИ", "#e67e22"),
    "D": ("GEOMETRIA", "ГЕОМЕТРІЯ", "#7b4db8"),
    "E": ("MIARY", "ВЕЛИЧИНИ", "#1a9b9b"),
    "F": ("DANE", "ДАНІ", "#d14f8a"),
}

cards_html = []
for p in pages:
    accent = CAT_NAMES[p["cat"]][2]
    cat_pl, cat_ua = CAT_NAMES[p["cat"]][0], CAT_NAMES[p["cat"]][1]
    cards_html.append(f'''
    <a class="toc-card" href="pages/{p["file"]}" data-cat="{p["cat"]}" style="--accent:{accent}">
      <div class="toc-num">{p["n"]:02d}</div>
      <div>
        <h3>{esc(p["title_pl"])}</h3>
        <p class="ua">{esc(p["title_ua"])}</p>
        <p class="about">{esc(p["intro_pl"])}</p>
        <span class="tag">{p["cat"]} · {cat_pl} / {cat_ua}</span>
      </div>
    </a>''')

index = f'''<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <meta name="theme-color" content="#1e4f9c" />
  <title>Mini-słownik matematyki PL-UA — EduMost</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="style.css" />
  <link rel="stylesheet" href="media.css" />
</head>
<body>
  <header class="hero">
    <div class="wrap">
      <div class="brand">
        <div class="brand-mark"><span class="star">★</span> EduMost</div>
        <span class="pill">POLSKI ↔ УКРАЇНСЬКА</span>
      </div>
      <h1>MINI-SŁOWNIK MATEMATYKI — DLA SZKOŁY PODSTAWOWEJ</h1>
      <p class="ua-title">МІНІ-ДОВІДНИК З МАТЕМАТИКИ — ДЛЯ ПОЧАТКОВОЇ ШКОЛИ</p>
      <p class="lead">
        {len(pages)} tematów: co to jest, jak w szkole, przykład.
        Jedną stronę lub <strong>całą książkę</strong> zapiszesz jako PDF.
      </p>
      <div class="hero-cta no-print">
        <a class="btn-print btn-print-lg" href="book.html">📚 Książka PDF — wszystkie {len(pages)} tematów</a>
      </div>
      <div class="features">
        <div class="feature"><strong>📚 1 PDF</strong>Cała książka jednym plikiem</div>
        <div class="feature"><strong>📱 Telefon</strong>Wygodnie na mobile</div>
        <div class="feature"><strong>🎨 Obrazki</strong>Ilustracje do haseł i przykładów</div>
        <div class="feature"><strong>🇺🇦 PL+UA</strong>Szkolny język + wsparcie</div>
        <div class="feature"><strong>🖨 Druk</strong>Strona lub całość</div>
      </div>
    </div>
  </header>

  <section class="toc-section">
    <div class="wrap">
      <div class="toc-head">
        <div>
          <h2>Spis treści / Зміст</h2>
          <p><a href="book.html">→ Otwórz książkę i zapisz PDF</a></p>
        </div>
        <label class="search">🔎 <input id="toc-search" type="search" placeholder="Szukaj tematu…" inputmode="search" /></label>
      </div>
      <div class="cat-filters" role="toolbar" aria-label="Filtry">
        <button class="cat-btn active" data-cat="all" type="button">Wszystkie</button>
        <button class="cat-btn" data-cat="A" type="button">A Liczby</button>
        <button class="cat-btn" data-cat="B" type="button">B Działania</button>
        <button class="cat-btn" data-cat="C" type="button">C Ułamki</button>
        <button class="cat-btn" data-cat="D" type="button">D Geometria</button>
        <button class="cat-btn" data-cat="E" type="button">E Miary</button>
        <button class="cat-btn" data-cat="F" type="button">F Dane</button>
      </div>
      <div class="toc-grid">{"".join(cards_html)}</div>
    </div>
  </section>
  <footer class="site-footer">
    <p class="site-footer-tagline">ZROZUM ★ ZAPAMIĘTAJ ★ DZIAŁAJ · 7–12 lat</p>
    <div class="site-copyright">
      <p>© 2026 <strong>EduMost</strong>. Wszelkie prawa zastrzeżone. / Усі права захищені.</p>
      <p class="site-copyright-note">Kopiowanie, udostępnianie i sprzedaż bez pisemnej zgody autora są zabronione. · Копіювання, поширення та продаж без письмової згоди автора заборонені.</p>
      <p class="site-copyright-links"><a href="regulamin.html">Regulamin</a> · <a href="rodo.html">Polityka prywatności / RODO</a></p>
    </div>
  </footer>
  <script src="script.js"></script>
</body>
</html>
'''
(ROOT / "index.html").write_text(index, encoding="utf-8")
print(f"OK: {len(pages)} pages + index + book.html")
