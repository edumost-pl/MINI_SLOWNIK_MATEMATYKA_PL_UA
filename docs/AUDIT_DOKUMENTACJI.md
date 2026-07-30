# Audyt dokumentacji technicznej — EduMost (Mini-słownik matematyki PL–UA)

**Data:** 2026-07-29  
**Zakres:** cały repozytorium dokumentacji + zgodność z aktualnym kodem  
**Zasada:** ten raport **nie usuwa** plików — tylko rekomendacje. Usuwanie dopiero po akceptacji autora.

---

## 0. Prawda o projekcie (stan aktualny)

| Warstwa | Stan |
|---------|------|
| Produkt | Statyczny mini-słownik PL–UA, SP kl. 1–8 |
| Strony | **75** (`pages/page01.html` … `page75.html`) |
| Karty | **~429** haseł |
| Build | `python3 build_pages.py` → `pages/`, `index.html`, `book.html` |
| Dane | `pages_data.py` + `pages_new_*.py` → `handbook_enrich` → `structure_apply` |
| UX | `card_ux.py`, `page_summary_ux.py`, `examples_bank.py` |
| Wordwall | `wordwall_embeds.py` — **58** iframe (po `source_n`) |
| Backend / DB / API | **Brak** — tylko HTML/CSS/JS |
| README w root | **Brak** |
| LICENSE / CONTRIBUTING / AGENTS | **Brak** |

---

## 1. Statystyka ogólna

| Metryka | Liczba |
|---------|--------|
| **Dokumenty przeanalizowane** (md/json/html/txt/csv w `docs/` + `ocr/*.txt` jako źródła) | **68** |
| — w tym `docs/` | **25** |
| — w tym `ocr/*.txt` | **43** |
| **Używane / częściowo aktualne** | **10** |
| **Przestarzałe** | **18** (`docs`) + **43** (`ocr`, archiwum źródłowe) |
| **Duplikaty / nakładające się** | **6 grup** |
| **Rekomendowane do usunięcia** | **17 plików w `docs/`** (+ opcjonalnie archiwizacja `ocr/`) |
| **Rekomendowane do połączenia** | **4 pary/grupy** |
| **Brakujące dokumenty obowiązkowe** | README (+ opcjonalnie LICENSE) |

*Uwaga:* `ocr/` to zrzuty OCR ze skanów — nie „żywa” dokumentacja produktowa, ale surowiec historyczny.

---

## 2. Tabela — każdy dokument

### 2.1. `docs/*.md`

| Dokument | Używany? | Powód | Działanie |
|----------|----------|-------|-----------|
| `METODOLOGIA.md` | CZĘŚCIOWO | Kanon produktu (cel, karta, PP) nadal ważny; liczby **60 tematów / ~359 pojęć** nieaktualne | **Aktualizować** |
| `DLA_PROGRAMISTY.md` | CZĘŚCIOWO | Build i model danych w duchu OK; brak `structure_apply`, `pages_new_extra`, Wordwall, UX trio; „OK: 60 pages” | **Aktualizować** |
| `ETALON_MAPA_POJEC.md` | CZĘŚCIOWO | Model „mapa pojęć” nadal kanoniczny; lista braków sprzed stron 62–75 | **Aktualizować** |
| `NOWA_STRUKTURA.md` | NIE | Napisany jako *szkic bez wdrożenia* — Faza A **już wdrożona**; zawiera plany liceum (Faza B) | **Usunąć** lub **Przenieść** do `docs/archive/` po skróceniu |
| `RAPORT_PRZEBUDOWA.md` | TAK | Zgodny ze stanem 75 stron / 58 embedów | **Zostawić** |
| `RAPORT_PRZEGLAD_MERYTORYCZNY.md` | TAK | Przegląd 75 stron; sekcja „decyzje autora” częściowo już rozstrzygnięta | **Aktualizować** (domknąć decyzje) |
| `RESOURCE_MAP.md` | NIE | Baseline **przed** rebuildem (61 stron, GATE=FALSE, 25 missing images) — wszystko naprawione | **Usunąć** |
| `WORDWALL_ZADANIA.md` | CZĘŚCIOWO | Scenariusze quizów S01–S61; nie w buildzie; numeracja = stary `source_n` | **Zostawić** jako materiał autorski **albo** przenieść do `docs/content/wordwall/` |
| `POLSKI_MAPA_PP.md` | NIE | Stub „przeniesione do innego repo” | **Usunąć** |
| `POLSKI_UWAGA.md` | NIE | Duplikat stubu polskiego | **Usunąć** |

### 2.2. `docs/*.json` / csv / txt / html / py

