# Nowa struktura Mini-słownika matematyki PL–UA

> **Aktualny kanon treści:** najpierw mapa **pojęć** (znajdowalność terminów), nie renumeracja stron.  
> → Patrz **[`ETALON_MAPA_POJEC.md`](./ETALON_MAPA_POJEC.md)** i `etalon_terms_map.json`.  
> Ten plik (kolejność stron) zostaje jako szkic nawigacji — **bez wdrożenia numerów**, dopóki etalon pojęć nie jest domknięty.

**Status:** szkic nawigacji (bez zmian HTML / numerów stron)  
**Data:** 2026-07-28  
**Zasada produktowa:** słownik do wyszukania pojęcia z lekcji — **nie** kopia układu podręcznika. Liczy się pokrycie terminów.

---

## 0. Werdykt metodyczny (krótko)

| Aspekt | Ocena |
|--------|--------|
| Pokrycie klas 1–6 | Bardzo dobre (~376 haseł, rdzeń PP) |
| Pokrycie klas 7–8 | Dobre w algebrze/ułamkach; **słabe rozbicie brył i pojęć „dużych”** (często w 1 karcie) |
| Kolejność obecna | **Nielogiczna** — bloki 43–61 dopięte „na końcu”, a nie w ciągu dydaktycznym |
| Rola produktu | Słownik pojęć na 1–2 minuty — **nie** podręcznik; kolejność = ścieżka wyszukiwania + naturalny rozwój pojęć |

**Główny problem kolejności:** strony 01–42 mają sensowny zarys, ale **43–61 to „doklejka chronologiczna”** (kolejność pisania, nie nauczania). Stąd skoki: po „Ściąga znaków” → działania pisemne; procenty rozbite (15 vs 52); proporcje (16 vs 56); bryły (36) vs graniastosłup (51); stosunki przestrzenne kl. 1–3 na pozycji **61**.

---

## 1. Co jest nie tak w obecnej kolejności

### 1.1 Skoki i rozjazdy

| Problem | Gdzie teraz | Dlaczego źle |
|---------|-------------|--------------|
| Stosunki przestrzenne na końcu | 61 | To fundament kl. 1–3 — powinno być **na początku** (przed/obok liczb i figur) |
| Działania pisemne / rozdzielność / NWD | 43–45 | Powinny iść **zaraz po** + − × : i podzielności, przed pełnym ciągiem ułamków |
| Potęgi i pierwiastki wbijają się w ułamki | 13–14 między 12 a 15 | Przerywają łańcuch: ułamki → % → proporcje |
| Algebra przed miarami i geometrią | 17–19 → 20–27 | Dla słownika tematycznego OK, ale **proporcje** (16) lądują w „działaniach” obok algebry — lepiej trzymać z % |
| Procenty rozcięte | 15 … 52 | Uczeń szuka „procent” — dwie odległe strony |
| Proporcje rozcięte | 16 … 56 | To samo |
| Geometria płaska ↔ bryły ↔ współrzędne pomieszane | 28–38, potem 48–51, 57–60 | Brak warstw: podstawy → kąty → pola → przekształcenia → Pitagoras → bryły |
| „Ściąga znaków” w środku danych | 42 | To **powtórzenie / ściąga** — koniec słownika |
| Doklejka 43–61 | po 42 | Największy skok dydaktyczny w projekcie |

### 1.2 Co jest OK

- Blok liczb 01–03 + działań 04–08 — rozsądny start.
- Ułamki 09–12 — dobry mini-ciąg.
- Miary 20–27 — spójny zestaw praktyczny.
- Rdzeń geometrii 28–35 — czytelny (z zastrzeżeniem późniejszych „doklejek”).

---

## 2. FAZA A — tylko przestawienie istniejących 61 tematów

**Bez nowych stron. Bez edycji kart.**  
Nowe litery działów (propozycja):

| Litera | Dział | Zakres nowych nr |
|--------|-------|------------------|
| **A** | Liczby i orientacja | 01–04 |
| **B** | Działania | 05–16 |
| **C** | Ułamki, procenty, proporcje | 17–25 |
| **D** | Algebra | 26–29 |
| **E** | Geometria płaska | 30–46 |
| **F** | Bryły | 47–48 |
| **G** | Miary | 49–57 |
| **H** | Dane i prawdopodobieństwo | 58–60 |
| **J** | Powtórzenie / symbole | 61 |

