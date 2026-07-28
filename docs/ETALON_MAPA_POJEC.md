# Etalonowa mapa pojęć — Mini-słownik PL–UA

**Status:** mapa treści (bez zmiany numerów stron / HTML)  
**Data:** 2026-07-28  
**Pytanie sterujące:** *Jakie matematyczne pojęcia powinien znaleźć uczeń klas 1–8, gdy otworzy ten słownik?*

---

## 0. Cel produktu (kanon)

To **nie** jest podręcznik i **nie** kopiuje układu lekcji.

| Priorytet | Znaczenie |
|-----------|-----------|
| **1. Znajdowalność pojęcia** | Uczeń słyszy słowo na lekcji → w ≤ 1–2 min ma hasło PL + UA |
| **2. Pokrycie terminów** | Liczy się % pojęć z etalonu, **nie** liczba stron |
| **3. Jedno hasło = jedno samodzielne pojęcie** | Jeśli strona zbija wiele niezależnych terminów — plan rozdzielenia w kolejnej wersji |
| **4. Kolejność stron** | Dopiero po zamknięciu mapy pojęć (nawigacja / działy / spis) |

Źródło etalonu SP: *podstawa programowa matematyki* (MEN/ZPE, klasa 1–3 + 4–8, stan 2024/25) + typowe słownictwo lekcyjne podręczników.  
Dział **I (most)** = pojęcia *poza* wąskim rdzeniem PP (liceum / kółko) — śledzone osobno, **nie** liczone do 100% SP.

Dane maszynowe: `docs/etalon_terms_map.json` (244 hasła etalonowe).

---

## 1. Pokrycie — wynik

| Zbiór | Liczba | Covered (osobne hasło) | Partial (jest, ale w bundlu / za cienko) | Missing |
|-------|--------|------------------------|------------------------------------------|---------|
| **SP (A–H + J)** | **237** | **213 (89,9%)** | **9 (3,8%)** | **15 (6,3%)** |
| + most (I / liceum) | 244 | 213 | 9 | 15 + 7 most |

| Metryka | Wartość |
|---------|---------|
| Soft coverage SP (covered + partial) | **93,7%** |
| Strict findability SP (tylko covered) | **89,9%** |
| Do **100% findability SP** | **24 pojęcia** (15 missing + 9 partial → rozdzielić / dopisać) |

**Cel produktowy:** 100% = każde pojęcie ze zbioru SP ma **własne, wyszukiwalne hasło** (karta lub krótka strona), nie „wspomniane w tekście innej karty”.

---

## 2. Braki (missing) — co dopisać

| PL | UA | Klasy | Dział | Dokąd logicznie |
|----|----|-------|-------|-----------------|
| liczba wymierna | раціональне число | 7–8 | A | nowa strona *Liczby wymierne* (obok całkowitych / ułamków) |
| nierówność | нерівність | 7–8 | D | nowa strona *Nierówności* (obok równań, s. 19) |
| rozwiązanie nierówności | розв'язок нерівності | 7–8 | D | ta sama strona *Nierówności* |
| przekształcanie wzoru | перетворення формули | 7–8 | D | nowa strona / hasła przy równaniach + prędkość (s. 19, 27) |
| wielokąt foremny | правильний многокутник | 7–8 | E | nowa strona lub hasło przy wielokątach (s. 28–29) |
| środkowa trójkąta | медіана трикутника | 6–8 | E | strona *Wysokość, środkowa, dwusieczna w trójkącie* (obok s. 60) |
| podobieństwo figur | подібність фігур | 7–8 | E | nowa strona po przystawaniu (s. 58) |
| skala podobieństwa | коефіцієнт подібності | 7–8 | E | ta sama strona *Podobieństwo* |
| okrąg wpisany | вписане коло | 7–8 | E | nowa strona *Okręgi wpisane i opisane* (po kole, s. 30) |
| okrąg opisany | описане коло | 7–8 | E | ta sama |
| przesunięcie | паралельне перенесення | 7–8 | E | nowa strona *Przekształcenia* (obok symetrii, s. 37) |
| obrót (przekształcenie) | поворот (перетворення) | 7–8 | E | ta sama |
| sfera | сфера | 7–8 | F | przy *kula* (po rozdzieleniu s. 36) |
| objętość ostrosłupa | об'єм піраміди | 7–8 | F | osobna strona *Ostrosłup* (dziś tylko rozpoznanie na s. 36) |
| pole powierzchni ostrosłupa | площа поверхні піраміди | 7–8 | F | ta sama |

---

## 3. Partial — rozdzielić / wzmocnić hasła

| PL | Teraz | Problem | Plan |
|----|-------|---------|------|
| liczba dodatnia / ujemna | 03 · „dodatnie, ujemne, zero” | dwa pojęcia + zero w jednej karcie | 3 osobne hasła na s. 03 (lub mini-strona) |
| łączność | 04 · „właściwości +” | słabo wyszukiwalne | osobne hasło *łączność* |
| trójkąt równoboczny | 29 · „rodzaje trójkątów” | schowane w „rodzajach” | osobne hasło |
| ostrosłup | 36 | tylko rozpoznanie; brak V/P | osobna strona 7–8 |
| walec | 36 · „walec / stożek / kula” | **3 bryły w 1 karcie** | 3 hasła / 3 strony |
| stożek | 36 | j.w. | j.w. |
| kula | 36 | j.w. | j.w. (+ sfera) |
| doświadczenie losowe | 41 | schowane w prawdopodobieństwie | osobne hasło |

