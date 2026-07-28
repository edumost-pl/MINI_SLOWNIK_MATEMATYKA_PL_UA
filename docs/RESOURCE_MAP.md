# Mapa zasobów + baseline integralności

**Data:** 2026-07-28  
**Status:** `GATE rebuild_allowed = FALSE`  
**Zasada:** żadnej przebudowy / renumeracji, dopóki lista błędów nie zostanie zaakceptowana lub naprawiona.

Automatyczny audyt: `docs/audit_integrity.py` → `docs/INTEGRITY_BASELINE.json`  
Mapa embedów Wordwall: `docs/WORDWALL_EMBED_MAP.json`

---

## 1. Baseline — liczby DO (stan obecny)

| Zasób | DO |
|-------|----|
| Strony `pages/pageXX.html` | **61** |
| Pliki HTML (cały projekt) | 66 |
| Przyciski / linki `wordwall-link` | **63** (wszystkie `href="#"`, głównie `book.html`) |
| **Wordwall iframe (live embed)** | **58** |
| Unikalne URL Wordwall | **59** |
| Strony z sekcją `page-wordwall` | **61/61** |
| Strony z żywym iframe | **58/61** |
| Obrazy na dysku (png/jpg/svg/…) | **533** |
| Referencje `src`/`href` do obrazów | **1122** |
| Linki wewnętrzne (lokalne) | **2010** |
| Linki zewnętrzne | **255** |
| Inline SVG (`<svg>`) | **0** |
| Ikony w `assets/icons/` | **0** (folder pusty; brak refów w pages) |
| Audio | **0** |
| Video | **0** |
| CSS | `style.css` (+ ewentualnie inne) |
| JS | `script.js` |

### Wordwall — ważne

| Forma | Gdzie | Stan |
|-------|-------|------|
| `<iframe src="https://wordwall.net/...">` | `pages/pageXX.html` | **58 live** — to jest właściwy zasób do zachowania |
| `<a class="wordwall-link" href="#">` | głównie `book.html` (61× pending) | zaślepki, **bez** prawdziwego URL |
| Brak iframe | `page16`, `page42`, `page43` | sekcja jest, embedu nie ma |

**Ryzyko przebudowy:** `book.html` **nie zawiera** iframe’ów Wordwall. Po przebudowie trzeba albo skopiować embedy ze stron, albo świadomie zostawić book bez quizów. **Nie wolno zgubić 58 URL z `WORDWALL_EMBED_MAP.json`.**

---

## 2. Mapa zasobów (struktura)

```
MINI_SLOWNIK_MATEMATYKA_PL_UA/
├── index.html          # spis + filtr (#toc-search, .cat-btn, .toc-card)
├── book.html           # całość do druku (Wordwall = linki #, bez iframe)
├── regulamin.html
├── rodo.html
├── style.css
├── script.js           # TOC search, print modes, card zoom
├── pages/page01.html … page61.html
├── assets/
│   ├── images/         # ~486 PNG (hero/karty)
│   ├── icons/          # PUSTY
│   ├── logo.png, logo-icon.png, logo-owl-circle.png, logo.svg
├── docs/
│   ├── INTEGRITY_BASELINE.json
│   ├── WORDWALL_EMBED_MAP.json
│   ├── ETALON_MAPA_POJEC.md
│   ├── audit_integrity.py
│   ├── howto-obrazy.html   # ścieżki względne zepsute po przeniesieniu
│   └── …
```

**Demo:** katalog `demo/` — **nie istnieje** (link z `regulamin.html` → `demo/index.html` jest martwy).

---

## 3. JavaScript — zależności (nie usuwać klas/id)

| Selektor / API | Rola |
|----------------|------|
| `#toc-search` | wyszukiwanie w spisie |
| `.cat-btn` + `data-cat` | filtr kategorii |
| `.toc-card` + `data-cat` + klasa `.hidden` | karty spisu |
| `[data-print]` | tryby druku (`compact` → `body.print-compact`) |
| `article.card`, `section.life-strip` | zoom bloku |
| `.card-zoom-overlay` / `.card-zoom-panel` / … | tworzone dynamicznie w JS (brak w HTML = OK) |
| `body.is-printing`, `body.card-zoom-open` | stany UI |

