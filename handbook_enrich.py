# -*- coding: utf-8 -*-
"""
Wzbogacenie treści do mini-słownika jako krótkiego podręcznika PL–UA
(wiek ~7–12, podstawa programowa SP): jasne „co to jest”, „jak w szkole”,
oraz zasady (wzory) na końcu strony.
"""
from __future__ import annotations

import re
from html import unescape


def _plain(visual: str) -> str:
    if not visual:
        return ""
    t = unescape(visual)
    t = re.sub(r"<br\s*/?>", " · ", t, flags=re.I)
    t = re.sub(r"<[^>]+>", "", t)
    return " ".join(t.split())


def _looks_formula(s: str) -> bool:
    if not s:
        return False
    return bool(re.search(r"[=≈→↔]|\d|π|√|%|×|:|/|²|³", s))


def _is_pure_formula(s: str) -> bool:
    """Czysty wzór egzaminacyjny (symbole), nie zdanie typu „Obwód = suma boków”."""
    s = (s or "").strip().rstrip(".")
    if not s or len(s) > 64 or not _looks_formula(s):
        return False
    words = re.findall(r"[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźżА-Яа-яЇїІіЄєҐґ']+", s)
    skip = {
        "lub", "oraz", "and", "abo", "або", "та", "plus", "minus", "gdy", "dla",
        "nie", "wolno",
    }
    long_words = [w for w in words if len(w) >= 4 and w.lower() not in skip]
    if len(long_words) >= 2:
        return False
    return True


def _expand_pair(pl: str, ua: str, term_pl: str) -> tuple[str, str]:
    """Jeśli wyjaśnienie jest za krótkie — dopisz kontekst dla dziecka."""
    pl = (pl or "").strip()
    ua = (ua or "").strip()
    if len(pl) >= 70:
        return pl, ua
    if len(pl) >= 45:
        # lekko domykamy myśl
        if not pl.endswith((".", "!", "…", "?")):
            pl = pl + "."
        if ua and not ua.endswith((".", "!", "…", "?", "…")):
            ua = ua + "."
        return pl, ua

    # krótkie hasła — domykamy kropką; bez szablonowego „ważne pojęcie…”
    if pl and not pl.endswith((".", "!", "…", "?")):
        pl = pl + "."
    if ua and not ua.endswith((".", "!", "…", "?")):
        ua = ua + "."
    return pl.strip(), ua.strip()


_TEMPLATE_MARKERS = (
    "Porównaj z definicją",
    "powiedz własnymi słowami",
    "Najpierw zrozum zapis, potem licz",
    "Sprawdzaj na przykładzie:",
    "W zeszycie zapisujemy:",
    "Zapisz w zeszycie i",
    "Zapisz definicję w zeszycie",
    "Порівняй з означенням",
    "скажи своїми словами",
    "Спочатку зрозумій запис, потім рахуй",
    "Перевір на прикладі:",
    "У зошиті записуємо:",
    "Запиши в зошит",
    "Запиши означення в зошит",
)


def _is_template_rule(text: str) -> bool:
    t = text or ""
    return any(m in t for m in _TEMPLATE_MARKERS)


def _school_rule(card: dict) -> tuple[str, str]:
    """Krótka kotwica Zapamiętaj (v1.0) — bez szablonów „porównaj / powiedz swoimi słowami”."""
    visual = _plain(card.get("visual") or "")
    def_pl = (card.get("def_pl") or card.get("explain") or "").strip()
    def_ua = (card.get("def_ua") or card.get("explain_ua") or "").strip()

    if visual and len(visual) <= 70:
        # UA: krótko wyjaśnij rdzeń; bez kalki szablonu
        ua = def_ua.split(".")[0].strip() if def_ua else visual
        if len(ua) > 90:
            ua = ua[:87].rsplit(" ", 1)[0] + "…"
        return visual, ua

    if def_pl:
        tip_pl = def_pl.split(".")[0].strip()
        tip_ua = def_ua.split(".")[0].strip() if def_ua else tip_pl
        if len(tip_pl) > 100:
            tip_pl = tip_pl[:97].rsplit(" ", 1)[0] + "…"
        if len(tip_ua) > 100:
            tip_ua = tip_ua[:97].rsplit(" ", 1)[0] + "…"
        return tip_pl, tip_ua

    return ("Zapamiętaj definicję z karty.", "Запам'ятай означення з картки.")


def _same_rule_text(a: str, b: str) -> bool:
    """Czy dwa teksty to ta sama zasada/wzór (ignoruj spacje, kropki, prefiksy)."""
    def norm(s: str) -> str:
        s = (s or "").strip().lower()
        s = re.sub(r"^(zapamiętaj wzór:\s*|запам'ятай формулу:\s*)", "", s)
        s = re.sub(r"[\s.]+$", "", s)
        s = re.sub(r"\s+", "", s)
        return s

    return bool(a and b and norm(a) == norm(b))


def _split_label_formula(text: str) -> tuple[str, str] | tuple[None, None]:
    """'Romb: P=a·h' → ('Romb', 'P=a·h'). Nie dziel wzorów typu 'ℚ = { a/b : … }'."""
    text = (text or "").strip()
    # Etykieta bez '=', bez '{' — samo słowo/fraza przed dwukropkiem
    m = re.match(r"^([^:={]{2,36}):\s*(.+)$", text)
    if not m:
        return None, None
    label, rest = m.group(1).strip(), m.group(2).strip().rstrip(".")
    # etykieta nie może wyglądać jak wzór
    if re.search(r"[=·×+/√²³ℚℕℤℝ]|^\d", label):
        return None, None
    if _looks_formula(rest) or re.search(r"[=·×:/²³√]|m²|ha|\d", rest):
        return label, rest
    return None, None


def _enrich_remember(items: list) -> list:
    """
    Każda zasada: formula/core = czysta rzecz do egzaminu;
    pl/ua = rozszyfrowanie / krótkie wyjaśnienie (NIE powtórka wzoru).
    """
    out = []
    for r in items:
        pl = (r.get("pl") or "").strip()
        ua = (r.get("ua") or "").strip()
        formula = (r.get("formula") or "").strip()

        pl = re.sub(r"^Zapamiętaj wzór:\s*", "", pl, flags=re.I).strip()
        ua = re.sub(r"^Запам'ятай формулу:\s*", "", ua, flags=re.I).strip()

        # „Etykieta: wzór” → wzór w ramce, etykieta w wyjaśnieniu
        if not formula:
            label, core = _split_label_formula(pl)
            if core and _is_pure_formula(core):
                formula = core
                pl = f"{label} — wzór poniżej."
                ua_label, ua_core = _split_label_formula(ua)
                if ua_core and _is_pure_formula(ua_core):
                    ua = f"{ua_label or label} — формула нижче."
            elif _is_pure_formula(pl):
                formula = pl.rstrip(".")
                pl = "Znaczenie liter we wzorze — jak w podręczniku."
                if not ua or _same_rule_text(ua, formula) or _is_pure_formula(ua):
                    ua = "Значення літер у формулі — як у підручнику."

        # Jeśli wyjaśnienie = sam wzór → krótkie rozszyfrowanie (bez porad)
        if formula and _same_rule_text(pl, formula):
            pl = "Wzór — litery jak w zadaniu / podręczniku."
        if formula and ua and _same_rule_text(ua, formula):
            ua = "Формула — літери як у задачі / підручнику."

        if pl and not pl.endswith((".", "!", "…", "?")) and len(pl) < 100:
            pl = pl + "."
        if ua and not ua.endswith((".", "!", "…", "?")) and len(ua) < 100:
            ua = ua + "."

        d = {"pl": pl, "ua": ua}
        if formula:
            d["formula"] = formula.rstrip(".")
        out.append(d)
    return out


