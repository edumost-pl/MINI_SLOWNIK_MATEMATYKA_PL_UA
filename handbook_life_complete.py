# -*- coding: utf-8 -*-
"""
Pełne przykłady „z życia” + paski W życiu + częste błędy — poziom strony 1.
Analiza: nauczyciel PL, native, metodyk SP, designer (jasna scena + zapis).
"""

def E(pl, ua):
    return {"example_pl": pl, "example_ua": ua}


# ——— Pasek „W życiu” na każdej stronie (nie domyślna kategoria) ———
PAGE_LIFE = {
    1: ("Liczby w sklepie, na boisku, w klasie — wszędzie, gdzie coś liczysz.",
        "Числа в магазині, на майданчику, у класі — скрізь, де щось лічиш."),
    2: ("Na zegarach, w numerach rozdziałów i na pomnikach — liczby rzymskie wciąż żyją.",
        "На годинниках, у номерах розділів і на пам'ятниках — римські числа досі живі."),
    3: ("Temperatura, dług, piętra pod ziemią — tu pojawiają się liczby ujemne.",
        "Температура, борг, поверхи під землею — тут з'являються від'ємні числа."),
    4: ("Punkty w grze, cukierki, zakupy: ile razem? ile zostało?",
        "Очки в грі, цукерки, покупки: скільки разом? скільки лишилось?"),
    5: ("Rzędy ławek, pudełka kredek — mnożenie to szybkie dodawanie tej samej liczby.",
        "Ряди парт, коробки олівців — множення = швидке додавання того самого числа."),
    6: ("Rozdajesz cukierki po równo w klasie — sprawiedliwe rozdawanie = dzielenie.",
        "Роздаєш цукерки порівну в класі — справедлива роздача = ділення."),
    7: ("W zeszycie liczysz krok po kroku: najpierw nawiasy, potem potęgi, potem × i :.",
        "У зошиті рахуєш крок за кроком: спочатку дужки, потім степені, потім × і :."),
    8: ("Szybki test bez długiego dzielenia: czy numer domu dzieli się przez 2, 3, 5…?",
        "Швидкий тест без довгого ділення: чи номер будинку ділиться на 2, 3, 5…?"),
    9: ("Pizza, tort, czekolada — ułamek to część całości.",
        "Піца, торт, шоколад — дріб це частина цілого."),
    10: ("Skracasz ułamek albo sprowadzasz do wspólnego mianownika — żeby łatwiej liczyć.",
        "Скорочуєш дріб або зводиш до спільного знаменника — щоб легше рахувати."),
    11: ("Cena 12,50 zł, wynik na kalkulatorze — ułamki dziesiętne w codziennych liczbach.",
        "Ціна 12,50 zł, результат на калькуляторі — десяткові дроби в щоденних числах."),
    12: ("Składasz kawałki pizzy, mnożysz w przepisie — działania na ułamkach.",
        "Складаєш шматки піци, множиш у рецепті — дії з дробами."),
    13: ("Szybki zapis: zamiast 2·2·2·2 piszesz 2⁴ — to potęga.",
        "Швидкий запис: замість 2·2·2·2 пишеш 2⁴ — це степінь."),
    14: ("Znasz pole kwadratowego dywanu — pierwiastek mówi, jaki ma bok.",
        "Знаєш площу квадратного килима — корінь каже, який у нього бік."),
    15: ("Wyprzedaż −20%, wynik testu 80% — procenty to części ze 100.",
        "Розпродаж −20%, результат тесту 80% — відсотки це частини зі 100."),
    16: ("Cena za kilogram, mapa w skali — gdy jedno rośnie, drugie też (proporcja).",
        "Ціна за кілограм, мапа в масштабі — коли одне росте, друге теж (пропорція)."),
    17: ("Przepis: 3x cukru — litera zamiast liczby, bo jeszcze nie wiesz ile.",
        "Рецепт: 3x цукру — літера замість числа, бо ще не знаєш скільки."),
    18: ("Długi zapis z x upraszczasz: łączysz wyrazy podobne — jak porządki w zeszycie.",
        "Довгий запис з x спрощуєш: об'єднуєш подібні доданки — як порядок у зошиті."),
    19: ("Zagadka: „myślałem liczbę, dodałem 5, wyszło 12” — szukasz niewiadomej.",
        "Загадка: «думав число, додав 5, вийшло 12» — шукаєш невідоме."),
    20: ("Linijka, wzrost, boisko — mierzymy długość i przeliczamy jednostki.",
        "Лінійка, зріст, поле — міряємо довжину й перетворюємо одиниці."),
    21: ("Waga w sklepie, przepis na ciasto — masa w gramach i kilogramach.",
        "Ваги в магазині, рецепт тістечка — маса в грамах і кілограмах."),
    22: ("Butelka soku, pudełko — objętość w litrach i centymetrach sześciennych.",
        "Пляшка соку, коробка — об'єм у літрах і кубічних сантиметрах."),
    23: ("Przerwa 15 minut, lekcja 45 — czas w szkole liczysz w minutach i godzinach.",
        "Перерва 15 хвилин, урок 45 — час у школі рахуєш у хвилинах і годинах."),
    24: ("Urodziny, ferie, plan tygodnia — kalendarz porządkuje dni i miesiące.",
        "День народження, канікули, план тижня — календар впорядковує дні й місяці."),
    25: ("Prognoza pogody rano: +12°C albo −5°C — temperatura na termometrze.",
        "Прогноз погоди вранці: +12°C або −5°C — температура на термометрі."),
    26: ("5 zł na bułkę, reszta z 10 zł, kieszonkowe — pieniądze jak w sklepie.",
        "5 zł на булочку, решта з 10 zł, кишенькові — гроші як у магазині."),
    27: ("Samochód w podróży, mapa wycieczki — prędkość, droga, skala.",
        "Авто в подорожі, мапа екскурсії — швидкість, шлях, масштаб."),
    28: ("Okno = prostokąt, znak = trójkąt — figury wokół Ciebie w klasie i na dworze.",
        "Вікно = прямокутник, знак = трикутник — фігури навколо тебе в класі й надворі."),
    29: ("Dach, drzwi, kafelek — trójkąty i czworokąty wokół Ciebie.",
        "Дах, двері, плитка — трикутники й чотирикутники навколо тебе."),
    30: ("Talerz, koło roweru, pierścień — okrąg i koło w życiu.",
        "Тарілка, колесо велосипеда, кільце — коло й круг у житті."),
    31: ("Obwód okrągłego dywanu albo pole pizza — tu pomaga liczba π.",
        "Обвід круглого килима або площа піци — тут допомагає число π."),
    32: ("Otwarte nożyczki, róg książki — kąt to „rozwór” dwóch ramion.",
        "Відкриті ножиці, кут книжки — кут це «розхил» двох сторін."),
    33: ("Porównujesz kąty na rysunku: ostry, prosty, rozwarty…",
        "Порівнюєш кути на малюнку: гострий, прямий, тупий…"),
    34: ("Tory kolejowe i przecznica — kąty przy prostych równoległych.",
        "Залізничні колії й поперечна — кути при паралельних прямих."),
    35: ("Ramka na zdjęcie, trawnik — obwód to „dookoła”, pole to „ile w środku”.",
        "Рамка для фото, газон — периметр це «довкола», площа — «скільки всередині»."),
    36: ("Pudełko, kostka, piłka — bryły mają objętość w trzech wymiarach.",
        "Коробка, кубик, м'яч — тіла мають об'єм у трьох вимірах."),
    37: ("Motyl, odbicie w lustrze — symetria to lustrzane powtórzenie.",
        "Метелик, відбиття в дзеркалі — симетрія це дзеркальне повторення."),
    38: ("Szukasz skarbu na mapie kratkowanej — punkt ma adres (x, y).",
        "Шукаєш скарб на картатій мапі — точка має адресу (x, y)."),
    39: ("Ankieta w klasie: ulubiony kolor — dane zbierasz, potem pokazujesz na wykresie.",
        "Опитування в класі: улюблений колір — дані збираєш, потім показуєш на діаграмі."),
    40: ("Średnia ocen, najczęściej wybierany smak lodów — średnia, mediana, moda.",
        "Середнє оцінок, найчастіший смак морозива — середнє, медіана, мода."),
    41: ("Losowanie dyżurnego, rzut kostką — ile sposobów? jaka szansa?",
        "Жеребкування чергового, кидок кубика — скільки способів? який шанс?"),
    42: ("Szybki zapis w zeszycie: +, −, ×, :, √, % — znaki, które musisz znać.",
        "Швидкий запис у зошиті: +, −, ×, :, √, % — знаки, які треба знати."),
    43: ("W zeszycie liczysz „w słupku” i najpierw szacujesz wynik w pamięci.",
        "У зошиті рахуєш «стовпчиком» і спочатку оцінюєш результат у пам'яті."),
    44: ("6·13 łatwiej jako 6·10+6·3 — rozdzielność pomaga w rachunku pamięciowym.",
        "6·13 легше як 6·10+6·3 — розподільність допомагає в усному рахунку."),
    45: ("Skracasz ułamek przez NWD; wspólny mianownik szukasz przez NWW.",
        "Скорочуєш дріб через НСД; спільний знаменник шукаєш через НСК."),
    46: ("3/4 z kieszonkowego albo „15 to 3/4 całości” — część i całość.",
        "3/4 від кишенькових або «15 — це 3/4 цілого» — частина і ціле."),
    47: ("Wzrost 1 m 42 cm, film 1 h 45 min — wyrażenia dwumianowane wokół Ciebie.",
        "Зріст 1 м 42 см, фільм 1 год 45 хв — двочленні вирази навколо тебе."),
    48: ("Ściana ⊥ podłoga, róg zeszytu — prostopadłość i najkrótsza odległość.",
        "Стіна ⊥ підлога, кут зошита — перпендикулярність і найкоротша відстань."),
    49: ("Znasz dwa kąty trójkąta — trzeci zawsze dopełnia do 180°.",
        "Знаєш два кути трикутника — третій завжди доповнює до 180°."),
    50: ("Pole działki w arach i hektarach; romb i trapez w zeszycie.",
        "Площа ділянки в арах і гектарах; ромб і трапеція в зошиті."),
    51: ("Pudełko, siatka do sklejenia modelu, ile papieru na opakowanie.",
        "Коробка, сітка для склеювання моделі, скільки паперу на обгортку."),
    52: ("Rabat, wynik testu, „jaki to procent?” — cztery typy zadań.",
        "Знижка, результат тесту, «який це відсоток?» — чотири типи задач."),
    53: ("Odległość do gwiazd albo małe bakterie — zapis z 10ᵏ.",
        "Відстань до зірок або малі бактерії — запис із 10ᵏ."),
    54: ("∛8=2; √50 upraszczasz do 5√2 — pierwiastki w zadaniach.",
        "∛8=2; √50 спрощуєш до 5√2 — корені в задачах."),
    55: ("Otwierasz nawiasy: każdy z każdym — jak w klasie 7–8.",
        "Розкриваєш дужки: кожен з кожним — як у класі 7–8."),
    56: ("Dzielicie nagrodę 2:3 albo składkę w stosunku — sprawiedliwie.",
        "Ділите нагороду 2:3 або складку у відношенні — справедливо."),
    57: ("Drabina przy ścianie, przekątna TV — a²+b²=c².",
        "Драбина біля стіни, діагональ TV — a²+b²=c²."),
    58: ("Dwa trójkąty „takie same” — cechy BBB, BKB, KBK.",
        "Два трикутники «такі самі» — ознаки ССС, СКС, КСК."),
    59: ("Na mapie w kratkę: środek odcinka i odległość między punktami.",
        "На мапі в клітинку: середина відрізка і відстань між точками."),
    60: ("Symetralna i dwusieczna — dzielą na pół (odcinek lub kąt).",
        "Серединний перпендикуляр і бісектриса — ділять навпіл (відрізок або кут)."),
    61: ("Na boisku i w klasie: prawo/lewo, dłuższy szalik, więcej cukierków — porównujesz świat.",
        "На майданчику і в класі: право/ліво, довший шарф, більше цукерок — порівнюєш світ."),
}