### 2.1 Mapa: stary nr → nowy nr

| Nowy | Stary | Tytuł (bez zmian) | Dział |
|------|-------|-------------------|-------|
| **01** | 61 | Stosunki przestrzenne i porównywanie | A |
| **02** | 01 | Liczby naturalne | A |
| **03** | 02 | Liczby rzymskie | A |
| **04** | 03 | Liczby całkowite | A |
| **05** | 04 | Dodawanie i odejmowanie | B |
| **06** | 05 | Tabliczka mnożenia | B |
| **07** | 06 | Dzielenie | B |
| **08** | 07 | Kolejność działań | B |
| **09** | 43 | Działania pisemne i szacowanie | B |
| **10** | 44 | Rozdzielność mnożenia | B |
| **11** | 08 | Podzielność | B |
| **12** | 45 | NWD, NWW i rozkład na czynniki | B |
| **13** | 13 | Potęgi | B |
| **14** | 53 | Notacja wykładnicza i potęga potęgi | B |
| **15** | 14 | Pierwiastki | B |
| **16** | 54 | Pierwiastek sześcienny i działania na √ | B |
| **17** | 09 | Ułamki zwykłe (1) | C |
| **18** | 10 | Ułamki zwykłe (2) | C |
| **19** | 11 | Ułamki dziesiętne | C |
| **20** | 12 | Działania na ułamkach | C |
| **21** | 46 | Ułamek liczby i całość z części | C |
| **22** | 15 | Procenty | C |
| **23** | 52 | Obliczenia procentowe — wszystkie typy | C |
| **24** | 16 | Proporcjonalność | C |
| **25** | 56 | Podział proporcjonalny | C |
| **26** | 17 | Wyrażenia algebraiczne | D |
| **27** | 18 | Sumy algebraiczne | D |
| **28** | 55 | Mnożenie wyrażeń algebraicznych | D |
| **29** | 19 | Równania | D |
| **30** | 28 | Figury płaskie (1) | E |
| **31** | 29 | Figury płaskie (2) | E |
| **32** | 48 | Proste prostopadłe i odległość | E |
| **33** | 32 | Kąt — pojęcie | E |
| **34** | 33 | Rodzaje kątów | E |
| **35** | 34 | Pary kątów / kąty przy ∥ | E |
| **36** | 49 | Suma kątów w trójkącie | E |
| **37** | 30 | Koło i okrąg | E |
| **38** | 31 | Długość okręgu i pole koła (π) | E |
| **39** | 35 | Obwód i pole | E |
| **40** | 50 | Pole rombu i trapezu; ar, ha | E |
| **41** | 37 | Symetria | E |
| **42** | 60 | Symetralna i dwusieczna | E |
| **43** | 38 | Współrzędne | E |
| **44** | 59 | Środek i długość odcinka | E |
| **45** | 58 | Przystawanie trójkątów | E |
| **46** | 57 | Twierdzenie Pitagorasa | E |
| **47** | 36 | Bryły | F |
| **48** | 51 | Graniastosłup, siatki, pole powierzchni | F |
| **49** | 20 | Długość | G |
| **50** | 21 | Masa | G |
| **51** | 22 | Objętość i litr | G |
| **52** | 23 | Czas | G |
| **53** | 24 | Kalendarz | G |
| **54** | 25 | Temperatura | G |
| **55** | 26 | Pieniądze | G |
| **56** | 27 | Prędkość i skala | G |
| **57** | 47 | Wyrażenia dwumianowane | G |
| **58** | 39 | Statystyka (1) | H |
| **59** | 40 | Statystyka (2) | H |
| **60** | 41 | Kombinatoryka i prawdopodobieństwo | H |
| **61** | 42 | Ściąga znaków | J |

### 2.2 Dlaczego taka kolejność wewnątrz działów

