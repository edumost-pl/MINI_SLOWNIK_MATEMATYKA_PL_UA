# -*- coding: utf-8 -*-
"""
Pełne pogłębienie kart (klasy ~3–8 / cała SP):
język dydaktyczny — najpierw sens, potem zapis szkolny, potem przykład.
"""

def T(def_pl, def_ua, rule, rule_ua):
    return {"def_pl": def_pl, "def_ua": def_ua, "rule": rule, "rule_ua": rule_ua}


# (nr_strony, hasło_pl) → teksty
MORE_OVERRIDES = {
    # ——— 3 Liczby całkowite ———
    (3, "oś liczbowa"): T(
        "Oś liczbowa to prosta, na której liczby stoją w kolejności — jak linijka w obie strony od zera.",
        "Числова пряма — пряма, на якій числа стоять у порядку — як лінійка в обидва боки від нуля.",
        "Na lewo od 0 liczby ujemne, na prawo — dodatnie. Im dalej w lewo, tym mniejsza liczba.",
        "Ліворуч від 0 — від'ємні, праворуч — додатні. Що далі ліворуч — то менше число.",
    ),
    (3, "dodatnie, ujemne, zero"): T(
        "Dodatnie są większe od zera, ujemne — mniejsze. Zero jest „środkiem” — ani plus, ani minus.",
        "Додатні більші за нуль, від'ємні — менші. Нуль — «середина» — ні плюс, ні мінус.",
        "Zapisuj znak − przy ujemnych: −3. Zero zapisujemy bez znaku: 0.",
        "Записуй знак − біля від'ємних: −3. Нуль без знака: 0.",
    ),
    (3, "wartość bezwzględna"): T(
        "Wartość bezwzględna to odległość liczby od zera — zawsze nieujemna (jak długość kroku).",
        "Модуль — відстань числа від нуля — завжди невід'ємна (як довжина кроку).",
        "|5|=5 i |−5|=5. Znak „znika”, zostaje odległość.",
        "|5|=5 і |−5|=5. Знак «зникає», лишається відстань.",
    ),
    (3, "porównywanie"): T(
        "Porównujemy całkowite tak jak na osi: im bardziej w lewo, tym mniejsza.",
        "Порівнюємо цілі як на прямій: що лівіше — то менше.",
        "−7 < −2 < 0 < 4. Najpierw ustaw w głowie na osi, potem zapisz znak.",
        "−7 < −2 < 0 < 4. Спочатку постав у голові на прямій, потім запиши знак.",
    ),
    (3, "dodawanie"): T(
        "Dodawanie całkowitych uwzględnia znaki — jak kroki w lewo i w prawo na osi.",
        "Додавання цілих враховує знаки — як кроки вліво й вправо на прямій.",
        "(−3)+(+5)=2. Możesz myśleć: 3 kroki w lewo, 5 w prawo → netto 2 w prawo.",
        "(−3)+(+5)=2. Можна думати: 3 кроки вліво, 5 вправо → нетто 2 вправо.",
    ),
    (3, "odejmowanie"): T(
        "Odejmowanie całkowitych zamieniamy na dodawanie liczby przeciwnej.",
        "Віднімання цілих замінюємо на додавання протилежного числа.",
        "a − b = a + (−b). Najpierw zmień znak odjemnika, potem dodaj.",
        "a − b = a + (−b). Спочатку зміни знак від'ємника, потім додай.",
    ),
    (3, "liczba przeciwna"): T(
        "Liczba przeciwna ma tę samą odległość od zera, ale przeciwny znak.",
        "Протилежне число має ту саму відстань від нуля, але протилежний знак.",
        "Przeciwna do 7 to −7; przeciwna do −4 to 4. Na osi: odbicie względem 0.",
        "Протилежне до 7 — −7; до −4 — 4. На прямій: відбиття відносно 0.",
    ),
    (3, "zastosowania"): T(
        "Ujemne i dodatnie opisują świat: temperatura, dług, piętra pod ziemią.",
        "Від'ємні й додатні описують світ: температура, борг, поверхи під землею.",
        "Przykłady: −8°C, dług 20 zł, parking na poziomie −1.",
        "Приклади: −8°C, борг 20 zł, паркінг на рівні −1.",
    ),

    # ——— 7 Kolejność działań ———
    (7, "potęgi"): T(
        "Po nawiasach liczymy potęgi — bo to „skrócone mnożenie”.",
        "Після дужок рахуємо степені — бо це «скорочене множення».",
        "2+3² = 2+9 = 11 (nie 5²!). Najpierw 3², potem dodawanie.",
        "2+3² = 2+9 = 11 (не 5²!). Спочатку 3², потім додавання.",
    ),
    (7, "× i :"): T(
        "Mnożenie i dzielenie są „silniejsze” niż dodawanie i odejmowanie.",
        "Множення і ділення «сильніші» за додавання й віднімання.",
        "2+3×4 = 2+12 = 14. Najpierw ×, potem +.",
        "2+3×4 = 2+12 = 14. Спочатку ×, потім +.",
    ),
    (7, "+ i −"): T(
        "Dodawanie i odejmowanie robimy na końcu, od lewej do prawej.",
        "Додавання й віднімання робимо наприкінці, зліва направо.",
        "10−3+2 = 7+2 = 9. Nie zmieniaj kolejności bez nawiasów.",
        "10−3+2 = 7+2 = 9. Не міняй порядок без дужок.",
    ),
    (7, "ten sam poziom"): T(
        "Gdy działania są „tej samej mocy” (np. × i :), idziemy od lewej.",
        "Коли дії «тієї самої сили» (напр. × і :), йдемо зліва.",
        "24:6×2 = 4×2 = 8 (nie 24:12).",
        "24:6×2 = 4×2 = 8 (не 24:12).",
    ),
    (7, "przykład"): T(
        "Trudniejszy zapis liczysz warstwami: nawias → potęga → ×: → +−.",
        "Складніший запис рахуєш шарами: дужки → степінь → ×: → +−.",
        "2+3×(8−2²)=2+3×(8−4)=2+3×4=2+12=14. Zapisuj każdy krok.",
        "2+3×(8−2²)=2+3×(8−4)=2+3×4=2+12=14. Записуй кожен крок.",
    ),

    # ——— 8 Podzielność ———
    (8, "przez 2"): T(
        "Liczba dzieli się przez 2, gdy ostatnia cyfra jest parzysta.",
        "Число ділиться на 2, коли остання цифра парна.",
        "Końcówka 0,2,4,6,8 → tak. Nie musisz dzielić całej liczby.",
        "Кінець 0,2,4,6,8 → так. Не треба ділити все число.",
    ),
    (8, "przez 3"): T(
        "Przez 3: dodaj cyfry liczby. Jeśli suma dzieli się przez 3 — cała liczba też.",
        "На 3: додай цифри числа. Якщо сума ділиться на 3 — і все число теж.",
        "Np. 123 → 1+2+3=6, a 6:3=2 → 123 dzieli się przez 3.",
        "Напр. 123 → 1+2+3=6, а 6:3=2 → 123 ділиться на 3.",
    ),
    (8, "przez 4"): T(
        "Przez 4 patrzymy tylko na dwie ostatnie cyfry.",
        "На 4 дивимось лише на дві останні цифри.",
        "Jeśli liczba z dwóch ostatnich dzieli się przez 4 — cała też (np. …16, …24).",
        "Якщо число з двох останніх ділиться на 4 — і все теж (напр. …16, …24).",
    ),
    (8, "przez 5"): T(
        "Przez 5 kończy się na 0 lub 5 — jak „piątki” na linijce.",
        "На 5 закінчується на 0 або 5 — як «п'ятірки» на лінійці.",
        "…0 lub …5 → dzieli się przez 5.",
        "…0 або …5 → ділиться на 5.",
    ),
    (8, "przez 9"): T(
        "Przez 9 jak przez 3, ale suma cyfr musi dzielić się przez 9.",
        "На 9 як на 3, але сума цифр має ділитися на 9.",
        "Dodaj cyfry (ew. kilka razy), sprawdź podzielność przez 9.",
        "Додай цифри (інколи кілька разів), перевір подільність на 9.",
    ),
    (8, "przez 10"): T(
        "Przez 10 kończy się dokładnie na 0.",
        "На 10 закінчується рівно на 0.",
        "Końcówka 0 → tak; inaczej → nie.",
        "Кінець 0 → так; інакше → ні.",
    ),
    (8, "dzielnik / wielokrotność"): T(
        "Dzielnik dzieli liczbę bez reszty. Wielokrotność to wynik mnożenia przez liczbę naturalną.",
        "Дільник ділить число без остачі. Кратне — результат множення на натуральне число.",
        "Dzielniki 12: 1,2,3,4,6,12. 12 jest wielokrotnością 3, bo 3×4=12.",
        "Дільники 12: 1,2,3,4,6,12. 12 — кратне 3, бо 3×4=12.",
    ),
    (8, "liczba pierwsza"): T(
        "Liczba pierwsza ma dokładnie dwa dzielniki: 1 i samą siebie.",
        "Просте число має рівно два дільники: 1 і саме себе.",
        "2,3,5,7,11,13… Liczba 1 nie jest pierwsza. 4 nie jest (dzielniki 1,2,4).",
        "2,3,5,7,11,13… Число 1 не просте. 4 не є (дільники 1,2,4).",
    ),

    # ——— 9 Ułamki (1) ———
    (9, "licznik"): T(
        "Licznik (nad kreską) mówi, ile części bierzemy.",
        "Чисельник (над рискою) каже, скільки частин беремо.",
        "W 3/4 licznik to 3 — bierzemy trzy części.",
        "У 3/4 чисельник — 3 — беремо три частини.",
    ),
    (9, "mianownik"): T(
        "Mianownik (pod kreską) mówi, na ile równych części podzielono całość.",
        "Знаменник (під рискою) каже, на скільки рівних частин поділено ціле.",
        "W 3/4 mianownik to 4. Mianownik nigdy nie może być 0.",
        "У 3/4 знаменник — 4. Знаменник ніколи не може бути 0.",
    ),
    (9, "właściwy / niewłaściwy"): T(
        "Właściwy: licznik mniejszy od mianownika (mniej niż całość). Niewłaściwy: licznik ≥ mianownik.",
        "Правильний: чисельник менший за знаменник (менше за ціле). Неправильний: чисельник ≥ знаменник.",
        "2/5 < 1 (właściwy); 7/4 > 1 (niewłaściwy).",
        "2/5 < 1 (правильний); 7/4 > 1 (неправильний).",
    ),
    (9, "liczba mieszana"): T(
        "Liczba mieszana to całość + ułamek właściwy — wygodny zapis „ile i jeszcze kawałek”.",
        "Мішане число — ціле + правильний дріб — зручний запис «скільки і ще шматок».",
        "1 3/4 = 7/4. Żeby zamienić: całość × mianownik + licznik.",
        "1 3/4 = 7/4. Щоб перетворити: ціле × знаменник + чисельник.",
    ),
    (9, "ułamki równe"): T(
        "Równe ułamki mają tę samą wartość, choć wyglądają inaczej — jak 1/2 pizzy i 2/4 pizzy.",
        "Рівні дроби мають те саме значення, хоч виглядають інакше — як 1/2 піци і 2/4 піци.",
        "1/2 = 2/4 = 3/6. Powstają przez rozszerzanie lub skracanie.",
        "1/2 = 2/4 = 3/6. Виникають через розширення або скорочення.",
    ),

    # ——— 10 Ułamki (2) ———
    (10, "skracanie"): T(
        "Skracanie upraszcza ułamek: dzielimy licznik i mianownik tą samą liczbą ≠ 0.",
        "Скорочення спрощує дріб: ділимо чисельник і знаменник тим самим числом ≠ 0.",
        "4/6 = 2/3 (÷2). Wartość się nie zmienia — zmienia się tylko zapis.",
        "4/6 = 2/3 (÷2). Значення не змінюється — змінюється лише запис.",
    ),
    (10, "rozszerzanie"): T(
        "Rozszerzanie: mnożymy licznik i mianownik tą samą liczbą ≠ 0 — np. by mieć wspólny mianownik.",
        "Розширення: множимо чисельник і знаменник тим самим ≠ 0 — напр. щоб мати спільний знаменник.",
        "2/3 = 4/6 (×2). Znowu: wartość ta sama.",
        "2/3 = 4/6 (×2). Знову: значення те саме.",
    ),
    (10, "ułamek nieskracalny"): T(
        "Nieskracalny = nie da się już skrócić (licznik i mianownik nie mają wspólnego dzielnika > 1).",
        "Нескоротний = уже не можна скоротити (чисельник і знаменник не мають спільного дільника > 1).",
        "12/18 → ÷6 → 2/3. Często dzielimy przez NWD.",
        "12/18 → ÷6 → 2/3. Часто ділимо на НСД.",
    ),
    (10, "wspólny mianownik"): T(
        "Wspólny mianownik potrzebny do dodawania, odejmowania i porównywania ułamków.",
        "Спільний знаменник потрібний для додавання, віднімання й порівняння дробів.",
        "1/2 i 1/3 → 3/6 i 2/6. Szukaj wspólnej wielokrotności mianowników.",
        "1/2 і 1/3 → 3/6 і 2/6. Шукай спільне кратне знаменників.",
    ),
    (10, "porównywanie"): T(
        "Przy tym samym mianowniku większy licznik = większy ułamek. Przy różnych — najpierw wspólny mianownik.",
        "При однаковому знаменнику більший чисельник = більший дріб. При різних — спочатку спільний знаменник.",
        "2/5 < 3/5; 1/2 > 1/3 (bo 3/6 > 2/6).",
        "2/5 < 3/5; 1/2 > 1/3 (бо 3/6 > 2/6).",
    ),
    (10, "ułamek = dzielenie"): T(
        "Ułamek to też wynik dzielenia: licznik dzielony przez mianownik.",
        "Дріб — також результат ділення: чисельник, поділений на знаменник.",
        "3/4 = 3:4. To pomaga przy zamianie na dziesiętne.",
        "3/4 = 3:4. Це допомагає при перетворенні на десяткові.",
    ),

    # ——— 11 Ułamki dziesiętne ———
    (11, "ułamek dziesiętny"): T(
        "Ułamek dziesiętny zapisujemy z przecinkiem — wygodny w pieniądzach, miarach, wynikach.",
        "Десятковий дріб записуємо з комою — зручний у грошах, мірах, результатах.",
        "0,5 · 2,75 · 3,14. Przecinek oddziela część całkowitą od ułamkowej.",
        "0,5 · 2,75 · 3,14. Кома відокремлює цілу частину від дробової.",
    ),
    (11, "miejsca po przecinku"): T(
        "Kolejne miejsca po przecinku to dziesiętne, setne, tysięczne…",
        "Наступні місця після коми — десяті, соті, тисячні…",
        "W 2,375: 3 — dziesiętne, 7 — setne, 5 — tysięczne.",
        "У 2,375: 3 — десяті, 7 — соті, 5 — тисячні.",
    ),
    (11, "równoważność"): T(
        "Zera na końcu po przecinku nie zmieniają wartości — jak 0,5 i 0,50.",
        "Нулі в кінці після коми не змінюють значення — як 0,5 і 0,50.",
        "0,5 = 0,50 = 0,500. Nie dopisuj zer „w środku” bez sensu.",
        "0,5 = 0,50 = 0,500. Не дописуй нулів «всередині» без сенсу.",
    ),
    (11, "zamiana na zwykły"): T(
        "Zamiana na zwykły: cyfry po przecinku → licznik; mianownik 10, 100, 1000…",
        "Перетворення на звичайний: цифри після коми → чисельник; знаменник 10, 100, 1000…",
        "0,25 = 25/100 = 1/4. Potem skróć, jeśli się da.",
        "0,25 = 25/100 = 1/4. Потім скороти, якщо можна.",
    ),
    (11, "porównywanie"): T(
        "Porównujemy rozrząd po rozrządzie: najpierw części całkowite, potem kolejne miejsca po przecinku.",
        "Порівнюємо розряд за розрядом: спочатку цілі, потім наступні місця після коми.",
        "1,25 < 1,3, bo 1,25 < 1,30.",
        "1,25 < 1,3, бо 1,25 < 1,30.",
    ),
    (11, "zaokrąglanie"): T(
        "Zaokrąglanie dziesiętnych: patrz na następną cyfrę (≥5 w górę, <5 w dół).",
        "Округлення десяткових: дивись на наступну цифру (≥5 вгору, <5 вниз).",
        "3,141 → 3,14 (do setnych). Powiedz, do którego miejsca zaokrąglasz.",
        "3,141 → 3,14 (до сотих). Скажи, до якого місця округлюєш.",
    ),

    # ——— 12 Działania na ułamkach ———
    (12, "+/− ten sam mianownik"): T(
        "Przy wspólnym mianowniku dodajemy lub odejmujemy tylko liczniki.",
        "При спільному знаменнику додаємо або віднімаємо лише чисельники.",
        "2/7 + 3/7 = 5/7. Mianownik bez zmian.",
        "2/7 + 3/7 = 5/7. Знаменник без змін.",
    ),
    (12, "różne mianowniki"): T(
        "Przy różnych mianownikach najpierw sprowadź do wspólnego, potem +/− liczniki.",
        "При різних знаменниках спочатку зведи до спільного, потім +/− чисельники.",
        "1/2 + 1/3 = 3/6 + 2/6 = 5/6.",
        "1/2 + 1/3 = 3/6 + 2/6 = 5/6.",
    ),
    (12, "mnożenie"): T(
        "Mnożenie ułamków: licznik×licznik, mianownik×mianownik.",
        "Множення дробів: чисельник×чисельник, знаменник×знаменник.",
        "2/3 × 4/5 = 8/15. Potem skróć, jeśli można.",
        "2/3 × 4/5 = 8/15. Потім скороти, якщо можна.",
    ),
    (12, "odwrotność"): T(
        "Odwrotność ułamka: zamieniamy licznik z mianownikiem.",
        "Обернений дріб: міняємо чисельник і знаменник місцями.",
        "3/4 → 4/3. Iloczyn liczby i jej odwrotności = 1 (≠0).",
        "3/4 → 4/3. Добуток числа і його оберненого = 1 (≠0).",
    ),
    (12, "skracanie przed ×"): T(
        "Przed mnożeniem warto skracać „na krzyż” — mniej rachunków i mniejsze liczby.",
        "Перед множенням варто скорочувати «навхрест» — менше рахунку і менші числа.",
        "2/9 × 3/4: skróć 3 i 9 → 2/3 × 1/4 = 2/12 = 1/6.",
        "2/9 × 3/4: скороти 3 і 9 → 2/3 × 1/4 = 2/12 = 1/6.",
    ),

    # ——— 13 Potęgi ———
    (13, "potęga"): T(
        "Potęga to skrót: ta sama liczba mnożona przez siebie kilka razy.",
        "Степінь — скорочення: те саме число, помножене на себе кілька разів.",
        "2³ = 2×2×2 = 8. Nie myl z 2×3=6!",
        "2³ = 2×2×2 = 8. Не плутай із 2×3=6!",
    ),
    (13, "podstawa i wykładnik"): T(
        "Podstawa — co mnożymy; wykładnik — ile razy (mała liczba u góry).",
        "Основа — що множимо; показник — скільки разів (маленьке число вгорі).",
        "W aⁿ: a to podstawa, n to wykładnik.",
        "В aⁿ: a — основа, n — показник.",
    ),
    (13, "kwadrat i sześcian"): T(
        "Do drugiej potęgi nazywamy kwadratem, do trzeciej — sześcianem.",
        "До другого степеня називаємо квадратом, до третього — кубом.",
        "5²=25; 2³=8. W geometrii: pole kwadratu, objętość sześcianu.",
        "5²=25; 2³=8. У геометрії: площа квадрата, об'єм куба.",
    ),
    (13, "0, 1, 10"): T(
        "Wykładnik 1 nic nie zmienia; wykładnik 0 daje 1 (gdy podstawa ≠ 0). Potęgi 10 to „1 i zera”.",
        "Показник 1 нічого не змінює; показник 0 дає 1 (коли основа ≠ 0). Степені 10 — «1 і нулі».",
        "a¹=a; a⁰=1 (a≠0); 10ⁿ = 1 i n zer.",
        "a¹=a; a⁰=1 (a≠0); 10ⁿ = 1 і n нулів.",
    ),
    (13, "mnożenie potęg"): T(
        "Przy tej samej podstawie mnożenie potęg = dodawanie wykładników.",
        "При тій самій основі множення степенів = додавання показників.",
        "aᵐ · aⁿ = aᵐ⁺ⁿ. Np. 2³·2² = 2⁵.",
        "aᵐ · aⁿ = aᵐ⁺ⁿ. Напр. 2³·2² = 2⁵.",
    ),
    (13, "dzielenie potęg"): T(
        "Przy tej samej podstawie dzielenie potęg = odejmowanie wykładników (podstawa ≠ 0).",
        "При тій самій основі ділення степенів = віднімання показників (основа ≠ 0).",
        "aᵐ : aⁿ = aᵐ⁻ⁿ. Np. 2⁵:2² = 2³.",
        "aᵐ : aⁿ = aᵐ⁻ⁿ. Напр. 2⁵:2² = 2³.",
    ),

    # ——— 14 Pierwiastki ———
    (14, "pierwiastek kwadratowy"): T(
        "Pierwiastek kwadratowy z liczby to taka liczba, której kwadrat daje tę pod pierwiastkiem.",
        "Квадратний корінь з числа — таке число, квадрат якого дає те, що під коренем.",
        "√9 = 3, bo 3² = 9. W SP bierzemy nieujemny wynik.",
        "√9 = 3, бо 3² = 9. У школі беремо невід'ємний результат.",
    ),
    (14, "zapis"): T(
        "Znak √ stoi przed wyrażeniem podpierwiastkowym.",
        "Знак √ стоїть перед підкореневим виразом.",
        "√□ — najpierw policz to, co pod znakiem (gdy trzeba), potem pierwiastek.",
        "√□ — спочатку порахуй те, що під знаком (коли треба), потім корінь.",
    ),
    (14, "przykłady"): T(
        "Najczęstsze pierwiastki warto znać na pamięć — jak tabliczkę.",
        "Найчастіші корені варто знати напам'ять — як таблицю.",
        "√4=2, √16=4, √25=5, √100=10.",
        "√4=2, √16=4, √25=5, √100=10.",
    ),
    (14, "związek z potęgą"): T(
        "Pierwiastek i potęga druga to działania odwrotne.",
        "Корінь і другий степінь — обернені дії.",
        "(√a)² = a oraz √(a²)=|a| (w SP zwykle a≥0).",
        "(√a)² = a та √(a²)=|a| (у школі зазвичай a≥0).",
    ),
    (14, "kwadraty doskonałe"): T(
        "Kwadrat doskonały to wynik podniesienia liczby naturalnej do kwadratu.",
        "Повний квадрат — результат піднесення натурального числа до квадрата.",
        "1,4,9,16,25,36,49,64,81,100 — ucz się do 10².",
        "1,4,9,16,25,36,49,64,81,100 — вчи до 10².",
    ),
    (14, "szacowanie"): T(
        "Gdy nie ma dokładnego pierwiastka, szacujemy między kwadratami doskonałymi.",
        "Коли немає точного кореня, оцінюємо між повними квадратами.",
        "√50 ≈ 7,1, bo 7²=49 (blisko 50).",
        "√50 ≈ 7,1, бо 7²=49 (близько 50).",
    ),

    # ——— 15 Procenty ———
    (15, "procent"): T(
        "Procent to setna część całości — wygodny sposób porównywania części.",
        "Відсоток — сота частина цілого — зручний спосіб порівнювати частини.",
        "1% = 1/100 = 0,01. 100% = całość.",
        "1% = 1/100 = 0,01. 100% = ціле.",
    ),
    (15, "zwiększenie o p%"): T(
        "Zwiększenie o p% to dodanie p% od liczby do niej samej.",
        "Збільшення на p% — додавання p% від числа до нього самого.",
        "Nowa wartość = a(1 + p/100). Np. +20% z 50 → 60.",
        "Нове значення = a(1 + p/100). Напр. +20% від 50 → 60.",
    ),
    (15, "zmniejszenie o p%"): T(
        "Zmniejszenie o p% to odjęcie p% od liczby.",
        "Зменшення на p% — віднімання p% від числа.",
        "Nowa wartość = a(1 − p/100). Uważaj: −20% a potem +20% ≠ start.",
        "Нове значення = a(1 − p/100). Увага: −20% а потім +20% ≠ старт.",
    ),
    (15, "zamiany"): T(
        "Procent, ułamek i zapis dziesiętny to trzy twarze tej samej części.",
        "Відсоток, дріб і десятковий запис — три обличчя тієї самої частини.",
        "25% = 1/4 = 0,25. Wybierz formę najwygodniejszą do liczenia.",
        "25% = 1/4 = 0,25. Вибери форму, зручнішу для рахунку.",
    ),
    (15, "przykłady"): T(
        "Ćwicz „łatwe procenty”: 10%, 25%, 50% — potem resztę.",
        "Тренуй «легкі відсотки»: 10%, 25%, 50% — потім решту.",
        "20% z 50 = 10; 15% z 200 = 30. 10%=1/10, 50%=1/2, 25%=1/4.",
        "20% від 50 = 10; 15% від 200 = 30. 10%=1/10, 50%=1/2, 25%=1/4.",
    ),

    # ——— 16 Proporcjonalność ———
    (16, "proporcjonalność prosta"): T(
        "Proporcjonalność prosta: gdy jedna wielkość rośnie, druga rośnie tyle samo „razy”.",
        "Пряма пропорційність: коли одна величина зростає, друга зростає стільки само «разів».",
        "y = k·x. Stosunek y/x jest stały.",
        "y = k·x. Відношення y/x стале.",
    ),
    (16, "współczynnik"): T(
        "Współczynnik proporcjonalności k mówi, ile razy y jest względem x.",
        "Коефіцієнт пропорційності k каже, у скільки разів y щодо x.",
        "k = y/x. Gdy znasz k i x, liczysz y = k·x.",
        "k = y/x. Коли знаєш k і x, рахуєш y = k·x.",
    ),
    (16, "wykres"): T(
        "Wykres proporcjonalności prostej to prosta przechodząca przez początek układu (0,0).",
        "Графік прямої пропорційності — пряма через початок координат (0,0).",
        "Jeśli prosta nie przechodzi przez (0,0) — to już nie ta sama sytuacja.",
        "Якщо пряма не проходить через (0,0) — це вже не та сама ситуація.",
    ),
    (16, "tabela wartości"): T(
        "Tabela pomaga zobaczyć stały stosunek: x rośnie, y rośnie proporcjonalnie.",
        "Таблиця допомагає побачити стале відношення: x зростає, y зростає пропорційно.",
        "x: 1,2,3 → y: 2,4,6 (tu k=2).",
        "x: 1,2,3 → y: 2,4,6 (тут k=2).",
    ),
    (16, "przykład"): T(
        "W życiu: cena za kilogram — im więcej kg, tym proporcjonalnie więcej zł.",
        "У житті: ціна за кілограм — що більше кг, то пропорційно більше zł.",
        "3 kg → 12 zł ⇒ 1 kg = 4 zł ⇒ 5 kg → 20 zł.",
        "3 кг → 12 zł ⇒ 1 кг = 4 zł ⇒ 5 кг → 20 zł.",
    ),
    (16, "proporcja"): T(
        "Proporcja to równość dwóch stosunków.",
        "Пропорція — рівність двох відношень.",
        "a/b = c/d → a·d = b·c (iloczyn skrajnych = iloczyn środkowych).",
        "a/b = c/d → a·d = b·c (добуток крайніх = добуток середніх).",
    ),

    # ——— 17 Wyrażenia algebraiczne ———
    (17, "wyrażenie algebraiczne"): T(
        "Wyrażenie algebraiczne to zapis z liczbami, literami i znakami działań — bez znaku „=”.",
        "Алгебраїчний вираз — запис із числами, літерами і знаками дій — без знака «=».",
        "Np. 3x + 5y − 8. To przepis na obliczenie, gdy poznasz litery.",
        "Напр. 3x + 5y − 8. Це рецепт обчислення, коли дізнаєшся літери.",
    ),
    (17, "elementy"): T(
        "Elementy wyrażenia: liczby, litery (zmienne) i znaki działań oraz nawiasy.",
        "Елементи виразу: числа, літери (змінні) і знаки дій та дужки.",
        "Rozpoznaj części, zanim zaczniesz liczyć.",
        "Розпізнай частини, перш ніж рахувати.",
    ),
    (17, "zmienna"): T(
        "Zmienna (litera) oznacza liczbę, która może się zmieniać lub jest na razie nieznana.",
        "Змінна (літера) означає число, яке може змінюватися або поки що невідоме.",
        "Częste litery: x, y, a, n. Najpierw podstaw, potem licz.",
        "Часті літери: x, y, a, n. Спочатку підстав, потім рахуй.",
    ),
    (17, "wartość liczbowa"): T(
        "Wartość liczbowa powstaje, gdy zamiast litery wstawisz konkretną liczbę.",
        "Числове значення виникає, коли замість літери підставляєш конкретне число.",
        "Dla x=2: 3x+1 = 3·2+1 = 7.",
        "Для x=2: 3x+1 = 3·2+1 = 7.",
    ),
    (17, "zapis skrócony"): T(
        "Przy literach często nie piszemy znaku mnożenia: 3x znaczy 3·x.",
        "Біля літер часто не пишемо знака множення: 3x означає 3·x.",
        "3x = x+x+x; xy = x·y. To standard szkolny.",
        "3x = x+x+x; xy = x·y. Це шкільний стандарт.",
    ),
    (17, "kolejność"): T(
        "W wyrażeniach algebraicznych obowiązuje ta sama kolejność działań co w arytmetyce.",
        "У алгебраїчних виразах той самий порядок дій, що в арифметиці.",
        "Nawiasy → potęgi → ×: → +−.",
        "Дужки → степені → ×: → +−.",
    ),

    # ——— 18 Sumy algebraiczne ———
    (18, "jednomian"): T(
        "Jednomian to iloczyn liczby i liter (albo sama liczba) — jeden „kawałek” zapisu.",
        "Одночлен — добуток числа і літер (або саме число) — один «шматок» запису.",
        "Przykłady: 5x², −3ab, 7.",
        "Приклади: 5x², −3ab, 7.",
    ),
    (18, "suma algebraiczna"): T(
        "Suma algebraiczna to dodawanie i odejmowanie jednomianów.",
        "Алгебраїчна сума — додавання й віднімання одночленів.",
        "Np. 3x − 2y + 5.",
        "Напр. 3x − 2y + 5.",
    ),
    (18, "wyrazy podobne"): T(
        "Wyrazy podobne mają te same litery z tymi samymi wykładnikami — różnią się tylko liczbą z przodu.",
        "Подібні доданки мають ті самі літери з тими самими показниками — відрізняються лише числом спереду.",
        "3x i −5x są podobne; 3x i 3x² — nie.",
        "3x і −5x подібні; 3x і 3x² — ні.",
    ),
    (18, "redukcja"): T(
        "Redukcja (upraszczanie): łączymy wyrazy podobne, dodając ich współczynniki.",
        "Зведення (спрощення): об'єднуємо подібні доданки, додаючи їхні коефіцієнти.",
        "3x + 5x = 8x. Najpierw znajdź podobne, potem policz współczynniki.",
        "3x + 5x = 8x. Спочатку знайди подібні, потім порахуй коефіцієнти.",
    ),
    (18, "współczynnik"): T(
        "Współczynnik to czynnik liczbowy stojący przy literach.",
        "Коефіцієнт — числовий множник біля літер.",
        "W 7a²b współczynnik to 7.",
        "У 7a²b коефіцієнт — 7.",
    ),
    (18, "przykład"): T(
        "Przykład redukcji: grupujemy litery osobno i liczby osobno.",
        "Приклад зведення: групуємо літери окремо і числа окремо.",
        "2a+5−a+3 = (2a−a)+(5+3) = a+8.",
        "2a+5−a+3 = (2a−a)+(5+3) = a+8.",
    ),

    # ——— 19 Równania ———
    (19, "równanie"): T(
        "Równanie to równość z niewiadomą — waga, która ma być zrównoważona.",
        "Рівняння — рівність із невідомим — терези, які мають бути в рівновазі.",
        "x + 5 = 12. Szukamy takiej liczby x, by obie strony były równe.",
        "x + 5 = 12. Шукаємо таке число x, щоб обидва боки були рівні.",
    ),
    (19, "niewiadoma"): T(
        "Niewiadoma to liczba, którą mamy znaleźć — zwykle oznaczana x lub y.",
        "Невідоме — число, яке треба знайти — зазвичай позначається x або y.",
        "Cel: odkryć wartość niewiadomej.",
        "Мета: відкрити значення невідомого.",
    ),
    (19, "rozwiązanie"): T(
        "Rozwiązanie to wartość, która spełnia równanie (po podstawieniu obie strony się zgadzają).",
        "Розв'язок — значення, що задовольняє рівняння (після підставляння обидва боки збігаються).",
        "Dla x+5=12 rozwiązaniem jest x=7.",
        "Для x+5=12 розв'язок — x=7.",
    ),
    (19, "przenoszenie"): T(
        "Przenoszenie na drugą stronę zmienia znak — to skrót bilansowania.",
        "Перенесення на другий бік змінює знак — це скорочення методу рівноваги.",
        "+ po drugiej stronie staje się − (i odwrotnie). Zawsze sprawdzaj!",
        "+ на другому боці стає − (і навпаки). Завжди перевіряй!",
    ),
    (19, "sprawdzenie"): T(
        "Sprawdzenie: podstaw wynik do równania i policz obie strony.",
        "Перевірка: підстав результат у рівняння і порахуй обидва боки.",
        "7+5=12 ✓ — rozwiązanie jest poprawne.",
        "7+5=12 ✓ — розв'язок правильний.",
    ),

    # ——— 22 Objętość ———
    (22, "objętość"): T(
        "Objętość mówi, ile miejsca zajmuje ciało lub ciecz — „ile się mieści w środku”.",
        "Об'єм каже, скільки місця займає тіло або рідина — «скільки вміщується всередині».",
        "Jednostki: cm³, m³, litr, mililitr.",
        "Одиниці: cm³, m³, літр, мілілітр.",
    ),
    (22, "litr"): T(
        "Litr to wygodna jednostka objętości płynów (napoje, przepisy).",
        "Літр — зручна одиниця об'єму рідин (напої, рецепти).",
        "1 l = 1000 ml.",
        "1 l = 1000 ml.",
    ),
    (22, "mililitr"): T(
        "Mililitr to tysięczna część litra — małe ilości (leki, miarki kuchenne).",
        "Мілілітр — тисячна частина літра — малі кількості (ліки, мірки).",
        "1 ml = 1 cm³.",
        "1 ml = 1 cm³.",
    ),
    (22, "przeliczanie"): T(
        "Przeliczanie litr ↔ mililitr: × lub ÷ przez 1000.",
        "Перетворення літр ↔ мілілітр: × або ÷ на 1000.",
        "2,5 l = 2500 ml.",
        "2,5 l = 2500 ml.",
    ),
    (22, "objętość bryły"): T(
        "Objętość prostopadłościanu to iloczyn trzech wymiarów.",
        "Об'єм прямокутного паралелепіпеда — добуток трьох вимірів.",
        "V = a·b·c (długość × szerokość × wysokość).",
        "V = a·b·c (довжина × ширина × висота).",
    ),
    (22, "przykład"): T(
        "Policz objętość pudełka — pomnóż trzy boki.",
        "Порахуй об'єм коробки — помнож три сторони.",
        "2×3×4 cm → V = 24 cm³.",
        "2×3×4 cm → V = 24 cm³.",
    ),

    # ——— 25 Temperatura ———
    (25, "stopień Celsjusza"): T(
        "W szkole temperaturę podajemy w stopniach Celsjusza (°C).",
        "У школі температуру подаємо в градусах Цельсія (°C).",
        "Zapis: 20°C, −5°C. Zawsze pisz jednostkę.",
        "Запис: 20°C, −5°C. Завжди пиши одиницю.",
    ),
    (25, "termometr"): T(
        "Termometr pokazuje temperaturę na skali — często z + i −.",
        "Термометр показує температуру на шкалі — часто з + і −.",
        "Odczytuj uważnie: gdzie jest kreska / słupek względem zera.",
        "Зчитуй уважно: де риска / стовпчик відносно нуля.",
    ),
    (25, "powyżej / poniżej zera"): T(
        "Powyżej zera — ciepło na plusie; poniżej — mróz (ujemne).",
        "Вище нуля — тепло на плюсі; нижче — мороз (від'ємні).",
        "+5°C · −8°C. Ujemne zapisuj ze znakiem −.",
        "+5°C · −8°C. Від'ємні записуй зі знаком −.",
    ),
    (25, "porównywanie"): T(
        "Temperatury porównujemy jak liczby całkowite na osi.",
        "Температури порівнюємо як цілі числа на прямій.",
        "−3°C < 2°C, bo −3 jest bardziej w lewo na osi.",
        "−3°C < 2°C, бо −3 лівіше на прямій.",
    ),
    (25, "różnica temperatur"): T(
        "Różnica temperatur to „o ile się zmieniło” — zawsze nieujemna odległość.",
        "Різниця температур — «на скільки змінилося» — завжди невід'ємна відстань.",
        "Z −4 do +6: |6 − (−4)| = 10°.",
        "З −4 до +6: |6 − (−4)| = 10°.",
    ),
    (25, "w życiu"): T(
        "Temperaturę czytamy w pogodzie, piekarniku, przy zdrowiu.",
        "Температуру читаємо в погоді, духовці, при здоров'ї.",
        "Sprawdzaj jednostki i znak (− zimą!).",
        "Перевіряй одиниці і знак (− взимку!).",
    ),

    # ——— 27 Prędkość i skala ———
    (27, "prędkość"): T(
        "Prędkość mówi, jak szybko pokonujemy drogę — droga na jednostkę czasu.",
        "Швидкість каже, як швидко долаємо шлях — шлях на одиницю часу.",
        "v = s/t. Zapamiętaj trójkąt: v, s, t.",
        "v = s/t. Запам'ятай трикутник: v, s, t.",
    ),
    (27, "jednostki"): T(
        "Najczęstsze jednostki: km/h (samochód) i m/s (fizyka w szkole).",
        "Найчастіші одиниці: km/h (авто) і m/s (фізика в школі).",
        "Uważaj na zamianę jednostek przed liczeniem.",
        "Увага на перетворення одиниць перед рахунком.",
    ),
    (27, "droga i czas"): T(
        "Z jednego wzoru robimy trzy: prędkość, droga, czas.",
        "З однієї формули робимо три: швидкість, шлях, час.",
        "s = v·t; t = s/v; v = s/t.",
        "s = v·t; t = s/v; v = s/t.",
    ),
    (27, "skala mapy"): T(
        "Skala mapy mówi, ile razy rzeczywistość jest pomniejszona na papierze.",
        "Масштаб карти каже, у скільки разів дійсність зменшена на папері.",
        "1:100 000 → 1 cm na mapie = 100 000 cm w terenie (= 1 km).",
        "1:100 000 → 1 см на карті = 100 000 см на місцевості (= 1 км).",
    ),
    (27, "obliczanie odległości"): T(
        "Odległość w terenie = miara na mapie × skala (po zamianie jednostek).",
        "Відстань на місцевості = міра на карті × масштаб (після перетворення одиниць).",
        "3 cm · 100 000 = 300 000 cm = 3 km.",
        "3 см · 100 000 = 300 000 см = 3 км.",
    ),
    (27, "przykład v"): T(
        "Przykład prędkości: podziel drogę przez czas.",
        "Приклад швидкості: поділи шлях на час.",
        "120 km / 2 h = 60 km/h.",
        "120 км / 2 год = 60 км/год.",
    ),

    # ——— 29 Figury (2) ———
    (29, "trójkąt"): T(
        "Trójkąt ma 3 boki i 3 kąty. To najprostszy wielokąt.",
        "Трикутник має 3 сторони і 3 кути. Це найпростіший многокутник.",
        "Suma kątów w trójkącie zawsze = 180°.",
        "Сума кутів у трикутнику завжди = 180°.",
    ),
    (29, "rodzaje trójkątów"): T(
        "Trójkąty dzielimy według boków i według kątów.",
        "Трикутники ділимо за сторонами і за кутами.",
        "Boki: równoboczny / równoramienny / różnoboczny. Kąty: ostro-, prawo-, rozwartokątny.",
        "Сторони: рівносторонній / рівнобедрений / різносторонній. Кути: гостро-, прямо-, тупокутний.",
    ),
    (29, "kwadrat"): T(
        "Kwadrat: 4 równe boki i 4 kąty proste — bardzo „regularny” czworokąt.",
        "Квадрат: 4 рівні сторони і 4 прямі кути — дуже «правильний» чотирикутник.",
        "Jest szczególnym prostokątem i szczególnym rombem.",
        "Є особливим прямокутником і особливим ромбом.",
    ),
    (29, "prostokąt"): T(
        "Prostokąt: wszystkie kąty proste; przeciwległe boki równe.",
        "Прямокутник: усі кути прямі; протилежні сторони рівні.",
        "Nie każdy prostokąt jest kwadratem (tylko gdy boki równe).",
        "Не кожен прямокутник — квадрат (лише коли сторони рівні).",
    ),
    (29, "romb / równoległobok"): T(
        "Równoległobok ma przeciwległe boki równoległe. Romb: wszystkie boki równe.",
        "Паралелограм має протилежні сторони паралельні. Ромб: усі сторони рівні.",
        "Kwadrat jest rombem i prostokątem jednocześnie.",
        "Квадрат є ромбом і прямокутником одночасно.",
    ),
    (29, "trapez"): T(
        "Trapez ma dokładnie jedną parę boków równoległych (podstawy).",
        "Трапеція має рівно одну пару паралельних сторін (основи).",
        "Szukaj jednej pary równoległych — to znak trapezu.",
        "Шукай одну пару паралельних — це ознака трапеції.",
    ),

    # ——— 30 Koło i okrąg ———
    (30, "okrąg"): T(
        "Okrąg to tylko linia — wszystkie punkty w równej odległości od środka.",
        "Коло — лише лінія — усі точки на однаковій відстані від центра.",
        "To „brzeg”, bez wnętrza.",
        "Це «межа», без внутрішньої частини.",
    ),
    (30, "koło"): T(
        "Koło to okrąg razem z wnętrzem — cała „tarcza”.",
        "Круг — коло разом із серединою — увесь «диск».",
        "Nie myl: okrąg = linia; koło = linia + środek.",
        "Не плутай: коло = лінія; круг = лінія + середина.",
    ),
    (30, "środek"): T(
        "Środek to punkt jednakowo odległy od wszystkich punktów okręgu.",
        "Центр — точка, однаково віддалена від усіх точок кола.",
        "Oznaczamy zwykle O.",
        "Позначаємо зазвичай O.",
    ),
    (30, "promień"): T(
        "Promień to odcinek od środka do punktu na okręgu.",
        "Радіус — відрізок від центра до точки на колі.",
        "r = OA. Wszystkie promienie tego samego okręgu są równe.",
        "r = OA. Усі радіуси того самого кола рівні.",
    ),
    (30, "średnica"): T(
        "Średnica przechodzi przez środek i łączy dwa punkty okręgu — najdłuższa cięciwa.",
        "Діаметр проходить через центр і з'єднує дві точки кола — найдовша хорда.",
        "d = 2r. Zapamiętaj na zawsze.",
        "d = 2r. Запам'ятай назавжди.",
    ),
    (30, "cięciwa"): T(
        "Cięciwa łączy dwa punkty okręgu, niekoniecznie przez środek.",
        "Хорда з'єднує дві точки кола, не обов'язково через центр.",
        "Średnica to szczególna (najdłuższa) cięciwa.",
        "Діаметр — особлива (найдовша) хорда.",
    ),

    # ——— 31 π ———
    (31, "liczba π"): T(
        "π (pi) to stała: stosunek długości okręgu do średnicy — zawsze ten sam.",
        "π (пі) — стала: відношення довжини кола до діаметра — завжди те саме.",
        "W SP zwykle π ≈ 3,14 (albo 22/7, jeśli nauczyciel tak poda).",
        "У школі зазвичай π ≈ 3,14 (або 22/7, якщо так сказав учитель).",
    ),
    (31, "pole koła"): T(
        "Pole koła to miara powierzchni „tarczy”.",
        "Площа круга — міра поверхні «диска».",
        "P = πr². Najpierw r², potem ×π.",
        "P = πr². Спочатку r², потім ×π.",
    ),
    (31, "przykład C"): T(
        "Przykład długości okręgu: podstaw r do wzoru.",
        "Приклад довжини кола: підстав r у формулу.",
        "r=5 → C ≈ 2·3,14·5 = 31,4.",
        "r=5 → C ≈ 2·3,14·5 = 31,4.",
    ),
    (31, "przykład P"): T(
        "Przykład pola: najpierw kwadrat promienia, potem ×π.",
        "Приклад площі: спочатку квадрат радіуса, потім ×π.",
        "r=5 → P ≈ 3,14·25 = 78,5.",
        "r=5 → P ≈ 3,14·25 = 78,5.",
    ),
    (31, "zależność"): T(
        "Gdy promień rośnie 2 razy, długość okręgu też ×2, ale pole rośnie ×4.",
        "Коли радіус зростає в 2 рази, довжина кола теж ×2, але площа — ×4.",
        "Pole zależy od r², dlatego rośnie szybciej niż obwód.",
        "Площа залежить від r², тому росте швидше за довжину кола.",
    ),

    # ——— 32 Kąt ———
    (32, "kąt"): T(
        "Kąt to figura z dwóch półprostych o wspólnym początku (wierzchołku).",
        "Кут — фігура з двох півпрямих зі спільним початком (вершиною).",
        "Zapis: ∠AOB. Środkowa litera to wierzchołek.",
        "Запис: ∠AOB. Середня літера — вершина.",
    ),
    (32, "wierzchołek"): T(
        "Wierzchołek kąta to wspólny początek obu ramion.",
        "Вершина кута — спільний початок обох сторін.",
        "W ∠AOB wierzchołek to O.",
        "В ∠AOB вершина — O.",
    ),
    (32, "ramiona / strony"): T(
        "Ramiona (strony) kąta to dwie półproste wychodzące z wierzchołka.",
        "Сторони кута — дві півпрямі, що виходять із вершини.",
        "OA i OB tworzą kąt AOB.",
        "OA і OB утворюють кут AOB.",
    ),
    (32, "miara kąta"): T(
        "Miara kąta mówi, „jak szeroko” otwarte są ramiona — w stopniach.",
        "Міра кута каже, «як широко» відкриті сторони — у градусах.",
        "Pełny obrót = 360°. Jednostka: stopień (°).",
        "Повний оберт = 360°. Одиниця: градус (°).",
    ),
    (32, "kątomierz"): T(
        "Kątomierz to narzędzie do mierzenia kątów (półkole ze skalą).",
        "Кутомір — інструмент для вимірювання кутів (півколо зі шкалою).",
        "Przyłóż środek do wierzchołka, 0° wzdłuż jednego ramienia, odczytaj drugie.",
        "Приклади центр до вершини, 0° вздовж однієї сторони, зчитай другу.",
    ),
    (32, "półobrót / obrót"): T(
        "Półobrót to 180° (prosta). Pełny obrót to 360°.",
        "Півоберт — 180° (пряма). Повний оберт — 360°.",
        "180° · 360° — zapamiętaj jak punkty orientacyjne.",
        "180° · 360° — запам'ятай як орієнтири.",
    ),

    # ——— 33 Rodzaje kątów ———
    (33, "kąt zerowy"): T(
        "Kąt zerowy: ramiona się pokrywają — miara 0°.",
        "Нульовий кут: сторони збігаються — міра 0°.",
        "0° — start skali.",
        "0° — старт шкали.",
    ),
    (33, "kąt ostry"): T(
        "Kąt ostry jest mniejszy od prostego — „ostry jak róg”.",
        "Гострий кут менший за прямий — «гострий як ріг».",
        "0° < α < 90°.",
        "0° < α < 90°.",
    ),
    (33, "kąt prosty"): T(
        "Kąt prosty ma 90° — jak róg kartki lub kwadratu.",
        "Прямий кут має 90° — як кут аркуша або квадрата.",
        "α = 90°. To najważniejszy kąt-orientacyjny.",
        "α = 90°. Це найважливіший кут-орієнтир.",
    ),
    (33, "kąt rozwarty"): T(
        "Kąt rozwarty jest większy od prostego, ale mniejszy od półpełnego.",
        "Тупий кут більший за прямий, але менший за розгорнутий.",
        "90° < α < 180°.",
        "90° < α < 180°.",
    ),
    (33, "kąt półpełny"): T(
        "Kąt półpełny to 180° — ramiona tworzą prostą.",
        "Розгорнутий кут — 180° — сторони утворюють пряму.",
        "α = 180°.",
        "α = 180°.",
    ),
    (33, "kąt pełny"): T(
        "Kąt pełny to pełny obrót — 360°.",
        "Повний кут — повний оберт — 360°.",
        "α = 360°.",
        "α = 360°.",
    ),

    # ——— 34 Pary kątów ———
    (34, "proste równoległe"): T(
        "Proste równoległe nigdy się nie przecinają i biegną „obok siebie”.",
        "Паралельні прямі ніколи не перетинаються і йдуть «поряд».",
        "Zapis: a ∥ b.",
        "Запис: a ∥ b.",
    ),
    (34, "sieczna"): T(
        "Sieczna to prosta, która przecina obie równoległe.",
        "Січна — пряма, що перетинає обидві паралельні.",
        "Tworzy wiele kątów — część z nich jest równa.",
        "Утворює багато кутів — частина з них рівні.",
    ),
    (34, "kąty odpowiadające"): T(
        "Kąty odpowiadające leżą w tych samych „pozycjach” przy obu przecięciach.",
        "Відповідні кути лежать у тих самих «позиціях» при обох перетинах.",
        "Przy a ∥ b kąty odpowiadające są równe.",
        "При a ∥ b відповідні кути рівні.",
    ),
    (34, "naprzemianległe"): T(
        "Kąty naprzemianległe leżą na przemian po stronach siecznej, między prostymi.",
        "Навхрест лежачі кути лежать навперемінно по боках січної, між прямими.",
        "Przy a ∥ b są równe.",
        "При a ∥ b вони рівні.",
    ),
    (34, "przyległe"): T(
        "Kąty przyległe mają wspólne ramię i razem dają półpełny.",
        "Суміжні кути мають спільну сторону і разом дають розгорнутий.",
        "Suma = 180°.",
        "Сума = 180°.",
    ),
    (34, "wierzchołkowe"): T(
        "Kąty wierzchołkowe są naprzeciw siebie przy przecięciu dwóch prostych.",
        "Вертикальні кути — навпроти один одного при перетині двох прямих.",
        "Są zawsze równe.",
        "Завжди рівні.",
    ),

    # ——— 35 Obwód i pole ———
    (35, "obwód"): T(
        "Obwód to długość „dookoła” figury — ile zmierzysz, idąc po brzegu.",
        "Периметр — довжина «навколо» фігури — скільки виміряєш, ідучи по краю.",
        "Obwód = suma długości boków.",
        "Периметр = сума довжин сторін.",
    ),
    (35, "pole"): T(
        "Pole to miara powierzchni w środku figury — „ile zajmuje miejsca na kartce”.",
        "Площа — міра поверхні всередині фігури — «скільки займає місця на аркуші».",
        "Jednostki: cm², m². Nie myl z obwodem!",
        "Одиниці: cm², m². Не плутай із периметром!",
    ),
    (35, "prostokąt"): T(
        "Dla prostokąta liczymy obwód i pole z boków a i b.",
        "Для прямокутника рахуємо периметр і площу зі сторін a і b.",
        "Obw = 2(a+b); Pole = a·b.",
        "Перим. = 2(a+b); Площа = a·b.",
    ),
    (35, "kwadrat"): T(
        "Kwadrat ma wszystkie boki równe — wzory się upraszczają.",
        "Квадрат має всі сторони рівні — формули спрощуються.",
        "Obw = 4a; Pole = a².",
        "Перим. = 4a; Площа = a².",
    ),
    (35, "równoległobok"): T(
        "Pole równoległoboku = podstawa × wysokość (wysokość prostopadła do podstawy).",
        "Площа паралелограма = основа × висота (висота перпендикулярна до основи).",
        "P = a·h. Nie mnoż boków „na skos” bez wysokości.",
        "P = a·h. Не множ сторони «навскіс» без висоти.",
    ),

    # ——— 36 Bryły ———
    (36, "bryła"): T(
        "Bryła to figura przestrzenna — ma długość, szerokość i wysokość oraz objętość.",
        "Тіло — просторова фігура — має довжину, ширину й висоту та об'єм.",
        "To 3D, nie płaska figura na kartce.",
        "Це 3D, не плоска фігура на аркуші.",
    ),
    (36, "sześcian"): T(
        "Sześcian ma 6 kwadratowych ścian i wszystkie krawędzie równe — jak kostka.",
        "Куб має 6 квадратних граней і всі ребра рівні — як кубик.",
        "V = a³.",
        "V = a³.",
    ),
    (36, "prostopadłościan"): T(
        "Prostopadłościan wygląda jak pudełko: ściany to prostokąty.",
        "Прямокутний паралелепіпед схожий на коробку: грані — прямокутники.",
        "V = a·b·c.",
        "V = a·b·c.",
    ),
    (36, "ostrosłup"): T(
        "Ostrosłup ma podstawę i ściany boczne zbiegające się w wierzchołku.",
        "Піраміда має основу і бічні грані, що збігаються у вершині.",
        "Np. ostrosłup o podstawie kwadratu.",
        "Напр. піраміда з квадратною основою.",
    ),
    (36, "walec / stożek / kula"): T(
        "Walec, stożek i kula to bryły „okrągłe” — często w życiu (puszka, rożek, piłka).",
        "Циліндр, конус і куля — «круглі» тіла — часто в житті (банка, ріжок, м'яч).",
        "Walec: 2 podstawy-koła; kula: wszystkie punkty w odległości r od środka.",
        "Циліндр: 2 основи-круги; куля: усі точки на відстані r від центра.",
    ),
    (36, "objętość sześcianu"): T(
        "Objętość sześcianu to krawędź do trzeciej potęgi.",
        "Об'єм куба — ребро до третього степеня.",
        "V = a³. Najpierw a·a·a.",
        "V = a³. Спочатку a·a·a.",
    ),

    # ——— 37 Symetria ———
    (37, "symetria"): T(
        "Symetria to powtórzenie kształtu przez odbicie lub obrót — porządek i harmonia.",
        "Симетрія — повторення форми через відбиття або обертання — порядок і гармонія.",
        "Szukaj „lustra” lub obrotu o 180°.",
        "Шукай «дзеркало» або поворот на 180°.",
    ),
    (37, "oś symetrii"): T(
        "Oś symetrii działa jak lustro: dzieli figurę na dwie lustrzane części.",
        "Вісь симетрії діє як дзеркало: ділить фігуру на дві дзеркальні частини.",
        "Odległości punktów od osi po obu stronach są równe.",
        "Відстані точок від осі з обох боків рівні.",
    ),
    (37, "środek symetrii"): T(
        "Środek symetrii: figura pokrywa się sama ze sobą po obrocie o 180° wokół punktu.",
        "Центр симетрії: фігура збігається сама з собою після повороту на 180° навколо точки.",
        "Punkt „środka” jest wspólny dla odpowiadających sobie punktów.",
        "Точка «центра» спільна для відповідних точок.",
    ),
    (37, "przykłady"): T(
        "Symetryczne bywają figury i litery — ćwicz rozpoznawanie.",
        "Симетричними бувають фігури і літери — тренуй розпізнавання.",
        "Kwadrat, koło, litery H, O, X.",
        "Квадрат, коло, літери H, O, X.",
    ),
    (37, "rysowanie"): T(
        "Przy rysowaniu odbicia przenoś punkty prostopadle do osi, zachowując odległość.",
        "При малюванні відбиття перенось точки перпендикулярно до осі, зберігаючи відстань.",
        "Odległość od osi po obu stronach musi być równa.",
        "Відстань від осі з обох боків має бути рівною.",
    ),
    (37, "w przyrodzie"): T(
        "W przyrodzie symetria jest wszędzie — uczysz się ją dostrzegać.",
        "У природі симетрія всюди — вчишся її помічати.",
        "Motyl, liść, płatki kwiatu.",
        "Метелик, листок, пелюстки квітки.",
    ),

    # ——— 38 Współrzędne ———
    (38, "układ współrzędnych"): T(
        "Układ współrzędnych to „mapa” płaszczyzny z dwiema osiami — do opisu położenia punktów.",
        "Система координат — «карта» площини з двома осями — для опису положення точок.",
        "Osie: X (pozioma) i Y (pionowa).",
        "Осі: X (горизонтальна) і Y (вертикальна).",
    ),
    (38, "oś X"): T(
        "Oś X jest pozioma: w prawo wartości dodatnie, w lewo ujemne.",
        "Вісь X горизонтальна: праворуч додатні, ліворуч від'ємні.",
        "Najpierw czytamy x w parze (x, y).",
        "Спочатку читаємо x у парі (x, y).",
    ),
    (38, "oś Y"): T(
        "Oś Y jest pionowa: w górę +, w dół −.",
        "Вісь Y вертикальна: вгору +, вниз −.",
        "Druga współrzędna w (x, y) to y.",
        "Друга координата в (x, y) — y.",
    ),
    (38, "punkt (x, y)"): T(
        "Punkt zapisujemy parą liczb: najpierw x, potem y.",
        "Точку записуємо парою чисел: спочатку x, потім y.",
        "A(3, 2): 3 w prawo, 2 w górę. Nie zamieniaj kolejności!",
        "A(3, 2): 3 вправо, 2 вгору. Не міняй порядок!",
    ),
    (38, "ćwiartki"): T(
        "Płaszczyzna dzieli się na 4 ćwiartki — zależnie od znaków x i y.",
        "Площина ділиться на 4 чверті — залежно від знаків x і y.",
        "I: (+,+); II: (−,+); III: (−,−); IV: (+,−).",
        "I: (+,+); II: (−,+); III: (−,−); IV: (+,−).",
    ),
    (38, "początek układu"): T(
        "Początek układu to przecięcie osi — punkt O(0, 0).",
        "Початок координат — перетин осей — точка O(0, 0).",
        "Stąd zaczynamy odliczanie w prawo/lewo i góra/dół.",
        "Звідси починаємо відлік вправо/вліво і вгору/вниз.",
    ),

    # ——— 39 Statystyka (1) ———
    (39, "statystyka"): T(
        "Statystyka pomaga opisywać świat liczbami i wykresami oraz wyciągać wnioski.",
        "Статистика допомагає описувати світ числами і графіками та робити висновки.",
        "Dane → porządek → wykres → wniosek.",
        "Дані → порядок → графік → висновок.",
    ),
    (39, "dane"): T(
        "Dane to zebrane informacje: wyniki ankiet, pomiarów, obserwacji.",
        "Дані — зібрана інформація: результати опитувань, вимірів, спостережень.",
        "Bez danych nie ma statystyki — najpierw zbierz.",
        "Без даних немає статистики — спочатку збери.",
    ),
    (39, "etapy"): T(
        "Praca ze statystyką ma kolejne kroki — jak przepis.",
        "Робота зі статистикою має наступні кроки — як рецепт.",
        "Zbierz → uporządkuj → przedstaw → analizuj.",
        "Збери → упорядкуй → представ → аналізуй.",
    ),
    (39, "tabela"): T(
        "Tabela porządkuje dane w wierszach i kolumnach — łatwiej porównywać.",
        "Таблиця впорядковує дані в рядках і стовпцях — легше порівнювати.",
        "Najpierw tabela, potem wykres.",
        "Спочатку таблиця, потім графік.",
    ),
    (39, "wykres słupkowy"): T(
        "Wykres słupkowy porównuje kategorie: wysokość słupka = wartość.",
        "Стовпчикова діаграма порівнює категорії: висота стовпчика = значення.",
        "Dobry do „co większe / co mniejsze”.",
        "Добре для «що більше / що менше».",
    ),
    (39, "wykres kołowy"): T(
        "Wykres kołowy pokazuje części całości — jak kawałki tortu.",
        "Кругова діаграма показує частини цілого — як шматки торта.",
        "Suma udziałów = 100% (całość).",
        "Сума часток = 100% (ціле).",
    ),

    # ——— 40 Statystyka (2) ———
    (40, "mediana"): T(
        "Mediana to wartość środkowa po ustawieniu danych w kolejności.",
        "Медіана — середнє значення після впорядкування даних.",
        "Przy parzystej liczbie danych: średnia dwóch środkowych.",
        "При парній кількості даних: середнє двох середніх.",
    ),
    (40, "moda"): T(
        "Moda to wartość, która pojawia się najczęściej.",
        "Мода — значення, яке з'являється найчастіше.",
        "Może być więcej niż jedna moda — albo żadnej wyraźnej.",
        "Може бути більше однієї моди — або жодної виразної.",
    ),
    (40, "przykład średniej"): T(
        "Średnia: dodaj wszystkie wartości i podziel przez ich liczbę.",
        "Середнє: додай усі значення і поділи на їх кількість.",
        "(2+5+5+8)/4 = 5.",
        "(2+5+5+8)/4 = 5.",
    ),
    (40, "przykład mediany"): T(
        "Mediana: uporządkuj, weź środek.",
        "Медіана: упорядкуй, візьми середину.",
        "2,5,5,8 → środkowe 5 i 5 → mediana 5.",
        "2,5,5,8 → середні 5 і 5 → медіана 5.",
    ),
    (40, "przykład mody"): T(
        "Moda: szukaj najczęstszej wartości.",
        "Мода: шукай найчастіше значення.",
        "2,5,5,8 → moda = 5.",
        "2,5,5,8 → мода = 5.",
    ),

    # ——— 41 Kombinatoryka ———
    (41, "kombinatoryka"): T(
        "Kombinatoryka liczy, ile jest sposobów wyboru lub ułożenia.",
        "Комбінаторика рахує, скільки є способів вибору або впорядкування.",
        "Najpierw zrozum, czy kolejność ma znaczenie.",
        "Спочатку зрозумій, чи порядок має значення.",
    ),
    (41, "zasada mnożenia"): T(
        "Gdy etapy są niezależne, mnożymy liczby możliwości.",
        "Коли етапи незалежні, множимо числа можливостей.",
        "3 drogi · 4 autobusy = 12 sposobów.",
        "3 дороги · 4 автобуси = 12 способів.",
    ),
    (41, "zasada dodawania"): T(
        "Gdy wybieramy „albo… albo…” (wykluczające się opcje), dodajemy.",
        "Коли вибираємо «або… або…» (взаємовиключні варіанти), додаємо.",
        "Nie mnoż opcji, które się wykluczają.",
        "Не множ варіантів, які виключають одне одного.",
    ),
    (41, "permutacje"): T(
        "Permutacje to różne uporządkowania bez powtórzeń.",
        "Перестановки — різні впорядкування без повторень.",
        "n! = n·(n−1)·…·1. Np. 3! = 3·2·1 = 6.",
        "n! = n·(n−1)·…·1. Напр. 3! = 3·2·1 = 6.",
    ),
    (41, "przykład P"): T(
        "Na kostce każdy wynik 1–6 jest jednakowo możliwy.",
        "На кубику кожен результат 1–6 однаково можливий.",
        "P(6) = 1/6. Korzystne / wszystkie.",
        "P(6) = 1/6. Сприятливі / усі.",
    ),

    # ——— 42 Znaki ———
    (42, "+ plus / dodawanie"): T(
        "Znak + oznacza dodawanie — łączymy liczby.",
        "Знак + означає додавання — об'єднуємо числа.",
        "3 + 5. Czytamy: „plus” lub „dodać”.",
        "3 + 5. Читаємо: «плюс» або «додати».",
    ),
    (42, "− minus / odejmowanie"): T(
        "Znak − oznacza odejmowanie — zabieramy.",
        "Знак − означає віднімання — забираємо.",
        "9 − 4. Ten sam znak bywa przy liczbach ujemnych.",
        "9 − 4. Той самий знак буває біля від'ємних чисел.",
    ),
    (42, "× · mnożenie"): T(
        "Znak × lub · oznacza mnożenie.",
        "Знак × або · означає множення.",
        "4 × 3. Przy literach często piszemy 4a zamiast 4·a.",
        "4 × 3. Біля літер часто пишемо 4a замість 4·a.",
    ),
    (42, ": / dzielenie"): T(
        "Znak : lub / oznacza dzielenie.",
        "Знак : або / означає ділення.",
        "12 : 3. Ułamek a/b też jest dzieleniem.",
        "12 : 3. Дріб a/b теж є діленням.",
    ),
    (42, "= &lt; &gt; ≤ ≥ ≠"): T(
        "Znaki porównania mówią, jak liczby mają się do siebie.",
        "Знаки порівняння кажуть, як числа стосуються одне одного.",
        "= równe; < mniejsze; > większe; ≤ ≥; ≠ różne.",
        "= рівне; < менше; > більше; ≤ ≥; ≠ різне.",
    ),
    (42, "() [] √ ² % π ∠ ∥"): T(
        "Znaki specjalne skracają zapis trudniejszych pojęć.",
        "Спеціальні знаки скорочують запис складніших понять.",
        "() nawiasy; √ pierwiastek; ² potęga; % procent; π pi; ∠ kąt; ∥ równoległość.",
        "() дужки; √ корінь; ² степінь; % відсоток; π пі; ∠ кут; ∥ паралельність.",
    ),
}
