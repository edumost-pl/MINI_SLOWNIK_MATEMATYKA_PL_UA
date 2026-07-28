# Raport końcowy przebudowy (2026-07-28)

## Cel
Przestawienie tematów (Faza A) + nowe strony (rozdzielenia / braki P1) **bez utraty** Wordwall, nawigacji i treści kart.

## Wynik liczbowy

| Metryka | DO | PO |
|---------|----|----|
| Strony `pages/page*.html` | 61 | **75** |
| Wordwall iframe (live) | 58 | **58** (100% zachowane, także w `book.html`) |
| Brakujące obrazy (refy) | 25 | **0** |
| Martwe linki plików | 10 | **0** |
| Błędy HTML (stylesheet/script) | 2 | **0** |

Audyt: `python3 docs/audit_integrity.py` → broken=0, missing images=0.

## Co zmieniono

### 1. Faza A — kolejność (treść kart bez zmian)
- `structure_apply.py` — mapa stary→nowy
- Obrazy: `asset_n` = stary numer (ścieżki `imgXX_*` działają)
- Wordwall: `wordwall_embeds.py` po `source_n` — **58/58** URL
- Build wstawia **iframe** (wcześniej ginęły przy rebuildzie)

Pierwsza strona spisu: **Stosunki przestrzenne** (było 61).  
Procenty / proporcje zebrane w bloku ułamków; algebra po nich; geometria → bryły → miary → dane; ściąga na końcu bloku 1–61.

### 2. Nowe strony (stare **nie usunięte**)

| Nr | Temat | Powód |
|----|-------|-------|
| 62 | Walec | split z „walec/stożek/kula” |
| 63 | Stożek | j.w. |
| 64 | Kula i sfera | j.w. + sfera |
| 65 | Ostrosłup — pole i objętość | V/P (7–8) |
| 66 | Nierówności | brak P1 |
| 67 | Przekształcanie wzorów | brak P1 |
| 68 | Wielokąt foremny | brak P1 |
| 69 | Podobieństwo figur | brak P1 |
| 70 | Okręgi wpisane i opisane | brak P1 |
| 71 | Przekształcenia geometryczne | brak P1 |
| 72 | Liczby wymierne | brak P1 |
| 73 | Środkowa w trójkącie | brak P1 |
| 74 | Prawdopodobieństwo | osobna strona (s.41 zostaje) |
| 75 | Skala mapy | osobna strona (s. prędkość zostaje) |

### 3. Naprawy techniczne
- `docs/howto-obrazy.html` — ścieżki `../`
- `regulamin.html` — `demo/` → `index.html`
- Uzupełnione brakujące `img*_N.png` (kopia sąsiedniego slotu)
- CSS: `.page-wordwall-embed`

## Potwierdzenie funkcjonalności
- ✓ 58 embedów Wordwall = mapa źródłowa (pages + book)
- ✓ Nawigacja prev/next + spis (`index.html`) dla 75 stron
- ✓ `script.js` (TOC, print, zoom) — bez zmian selektorów
- ✓ Karty istniejących tematów — bez edycji tekstów (tylko kolejność / meta)

## Pliki kluczowe
- `structure_apply.py`, `wordwall_embeds.py`, `pages_new_extra.py`
- `pages_data.py` (extras + apply_phase_a)
- `build_pages.py` (iframe + asset_n)