| Dokument | Używany? | Powód | Działanie |
|----------|----------|-------|-----------|
| `etalon_terms_map.json` | CZĘŚCIOWO | Mapa maszynowa etalonu; **nie importowana** przez build; statusy braków stare | **Aktualizować** (przeliczyć pokrycie) |
| `WORDWALL_EMBED_MAP.json` | NIE | Snapshot 61 plików; żywe źródło = `wordwall_embeds.py` | **Usunąć** (lub archive) |
| `INTEGRITY_BASELINE.json` | TAK | Artefakt `audit_integrity.py` (nadpisywany) | **Zostawić**; rozważyć `.gitignore` |
| `REVIEW_MERITORYCZNY.json` | NIE | Duplikat raportu MD | **Usunąć** |
| `missing_images.json` | NIE | Kolejka AI (~397) — dziś **0** missing images | **Usunąć** |
| `missing_images_queue.json` | NIE | Wariant powyższego | **Usunąć** |
| `gen_chunk_0.json` … `gen_chunk_4.json` | NIE | Jednorazowe batche promptów obrazów | **Usunąć** (5 plików) |
| `_all_terms.txt` | NIE | Eksport 374 haseł; kod nie czyta; żywo ~429 | **Usunąć** |
| `WORDWALL_ZADANIA.csv` | CZĘŚCIOWO | To samo co MD, do importu Wordwall | **Scalić** z MD (zostawić CSV *albo* MD) |
| `howto-obrazy.html` | CZĘŚCIOWO | Przewodnik obrazów; niepodlinkowany ze strony; sprzeczność „edytuj HTML ręcznie” vs generator | **Aktualizować** + **Przenieść** |
| `audit_integrity.py` | TAK | Narzędzie audytu (kod, nie „proza”) | **Zostawić**; poprawić liczenie iframe Wordwall |

### 2.3. `ocr/*.txt` (43 pliki)

| Dokument | Używany? | Powód | Działanie |
|----------|----------|-------|-----------|
| `ocr/*.txt` | NIE (runtime) | Surowy OCR ze skanów PDF/PNG; build ich nie czyta | **Przenieść** do `archive/ocr/` lub osobne archiwum; **nie** w żywej `docs/` |

### 2.4. Braki (nie istnieją, a powinny)

| Dokument | Status | Działanie |
|----------|--------|-----------|
| `README.md` (root) | Brak | **Utworzyć** (krótki: produkt, build, linki do docs) |
| `LICENSE` | Brak | Decyzja autora |
| Roadmap / TODO plik | Brak osobnego pliku | Roadmap żyje w `NOWA_STRUKTURA` (przestarzały) → nowy krótki `docs/ROADMAP.md` **tylko** z realnymi planami |
| DB / API docs | N/A | Projekt **nie ma** bazy ani API — **nie tworzyć** pustej dokumentacji |

---

## 3. Duplikaty (grupy)

| Temat | Pliki | Rekomendacja |
|-------|-------|--------------|
| Struktura / przebudowa | `NOWA_STRUKTURA`, `RESOURCE_MAP`, `ETALON_*`, `RAPORT_PRZEBUDOWA` | Kanoniczny: **RAPORT_PRZEBUDOWA** + zaktualizowany **ETALON**; resztę usunąć/archiwizować |
| Przegląd merytoryczny | `RAPORT_PRZEGLAD_*.md` + `REVIEW_*.json` | Zostawić **MD**; usunąć JSON |
| Wordwall | `WORDWALL_ZADANIA.md` + `.csv` + `EMBED_MAP.json` + `wordwall_embeds.py` | Kod = źródło URL; zostawić **jeden** format scenariuszy (MD *lub* CSV) |
| Generacja obrazów | `missing_images*.json` + `gen_chunk_*.json` | Usunąć wszystkie |
| Stub PL | `POLSKI_*.md` | Usunąć oba; 1 zdanie w README |

---

## 4. Aktualność vs kod

### Opisane, a już nieprawdziwe

- „60 / 61 stron” w `METODOLOGIA`, `DLA_PROGRAMISTY`, `RESOURCE_MAP`, `NOWA_STRUKTURA`
- `GATE rebuild_allowed = FALSE` i 25 brakujących obrazów / 10 martwych linków (`RESOURCE_MAP`)
- „bez wdrożenia numerów” (`NOWA_STRUKTURA`) — Faza A wdrożona
- Otwarte decyzje autora w `RAPORT_PRZEGLAD` (permutacje, sfera, √2…) — **już rozstrzygnięte** w kodzie
- `howto-obrazy`: ręczne edycje HTML — przeczą generatorowi

### W kodzie, a nieopisane

- `structure_apply.py` (`asset_n` / `source_n`)
- `pages_new_extra.py` (strony 62–75)
- `wordwall_embeds.py`
- `card_ux.py` / `page_summary_ux.py` / `examples_bank.py`
- Pipeline UX karty (Co to jest / Zapamiętaj / Nie pomyl / Przykłady)

### DB / API / ER

**Nie dotyczy** — brak warstwy danych serwerowych. Nie tworzyć sekcji „na zapas”.

---

## 5. Linki

| Wynik | Szczegóły |
|-------|-----------|
| Martwe linki plików w HTML produktu | **0** (`audit_integrity`) |
| Linki MD `docs/` → istniejące pliki | OK (`ETALON`, `METODOLOGIA` ↔ `DLA_PROGRAMISTY`) |
| `docs/` w nawigacji publicznej | **Brak** — dokumentacja nie jest podlinkowana z `index.html` |
| Embedy Wordwall | 58 iframe; audyt czasem liczy tylko `<a class=wordwall>` → **fałszywe „live 0”** |