- **A:** najpierw przestrzeń i porównywanie (język matematyki dziecka), potem liczby.
- **B:** cztery działania → pisemne i prawa → podzielność/NWD (potrzebne do ułamków) → potęgi/pierwiastki.
- **C:** pojęcie ułamka → działania → „ułamek liczby” → % → proporcje (naturalny most do zadań tekstowych).
- **D:** litera → suma → mnożenie wyrażeń → równanie.
- **E:** figury → proste ⊥ → kąty → trójkąt → koło → pole → symetria → układ → przystawanie → Pitagoras.
- **F:** rozpoznawanie brył, potem graniastosłup / siatki / P i V.
- **G / H / J:** praktyka miar, dane, ściąga na końcu.

---

## 3. FAZA B — słownik etalonowy (~90–120 tematów)

Cel produktowy: **wszystkie pojęcia, które uczeń SP 1–8 może usłyszeć na lekcji**, z powrotem przez kilka lat.  
Orientacja: **~100–120 stron tematycznych**, **~600–800 haseł** (po rozbiciu „tłustych” kart typu *walec/stożek/kula*).

### 3.1 Proponowane działy (zbliżone do Twojej siatki)

| Dział | Proponowany zakres | Uwaga |
|-------|--------------------|--------|
| **A. Liczby** | 01–08 | + orientacja przestrzenna |
| **B. Działania** | 09–20 | pisemne, prawa, NWD, potęgi, pierwiastki |
| **C. Ułamki i procenty** | 21–32 | + proporcje |
| **D. Algebra** | 33–42 | + nierówności, wzory; opcjonalnie układy |
| **E. Geometria płaska** | 43–62 | + podobieństwo, okręgi wpisane/opisane, wielokąt foremny |
| **F. Bryły** | 63–72 | osobno: ostrosłup, walec, stożek, kula |
| **G. Miary** | 73–80 | jak dziś + ewentualnie jednostki pola/objętości osobno |
| **H. Dane i statystyka** | 81–86 | |
| **I. Most do szkoły średniej** | 87–92 | funkcja, trygonometria — **ponad wąskie minimum PP** (patrz §5) |
| **J. Powtórzenie** | 93–95 | ściąga, symbole, (opc.) strategie zadań |

Twoja siatka 01–90 jest **dobrym szkieletem**; poniżej korekty metodyczne:

1. **Trygonometria (Twój 80–87)** — w aktualnej PP SP **nie ma** sin/cos/tg jako obowiązkowego bloku egzaminacyjnego. Lepiej: **2–4 strony** w dziale **I (most)**, nie 8 stron w rdzeniu SP.
2. **Miary** lepiej trzymać jako dział własny (jak u Ciebie), nawet jeśli w szkole idą równolegle z kl. 1–3 — w słowniku liczy się **grupowanie pojęć**, nie kalendarz lekcji.
3. **Bryły** — dziś za ciasno (36 + 51); etalon wymaga **osobnych** tematów.

---

## 4. Brakujące tematy (do dodania po zatwierdzeniu kolejności)

Legenda statusu względem PP SP 1–8 (MEN):  
**PP** = w podstawie / typowe podręczniki · **część** = fragmentarycznie już w hasłach · **most** = ponad minimum / przygotowanie do liceum.

