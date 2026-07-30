# -*- coding: utf-8 -*-
"""
Strony-wzorcowe (pilot): jasno, bez wody, jak w polskiej SP + oznaczenie klasy.
Strony: 4 (dodawanie/odejmowanie), 12 (działania na ułamkach).
"""

PILOT_PAGES = {4, 12}

# Pełna treść kart: nadpisuje def/rule/example/klasa po zwykłym enrich
PILOT = {
    4: {
        "intro_pl": "Uczymy się łączyć i zabierać — podstawowe działania w klasach 1–3.",
        "intro_ua": "Вчимося об'єднувати і забирати — основні дії в класах 1–3.",
        "life_pl": "Punkty w grze, cukierki, zakupy: ile razem? ile zostanie?",
        "life_ua": "Очки в грі, цукерки, покупки: скільки разом? скільки лишиться?",
        "howto_pl": "",
        "howto_ua": "",
        "mistake_pl": "Przy odejmowaniu dzieci często odwracają kolejność (piszą 4−9 zamiast 9−4). Zawsze: większa (odjemna) pierwsza, potem odejmujemy.",
        "mistake_ua": "При відніманні діти часто міняють порядок (пишуть 4−9 замість 9−4). Завжди: більше (зменшуване) перше, потім віднімаємо.",
        "remember": [
            {"pl": "Dodawanie = ile razem?", "ua": "Додавання = скільки разом?", "formula": "a + b = suma"},
            {"pl": "Odejmowanie = ile zostanie?", "ua": "Віднімання = скільки лишиться?", "formula": "a − b = różnica"},
            {"pl": "Sprawdź odejmowanie dodawaniem.", "ua": "Перевір віднімання додаванням.", "formula": "różnica + odjemnik = odjemna"},
        ],
        "cards": [
            {
                "pl": "dodawanie",
                "klasa": "klasy 1–3",
                "def_pl": "Łączymy dwie (lub więcej) liczby. Pytanie: ile będzie razem?",
                "def_ua": "Об'єднуємо два (чи більше) числа. Питання: скільки буде разом?",
                "rule": "Zapis w zeszycie: składnik + składnik = suma.",
                "rule_ua": "Запис у зошиті: доданок + доданок = сума.",
                "example_pl": "W pudełku 3 kredki, dokładasz 5. Razem 8.",
                "example_ua": "У коробці 3 олівці, докладаєш 5. Разом 8.",
                "visual": "3 + 5 = 8",
            },
            {
                "pl": "suma",
                "klasa": "klasy 1–3",
                "def_pl": "Suma to wynik dodawania — liczba, którą dostajesz po znaku =. Odpowiada: ile razem?",
                "def_ua": "Сума — результат додавання — число після знака =. Відповідає: скільки разом?",
                "rule": "składnik + składnik = suma",
                "rule_ua": "У 2+6=8 число 8 — саме сума.",
                "example_pl": "W jednym pudełku 2 ołówki, w drugim 6. Suma = 8 ołówków.",
                "example_ua": "В одній коробці 2 олівці, в другій 6. Сума = 8 олівців.",
                "visual": "składnik + składnik = suma",
            },
            {
                "pl": "odejmowanie",
                "klasa": "klasy 1–3",
                "def_pl": "Zabieramy część. Pytanie: ile zostanie? albo: o ile więcej?",
                "def_ua": "Забираємо частину. Питання: скільки лишиться? або: на скільки більше?",
                "rule": "Zapis: odjemna − odjemnik = różnica.",
                "rule_ua": "Запис: зменшуване − від'ємник = різниця.",
                "example_pl": "Miałaś 9 naklejek, oddałaś 4. Zostaje 5.",
                "example_ua": "Мала 9 наліпок, віддала 4. Лишається 5.",
                "visual": "9 − 4 = 5",
            },
            {
                "pl": "różnica",
                "klasa": "klasy 1–3",
                "def_pl": "Różnica to wynik odejmowania — to, co zostało, albo o ile jedna liczba jest większa.",
                "def_ua": "Різниця — результат віднімання — те, що лишилось, або на скільки одне число більше.",
                "rule": "Zapis: odjemna − odjemnik = różnica. Sprawdź: różnica + odjemnik = odjemna.",
                "rule_ua": "Запис: зменшуване − від'ємник = різниця. Перевір: різниця + від'ємник = зменшуване.",
                "example_pl": "Ty 10 punktów, kolega 7. Różnica = 3 — o tyle wygrywasz.",
                "example_ua": "Ти 10 очок, друг 7. Різниця = 3 — на стільки виграєш.",
                "visual": "10 − 7 = 3",
            },
            {
                "pl": "składnik",
                "klasa": "klasy 1–3",
                "def_pl": "Składnik to liczba, którą dodajemy (jedna z „części” sumy).",
                "def_ua": "Доданок — число, яке додаємо (одна з «частин» суми).",
                "rule": "W 4+5=9 liczby 4 i 5 to składniki.",
                "rule_ua": "У 4+5=9 числа 4 і 5 — доданки.",
                "example_pl": "Nauczyciel pyta: „Podaj składniki sumy 7.” Np. 3 i 4.",
                "example_ua": "Учитель питає: «Назви доданки суми 7.» Напр. 3 і 4.",
                "visual": "3 + 4 = 7",
            },
            {
                "pl": "odjemna i odjemnik",
                "klasa": "klasy 2–3",
                "def_pl": "Odjemna — od czego odejmujesz. Odjemnik — ile odejmujesz.",
                "def_ua": "Зменшуване — від чого віднімаєш. Від'ємник — скільки віднімаєш.",
                "rule": "W 8−3=5: 8 odjemna, 3 odjemnik, 5 różnica.",
                "rule_ua": "У 8−3=5: 8 зменшуване, 3 від'ємник, 5 різниця.",
                "example_pl": "Z 8 jabłek zabierasz 3. Nie odwrotnie!",
                "example_ua": "З 8 яблук забираєш 3. Не навпаки!",
                "visual": "8 − 3 = 5",
            },
            {
                "pl": "właściwości +",
                "klasa": "klasy 2–4",
                "def_pl": "Przy dodawaniu możesz zmienić kolejność — wynik ten sam (przemienność).",
                "def_ua": "При додаванні можна змінити порядок — результат той самий (переставна).",
                "rule": "a+b=b+a oraz (a+b)+c=a+(b+c).",
                "rule_ua": "a+b=b+a та (a+b)+c=a+(b+c).",
                "example_pl": "Łatwiej: 8+5 → 5+8, albo 17+3 → najpierw 17+3=20.",
                "example_ua": "Легше: 8+5 → 5+8, або 17+3 → спочатку 17+3=20.",
                "visual": "3+5=5+3",
            },
            {
                "pl": "właściwości −",
                "klasa": "klasy 2–4",
                "def_pl": "Przy odejmowaniu: minus zero nic nie zmienia; liczba minus ona sama daje 0. Kolejności nie wolno odwracać!",
                "def_ua": "При відніманні: мінус нуль нічого не змінює; число мінус воно саме дає 0. Порядок не можна міняти!",
                "rule": "Zapamiętaj: a−0=a oraz a−a=0. Uwaga: 9−4 ≠ 4−9 — wynik się zmienia.",
                "rule_ua": "Запам'ятай: a−0=a та a−a=0. Увага: 9−4 ≠ 4−9 — результат змінюється.",
                "example_pl": "7−0=7. Sprawdzenie odejmowania: 5+4=9, więc 9−4=5.",
                "example_ua": "7−0=7. Перевірка віднімання: 5+4=9, отже 9−4=5.",
                "visual": "a−0=a · a−a=0",
            },
            {
                "pl": "przykłady",
                "klasa": "klasy 1–3",
                "def_pl": "Ćwiczemy oba działania i od razu sprawdzamy wynik.",
                "def_ua": "Тренуємо обидві дії й одразу перевіряємо результат.",
                "rule": "Po odejmowaniu dodaj: różnica + odjemnik = odjemna.",
                "rule_ua": "Після віднімання додай: різниця + від'ємник = зменшуване.",
                "example_pl": "15−6=9, bo 9+6=15. 7+8=15 — policz na palcach lub w pamięci.",
                "example_ua": "15−6=9, бо 9+6=15. 7+8=15 — порахуй на пальцях або в пам'яті.",
                "visual": "15−6=9 · sprawdź: 9+6=15",
            },
        ],
    },
    12: {
        "intro_pl": "Jak dodawać, odejmować, mnożyć i dzielić ułamki — reguły jak w klasach 4–6.",
        "intro_ua": "Як додавати, віднімати, множити і ділити дроби — правила як у класах 4–6.",
        "life_pl": "Pizza, tort, przepis: łączysz kawałki albo bierzesz część z części.",
        "life_ua": "Піца, торт, рецепт: з'єднуєш шматки або береш частину від частини.",
        "howto_pl": "",
        "howto_ua": "",
        "mistake_pl": "Przy +/− ułamków dzieci często dodają też mianowniki (2/7+3/7 ≠ 5/14). Mianownik przy wspólnym zostaje ten sam — zmieniasz tylko liczniki.",
        "mistake_ua": "При +/− дробів діти часто додають і знаменники (2/7+3/7 ≠ 5/14). Знаменник при спільному лишається той самий — змінюєш лише чисельники.",
        "remember": [
            {"pl": "+/− : najpierw wspólny mianownik, potem liczniki.", "ua": "+/− : спочатку спільний знаменник, потім чисельники.", "formula": "2/7+3/7=5/7"},
            {"pl": "× : licznik×licznik, mianownik×mianownik.", "ua": "× : чисельник×чисельник, знаменник×знаменник.", "formula": "a/b · c/d = ac/bd"},
            {"pl": "Dzielenie = mnożenie przez odwrotność.", "ua": "Ділення = множення на обернений.", "formula": "a/b : c/d = a/b · d/c"},
        ],
        "cards": [
            {
                "pl": "+/− ten sam mianownik",
                "klasa": "klasy 4–5",
                "def_pl": "Gdy mianownik ten sam, dodajesz lub odejmujesz tylko liczniki — „kawałki tego samego podziału”.",
                "def_ua": "Коли знаменник той самий, додаєш або віднімаєш лише чисельники — «шматки того самого поділу».",
                "rule": "Liczniki +/− , mianownik bez zmian.",
                "rule_ua": "Чисельники +/− , знаменник без змін.",
                "example_pl": "Zjadłaś 2/7 tortu, potem jeszcze 3/7. Razem 5/7 tortu.",
                "example_ua": "З'їла 2/7 торта, потім ще 3/7. Разом 5/7 торта.",
                "visual": "2/7 + 3/7 = 5/7",
            },
            {
                "pl": "różne mianowniki",
                "klasa": "klasy 5–6",
                "def_pl": "Gdy mianowniki różne, najpierw sprowadź do wspólnego (jak wspólna „kratka”), potem +/− liczniki.",
                "def_ua": "Коли знаменники різні, спочатку зведи до спільного (як спільна «клітинка»), потім +/− чисельники.",
                "rule": "1. Wspólny mianownik  2. Rozszerz  3. +/− liczniki  4. Skróć.",
                "rule_ua": "1. Спільний знаменник  2. Розшир  3. +/− чисельники  4. Скороти.",
                "example_pl": "Pół pizzy + jedna trzecia: 1/2+1/3 = 3/6+2/6 = 5/6.",
                "example_ua": "Пів піци + одна третя: 1/2+1/3 = 3/6+2/6 = 5/6.",
                "visual": "1/2 + 1/3 = 5/6",
            },
            {
                "pl": "mnożenie",
                "klasa": "klasy 5–6",
                "def_pl": "Mnożenie ułamków: bierzesz „część z części” — mnożysz liczniki i mianowniki.",
                "def_ua": "Множення дробів: береш «частину від частини» — множиш чисельники і знаменники.",
                "rule": "a/b × c/d = (a×c)/(b×d). Potem skróć, jeśli można.",
                "rule_ua": "a/b × c/d = (a×c)/(b×d). Потім скороти, якщо можна.",
                "example_pl": "2/3 tabliczki czekolady × 4/5 porcji → 8/15.",
                "example_ua": "2/3 плитки шоколаду × 4/5 порції → 8/15.",
                "visual": "2/3 × 4/5 = 8/15",
            },
            {
                "pl": "dzielenie",
                "klasa": "klasy 5–6",
                "def_pl": "Dzielenie ułamków w szkole zamieniamy na mnożenie przez ułamek odwrotny (odwracamy drugi ułamek).",
                "def_ua": "Ділення дробів у школі замінюємо на множення на обернений дріб (перевертаємо другий дріб).",
                "rule": "Wzór: a/b : c/d = a/b × d/c. Najpierw odwróć dzielnik, potem mnoż.",
                "rule_ua": "Формула: a/b : c/d = a/b × d/c. Спочатку переверни дільник, потім множ.",
                "example_pl": "Masz 2/3 litra soku i rozlewasz po 1/4 litra → ile porcji? 2/3:1/4 = 2/3×4/1 = 8/3.",
                "example_ua": "Маєш 2/3 літра соку і розливаєш по 1/4 літра → скільки порцій? 2/3:1/4 = 2/3×4/1 = 8/3.",
                "visual": "2/3 : 1/4 = 2/3 × 4/1",
            },
            {
                "pl": "odwrotność",
                "klasa": "klasy 5–6",
                "def_pl": "Odwrotność: zamieniasz licznik z mianownikiem (odwracasz ułamek).",
                "def_ua": "Обернений: міняєш чисельник і знаменник (перевертаєш дріб).",
                "rule": "3/4 → 4/3. Iloczyn liczby i odwrotności = 1 (gdy ≠ 0).",
                "rule_ua": "3/4 → 4/3. Добуток числа і оберненого = 1 (коли ≠ 0).",
                "example_pl": "Odwracasz 3/4 przy dzieleniu — dostajesz 4/3.",
                "example_ua": "Перевертаєш 3/4 при діленні — отримуєш 4/3.",
                "visual": "3/4 → 4/3",
            },
            {
                "pl": "skracanie przed ×",
                "klasa": "klasy 5–6",
                "def_pl": "Przed mnożeniem skracaj „na krzyż” — mniej rachunku i mniejszy wynik do uproszczenia.",
                "def_ua": "Перед множенням скорочуй «навхрест» — менше рахунку і менший результат.",
                "rule": "Skracaj wspólne czynniki licznika z mianownikiem (także na skos).",
                "rule_ua": "Скорочуй спільні множники чисельника зі знаменником (також навскіс).",
                "example_pl": "2/9 × 3/4: skróć 3 i 9 → 2/3 × 1/4 = 2/12 = 1/6.",
                "example_ua": "2/9 × 3/4: скороти 3 і 9 → 2/3 × 1/4 = 2/12 = 1/6.",
                "visual": "2/9 × 3/4 = 1/6",
            },
        ],
    },
}


def apply_pilot(page: dict) -> None:
    n = int(page.get("n") or 0)
    if n not in PILOT:
        return
    data = PILOT[n]
    for key in (
        "intro_pl",
        "intro_ua",
        "life_pl",
        "life_ua",
        "howto_pl",
        "howto_ua",
        "mistake_pl",
        "mistake_ua",
        "remember",
    ):
        if key in data:
            page[key] = data[key]

    by_pl = {
        (c.get("pl") or "").strip(): c
        for c in (data.get("cards") or [])
        if (c.get("pl") or "").strip()
    }
    for card in page.get("cards") or []:
        key = (card.get("pl") or "").strip()
        upd = by_pl.get(key)
        if not upd:
            continue
        card.update(upd)
        # Pilot: nie doklejaj generycznych „zobacz poniżej”
        card.pop("_generic_example", None)