# Ręcznie dopracowane wzory / zasady końcowe (nadpisują remember, gdy podane)
PAGE_RULES = {
    1: [
        {"pl": "Liczymy: jabłka, dzieci, kroki.", "ua": "Лічимо: яблука, дітей, кроки."},
        {"pl": "Cyfr jest 10 (0–9). Z nich budujesz liczby.", "ua": "Цифр 10 (0–9). З них будуєш числа.", "formula": "cyfra ≠ liczba"},
        {"pl": "Miejsce cyfry = ile jest warta (palce, klocki).", "ua": "Місце цифри = скільки варта (пальці, кубики).", "formula": "23 = 2 dziesiątki + 3"},
        {"pl": "Pierwszy, drugi… = kolejność (liczba porządkowa).", "ua": "Перший, другий… = порядок (порядкове число)."},
        {"pl": "Zero = pusto; w szkole pytaj o 0 w naturalnych.", "ua": "Нуль = порожньо; у школі питай про 0 у натуральних."},
    ],
    2: [
        {"pl": "Siedem liter-znaków: I V X L C D M.", "ua": "Сім літер-знаків: I V X L C D M.", "formula": "I=1 V=5 X=10"},
        {"pl": "Mniejszy znak po prawej → dodaj (VI=6).", "ua": "Менший знак праворуч → додай (VI=6).", "formula": "VI = 5+1"},
        {"pl": "Mniejszy znak po lewej → odejmij (IV=4).", "ua": "Менший знак ліворуч → відніми (IV=4).", "formula": "IV = 5−1"},
        {"pl": "Widzisz je na zegarach i w książkach.", "ua": "Бачиш їх на годинниках і в книгах."},
    ],
    3: [
        {"pl": "Liczby całkowite: naturalne, zero i ujemne.", "ua": "Цілі числа: натуральні, нуль і від'ємні."},
        {"pl": "Wartość bezwzględna = odległość od zera.", "ua": "Модуль = відстань від нуля.", "formula": "|a|"},
        {"pl": "Odejmowanie = dodawanie liczby przeciwnej.", "ua": "Віднімання = додавання протилежного.", "formula": "a−b = a+(−b)"},
        {"pl": "Na osi: im bardziej w lewo, tym mniejsza liczba.", "ua": "На прямій: що лівіше — то менше число."},
    ],
    4: [
        {"pl": "Dodawanie = „ile razem?”", "ua": "Додавання = «скільки разом?»", "formula": "3 + 5 = 8"},
        {"pl": "Odejmowanie = „ile zostanie?”", "ua": "Віднімання = «скільки лишиться?»", "formula": "9 − 4 = 5"},
        {"pl": "Suma to wynik + ; różnica to wynik −.", "ua": "Сума — результат + ; різниця — результат −."},
        {"pl": "Sprawdź odejmowanie dodawaniem.", "ua": "Перевір віднімання додаванням.", "formula": "5 + 4 = 9"},
    ],
    5: [
        {"pl": "Mnożenie = szybkie dodawanie tej samej liczby.", "ua": "Множення = швидке додавання того самого числа.", "formula": "4×3 = 4+4+4"},
        {"pl": "Wynik mnożenia to iloczyn.", "ua": "Результат множення — добуток.", "formula": "2 × 5 = 10"},
        {"pl": "×0 = 0; ×1 = ta sama liczba.", "ua": "×0 = 0; ×1 = те саме число.", "formula": "a×0=0 · a×1=a"},
        {"pl": "Ucz się tabliczki po trochu codziennie.", "ua": "Вчи таблицю потроху щодня."},
    ],
    6: [
        {"pl": "Dzielenie = równe części („po ile?”).", "ua": "Ділення = рівні частини («по скільки?»).", "formula": "12 : 3 = 4"},
        {"pl": "Nigdy nie dziel przez zero.", "ua": "Ніколи не діли на нуль.", "formula": "nie wolno : 0"},
        {"pl": "Sprawdź dzielenie mnożeniem.", "ua": "Перевір ділення множенням.", "formula": "4 × 3 = 12"},
        {"pl": "Czasem zostaje reszta.", "ua": "Іноді лишається остача.", "formula": "17 : 5 = 3 r. 2"},
    ],
    7: [
        {"pl": "Najpierw nawiasy.", "ua": "Спочатку дужки.", "formula": "1. ( )"},
        {"pl": "Potem potęgi.", "ua": "Потім степені.", "formula": "2. aⁿ"},
        {"pl": "Następnie mnożenie i dzielenie (od lewej).", "ua": "Далі множення і ділення (зліва).", "formula": "3. × :"},
        {"pl": "Na końcu dodawanie i odejmowanie (od lewej).", "ua": "Наприкінці додавання і віднімання (зліва).", "formula": "4. + −"},
    ],
    8: [
        {"pl": "Przez 2: ostatnia cyfra parzysta.", "ua": "На 2: остання цифра парна."},
        {"pl": "Przez 3 i 9: suma cyfr podzielna przez 3 lub 9.", "ua": "На 3 і 9: сума цифр ділиться на 3 або 9."},
        {"pl": "Przez 5: końcówka 0 lub 5; przez 10: tylko 0.", "ua": "На 5: кінець 0 або 5; на 10: лише 0."},
        {"pl": "Liczba pierwsza ma dokładnie dwa dzielniki: 1 i siebie.", "ua": "Просте число має рівно два дільники: 1 і себе."},
    ],
    9: [
        {"pl": "Licznik — ile części bierzemy.", "ua": "Чисельник — скільки частин беремо."},
        {"pl": "Mianownik — na ile równych części podzielono całość.", "ua": "Знаменник — на скільки рівних частин поділено ціле."},
        {"pl": "Mianownik nigdy nie może być zerem.", "ua": "Знаменник ніколи не може бути нулем.", "formula": "mianownik ≠ 0"},
    ],
    10: [
        {"pl": "Skracanie: dzielimy licznik i mianownik tą samą liczbą ≠ 0.", "ua": "Скорочення: ділимо чисельник і знаменник тим самим ≠ 0.", "formula": "÷"},
        {"pl": "Rozszerzanie: mnożymy licznik i mianownik tą samą liczbą ≠ 0.", "ua": "Розширення: множимо чисельник і знаменник тим самим ≠ 0.", "formula": "×"},
        {"pl": "Skracanie i rozszerzanie nie zmieniają wartości ułamka.", "ua": "Скорочення й розширення не змінюють значення дробу."},
    ],
    11: [
        {"pl": "Przecinek oddziela część całkowitą od części ułamkowej.", "ua": "Кома відокремлює цілу частину від дробової."},
        {"pl": "0,5 = 1/2 = 50%.", "ua": "0,5 = 1/2 = 50%.", "formula": "0,5 = 1/2 = 50%"},
        {"pl": "Zera na końcu po przecinku nie zmieniają wartości.", "ua": "Нулі в кінці після коми не змінюють значення.", "formula": "0,5 = 0,50"},
    ],
    12: [
        {"pl": "Przy +/− najpierw wspólny mianownik.", "ua": "При +/− спочатку спільний знаменник."},
        {"pl": "Mnożenie: licznik×licznik, mianownik×mianownik.", "ua": "Множення: чисельник×чисельник, знаменник×знаменник."},
        {"pl": "Dzielenie ułamków = mnożenie przez odwrotność.", "ua": "Ділення дробів = множення на обернений.", "formula": "a/b : c/d = a/b × d/c"},
    ],
    13: [
        {"pl": "Potęga to iloczyn jednakowych czynników.", "ua": "Степінь — добуток однакових множників.", "formula": "aⁿ = a·a·… (n razy)"},
        {"pl": "a¹ = a; a⁰ = 1 (gdy a ≠ 0).", "ua": "a¹ = a; a⁰ = 1 (коли a ≠ 0).", "formula": "a¹=a · a⁰=1"},
        {"pl": "Przy × potęg o tej samej podstawie dodajemy wykładniki.", "ua": "При × степенів з тією самою основою додаємо показники.", "formula": "aᵐ·aⁿ = aᵐ⁺ⁿ"},
    ],
    14: [
        {"pl": "Pierwiastek kwadratowy „odwraca” podnoszenie do kwadratu.", "ua": "Квадратний корінь «повертає» піднесення до квадрата.", "formula": "(√a)² = a"},
        {"pl": "W szkole podstawowej: a ≥ 0.", "ua": "У початковій школі: a ≥ 0."},
        {"pl": "Warto znać kwadraty doskonałe do 10².", "ua": "Варто знати повні квадрати до 10².", "formula": "1,4,9,16,25,36,49,64,81,100"},
    ],
    15: [
        {"pl": "1% = 1/100 = 0,01.", "ua": "1% = 1/100 = 0,01.", "formula": "1% = 1/100"},
        {"pl": "p% z liczby a = a · p / 100.", "ua": "p% від числа a = a · p / 100.", "formula": "p% z a = a·p/100"},
        {"pl": "100% to całość.", "ua": "100% — це ціле.", "formula": "100% = całość"},
    ],
    16: [
        {"pl": "Przy proporcjonalności prostej stosunek jest stały.", "ua": "При прямій пропорційності відношення стале.", "formula": "y = k·x"},
        {"pl": "Wykres to prosta przez punkt (0,0).", "ua": "Графік — пряма через точку (0,0)."},
        {"pl": "W proporcji: iloczyn skrajnych = iloczyn środkowych.", "ua": "У пропорції: добуток крайніх = добуток середніх.", "formula": "a/b = c/d → a·d = b·c"},
    ],
    17: [
        {"pl": "Litera w wyrażeniu to zmienna.", "ua": "Літера у виразі — змінна."},
        {"pl": "Aby obliczyć wartość, podstaw liczbę zamiast litery.", "ua": "Щоб обчислити значення, підстав число замість літери."},
        {"pl": "Zapis 3x oznacza 3 · x.", "ua": "Запис 3x означає 3 · x.", "formula": "3x = 3·x"},
    ],
    18: [
        {"pl": "Wyrazy podobne mają te same litery z tymi samymi wykładnikami.", "ua": "Подібні доданки мають ті самі літери з тими самими показниками."},
        {"pl": "Redukcja: dodajemy współczynniki wyrazów podobnych.", "ua": "Зведення: додаємо коефіцієнти подібних доданків.", "formula": "3x+5x=8x"},
        {"pl": "Celem jest uproszczenie zapisu.", "ua": "Мета — спрощення запису."},
    ],
    19: [
        {"pl": "Cel równania: znaleźć niewiadomą.", "ua": "Мета рівняння: знайти невідоме."},
        {"pl": "To samo działanie wykonujemy po obu stronach równości.", "ua": "Ту саму дію виконуємо з обох боків рівності."},
        {"pl": "Zawsze sprawdzaj rozwiązanie przez podstawienie.", "ua": "Завжди перевіряй розв'язок підставлянням."},
    ],
    20: [
        {"pl": "Długość: m, cm, mm, km.", "ua": "Довжина: m, cm, mm, km.", "formula": "1 m = 100 cm"},
        {"pl": "1 km = 1000 m.", "ua": "1 km = 1000 m.", "formula": "1 km = 1000 m"},
        {"pl": "Porównuj w tych samych jednostkach.", "ua": "Порівнюй в однакових одиницях."},
    ],
    21: [
        {"pl": "Masa: kg i g.", "ua": "Маса: kg і g.", "formula": "1 kg = 1000 g"},
        {"pl": "1 t = 1000 kg.", "ua": "1 t = 1000 kg.", "formula": "1 t = 1000 kg"},
        {"pl": "Porównuj w tej samej jednostce.", "ua": "Порівнюй в тій самій одиниці."},
    ],
    22: [
        {"pl": "1 l = 1000 ml = 1000 cm³.", "ua": "1 l = 1000 ml = 1000 cm³.", "formula": "1 l = 1000 ml"},
        {"pl": "Objętość mówi, ile miejsca zajmuje ciało lub ciecz.", "ua": "Об'єм каже, скільки місця займає тіло або рідина."},
        {"pl": "Objętość prostopadłościanu: V = a · b · c.", "ua": "Об'єм прямокутного паралелепіпеда: V = a · b · c.", "formula": "V = a·b·c"},
    ],
    23: [
        {"pl": "60 s = 1 min; 60 min = 1 h.", "ua": "60 с = 1 хв; 60 хв = 1 год.", "formula": "60–60"},
        {"pl": "Przerwa ~15 min, lekcja ~45 min.", "ua": "Перерва ~15 хв, урок ~45 хв."},
        {"pl": "Czas liczymy „po 60”, nie po 100.", "ua": "Час рахуємо «по 60», не по 100."},
    ],
    24: [
        {"pl": "Tydzień = 7 dni.", "ua": "Тиждень = 7 днів.", "formula": "7 dni"},
        {"pl": "Urodziny i ferie — szukaj w kalendarzu.", "ua": "День народження і канікули — шукай у календарі."},
        {"pl": "Przestępny: luty ma 29 dni.", "ua": "Високосний: лютий має 29 днів."},
    ],
    25: [
        {"pl": "W szkole temperaturę podajemy w °C.", "ua": "У школі температуру подаємо в °C.", "formula": "°C"},
        {"pl": "Temperatury ujemne = poniżej zera.", "ua": "Від'ємні температури = нижче нуля."},
        {"pl": "Różnica temperatur: |t₂ − t₁|.", "ua": "Різниця температур: |t₂ − t₁|.", "formula": "|t₂ − t₁|"},
    ],
    26: [
        {"pl": "1 złoty = 100 groszy.", "ua": "1 злотий = 100 грошів.", "formula": "1 zł = 100 gr"},
        {"pl": "Bułka 5 zł — ile zostaje z 10 zł?", "ua": "Булочка 5 zł — скільки лишається з 10 zł?"},
        {"pl": "Reszta = ile dałeś − cena.", "ua": "Решта = скільки дав − ціна."},
    ],
    27: [
        {"pl": "Prędkość = droga / czas.", "ua": "Швидкість = шлях / час.", "formula": "v = s/t"},
        {"pl": "Droga = prędkość · czas; czas = droga / prędkość.", "ua": "Шлях = швидкість · час; час = шлях / швидкість.", "formula": "s=v·t · t=s/v"},
        {"pl": "Skala 1:n oznacza pomniejszenie n razy.", "ua": "Масштаб 1:n означає зменшення в n разів."},
    ],
    28: [
        {"pl": "Okno = prostokąt, znak = trójkąt — figury wokół nas.", "ua": "Вікно = прямокутник, знак = трикутник — фігури навколо."},
        {"pl": "Punkt = miejsce (kropka).", "ua": "Точка = місце (крапка)."},
        {"pl": "Odcinek ma 2 końce; prostą ciągniesz bez końca.", "ua": "Відрізок має 2 кінці; пряму тягнеш без кінця."},
        {"pl": "Wielokąt = zamknięta figura z odcinków.", "ua": "Многокутник = замкнена фігура з відрізків."},
    ],
    29: [
        {"pl": "Dach, drzwi, kafelek — szukaj figur wokół siebie.", "ua": "Дах, двері, плитка — шукай фігури навколо себе."},
        {"pl": "Suma kątów w trójkącie = 180°.", "ua": "Сума кутів у трикутнику = 180°.", "formula": "180°"},
        {"pl": "Kwadrat: 4 równe boki i 4 kąty proste.", "ua": "Квадрат: 4 рівні сторони і 4 прямі кути."},
    ],
    61: [
        {"pl": "Najpierw ustal, względem czego porównujesz.", "ua": "Спочатку з'ясуй, відносно чого порівнюєш."},
        {"pl": "Prawo/lewo na sobie sprawdź na obrazku.", "ua": "Право/ліво на собі перевір на малюнку."},
        {"pl": "Porównuj długość z długością, ciężar z ciężarem.", "ua": "Порівнюй довжину з довжиною, вагу з вагою."},
    ],
    30: [
        {"pl": "Średnica = 2 · promień.", "ua": "Діаметр = 2 · радіус.", "formula": "d = 2r"},
        {"pl": "Okrąg to linia; koło to okrąg z wnętrzem.", "ua": "Коло — лінія; круг — коло зсерединою."},
        {"pl": "Wszystkie promienie tego samego okręgu są równe.", "ua": "Усі радіуси того самого кола рівні."},
    ],
    31: [
        {"pl": "π ≈ 3,14.", "ua": "π ≈ 3,14.", "formula": "π ≈ 3,14"},
        {"pl": "Długość okręgu: C = 2πr = πd.", "ua": "Довжина кола: C = 2πr = πd.", "formula": "C = 2πr"},
        {"pl": "Pole koła: P = πr².", "ua": "Площа круга: P = πr².", "formula": "P = πr²"},
    ],
    32: [
        {"pl": "Kąt = dwie półproste o wspólnym wierzchołku.", "ua": "Кут = дві півпрямі зі спільною вершиною."},
        {"pl": "Miara kąta: stopień (°).", "ua": "Міра кута: градус (°).", "formula": "°"},
        {"pl": "Pełny obrót = 360°.", "ua": "Повний оберт = 360°.", "formula": "360°"},
    ],
    33: [
        {"pl": "Kąt ostry < 90° < kąt rozwarty.", "ua": "Гострий кут < 90° < тупий кут."},
        {"pl": "Kąt prosty = 90°.", "ua": "Прямий кут = 90°.", "formula": "90°"},
        {"pl": "Półpełny = 180°; pełny = 360°.", "ua": "Розгорнутий = 180°; повний = 360°.", "formula": "180° · 360°"},
    ],
    34: [
        {"pl": "Przy prostych równoległych kąty odpowiadające są równe.", "ua": "При паралельних прямих відповідні кути рівні."},
        {"pl": "Kąty naprzemianległe są równe.", "ua": "Навхрест лежачі кути рівні."},
        {"pl": "Kąty przyległe: suma 180°.", "ua": "Суміжні кути: сума 180°.", "formula": "α + β = 180°"},
    ],
    35: [
        {"pl": "Obwód = suma długości boków.", "ua": "Периметр = сума довжин сторін."},
        {
            "pl": "Pole prostokąta: a i b to długości boków.",
            "ua": "Площа прямокутника: a і b — довжини сторін.",
            "formula": "P = a·b",
        },
        {
            "pl": "Pole trójkąta: a = podstawa, h = wysokość.",
            "ua": "Площа трикутника: a = основа, h = висота.",
            "formula": "P = (a·h)/2",
        },
    ],
    36: [
        {"pl": "Bryła ma trzy wymiary i objętość.", "ua": "Тіло має три виміри й об'єм."},
        {
            "pl": "Objętość sześcianu: a = długość krawędzi.",
            "ua": "Об'єм куба: a = довжина ребра.",
            "formula": "V = a³",
        },
        {
            "pl": "Objętość prostopadłościanu: a, b, c = krawędzie.",
            "ua": "Об'єм прямокутного паралелепіпеда: a, b, c = ребра.",
            "formula": "V = a·b·c",
        },
    ],
    37: [
        {"pl": "Oś symetrii działa jak lustro.", "ua": "Вісь симетрії діє як дзеркало."},
        {"pl": "Odległości punktów od osi po obu stronach są równe.", "ua": "Відстані точок від осі з обох боків рівні."},
        {"pl": "Kwadrat ma 4 osie symetrii.", "ua": "Квадрат має 4 осі симетрії."},
    ],
    38: [
        {"pl": "Punkt zapisujemy jako (x, y).", "ua": "Точку записуємо як (x, y).", "formula": "(x, y)"},
        {"pl": "Oś X: w prawo +; oś Y: w górę +.", "ua": "Вісь X: праворуч +; вісь Y: вгору +."},
        {"pl": "Początek układu to O(0, 0).", "ua": "Початок координат — O(0, 0).", "formula": "O(0,0)"},
    ],
    39: [
        {"pl": "Dane najpierw zbieramy i porządkujemy.", "ua": "Дані спочатку збираємо й упорядковуємо."},
        {"pl": "Wykres pomaga zobaczyć zależności.", "ua": "Графік допомагає побачити залежності."},
        {"pl": "Po analizie wyciągamy wnioski.", "ua": "Після аналізу робимо висновки."},
    ],
    40: [
        {"pl": "Średnia = suma wartości / ich liczba.", "ua": "Середнє = сума значень / їх кількість.", "formula": "średnia = suma / n"},
        {"pl": "Mediana = wartość środkowa po uporządkowaniu.", "ua": "Медіана = значення посередині після впорядкування."},
        {"pl": "Moda = wartość najczęstsza.", "ua": "Мода = найчастіше значення."},
    ],
    41: [
        {"pl": "Etapy niezależne mnożymy (zasada mnożenia).", "ua": "Незалежні етапи множимо (правило множення)."},
        {"pl": "Prawdopodobieństwo = liczba korzystnych / liczba wszystkich.", "ua": "Ймовірність = число сприятливих / число всіх.", "formula": "P = korzystne / wszystkie"},
        {"pl": "0 ≤ P ≤ 1.", "ua": "0 ≤ P ≤ 1.", "formula": "0 ≤ P ≤ 1"},
    ],
    42: [
        {"pl": "Znaki skracają i ujednolicają zapis matematyczny.", "ua": "Знаки скорочують і уніфікують математичний запис."},
        {"pl": "Najpierw opanuj: + − × : = < >.", "ua": "Спочатку опануй: + − × : = < >."},
        {"pl": "Potem poznaj: √ ² % π ∠ ∥.", "ua": "Потім пізнай: √ ² % π ∠ ∥."},
    ],
}