Inline `onclick`: **0**.  
Zdarzenia: `DOMContentLoaded`, `click`, `input`, `keydown` (Esc w zoom).

---

## 4. Błędy integralności (BLOKUJĄ przebudowę)

### 4.1 Martwe linki plików — **10**

| Plik | Ref | Problem |
|------|-----|---------|
| `docs/howto-obrazy.html` | `style.css`, `media.css` | po przeniesieniu do `docs/` ścieżki niepoprawne |
| `docs/howto-obrazy.html` | `index.html`, `pages/…`, `regulamin`, `rodo` | j.w. (brak `../`) |
| `regulamin.html` | `demo/index.html` | katalog `demo/` nie istnieje |

### 4.2 Brakujące obrazy — **25 refów / 13 unikalnych plików**

| Plik | Gdzie referowany |
|------|------------------|
| `img01_12.png`, `img01_13.png` | page01, book |
| `img04_12.png`, `img04_13.png` | page04, book |
| `img05_9.png` | page05, book |
| `img06_9.png` | page06, book |
| `img07_8.png` | page07, book |
| `img23_9.png` | page23, book |
| `img24_9.png` | page24, book |
| `img26_9.png` | page26, book |
| `img28_9.png` | page28, book |
| `img29_9.png` | page29, book |
| `assets/pizza.jpg` | tylko `docs/howto-obrazy.html` |

### 4.3 Problemy HTML — **2**

- `docs/howto-obrazy.html`: brakujące stylesheety (`style.css`, `media.css` względem `docs/`).

### 4.4 JavaScript

- Błędów runtime w audycie statycznym: **brak krytycznych**.
- Klasy `.card-zoom-*` „brak w HTML” — **oczekiwane** (JS je tworzy).

### 4.5 Inne (info, niekoniecznie blocker)

| Item | Stan |
|------|------|
| Orphan assets (niepodlinkowane) | `logo-icon.png`, `logo-owl-circle.png`, `logo.svg` |
| Duplikaty `id` w jednym pliku | 0 |
| Audio / video | brak |
| SVG inline | 0 (`logo.svg` jako plik) |
| Wordwall bez iframe | page16, page42, page43 |
| book vs pages Wordwall | **rozjazd** (book bez embedów) |

---

## 5. Raport porównawczy (szablon PO — jeszcze nie dotyczy)

Przebudowa **nie została zastosowana**. Po ewentualnej przyszłej zmianie wypełnić:

| Metryka | DO | PO | Δ |
|---------|----|----|---|
| Strony | 61 | — | — |
| Wordwall iframe | 58 | — | — |
| Wordwall linki `#` | 63 | — | — |
| Obrazy na dysku | 533 | — | — |
| Linki wewnętrzne | 2010 | — | — |

---

## 6. Decyzja GATE

```
rebuild_allowed: FALSE
```

**Powód:** znaleziono ≥1 niespójność (martwe linki + brakujące PNG + rozjazd Wordwall book/pages).

Zgodnie z regułą użytkownika:

> Jeśli znajdzie się choć jedno niespójnienie — **zatrzymać się**, wypisać błędy, **niczego nie stosować automatycznie**.

### Co wolno teraz (po potwierdzeniu)

1. Naprawić blocker’y (obrazy / howto / demo link / uzgodnić Wordwall w book), **albo**  
2. Świadomie zaakceptować listę jako znany dług techniczny i dopiero wtedy planować przebudowę **bez utraty** 58 embedów.

### Czego nie robić

- nie zmieniać numerów stron  
- nie dzielić tematów  
- nie usuwać HTML / kart / obrazów  
- nie regenerować `book.html` bez kopiowania mapy embedów