---

## 4. Strony „grube” — kandydaci do podziału w następnej wersji

Orientacja: *czy uczeń szukający jednego słowa trafia w stronę z 5+ niezależnymi pojęciami?*

| Strona | Tytuł | Dlaczego dzielić | Propozycja rozbicia (kolejna wersja) |
|--------|-------|------------------|--------------------------------------|
| **36** | Bryły | `walec/stożek/kula` + ostrosłup bez wzorów | Sześcian & prostopadłościan · Ostrosłup · Walec · Stożek · Kula/sfera |
| **29** | Figury płaskie (2) | wiele figur + rodzaje trójkątów | Trójkąty (rodzaje) · Czworokąty (kwadrat…trapez) |
| **41** | Kombinatoryka i prawdopodobieństwo | dwa działy PP | Kombinatoryka · Prawdopodobieństwo |
| **34** | Pary kątów / kąty przy ∥ | pary lokalne + kąty przy równoległych | Kąty przyległe i wierzchołkowe · Kąty przy prostych równoległych |
| **27** | Prędkość i skala | dwa konteksty praktyczne | Prędkość · Skala mapy |
| **50** | Pole rombu i trapezu; ar, ha | wzory + jednostki | Pole rombu i trapezu · Jednostki pola (ar, ha) |
| **01** | Liczby naturalne | 11 kart, gęsto | opcjonalnie: wartość pozycyjna / zaokrąglanie jako osobne krótkie strony |
| **42** | Ściąga znaków | wiele symboli | **nie dzielić** — to indeks, nie lekcja |

*Antonimiczne pary* (`parzysta/nieparzysta`, `prawo/lewo`) mogą zostać na jednej karcie — to **jedno** wyszukiwanie „rodzaj porównania”, nie trzy niezależne bryły.

---

## 5. Most (poza 100% SP) — świadomie osobno

PP (komentarz realizacji): *funkcja / monotoniczność — nie wprowadzać formalnie w SP*.  
Sin / cos / tg — **liceum**, nie rdzeń egzaminu ósmoklasisty.

| PL | UA | Status |
|----|----|--------|
| funkcja | функція | missing · most |
| wykres funkcji | графік функції | missing · most |
| sinus / cosinus / tangens | синус / косинус / тангенс | missing · most |
| układ równań | система рівнянь | missing · most |
| liczba niewymierna | ірраціональне число | missing · most |

Jeśli kiedyś dodawać — dział **I Most do szkoły średniej**, wyraźnie oznaczony, **bez** wliczania do „100% SP”.

---

## 6. Jak organizować działy (dla wyszukiwania, nie dla podręcznika)

Działy = **klastry nazw**, żeby spis i filtry pomagały znaleźć hasło:

| Litera | Klaster | Po co w słowniku |
|--------|---------|------------------|
| A | Liczby i orientacja | słowa o liczbach i przestrzeni |
| B | Działania | + − × : , potęgi, pierwiastki, NWD… |
| C | Ułamki, procenty, proporcje | wszystko „część / % / stosunek” |
| D | Algebra | litera, równanie, nierówność |
| E | Geometria płaska | figury, kąty, pole, Pitagoras… |
| F | Bryły | osobne nazwy brył |
| G | Miary | długość, czas, pieniądze… |
| H | Dane | wykres, średnia, P |
| I | Most (opc.) | poza SP |
| J | Symbole / ściąga | szybki indeks znaków |

**Numeracja stron** — dopiero gdy mapa pojęć (sekcje 2–3) jest domknięta. Teraz **nie zmieniamy** numerów.

---

## 7. Droga do 100% findability SP

1. **Dopisać 15 missing** (sekcja 2) — nowe hasła / krótkie strony.  
2. **Rozdzielić 9 partial** (sekcja 3) — zwłaszcza `walec/stożek/kula` i ostrosłup V/P.  
3. **Opcjonalnie** rozbić „grube” strony z sekcji 4 (wygoda, nie warunek 100%).  
4. Dopiero potem: spis, filtry, ewentualna renumeracja.

Po krokach 1–2: **strict ≈ 100%** na zbiorze 237 pojęć SP tej mapy.

---

## 8. Uwaga o kompletności mapy

244 hasła to **rdzeń lekcyjny** (to, co uczeń słyszy w SP + świadomy most).  
Pełny „leksykon wszystkich wariantów nazw” (np. osobno *km/h*, *dag*, *kąt zerowy* już covered…) można rozszerzać — ale **metryka 100%** odnosi się do zamkniętej listy w `etalon_terms_map.json`.  
Rozszerzanie listy = nowa wersja etalonu + ponowny pomiar, nie „nieskończony podręcznik”.
