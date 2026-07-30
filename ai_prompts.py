# -*- coding: utf-8 -*-
"""
Prompty AI do obrazków — perspektywa nauczyciela matematyki / metodyka SP (PL).
Styl: podręcznik 7–12 lat, jasno, czytelnie, bez zbędnego tekstu na obrazku.
"""

STYLE = (
    "Styl: ilustracja do polskiego podręcznika matematyki szkoły podstawowej, "
    "wiek 7–12 lat, jasne kolory, płaska/vector, duże czytelne kształty, "
    "białe lub bardzo jasne tło, bez drobnego tekstu, bez watermarków, "
    "przyjazna, edukacyjna, nie infantylna."
)

# hero + „w życiu” dla każdej strony (n: 1..42)
PAGE_PROMPTS = {
    1: {
        "hero": "Dzieci liczą kolorowe jabłka i klocki na stoliku w klasie; w tle oś liczbowa 1–10. Temat: liczby naturalne.",
        "life": "Scena z życia: dziecko liczy owoce w koszyku w sklepie / na straganie.",
    },
    2: {
        "hero": "Stary zegar z cyframi rzymskimi I–XII i kamienna tablica z napisem MMXXIV; styl edukacyjny.",
        "life": "Zegar wieżowy lub zegar ścienny z cyframi rzymskimi w codziennym otoczeniu.",
    },
    3: {
        "hero": "Oś liczbowa z liczbami ujemnymi i dodatnimi (−3…0…3), termometr obok pokazujący −5°C i +5°C.",
        "life": "Termometr za oknem z temperaturą poniżej zera zimą.",
    },
    4: {
        "hero": "Dwie grupy klocków: łączenie (dodawanie) i zabranie części (odejmowanie); proste ikony + i −.",
        "life": "Dziecko dokłada lub zabiera kredki z pudełka — dodawanie i odejmowanie w życiu.",
    },
    5: {
        "hero": "Siatka 3×4 kolorowych kropek / cukierków ukazująca 3×4=12; tabliczka mnożenia w tle lekko.",
        "life": "Tacka z ciasteczkami ułożonymi w rzędy i kolumny (mnożenie jako powtarzanie).",
    },
    6: {
        "hero": "12 cukierków podzielonych na 3 równe grupki po 4; strzałka „dzielimy sprawiedliwie”.",
        "life": "Dzieci dzielą pizzę lub kanapki na równe części przy stole.",
    },
    7: {
        "hero": "Kolorowa „kolejka działań”: nawiasy → potęga → ×: → +− jako 4 stacje metra / pociągu.",
        "life": "Kartka z przykładem 2+3×4 i wyróżnionym najpierw mnożeniem (jak w zeszycie).",
    },
    8: {
        "hero": "Lupa nad liczbą kończącą się na 0,2,4,6,8 (parzyste) vs 1,3,5,7,9; cechy podzielności.",
        "life": "Dziecko sprawdza, czy liczba osób w klasie dzieli się równo do grup.",
    },
    9: {
        "hero": "Pizza lub tort podzielony na 4 równe części, 1 część zaznaczona (1/4); podpis wizualny ułamka.",
        "life": "Czekolada połamana na równe kostki — części całości.",
    },
    10: {
        "hero": "Dwa prostokąty-paski: 2/4 i 1/2 pokazujące ten sam obszar (skracanie/rozszerzanie).",
        "life": "Szklanka do połowy pełna wody = 1/2.",
    },
    11: {
        "hero": "Duża liczba 2,75 z kolorowymi miejscami po przecinku (dziesiętne, setne); linijka dziesiętna.",
        "life": "Etykieta ceny 3,49 zł lub waga 1,5 kg — ułamki dziesiętne w sklepie.",
    },
    12: {
        "hero": "Schemat dodawania 1/4+1/4 i mnożenia 1/2×1/3 na prostych paskach/kołach.",
        "life": "Przepis kulinarny: 1/2 szklanki + 1/4 szklanki składnika.",
    },
    13: {
        "hero": "Wizualizacja 2³ jako trzy „piętra” po 2 klocki / drzewo mnożenia; duża dwójka z wykładnikiem 3.",
        "life": "Kostka Rubika lub pudełka ułożone w sześcian — potęgi w przestrzeni.",
    },
    14: {
        "hero": "Kwadrat o boku 3 i polu 9 obok znaku √9=3; pierwiastek jako „odwrócenie” kwadratu.",
        "life": "Kwadratowa ramka / płytka: bok a, pole a² — związek z pierwiastkiem.",
    },
    15: {
        "hero": "Pasek 100% z zaznaczonymi 25% (1/4); moneta lub wykres kołowy 25%.",
        "life": "Wyprzedaż −20% na metce w sklepie (czytelna, dla dziecka).",
    },
    16: {
        "hero": "Wykres y=kx: prosta przez (0,0) i punkty (1,2),(2,4); waga produktów i cena proporcjonalna.",
        "life": "Mapa skali lub przepis „2× składniki” — proporcja w kuchni.",
    },
    17: {
        "hero": "Klocki z literami x, y i liczbami tworzące wyrażenie 3x+5; styl algebra dla SP.",
        "life": "Bilet: cena = 5 zł × liczba osób — litera zamiast liczby.",
    },
    18: {
        "hero": "Kolorowe „kafelki” 3x i 2x łączące się w 5x; redukcja wyrazów podobnych.",
        "life": "Segregowanie klocków tego samego koloru/kształtu — wyrazy podobne.",
    },
    19: {
        "hero": "Waga szalkowa w równowadze: x+5 po lewej, 12 po prawej; potem x=7.",
        "life": "Zagadka: „myślę liczbę, dodaję 5, mam 12” — równanie w słowach.",
    },
    20: {
        "hero": "Kolorowa linijka szkolna w cm i taśma miernicza; dziecko mierzy biurko.",
        "life": "Mierzenie wzrostu dziecka przy furtce / ścianie.",
    },
    21: {
        "hero": "Waga kuchenna z mąką 1 kg = 1000 g; odważniki.",
        "life": "Zakupy: waży się jabłka na wadze w sklepie.",
    },
    22: {
        "hero": "Butelka 1 l i kubek 250 ml; prostopadłościan z wymiarami a,b,c i strzałką objętości.",
        "life": "Nalewanie wody do butelki / foremki — litr i mililitr.",
    },
    23: {
        "hero": "Zegar analogowy i cyfrowy 14:20; strzałki godziny i minuty wyraźne.",
        "life": "Plan dnia dziecka: szkoła, obiad, trening — odcinki czasu.",
    },
    24: {
        "hero": "Kartka kalendarza z datą i zaznaczonym tygodniem (7 dni); luty w roku przestępnym lekko.",
        "life": "Kalendarz rodzinny na lodówce z ważnymi dniami.",
    },
    25: {
        "hero": "Duży termometr °C: strefa ujemna niebieska, dodatnia czerwona; −5 i +20.",
        "life": "Dziecko w szaliku przy mrozie vs latem w koszulce — temperatura.",
    },
    26: {
        "hero": "Ilustracja monet i banknotów (umowna, nie realistyczny skan) 1 zł = 100 gr; cena 12,50 zł.",
        "life": "Dziecko płaci w sklepiku szkolnym i dostaje resztę.",
    },
    27: {
        "hero": "Samochód na drodze z podpisem v=s/t; obok mapa z podziałką 1:100 000.",
        "life": "Rodzina w aucie patrzy na czas dojazdu; dziecko z mapą turystyczną.",
    },
    28: {
        "hero": "Zestaw: punkt, odcinek, prosta, półprosta, trójkąt — czyste figury na kratce.",
        "life": "Znaki drogowe i okna budynku jako figury płaskie wokół nas.",
    },
    29: {
        "hero": "Galeria figur: trójkąt, kwadrat, prostokąt, romb, trapez — podpisane kształtami.",
        "life": "Dach domu (trójkąt), drzwi (prostokąt), znak STOP (ośmiokąt uproszczony).",
    },
    30: {
        "hero": "Okrąg i koło obok siebie: okrąg = linia, koło = wypełnione; środek O, promień r, średnica d.",
        "life": "Talerz, koło rowerowe, przycisk — okręgi w domu.",
    },
    31: {
        "hero": "Koło z zaznaczonym obwodem C=2πr i polem P=πr²; π≈3,14 jako „wstążka” wokół.",
        "life": "Opaska / sznurek wokół puszki — długość okręgu w praktyce.",
    },
    32: {
        "hero": "Kąt z wierzchołkiem i dwoma ramionami; kątomierz szkolny przykładający się do kąta.",
        "life": "Otwarta książka / nożyczki tworzące kąt.",
    },
    33: {
        "hero": "Cztery kąty obok siebie: ostry, prosty (z kwadratem), rozwarty, półpełny — różne kolory.",
        "life": "Róg zeszytu = kąt prosty; otwarte drzwi pod różnymi kątami.",
    },
    34: {
        "hero": "Dwie proste równoległe przecięte sieczną; zaznaczone kąty odpowiadające tym samym kolorem.",
        "life": "Tor kolejowy (równoległe szyny) i kładka / przejście jako sieczna.",
    },
    35: {
        "hero": "Prostokąt: taśma „obwód” dookoła i wypełnione „pole” w środku — jasny kontrast.",
        "life": "Ramka na zdjęcie (obwód) vs powierzchnia kartki do malowania (pole).",
    },
    36: {
        "hero": "Sześcian, prostopadłościan, ostrosłup, walec, kula — mała wystawa brył szkolnych.",
        "life": "Pudełko, piłka, puszka, dach namiotu — bryły w domu.",
    },
    37: {
        "hero": "Motyl lub liść z wyraźną osią symetrii (linia przerywana); odbicie lustrzane figury.",
        "life": "Dziecko przed lustrem; wycięte serce złożone na pół.",
    },
    38: {
        "hero": "Układ współrzędnych X/Y z punktem A(3,2); oś X w prawo, Y w górę, początek O(0,0).",
        "life": "Plan miasta / gra w statki — odczytywanie pozycji jak współrzędne.",
    },
    39: {
        "hero": "Prosty wykres słupkowy „ulubione owoce klasy” i tabela danych obok.",
        "life": "Ankieta w klasie: podnoszenie rąk i zapis wyników.",
    },
    40: {
        "hero": "Trzy ikony: średnia (waga), mediana (środkowa wartość w szeregu), moda (najczęstsza gwiazdka).",
        "life": "Oceny z klasówki na osi — wskazywanie środka i najczęstszej oceny.",
    },
    41: {
        "hero": "Kostka do gry i drzewko możliwości (2 spódnice × 3 bluzki); P=korzystne/wszystkie.",
        "life": "Losowanie dyżurnego z kapelusza / karty — prawdopodobieństwo na co dzień.",
    },
    42: {
        "hero": "Kolorowa ściąga znaków: + − × : = < > √ ² % π ∠ ∥ na kartce jak plakat klasowy.",
        "life": "Zeszyt ucznia z zapisanymi znakami działań na marginesie.",
    },
    43: {
        "hero": "Dodawanie i odejmowanie pisemne w kolorowym słupku; obok chmurka z szacunkiem ≈.",
        "life": "Dziecko liczy w zeszycie w słupku zadanie z podręcznika.",
    },
    44: {
        "hero": "Prostokąt podzielony na dwa: wizualizacja a·(b+c)=a·b+a·c.",
        "life": "Sześć rzędów po 13 cukierków liczone jako 6·10+6·3.",
    },
    45: {
        "hero": "Drzewko rozkładu 60=2·2·3·5; obok NWD i NWW dwóch liczb.",
        "life": "Skracanie ułamka 12/18 przez wspólny dzielnik 6.",
    },
    46: {
        "hero": "Pasek 20 podzielony na 4 równe części, 3 zaznaczone (3/4 z 20).",
        "life": "Kieszonkowe: bierzesz 3/4 kwoty na książkę.",
    },
    47: {
        "hero": "Linijka: 2 m 15 cm = 215 cm = 2,15 m — trzy zapisy tej samej długości.",
        "life": "Miarka wzrostu dziecka: 1 m 42 cm.",
    },
    48: {
        "hero": "Dwie proste z kątem prostym □ i znakiem ⊥; odcinek prostopadły od punktu do prostej.",
        "life": "Ekierka przy krawędzi biurka — kąt prosty.",
    },
    49: {
        "hero": "Trójkąt z kątami 40°, 60°, 80°; suma 180° wyróżniona.",
        "life": "Uczeń wylicza trzeci kąt w zeszycie: 180−(40+60).",
    },
    50: {
        "hero": "Romb z przekątnymi i trapez z wysokością; obok kwadrat 10×10 m = 1 ar.",
        "life": "Tabliczka „działka 5 arów” przy ogrodzeniu.",
    },
    51: {
        "hero": "Prostopadłościan i jego siatka obok; strzałka „sklej model”.",
        "life": "Pudełko po butach i rozłożony karton (siatka).",
    },
    52: {
        "hero": "Cztery ikony zadań procentowych: % z liczby, jaki %, całość, +/− p%.",
        "life": "Metka −30% i kalkulator przy kasie.",
    },
    53: {
        "hero": "3,5·10³ obok 3500; schemat (aᵐ)ⁿ=aᵐⁿ.",
        "life": "Duża liczba mieszkańców miasta zapisana z 10ᵏ.",
    },
    54: {
        "hero": "Kostka 2×2×2 i ∛8=2; obok √50=5√2.",
        "life": "Uczeń upraszcza pierwiastek na tablicy.",
    },
    55: {
        "hero": "Strzałki „każdy z każdym” przy (x+1)(x+3); wynik x²+4x+3.",
        "life": "Zeszyt z otwartymi nawiasami i redukcją wyrazów.",
    },
    56: {
        "hero": "Prostokąt podzielony w stosunku 2:3 na dwie części; monety 20 i 40.",
        "life": "Dwoje dzieci dzieli 60 zł według umowy 1:2.",
    },
    57: {
        "hero": "Trójkąt prostokątny 3-4-5 z kwadratami na bokach (ilustracja Pitagorasa).",
        "life": "Drabina oparta o ścianę — trójkąt prostokątny.",
    },
    58: {
        "hero": "Dwa trójkąty z zaznaczonymi równymi bokami (cecha BBB) i znakiem ≅.",
        "life": "Wycinanki dwóch jednakowych trójkątów z papieru.",
    },
    59: {
        "hero": "Układ współrzędnych z odcinkiem AB, środkiem M i długością 5.",
        "life": "Plan osiedla w kratkę — odległość między dwoma punktami.",
    },
    60: {
        "hero": "Odcinek z symetralną oraz kąt z dwusieczną; łuki równości.",
        "life": "Składanie kartki na pół — intuicja dwusiecznej / symetrii.",
    },
    61: {
        "hero": "Klasa: dziecko pokazuje lewo/prawo, strzałki góra/dół przy drabinie, dłuższy i krótszy szalik, dwie miseczki z różną liczbą cukierków.",
        "life": "Boisko szkolne: dzieci porównują prawo/lewo, dłuższy kij, więcej piłek w koszu.",
        "cards": {
            "prawo / lewo": "Dziecko od tyłu, ramiona w bok: LEWO po lewej, PRAWO po prawej (ta sama orientacja co czytelnik).",
            "góra / dół": "Dom z ptakiem u góry (↑) i piłką na dole (↓).",
            "przed / za / obok": "Trzy sceny: dziecko przed biurkiem, za krzesłem, obok tornistra.",
            "dłuższy / krótszy": "Długi i krótki ołówek / szalik obok siebie.",
            "cięższy / lżejszy": "Waga szalkowa: książka cięższa, piórko lżejsze.",
            "więcej / mniej / tyle samo": "Miseczki z jabłkami: 5 vs 2, 2 vs 5, 3 = 3.",
        },
    },
}