# Wybrane karty: pełniejsze wyjaśnienia + „jak w szkole” (klucz: (nr_strony, hasło_pl))
# Klasy 1–3: język konkretny, z życia — dziecko od razu wie, „co to jest”.
CARD_OVERRIDES = {
    # ——— strona 1: Liczby naturalne ———
    (1, "liczba naturalna"): {
        "def_pl": "To liczby do liczenia rzeczy: 1 jabłko, 2 dzieci, 3 kroki. Zaczynamy od 1 i idziemy dalej: 1, 2, 3, 4…",
        "def_ua": "Це числа для лічби речей: 1 яблуко, 2 дитини, 3 кроки. Починаємо від 1 і далі: 1, 2, 3, 4…",
        "rule": "W klasach 1–3 liczymy nimi przedmioty. W wielu podręcznikach ℕ zaczyna się od 1; czasem umowa szkolna obejmuje też 0.",
        "rule_ua": "У класах 1–3 ними лічимо предмети. У багатьох підручниках ℕ починається від 1; інколи шкільна домовленість включає й 0.",
    },
    (1, "cyfra"): {
        "def_pl": "Cyfra to „klocek” do budowania liczb. Jest ich tylko dziesięć: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.",
        "def_ua": "Цифра — «цеглинка» для чисел. Їх лише десять: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.",
        "rule": "3 to cyfra i mała liczba. 35 to już liczba z dwóch cyfr. Cyfra ≠ liczba!",
        "rule_ua": "3 — цифра і мале число. 35 — число з двох цифр. Цифра ≠ число!",
    },
    (1, "liczba"): {
        "def_pl": "Liczba mówi, ile czegoś jest. Może być krótka (7) albo długa (347).",
        "def_ua": "Число каже, скільки чогось є. Може бути коротким (7) або довгим (347).",
        "rule": "Czytamy od lewej: najpierw większe „paczki” (setki), potem dziesiątki, na końcu jednostki.",
        "rule_ua": "Читаємо зліва: спочатку більші «пакунки» (сотні), потім десятки, в кінці одиниці.",
    },
    (1, "wartość pozycyjna"): {
        "def_pl": "To samo „3” znaczy co innego zależnie od miejsca: w 347 to 3 setki, a nie 3 jednostki. Jak klocki: paczka dziesiątek i osobne jedności.",
        "def_ua": "Те саме «3» означає різне залежно від місця: у 347 це 3 сотні, а не 3 одиниці. Як кубики: пачка десятків і окремі одиниці.",
        "rule": "Na palcach lub klockach: 23 = 2 dziesiątki + 3 jedności. Im bardziej w lewo, tym „mocniejsze” miejsce.",
        "rule_ua": "На пальцях або кубиках: 23 = 2 десятки + 3 одиниці. Що лівіше — то «сильніше» місце.",
    },
    (1, "liczba porządkowa"): {
        "def_pl": "Liczba porządkowa mówi o kolejności: pierwszy, drugi, trzeci… — nie „ile”, tylko „który z kolei”.",
        "def_ua": "Порядкове число каже про порядок: перший, другий, третій… — не «скільки», а «який за порядком».",
        "rule": "W wyścigu: kto dobiegł pierwszy? To liczba porządkowa. Ile dzieci biegło? To liczba naturalna.",
        "rule_ua": "На перегонах: хто прибіг перший? Це порядкове. Скільки дітей бігло? Це натуральне.",
    },
    (1, "zero"): {
        "def_pl": "Zero = nic / pusto (0 cukierków). W kl. 1–3 bywa umowa: liczby naturalne od 1 albo od 0 — ważne, jak w Twojej klasie.",
        "def_ua": "Нуль = нічого / порожньо (0 цукерок). У кл. 1–3 буває домовленість: натуральні від 1 або від 0 — важливо, як у твоєму класі.",
        "rule": "0 to cyfra i specjalna liczba. Nie dziel przez zero!",
        "rule_ua": "0 — цифра і особливе число. Не діли на нуль!",
    },
    (1, "parzysta / nieparzysta"): {
        "def_pl": "Parzysta dzieli się równo na 2 (jak pary skarpetek). Nieparzysta — zostaje 1 „bez pary”.",
        "def_ua": "Парне ділиться порівну на 2 (як пари шкарпеток). Непарне — лишається 1 «без пари».",
        "rule": "Patrz tylko na ostatnią cyfrę: 0,2,4,6,8 → parzysta; 1,3,5,7,9 → nieparzysta.",
        "rule_ua": "Дивись лише на останню цифру: 0,2,4,6,8 → парне; 1,3,5,7,9 → непарне.",
    },
    (1, "porównanie"): {
        "def_pl": "Porównanie odpowiada: która liczba jest mniejsza, równa albo większa.",
        "def_ua": "Порівняння відповідає: яке число менше, рівне чи більше.",
        "rule": "Znak < i > ma „otwarty dziób” w stronę większej liczby: 3 < 7, 9 > 2.",
        "rule_ua": "Знак < і > має «відкритий рот» до більшого числа: 3 < 7, 9 > 2.",
    },
    (1, "zaokrąglanie"): {
        "def_pl": "Zaokrąglanie to zamiana liczby na bliską, wygodną (np. łatwiej myśleć o 50 niż o 47).",
        "def_ua": "Округлення — заміна числа на близьке, зручне (напр. легше думати про 50, ніж про 47).",
        "rule": "Patrz na następną cyfrę: 0–4 → w dół; 5–9 → w górę. Przykład: 47 → 50.",
        "rule_ua": "Дивись на наступну цифру: 0–4 → вниз; 5–9 → вгору. Приклад: 47 → 50.",
    },
    (1, "następnik / poprzednik"): {
        "def_pl": "Poprzednik to liczba o 1 mniejsza. Następnik to liczba o 1 większa.",
        "def_ua": "Попередник — число на 1 менше. Наступник — число на 1 більше.",
        "rule": "Na osi liczbowej: sąsiad z lewej (poprzednik) i z prawej (następnik). Dla 9: 8 i 10.",
        "rule_ua": "На числовій прямій: сусід зліва (попередник) і справа (наступник). Для 9: 8 і 10.",
    },
    (1, "kolejność liczb"): {
        "def_pl": "Kolejność to układanie liczb od najmniejszej do największej (albo odwrotnie).",
        "def_ua": "Порядок — розкладання чисел від найменшого до найбільшого (або навпаки).",
        "rule": "Porównuj po kolei albo ustaw liczby na osi — od razu widać porządek.",
        "rule_ua": "Порівнюй по черзі або постав числа на пряму — одразу видно порядок.",
    },
    # ——— strona 2: Liczby rzymskie (lekko, jak w klasie 2–3) ———
    (2, "Podstawowe znaki"): {
        "def_pl": "Dawniej Rzymianie pisali liczby literami. Siedem znaków wystarczy, by złożyć inne liczby.",
        "def_ua": "Колись римляни писали числа літерами. Семи знаків досить, щоб скласти інші числа.",
        "rule": "Zapamiętaj jak piosenkę: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.",
        "rule_ua": "Запам'ятай як пісню: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.",
    },
    (2, "Przykłady"): {
        "def_pl": "Liczbę rzymską składamy ze znaków obok siebie — jak klocki.",
        "def_ua": "Римське число складаємо зі знаків поруч — як кубики.",
        "rule": "Przykłady: 1=I, 4=IV, 9=IX, 14=XIV, 50=L, 100=C.",
        "rule_ua": "Приклади: 1=I, 4=IV, 9=IX, 14=XIV, 50=L, 100=C.",
    },
    (2, "Składanie liczb"): {
        "def_pl": "Liczbę rzymską składamy ze znaków obok siebie — jak klocki.",
        "def_ua": "Римське число складаємо зі знаків поруч — як кубики.",
        "rule": "1=I, 4=IV, 9=IX, 14=XIV, 50=L, 100=C.",
        "rule_ua": "1=I, 4=IV, 9=IX, 14=XIV, 50=L, 100=C.",
    },
    (2, "Dodawanie znaków"): {
        "def_pl": "Gdy mniejszy znak stoi po prawej — dodajemy wartości (jak dokładanie klocków).",
        "def_ua": "Коли менший знак стоїть праворуч — додаємо значення (як докладання кубиків).",
        "rule": "VI = V + I = 6. Najpierw większy, potem dokładamy mniejszy z prawej.",
        "rule_ua": "VI = V + I = 6. Спочатку більший, потім докладаємо менший справа.",
    },
    (2, "Odejmowanie znaków"): {
        "def_pl": "Gdy mniejszy znak stoi tuż przed większym — odejmujemy (to skrót zapisu).",
        "def_ua": "Коли менший знак стоїть одразу перед більшим — віднімаємо (це скорочений запис).",
        "rule": "IV = 5 − 1 = 4; IX = 10 − 1 = 9. Do odejmowania: tylko I, X, C.",
        "rule_ua": "IV = 5 − 1 = 4; IX = 10 − 1 = 9. Для віднімання: лише I, X, C.",
    },
    (2, "Ograniczenia"): {
        "def_pl": "Nie każdy znak może stać przed większym. Są proste reguły — jak przepisy gry.",
        "def_ua": "Не кожен знак може стояти перед більшим. Є прості правила — як правила гри.",
        "rule": "I tylko przed V i X; X przed L i C; C przed D i M.",
        "rule_ua": "I лише перед V і X; X перед L і C; C перед D і M.",
    },
    (2, "Większe przykłady"): {
        "def_pl": "Większe liczby czytamy od lewej: czasem dodajemy, czasem odejmujemy według zasad.",
        "def_ua": "Більші числа читаємо зліва: іноді додаємо, іноді віднімаємо за правилами.",
        "rule": "44=XLIV, 99=XCIX, 2024=MMXXIV. Idź znak po znaku.",
        "rule_ua": "44=XLIV, 99=XCIX, 2024=MMXXIV. Іди знак за знаком.",
    },
    (2, "Gdzie spotykamy?"): {
        "def_pl": "Liczby rzymskie wciąż żyją wokół nas — nie tylko w podręczniku.",
        "def_ua": "Римські числа досі живуть навколо нас — не лише в підручнику.",
        "rule": "Szukaj na zegarach, w numerach rozdziałów, na pomnikach i w tytułach filmów.",
        "rule_ua": "Шукай на годинниках, у номерах розділів, на пам'ятниках і в назвах фільмів.",
    },
    (2, "Zamiana na arabskie"): {
        "def_pl": "Zamiana na „zwykłe” liczby: czytamy, odejmujemy gdy trzeba, dodajemy i sumujemy.",
        "def_ua": "Перетворення на «звичайні» числа: читаємо, віднімаємо коли треба, додаємо і підсумовуємо.",
        "rule": "LXIV → 50+10+4 = 64. Zapisz kroki w zeszycie.",
        "rule_ua": "LXIV → 50+10+4 = 64. Запиши кроки в зошит.",
    },
    # ——— strona 4: Dodawanie i odejmowanie ———
    (4, "dodawanie"): {
        "def_pl": "Dodawanie to łączenie: „ile będzie razem?”. Dwa worki cukierków → jeden wynik.",
        "def_ua": "Додавання — об'єднання: «скільки буде разом?». Два пакети цукерок → один результат.",
        "rule": "Piszemy: składnik + składnik = suma. 3+5 i 5+3 dają to samo.",
        "rule_ua": "Пишемо: доданок + доданок = сума. 3+5 і 5+3 дають те саме.",
    },
    (4, "suma"): {
        "def_pl": "Suma to wynik dodawania — liczba, którą dostajesz po znaku =.",
        "def_ua": "Сума — результат додавання — число, яке отримуєш після знака =.",
        "rule": "W zapisie: składnik + składnik = suma. Suma jest „razem”.",
        "rule_ua": "У записі: доданок + доданок = сума. Сума — це «разом».",
    },
    (4, "odejmowanie"): {
        "def_pl": "Odejmowanie to zabieranie: „ile zostanie?” albo „o ile więcej ma ktoś?”.",
        "def_ua": "Віднімання — забирання: «скільки лишиться?» або «на скільки більше в когось?».",
        "rule": "Piszemy: odjemna − odjemnik = różnica. Sprawdź: różnica + odjemnik = odjemna.",
        "rule_ua": "Пишемо: зменшуване − від'ємник = різниця. Перевір: різниця + від'ємник = зменшуване.",
    },
    (4, "różnica"): {
        "def_pl": "Różnica to wynik odejmowania — ile zostało po zabraniu.",
        "def_ua": "Різниця — результат віднімання — скільки лишилось після забирання.",
        "rule": "odjemna − odjemnik = różnica. Różnica to „to, co zostało”.",
        "rule_ua": "зменшуване − від'ємник = різниця. Різниця — «те, що лишилось».",
    },
    (4, "składnik"): {
        "def_pl": "Składnik to liczba, którą dodajemy. W sumie mogą być dwa lub więcej składników.",
        "def_ua": "Доданок — число, яке додаємо. У сумі може бути два або більше доданків.",
        "rule": "W 1+3=4 oba (1 i 3) to składniki. Razem dają sumę.",
        "rule_ua": "У 1+3=4 обидва (1 і 3) — доданки. Разом дають суму.",
    },
    (4, "odjemna i odjemnik"): {
        "def_pl": "Odjemna — liczba, od której zabieramy. Odjemnik — ile zabieramy.",
        "def_ua": "Зменшуване — число, від якого забираємо. Від'ємник — скільки забираємо.",
        "rule": "W 8−3=5: 8 to odjemna, 3 to odjemnik, 5 to różnica.",
        "rule_ua": "У 8−3=5: 8 — зменшуване, 3 — від'ємник, 5 — різниця.",
    },
    (4, "dodawanie na palcach / osi"): {
        "def_pl": "Jak w kl. 1–2: dodajesz na palcach albo skaczesz w prawo po osi liczbowej.",
        "def_ua": "Як у кл. 1–2: додаєш на пальцях або стрибаєш вправо по числовій прямій.",
        "rule": "3+2: pokaż 3 palce, dołóż 2 — ile razem? Albo: start 3, dwa skoki w prawo → 5.",
        "rule_ua": "3+2: покажи 3 пальці, додай 2 — скільки разом? Або: старт 3, два стрибки вправо → 5.",
    },
    (4, "odejmowanie: ile zostało"): {
        "def_pl": "Jak w kl. 1–2: miałem 9 cukierków, zabrałem 4 — ile zostało?",
        "def_ua": "Як у кл. 1–2: мав 9 цукерок, забрав 4 — скільки лишилось?",
        "rule": "Zawsze pytaj: „ile zostało?”. Sprawdź dodawaniem: 5+4=9.",
        "rule_ua": "Завжди питай: «скільки лишилось?». Перевір додаванням: 5+4=9.",
    },
    (4, "właściwości +"): {
        "def_pl": "Przy dodawaniu kolejność nie psuje wyniku — możesz przestawiać i grupować.",
        "def_ua": "При додаванні порядок не псує результату — можна переставляти і групувати.",
        "rule": "3+5=5+3. Też: (2+3)+4 = 2+(3+4). To pomaga liczyć wygodniej.",
        "rule_ua": "3+5=5+3. Також: (2+3)+4 = 2+(3+4). Це допомагає рахувати зручніше.",
    },
    (4, "właściwości −"): {
        "def_pl": "Odejmowanie zero nic nie zmienia. Odejmowanie tej samej liczby daje zero.",
        "def_ua": "Віднімання нуля нічого не змінює. Віднімання того самого числа дає нуль.",
        "rule": "a−0=a; a−a=0. Pamiętaj: odejmowanie nie jest „przemienne” jak dodawanie.",
        "rule_ua": "a−0=a; a−a=0. Пам'ятай: віднімання не «переставне», як додавання.",
    },
    (4, "przykłady"): {
        "def_pl": "Ćwiczenia utrwalają: najpierw dodawanie, potem odejmowanie — spokojnie, krok po kroku.",
        "def_ua": "Вправи закріплюють: спочатку додавання, потім віднімання — спокійно, крок за кроком.",
        "rule": "Policz: 2+3, 7+8, 8−3, 15−6. Potem wymyśl własne przykłady z życia (zabawki, cukierki).",
        "rule_ua": "Порахуй: 2+3, 7+8, 8−3, 15−6. Потім вигадай свої приклади з життя.",
    },
    # ——— strona 5: Tabliczka mnożenia ———
    (5, "mnożenie"): {
        "def_pl": "Mnożenie to szybkie dodawanie tej samej liczby. 4×3 znaczy: 4+4+4.",
        "def_ua": "Множення — швидке додавання того самого числа. 4×3 означає: 4+4+4.",
        "rule": "Zapis: czynnik × czynnik = iloczyn. Najpierw zrozum sens, potem ucz się na pamięć.",
        "rule_ua": "Запис: множник × множник = добуток. Спочатку зрозумій сенс, потім вчи напам'ять.",
    },
    (5, "mnożenie = dodawanie tej samej"): {
        "def_pl": "Trzy paczki po 4 cukierki: 4+4+4. Mnożenie to skrót takiego dodawania.",
        "def_ua": "Три пачки по 4 цукерки: 4+4+4. Множення — скорочення такого додавання.",
        "rule": "4×3 = 4+4+4 = 12. Najpierw zobacz „dodawanie tej samej”, potem ucz się tabliczki.",
        "rule_ua": "4×3 = 4+4+4 = 12. Спочатку побач «додавання тієї самої», потім вчи таблицю.",
    },
    (5, "iloczyn"): {
        "def_pl": "Iloczyn to wynik mnożenia — liczba po znaku =.",
        "def_ua": "Добуток — результат множення — число після знака =.",
        "rule": "W 2×5=10 liczba 10 to iloczyn. To „ile wyszło”.",
        "rule_ua": "У 2×5=10 число 10 — добуток. Це «скільки вийшло».",
    },
    (5, "czynnik"): {
        "def_pl": "Czynnik to liczba, którą mnożymy. W mnożeniu są zwykle dwa czynniki.",
        "def_ua": "Множник — число, яке множимо. У множенні зазвичай два множники.",
        "rule": "W 2×5=10 zarówno 2, jak i 5 to czynniki.",
        "rule_ua": "У 2×5=10 і 2, і 5 — множники.",
    },
    (5, "przemienność"): {
        "def_pl": "Kolejność czynników nie zmienia wyniku: trzy rzędy po 4 to to samo co cztery rzędy po 3.",
        "def_ua": "Порядок множників не змінює результату: три ряди по 4 — те саме, що чотири ряди по 3.",
        "rule": "3×4 = 4×3. Możesz przestawić, by było łatwiej liczyć.",
        "rule_ua": "3×4 = 4×3. Можеш переставити, щоб було легше рахувати.",
    },
    (5, "×0 i ×1"): {
        "def_pl": "Przez zero zawsze wychodzi zero. Przez jeden — ta sama liczba (nic nie „rośnie”).",
        "def_ua": "На нуль завжди виходить нуль. На один — те саме число (нічого не «росте»).",
        "rule": "a×0=0; a×1=a. Zapamiętaj na zawsze — bardzo się przydaje.",
        "rule_ua": "a×0=0; a×1=a. Запам'ятай назавжди — дуже знадобиться.",
    },
    (5, "kluczowe wyniki"): {
        "def_pl": "Niektóre wyniki warto znać „od ręki” — wtedy całe zadania idą szybciej.",
        "def_ua": "Деякі результати варто знати «з руки» — тоді всі завдання йдуть швидше.",
        "rule": "Ćwicz szczególnie: 5×5, 6×7, 7×8, 9×9. Potem całą tabliczkę 1–10.",
        "rule_ua": "Тренуй особливо: 5×5, 6×7, 7×8, 9×9. Потім усю таблицю 1–10.",
    },
    # ——— strona 6: Dzielenie ———
    (6, "dzielenie"): {
        "def_pl": "Dzielenie to sprawiedliwe rozdawanie: „po ile każdemu?” albo „ile razy się mieści?”.",
        "def_ua": "Ділення — справедливий розподіл: «по скільки кожному?» або «скільки разів вміщується?».",
        "rule": "12 : 3 = 4. Zapis: dzielna : dzielnik = iloraz. Nie dziel przez 0!",
        "rule_ua": "12 : 3 = 4. Запис: ділене : дільник = частка. Не діли на 0!",
    },
    (6, "sprawiedliwe rozdawanie"): {
        "def_pl": "Dzielenie = rozdajemy po równo: każdemu tyle samo, nic nie zostaje „na boku”.",
        "def_ua": "Ділення = роздаємо порівну: кожному стільки само, нічого не лишається «збоку».",
        "rule": "12 cukierków, 3 dzieci → po 4. To sprawiedliwe rozdawanie.",
        "rule_ua": "12 цукерок, 3 дітей → по 4. Це справедлива роздача.",
    },
    (6, "iloraz"): {
        "def_pl": "Iloraz to wynik dzielenia — ile wyszło po rozdzieleniu.",
        "def_ua": "Частка — результат ділення — скільки вийшло після розподілу.",
        "rule": "W 15:5=3 liczba 3 to iloraz.",
        "rule_ua": "У 15:5=3 число 3 — частка.",
    },
    (6, "dzielna i dzielnik"): {
        "def_pl": "Dzielna — co dzielimy. Dzielnik — na ile części (lub przez co dzielimy).",
        "def_ua": "Ділене — що ділимо. Дільник — на скільки частин (або на що ділимо).",
        "rule": "W 15:5=3: 15 to dzielna, 5 to dzielnik, 3 to iloraz.",
        "rule_ua": "У 15:5=3: 15 — ділене, 5 — дільник, 3 — частка.",
    },
    (6, "z resztą"): {
        "def_pl": "Czasem nie wychodzi równo — zostaje reszta (jak cukierki, których nie da się podzielić po równo).",
        "def_ua": "Іноді не виходить порівну — лишається остача (як цукерки, які не можна поділити порівну).",
        "rule": "17:5 = 3 reszty 2. Reszta zawsze mniejsza od dzielnika.",
        "rule_ua": "17:5 = 3 остачі 2. Остача завжди менша за дільник.",
    },
    (6, "związek z ×"): {
        "def_pl": "Dzielenie i mnożenie to para: jedno sprawdza drugie.",
        "def_ua": "Ділення і множення — пара: одне перевіряє друге.",
        "rule": "Jeśli 12:3=4, to 4×3=12. Zawsze możesz sprawdzić mnożeniem.",
        "rule_ua": "Якщо 12:3=4, то 4×3=12. Завжди можеш перевірити множенням.",
    },
    (6, ":1 i : siebie"): {
        "def_pl": "Dzielenie przez 1 nic nie zmienia. Dzielenie liczby przez siebie daje 1.",
        "def_ua": "Ділення на 1 нічого не змінює. Ділення числа на себе дає 1.",
        "rule": "a:1=a; a:a=1 (gdy a ≠ 0). Nigdy a:0!",
        "rule_ua": "a:1=a; a:a=1 (коли a ≠ 0). Ніколи a:0!",
    },
    # ——— strona 20: Długość ———
    (20, "jednostki długości"): {
        "def_pl": "Długość mówimy w metrach i „rodzinie” metra: km, m, cm, mm.",
        "def_ua": "Довжину кажемо в метрах і «родині» метра: km, m, cm, mm.",
        "rule": "W szkole podstawowa jednostka to metr (m). Linijka pokazuje cm i mm.",
        "rule_ua": "У школі основна одиниця — метр (m). Лінійка показує cm і mm.",
    },
    (20, "zamiana"): {
        "def_pl": "Żeby porównać lub dodać, zamieniamy jednostki (jak wymiana monet).",
        "def_ua": "Щоб порівняти або додати, міняємо одиниці (як обмін монет).",
        "rule": "1 km = 1000 m; 1 m = 100 cm = 1000 mm. × lub ÷ przez 10, 100, 1000…",
        "rule_ua": "1 km = 1000 m; 1 m = 100 cm = 1000 mm. × або ÷ на 10, 100, 1000…",
    },
    (20, "mierzenie"): {
        "def_pl": "Mierzenie to przykładanie linijki lub taśmy od zera do końca przedmiotu.",
        "def_ua": "Вимірювання — прикладання лінійки або стрічки від нуля до кінця предмета.",
        "rule": "Zaczynaj od 0 na linijce. Patrz, na której kresce kończy się przedmiot.",
        "rule_ua": "Починай від 0 на лінійці. Дивись, на якій рисочці закінчується предмет.",
    },
    (20, "porównywanie"): {
        "def_pl": "Aby wiedzieć, co dłuższe, najpierw ustaw te same jednostki.",
        "def_ua": "Щоб знати, що довше, спочатку постав однакові одиниці.",
        "rule": "1,2 m i 95 cm → zamień: 120 cm > 95 cm.",
        "rule_ua": "1,2 m і 95 cm → перетвори: 120 cm > 95 cm.",
    },
    (20, "obwód a długość"): {
        "def_pl": "Obwód to długość „dookoła” figury — jak spacer wokół boiska.",
        "def_ua": "Периметр — довжина «навколо» фігури — як прогулянка навколо поля.",
        "rule": "Obwód = suma długości wszystkich boków.",
        "rule_ua": "Периметр = сума довжин усіх сторін.",
    },
    (20, "przykład"): {
        "def_pl": "Przykład pomaga zobaczyć, jak „przesuwają się” zera i przecinek przy zamianie.",
        "def_ua": "Приклад допомагає побачити, як «зсуваються» нулі й кома при перетворенні.",
        "rule": "2,5 m = 250 cm = 2500 mm. Sprawdź na linijce w głowie: metr ma 100 cm.",
        "rule_ua": "2,5 m = 250 cm = 2500 mm. Перевір у голові: метр має 100 cm.",
    },
    # ——— strona 21: Masa ———
    (21, "jednostki masy"): {
        "def_pl": "Masa mówi, jak ciężkie jest coś. W szkole najczęściej: kilogram i gram.",
        "def_ua": "Маса каже, яке щось важке. У школі найчастіше: кілограм і грам.",
        "rule": "Podstawowa jednostka: kilogram (kg). Lekkie rzeczy — w gramach (g).",
        "rule_ua": "Основна одиниця: кілограм (kg). Легкі речі — в грамах (g).",
    },
    (21, "zamiana"): {
        "def_pl": "Przy masie często × lub ÷ przez 1000 (jak duże woreczki i małe).",
        "def_ua": "При масі часто × або ÷ на 1000 (як великі й маленькі пакетики).",
        "rule": "1 kg = 1000 g; 1 t = 1000 kg.",
        "rule_ua": "1 kg = 1000 g; 1 t = 1000 kg.",
    },
    (21, "porównywanie"): {
        "def_pl": "Żeby porównać ciężar, obie liczby muszą być w tej samej jednostce.",
        "def_ua": "Щоб порівняти вагу, обидва числа мають бути в тій самій одиниці.",
        "rule": "1 kg > 800 g, bo 1 kg = 1000 g.",
        "rule_ua": "1 kg > 800 g, бо 1 kg = 1000 g.",
    },
    (21, "ważenie"): {
        "def_pl": "Ważenie to sprawdzanie masy na wadze — w sklepie, w kuchni, w szkole.",
        "def_ua": "Зважування — перевірка маси на вагах — у магазині, на кухні, у школі.",
        "rule": "Masa to „ile materii”. Na wadze czytamy wynik w g lub kg.",
        "rule_ua": "Маса — «скільки речовини». На вагах читаємо результат у g або kg.",
    },
    (21, "przykłady"): {
        "def_pl": "Ćwicz zamianę: przecinek „skacze” o 3 miejsca przy kg ↔ g.",
        "def_ua": "Тренуй перетворення: кома «стрибає» на 3 місця при kg ↔ g.",
        "rule": "250 g = 0,25 kg; 2,5 kg = 2500 g.",
        "rule_ua": "250 g = 0,25 kg; 2,5 kg = 2500 g.",
    },
    (21, "w życiu"): {
        "def_pl": "Masę widzisz na etykietach: zakupy, przepisy, paczki.",
        "def_ua": "Масу бачиш на етикетках: покупки, рецепти, посилки.",
        "rule": "Czytaj „masa netto” na opakowaniu — to ile produktu jest w środku.",
        "rule_ua": "Читай «маса нетто» на упаковці — це скільки продукту всередині.",
    },
    # ——— strona 23: Czas ———
    (23, "jednostki czasu"): {
        "def_pl": "Czas mierzymy sekundami, minutami i godzinami — jak „pudełka” w pudełkach.",
        "def_ua": "Час міряємо секундами, хвилинами і годинами — як «коробки» в коробках.",
        "rule": "1 minuta = 60 sekund; 1 godzina = 60 minut. To system 60!",
        "rule_ua": "1 хвилина = 60 секунд; 1 година = 60 хвилин. Це система 60!",
    },
    (23, "zegar"): {
        "def_pl": "Zegar pokazuje, która jest godzina teraz. Bywa 12-godzinny albo 24-godzinny.",
        "def_ua": "Годинник показує, котра зараз година. Буває 12-годинний або 24-годинний.",
        "rule": "Nauczyciel często używa zapisu 14:20 (to 2:20 po południu).",
        "rule_ua": "Учитель часто використовує запис 14:20 (це 2:20 дня).",
    },
    (23, "upływ czasu"): {
        "def_pl": "Upływ czasu to „jak długo trwało” — od startu do końca.",
        "def_ua": "Проміжок часу — «як довго тривало» — від старту до кінця.",
        "rule": "Od 14:20 do 15:05 minęło 45 minut. Koniec minus początek.",
        "rule_ua": "Від 14:20 до 15:05 минуло 45 хвилин. Кінець мінус початок.",
    },
    (23, "doba"): {
        "def_pl": "Doba to cały dzień i cała noc — pełne 24 godziny.",
        "def_ua": "Доба — цілий день і ціла ніч — повні 24 години.",
        "rule": "1 doba = 24 h. Potem znowu zaczyna się kolejny dzień.",
        "rule_ua": "1 доба = 24 год. Потім знову починається наступний день.",
    },
    (23, "zamiana"): {
        "def_pl": "Przy czasie uważaj: tu nie ma „100 minut w godzinie” — jest 60.",
        "def_ua": "При часі увага: тут немає «100 хвилин у годині» — є 60.",
        "rule": "2,5 h = 2 h 30 min = 150 min. Najpierw godziny, potem minuty.",
        "rule_ua": "2,5 год = 2 год 30 хв = 150 хв. Спочатку години, потім хвилини.",
    },
    # ——— strona 24: Kalendarz ———
    (24, "jednostki kalendarzowe"): {
        "def_pl": "Kalendarz układa dni w tygodnie, miesiące i lata — pomaga planować.",
        "def_ua": "Календар впорядковує дні в тижні, місяці й роки — допомагає планувати.",
        "rule": "1 tydzień = 7 dni. Zapamiętaj dni: pn, wt, śr, cz, pt, so, nd.",
        "rule_ua": "1 тиждень = 7 днів. Запам'ятай дні: пн, вт, ср, чт, пт, сб, нд.",
    },
    (24, "data"): {
        "def_pl": "Data mówi: który dzień, który miesiąc, który rok.",
        "def_ua": "Дата каже: який день, який місяць, який рік.",
        "rule": "Zapis w Polsce: dzień.miesiąc.rok — np. 18.07.2026.",
        "rule_ua": "Запис у Польщі: день.місяць.рік — напр. 18.07.2026.",
    },
    (24, "rok przestępny"): {
        "def_pl": "W roku przestępnym jest jeden dzień więcej — luty ma 29 dni.",
        "def_ua": "У високосному році є один день більше — лютий має 29 днів.",
        "rule": "Zwykle co 4 lata (z wyjątkami). Wtedy rok ma 366 dni.",
        "rule_ua": "Звичайно кожні 4 роки (з винятками). Тоді рік має 366 днів.",
    },
    (24, "miesiące"): {
        "def_pl": "Miesiące mają 28/29, 30 albo 31 dni — warto znać długości.",
        "def_ua": "Місяці мають 28/29, 30 або 31 день — варто знати довжину.",
        "rule": "Pamiętaj rymowankę lub „kostki na knykciach” — pomaga przy 30/31.",
        "rule_ua": "Пам'ятай віршик або «кісточки на суглобах» — допомагає при 30/31.",
    },
    (24, "kolejność dni"): {
        "def_pl": "Dni tygodnia idą zawsze w tej samej kolejności.",
        "def_ua": "Дні тижня завжди йдуть у тому самому порядку.",
        "rule": "pn → wt → śr → cz → pt → so → nd → i znowu pn.",
        "rule_ua": "пн → вт → ср → чт → пт → сб → нд → і знову пн.",
    },
    (24, "przykład"): {
        "def_pl": "Przy liczeniu dni uważaj na koniec lutego — tam bywa „haczyk”.",
        "def_ua": "При лічбі днів увага на кінець лютого — там буває «гачок».",
        "rule": "Od 28.02 do 3.03: sprawdź, czy rok jest przestępny.",
        "rule_ua": "Від 28.02 до 3.03: перевір, чи рік високосний.",
    },
    # ——— strona 26: Pieniądze ———
    (26, "złoty i grosz"): {
        "def_pl": "W Polsce płacimy złotymi i groszami. Grosz to mała część złotego.",
        "def_ua": "У Польщі платимо злотими і грошами. Грош — маленька частина злотого.",
        "rule": "1 zł = 100 gr. Jak 1 złoty = 100 małych monet-groszy.",
        "rule_ua": "1 zł = 100 gr. Як 1 злотий = 100 маленьких монет-грошів.",
    },
    (26, "zapis"): {
        "def_pl": "Zapis pieniędzy wygląda jak liczba z przecinkiem: złote przed, grosze po.",
        "def_ua": "Запис грошей виглядає як число з комою: злоті перед, гроші після.",
        "rule": "12,50 zł = 12 złotych i 50 groszy.",
        "rule_ua": "12,50 zł = 12 злотих і 50 грошів.",
    },
    (26, "dodawanie / odejmowanie"): {
        "def_pl": "Pieniądze dodajemy i odejmujemy jak zwykłe liczby z przecinkiem.",
        "def_ua": "Гроші додаємо й віднімаємо як звичайні числа з комою.",
        "rule": "3,40 + 1,75 = 5,15. Pilnuj przecinka w jednej kolumnie.",
        "rule_ua": "3,40 + 1,75 = 5,15. Стеж, щоб коми були в одному стовпчику.",
    },
    (26, "reszta"): {
        "def_pl": "Reszta to pieniądze, które wracają, gdy płacisz więcej niż cena.",
        "def_ua": "Решта — гроші, які повертають, коли платиш більше за ціну.",
        "rule": "Reszta = ile dałeś − cena. 10 − 7,30 = 2,70.",
        "rule_ua": "Решта = скільки дав − ціна. 10 − 7,30 = 2,70.",
    },
    (26, "porównywanie cen"): {
        "def_pl": "Żeby wiedzieć, co tańsze, porównuj „za to samo” (np. za 100 g).",
        "def_ua": "Щоб знати, що дешевше, порівнюй «за те саме» (напр. за 100 г).",
        "rule": "Sprowadź ceny do tej samej ilości, potem porównaj.",
        "rule_ua": "Зведи ціни до тієї самої кількості, потім порівняй.",
    },
    (26, "budżet"): {
        "def_pl": "Budżet to plan: ile mam i ile mogę wydać.",
        "def_ua": "Бюджет — план: скільки маю і скільки можу витратити.",
        "rule": "Prosto: przychód − wydatek. Nie wydawaj więcej, niż masz.",
        "rule_ua": "Просто: дохід − витрата. Не витрачай більше, ніж маєш.",
    },
    # ——— strona 28: Figury płaskie (1) ———
    (28, "punkt"): {
        "def_pl": "Punkt to miejsce — jak kropka na mapie. Nie ma długości ani szerokości.",
        "def_ua": "Точка — місце — як крапка на карті. Не має довжини й ширини.",
        "rule": "Oznaczamy wielką literą: A, B, C.",
        "rule_ua": "Позначаємо великою літерою: A, B, C.",
    },
    (28, "prosta"): {
        "def_pl": "Prosta to linia, która idzie bez końca w obie strony — jak nieskończona szyna.",
        "def_ua": "Пряма — лінія, що йде без кінця в обидва боки — як нескінченна рейка.",
        "rule": "Nie ma początku ani końca. Rysujemy ze strzałkami na końcach.",
        "rule_ua": "Не має початку й кінця. Малюємо зі стрілками на кінцях.",
    },
    (28, "odcinek"): {
        "def_pl": "Odcinek to kawałek prostej z dwoma końcami — możesz go zmierzyć linijką.",
        "def_ua": "Відрізок — шматок прямої з двома кінцями — можеш виміряти лінійкою.",
        "rule": "Odcinek AB ma końce A i B. Ma konkretną długość.",
        "rule_ua": "Відрізок AB має кінці A і B. Має конкретну довжину.",
    },
    (28, "półprosta"): {
        "def_pl": "Półprosta ma początek (punkt) i biegnie w jedną stronę bez końca — jak promień latarki.",
        "def_ua": "Півпряма має початок (точку) і йде в один бік без кінця — як промінь ліхтарика.",
        "rule": "Zapis: półprosta OA (zaczyna się w O, przechodzi przez A). Nie myl z promieniem okręgu!",
        "rule_ua": "Запис: півпряма OA (починається в O, проходить через A). Не плутай із радіусом кола!",
    },
    (28, "łamana"): {
        "def_pl": "Łamana to linia z odcinków połączonych końcami — jak ścieżka z zakrętami.",
        "def_ua": "Ламана — лінія з відрізків, з'єднаних кінцями — як стежка з поворотами.",
        "rule": "Odcinki stykają się końcami. Może być otwarta lub zamknięta.",
        "rule_ua": "Відрізки стикаються кінцями. Може бути відкритою або замкненою.",
    },
    (28, "wielokąt"): {
        "def_pl": "Wielokąt to zamknięta figura z odcinków: trójkąt, czworokąt i inne.",
        "def_ua": "Многокутник — замкнена фігура з відрізків: трикутник, чотирикутник та інші.",
        "rule": "Policz boki: 3 → trójkąt, 4 → czworokąt. Figura musi być zamknięta.",
        "rule_ua": "Полічи сторони: 3 → трикутник, 4 → чотирикутник. Фігура має бути замкненою.",
    },
    # ——— starsze tematy (zostawiamy wcześniejsze dopracowania) ———
    (7, "nawiasy"): {
        "def_pl": "Nawiasy mówią: „to policz najpierw”. Bez nawiasów wynik może być inny.",
        "def_ua": "Дужки кажуть: «це порахуй спочатку». Без дужок результат може бути іншим.",
        "rule": "Kolejność: nawiasy → potęgi → ×: → +−. Zapamiętaj jak wierszyk.",
        "rule_ua": "Порядок: дужки → степені → ×: → +−. Запам'ятай як віршик.",
    },
    (9, "ułamek zwykły"): {
        "def_pl": "Ułamek zwykły pokazuje część całości: licznik nad kreską, mianownik pod kreską.",
        "def_ua": "Звичайний дріб показує частину цілого: чисельник над рискою, знаменник під рискою.",
        "rule": "Zapis a/b. Mianownik mówi, na ile równych części podzielono całość (≠ 0).",
        "rule_ua": "Запис a/b. Знаменник — на скільки рівних частин поділено ціле (≠ 0).",
    },
    (12, "dzielenie"): {
        "def_pl": "Dzielenie ułamków zamieniamy na mnożenie przez ułamek odwrotny.",
        "def_ua": "Ділення дробів замінюємо на множення на обернений дріб.",
        "rule": "a/b : c/d = a/b × d/c. Najpierw odwrotność, potem mnożenie (i skracanie).",
        "rule_ua": "a/b : c/d = a/b × d/c. Спочатку обернений, потім множення.",
    },
    (15, "procent z liczby"): {
        "def_pl": "Procent z liczby to część tej liczby — np. 20% z 50 to dwadzieścia setnych z 50.",
        "def_ua": "Відсоток від числа — частина цього числа — напр. 20% від 50.",
        "rule": "p% z a = a · p / 100. Możesz też liczyć: 1% = a/100, potem × p.",
        "rule_ua": "p% від a = a · p / 100. Або: 1% = a/100, потім × p.",
    },
    (19, "metoda bilansowania"): {
        "def_pl": "Równanie to waga: co zrobisz po lewej, zrób to samo po prawej — równowaga zostaje.",
        "def_ua": "Рівняння — терези: що робиш ліворуч, те саме роби праворуч — рівновага лишається.",
        "rule": "x+5=12 → odejmij 5 po obu stronach → x=7. Zawsze sprawdź podstawieniem.",
        "rule_ua": "x+5=12 → відніми 5 з обох боків → x=7. Завжди перевір підставлянням.",
    },
    (31, "długość okręgu"): {
        "def_pl": "Długość okręgu to „obwód” koła — jak długość linii dookoła.",
        "def_ua": "Довжина кола — «периметр» круга — довжина лінії навколо.",
        "rule": "C = 2πr albo C = πd. Przyjmuj π ≈ 3,14 (chyba że nauczyciel poda inaczej).",
        "rule_ua": "C = 2πr або C = πd. Бери π ≈ 3,14 (якщо вчитель не сказав інакше).",
    },
    (35, "trójkąt"): {
        "def_pl": "Pole trójkąta to miara powierzchni w środku trójkąta.",
        "def_ua": "Площа трикутника — міра поверхні всередині трикутника.",
        "rule": "P = (podstawa · wysokość) / 2. Wysokość pada prostopadle na podstawę.",
        "rule_ua": "P = (основа · висота) / 2. Висота падає перпендикулярно на основу.",
    },
    (40, "średnia arytmetyczna"): {
        "def_pl": "Średnia arytmetyczna to „typowa” wartość: suma wszystkich danych podzielona przez ich liczbę.",
        "def_ua": "Середнє арифметичне — «типове» значення: сума всіх даних, поділена на їх кількість.",
        "rule": "średnia = (x₁+x₂+…+xₙ) / n. Najpierw dodaj, potem podziel.",
        "rule_ua": "середнє = (x₁+x₂+…+xₙ) / n. Спочатку додай, потім поділи.",
    },
    (41, "prawdopodobieństwo"): {
        "def_pl": "Prawdopodobieństwo mówi, jaka jest szansa zdarzenia — od niemożliwego (0) do pewnego (1).",
        "def_ua": "Ймовірність каже, який шанс події — від неможливого (0) до певного (1).",
        "rule": "P = liczba wyników korzystnych / liczba wszystkich jednakowo możliwych.",
        "rule_ua": "P = число сприятливих / число всіх однаково можливих.",
    },
    (23, "przykład"): {
        "def_pl": "W szkole: przerwa 15 minut, lekcja zwykle 45. Policz od dzwonka do dzwonka.",
        "def_ua": "У школі: перерва 15 хвилин, урок зазвичай 45. Порахуй від дзвінка до дзвінка.",
        "rule": "Od 10:00 do 10:15 = 15 min przerwy. Od 8:00 do 8:45 = 45 min lekcji.",
        "rule_ua": "Від 10:00 до 10:15 = 15 хв перерви. Від 8:00 до 8:45 = 45 хв уроку.",
    },
    (24, "urodziny i święta"): {
        "def_pl": "Kalendarz w kl. 1–3: kiedy urodziny, kiedy ferie, który dziś dzień tygodnia.",
        "def_ua": "Календар у кл. 1–3: коли день народження, коли канікули, який сьогодні день тижня.",
        "rule": "Zaznacz urodziny w kalendarzu. Policz, ile dni do ferii.",
        "rule_ua": "Познач день народження в календарі. Порахуй, скільки днів до канікул.",
    },
    (26, "5 zł na bułkę"): {
        "def_pl": "Jak w kl. 1–3: masz 10 zł, bułka kosztuje 5 zł — ile zostanie?",
        "def_ua": "Як у кл. 1–3: маєш 10 zł, булочка коштує 5 zł — скільки лишиться?",
        "rule": "10 − 5 = 5 zł reszty. Za 15 zł kupisz 3 bułki po 5 zł.",
        "rule_ua": "10 − 5 = 5 zł решти. За 15 zł купиш 3 булочки по 5 zł.",
    },
    (28, "figury wokół nas"): {
        "def_pl": "Szukaj figur w klasie i na podwórku: okno, drzwi, znak drogowy, piłka.",
        "def_ua": "Шукай фігури в класі й на подвір'ї: вікно, двері, дорожній знак, м'яч.",
        "rule": "Okno ≈ prostokąt, znak ostrzegawczy ≈ trójkąt, piłka ≈ koło.",
        "rule_ua": "Вікно ≈ прямокутник, попереджувальний знак ≈ трикутник, м'яч ≈ коло.",
    },
    (29, "figury wokół nas"): {
        "def_pl": "Dach jak trójkąt, drzwi i zeszyt jak prostokąt, kafelek jak kwadrat.",
        "def_ua": "Дах як трикутник, двері й зошит як прямокутник, плитка як квадрат.",
        "rule": "Nazwij 3 figury w klasie na głos — to już geometria!",
        "rule_ua": "Назви 3 фігури в класі вголос — це вже геометрія!",
    },
}