# ——— Częsty błąd (jak na stronach-wzorcach) ———
PAGE_MISTAKE = {
    1: ("Cyfra to nie to samo co liczba: 3 to cyfra; 35 to liczba z dwóch cyfr. Zero = pusto — o naturalnych pytaj nauczyciela.",
        "Цифра — не те саме, що число: 3 — цифра; 35 — число з двох цифр. Нуль = порожньо — про натуральні питай учителя."),
    2: ("IV to 4 (5−1), a VI to 6 (5+1). Kolejność znaków zmienia wynik!",
        "IV — це 4 (5−1), а VI — 6 (5+1). Порядок знаків змінює результат!"),
    3: ("−7 jest mniejsze niż −2 (leży bardziej w lewo), choć „7” wygląda na większe.",
        "−7 менше за −2 (лежить лівіше), хоча «7» виглядає більшим."),
    4: ("Przy odejmowaniu nie odwracaj kolejności: 9−4, nie 4−9. Pytaj: ile zostało?",
        "При відніманні не міняй порядок: 9−4, не 4−9. Питай: скільки лишилось?"),
    5: ("Tabliczka: 7×8 to nie 7+8. Najpierw zobacz 7+7+7…, potem skrót ×.",
        "Таблиця: 7×8 — це не 7+8. Спочатку побач 7+7+7…, потім скорочення ×."),
    6: ("Dzielenie = po równo. Dzielna / dzielnik: w 12:3 → 12 dzielimy, 3 — na ile.",
        "Ділення = порівну. Ділене / дільник: у 12:3 → 12 ділимо, 3 — на скільки."),
    7: ("2+3×4 = 14, nie 20. Najpierw mnożenie, potem dodawanie.",
        "2+3×4 = 14, не 20. Спочатку множення, потім додавання."),
    8: ("Cecha przez 3: suma cyfr, nie „ostatnia cyfra” (to jest przez 2 i 5/10).",
        "Ознака на 3: сума цифр, не «остання цифра» (це для 2 і 5/10)."),
    9: ("W ułamku 3/4: 3 to licznik (ile części), 4 — mianownik (na ile dzielimy).",
        "У дробі 3/4: 3 — чисельник (скільки частин), 4 — знаменник (на скільки ділимо)."),
    10: ("Przy dodawaniu ułamków nie dodawaj mianowników: 1/2+1/3 ≠ 2/5.",
        "При додаванні дробів не додавай знаменники: 1/2+1/3 ≠ 2/5."),
    11: ("1,25 < 1,3 — dopisz zero: 1,25 < 1,30. Nie porównuj „długości zapisu”.",
        "1,25 < 1,3 — допиши нуль: 1,25 < 1,30. Не порівнюй «довжину запису»."),
    12: ("Przy mnożeniu ułamków mnożysz licznik z licznikiem i mianownik z mianownikiem — nie na krzyż jak w proporcji.",
        "При множенні дробів множиш чисельник на чисельник і знаменник на знаменник — не навхрест як у пропорції."),
    13: ("2³ = 2·2·2 = 8, nie 2·3 = 6. Wykładnik mówi, ile razy mnożysz podstawę.",
        "2³ = 2·2·2 = 8, не 2·3 = 6. Показник каже, скільки разів множиш основу."),
    14: ("√9 = 3, bo 3²=9. Pierwiastek to nie „podziel przez 2”.",
        "√9 = 3, бо 3²=9. Корінь — це не «поділи на 2»."),
    15: ("„Więcej o 20%” to nie to samo co „20% z liczby”. Nowa = a·(1+20/100).",
        "«Більше на 20%» — не те саме, що «20% від числа». Нова = a·(1+20/100)."),
    16: ("W proporcji a/b = c/d iloczyn skrajnych = iloczyn środkowych (a·d = b·c).",
        "У пропорції a/b = c/d добуток крайніх = добуток середніх (a·d = b·c)."),
    19: ("Przenosząc na drugą stronę równania, zmieniasz znak: + staje się −.",
        "Переносячи на другий бік рівняння, змінюєш знак: + стає −."),
    20: ("1,2 m to 120 cm, nie 12 cm — patrz na „przesunięcie” przecinka przy zamianie.",
        "1,2 м — це 120 см, не 12 см — дивись на «зсув» коми при перетворенні."),
    23: ("1,5 h to 1 h 30 min, nie 1 h 50 min. 0,5 h = 30 minut.",
        "1,5 h — це 1 год 30 хв, не 1 год 50 хв. 0,5 h = 30 хвилин."),
    26: ("Przy pieniądzach ustawiaj przecinek pod przecinkiem: złote pod złotymi, grosze pod groszami.",
        "При грошах став кому під комою: злоті під злотими, гроші під грошима."),
    30: ("Promień to od środka do okręgu; średnica przechodzi przez środek i = 2·promień.",
        "Радіус — від центра до кола; діаметр проходить через центр і = 2·радіус."),
    31: ("Pole koła to π·r², nie π·d. Najpierw r, potem kwadrat, potem ×π.",
        "Площа круга — π·r², не π·d. Спочатку r, потім квадрат, потім ×π."),
    33: ("Kąt prosty ma 90°, nie „wygląda ostro”. Mierz kątomierzem.",
        "Прямий кут має 90°, не «виглядає гострим». Міряй кутоміром."),
    35: ("Pole to „ile w środku” (cm²), obwód to „dookoła” (cm). Nie myl jednostek!",
        "Площа — «скільки всередині» (см²), периметр — «довкола» (см). Не плутай одиниці!"),
    40: ("Średnia to nie zawsze „środkowa liczba” — to suma dzielona przez ilość. Środkowa to mediana.",
        "Середнє — не завжди «середнє число» — це сума, поділена на кількість. Середнє за порядком — медіана."),
    43: ("Przy odejmowaniu pisemnym nie zapomnij o pożyczce — i sprawdź dodawaniem.",
        "При письмовому відніманні не забудь про позичку — і перевір додаванням."),
    45: ("NWD ≠ NWW: NWD jest dzielnikiem (mniejszy lub równy), NWW — wielokrotnością (większa lub równa).",
        "НСД ≠ НСК: НСД — дільник (менший або рівний), НСК — кратне (більше або рівне)."),
    46: ("„3/4 z 20” to nie „3/4 + 20”. Najpierw znajdź jedną część, potem pomnóż.",
        "«3/4 від 20» — не «3/4 + 20». Спочатку знайди одну частину, потім помнож."),
    49: ("Suma kątów w trójkącie to 180°, nie 360° (360° to kąt pełny / obrót).",
        "Сума кутів у трикутнику — 180°, не 360° (360° — повний кут / оберт)."),
    52: ("Po +20% i −20% nie wracasz do startu: 100→120→96.",
        "Після +20% і −20% не повертаєшся до старту: 100→120→96."),
    57: ("c to bok naprzeciw kąta prostego — nie byle który bok trójkąta!",
        "c — бік навпроти прямого кута, не аби-який бік трикутника!"),
    58: ("Przy BKB kąt musi leżeć między tymi dwoma bokami (kąt zawarty).",
        "При СКС кут має лежати між цими двома сторонами (уключений кут)."),
    61: ("Prawo na sobie ≠ zawsze prawo na obrazku — najpierw ustal punkt odniesienia.",
        "Право на собі ≠ завжди право на малюнку — спочатку з'ясуй точку відліку."),
}