def _clean(s: str) -> str:
    return " ".join(s.split())


def prompt_hero(page: dict) -> str:
    n = page["n"]
    base = PAGE_PROMPTS.get(n, {}).get("hero") or (
        f"Ilustracja tytułowa tematu „{page['title_pl']}” dla klasy SP."
    )
    return _clean(f"{base} {STYLE}")


def prompt_life(page: dict) -> str:
    n = page["n"]
    base = PAGE_PROMPTS.get(n, {}).get("life") or (
        f"Scena z życia dziecka związana z tematem „{page['title_pl']}”."
    )
    return _clean(f"{base} {STYLE}")


# Słownik podpowiedzi do haseł (fragment nazwy → idea obrazka)
TERM_HINTS = [
    ("naturaln", "kilka jabłek / klocków do policzenia: 1,2,3,4,5"),
    ("cyfr", "dziesięć kafelków z cyframi 0–9 jak pieczątki"),
    ("pozycyjn", "trzy pudełka: setki, dziesiątki, jednostki z cyframi 3,4,7"),
    ("parzyst", "dwa rzędy stopek: parzyste/nieparzyste ostatnie cyfry"),
    ("porówn", "waga lub dwie wieże klocków: 3 < 7"),
    ("zaokrągl", "oś liczbowa ze strzałką 47 → 50"),
    ("następn", "oś: 8 ← 9 → 10 z podpisami poprzednik/następnik"),
    ("kolejność liczb", "pociąg wagoników z liczbami 1–6 rosnąco"),
    ("rzymsk", "tablice I V X L C D M jak w muzeum"),
    ("całkowit", "oś z ujemnymi i dodatnimi, zero w środku"),
    ("bezwzględ", "odległość od zera na osi: |−5|=5"),
    ("dodawa", "dwie grupy kropek łączące się w jedną"),
    ("odejmow", "grupa obiektów z częścią przekreśloną / zabraną"),
    ("sum", "etykiety: składnik + składnik = suma"),
    ("różnic", "etykiety: odjemna − odjemnik = różnica"),
    ("mnoż", "siatka rzędów i kolumn (tabliczka)"),
    ("dziel", "obiekty w równych grupach"),
    ("kolejność działa", "4 kolory stacji: () , aⁿ , ×: , +−"),
    ("podzieln", "lupa na ostatnią cyfrę liczby"),
    ("ułamek", "koło lub pasek podzielony na równe części z zaznaczeniem"),
    ("licznik", "górna część ułamka wyróżniona kolorem"),
    ("mianownik", "dolna część ułamka — na ile części podzielono"),
    ("skrac", "2/4 i 1/2 jako ten sam obszar"),
    ("rozszerz", "1/2 → 2/4 powiększenie tego samego ułamka"),
    ("dziesiętn", "liczba z przecinkiem i kolorowymi miejscami po przecinku"),
    ("procent", "pasek 100% z wycinkiem p%"),
    ("potęg", "powtarzane mnożenie tej samej liczby; aⁿ"),
    ("pierwiast", "kwadrat i jego bok; √ jako odwrotność"),
    ("proporc", "prosta przez początek układu; tabela x,y"),
    ("algebr", "litery-klocki x,y i liczby w wyrażeniu"),
    ("jednomian", "jeden kafelek typu 5x²"),
    ("sumy algebr", "kafelki 3x i 2x łączone w 5x"),
    ("równan", "waga w równowadze z niewiadomą x"),
    ("długość", "linijka szkolna przy przedmiocie"),
    ("masa", "waga kuchenna i produkty w gramach/kg"),
    ("objęto", "butelka 1 l i miarki ml"),
    ("czas", "zegar ze wskazówkami"),
    ("kalendar", "kartka kalendarza z datą"),
    ("temperat", "termometr °C z + i −"),
    ("pieniądz", "monety/banknoty ilustracyjne i cena z przecinkiem"),
    ("prędkość", "auto i wzór v=s/t w prostym schemacie"),
    ("skala", "mapa z podziałką 1:n"),
    ("figur", "podstawowe figury na kratce"),
    ("trójkąt", "trójkąt z zaznaczonymi bokami/kątami"),
    ("kwadrat", "kwadrat z równymi bokami i kątami prostymi"),
    ("prostokąt", "prostokąt a×b"),
    ("koło", "wypełnione koło"),
    ("okrąg", "sama okrągła linia ze środkiem"),
    ("promień", "odcinek od środka do okręgu"),
    ("średnic", "odcinek przez środek okręgu"),
    ("π", "wstążka wokół koła; π≈3,14"),
    ("kąt", "dwa ramiona i wierzchołek; kątomierz"),
    ("ostry", "kąt mniejszy niż 90°"),
    ("prosty", "kąt 90° z małym kwadracikiem"),
    ("rozwart", "kąt między 90° a 180°"),
    ("równoleg", "dwie proste || i sieczna"),
    ("obwód", "taśma dookoła figury"),
    ("pole", "wypełnione wnętrze figury"),
    ("brył", "sześcian / pudełko 3D"),
    ("sześcian", "kostka z równymi krawędziami"),
    ("symetr", "figura i oś lustrzana"),
    ("współrzęd", "punkt (x,y) na osiach"),
    ("statyst", "wykres słupkowy z danymi klasy"),
    ("średni", "liczby i ich średnia jako „środek ciężkości”"),
    ("median", "uporządkowany szereg ze środkową wartością"),
    ("moda", "najczęściej powtarzający się symbol"),
    ("prawdopodob", "kostka / losowanie; korzystne vs wszystkie"),
    ("kombinator", "drzewko możliwości ubrań/dróg"),
    ("znak", "plakat ze znakami + − × : ="),
]


