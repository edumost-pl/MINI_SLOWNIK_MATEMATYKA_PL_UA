# -*- coding: utf-8 -*-
"""
Przykłady „z życia” — krótka scena + zapis matematyczny.
Cel: dziecko od razu widzi sens, nie samą suchą formułę.
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


def E(story_pl: str, story_ua: str) -> dict:
    return {"example_pl": story_pl, "example_ua": story_ua}


# Ręcznie dopracowane sceny (klucz: nr strony, hasło)
LIFE = {
    # 1
    (1, "liczba naturalna"): E(
        "W koszyku leży 5 jabłek. Liczysz: 1, 2, 3, 4, 5 — to liczby naturalne.",
        "У кошику 5 яблук. Лічиш: 1, 2, 3, 4, 5 — це натуральні числа.",
    ),
    (1, "cyfra"): E(
        "Na kostce do gry widzisz tylko cyfry 1–6. Z cyfr składasz potem większe liczby.",
        "На гральному кубику бачиш лише цифри 1–6. З цифр потім складаєш більші числа.",
    ),
    (1, "liczba"): E(
        "Numer domu 347 to liczba z trzech cyfr — mówi, który to dom.",
        "Номер будинку 347 — число з трьох цифр — каже, який це будинок.",
    ),
    (1, "wartość pozycyjna"): E(
        "W numerze 347 cyfra 3 to setki (300), a nie „po prostu trzy”.",
        "У номері 347 цифра 3 — сотні (300), а не «просто три».",
    ),
    (1, "parzysta / nieparzysta"): E(
        "Dzieci ustawiają się parami. Liczba parzysta → wszyscy mają parę; nieparzysta → ktoś zostaje.",
        "Діти стають парами. Парне число → всі мають пару; непарне → хтось лишається.",
    ),
    (1, "porównanie"): E(
        "Ty masz 3 naklejki, kolega 7. Piszesz 3 < 7 — u niego więcej.",
        "У тебе 3 наліпки, у друга 7. Пишеш 3 < 7 — у нього більше.",
    ),
    (1, "zaokrąglanie"): E(
        "W sklepie jest 47 cukierków. Mówisz w przybliżeniu: „ze 50” — łatwiej planować.",
        "У магазині 47 цукерок. Кажеш приблизно: «з 50» — легше планувати.",
    ),
    (1, "następnik / poprzednik"): E(
        "Stoisz na stopniu 9. Stopień niżej to 8 (poprzednik), wyżej — 10 (następnik).",
        "Стоїш на сходинці 9. Нижче — 8 (попередник), вище — 10 (наступник).",
    ),
    (1, "kolejność liczb"): E(
        "Układacie wyniki biegu od najmniejszego czasu do największego — to kolejność.",
        "Розкладаєте результати бігу від найменшого часу до найбільшого — це порядок.",
    ),
    # 4
    (4, "dodawanie"): E(
        "Masz 3 cukierki, dostajesz jeszcze 5. Razem? 3+5=8.",
        "Маєш 3 цукерки, отримуєш ще 5. Разом? 3+5=8.",
    ),
    (4, "suma"): E(
        "W jednym pudełku 2 ołówki, w drugim 3. Suma = 5 ołówków.",
        "В одній коробці 2 олівці, в другій 3. Сума = 5 олівців.",
    ),
    (4, "odejmowanie"): E(
        "Było 9 naklejek, oddałeś 4. Zostaje 9−4=5.",
        "Було 9 наліпок, віддав 4. Лишається 9−4=5.",
    ),
    (4, "różnica"): E(
        "Ty masz 8 punktów, kolega 3. Różnica to 5 — o tyle wygrywasz.",
        "У тебе 8 очок, у друга 3. Різниця — 5 — на стільки виграєш.",
    ),
    (4, "składnik"): E(
        "W zadaniu 1+3=4 liczby 1 i 3 to składniki — „co dodajemy”.",
        "У завданні 1+3=4 числа 1 і 3 — доданки — «що додаємо».",
    ),
    (4, "odjemna i odjemnik"): E(
        "Z 8 jabłek zabierasz 3. 8 to odjemna, 3 to odjemnik.",
        "З 8 яблук забираєш 3. 8 — зменшуване, 3 — від'ємник.",
    ),
    (4, "właściwości +"): E(
        "3+5 cukierków to to samo co 5+3 — kolejność nie psuje wyniku.",
        "3+5 цукерок — те саме, що 5+3 — порядок не псує результату.",
    ),
    (4, "właściwości −"): E(
        "Masz 7 punktów. Minus 0 nic nie zmienia. Minus 7 → zostaje 0.",
        "Маєш 7 очок. Мінус 0 нічого не змінює. Мінус 7 → лишається 0.",
    ),
    (4, "przykłady"): E(
        "Policz zakupy w głowie: 2+3 i 8−3 — jak na lekcji, tylko z życia.",
        "Порахуй покупки в голові: 2+3 і 8−3 — як на уроці, тільки з життя.",
    ),
    # 5
    (5, "mnożenie"): E(
        "3 półki, na każdej 4 książki. Szybko: 4×3=12 zamiast 4+4+4.",
        "3 полиці, на кожній 4 книжки. Швидко: 4×3=12 замість 4+4+4.",
    ),
    (5, "iloczyn"): E(
        "2 rzędy po 5 krzeseł → iloczyn 10 — tyle krzeseł w sali.",
        "2 ряди по 5 стільців → добуток 10 — стільки стільців у класі.",
    ),
    (5, "czynnik"): E(
        "W 2×5 obie liczby to czynniki — „co przez co mnożymy”.",
        "У 2×5 обидва числа — множники — «що на що множимо».",
    ),
    (5, "przemienność"): E(
        "3 rzędy po 4 krzesła = 4 rzędy po 3 — ta sama liczba miejsc.",
        "3 ряди по 4 стільці = 4 ряди по 3 — та сама кількість місць.",
    ),
    (5, "×0 i ×1"): E(
        "0 torebek cukierków → 0 cukierków. 1 torebka z 6 → nadal 6.",
        "0 пакетів цукерок → 0 цукерок. 1 пакет із 6 → далі 6.",
    ),
    (5, "kluczowe wyniki"): E(
        "W grze trzeba szybko: 7×8. Gdy znasz tabliczkę — odpowiadasz od razu.",
        "У грі треба швидко: 7×8. Коли знаєш таблицю — відповідаєш одразу.",
    ),
    # 6
    (6, "dzielenie"): E(
        "12 cukierków dla 3 dzieci po równo → 12:3=4. Każdy dostaje 4.",
        "12 цукерок для 3 дітей порівну → 12:3=4. Кожен отримує 4.",
    ),
    (6, "iloraz"): E(
        "15 naklejek : 5 albumów = 3 — to iloraz (wynik dzielenia).",
        "15 наліпок : 5 альбомів = 3 — це частка (результат ділення).",
    ),
    (6, "dzielna i dzielnik"): E(
        "Dzielisz 15 jabłek na 5 koszyków: 15 — dzielna, 5 — dzielnik.",
        "Ділиш 15 яблук на 5 кошиків: 15 — ділене, 5 — дільник.",
    ),
    (6, "z resztą"): E(
        "17 cukierków, 5 dzieci. Po 3 każdemu i zostaje 2 — reszta.",
        "17 цукерок, 5 дітей. По 3 кожному і лишається 2 — остача.",
    ),
    (6, "związek z ×"): E(
        "Sprawdzasz: jeśli 12:3=4, to 4×3 musi dać 12.",
        "Перевіряєш: якщо 12:3=4, то 4×3 має дати 12.",
    ),
    (6, ":1 i : siebie"): E(
        "6 ciastek : 1 osoba = 6. 6 ciastek : 6 osób = po 1.",
        "6 печив : 1 особа = 6. 6 печив : 6 осіб = по 1.",
    ),
    # 9–12 ułamki
    (9, "ułamek zwykły"): E(
        "Pizza na 4 części, bierzesz 3 — to 3/4 pizzy.",
        "Піца на 4 частини, береш 3 — це 3/4 піци.",
    ),
    (9, "licznik"): E(
        "W 3/4 cyfra 3 (licznik) = ile kawałków bierzesz.",
        "У 3/4 цифра 3 (чисельник) = скільки шматків береш.",
    ),
    (9, "mianownik"): E(
        "W 3/4 cyfra 4 (mianownik) = na ile równych części pokrojono.",
        "У 3/4 цифра 4 (знаменник) = на скільки рівних частин порізали.",
    ),
    (12, "dzielenie"): E(
        "Masz 2/3 tabliczki i dzielisz przez 4/5 porcji — zamieniasz na × odwrotność.",
        "Маєш 2/3 плитки і ділиш на 4/5 порції — міняєш на × обернений.",
    ),
    (15, "procent z liczby"): E(
        "Sklep: −20% z 50 zł. Liczysz 20% z 50 = 10, płacisz 40 zł.",
        "Магазин: −20% від 50 zł. Рахуєш 20% від 50 = 10, платиш 40 zł.",
    ),
    (15, "procent"): E(
        "100 uczniów w szkole. 1% to 1 uczeń. 25% to ćwierć klasy.",
        "100 учнів у школі. 1% — 1 учень. 25% — чверть класу.",
    ),
    # 19
    (19, "równanie"): E(
        "Myślisz: „mam x naklejek, dostałem 5, mam 12”. Równanie: x+5=12.",
        "Думаєш: «маю x наліпок, отримав 5, маю 12». Рівняння: x+5=12.",
    ),
    (19, "metoda bilansowania"): E(
        "Waga: po lewej x+5, po prawej 12. Odejmujesz 5 z obu stron → x=7.",
        "Терези: ліворуч x+5, праворуч 12. Віднімаєш 5 з обох боків → x=7.",
    ),
    # 26
    (26, "złoty i grosz"): E(
        "Kupujesz bułkę za 2 zł 50 gr — to 2,50 zł (100 gr = 1 zł).",
        "Купуєш булочку за 2 zł 50 gr — це 2,50 zł (100 gr = 1 zł).",
    ),
    (26, "reszta"): E(
        "Dajesz 10 zł za rzecz za 7,30 zł. Reszta: 10−7,30=2,70 zł.",
        "Даєш 10 zł за річ за 7,30 zł. Решта: 10−7,30=2,70 zł.",
    ),
    # 31
    (31, "długość okręgu"): E(
        "Opaska na okrągły stolik: mierzysz „dookoła” wzorem C=2πr.",
        "Стрічка навколо круглого столика: міряєш «навколо» формулою C=2πr.",
    ),
    (31, "pole koła"): E(
        "Jak duża jest okrągła mata? Pole „w środku”: P=πr².",
        "Який великий круглий килимок? Площа «всередині»: P=πr².",
    ),
    # 35
    (35, "obwód"): E(
        "Płotek dookoła ogródka: dodajesz długości wszystkich boków — to obwód.",
        "Паркан навколо городу: додаєш довжини всіх сторін — це периметр.",
    ),
    (35, "trójkąt"): E(
        "Żagiel w kształcie trójkąta: pole = (podstawa×wysokość)/2.",
        "Вітрило у формі трикутника: площа = (основа×висота)/2.",
    ),
    # 40–41
    (40, "średnia arytmetyczna"): E(
        "Oceny: 2,5,5,8. Średnia (2+5+5+8)/4=5 — „typowa” ocena.",
        "Оцінки: 2,5,5,8. Середнє (2+5+5+8)/4=5 — «типова» оцінка.",
    ),
    (41, "prawdopodobieństwo"): E(
        "Kostka: szansa na 6 to 1 na 6 możliwych wyników → P=1/6.",
        "Кубик: шанс на 6 — 1 з 6 можливих результатів → P=1/6.",
    ),
    (2, "Podstawowe znaki"): E(
        "Na starym zegarze zamiast 4 widzisz IV — to znak rzymski.",
        "На старому годиннику замість 4 бачиш IV — це римський знак.",
    ),
    (2, 'Dodawanie znaków'): E(
        "VI na zegarze to 5+1=6. Mniejszy znak po prawej — dodajesz.",
        "VI на годиннику — 5+1=6. Менший знак праворуч — додаєш.",
    ),
    (2, 'Odejmowanie znaków'): E(
        "IV to „o jeden mniej niż 5” → 4. Mniejszy znak przed większym — odejmujesz.",
        "IV — «на один менше ніж 5» → 4. Менший знак перед більшим — віднімаєш.",
    ),
    (2, 'Gdzie spotykamy?'): E(
        "Rozdział IX w książce, data na pomniku, film „Rocky II” — wszędzie liczby rzymskie.",
        "Розділ IX у книзі, дата на пам'ятнику, фільм «Rocky II» — скрізь римські числа.",
    ),
    (3, 'oś liczbowa'): E(
        "Jak linijka przez zero: w lewo mróz (−), w prawo plus (+).",
        "Як лінійка через нуль: ліворуч мороз (−), праворуч плюс (+).",
    ),
    (3, 'wartość bezwzględna'): E(
        "Od domu do sklepu 5 minut w lewo albo w prawo — odległość | | ta sama.",
        "Від дому до магазину 5 хвилин ліворуч або праворуч — відстань | | та сама.",
    ),
    (3, 'zastosowania'): E(
        "Piętro −1 na parkingu, −3°C za oknem, dług 20 zł — liczby ujemne w życiu.",
        "Поверх −1 на паркінгу, −3°C за вікном, борг 20 zł — від'ємні числа в житті.",
    ),
    (7, 'nawiasy'): E(
        "Najpierw to, co w nawiasie — jak „najpierw ubierz buty, potem wyjdź”.",
        "Спочатку те, що в дужках — як «спочатку взуй черевики, потім виходь».",
    ),
    (7, '× i :'): E(
        "2+3×4 cukierków w pudełkach: najpierw 3×4, potem +2 → 14, nie 20.",
        "2+3×4 цукерок у коробках: спочатку 3×4, потім +2 → 14, не 20.",
    ),
    (8, 'przez 2'): E(
        "Numer domu kończy się na 6 — parzysty, dzieli się przez 2. Szybki test!",
        "Номер будинку кінчається на 6 — парний, ділиться на 2. Швидкий тест!",
    ),
    (8, 'przez 5'): E(
        "Cena 45 zł kończy się na 5 — dzieli się przez 5.",
        "Ціна 45 zł кінчається на 5 — ділиться на 5.",
    ),
    (8, 'liczba pierwsza'): E(
        "Liczba 7 ma tylko dzielniki 1 i 7 — jak „samotna” liczba pierwsza.",
        "Число 7 має лише дільники 1 і 7 — як «самотнє» просте число.",
    ),
    (10, 'skracanie'): E(
        "4/6 tortu to to samo co 2/3 — skracasz, żeby było prościej.",
        "4/6 торта — те саме, що 2/3 — скорочуєш, щоб було простіше.",
    ),
    (10, 'rozszerzanie'): E(
        "1/2 pizzy = 2/4 — rozszerzasz, by dodać do innego ułamka.",
        "1/2 піци = 2/4 — розширюєш, щоб додати до іншого дробу.",
    ),
    (11, 'ułamek dziesiętny'): E(
        "Bułka kosztuje 2,50 zł — to ułamek dziesiętny w codziennych zakupach.",
        "Булочка коштує 2,50 zł — це десятковий дріб у щоденних покупках.",
    ),
    (13, 'potęga'): E(
        "Kwadratowa płytka 5×5: zamiast pisać 5·5 piszesz 5²=25.",
        "Квадратна плитка 5×5: замість писати 5·5 пишеш 5²=25.",
    ),
    (14, 'pierwiastek kwadratowy'): E(
        "Pole kwadratu 9 m² — jaki bok? √9=3 m.",
        "Площа квадрата 9 м² — який бік? √9=3 м.",
    ),
    (16, 'przykład'): E(
        "3 kg jabłek za 12 zł → 5 kg za 20 zł. Cena rośnie proporcjonalnie.",
        "3 кг яблук за 12 zł → 5 кг за 20 zł. Ціна зростає пропорційно.",
    ),
    (17, 'zmienna'): E(
        "„n uczniów w klasie” — n to zmienna. Dziś 24, jutro może 25.",
        "«n учнів у класі» — n змінна. Сьогодні 24, завтра може 25.",
    ),
    (18, 'redukcja'): E(
        "3x + 5x naklejek to 8x — łączysz podobne, jak 3+5 jabłek.",
        "3x + 5x наліпок — це 8x — об'єднуєш подібні, як 3+5 яблук.",
    ),
    (20, 'mierzenie'): E(
        "Linijka od 0 do końca ołówka — tak mierzysz długość.",
        "Лінійка від 0 до кінця олівця — так міряєш довжину.",
    ),
    (20, 'zamiana'): E(
        "Twój wzrost 1,40 m = 140 cm — zamiana pomaga porównać.",
        "Твій зріст 1,40 m = 140 cm — перетворення допомагає порівняти.",
    ),
    (21, 'zamiana'): E(
        "Mąka 0,5 kg = 500 g — przepis w gramach, waga w kilogramach.",
        "Борошно 0,5 kg = 500 g — рецепт у грамах, вага в кілограмах.",
    ),
    (22, 'litr'): E(
        "Butelka 1 l soku = 1000 ml — wygodnie przy nalewaniu.",
        "Пляшка 1 л соку = 1000 ml — зручно при наливанні.",
    ),
    (23, 'upływ czasu'): E(
        "Film od 14:20 do 15:05 — trwa 45 minut. Koniec minus początek.",
        "Фільм від 14:20 до 15:05 — триває 45 хвилин. Кінець мінус початок.",
    ),
    (24, 'data'): E(
        "Twoje urodziny 18.07.2026 — dzień, miesiąc, rok w kalendarzu.",
        "Твій день народження 18.07.2026 — день, місяць, рік у календарі.",
    ),
    (25, 'różnica temperatur'): E(
        "Rano −4°C, w południe +6°C. Ociepliło się o 10°.",
        "Вранці −4°C, вдень +6°C. Потеплішало на 10°.",
    ),
    (27, 'prędkość'): E(
        "120 km w 2 godziny → 60 km/h. Droga dzielona przez czas.",
        "120 км за 2 години → 60 км/год. Шлях, поділений на час.",
    ),
    (27, 'skala mapy'): E(
        "Na mapie 3 cm, skala 1:100 000 → w terenie 3 km. Planujesz wycieczkę.",
        "На карті 3 см, масштаб 1:100 000 → на місцевості 3 км. Плануєш екскурсію.",
    ),
    (28, 'odcinek'): E(
        "Kreska od A do B na linijce — odcinek o konkretnej długości.",
        "Риска від A до B на лінійці — відрізок конкретної довжини.",
    ),
    (29, 'kwadrat'): E(
        "Serwetka: 4 równe boki i kąty jak róg kartki — to kwadrat.",
        "Серветка: 4 рівні сторони і кути як ріг аркуша — це квадрат.",
    ),
    (29, 'trójkąt'): E(
        "Znak „ustąp pierwszeństwa” ma kształt trójkąta. Suma kątów = 180°.",
        "Знак «дай дорогу» має форму трикутника. Сума кутів = 180°.",
    ),
    (30, 'okrąg'): E(
        "Obręcz od roweru to okrąg — sama linia, bez „środka wypełnionego”.",
        "Обідок велосипеда — коло — лише лінія, без «заповненої середини».",
    ),
    (30, 'koło'): E(
        "Talerz to koło — okrągły brzeg i całe wnętrze.",
        "Тарілка — круг — круглий край і вся середина.",
    ),
    (32, 'kąt prosty'): E(
        "Róg zeszytu ma 90° — kąt prosty. Przyłóż kątomierz i sprawdź.",
        "Кут зошита має 90° — прямий кут. Приклади кутомір і перевір.",
    ),
    (33, 'kąt ostry'): E(
        "Otwarte nożyczki pod małym kątem — to kąt ostry (< 90°).",
        "Відкриті ножиці під малим кутом — це гострий кут (< 90°).",
    ),
    (34, 'proste równoległe'): E(
        "Szyny torów idą obok siebie i się nie spotykają — równoległe.",
        "Рейки колій ідуть поряд і не зустрічаються — паралельні.",
    ),
    (36, 'sześcian'): E(
        "Kostka do gry to sześcian — 6 kwadratowych ścian, V=a³.",
        "Гральний кубик — куб — 6 квадратних граней, V=a³.",
    ),
    (37, 'oś symetrii'): E(
        "Motyl: lewe skrzydło lustrzanie prawe — oś symetrii w środku.",
        "Метелик: ліве крило дзеркально праве — вісь симетрії посередині.",
    ),
    (38, 'punkt (x, y)'): E(
        "Skarb na mapie w kratkę: 3 w prawo, 2 w górę → punkt (3, 2).",
        "Скарб на карті в клітинку: 3 вправо, 2 вгору → точка (3, 2).",
    ),
    (39, 'wykres słupkowy'): E(
        "Ankieta „ulubiony kolor”: wyższy słupek = więcej głosów.",
        "Опитування «улюблений колір»: вищий стовпчик = більше голосів.",
    ),
    (40, 'moda'): E(
        "W klasie najczęściej wybierają pizzę — to moda (najczęstsza wartość).",
        "У класі найчастіше обирають піцу — це мода (найчастіше значення).",
    ),
    (41, 'zasada mnożenia'): E(
        "3 drogi do parku × 4 autobusy = 12 sposobów dojazdu.",
        "3 дороги до парку × 4 автобуси = 12 способів дістатися.",
    ),
    (42, '+ plus / dodawanie'): E(
        "W zeszycie zamiast „dodać” stawiasz + — krócej i czytelniej.",
        "У зошиті замість «додати» ставиш + — коротше й зрозуміліше.",
    ),
}


# Sceny-tło per strona (gdy brak ręcznego przykładu)
PAGE_HOOK = {
    1: ("Liczenie rzeczy wokół Ciebie", "Лічба речей навколо тебе"),
    2: ("Zegar albo numer rozdziału w książce", "Годинник або номер розділу в книзі"),
    3: ("Termometr albo piętro pod ziemią", "Термометр або поверх під землею"),
    4: ("Cukierki, punkty w grze, naklejki", "Цукерки, очки в грі, наліпки"),
    5: ("Rzędy ławek albo pudełka z kredkami", "Ряди парт або коробки з олівцями"),
    6: ("Rozdawanie po równo w klasie", "Розподіл порівну в класі"),
    7: ("Liczenie krok po kroku w zeszycie", "Рахунок крок за кроком у зошиті"),
    8: ("Szybki test: czy liczba dzieli się…?", "Швидкий тест: чи число ділиться…?"),
    9: ("Pizza, tort, czekolada w kawałkach", "Піца, торт, шоколад шматочками"),
    10: ("Upraszczanie zapisu ułamka", "Спрощення запису дробу"),
    11: ("Cena w sklepie albo wynik na kalkulatorze", "Ціна в магазині або результат на калькуляторі"),
    12: ("Kawałki pizzy i przepisy kulinarne", "Шматки піци й кулінарні рецепти"),
    13: ("Szybki zapis wielokrotnego mnożenia", "Швидкий запис багаторазового множення"),
    14: ("Szukanie boku kwadratu o danym polu", "Пошук сторони квадрата із заданою площею"),
    15: ("Promocja w sklepie albo wynik testu", "Акція в магазині або результат тесту"),
    16: ("Cena za kilogram na bazarze", "Ціна за кілограм на базарі"),
    17: ("Przepis z literą zamiast liczby", "Рецепт із літерою замість числа"),
    18: ("Upraszczanie długiego zapisu z x", "Спрощення довгого запису з x"),
    19: ("Zagadka: ile było na początku?", "Загадка: скільки було на початку?"),
    20: ("Linijka, wzrost, długość boiska", "Лінійка, зріст, довжина поля"),
    21: ("Waga w sklepie albo przepis na ciasto", "Ваги в магазині або рецепт тістечка"),
    22: ("Butelka soku albo pudełko", "Пляшка соку або коробка"),
    23: ("Ile trwa lekcja albo film?", "Скільки триває урок або фільм?"),
    24: ("Urodziny, ferie, plan tygodnia", "День народження, канікули, план тижня"),
    25: ("Prognoza pogody rano", "Прогноз погоди вранці"),
    26: ("Zakupy i wydawanie reszty", "Покупки і видача решти"),
    27: ("Samochód w podróży albo mapa wycieczki", "Авто в подорожі або карта екскурсії"),
    28: ("Rysunek w zeszycie od punktu", "Малюнок у зошиті від точки"),
    29: ("Znaki drogowe i kształty okien", "Дорожні знаки й форми вікон"),
    30: ("Talerz, koło od roweru, pierścień", "Тарілка, колесо велосипеда, кільце"),
    31: ("Obwód okrągłego dywanu", "Обвід круглого килима"),
    32: ("Otwarte nożyczki albo róg książki", "Відкриті ножиці або кут книжки"),
    33: ("Porównanie kątów na rysunku", "Порівняння кутів на малюнку"),
    34: ("Tory kolejowe i przecznica", "Залізничні колії й поперечна"),
    35: ("Ramka na zdjęcie albo trawnik", "Рамка для фото або газон"),
    36: ("Pudełko, kostka, piłka", "Коробка, кубик, м'яч"),
    37: ("Motyl albo odbicie w lustrze", "Метелик або відбиття в дзеркалі"),
    38: ("Szukanie skarbu na mapie kratkowanej", "Пошук скарбу на картатій мапі"),
    39: ("Ankieta w klasie: ulubiony kolor", "Опитування в класі: улюблений колір"),
    40: ("Średnia ocen albo najczęściej wybierany smak", "Середнє оцінок або найчастіший смак"),
    41: ("Losowanie dyżurnego albo rzut kostką", "Жеребкування чергового або кидок кубика"),
    42: ("Szybki zapis w zeszycie", "Швидкий запис у зошиті"),
    43: ("Liczenie w słupku w zeszycie", "Рахунок стовпчиком у зошиті"),
    44: ("Łatwiejsze mnożenie w pamięci", "Легше множення в пам'яті"),
    45: ("Skracanie ułamka i wspólny mianownik", "Скорочення дробу і спільний знаменник"),
    46: ("Część kieszonkowego / całość z części", "Частина кишенькових / ціле з частини"),
    47: ("Wzrost, czas, masa w dwóch jednostkach", "Зріст, час, маса в двох одиницях"),
    48: ("Róg kartki i najkrótsza droga do linii", "Кут аркуша і найкоротший шлях до лінії"),
    49: ("Trzeci kąt trójkąta na klasówce", "Третій кут трикутника на контрольній"),
    50: ("Działka w arach; romb i trapez", "Ділянка в арах; ромб і трапеція"),
    51: ("Pudełko i siatka do sklejenia", "Коробка і сітка для склеювання"),
    52: ("Rabat i wynik testu w procentach", "Знижка і результат тесту у відсотках"),
    53: ("Duże liczby z potęgą 10", "Великі числа зі степенем 10"),
    54: ("Upraszczanie pierwiastków w zadaniu", "Спрощення коренів у задачі"),
    55: ("Otwieranie nawiasów w algebrze", "Розкриття дужок в алгебрі"),
    56: ("Podział nagrody w stosunku", "Поділ нагороди у відношенні"),
    57: ("Drabina przy ścianie — Pitagoras", "Драбина біля стіни — Піфагор"),
    58: ("Dwa jednakowe trójkąty na rysunku", "Два однакові трикутники на малюнку"),
    59: ("Odległość na mapie w kratkę", "Відстань на мапі в клітинку"),
    60: ("Podział odcinka i kąta na pół", "Поділ відрізка і кута навпіл"),
}


def make_life_example(card: dict, page_n: int) -> tuple[str, str, str]:
    """
    Zwraca (story_pl, story_ua, math_html).
    math_html = visual (może mieć <br>).
    """
    visual = card.get("visual") or ""
    math = visual if visual else ""
    key = (page_n, card.get("pl") or "")
    if key in LIFE:
        e = LIFE[key]
        return e["example_pl"], e["example_ua"], math

    hook_pl, hook_ua = PAGE_HOOK.get(
        page_n, ("Sytuacja z lekcji lub z życia", "Ситуація з уроку або з життя")
    )
    term_pl = card.get("pl") or "to pojęcie"
    term_ua = card.get("ua") or "це поняття"
    v = _plain(visual)

    if v:
        story_pl = f"{hook_pl}. Przykład: {v}."
        story_ua = f"{hook_ua}. Приклад: {v}."
    else:
        story_pl = f"{hook_pl}. To właśnie „{term_pl}” — wymyśl własny przykład z lekcji."
        story_ua = f"{hook_ua}. Це саме «{term_ua}» — вигадай власний приклад з уроку."
    return story_pl, story_ua, math


# Pełne przykłady (poziom strony 1) — uzupełniają LIFE
from handbook_life_complete import merge_life_into

merge_life_into(LIFE)


def attach_examples(card: dict, page_n: int) -> None:
    """Dopina example_pl / example_ua (nie nadpisuje ręcznych)."""
    if card.get("example_pl") and card.get("example_ua"):
        return
    pl, ua, _ = make_life_example(card, page_n)
    card.setdefault("example_pl", pl)
    card.setdefault("example_ua", ua)