# ——— Przykłady kart (brakujące w handbook_examples.LIFE) ———
MORE_LIFE = {
    (2, "Przykłady"): E(
        "Na zegarze z rzymskimi cyframi widzisz IV (4) albo IX (9) — to skróty zapisu.",
        "На годиннику з римськими цифрами бачиш IV (4) або IX (9) — це скорочення запису.",
    ),
    (2, "Ograniczenia"): E(
        "Nie napiszesz „IL” na 49. Reguła: I tylko przed V i X → 49 = XLIX.",
        "Не напишеш «IL» на 49. Правило: I лише перед V і X → 49 = XLIX.",
    ),
    (2, "Większe przykłady"): E(
        "Rok na filmie MMXXIV = 2024. Czytasz od lewej: dwa M, dwa X, I, V.",
        "Рік на фільмі MMXXIV = 2024. Читаєш зліва: два M, два X, I, V.",
    ),
    (2, "Zamiana na arabskie"): E(
        "Na pomniku LXIV: L=50, X=10, IV=4 → razem 64.",
        "На пам'ятнику LXIV: L=50, X=10, IV=4 → разом 64.",
    ),
    (3, "dodatnie, ujemne, zero"): E(
        "Na termometrze +5°C jest powyżej zera, −3°C — poniżej. Zero to środek skali.",
        "На термометрі +5°C вище нуля, −3°C — нижче. Нуль — середина шкали.",
    ),
    (3, "porównywanie"): E(
        "−7°C jest zimniej niż −2°C, bo −7 leży bardziej w lewo: −7 < −2.",
        "−7°C холодніше за −2°C, бо −7 лежить лівіше: −7 < −2.",
    ),
    (3, "dodawanie"): E(
        "Było −3°C, ociepliło się o 5°: (−3)+(+5)=2. Teraz jest 2°C.",
        "Було −3°C, потепліло на 5°: (−3)+(+5)=2. Тепер 2°C.",
    ),
    (3, "odejmowanie"): E(
        "Odejmowanie zamieniasz na dodawanie przeciwnej: 4−(−1)=4+1=5.",
        "Віднімання замінюєш на додавання протилежного: 4−(−1)=4+1=5.",
    ),
    (3, "liczba przeciwna"): E(
        "Jesteś na piętrze +3; „odbite” względem zera to −3 — ta sama odległość.",
        "Ти на поверсі +3; «відбитий» відносно нуля — −3, та сама відстань.",
    ),
    (7, "potęgi"): E(
        "W 2+3² najpierw 3²=9, potem 2+9=11. Nie liczysz (2+3)²!",
        "У 2+3² спочатку 3²=9, потім 2+9=11. Не рахуй (2+3)²!",
    ),
    (7, "+ i −"): E(
        "10 punktów, −3, +2: 10−3+2=9. Na tym poziomie liczysz od lewej.",
        "10 очок, −3, +2: 10−3+2=9. На цьому рівні рахуєш зліва.",
    ),
    (7, "ten sam poziom"): E(
        "24:6×2 — × i : są równe, więc od lewej: 4×2=8.",
        "24:6×2 — × і : рівні, тож зліва: 4×2=8.",
    ),
    (7, "przykład"): E(
        "2+3×(8−2²): nawias → potęga → × → + → wynik 14.",
        "2+3×(8−2²): дужки → степінь → × → + → результат 14.",
    ),
    (8, "przez 3"): E(
        "Numer 123: 1+2+3=6, 6÷3=2 → 123 dzieli się przez 3.",
        "Номер 123: 1+2+3=6, 6÷3=2 → 123 ділиться на 3.",
    ),
    (8, "przez 4"): E(
        "Rok 2024: ostatnie dwie cyfry 24, 24÷4=6 → dzieli się przez 4.",
        "Рік 2024: останні дві цифри 24, 24÷4=6 → ділиться на 4.",
    ),
    (8, "przez 9"): E(
        "81: 8+1=9, 9÷9=1 → 81 dzieli się przez 9.",
        "81: 8+1=9, 9÷9=1 → 81 ділиться на 9.",
    ),
    (8, "przez 10"): E(
        "Bilety po 10 zł: liczba musi kończyć się zerem (20, 70, 150).",
        "Квитки по 10 zł: число має закінчуватися нулем (20, 70, 150).",
    ),
    (8, "dzielnik / wielokrotność"): E(
        "12 cukierków możesz rozdać po 1,2,3,4,6,12 — to dzielniki. 24,36… to wielokrotności 12.",
        "12 цукерок можна роздати по 1,2,3,4,6,12 — дільники. 24,36… — кратні 12.",
    ),
    (9, "właściwy / niewłaściwy"): E(
        "2 z 5 kawałków pizzy (2/5) to mniej niż całość. 7/4 to już więcej niż jedna pizza.",
        "2 з 5 шматків піци (2/5) — менше за ціле. 7/4 — уже більше за одну піцу.",
    ),
    (9, "liczba mieszana"): E(
        "1 całe jabłko i 3/4: piszesz 1 3/4 albo 7/4.",
        "1 ціле яблуко і 3/4: пишеш 1 3/4 або 7/4.",
    ),
    (9, "ułamki równe"): E(
        "Pół tortu = 1/2 = 2/4 = 3/6 — różne zapisy, ta sama część.",
        "Пів торта = 1/2 = 2/4 = 3/6 — різні записи, та сама частина.",
    ),
    (10, "ułamek nieskracalny"): E(
        "12/18 dzielisz przez 6 → 2/3. Dalej się nie da — nieskracalny.",
        "12/18 ділиш на 6 → 2/3. Далі не можна — нескоротний.",
    ),
    (10, "wspólny mianownik"): E(
        "Dodajesz 1/2 i 1/3 pizzy. Wspólny mianownik 6: 3/6+2/6=5/6.",
        "Додаєш 1/2 і 1/3 піци. Спільний знаменник 6: 3/6+2/6=5/6.",
    ),
    (10, "porównywanie"): E(
        "2/5 tortu < 3/5. Przy tym samym mianowniku większy licznik = więcej.",
        "2/5 торта < 3/5. При тому самому знаменнику більший чисельник = більше.",
    ),
    (10, "ułamek = dzielenie"): E(
        "3 batony na 4 dzieci: każdy dostaje 3:4 = 3/4 batona.",
        "3 батончики на 4 дітей: кожен отримує 3:4 = 3/4 батончика.",
    ),
    (11, "miejsca po przecinku"): E(
        "Cena 2,375 zł: 3 — dziesiąte, 7 — setne, 5 — tysięczne.",
        "Ціна 2,375 zł: 3 — десяті, 7 — соті, 5 — тисячні.",
    ),
    (11, "równoważność"): E(
        "0,5 zł = 0,50 zł = 0,500 zł — ta sama kwota, zera na końcu nie zmieniają wartości.",
        "0,5 zł = 0,50 zł = 0,500 zł — та сама сума, нулі в кінці не змінюють значення.",
    ),
    (11, "zamiana na zwykły"): E(
        "Rabat 0,25 = 25/100 = 1/4 — ćwiartka ceny.",
        "Знижка 0,25 = 25/100 = 1/4 — чверть ціни.",
    ),
    (11, "porównywanie"): E(
        "1,25 i 1,3: dopisz zero → 1,25 < 1,30.",
        "1,25 і 1,3: допиши нуль → 1,25 < 1,30.",
    ),
    (11, "zaokrąglanie"): E(
        "π≈3,141… Na klasówce często wystarczy 3,14 (dwa miejsca po przecinku).",
        "π≈3,141… На контрольній часто досить 3,14 (два знаки після коми).",
    ),
    (12, "+/− ten sam mianownik"): E(
        "Zjadłaś 2/7 pizzy, kolega 3/7. Razem 5/7 — mianownik ten sam, dodajesz liczniki.",
        "З'їла 2/7 піци, друг 3/7. Разом 5/7 — знаменник той самий, додаєш чисельники.",
    ),
    (12, "różne mianowniki"): E(
        "Pół szklanki + 1/3 szklanki: wspólny mianownik 6 → 3/6+2/6=5/6.",
        "Пів склянки + 1/3 склянки: спільний знаменник 6 → 3/6+2/6=5/6.",
    ),
    (12, "mnożenie"): E(
        "Bierzemy 2/3 z 4/5 tabliczki czekolady: 2/3×4/5=8/15.",
        "Беремо 2/3 від 4/5 плитки шоколаду: 2/3×4/5=8/15.",
    ),
    (12, "odwrotność"): E(
        "Odwrotność 3/4 to 4/3 — licznik i mianownik zamieniają się miejscami.",
        "Обернений до 3/4 — 4/3: чисельник і знаменник міняються місцями.",
    ),
    (12, "skracanie przed ×"): E(
        "2/9×3/4: skróć 3 i 9 → 2/3×1/4=2/12=1/6. Mniej rachunku!",
        "2/9×3/4: скороти 3 і 9 → 2/3×1/4=2/12=1/6. Менше рахунку!",
    ),
    (13, "podstawa i wykładnik"): E(
        "W 2⁴ liczba 2 to podstawa (co mnożysz), 4 — wykładnik (ile razy).",
        "У 2⁴ число 2 — основа (що множиш), 4 — показник (скільки разів).",
    ),
    (13, "kwadrat i sześcian"): E(
        "Kwadrat pokoju 5×5: 5²=25 m². Kostka 2×2×2: 2³=8 cm³.",
        "Квадрат кімнати 5×5: 5²=25 м². Кубик 2×2×2: 2³=8 см³.",
    ),
    (13, "0, 1, 10"): E(
        "a¹=a, a⁰=1 (gdy a≠0). 10³=1000 — jedynka i trzy zera.",
        "a¹=a, a⁰=1 (коли a≠0). 10³=1000 — одиниця і три нулі.",
    ),
    (13, "mnożenie potęg"): E(
        "2³·2² = 2⁵ — przy tej samej podstawie dodajesz wykładniki.",
        "2³·2² = 2⁵ — при тій самій основі додаєш показники.",
    ),
    (13, "dzielenie potęg"): E(
        "2⁵:2² = 2³ — przy tej samej podstawie odejmujesz wykładniki.",
        "2⁵:2² = 2³ — при тій самій основі віднімаєш показники.",
    ),
    (14, "zapis"): E(
        "Znak √ mówi: „znajdź liczbę, która podniesiona do kwadratu daje to, co pod spodem”.",
        "Знак √ каже: «знайди число, яке в квадраті дає те, що під ним».",
    ),
    (14, "przykłady"): E(
        "√16=4, bo 4·4=16. √25=5 — znasz z tabliczki kwadratów.",
        "√16=4, бо 4·4=16. √25=5 — знаєш з таблиці квадратів.",
    ),
    (14, "związek z potęgą"): E(
        "(√9)²=9 — pierwiastek i kwadrat „odwracają się”.",
        "(√9)²=9 — корінь і квадрат «взаємно обернені».",
    ),
    (14, "kwadraty doskonałe"): E(
        "1,4,9,16,25… to kwadraty 1²,2²,3²… — z nich pierwiastek wychodzi „ładnie”.",
        "1,4,9,16,25… — квадрати 1²,2²,3²… — з них корінь виходить «гарно».",
    ),
    (14, "szacowanie"): E(
        "√50: wiesz, że 7²=49, więc √50≈7,1 — prawie 7.",
        "√50: знаєш, що 7²=49, тож √50≈7,1 — майже 7.",
    ),
    (15, "zwiększenie o p%"): E(
        "Cena 100 zł rośnie o 20%: 100·(1+0,20)=120 zł.",
        "Ціна 100 zł зростає на 20%: 100·(1+0,20)=120 zł.",
    ),
    (15, "zmniejszenie o p%"): E(
        "Kurtka 200 zł, −25%: 200·(1−0,25)=150 zł. To nie „odjąć 25”!",
        "Куртка 200 zł, −25%: 200·(1−0,25)=150 zł. Це не «відняти 25»!",
    ),
    (15, "zamiany"): E(
        "25% = 25/100 = 1/4 = 0,25 — trzy zapisy tej samej części.",
        "25% = 25/100 = 1/4 = 0,25 — три записи тієї самої частини.",
    ),
    (15, "przykłady"): E(
        "20% z 50 zł = 10 zł. 15% z 200 punktów = 30 punktów.",
        "20% від 50 zł = 10 zł. 15% від 200 балів = 30 балів.",
    ),
    (16, "proporcjonalność prosta"): E(
        "2 kg jabłek za 10 zł → 4 kg za 20 zł. Podwój masa → podwój cena.",
        "2 кг яблук за 10 zł → 4 кг за 20 zł. Подвійна маса → подвійна ціна.",
    ),
    (16, "współczynnik"): E(
        "Cena = 5·masa. Współczynnik k=5 zł/kg — „ile za jedną jednostkę”.",
        "Ціна = 5·маса. Коефіцієнт k=5 zł/кг — «скільки за одну одиницю».",
    ),
    (16, "wykres"): E(
        "Na wykresie proporcji prostej linia idzie przez punkt (0,0).",
        "На графіку прямої пропорційності лінія йде через точку (0,0).",
    ),
    (16, "tabela wartości"): E(
        "x: 1,2,3 godziny → y: 2,4,6 km (przy v=2 km/h). Widać stały mnożnik.",
        "x: 1,2,3 години → y: 2,4,6 км (при v=2 км/год). Видно сталий множник.",
    ),
    (16, "proporcja"): E(
        "3/5 = 6/10. Sprawdzasz: 3·10 = 5·6. Iloczyn skrajnych = środkowych.",
        "3/5 = 6/10. Перевіряєш: 3·10 = 5·6. Добуток крайніх = середніх.",
    ),
    (17, "wyrażenie algebraiczne"): E(
        "„3x + 5” to przepis z literą: x jeszcze nie znasz, ale zapis już masz.",
        "«3x + 5» — рецепт із літерою: x ще не знаєш, але запис уже є.",
    ),
    (17, "elementy"): E(
        "W 3x+5y−8 są liczby, litery i znaki działań — jak klocki wyrażenia.",
        "У 3x+5y−8 є числа, літери й знаки дій — як кубики виразу.",
    ),
    (17, "wartość liczbowa"): E(
        "Gdy x=2, to 3x+1=3·2+1=7. Podstawiasz i liczysz.",
        "Коли x=2, то 3x+1=3·2+1=7. Підставляєш і рахуєш.",
    ),
    (17, "zapis skrócony"): E(
        "3x znaczy x+x+x. xy znaczy x·y. Tak skracamy zapis w zeszycie.",
        "3x означає x+x+x. xy означає x·y. Так скорочуємо запис у зошиті.",
    ),
    (17, "kolejność"): E(
        "W wyrażeniu z literami kolejność działań ta sama: nawiasy, potęgi, ×:, +−.",
        "У виразі з літерами порядок дій той самий: дужки, степені, ×:, +−.",
    ),
    (18, "jednomian"): E(
        "5x² albo −3ab — jeden „blok” liczb i liter. To jednomian.",
        "5x² або −3ab — один «блок» чисел і літер. Це одночлен.",
    ),
    (18, "suma algebraiczna"): E(
        "3x − 2y + 5 — kilka jednomianów połączonych + i −.",
        "3x − 2y + 5 — кілька одночленів, з'єднаних + і −.",
    ),
    (18, "wyrazy podobne"): E(
        "3x i −5x mają tę samą część literową — możesz je połączyć: −2x.",
        "3x і −5x мають ту саму літерну частину — можна об'єднати: −2x.",
    ),
    (18, "współczynnik"): E(
        "W 7a²b liczba 7 to współczynnik — „ile razy” część literowa.",
        "У 7a²b число 7 — коефіцієнт: «скільки разів» літерна частина.",
    ),
    (18, "przykład"): E(
        "2a+5−a+3: łączysz 2a−a oraz 5+3 → a+8.",
        "2a+5−a+3: об'єднуєш 2a−a та 5+3 → a+8.",
    ),
    (19, "niewiadoma"): E(
        "W zagadce „myślałem liczbę…” ta liczba to niewiadoma — zwykle x.",
        "У загадці «думав число…» це число — невідоме, зазвичай x.",
    ),
    (19, "rozwiązanie"): E(
        "Równanie x+5=12. Rozwiązanie: x=7 — to liczba, która pasuje.",
        "Рівняння x+5=12. Розв'язок: x=7 — число, яке підходить.",
    ),
    (19, "przenoszenie"): E(
        "x+5=12 → x=12−5. Przenosisz +5 na prawą stronę jako −5.",
        "x+5=12 → x=12−5. Переносиш +5 на правий бік як −5.",
    ),
    (19, "sprawdzenie"): E(
        "Wyszło x=7. Sprawdzasz: 7+5=12 — zgadza się ✓.",
        "Вийшло x=7. Перевіряєш: 7+5=12 — сходиться ✓.",
    ),
    (20, "jednostki długości"): E(
        "Od mm do km: każdy krok ×10 (mm→cm→dm→m…). Jak drabinka.",
        "Від мм до км: кожен крок ×10 (мм→см→дм→м…). Як драбинка.",
    ),
    (20, "porównywanie"): E(
        "1,2 m i 95 cm: zamień na cm → 120 cm > 95 cm.",
        "1,2 м і 95 см: переведи в см → 120 см > 95 см.",
    ),
    (20, "obwód a długość"): E(
        "Obwód ramki = suma długości wszystkich boków — „dookoła”.",
        "Периметр рамки = сума довжин усіх сторін — «довкола».",
    ),
    (20, "przykład"): E(
        "Wzrost 2,5 m = 250 cm = 2500 mm. Przecinek „skacze” przy zamianie.",
        "Зріст 2,5 м = 250 см = 2500 мм. Кома «стрибає» при перетворенні.",
    ),
    (21, "jednostki masy"): E(
        "Zakupy: 1 kg mąki = 1000 g. Mg — bardzo małe; tona — bardzo duże.",
        "Покупки: 1 кг борошна = 1000 г. Мг — дуже мале; тонна — дуже велике.",
    ),
    (21, "porównywanie"): E(
        "1 kg > 800 g, bo 1 kg = 1000 g.",
        "1 кг > 800 г, бо 1 кг = 1000 г.",
    ),
    (21, "ważenie"): E(
        "Na wadze w sklepie kładziesz jabłka — odczytujesz masę w kg lub g.",
        "На вагах у магазині кладеш яблука — зчитуєш масу в кг або г.",
    ),
    (21, "przykłady"): E(
        "250 g cukru = 0,25 kg. 2,5 kg mąki = 2500 g.",
        "250 г цукру = 0,25 кг. 2,5 кг борошна = 2500 г.",
    ),
    (21, "w życiu"): E(
        "Przepis, paczka z poczty, zakupy na wagę — wszędzie masa.",
        "Рецепт, посилка з пошти, покупки на вагу — скрізь маса.",
    ),
    (22, "objętość"): E(
        "Sok w butelce (litry) albo powietrze w pudełku (cm³) — to objętość.",
        "Сік у пляшці (літри) або повітря в коробці (см³) — це об'єм.",
    ),
    (22, "mililitr"): E(
        "Łyżeczka syropu ~5 ml. 1 ml = 1 cm³ — ta sama „ilość miejsca”.",
        "Чайна ложка сиропу ~5 мл. 1 мл = 1 см³ — той самий «об'єм місця».",
    ),
    (22, "przeliczanie"): E(
        "Duża butelka 2,5 l = 2500 ml. Mnożysz przez 1000.",
        "Велика пляшка 2,5 л = 2500 мл. Множиш на 1000.",
    ),
    (22, "objętość bryły"): E(
        "Pudełko a×b×c: V=a·b·c. Mnożysz trzy wymiary.",
        "Коробка a×b×c: V=a·b·c. Множиш три виміри.",
    ),
    (22, "przykład"): E(
        "Pudełko 2×3×4 cm → V=24 cm³ — tyle „miejsce w środku”.",
        "Коробка 2×3×4 см → V=24 см³ — стільки «місця всередині».",
    ),
    (23, "jednostki czasu"): E(
        "1 godzina = 60 minut, 1 minuta = 60 sekund — zapamiętaj jak tabliczkę.",
        "1 година = 60 хвилин, 1 хвилина = 60 секунд — запам'ятай як таблицю.",
    ),
    (23, "zegar"): E(
        "W szkole często 24 h (14:00), w domu bywa 12 h (2 po południu).",
        "У школі часто 24 год (14:00), вдома буває 12 год (2 по полудні).",
    ),
    (23, "doba"): E(
        "Od północy do północy = 1 doba = 24 godziny — potem dzień zaczyna się od nowa.",
        "Від півночі до півночі = 1 доба = 24 години — потім день починається знову.",
    ),
    (23, "zamiana"): E(
        "2,5 h = 2 h 30 min = 150 min. Pół godziny = 30 minut.",
        "2,5 год = 2 год 30 хв = 150 хв. Пів години = 30 хвилин.",
    ),
    (23, "przykład"): E(
        "Film od 8:45 do 10:10 trwa 1 h 25 min.",
        "Фільм з 8:45 до 10:10 триває 1 год 25 хв.",
    ),
    (24, "jednostki kalendarzowe"): E(
        "Dzień, tydzień, miesiąc, rok — paczki czasu w kalendarzu.",
        "День, тиждень, місяць, рік — пакунки часу в календарі.",
    ),
    (24, "rok przestępny"): E(
        "Co 4 lata luty ma 29 dni — rok przestępny (np. 2024).",
        "Кожні 4 роки лютий має 29 днів — високосний рік (напр. 2024).",
    ),
    (24, "miesiące"): E(
        "Zapamiętaj: 30 dni mają kwiecień, czerwiec, wrzesień, listopad; luty — osobno.",
        "Запам'ятай: 30 днів мають квітень, червень, вересень, листопад; лютий — окремо.",
    ),
    (24, "kolejność dni"): E(
        "pn → wt → śr → cz → pt → so → nd — i znowu poniedziałek.",
        "пн → вт → ср → чт → пт → сб → нд — і знову понеділок.",
    ),
    (24, "przykład"): E(
        "Od 28 lutego do 3 marca: w roku zwykłym to 3 dni (1,2,3 marca).",
        "Від 28 лютого до 3 березня: у звичайному році це 3 дні (1,2,3 березня).",
    ),
    (24, "data"): E(
        "Twoje urodziny zapisujesz: dzień.miesiąc.rok — np. 18.07.2015.",
        "День народження пишеш: день.місяць.рік — напр. 18.07.2015.",
    ),
    (25, "stopień Celsjusza"): E(
        "W Polsce temperaturę podajemy w °C — stopnie Celsjusza.",
        "У Польщі температуру подаємо в °C — градуси Цельсія.",
    ),
    (25, "termometr"): E(
        "Na termometrze widać skalę ze znakiem + i − — powyżej i poniżej zera.",
        "На термометрі видно шкалу зі знаком + і − — вище й нижче нуля.",
    ),
    (25, "powyżej / poniżej zera"): E(
        "+5°C to powyżej zera (cieplej), −8°C — poniżej (mróz).",
        "+5°C — вище нуля (тепліше), −8°C — нижче (мороз).",
    ),
    (25, "porównywanie"): E(
        "−3°C < 2°C — mróz jest „mniejszą” temperaturą niż plus.",
        "−3°C < 2°C — мороз «менша» температура, ніж плюс.",
    ),
    (25, "w życiu"): E(
        "Pogoda, piekarnik, temperatura ciała — wszędzie °C.",
        "Погода, духовка, температура тіла — скрізь °C.",
    ),
    (26, "zapis"): E(
        "12,50 zł — złote przed przecinkiem, grosze po. Jak ułamek dziesiętny.",
        "12,50 zł — злоті перед комою, гроші після. Як десятковий дріб.",
    ),
    (26, "dodawanie / odejmowanie"): E(
        "Bułka 3,40 zł + sok 1,75 zł = 5,15 zł. Przecinek pod przecinkiem!",
        "Булка 3,40 zł + сік 1,75 zł = 5,15 zł. Кома під комою!",
    ),
    (26, "porównywanie cen"): E(
        "Porównuj cenę za 100 g albo za 1 kg — wtedy widać, co naprawdę tańsze.",
        "Порівнюй ціну за 100 г або за 1 кг — тоді видно, що справді дешевше.",
    ),
    (26, "budżet"): E(
        "Dostałaś 20 zł, wydałaś 12 zł → zostaje 8 zł. Budżet = przychód − wydatek.",
        "Отримала 20 zł, витратила 12 zł → лишається 8 zł. Бюджет = дохід − витрата.",
    ),
    (27, "jednostki"): E(
        "Samochód: km/h. Bieg: czasem m/s. To „ile drogi na jednostkę czasu”.",
        "Авто: км/год. Біг: інколи м/с. Це «скільки шляху на одиницю часу».",
    ),
    (27, "droga i czas"): E(
        "Jedziesz 60 km/h przez 2 h → droga 120 km. s = v·t.",
        "Їдеш 60 км/год протягом 2 год → шлях 120 км. s = v·t.",
    ),
    (27, "obliczanie odległości"): E(
        "Na mapie 3 cm, skala 1:100 000 → w terenie 3 km.",
        "На мапі 3 см, масштаб 1:100 000 → на місцевості 3 км.",
    ),
    (27, "przykład v"): E(
        "120 km w 2 godziny → v = 120:2 = 60 km/h.",
        "120 км за 2 години → v = 120:2 = 60 км/год.",
    ),
    (28, "punkt"): E(
        "Kropka na kartce — punkt A. Nie ma długości, to „miejsce”.",
        "Крапка на аркуші — точка A. Немає довжини, це «місце».",
    ),
    (28, "prosta"): E(
        "Linia w obie strony bez końca — prosta. Ołówek tylko ją „pokazuje”.",
        "Лінія в обидва боки без кінця — пряма. Олівець лише її «показує».",
    ),
    (28, "półprosta"): E(
        "Półprosta na rysunku: start w punkcie i strzałka w jedną stronę — jak światło latarki.",
        "Півпряма на малюнку: старт у точці і стрілка в один бік — як світло ліхтарика.",
    ),
    (28, "łamana"): E(
        "Droga z kilku odcinków połączonych końcami — łamana (jak ścieżka zygzakiem).",
        "Шлях із кількох відрізків, з'єднаних кінцями — ламана (як стежка зигзагом).",
    ),
    (28, "wielokąt"): E(
        "Trójkąt, kwadrat, pięciokąt — figury zamknięte z odcinków. To wielokąty.",
        "Трикутник, квадрат, п'ятикутник — замкнені фігури з відрізків. Це многокутники.",
    ),
    (29, "rodzaje trójkątów"): E(
        "Znak „ustąp” to trójkąt. Może być równoboczny, równoramienny albo różnoboczny.",
        "Знак «поступися» — трикутник. Може бути рівносторонній, рівнобедрений або різносторонній.",
    ),
    (29, "prostokąt"): E(
        "Drzwi, zeszyt, telefon — zwykle prostokąt: kąty proste, boki parami równe.",
        "Двері, зошит, телефон — зазвичай прямокутник: прямі кути, сторони попарно рівні.",
    ),
    (29, "romb / równoległobok"): E(
        "Romb jak „pochylony kwadrat”; równoległobok — przeciwległe boki równoległe.",
        "Ромб як «нахилений квадрат»; паралелограм — протилежні сторони паралельні.",
    ),
    (29, "trapez"): E(
        "Dach albo torba: jedna para boków równoległych — trapez.",
        "Дах або сумка: одна пара сторін паралельна — трапеція.",
    ),
    (30, "środek"): E(
        "Środek talerza — punkt O. Od niego jednakowo daleko do brzegu.",
        "Центр тарілки — точка O. Від неї однаково далеко до краю.",
    ),
    (30, "promień"): E(
        "Od środka koła roweru do obręczy — promień r.",
        "Від центра колеса велосипеда до обода — радіус r.",
    ),
    (30, "średnica"): E(
        "Średnica przechodzi przez środek i łączy dwa punkty okręgu: d=2r.",
        "Діаметр проходить через центр і з'єднує дві точки кола: d=2r.",
    ),
    (30, "cięciwa"): E(
        "Odcinek między dwoma punktami na okręgu (niekoniecznie przez środek) — cięciwa.",
        "Відрізок між двома точками на колі (не обов'язково через центр) — хорда.",
    ),
    (31, "liczba π"): E(
        "π≈3,14 — stała, która łączy obwód z średnicą: C=π·d.",
        "π≈3,14 — стала, що зв'язує обвід із діаметром: C=π·d.",
    ),
    (31, "przykład C"): E(
        "Okrągły dywan r=5 → C≈2·3,14·5=31,4 (jednostki długości).",
        "Круглий килим r=5 → C≈2·3,14·5=31,4 (одиниці довжини).",
    ),
    (31, "przykład P"): E(
        "Pizza r=5 → pole ≈3,14·25=78,5 — „ile ciasta w środku”.",
        "Піца r=5 → площа ≈3,14·25=78,5 — «скільки тіста всередині».",
    ),
    (31, "zależność"): E(
        "Gdy promień ×2, obwód ×2, ale pole ×4 — pole rośnie szybciej.",
        "Коли радіус ×2, довжина ×2, але площа ×4 — площа росте швидше.",
    ),
    (32, "kąt"): E(
        "Otwarte nożyczki tworzą kąt ∠AOB — dwa ramiona ze wspólnym początkiem.",
        "Відкриті ножиці утворюють кут ∠AOB — дві сторони зі спільним початком.",
    ),
    (32, "wierzchołek"): E(
        "Punkt, w którym stykają się ramiona kąta — wierzchołek (u nożyczek: śrobek).",
        "Точка, де стикаються сторони кута — вершина (у ножиць: серединка).",
    ),
    (32, "ramiona / strony"): E(
        "Dwie półproste wychodzące z wierzchołka — to ramiona kąta.",
        "Дві півпрямі з вершини — це сторони кута.",
    ),
    (32, "miara kąta"): E(
        "Kąt mierzymy w stopniach (°). Półobrót = 180°, pełny obrót = 360°.",
        "Кут міряємо в градусах (°). Півоберт = 180°, повний оберт = 360°.",
    ),
    (32, "kątomierz"): E(
        "Kątomierz to półkole ze skalą — przykładujesz i odczytujesz stopnie.",
        "Кутомір — півколо зі шкалою: прикладаєш і зчитуєш градуси.",
    ),
    (32, "półobrót / obrót"): E(
        "Odwróć się o pół obrotu — 180°. Pełny obrót wokół siebie — 360°.",
        "Повернись на півоберта — 180°. Повний оберт навколо себе — 360°.",
    ),
    (33, "kąt zerowy"): E(
        "Ramiona „sklejone” — 0°. Jak zamknięte nożyczki.",
        "Сторони «склеєні» — 0°. Як закриті ножиці.",
    ),
    (33, "kąt prosty"): E(
        "Róg zeszytu, ściana z podłogą — zwykle 90°. Znaczek □.",
        "Кут зошита, стіна з підлогою — зазвичай 90°. Значок □.",
    ),
    (33, "kąt rozwarty"): E(
        "Większy niż prosty, mniejszy niż półpełny: np. 120° — rozwarty.",
        "Більший за прямий, менший за розгорнутий: напр. 120° — тупий.",
    ),
    (33, "kąt półpełny"): E(
        "Ramiona w jednej linii — 180°. Jak otwarta książka na płasko.",
        "Сторони на одній лінії — 180°. Як розкрита книжка плазом.",
    ),
    (33, "kąt pełny"): E(
        "Pełny obrót — 360°. Wracasz do tego samego kierunku.",
        "Повний оберт — 360°. Повертаєшся в той самий напрям.",
    ),
    (34, "sieczna"): E(
        "Prosta przecina dwie równoległe tory — to sieczna.",
        "Пряма перетинає дві паралельні колії — це січна.",
    ),
    (34, "kąty odpowiadające"): E(
        "Przy równoległych kąty „na tych samych miejscach” przy siecznej są równe.",
        "При паралельних кути «на тих самих місцях» біля січної рівні.",
    ),
    (34, "naprzemianległe"): E(
        "Kąty na przemian po obu stronach siecznej — przy ∥ też równe.",
        "Кути навхрест по обидва боки січної — при ∥ теж рівні.",
    ),
    (34, "przyległe"): E(
        "Dwa kąty tworzące razem prostą: suma 180° — przyległe.",
        "Два кути, що разом утворюють пряму: сума 180° — суміжні.",
    ),
    (34, "wierzchołkowe"): E(
        "Kąty naprzeciwko siebie przy przecięciu prostych — równe (wierzchołkowe).",
        "Кути навпроти один одного при перетині прямих — рівні (вертикальні).",
    ),
    (35, "pole"): E(
        "Ile kartki „w środku” ramki? To pole — w cm² lub m².",
        "Скільки аркуша «всередині» рамки? Це площа — в см² або м².",
    ),
    (35, "prostokąt"): E(
        "Pokój 4 m na 5 m: pole =4·5=20 m², obwód =2·(4+5)=18 m.",
        "Кімната 4 м на 5 м: площа =4·5=20 м², периметр =2·(4+5)=18 м.",
    ),
    (35, "kwadrat"): E(
        "Kwadratowa chustka bok 3: pole 3²=9, obwód 4·3=12.",
        "Квадратна хустка бік 3: площа 3²=9, периметр 4·3=12.",
    ),
    (35, "równoległobok"): E(
        "Pole = podstawa × wysokość (nie bok po skosie!). P=a·h.",
        "Площа = основа × висота (не бік навскіс!). P=a·h.",
    ),
    (36, "bryła"): E(
        "Pudełko ma długość, szerokość i wysokość — to bryła (3D).",
        "Коробка має довжину, ширину й висоту — це тіло (3D).",
    ),
    (36, "prostopadłościan"): E(
        "Pudełko po butach: V=a·b·c — mnożysz trzy wymiary.",
        "Коробка від взуття: V=a·b·c — множиш три виміри.",
    ),
    (36, "ostrosłup"): E(
        "Namiot albo piramida: podstawa i ściany zbiegające się w wierzchołku.",
        "Намет або піраміда: основа й грані, що сходяться у вершині.",
    ),
    (36, "walec / stożek / kula"): E(
        "Puszka (walec), rożek lodów (stożek), piłka (kula) — okrągłe bryły.",
        "Банка (циліндр), ріжок морозива (конус), м'яч (куля) — круглі тіла.",
    ),
    (36, "objętość sześcianu"): E(
        "Kostka do gry bok a: V=a³. Wszystkie krawędzie równe.",
        "Гральний кубик ребро a: V=a³. Усі ребра рівні.",
    ),
    (37, "symetria"): E(
        "Motyl: lewe skrzydło jak prawe w lustrze — to symetria.",
        "Метелик: ліве крило як праве в дзеркалі — це симетрія.",
    ),
    (37, "środek symetrii"): E(
        "Litera O: obrót o 180° wokół środka wygląda tak samo.",
        "Літера O: поворот на 180° навколо центра виглядає так само.",
    ),
    (37, "przykłady"): E(
        "Kwadrat, koło, litery H, O, X — mają osie lub środek symetrii.",
        "Квадрат, коло, літери H, O, X — мають осі або центр симетрії.",
    ),
    (37, "rysowanie"): E(
        "Odbijasz punkt: prostopadle do osi, w tej samej odległości po drugiej stronie.",
        "Відбиваєш точку: перпендикулярно до осі, на тій самій відстані з іншого боку.",
    ),
    (37, "w przyrodzie"): E(
        "Liść, płatki kwiatu, płatki śniegu — natura lubi symetrię.",
        "Листок, пелюстки квітки, сніжинки — природа любить симетрію.",
    ),
    (38, "układ współrzędnych"): E(
        "Mapa skarbu w kratkę: osie X (w prawo) i Y (w górę) — adres punktu.",
        "Мапа скарбу в клітинку: осі X (вправо) і Y (вгору) — адреса точки.",
    ),
    (38, "oś X"): E(
        "Oś X leży poziomo — jak linia horyzontu na rysunku.",
        "Вісь X лежить горизонтально — як лінія горизонту на малюнку.",
    ),
    (38, "oś Y"): E(
        "Oś Y stoi pionowo — w górę dodatnie wartości.",
        "Вісь Y стоїть вертикально — вгору додатні значення.",
    ),
    (38, "ćwiartki"): E(
        "Cztery „pokoje” układu: I (++, prawo-góra), II, III, IV.",
        "Чотири «кімнати» системи: I (++, право-вгору), II, III, IV.",
    ),
    (38, "początek układu"): E(
        "Punkt O(0,0) — skrzyżowanie osi. Stąd zaczynasz odliczanie.",
        "Точка O(0,0) — перетин осей. Звідси починаєш відлік.",
    ),
    (39, "statystyka"): E(
        "Ankieta w klasie → liczby → wniosek: „najwięcej lubi niebieski”. To statystyka.",
        "Опитування в класі → числа → висновок: «найбільше люблять синій». Це статистика.",
    ),
    (39, "dane"): E(
        "Wyniki pomiarów wzrostu albo odpowiedzi z ankiety — to dane.",
        "Результати вимірювання зросту або відповіді з опитування — це дані.",
    ),
    (39, "etapy"): E(
        "Zbierz → uporządkuj → przedstaw na wykresie → wyciągnij wniosek.",
        "Збери → впорядкуй → покажи на діаграмі → зроби висновок.",
    ),
    (39, "tabela"): E(
        "Kolumna „smak”, kolumna „ile osób” — dane w tabeli czytelniej niż w chaosie.",
        "Стовпчик «смак», стовпчик «скільки осіб» — дані в таблиці читабельніші.",
    ),
    (39, "wykres kołowy"): E(
        "Całe koło = 100% klasy. Wycinek pokazuje udział ulubionego koloru.",
        "Ціле коло = 100% класу. Сектор показує частку улюбленого кольору.",
    ),
    (40, "mediana"): E(
        "Oceny 2,5,5,8: po uporządkowaniu środek to mediana (tu średnia z 5 i 5).",
        "Оцінки 2,5,5,8: після впорядкування середина — медіана (тут середнє з 5 і 5).",
    ),
    (40, "przykład średniej"): E(
        "Punkty 2,5,5,8: średnia (2+5+5+8):4 = 5.",
        "Бали 2,5,5,8: середнє (2+5+5+8):4 = 5.",
    ),
    (40, "przykład mediany"): E(
        "Przy parzystej liczbie: środkowe 5 i 5 → mediana 5.",
        "При парній кількості: середні 5 і 5 → медіана 5.",
    ),
    (40, "przykład mody"): E(
        "W 2,5,5,8 najczęściej pada 5 — to moda (wartość modalna).",
        "У 2,5,5,8 найчастіше трапляється 5 — це мода.",
    ),
    (41, "kombinatoryka"): E(
        "Ile strojów z 3 koszulek i 2 spodni? Liczysz sposoby — kombinatoryka.",
        "Скільки образів із 3 футболок і 2 штанів? Рахуєш способи — комбінаторика.",
    ),
    (41, "zasada dodawania"): E(
        "Albo idziesz do kina (2 filmy), albo na basen (1 tor) → 2+1=3 wybory.",
        "Або йдеш у кіно (2 фільми), або на басейн (1 доріжка) → 2+1=3 вибори.",
    ),
    (41, "permutacje"): E(
        "3 książki na półce: ile ustawień? 3·2·1 = 3! = 6.",
        "3 книжки на полиці: скільки розстановок? 3·2·1 = 3! = 6.",
    ),
    (41, "przykład P"): E(
        "Kostka: szansa na 6 to 1 na 6 → P=1/6.",
        "Кубик: шанс на 6 — 1 з 6 → P=1/6.",
    ),
    (42, "− minus / odejmowanie"): E(
        "9 − 4 = 5. Znak − to odejmowanie albo liczba ujemna (−3).",
        "9 − 4 = 5. Знак − — віднімання або від'ємне число (−3).",
    ),
    (42, "× · mnożenie"): E(
        "4 × 3 = 12. W Polsce też · (kropka) znaczy mnożenie.",
        "4 × 3 = 12. У Польщі також · (крапка) означає множення.",
    ),
    (42, ": / dzielenie"): E(
        "12 : 3 = 4. Ułamek 12/3 to też dzielenie.",
        "12 : 3 = 4. Дріб 12/3 — це теж ділення.",
    ),
    (42, "= &lt; &gt; ≤ ≥ ≠"): E(
        "5=5 równe; 3<7 mniejsze; ≠ znaczy „różne”. Znaki porównania.",
        "5=5 рівні; 3<7 менше; ≠ означає «різні». Знаки порівняння.",
    ),
    (42, "() [] √ ² % π ∠ ∥"): E(
        "Nawiasy, √, ², %, π, ∠, ∥ — znaki, które skracają zapis w zeszycie.",
        "Дужки, √, ², %, π, ∠, ∥ — знаки, що скорочують запис у зошиті.",
    ),
}


def apply_page_meta(page: dict) -> None:
    n = int(page.get("n") or 0)
    if n in PAGE_LIFE:
        page["life_pl"], page["life_ua"] = PAGE_LIFE[n]
    if n in PAGE_MISTAKE:
        page["mistake_pl"], page["mistake_ua"] = PAGE_MISTAKE[n]


def merge_life_into(life_dict: dict) -> None:
    """Dopisz MORE_LIFE do handbook_examples.LIFE (nie nadpisuj ręcznych)."""
    for k, v in MORE_LIFE.items():
        if k not in life_dict:
            life_dict[k] = v