def hint_for_term(term_pl: str) -> str:
    t = term_pl.lower()
    for key, hint in TERM_HINTS:
        if key in t:
            return hint
    return f"prosty, czytelny rysunek wyjaśniający pojęcie „{term_pl}” bez zbędnego tekstu"


def prompt_card_media(page: dict, card: dict, kind: str) -> str:
    term = card.get("pl") or "hasło"
    topic = page.get("title_pl") or ""
    hint = hint_for_term(term)
    kind_pl = {
        "cover": "ilustracja do karty hasła",
        "photo": "zdjęcie/ilustracja z życia",
        "diagram": "schemat matematyczny / rysunek dydaktyczny",
        "icon": "prosta ikona 1 pojęcia",
        "hero": "duża ilustracja tematu",
    }.get(kind, "ilustracja edukacyjna")
    return _clean(
        f"{kind_pl.capitalize()} do tematu „{topic}”, hasło „{term}”: {hint}. {STYLE}"
    )


def prompt_icon(page: dict, card: dict) -> str:
    term = card.get("pl") or "hasło"
    return _clean(
        f"Prosta kwadratowa ikona (app-icon style) symbolizująca „{term}” "
        f"w temacie „{page.get('title_pl','')}”; jeden motyw, max 2 kolory + tło. {STYLE}"
    )


def prompt_svg_upgrade(page: dict, card: dict, fig_key: str) -> str:
    """Gdy jest już schemat SVG — prompt na bogatszą wersję / foto uzupełniające."""
    term = card.get("pl") or ""
    return _clean(
        f"Uzupełnienie schematu SVG („{fig_key}”) dla hasła „{term}” "
        f"w temacie „{page.get('title_pl','')}”: bardziej dopracowana ilustracja podręcznikowa "
        f"tego samego sensu dydaktycznego (nie zmieniaj idei schematu). {STYLE}"
    )