| # | PL | UA | Klasy | Dział | Status |
|---|----|----|-------|-------|--------|
| 1 | Liczby wymierne | Раціональні числа | 7–8 | A | PP |
| 2 | Oś liczbowa | Числова вісь | 4–6 | A | część (w 01/03) → osobna strona |
| 3 | Wartość bezwzględna (osobno) | Модуль числа | 4–7 | A | część (w 03) |
| 4 | Zaokrąglanie i szacowanie (osobno od działań pisemnych) | Округлення й оцінка | 4–6 | B | część (w 43) |
| 5 | Przemienność i łączność działań | Переставна й сполучна властивості | 4–6 | B | część (w 04/05) |
| 6 | Nierówności | Нерівності | 7–8 | D | **PP — brak osobnej strony** |
| 7 | Przekształcanie wzorów | Перетворення формул | 7–8 | D | partial w PP mapie |
| 8 | Układy równań (wprowadzenie) | Системи рівнянь (вступ) | 8 / most | D | most (nie rdzeń egzaminu) |
| 9 | Wielokąt foremny | Правильний многокутник | 7–8 | E | **gap PP** |
| 10 | Podobieństwo figur | Подібність фігур | 7–8 | E | **PP — brak** |
| 11 | Okrąg wpisany i opisany | Вписане й описане коло | 7–8 | E | PP / typowe podręczniki |
| 12 | Wysokość, środkowa, dwusieczna w trójkącie | Висота, медіана, бісектриса в трикутнику | 6–8 | E | część (60) → rozwinąć |
| 13 | Przekształcenia geometryczne (przesunięcie, obrót) | Геометричні перетворення | 7–8 | E | PP / rozszerzenie symetrii |
| 14 | Ostrosłup — pole i objętość | Піраміда — площа й об’єм | 7–8 | F | część (rozpoznanie w 36) |
| 15 | Walec | Циліндр | 7–8 | F | część (w 36) |
| 16 | Stożek | Конус | 7–8 | F | część (w 36) |
| 17 | Kula i sfera | Куля і сфера | 7–8 | F | część (w 36) |
| 18 | Jednostki pola i objętości (osobno) | Одиниці площі й об’єму | 4–8 | G | część (50, 22) |
| 19 | Funkcja (pojęcie) | Функція (поняття) | 7–8 / most | I | część przez proporcjonalność |
| 20 | Wykres funkcji / odczytywanie wykresu | Графік функції / читання графіка | 7–8 / most | I | część (wykres proporcjonalności) |
| 21 | Sinus | Синус | most (liceum) | I | **poza wąską PP SP** |
| 22 | Cosinus | Косинус | most | I | poza PP SP |
| 23 | Tangens | Тангенс | most | I | poza PP SP |
| 24 | Zadania tekstowe — strategie | Текстові задачі — стратегії | 4–6 | J | gap metodyczny (opcjonalnie) |
| 25 | Mediana, moda, średnia (jeśli rozdzielić ze Statystyka 2) | Медіана, мода, середнє | 7–8 | H | część (40) |
| 26 | Diagramy i wykresy (osobno od tabel) | Діаграми й графіки | 4–6 | H | część (39) |
| 27 | Prawdopodobieństwo (osobno od kombinatoryki) | Ймовірність | 7–8 | H | część (41) |
| 28 | Cecha podzielności przez 100 (dopisek lub mini-strona) | Ознака подільності на 100 | 4–5 | B | partial |

### 4.1 Priorytet wdrożenia (po Fazie A)

**P1 (must dla etalonu 7–8):** nierówności · podobieństwo · wielokąt foremny · ostrosłup / walec / stożek / kula · okręgi wpisane/opisane · przekształcanie wzorów  

**P2 (mocny słownik):** przekształcenia geometryczne · funkcja + wykres · jednostki P/V · oś liczbowa · liczby wymierne  

**P3 (most / opcjonalnie):** sin / cos / tg · układy równań · strategie zadań tekstowych  

---

## 5. Uwaga o trygonometrii i „120–150 tematach”

Twoja wizja **etalonu 120–150** jest spójna z rolą **wieloletniego przewodnika po języku lekcji**.  
Jednocześnie: sin/cos/tg **nie wypełniają luki PP SP** — wypełniają lukę **językową przed liceum** (dziecko może usłyszeć słowo na kółku / u starszego rodzeństwa / w zadaniach contestowych).

Rekomendacja produktowa:

- **Rdzeń SP (działy A–H + J)** ≈ 95–110 tematów.  
- **Dział I „Most”** ≈ 5–10 tematów (funkcja, wykres, sin/cos/tg, ewentualnie układ 2×2).  
- Łącznie **~100–120** stron = etalon bez wrażenia „podręcznika do liceum”.

---

## 6. Co zatwierdzić teraz

Proszę o decyzję (bez numeracji w plikach, dopóki nie potwierdzisz):

1. **Faza A:** czy akceptujesz mapę stary→nowy z §2.1 (61 tematów, tylko kolejność)?  
2. **Działy:** A–H + J jak wyżej, czy wolisz Twoje litery z trygonometrią jako pełny dział I w rdzeniu?  
3. **Faza B:** start od listy P1 (§4.1), cel ~100–120 stron (nie od razu 150)?  
4. **Miary:** zostawić po bryłach (jak w §2), czy przenieść **przed geometrię** (bliżej praktyki kl. 1–3)?

Po zatwierdzeniu: dopiero wtedy zmiana `n` / plików / spisu / `book.html` (osobny krok).