from handbook_overrides_all import MORE_OVERRIDES

CARD_OVERRIDES.update(MORE_OVERRIDES)

from handbook_clear import CLEAR_FIXES

CARD_OVERRIDES.update(CLEAR_FIXES)

from editorial_v1_overrides import EDITORIAL_V1

CARD_OVERRIDES.update(EDITORIAL_V1)

EARLY_PAGES = {1, 2, 4, 5, 6, 20, 21, 23, 24, 26, 28, 29, 61}
ALL_DEEP_PAGES = set(range(1, 62))


def enrich_card(card: dict, page_n: int) -> None:
    from handbook_examples import attach_examples

    term = card.get("pl") or ""
    ov = CARD_OVERRIDES.get((page_n, term))
    had_override = bool(ov)
    if ov:
        for k, v in ov.items():
            card[k] = v

    def_pl = card.get("def_pl") or card.get("explain") or ""
    def_ua = card.get("def_ua") or card.get("explain_ua") or ""
    # Dla klas 1–3 z ręcznym tekstem nie doklejaj ogólnego „dopiska”
    if not had_override:
        def_pl, def_ua = _expand_pair(def_pl, def_ua, term)
    card["def_pl"] = def_pl
    card["def_ua"] = def_ua

    rule = card.get("rule") or ""
    rule_ua = card.get("rule_ua") or ""
    if (not rule) or _is_template_rule(rule) or _is_template_rule(rule_ua):
        rule, rule_ua = _school_rule(card)
        card["rule"] = rule
        card["rule_ua"] = rule_ua
    elif not rule_ua and card.get("def_ua"):
        card["rule_ua"] = card["def_ua"]

    attach_examples(card, page_n)


def apply(pages: list) -> list:
    from pilot_pages import apply_pilot
    from klasa_map import resolve_klasa
    from handbook_life_complete import apply_page_meta

    for p in pages:
        n = int(p["n"])
        for c in p.get("cards") or []:
            enrich_card(c, n)
            c["klasa"] = resolve_klasa(n, c.get("pl") or "", c)

        if n in PAGE_RULES:
            p["remember"] = _enrich_remember([dict(r) for r in PAGE_RULES[n]])
        else:
            p["remember"] = _enrich_remember(p.get("remember") or [])

        # Jak na stronach-wzorcach: bez meta-howto
        p["howto_pl"] = ""
        p["howto_ua"] = ""

        apply_page_meta(p)
        apply_pilot(p)
        # Po pilocie jeszcze raz dopnij klasę + meta życia (pilot 4/12 ma własne life)
        if n not in (4, 12):
            apply_page_meta(p)
        for c in p.get("cards") or []:
            # Standard v1.0: redakcja pilota ma pierwszeństwo także po apply_pilot
            ov = EDITORIAL_V1.get((n, c.get("pl") or ""))
            if ov:
                c.update(ov)
            c["klasa"] = resolve_klasa(n, c.get("pl") or "", c)
    return pages
