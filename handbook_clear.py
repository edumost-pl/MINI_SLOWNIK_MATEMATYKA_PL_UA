# -*- coding: utf-8 -*-
"""
Dopracowanie jasności tekstów: każde hasło ma mieć
zrozumiałe „co to jest” + „jak w szkole” (nie sam wzór).
"""

def T(def_pl, def_ua, rule, rule_ua):
    return {"def_pl": def_pl, "def_ua": def_ua, "rule": rule, "rule_ua": rule_ua}


CLEAR_FIXES = {
    # ——— 4 (pilot też nadpisze — trzymaj spójnie) ———
    (4, "suma"): T(
        "Suma to wynik dodawania — liczba, którą dostajesz po znaku =. Odpowiada na pytanie: ile razem?",
        "Сума — результат додавання — число після знака =. Відповідає: скільки разом?",
        "Zapis: składnik + składnik = suma. W 2+6=8 liczba 8 to właśnie suma.",
        "Запис: доданок + доданок = сума. У 2+6=8 число 8 — саме сума.",
    ),
    (4, "różnica"): T(
        "Różnica to wynik odejmowania — to, co zostało, albo o ile jedna liczba jest większa.",
        "Різниця — результат віднімання — те, що лишилось, або на скільки одне число більше.",
        "Zapis: odjemna − odjemnik = różnica. Sprawdź: różnica + odjemnik = odjemna.",
        "Запис: зменшуване − від'ємник = різниця. Перевір: різниця + від'ємник = зменшуване.",
    ),
    (4, "właściwości −"): T(
        "Przy odejmowaniu: minus zero nic nie zmienia; liczba minus ona sama daje 0. Kolejności nie wolno odwracać!",
        "При відніманні: мінус нуль нічого не змінює; число мінус воно саме дає 0. Порядок не можна міняти!",
        "Zapamiętaj: a−0=a oraz a−a=0. Uwaga: 9−4 ≠ 4−9 — wynik się zmienia.",
        "Запам'ятай: a−0=a та a−a=0. Увага: 9−4 ≠ 4−9 — результат змінюється.",
    ),

    # ——— 5 ———
    (5, "iloczyn"): T(
        "Iloczyn to wynik mnożenia — liczba po znaku =. To „ile wyszło”, gdy mnożysz.",
        "Добуток — результат множення — число після знака =. Це «скільки вийшло».",
        "W zapisie 2×5=10 liczba 10 to iloczyn. Czynniki to 2 i 5.",
        "У записі 2×5=10 число 10 — добуток. Множники — 2 і 5.",
    ),

    # ——— 7 ———
    (7, "ten sam poziom"): T(
        "Gdy dwa działania mają tę samą „moc” (np. mnożenie i dzielenie), liczymy je od lewej do prawej.",
        "Коли дві дії мають ту саму «силу» (напр. множення і ділення), рахуємо зліва направо.",
        "Przykład: 24:6×2. Najpierw 24:6=4, potem 4×2=8. Nie łącz w 24:12!",
        "Приклад: 24:6×2. Спочатку 24:6=4, потім 4×2=8. Не об'єднуй у 24:12!",
    ),

    # ——— 8 ———
    (8, "przez 4"): T(
        "Żeby sprawdzić podzielność przez 4, patrzysz tylko na dwie ostatnie cyfry liczby.",
        "Щоб перевірити подільність на 4, дивиш лише на дві останні цифри числа.",
        "Jeśli liczba z dwóch ostatnich cyfr dzieli się przez 4 — cała też (np. …16, …24, …2024).",
        "Якщо число з двох останніх цифр ділиться на 4 — ціле теж (напр. …16, …24, …2024).",
    ),
    (8, "przez 10"): T(
        "Liczba dzieli się przez 10 dokładnie wtedy, gdy kończy się cyfrą 0.",
        "Число ділиться на 10 саме тоді, коли закінчується цифрою 0.",
        "Końcówka 0 → tak (20, 70, 150). Inna cyfra na końcu → nie dzieli się przez 10.",
        "Закінчення 0 → так (20, 70, 150). Інша цифра в кінці → не ділиться на 10.",
    ),

    # ——— 9 ———
    (9, "licznik"): T(
        "Licznik to liczba nad kreską ułamka — mówi, ile równych części bierzesz.",
        "Чисельник — число над рискою дробу — каже, скільки рівних частин береш.",
        "W ułamku 3/4 licznik to 3: bierzemy trzy części z czterech.",
        "У дробі 3/4 чисельник — 3: беремо три частини з чотирьох.",
    ),

    # ——— 10–11 ———
    (10, "porównywanie"): T(
        "Porównujemy ułamki: przy tym samym mianowniku większy licznik = większy ułamek. Przy różnych — najpierw wspólny mianownik.",
        "Порівнюємо дроби: при тому самому знаменнику більший чисельник = більший дріб. При різних — спочатку спільний знаменник.",
        "Przykłady: 2/5 < 3/5. Albo 1/2 i 1/3 → 3/6 i 2/6, więc 1/2 > 1/3.",
        "Приклади: 2/5 < 3/5. Або 1/2 і 1/3 → 3/6 і 2/6, тож 1/2 > 1/3.",
    ),
    (11, "porównywanie"): T(
        "Porównujemy liczby dziesiętne miejsce po miejscu: najpierw części całkowite, potem cyfry po przecinku.",
        "Порівнюємо десяткові місце за місцем: спочатку цілі частини, потім цифри після коми.",
        "Dopisz zera, żeby było równo miejsc: 1,25 i 1,3 → 1,25 < 1,30.",
        "Допиши нулі, щоб було порівну місць: 1,25 і 1,3 → 1,25 < 1,30.",
    ),

    # ——— 12 ———
    (12, "dzielenie"): T(
        "Dzielenie ułamków w szkole zamieniamy na mnożenie przez ułamek odwrotny (odwracamy drugi ułamek).",
        "Ділення дробів у школі замінюємо на множення на обернений дріб (перевертаємо другий дріб).",
        "Wzór: a/b : c/d = a/b × d/c. Najpierw odwróć dzielnik, potem mnoż.",
        "Формула: a/b : c/d = a/b × d/c. Спочатку переверни дільник, потім множ.",
    ),

    # ——— 13 ———
    (13, "potęga"): T(
        "Potęga to skrót zapisu: ta sama liczba mnożona przez siebie kilka razy.",
        "Степінь — скорочений запис: те саме число множиться само на себе кілька разів.",
        "W 2³ podstawa to 2, wykładnik 3: 2×2×2=8. Nie myl z 2×3=6!",
        "У 2³ основа — 2, показник 3: 2×2×2=8. Не плутай із 2×3=6!",
    ),
    (13, "0, 1, 10"): T(
        "Wykładnik 1 nic nie zmienia; wykładnik 0 daje 1 (gdy podstawa ≠ 0). Potęgi dziesiątki to „1 i zera”.",
        "Показник 1 нічого не змінює; показник 0 дає 1 (коли основа ≠ 0). Степені десятки — «1 і нулі».",
        "Zapamiętaj: a¹=a; a⁰=1 (a≠0); 10³=1000 (jedynka i trzy zera).",
        "Запам'ятай: a¹=a; a⁰=1 (a≠0); 10³=1000 (одиниця і три нулі).",
    ),
    (13, "mnożenie potęg"): T(
        "Gdy podstawa jest ta sama, mnożenie potęg = dodawanie wykładników.",
        "Коли основа та сама, множення степенів = додавання показників.",
        "Wzór: aᵐ · aⁿ = aᵐ⁺ⁿ. Przykład: 2³·2² = 2⁵ (wykładniki 3+2).",
        "Формула: aᵐ · aⁿ = aᵐ⁺ⁿ. Приклад: 2³·2² = 2⁵ (показники 3+2).",
    ),
    (13, "dzielenie potęg"): T(
        "Gdy podstawa jest ta sama, dzielenie potęg = odejmowanie wykładników (podstawa ≠ 0).",
        "Коли основа та сама, ділення степенів = віднімання показників (основа ≠ 0).",
        "Wzór: aᵐ : aⁿ = aᵐ⁻ⁿ. Przykład: 2⁵:2² = 2³.",
        "Формула: aᵐ : aⁿ = aᵐ⁻ⁿ. Приклад: 2⁵:2² = 2³.",
    ),

    # ——— 14 ———
    (14, "zapis"): T(
        "Znak pierwiastka √ stoi przed liczbą lub wyrażeniem — szukasz liczby, która „w kwadracie” daje to, co pod spodem.",
        "Знак кореня √ стоїть перед числом або виразом — шукаєш число, яке «в квадраті» дає те, що під ним.",
        "Najpierw policz to, co pod √ (gdy trzeba), potem znajdź pierwiastek. Np. √(9+7)=√16=4.",
        "Спочатку порахуй те, що під √ (коли треба), потім знайди корінь. Напр. √(9+7)=√16=4.",
    ),
    (14, "przykłady"): T(
        "Najczęstsze pierwiastki warto znać na pamięć — jak tabliczkę mnożenia.",
        "Найчастіші корені варто знати напам'ять — як таблицю множення.",
        "√4=2, √9=3, √16=4, √25=5, √100=10 — bo 2²=4, 3²=9 itd.",
        "√4=2, √9=3, √16=4, √25=5, √100=10 — бо 2²=4, 3²=9 тощо.",
    ),
    (14, "związek z potęgą"): T(
        "Pierwiastek kwadratowy i potęga druga to działania odwrotne — jedno „odwraca” drugie.",
        "Квадратний корінь і другий степінь — обернені дії: одне «відміняє» друге.",
        "Sprawdzenie: (√a)² = a. W szkole podstawowej zwykle bierzemy a ≥ 0.",
        "Перевірка: (√a)² = a. У початковій школі зазвичай беремо a ≥ 0.",
    ),
    (14, "szacowanie"): T(
        "Gdy pierwiastek nie wychodzi „ładnie”, szacujemy: szukamy między sąsiednimi kwadratami doskonałymi.",
        "Коли корінь не виходить «гарно», оцінюємо: шукаємо між сусідніми повними квадратами.",
        "√50 jest blisko 7, bo 7²=49. Piszesz ≈7,1 — to szacunek, nie dokładna wartość.",
        "√50 близько 7, бо 7²=49. Пишеш ≈7,1 — це оцінка, не точне значення.",
    ),

    # ——— 15 ———
    (15, "procent"): T(
        "Procent to setna część całości — wygodny sposób mówienia o częściach (jak „ze stu”).",
        "Відсоток — сота частина цілого — зручний спосіб говорити про частини («зі ста»).",
        "Zapamiętaj: 1% = 1/100 = 0,01. 100% to zawsze całość.",
        "Запам'ятай: 1% = 1/100 = 0,01. 100% — завжди ціле.",
    ),
    (15, "zmniejszenie o p%"): T(
        "Zmniejszenie o p% to odjęcie p procent od liczby — np. przecena w sklepie.",
        "Зменшення на p% — віднімання p відсотків від числа — напр. знижка в магазині.",
        "Nowa wartość = a·(1 − p/100). Uwaga: −20%, a potem +20% nie wraca do startu.",
        "Нове значення = a·(1 − p/100). Увага: −20%, а потім +20% не повертає до старту.",
    ),

    # ——— 16 ———
    (16, "tabela wartości"): T(
        "Tabela pokazuje, jak zmienia się y, gdy rośnie x — przy proporcji widać stały mnożnik.",
        "Таблиця показує, як змінюється y, коли росте x — при пропорції видно сталий множник.",
        "Przykład: x = 1,2,3 → y = 2,4,6 (tu y = 2·x). Każdy wiersz sprawdzaj osobno.",
        "Приклад: x = 1,2,3 → y = 2,4,6 (тут y = 2·x). Кожен рядок перевіряй окремо.",
    ),
    (16, "proporcja"): T(
        "Proporcja to równość dwóch stosunków — „tyle samo części z jednej i z drugiej strony”.",
        "Пропорція — рівність двох відношень: «стільки самих частин з одного і з другого боку».",
        "Zapis: a/b = c/d. Sprawdzenie: a·d = b·c (iloczyn skrajnych = iloczyn środkowych).",
        "Запис: a/b = c/d. Перевірка: a·d = b·c (добуток крайніх = добуток середніх).",
    ),

    # ——— 17–18 ———
    (17, "wartość liczbowa"): T(
        "Wartość liczbowa wyrażenia powstaje, gdy zamiast litery wstawisz konkretną liczbę i policzysz.",
        "Числове значення виразу виникає, коли замість літери підставиш конкретне число і порахуєш.",
        "Dla x=2: 3x+1 = 3·2+1 = 7. Najpierw podstaw, potem kolejność działań.",
        "Для x=2: 3x+1 = 3·2+1 = 7. Спочатку підстав, потім порядок дій.",
    ),
    (18, "suma algebraiczna"): T(
        "Suma algebraiczna to wyrażenie z + i − łączące jednomiany (bloki z literami i liczbami).",
        "Алгебраїчна сума — вираз із + і −, що з'єднує одночлени (блоки з літерами й числами).",
        "Przykład: 3x − 2y + 5. Potem możesz łączyć wyrazy podobne.",
        "Приклад: 3x − 2y + 5. Потім можна об'єднувати подібні доданки.",
    ),
    (18, "przykład"): T(
        "Redukcja: grupujesz litery osobno i zwykłe liczby osobno, potem upraszczasz.",
        "Зведення: групуєш літери окремо і звичайні числа окремо, потім спрощуєш.",
        "2a+5−a+3 = (2a−a)+(5+3) = a+8. Najpierw nawiasy „w głowie”, potem wynik.",
        "2a+5−a+3 = (2a−a)+(5+3) = a+8. Спочатку дужки «в голові», потім результат.",
    ),

    # ——— 21–22 ———
    (21, "zamiana"): T(
        "Przy masie często zamieniasz jednostki × lub ÷ przez 1000 (kg ↔ g, t ↔ kg).",
        "При масі часто перетворюєш одиниці × або ÷ на 1000 (кг ↔ г, т ↔ кг).",
        "Zapamiętaj drabinkę: 1 kg = 1000 g; 1 t = 1000 kg. Przecinek skacze o 3 miejsca.",
        "Запам'ятай драбинку: 1 кг = 1000 г; 1 т = 1000 кг. Кома стрибає на 3 місця.",
    ),
    (21, "porównywanie"): T(
        "Żeby porównać masy, obie liczby muszą być w tej samej jednostce.",
        "Щоб порівняти маси, обидва числа мають бути в тій самій одиниці.",
        "Przykład: 1 kg i 800 g → zamień: 1000 g > 800 g, więc 1 kg jest cięższe.",
        "Приклад: 1 кг і 800 г → переведи: 1000 г > 800 г, тож 1 кг важчий.",
    ),
    (21, "przykłady"): T(
        "Ćwicz zamianę: przy kg ↔ g przecinek „skacze” o trzy miejsca.",
        "Тренуй перетворення: при кг ↔ г кома «стрибає» на три місця.",
        "250 g = 0,25 kg; 2,5 kg = 2500 g. Sprawdź, czy wynik ma sens (większy / mniejszy).",
        "250 г = 0,25 кг; 2,5 кг = 2500 г. Перевір, чи результат має сенс (більше / менше).",
    ),
    (22, "litr"): T(
        "Litr to wygodna jednostka objętości płynów — soki, woda, przepisy kuchenne.",
        "Літр — зручна одиниця об'єму рідин: соки, вода, кулінарні рецепти.",
        "1 litr = 1000 mililitrów. Duża butelka 1,5 l = 1500 ml.",
        "1 літр = 1000 мілілітрів. Велика пляшка 1,5 л = 1500 мл.",
    ),
    (22, "mililitr"): T(
        "Mililitr to tysięczna część litra — małe ilości: syrop, miarki, krople.",
        "Мілілітр — тисячна частина літра: малі кількості — сироп, мірки, краплі.",
        "1 ml = 1 cm³. Łyżeczka to zwykle około 5 ml.",
        "1 мл = 1 см³. Чайна ложка зазвичай близько 5 мл.",
    ),
    (22, "przeliczanie"): T(
        "Przeliczanie litr ↔ mililitr: mnożysz lub dzielisz przez 1000.",
        "Перетворення літр ↔ мілілітр: множиш або ділиш на 1000.",
        "Z litrów na ml: ×1000 (2,5 l = 2500 ml). Z ml na litry: ÷1000.",
        "З літрів у мл: ×1000 (2,5 л = 2500 мл). З мл у літри: ÷1000.",
    ),
    (22, "przykład"): T(
        "Objętość prostopadłościanu (pudełka) liczysz, mnożąc trzy wymiary.",
        "Об'єм прямокутного паралелепіпеда (коробки) рахуєш, множачи три виміри.",
        "Pudełko 2×3×4 cm → V = 2·3·4 = 24 cm³. Jednostka: cm³ (sześcienne).",
        "Коробка 2×3×4 см → V = 2·3·4 = 24 см³. Одиниця: см³ (кубічні).",
    ),

    # ——— 23–27 ———
    (23, "doba"): T(
        "Doba to cały dzień i cała noc — pełne 24 godziny od północy do północy.",
        "Доба — весь день і вся ніч: повні 24 години від півночі до півночі.",
        "1 doba = 24 h. Potem kalendarz zaczyna kolejny dzień.",
        "1 доба = 24 год. Потім календар починає наступний день.",
    ),
    (24, "data"): T(
        "Data mówi, który to dzień, miesiąc i rok — adres dnia w kalendarzu.",
        "Дата каже, який це день, місяць і рік — адреса дня в календарі.",
        "W Polsce zapisujemy: dzień.miesiąc.rok — np. 18.07.2015.",
        "У Польщі пишемо: день.місяць.рік — напр. 18.07.2015.",
    ),
    (24, "kolejność dni"): T(
        "Dni tygodnia zawsze idą w tej samej kolejności — jak pętla, która wraca do poniedziałku.",
        "Дні тижня завжди йдуть у тому самому порядку — як петля, що повертається до понеділка.",
        "Kolejność: pn → wt → śr → cz → pt → so → nd → znowu pn.",
        "Порядок: пн → вт → ср → чт → пт → сб → нд → знову пн.",
    ),
    (25, "różnica temperatur"): T(
        "Różnica temperatur mówi, o ile stopni się ociepliło lub ochłodziło — to odległość na skali.",
        "Різниця температур каже, на скільки градусів потепліло або похолодало — відстань на шкалі.",
        "Z −4°C do +6°C: |6 − (−4)| = 10°. Liczysz „odległość”, nie odejmuj byle jak.",
        "З −4°C до +6°C: |6 − (−4)| = 10°. Рахуєш «відстань», не віднімай абияк.",
    ),
    (26, "budżet"): T(
        "Budżet to prosty plan pieniędzy: ile masz (przychód) i ile wydajesz (wydatek).",
        "Бюджет — простий план грошей: скільки маєш (дохід) і скільки витрачаєш (витрата).",
        "Zostaje: przychód − wydatek. Nie wydawaj więcej, niż masz — sprawdź resztę.",
        "Лишається: дохід − витрата. Не витрачай більше, ніж маєш — перевір залишок.",
    ),
    (27, "droga i czas"): T(
        "Z jednego związku prędkości robisz trzy obliczenia: drogę, czas albo prędkość.",
        "З одного зв'язку швидкості робиш три обчислення: шлях, час або швидкість.",
        "Wzory: s = v·t; t = s/v; v = s/t. Wybierz ten, którego szukasz.",
        "Формули: s = v·t; t = s/v; v = s/t. Вибери ту, яку шукаєш.",
    ),
    (27, "obliczanie odległości"): T(
        "Odległość w terenie liczysz z mapy: miara na mapie × liczba ze skali (po zamianie jednostek).",
        "Відстань на місцевості рахуєш з мапи: міра на мапі × число з масштабу (після перетворення одиниць).",
        "Przykład: 3 cm i skala 1:100 000 → 3·100 000 cm = 3 km.",
        "Приклад: 3 см і масштаб 1:100 000 → 3·100 000 см = 3 км.",
    ),
    (27, "przykład v"): T(
        "Prędkość liczysz, dzieląc przebytą drogę przez czas jazdy.",
        "Швидкість рахуєш, ділячи пройдений шлях на час руху.",
        "120 km w 2 godziny → v = 120:2 = 60 km/h. Jednostka: km na godzinę.",
        "120 км за 2 години → v = 120:2 = 60 км/год. Одиниця: км за годину.",
    ),

    # ——— 29–32 ———
    (29, "rodzaje trójkątów"): T(
        "Trójkąty dzielimy na rodzaje według boków oraz według kątów — to dwie osobne klasyfikacje.",
        "Трикутники ділимо на види за сторонами та за кутами — це дві окремі класифікації.",
        "Boki: równoboczny / równoramienny / różnoboczny. Kąty: ostro-, prawo- lub rozwartokątny.",
        "Сторони: рівносторонній / рівнобедрений / різносторонній. Кути: гостро-, прямо- або тупокутний.",
    ),
    (30, "koło"): T(
        "Koło to okrąg razem z całym wnętrzem — jak tarcza albo talerz.",
        "Круг — коло разом із усім серединам: як диск або тарілка.",
        "Nie myl: okrąg = tylko linia (brzeg); koło = linia + wszystko w środku.",
        "Не плутай: коло = лише лінія (край); круг = лінія + все всередині.",
    ),
    (30, "środek"): T(
        "Środek okręgu (lub koła) to punkt, z którego wszystkie punkty na brzegu są w równej odległości.",
        "Центр кола (або круга) — точка, від якої всі точки на краю на однаковій відстані.",
        "Oznaczamy zwykle literą O. Od O do brzegu — to promień.",
        "Позначаємо зазвичай літерою O. Від O до краю — це радіус.",
    ),
    (30, "promień"): T(
        "Promień to odcinek od środka do punktu na okręgu — „pół średnicy”.",
        "Радіус — відрізок від центра до точки на колі: «пів діаметра».",
        "Zapis: r = OA. Wszystkie promienie tego samego okręgu mają tę samą długość.",
        "Запис: r = OA. Усі радіуси того самого кола мають ту саму довжину.",
    ),
    (31, "pole koła"): T(
        "Pole koła to miara powierzchni „tarczy” — ile miejsca zajmuje wnętrze.",
        "Площа круга — міра поверхні «диска»: скільки місця займає середина.",
        "Wzór: P = π·r². Najpierw podnieś r do kwadratu, potem pomnóż przez π.",
        "Формула: P = π·r². Спочатку піднеси r до квадрата, потім помнож на π.",
    ),
    (31, "przykład C"): T(
        "Długość okręgu (obwód) liczysz ze wzoru C = 2·π·r albo C = π·d.",
        "Довжину кола (обвід) рахуєш за формулою C = 2·π·r або C = π·d.",
        "Dla r=5 i π≈3,14: C ≈ 2·3,14·5 = 31,4 (jednostki długości).",
        "Для r=5 і π≈3,14: C ≈ 2·3,14·5 = 31,4 (одиниці довжини).",
    ),
    (31, "przykład P"): T(
        "Pole koła liczysz ze wzoru P = π·r² — najpierw r², potem ×π.",
        "Площу круга рахуєш за формулою P = π·r² — спочатку r², потім ×π.",
        "Dla r=5: r²=25, P ≈ 3,14·25 = 78,5 (jednostki pola, np. cm²).",
        "Для r=5: r²=25, P ≈ 3,14·25 = 78,5 (одиниці площі, напр. см²).",
    ),
    (32, "wierzchołek"): T(
        "Wierzchołek kąta to punkt, w którym stykają się oba ramiona — wspólny początek.",
        "Вершина кута — точка, де стикаються обидві сторони: спільний початок.",
        "W oznaczeniu ∠AOB wierzchołek jest w środku nazwy: to punkt O.",
        "У позначенні ∠AOB вершина посередині назви: це точка O.",
    ),
    (32, "półobrót / obrót"): T(
        "Półobrót to obrót o 180° (jak odwrócenie się plecami). Pełny obrót to 360° — wracasz twarzą w tę samą stronę.",
        "Півоберт — поворот на 180° (як розвернутися спиною). Повний оберт — 360°: знову обличчям у той самий бік.",
        "Zapamiętaj punkty orientacyjne: 180° = półobrót, 360° = pełny obrót.",
        "Запам'ятай орієнтири: 180° = півоберт, 360° = повний оберт.",
    ),

    # ——— 33 kąty ———
    (33, "kąt zerowy"): T(
        "Kąt zerowy: oba ramiona leżą na sobie — jak zamknięte nożyczki. Miara wynosi 0°.",
        "Нульовий кут: обидві сторони лежать одна на одній — як закриті ножиці. Міра 0°.",
        "Na kątomierzu to początek skali: 0°. Jeszcze nie ma „rozworu”.",
        "На кутомірі це початок шкали: 0°. Ще немає «розхилу».",
    ),
    (33, "kąt ostry"): T(
        "Kąt ostry jest mniejszy od prostego — „ostry”, jak mało otwarte nożyczki.",
        "Гострий кут менший за прямий — «гострий», як трохи відкриті ножиці.",
        "Zapis: 0° < α < 90°. Wszystko między zerem a kątem prostym.",
        "Запис: 0° < α < 90°. Усе між нулем і прямим кутом.",
    ),
    (33, "kąt prosty"): T(
        "Kąt prosty ma dokładnie 90° — jak róg kartki, zeszytu albo kwadratu.",
        "Прямий кут має рівно 90° — як кут аркуша, зошита чи квадрата.",
        "α = 90°. Na rysunku często znaczek □ przy wierzchołku.",
        "α = 90°. На малюнку часто значок □ біля вершини.",
    ),
    (33, "kąt rozwarty"): T(
        "Kąt rozwarty jest większy od prostego, ale mniejszy od półpełnego — „szeroko otwarty”.",
        "Тупий кут більший за прямий, але менший за розгорнутий — «широко відкритий».",
        "Zapis: 90° < α < 180°. Przykład: 120°.",
        "Запис: 90° < α < 180°. Приклад: 120°.",
    ),
    (33, "kąt półpełny"): T(
        "Kąt półpełny to 180° — ramiona leżą w jednej linii prostej, jak otwarta książka na płasko.",
        "Розгорнутий кут — 180°: сторони лежать на одній прямій, як книжка плазом.",
        "α = 180°. To pół obrotu — ważny punkt orientacyjny.",
        "α = 180°. Це півоберта — важливий орієнтир.",
    ),
    (33, "kąt pełny"): T(
        "Kąt pełny to pełny obrót wokół wierzchołka — wracasz do tego samego ramienia. Miara 360°.",
        "Повний кут — повний оберт навколо вершини: повертаєшся до тієї самої сторони. Міра 360°.",
        "α = 360°. Cała „tarcza” wokół punktu.",
        "α = 360°. Увесь «диск» навколо точки.",
    ),

    # ——— 34–36 ———
    (34, "proste równoległe"): T(
        "Proste równoległe biegną obok siebie i nigdy się nie przecinają — jak szyny torów.",
        "Паралельні прямі йдуть поруч і ніколи не перетинаються — як рейки колії.",
        "Zapis w zeszycie: a ∥ b (znak równoległości).",
        "Запис у зошиті: a ∥ b (знак паралельності).",
    ),
    (34, "przyległe"): T(
        "Kąty przyległe mają wspólne ramię i razem tworzą prostą — ich suma to 180°.",
        "Суміжні кути мають спільну сторону і разом утворюють пряму — їхня сума 180°.",
        "Jeśli jeden ma 70°, drugi ma 110°, bo 70+110=180.",
        "Якщо один має 70°, другий має 110°, бо 70+110=180.",
    ),
    (34, "wierzchołkowe"): T(
        "Kąty wierzchołkowe leżą naprzeciw siebie przy przecięciu dwóch prostych — zawsze są równe.",
        "Вертикальні кути лежать навпроти при перетині двох прямих — завжди рівні.",
        "Zapamiętaj: naprzeciwko = równe. Nie trzeba mierzyć obu, jeśli znasz jeden.",
        "Запам'ятай: навпроти = рівні. Не треба міряти обидва, якщо знаєш один.",
    ),
    (35, "prostokąt"): T(
        "Dla prostokąta liczysz obwód (dookoła) i pole (ile w środku) z boków a i b.",
        "Для прямокутника рахуєш периметр (довкола) і площу (скільки всередині) зі сторін a і b.",
        "Obwód = 2·(a+b). Pole = a·b. Nie myl jednostek: cm vs cm².",
        "Периметр = 2·(a+b). Площа = a·b. Не плутай одиниці: см vs см².",
    ),
    (35, "kwadrat"): T(
        "Kwadrat ma wszystkie boki równe — wzory na obwód i pole są najprostsze.",
        "Квадрат має всі сторони рівні — формули периметра й площі найпростіші.",
        "Obwód = 4·a. Pole = a² (bok razy bok). Przykład: a=3 → pole 9, obwód 12.",
        "Периметр = 4·a. Площа = a² (бік на бік). Приклад: a=3 → площа 9, периметр 12.",
    ),
    (36, "sześcian"): T(
        "Sześcian to bryła jak kostka: 6 kwadratowych ścian i wszystkie krawędzie równe.",
        "Куб — тіло як гральний кубик: 6 квадратних граней і всі ребра рівні.",
        "Objętość: V = a³ (krawędź × krawędź × krawędź).",
        "Об'єм: V = a³ (ребро × ребро × ребро).",
    ),
    (36, "prostopadłościan"): T(
        "Prostopadłościan wygląda jak pudełko: ściany to prostokąty, krawędzie mogą mieć trzy różne długości.",
        "Прямокутний паралелепіпед виглядає як коробка: грані — прямокутники, ребра можуть мати три різні довжини.",
        "Objętość: V = a·b·c — mnożysz długość, szerokość i wysokość.",
        "Об'єм: V = a·b·c — множиш довжину, ширину й висоту.",
    ),
    (36, "objętość sześcianu"): T(
        "Objętość sześcianu to „ile miejsca w środku kostki” — krawędź do trzeciej potęgi.",
        "Об'єм куба — «скільки місця всередині кубика»: ребро в третьому степені.",
        "V = a³. Najpierw a·a·a. Jednostka: cm³, m³…",
        "V = a³. Спочатку a·a·a. Одиниця: см³, м³…",
    ),

    # ——— 38–42 ———
    (38, "oś Y"): T(
        "Oś Y jest pionowa: w górę wartości dodatnie, w dół — ujemne.",
        "Вісь Y вертикальна: вгору додатні значення, вниз — від'ємні.",
        "W zapisie punktu (x, y) druga liczba to właśnie y — „jak wysoko”.",
        "У записі точки (x, y) друге число — саме y: «як високо».",
    ),
    (38, "punkt (x, y)"): T(
        "Punkt na płaszczyźnie zapisujemy parą liczb: najpierw x (w prawo/lewo), potem y (w górę/dół).",
        "Точку на площині записуємо парою чисел: спочатку x (вправо/вліво), потім y (вгору/вниз).",
        "A(3, 2): 3 w prawo, 2 w górę. Nie zamieniaj kolejności — (2, 3) to inny punkt!",
        "A(3, 2): 3 вправо, 2 вгору. Не міняй порядок — (2, 3) це інша точка!",
    ),
    (38, "ćwiartki"): T(
        "Układ współrzędnych dzieli płaszczyznę na 4 ćwiartki — zależnie od znaków x i y.",
        "Система координат ділить площину на 4 чверті — залежно від знаків x і y.",
        "I: (+,+); II: (−,+); III: (−,−); IV: (+,−). Ćwiartka I to prawo-góra.",
        "I: (+,+); II: (−,+); III: (−,−); IV: (+,−). Чверть I — право-вгору.",
    ),
    (40, "moda"): T(
        "Moda to wartość, która pojawia się najczęściej w zestawie danych.",
        "Мода — значення, яке найчастіше трапляється в наборі даних.",
        "Może być więcej niż jedna moda, albo żadnej wyraźnej (gdy wszystko po równo).",
        "Може бути більше ніж одна мода, або жодної чіткої (коли все порівну).",
    ),
    (40, "przykład średniej"): T(
        "Średnia arytmetyczna: dodajesz wszystkie wartości i dzielisz przez ich liczbę.",
        "Середнє арифметичне: додаєш усі значення і ділиш на їхню кількість.",
        "Dla 2,5,5,8: (2+5+5+8):4 = 20:4 = 5. To „typowy” wynik w środku.",
        "Для 2,5,5,8: (2+5+5+8):4 = 20:4 = 5. Це «типовий» результат посередині.",
    ),
    (40, "przykład mediany"): T(
        "Mediana to wartość środkowa po uporządkowaniu liczb od najmniejszej do największej.",
        "Медіана — середнє за порядком значення після впорядкування від найменшого до найбільшого.",
        "Dla 2,5,5,8 (parzysta liczba): bierzemy średnią z dwóch środkowych → (5+5)/2 = 5.",
        "Для 2,5,5,8 (парна кількість): беремо середнє двох серединних → (5+5)/2 = 5.",
    ),
    (40, "przykład mody"): T(
        "Moda: szukasz liczby, która powtarza się najczęściej.",
        "Мода: шукаєш число, яке повторюється найчастіше.",
        "W zestawie 2,5,5,8 najczęściej pada 5 — więc moda = 5.",
        "У наборі 2,5,5,8 найчастіше трапляється 5 — тож мода = 5.",
    ),
    (41, "permutacje"): T(
        "Permutacje to różne ustawienia tych samych rzeczy w kolejności — bez powtórzeń.",
        "Перестановки — різні розстановки тих самих речей у порядку, без повторень.",
        "Dla n rzeczy: n! = n·(n−1)·…·1. Przykład: 3 książki → 3·2·1 = 6 ustawień.",
        "Для n речей: n! = n·(n−1)·…·1. Приклад: 3 книжки → 3·2·1 = 6 розстановок.",
    ),
    (41, "przykład P"): T(
        "Na kostce każdy wynik od 1 do 6 jest jednakowo możliwy — szansa na konkretną liczbę to 1 z 6.",
        "На кубику кожен результат від 1 до 6 однаково можливий — шанс на конкретне число 1 з 6.",
        "P(6) = 1/6. Wzór: korzystne wyniki / wszystkie możliwe wyniki.",
        "P(6) = 1/6. Формула: сприятливі / усі можливі результати.",
    ),
    (42, "+ plus / dodawanie"): T(
        "Znak + oznacza dodawanie — łączymy liczby albo dokładamy.",
        "Знак + означає додавання — об'єднуємо числа або докладаємо.",
        "Czytamy: „plus” albo „dodać”. Przykład: 3 + 5 = 8.",
        "Читаємо: «плюс» або «додати». Приклад: 3 + 5 = 8.",
    ),
    (42, "− minus / odejmowanie"): T(
        "Znak − oznacza odejmowanie — zabieramy część. Ten sam znak bywa przy liczbach ujemnych.",
        "Знак − означає віднімання — забираємо частину. Той самий знак буває біля від'ємних чисел.",
        "Czytamy: „minus” albo „odjąć”. Przykład: 9 − 4 = 5; temperatura −3°C.",
        "Читаємо: «мінус» або «відняти». Приклад: 9 − 4 = 5; температура −3°C.",
    ),
    (42, "× · mnożenie"): T(
        "Znak × albo kropka · oznacza mnożenie — szybkie dodawanie tej samej liczby.",
        "Знак × або крапка · означає множення — швидке додавання того самого числа.",
        "Przykład: 4 × 3 = 12. Przy literach często piszemy 4a zamiast 4·a.",
        "Приклад: 4 × 3 = 12. При літерах часто пишемо 4a замість 4·a.",
    ),
    (42, ": / dzielenie"): T(
        "Znak : albo kreska / oznacza dzielenie — rozdzielamy na równe części.",
        "Знак : або риска / означає ділення — розподіляємо на рівні частини.",
        "Przykład: 12 : 3 = 4. Ułamek 12/3 to też dzielenie 12÷3.",
        "Приклад: 12 : 3 = 4. Дріб 12/3 — це теж ділення 12÷3.",
    ),

    # ——— dopiski jasności (reszta) ———
    (7, "× i :"): T(
        "Mnożenie i dzielenie są „silniejsze” niż dodawanie i odejmowanie — robisz je wcześniej.",
        "Множення і ділення «сильніші» за додавання й віднімання — робиш їх раніше.",
        "Przykład: 2+3×4. Najpierw 3×4=12, potem 2+12=14 (nie 5×4!).",
        "Приклад: 2+3×4. Спочатку 3×4=12, потім 2+12=14 (не 5×4!).",
    ),
    (14, "kwadraty doskonałe"): T(
        "Kwadrat doskonały to wynik podniesienia liczby naturalnej do kwadratu — z niego pierwiastek wychodzi „ładnie”.",
        "Повний квадрат — результат піднесення натурального числа до квадрата: з нього корінь виходить «гарно».",
        "Ucz się do 10²: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 (bo 1²…10²).",
        "Вчи до 10²: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 (бо 1²…10²).",
    ),
    (16, "przykład"): T(
        "W życiu proporcja widać przy cenie za kilogram: im więcej kg, tym proporcjonalnie więcej złotych.",
        "У житті пропорцію видно при ціні за кілограм: що більше кг, то пропорційно більше злотих.",
        "3 kg → 12 zł ⇒ 1 kg = 4 zł ⇒ 5 kg → 20 zł. Najpierw znajdź cenę za 1, potem pomnóż.",
        "3 кг → 12 zł ⇒ 1 кг = 4 zł ⇒ 5 кг → 20 zł. Спочатку знайди ціну за 1, потім помнож.",
    ),
    (17, "kolejność"): T(
        "W wyrażeniach z literami obowiązuje ta sama kolejność działań, co przy zwykłych liczbach.",
        "У виразах із літерами той самий порядок дій, що й при звичайних числах.",
        "Kolejność: najpierw nawiasy, potem potęgi, potem × i :, na końcu + i −.",
        "Порядок: спочатку дужки, потім степені, потім × і :, наприкінці + і −.",
    ),
    (18, "jednomian"): T(
        "Jednomian to jeden „kawałek” zapisu: liczba, litery albo ich iloczyn — bez znaków + i − w środku.",
        "Одночлен — один «шматок» запису: число, літери або їхній добуток — без знаків + і − всередині.",
        "Przykłady jednomianów: 5x², −3ab, sama liczba 7. To nie jest jeszcze suma.",
        "Приклади одночленів: 5x², −3ab, саме число 7. Це ще не сума.",
    ),
    (33, "kąt rozwarty"): T(
        "Kąt rozwarty jest większy od prostego, ale mniejszy od półpełnego — „szeroko otwarty”.",
        "Тупий кут більший за прямий, але менший за розгорнутий — «широко відкритий».",
        "Miara: między 90° a 180° (nie wliczając końców). Przykład z życia: 120°.",
        "Міра: між 90° і 180° (без кінців). Приклад із життя: 120°.",
    ),
    (34, "naprzemianległe"): T(
        "Kąty naprzemianległe leżą na przemian po stronach siecznej, między dwiema prostymi.",
        "Навхрест лежачі кути лежать навперемінно по боках січної, між двома прямими.",
        "Gdy proste są równoległe (a ∥ b), kąty naprzemianległe są równe — jak „odbicia”.",
        "Коли прямі паралельні (a ∥ b), навхрест лежачі кути рівні — як «відбиття».",
    ),
    (40, "średnia arytmetyczna"): T(
        "Średnia arytmetyczna to „typowa” wartość: suma wszystkich danych podzielona przez ich liczbę.",
        "Середнє арифметичне — «типове» значення: сума всіх даних, поділена на їхню кількість.",
        "Wzór: średnia = (suma wartości) / (ile wartości). Najpierw dodaj, potem podziel.",
        "Формула: середнє = (сума значень) / (скільки значень). Спочатку додай, потім поділи.",
    ),
    (4, "właściwości +"): T(
        "Przy dodawaniu możesz zmienić kolejność składników — wynik będzie ten sam (przemienność).",
        "При додаванні можна змінити порядок доданків — результат буде той самий (переставна).",
        "a+b=b+a. Możesz też grupować: (a+b)+c = a+(b+c) — wybierz wygodniejszą kolejność.",
        "a+b=b+a. Можна й групувати: (a+b)+c = a+(b+c) — вибери зручніший порядок.",
    ),
    (6, "iloraz"): T(
        "Iloraz to wynik dzielenia — liczba po znaku =. To „ile wyszło w każdej części” albo „ile razy”.",
        "Частка — результат ділення — число після знака =. Це «скільки вийшло в кожній частині» або «скільки разів».",
        "W zapisie 15:5=3 liczba 3 to iloraz. Dzielna to 15, dzielnik to 5.",
        "У записі 15:5=3 число 3 — частка. Ділене — 15, дільник — 5.",
    ),
    (6, ":1 i : siebie"): T(
        "Dzielenie przez 1 nic nie zmienia. Liczba dzielona przez siebie daje 1. Przez zero nigdy nie dzielimy!",
        "Ділення на 1 нічого не змінює. Число, поділене на себе, дає 1. На нуль ніколи не ділимо!",
        "Zapamiętaj: a:1=a; a:a=1 (gdy a≠0). Zapis a:0 jest zabroniony.",
        "Запам'ятай: a:1=a; a:a=1 (коли a≠0). Запис a:0 заборонений.",
    ),
    (8, "przez 3"): T(
        "Liczba dzieli się przez 3, gdy suma jej cyfr dzieli się przez 3 — szybki test bez długiego dzielenia.",
        "Число ділиться на 3, коли сума його цифр ділиться на 3 — швидкий тест без довгого ділення.",
        "Przykład: 123 → 1+2+3=6, a 6:3=2 → więc 123 też dzieli się przez 3.",
        "Приклад: 123 → 1+2+3=6, а 6:3=2 → тож 123 теж ділиться на 3.",
    ),
    (8, "przez 5"): T(
        "Liczba dzieli się przez 5, gdy kończy się cyfrą 0 albo 5.",
        "Число ділиться на 5, коли закінчується цифрою 0 або 5.",
        "Końcówka 0 lub 5 → tak (10, 25, 80). Inna cyfra na końcu → nie.",
        "Закінчення 0 або 5 → так (10, 25, 80). Інша цифра в кінці → ні.",
    ),
    (15, "zwiększenie o p%"): T(
        "Zwiększenie o p% to dodanie p procent do liczby — np. podwyżka albo wzrost o część ze stu.",
        "Збільшення на p% — додавання p відсотків до числа: напр. підвищення або ріст на частину зі ста.",
        "Nowa wartość = a·(1 + p/100). Przykład: +20% z 50 → 50·1,2 = 60.",
        "Нове значення = a·(1 + p/100). Приклад: +20% від 50 → 50·1,2 = 60.",
    ),
    (18, "współczynnik"): T(
        "Współczynnik to liczba stojąca przed literami w jednomianie — mówi „ile razy” część literowa.",
        "Коефіцієнт — число перед літерами в одночлені: каже «скільки разів» літерна частина.",
        "W 7a²b współczynnik to 7. W −3x współczynnik to −3 (ze znakiem!).",
        "У 7a²b коефіцієнт — 7. У −3x коефіцієнт — −3 (зі знаком!).",
    ),
    (20, "porównywanie"): T(
        "Żeby porównać długości, obie miary muszą być w tej samej jednostce.",
        "Щоб порівняти довжини, обидві міри мають бути в тій самій одиниці.",
        "Przykład: 1,2 m i 95 cm → zamień na cm: 120 cm > 95 cm.",
        "Приклад: 1,2 м і 95 см → переведи в см: 120 см > 95 см.",
    ),
    (26, "zapis"): T(
        "Pieniądze zapisujemy jak liczbę dziesiętną: złote przed przecinkiem, grosze po przecinku.",
        "Гроші записуємо як десяткове число: злоті перед комою, гроші після коми.",
        "12,50 zł = 12 złotych i 50 groszy. Zawsze dwa miejsca po przecinku przy groszach.",
        "12,50 zł = 12 злотих і 50 грошів. Завжди два знаки після коми при грошах.",
    ),
    (30, "okrąg"): T(
        "Okrąg to sama linia — brzeg koła, bez wnętrza. Jak obwódka talerza, nie cały talerz.",
        "Коло — сама лінія: край круга, без нутра. Як край тарілки, не вся тарілка.",
        "Zapamiętaj: okrąg = brzeg; koło = brzeg + wnętrze.",
        "Запам'ятай: коло = край; круг = край + середина.",
    ),
    (32, "ramiona / strony"): T(
        "Ramiona kąta to dwie półproste wychodzące ze wspólnego wierzchołka — „boki” kąta.",
        "Сторони кута — дві півпрямі зі спільної вершини: «боки» кута.",
        "W ∠AOB ramiona to OA i OB. Wierzchołek O jest ich wspólnym początkiem.",
        "У ∠AOB сторони — OA і OB. Вершина O — їхній спільний початок.",
    ),

    # ——— język i metodyka (ostateczna korekta) ———
    (1, "porównanie"): T(
        "Porównanie mówi, która liczba jest mniejsza, równa albo większa.",
        "Порівняння каже, яке число менше, рівне або більше.",
        "Znak < i > ma otwartą stronę w kierunku większej liczby: 3 < 7, 9 > 2.",
        "Знак < і > має відкритий бік до більшого числа: 3 < 7, 9 > 2.",
    ),
    (28, "półprosta"): T(
        "Półprosta ma początek (punkt) i biegnie w jedną stronę bez końca — jak światło latarki.",
        "Півпряма має початок (точку) і йде в один бік без кінця — як світло ліхтарика.",
        "Zapis: półprosta OA. Nie myl z promieniem okręgu (odcinek od środka do okręgu)!",
        "Запис: півпряма OA. Не плутай із радіусом кола (відрізок від центра до кола)!",
    ),
    (31, "zależność"): T(
        "Gdy promień rośnie 2 razy, długość okręgu też ×2, ale pole rośnie ×4.",
        "Коли радіус зростає в 2 рази, довжина кола теж ×2, але площа — ×4.",
        "Pole zależy od r², dlatego rośnie szybciej niż obwód.",
        "Площа залежить від r², тому росте швидше за довжину кола.",
    ),
}