---

## 6. README

**Brak pliku.** To największa luka onboardingowa.

Proponowana zawartość (krótko):

1. Co to jest (1 akapit)  
2. Wymagania: Python 3  
3. Build: `python3 build_pages.py`  
4. Otwórz: `index.html` / `book.html`  
5. Gdzie treść: `pages_data.py`, …  
6. Linki: `docs/METODOLOGIA.md`, `docs/DLA_PROGRAMISTY.md`  
7. Audyt: `python3 docs/audit_integrity.py`

---

## 7. Roadmap

Źródło historyczne: `NOWA_STRUKTURA.md` (Faza B → ~100–120 stron, sin/cos, liceum).

| Plan | Status | Rekomendacja |
|------|--------|--------------|
| Faza A (kolejność) | **Zrobione** | Nie trzymać jako „plan” |
| Strony 62–75 | **Zrobione** | — |
| Wordwall 58 zachowane | **Zrobione** | — |
| Faza B / liceum / ~120 stron | Świadomie poza SP | **Usunąć z roadmapy** (lub „won’t do”) |
| Wordwall dla stron 62–75 | Realne | **Zostawić** w nowym ROADMAP |
| Odświeżenie etalonu po 75 stronach | Realne | **Zostawić** |
| README + porządek docs | Realne (ten audyt) | **Zostawić** |

---

## 8. Dług techniczny w dokumentacji / artefaktach

| Element | Problem | Działanie |
|---------|---------|-----------|
| Root `0.pdf`, `1_….png` … `42_….png` | Surowe skany obok kodu (~180 MB) | Poza `docs/`, ale warto `archive/sources/` |
| `ocr/` | 43 OCR | Archiwum |
| `INTEGRITY_BASELINE` gate zawsze false | Mylące | Poprawić skrypt |
| `__pycache__/` | Śmieci build | `.gitignore` |
| Brak README | Onboarding | Utworzyć |

---

## 9. Proponowana docelowa struktura (minimalna)

```text
README.md                          # NOWE — wejście do projektu

docs/
  METODOLOGIA.md                   # produkt, karta, PP (zaktualizowane)
  DLA_PROGRAMISTY.md               # build, pipeline, moduły (zaktualizowane)
  ETALON_MAPA_POJEC.md             # mapa pojęć (zaktualizowana)
  etalon_terms_map.json            # dane etalonu (przeliczone)
  ROADMAP.md                       # NOWE — tylko otwarte plany
  RAPORT_PRZEBUDOWA.md             # historia przebudowy 61→75
  RAPORT_PRZEGLAD_MERYTORYCZNY.md  # przegląd treści (domknięty)
  howto-obrazy.html                # przewodnik assetów
  audit_integrity.py               # narzędzie
  INTEGRITY_BASELINE.json          # artefakt (opcjonalnie gitignore)
  content/
    WORDWALL_ZADANIA.md            # LUB .csv — jeden format
  archive/                         # opcjonalnie, po akceptacji
    ...                            # to, co dziś rekomendujemy usunąć
```

**Nie tworzyć** pustych `api/`, `database/`, `backend/` — nie ma takiej warstwy.

---

## 10. Rekomendowana kolejność działań (po akceptacji)

1. **Usunąć** (po Twoim „OK”):  
   `POLSKI_*.md`, `RESOURCE_MAP.md`, `REVIEW_MERITORYCZNY.json`, `missing_images*.json`, `gen_chunk_*.json`, `_all_terms.txt`, `WORDWALL_EMBED_MAP.json`  
2. **Zdecydować:** `NOWA_STRUKTURA.md` → delete vs `archive/`  
3. **Zdecydować:** Wordwall — zostawić `.md` **lub** `.csv` (nie oba)  
4. **Zaktualizować:** `METODOLOGIA.md`, `DLA_PROGRAMISTY.md`, `ETALON_*`, `RAPORT_PRZEGLAD`  
5. **Utworzyć:** `README.md`, krótki `docs/ROADMAP.md`  
6. Opcjonalnie: przenieść `ocr/` + skany root do `archive/`

---

## 11. Werdykt

Dokumentacja **nie jest w stanie profesjonalnym**: brak README, wiele artefaktów sprzed przebudowy, sprzeczne liczby stron (60/61 vs 75), roadmapa z planami liceum, zero warstwy DB/API (i nie trzeba jej dokumentować).

**Rdzeń do utrzymania (po update):**  
`METODOLOGIA` · `DLA_PROGRAMISTY` · `ETALON` (+ json) · `RAPORT_PRZEBUDOWA` · `RAPORT_PRZEGLAD` · `howto-obrazy` · `audit_integrity` · (Wordwall content) · **nowy README**.

---

**Następny krok:** napisz, które pozycje z sekcji 10 akceptujesz do usunięcia/archiwizacji — wtedy wykonam zmiany bez „sprzątania na zapas”.
