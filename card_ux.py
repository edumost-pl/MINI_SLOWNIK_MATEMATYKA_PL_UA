# -*- coding: utf-8 -*-
"""
Prezentacja karty według standardu EduMost (15 sekund).
Nie zmienia treści merytorycznej w źródłach — tylko układ bloków.
"""
from __future__ import annotations

import re
from html import unescape


def _norm(term: str) -> str:
    t = (term or "").strip().lower()
    t = t.replace("ł", "l").replace("ó", "o")
    return t


def _strip_html(s: str) -> str:
    s = unescape(s or "")
    s = re.sub(r"<br\s*/?>", " · ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip()


def _sentences(text: str, max_n: int = 3) -> str:
    """Zostaw max 2–3 krótkie zdania."""
    text = _strip_html(text)
    if not text:
        return ""
    # split on . ! ? keeping short
    parts = re.split(r"(?<=[.!?…])\s+", text)
    parts = [p.strip() for p in parts if p.strip()]
    if not parts:
        return text[:180]
    chosen = parts[:max_n]
    # drop very long tails inside a sentence
    out = []
    for p in chosen:
        if len(p) > 160:
            p = p[:157].rsplit(" ", 1)[0] + "…"
        out.append(p)
    return " ".join(out)


def _split_bits(raw: str) -> list[str]:
    raw = _strip_html(raw)
    if not raw:
        return []
    # split on bullets separators
    bits = re.split(r"\s*[·•|/]\s*|\s*;\s*|\n+", raw)
    out = []
    for b in bits:
        b = b.strip(" ,;")
        if not b:
            continue
        # further split long comma lists of short tokens
        if "," in b and len(b) < 80 and not re.search(r"[a-zA-Ząćęłńóśźż]{8,}", b):
            for x in b.split(","):
                x = x.strip()
                if x:
                    out.append(x)
        else:
            out.append(b)
    return out


def co_to_jest(card: dict) -> tuple[str, str]:
    pl = _sentences(card.get("def_pl") or card.get("explain") or "", 3)
    ua = _sentences(card.get("def_ua") or card.get("explain_ua") or "", 3)
    return pl, ua


def zapamietaj(card: dict) -> tuple[str, str]:
    """Jedna główna rzecz do zapamiętania — wzór / lista / krótka reguła."""
    visual = _strip_html(card.get("visual") or "")
    rule = _strip_html(card.get("rule") or "")
    rule_ua = _strip_html(card.get("rule_ua") or "")
    # Prefer compact visual if it looks like formula / digits / table
    if visual and (
        re.search(r"[=×·÷+\-<>≤≥≠]|^\d|m =|cm|P =|V =|a ×|1 :", visual)
        or len(visual) <= 48
        or " " in visual and len(visual) < 70
    ):
        core = visual
    elif rule:
        # first sentence of rule, shorten
        core = _sentences(rule, 1)
        if len(core) > 120:
            core = core[:117].rsplit(" ", 1)[0] + "…"
    else:
        core = visual or _sentences(card.get("def_pl") or "", 1)
    ua = rule_ua
    if ua and len(ua) > 120:
        ua = _sentences(ua, 1)
    return core, ua


# Porównania „Nie pomyl” — treść merytoryczna zgodna ze szkołą, forma skrócona
NIE_POMYL: dict[str, list[tuple[str, str]]] = {
    "cyfra": [("3 → cyfra", "35 → liczba"), ("0–9 = cyfry", "347 = liczba")],
    "liczba": [("cyfra = klocek", "liczba = ile"), ("9 = cyfra i liczba", "29 = liczba")],
    "liczba naturalna": [("1, 2, 3…", "≠ ułamki"), ("do liczenia", "≠ liczby ujemne")],
    "wartość pozycyjna": [("3 w 35 = 3 dziesiątki", "3 w 3 = 3 jednostki"), ("miejsce = wartość", "ta sama cyfra ≠ to samo")],
    "liczba porządkowa": [("1. = pierwszy", "1 = jeden"), ("kolejność (który?)", "≠ ile?")],
    "zero": [("0 = nic", "nie „pusty znak”"), ("0 w naturalnych: zależnie od umowy", "0 zawsze jest cyfrą")],
    "parzysta / nieparzysta": [("parzysta :2 bez reszty", "nieparzysta: reszta 1"), ("ostatnia cyfra decyduje", "parzystość ≠ wielkość")],
    "porównanie": [("3 < 7", "7 > 3"), ("dziób < > do większej", "≠ znak minus")],
    "zaokrąglanie": [("47 → 50", "nie „obcinaj zawsze”"), ("0–4 w dół", "5–9 w górę")],
    "następnik / poprzednik": [("poprzednik = −1", "następnik = +1"), ("sąsiedzi na osi", "≠ zaokrąglanie")],
    "kolejność liczb": [("rosnąco: małe → duże", "malejąco: duże → małe"), ("kolejność liczb", "≠ liczba porządkowa")],
    "oś liczbowa": [("w lewo → mniejsze", "w prawo → większe"), ("oś liczbowa", "linia czasu")],
    "dodatnie, ujemne, zero": [("ujemne < 0", "zero = 0"), ("dodatnie > 0", "znak „−” przy dodatniej")],
    "wartość bezwzględna": [("|−5| = 5", "≠ −5"), ("odległość od 0", "≠ liczba przeciwna")],
    "porównywanie": [("−7 < −2", "nie „−7 większe bo 7”"), ("im bardziej w lewo, tym mniejsza", "≠ porównuj same cyfry")],
    "liczba przeciwna": [("przeciwna do 3 = −3", "|3| = 3"), ("3+(−3)=0", "≠ wartość bezwzględna")],
    "zastosowania": [("−8°C = zimno", "„minus” ≠ zawsze źle"), ("piętro −1 · dług −20 zł", "≠ tylko w ćwiczeniach")],
    # Liczby rzymskie (dłuższe klucze przed „dodawanie” / „odejmowanie”)
    "podstawowe znaki": [("I=1 V=5 X=10", "L=50 C=100 D=500 M=1000"), ("7 znaków-liter", "≠ cyfry arabskie 0–9")],
    "składanie liczb": [("znaki obok siebie", "jak klocki"), ("XIV = 10+4", "≠ osobne litery")],
    "dodawanie znaków": [("mniejszy z prawej → +", "VI = V+I = 6"), ("dodawanie znaków", "≠ odejmowanie znaków")],
    "odejmowanie znaków": [("mniejszy z lewej → −", "IV = V−I = 4"), ("tylko I, X, C przed większym", "≠ dowolna litera")],
    "ograniczenia": [("I przed V,X", "nie przed L,C,D,M"), ("max 3× ten sam znak", "nie powtarzaj V,L,D")],
    "większe przykłady": [("czytaj od lewej", "XLIV = 40+4"), ("łącz +/− według reguł", "≠ od prawej")],
    "gdzie spotykamy?": [("zegar: IV, IX, XII", "rozdział II"), ("data na pomniku", "≠ tylko w podręczniku")],
    "zamiana na arabskie": [("LXIV → 50+10+4", "wynik 64"), ("odejmij gdy trzeba, potem dodaj", "≠ czytaj litery jak litery")],
    "dodawanie": [("suma = wynik +", "składniki = to, co dodajesz"), ("kolejność nie zmienia sumy", "odejmowanie (kolejność ważna)")],
    "suma": [("suma = wynik dodawania", "znak „+” sam"), ("2+3=5 → suma 5", "składniki 2 i 3")],
    "odejmowanie": [("różnica = wynik −", "odjemna / odjemnik = części"), ("kolejność ważna", "dodawanie (można zamienić)")],
    "różnica": [("różnica = wynik odejmowania", "odjemna albo odjemnik"), ("sprawdź: różnica + odjemnik", "nie myl z samym znakiem −")],
    "dodawanie na palcach / osi": [("najpierw na palcach / osi", "od razu „w pamięci” bez sensu"), ("skok w prawo = +", "skok w lewo = −")],
    "odejmowanie: ile zostało": [("ile zostało?", "wynik bez pytania"), ("sprawdź dodawaniem", "nie sprawdzaj wcale")],
    "składnik": [("składnik → dodawanie", "czynnik → mnożenie"), ("2+5: składniki 2 i 5", "≠ odjemnik")],
    "odjemna i odjemnik": [("odjemna − odjemnik", "składnik + składnik"), ("kolejność ważna", "nie zamieniaj miejscami")],
    "właściwości +": [("przemienność +", "przemienność − (nie działa)"), ("łączność pomaga liczyć", "mieszaj kolejność przy −")],
    "właściwości −": [("a−0=a", "a−a=0"), ("9−4 ≠ 4−9", "jak przy dodawaniu")],
    "przykłady": [("sprawdź: różnica + odjemnik", "zgaduj bez sprawdzenia"), ("najpierw sens, potem wynik", "tylko wynik „z głowy”")],
    "mnożenie": [("× = dodawanie tej samej", "zwykłe + różnych liczb"), ("iloczyn = wynik ×", "≠ dzielenie")],
    "mnożenie = dodawanie tej samej": [("4×3 = 4+4+4", "4+3 = 7"), ("razy po tyle samo", "dodawanie różnych składników")],
    "iloczyn": [("iloczyn = wynik ×", "czynniki = to, co mnożysz"), ("2·5=10 → iloczyn 10", "≠ suma")],
    "czynnik": [("czynnik → mnożenie", "składnik → dodawanie"), ("3×7: czynniki 3 i 7", "≠ dzielnik")],
    "przemienność": [("3×4 = 4×3", "3−4 ≠ 4−3"), ("działa dla + i ×", "nie dla − i :")],
    "×0 i ×1": [("a×0=0", "a×1=a"), ("przez 0 zawsze 0", "przez 1 = ta sama")],
    "kluczowe wyniki": [("7×8 = 56", "7+8 = 15"), ("najpierw sens ×", "tylko pamięć bez sensu")],
    "dzielenie": [("dzielenie = po równo", "zabieranie „byle jak”"), ("iloraz = wynik :", "nie dziel przez 0")],
    "sprawiedliwe rozdawanie": [("każdemu tyle samo", "jednemu więcej „na oko”"), ("12:3 → po 4", "reszta bez zapisu")],
    "iloraz": [("iloraz = wynik dzielenia", "≠ reszta"), ("12:3=4 → iloraz 4", "≠ dzielna / dzielnik")],
    "dzielna i dzielnik": [("dzielna : dzielnik", "czynnik × czynnik"), ("dzielnik ≠ 0", "kolejność ważna")],
    "z resztą": [("14:3 = 4 r.2", "nie „zawsze równo”"), ("reszta < dzielnik", "≠ ułamek")],
    "związek z ×": [("12:3=4 ↔ 4×3=12", "bez sprawdzania"), ("dzielenie sprawdza ×", "≠ obce działania")],
    ":1 i : siebie": [("a:1=a", "a:a=1"), ("a:0 zabronione", "≠ a×0")],
    "nawiasy": [("najpierw ( )", "od lewej „na siłę”"), ("(2+3)×4 = 20", "2+3×4 = 14")],
    "kolejność działań": [("() → potęgi → ×: → +−", "nie „od lewej zawsze”"), ("ten sam poziom: od lewej", "nawiasy najpierw")],
    "potęgi": [("najpierw potęga", "najpierw + przy 2+3²"), ("2+3² = 11", "(2+3)² = 25")],
    "× i :": [("× i : przed + i −", "od lewej zawsze najpierw +"), ("2+3×4 = 14", "(2+3)×4 = 20")],
    "+ i −": [("+ i − na końcu", "przed ×"), ("od lewej do prawej", "od prawej")],
    "ten sam poziom": [("× i : od lewej", "najpierw × potem :"), ("24:6×2 = 8", "24:(6×2) = 2")],
    "przykład": [("warstwami: ( ) → aⁿ → ×: → +−", "wszystko naraz od lewej"), ("zapisuj kroki", "tylko wynik końcowy")],
    "działanie pisemne": [("cyfra pod cyfrą (słupek)", "pisz w jednej linii"), ("od prawej do lewej", "od lewej jak czytanie")],
    "dodawanie pisemne": [("jedności pod jednościami", "cyfry „jak leci”"), ("pamiętaj o przeniesieniu", "zapomnij o przeniesieniu")],
    "odejmowanie pisemne": [("pożycz, gdy za mało", "odejmuj na siłę"), ("sprawdź dodawaniem", "bez sprawdzenia")],
    "mnożenie pisemne": [("częściowe iloczyny + przesunięcie", "mnoż raz i zgaduj"), ("przeniesienie jak przy +", "bez przeniesienia")],
    "dzielenie pisemne": [("mnoż i odejmij krokami", "dziel na oko"), ("reszta < dzielnik", "reszta ≥ dzielnik")],
    "szacowanie": [("≈ wynik przybliżony", "tylko dokładny wynik"), ("zaokrąglij, potem policz", "zgaduj bez zaokrąglenia")],
    "rozdzielność": [("a·(b+c)=a·b+a·c", "a·(b+c)=a·b+c"), ("mnożysz każdy składnik", "tylko pierwszy")],
    "przykład liczbowy": [("6·13 = 6·10+6·3", "6·13 = 6+13"), ("wygodniej w pamięci", "zawsze tylko słupek")],
    "odwrotnie: wyłączanie": [("4·7+4·3 = 4·(7+3)", "tylko rozdzielaj"), ("wspólny czynnik przed ( )", "różne czynniki na siłę")],
    "w geometrii": [("(a+b)·c = a·c + b·c", "pole ≠ suma pól"), ("prostokąt z dwóch części", "≠ pole koła")],
    "z literami": [("x(x+2)=x²+2x", "x(x+2)=x+2"), ("otwierasz nawias ×", "dodajesz na ślepo")],
    "ułamek zwykły": [("licznik / mianownik", "3/4 ≠ 4/3"), ("część całości", "≠ liczba mieszana")],
    "licznik": [("góra ułamka", "ile części bierzemy"), ("3/5 → licznik 3", "≠ mianownik")],
    "mianownik": [("dół ułamka", "na ile części dzielimy"), ("3/5 → mianownik 5", "≠ licznik")],
    "liczba mieszana": [("1 ½ = 3/2", "całość + ułamek"), ("≠ ułamek właściwy", "można zamienić")],
    "skracanie": [("dzielimy licznik i mianownik", "wartość ta sama"), ("2/4 = 1/2", "≠ rozszerzanie")],
    "rozszerzanie": [("mnożymy licznik i mianownik", "wartość ta sama"), ("1/2 = 2/4", "≠ skracanie")],
    "ułamek dziesiętny": [("przecinek", "0,5 = 1/2"), ("miejsce po przecinku = wartość", "≠ ułamek zwykły zapisem")],
    "odwrotność": [("odwrotność 2/3 = 3/2", "iloczyn = 1"), ("do dzielenia ułamków", "≠ liczba przeciwna")],
    "procent": [("1% = 1/100", "50% = połowa"), ("% z liczby", "nie myl z „punktami procentowymi”")],
    "proporcja": [("a:b = c:d", "iloczyny krzyżowe"), ("≠ procent", "stosunek dwóch par")],
    "stosunek": [("a:b", "porównanie dwóch wielkości"), ("≠ ułamek „części całości” zawsze", "blisko proporcji")],
    "potęga": [("2³ = 2·2·2", "podstawa i wykładnik"), ("≠ mnożenie zwykłe 2×3", "wykładnik = ile razy")],
    "pierwiastek kwadratowy": [("√9 = 3", "bo 3² = 9"), ("≠ dzielenie przez 2", "odwrotność kwadratu")],
    "równanie": [("ma =", "szukamy niewiadomej"), ("≠ nierówność < >", "sprawdź podstawieniem")],
    "niewiadoma": [("x — niewiadoma", "szukamy jej wartości"), ("≠ zmienna „dowolna” w wyrażeniu", "w równaniu: do znalezienia")],
    "nierówność": [("< > ≤ ≥", "zakres rozwiązań"), ("≠ równanie =", "na osi: często promień")],
    "wyrażenie algebraiczne": [("ma litery", "2a+3"), ("≠ równanie (brak =)", "można obliczyć wartość")],
    "jednomian": [("jeden wyraz", "3x²"), ("≠ suma algebraiczna", "suma = kilka wyrazów")],
    "suma algebraiczna": [("wyrazy + / −", "redukcja podobnych"), ("≠ równanie", "to wyrażenie")],
    "punkt": [("punkt nie ma długości", "oznaczamy literą"), ("≠ odcinek", "odcinek ma 2 końce")],
    "prosta": [("nieskończona w obie strony", "≠ odcinek"), ("≠ półprosta", "półprosta: początek + jedna strona")],
    "odcinek": [("ma 2 końce", "długość"), ("≠ prosta", "≠ półprosta")],
    "półprosta": [("początek + jedna strona", "≠ prosta"), ("≠ odcinek", "odcinek ma 2 końce")],
    "kąt": [("dwa ramiona + wierzchołek", "miara w °"), ("≠ trójkąt", "kąt to „otwarcie”")],
    "kąt prosty": [("90°", "jak róg kartki"), ("≠ ostry (<90°)", "≠ rozwarty (>90°)")],
    "kąt ostry": [("< 90°", "≠ prosty"), ("≠ rozwarty", "spiczasty")],
    "kąt rozwarty": [("> 90° i < 180°", "≠ prosty"), ("≠ półpełny 180°", "")],
    "okrąg": [("linia — brzeg", "≠ koło"), ("punkty w odległości r", "koło = wnętrze + brzeg")],
    "koło": [("pełne wnętrze", "≠ okrąg"), ("pole koła", "długość = okręgu")],
    "promień": [("środek → okrąg", "r"), ("≠ średnica", "średnica = 2r")],
    "średnica": [("przez środek", "d = 2r"), ("≠ promień", "≠ cięciwa (nie musi przez środek)")],
    "cięciwa": [("łączy 2 punkty okręgu", "nie musi przez środek"), ("≠ średnica", "średnica = najdłuższa cięciwa")],
    "obwód": [("długość dookoła", "cm, m"), ("≠ pole", "pole = powierzchnia")],
    "pole": [("powierzchnia", "cm², m²"), ("≠ obwód", "≠ objętość")],
    "objętość": [("miejsce w środku", "cm³, litr"), ("≠ pole", "≠ obwód")],
    "trójkąt": [("3 boki, 3 kąty", "suma kątów 180°"), ("≠ prostokąt", "rodzaje: boki / kąty")],
    "kwadrat": [("4 równe boki + 4 kąty proste", "≠ romb (kąty)"), ("≠ prostokąt (boki)", "kwadrat ⊆ prostokąt")],
    "prostokąt": [("kąty proste", "przeciwległe boki równe"), ("≠ kwadrat zawsze", "kwadrat to szczególny prostokąt")],
    "romb": [("4 równe boki", "≠ kwadrat zawsze"), ("kąty nie muszą być proste", "kwadrat = romb + kąty proste")],
    "równoległobok": [("przeciwległe boki ∥ i równe", "≠ prostokąt zawsze"), ("≠ trapez (tylko 1 para ∥)", "")],
    "trapez": [("dokładnie 1 para boków ∥", "≠ równoległobok"), ("≠ prostokąt", "")],
    "proste równoległe": [("∥ nigdy się nie zetkną", "≠ prostopadłe ⊥"), ("sieczna tworzy kąty", "")],
    "proste prostopadłe": [("⊥ = kąt 90°", "≠ równoległe"), ("odległość: najkrótsza do prostej", "")],
    "symetria": [("odbicie / środek", "kształt „pasuje”"), ("≠ przystawanie zawsze tematycznie osobno", "oś ≠ środek")],
    "przystawanie": [("ten sam kształt i rozmiar", "≅"), ("≠ podobieństwo (~)", "podobieństwo może mieć inną skalę")],
    "podobieństwo": [("ten sam kształt, inna skala", "~"), ("≠ przystawanie", "k = 1 → przystawanie")],
    "twierdzenie pitagorasa": [("a²+b²=c²", "tylko prostokątny"), ("c = przeciwprostokątna", "≠ dowolny trójkąt")],
    "przyprostokątne i przeciwprostokątna": [("przyprostokątne przy 90°", "przeciwprostokątna naprzeciw 90°"), ("c najdłuższy bok", "nie myl nazw")],
    "sześcian": [("6 kwadratów", "wszystkie krawędzie równe"), ("≠ prostopadłościan", "prostopadłościan może mieć różne krawędzie")],
    "prostopadłościan": [("6 prostokątów", "≠ sześcian zawsze"), ("sześcian = szczególny przypadek", "")],
    "walec": [("2 koła + płaszcz", "≠ stożek"), ("≠ kula", "puszka ≈ walec")],
    "stożek": [("koło + wierzchołek", "≠ walec"), ("≠ ostrosłup (podstawa wielokąt)", "")],
    "kula": [("pełna piłka", "≠ sfera"), ("sfera = powierzchnia", "")],
    "sfera": [("tylko powierzchnia", "≠ kula"), ("jak skórka piłki", "")],
    "ostrosłup": [("podstawa + wierzchołek", "≠ graniastosłup"), ("V = ⅓·P·H", "≠ walec")],
    "graniastosłup": [("dwie podstawy ∥", "ściany boczne"), ("≠ ostrosłup", "prosty: krawędzie ⊥ podstawie")],
    "średnia arytmetyczna": [("suma / liczba danych", "≠ mediana"), ("≠ moda", "")],
    "mediana": [("środkowa po uporządkowaniu", "≠ średnia"), ("≠ moda", "")],
    "moda": [("najczęstsza wartość", "≠ średnia"), ("≠ mediana", "")],
    "prawdopodobieństwo": [("0 ≤ P ≤ 1", "korzystne / wszystkie"), ("≠ kombinatoryka (zliczanie)", "doświadczenie losowe")],
    "jednostki długości": [("m, cm, km", "≠ m² (pole)"), ("≠ kg (masa)", "")],
    "jednostki masy": [("kg, g, t", "≠ litr (objętość)"), ("≠ metr", "")],
    "litr": [("objętość cieczy", "1 l = 1 dm³"), ("≠ kilogram", "≠ metr")],
    "prędkość": [("v = s/t", "km/h, m/s"), ("≠ skala mapy", "droga / czas")],
    "skala mapy": [("1 : n", "mapa → teren"), ("≠ prędkość", "mnożysz przez n")],
    "złoty i grosz": [("1 zł = 100 gr", "≠ procent"), ("reszta przy zakupie", "")],
    "liczba wymierna": [("a/b, b≠0", "całkowite ∈ ℚ"), ("skończony / okresowy dziesiętny", "≠ „tylko ułamek zwykły”")],
    "przesunięcie": [("w bok o tyle samo", "≠ obrót"), ("kształt zostaje", "inne miejsce")],
    "obrót": [("wokół punktu + kąt", "≠ przesunięcie"), ("jak wskazówka zegara", "")],
    "środkowa": [("do środka boku", "≠ wysokość"), ("≠ dwusieczna", "")],
    "okrąg wpisany": [("styczny do boków", "≠ opisany"), ("środek: dwusieczne", "")],
    "okrąg opisany": [("przez wierzchołki", "≠ wpisany"), ("środek: symetralne", "")],
    "wielokąt foremny": [("równe boki i kąty", "≠ każdy romb"), ("foremny 4-kąt = kwadrat", "")],
    "przekształcanie wzoru": [("działania po obu stronach", "≠ tylko jedna strona"), ("v = s/t z s = v·t", "")],
}


def _fallback_nie_pomyl(card: dict) -> list[tuple[str, str]]:
    term = (card.get("pl") or "").strip()
    vis = _split_bits(card.get("visual") or "")
    pairs: list[tuple[str, str]] = []
    if len(vis) >= 2:
        pairs.append((vis[0][:40], vis[1][:40]))
    if len(vis) >= 4:
        pairs.append((vis[2][:40], vis[3][:40]))
    def_pl = (card.get("def_pl") or "").strip()
    if term and def_pl:
        short = def_pl.split(".")[0][:48]
        pairs.append((f"{term} = coś innego", short or term))
    while len(pairs) < 2:
        if term:
            pairs.append((f"Mylę {term}", f"Sprawdź definicję: {term}"))
        else:
            pairs.append(("Zła nazwa pojęcia", "Sprawdź kartę hasła"))
    return pairs[:4]


def nie_pomyl(card: dict) -> list[tuple[str, str]]:
    if card.get("nie_pomyl"):
        # optional explicit in data: list of "a|b" or tuples
        raw = card["nie_pomyl"]
        out = []
        for item in raw:
            if isinstance(item, (list, tuple)) and len(item) >= 2:
                out.append((str(item[0]), str(item[1])))
            elif isinstance(item, str) and "|" in item:
                a, b = item.split("|", 1)
                out.append((a.strip(), b.strip()))
        if out:
            return out[:4]
    key = (card.get("pl") or "").strip()
    key_l = key.lower()
    if key_l in NIE_POMYL:
        pairs = [(a, b) for a, b in NIE_POMYL[key_l] if a]
        return pairs[:4]
    # dopasowanie po najdłuższym kluczu (prefiks / cały wyraz) — bez „liczba”⊂„liczba wymierna”
    candidates: list[tuple[int, list]] = []
    for k, pairs in NIE_POMYL.items():
        if key_l == k:
            return [(a, b) for a, b in pairs if a][:4]
        if key_l.startswith(k + " ") or key_l.endswith(" " + k) or f" {k} " in f" {key_l} ":
            # tylko gdy k ma ≥ 5 znaków (unikaj „suma”, „pole” w dłuższych frazach przypadkiem OK jeśli całe słowo)
            if len(k) >= 5:
                candidates.append((len(k), pairs))
    if candidates:
        candidates.sort(key=lambda x: -x[0])
        return [(a, b) for a, b in candidates[0][1] if a][:4]
    return _fallback_nie_pomyl(card)


def przyklady(card: dict) -> list[str]:
    """4–6 przykładów ZASTOSOWANIA (nie powtórka definicji)."""
    from examples_bank import examples_for

    term = (card.get("pl") or "").strip()
    bank = examples_for(term)
    if bank:
        clean = []
        seen = set()
        for b in bank:
            b = _strip_html(str(b))
            if len(b) > 48:
                b = b[:45] + "…"
            key = b.lower()
            if not b or key in seen or b in {"…", "—", "..."}:
                continue
            # odrzuć gołe liczby
            if re.fullmatch(r"\d+[.,]?\d*", b):
                continue
            seen.add(key)
            clean.append(b)
        if len(clean) >= 4:
            return clean[:6]

    # jawna lista na karcie (jeśli autor podał)
    bits: list[str] = []
    for src in (card.get("przykłady"), card.get("examples")):
        if isinstance(src, list):
            bits.extend(str(x).strip() for x in src if str(x).strip())
        elif src:
            bits.extend(_split_bits(str(src)))

    # visual tylko jeśli wygląda na zastosowanie (ma kontekst: strzałka, ✔, słowo, wzór)
    vis = _strip_html(card.get("visual") or "")
    for b in _split_bits(vis):
        if re.fullmatch(r"\d+[.,]?\d*", b):
            continue
        if re.search(
            r"[a-zA-ZąćęłńóśźżА-яіІїЇєЄ]|[<>≤≥=≠→✔✖]|cm|kg|zł|°|√|π|∈",
            b,
            flags=re.I,
        ):
            bits.append(b)

    clean = []
    seen = set()
    for b in bits:
        b = _strip_html(b)
        if len(b) > 48:
            b = b[:45] + "…"
        key = b.lower()
        if not b or key in seen or b in {"…", "—", "..."}:
            continue
        if re.fullmatch(r"\d+[.,]?\d*", b):
            continue
        seen.add(key)
        clean.append(b)

    # ostatnia deska: mini-zadania z nazwy hasła (bez losowych liczb)
    if len(clean) < 4 and term:
        for extra in (
            f"rozpoznaj: {term}",
            f"zadanie: użyj „{term}”",
            f"porównaj z podobnym pojęciem",
            f"podaj własny przykład",
        ):
            if extra.lower() not in seen:
                clean.append(extra[:48])
                seen.add(extra.lower())
            if len(clean) >= 4:
                break

    while len(clean) < 4:
        clean.append("zadanie z podręcznika")

    return clean[:6]


def present_card(card: dict) -> dict:
    """Zwraca bloki gotowe do HTML."""
    co_pl, co_ua = co_to_jest(card)
    zap_pl, zap_ua = zapamietaj(card)
    return {
        "co_pl": co_pl,
        "co_ua": co_ua,
        "zap_pl": zap_pl,
        "zap_ua": zap_ua,
        "nie_pomyl": nie_pomyl(card),
        "przyklady": przyklady(card),
    }
