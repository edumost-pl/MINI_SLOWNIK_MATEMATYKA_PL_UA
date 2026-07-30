# -*- coding: utf-8 -*-
"""Strona 61: Stosunki przestrzenne i porównywanie (kl. 1–3)."""


def C(pl, ua, visual, def_pl, def_ua, wide="", **kwargs):
    d = {"pl": pl, "ua": ua, "visual": visual, "def_pl": def_pl, "def_ua": def_ua, **kwargs}
    if wide:
        d["wide"] = wide
    return d


def R(pl, ua, formula=""):
    d = {"pl": pl, "ua": ua}
    if formula:
        d["formula"] = formula
    return d


def P(n, file, cat, cat_pl, cat_ua, title_pl, title_ua, intro_pl, intro_ua, tip_pl, tip_ua, cards, remember):
    return {
        "n": n, "file": file, "cat": cat, "cat_pl": cat_pl, "cat_ua": cat_ua,
        "title_pl": title_pl, "title_ua": title_ua,
        "intro_pl": intro_pl, "intro_ua": intro_ua,
        "tip_pl": tip_pl, "tip_ua": tip_ua,
        "cards": cards, "remember": remember,
    }


def build_page_61():
    return P(
        61,
        "page61.html",
        "D",
        "GEOMETRIA",
        "ГЕОМЕТРІЯ",
        "Stosunki przestrzenne i porównywanie",
        "Просторові відношення і порівняння",
        "Prawo/lewo, góra/dół, przed/za oraz porównywanie: dłuższy, cięższy, więcej",
        "Право/ліво, вгору/вниз, перед/за та порівняння: довший, важчий, більше",
        "Najpierw ustal, względem czego porównujesz!",
        "Спочатку з'ясуй, відносно чого порівнюєш!",
        [
            C(
                "prawo / lewo",
                "право / ліво",
                "👉 prawo · 👈 lewo",
                "Prawa i lewa strona — jak prawa i lewa ręka. Na rysunku patrzymy od strony postaci.",
                "Права і ліва сторона — як права і ліва рука. На малюнку дивимось з боку персонажа.",
                klasa="klasy 1–3",
                media="diagram",
                rule="👉 prawo · 👈 lewo",
                rule_ua="👉 право · 👈 ліво",
            ),
            C(
                "góra / dół",
                "вгорі / внизу",
                "↑ góra · ↓ dół",
                "Góra — wyżej (sufit, półka). Dół — niżej (podłoga).",
                "Вгорі — вище. Внизу — нижче.",
                klasa="klasy 1–3",
                media="diagram",
                rule="↑ góra · ↓ dół",
                rule_ua="↑ вгорі · ↓ внизу",
                nie_pomyl=[],
            ),
            C(
                "przed / za / obok",
                "перед / за / біля",
                "przed · za · obok",
                "Przed — bliżej przodu. Za — z tyłu. Obok — z boku, obok kogoś lub czegoś.",
                "Перед — ближче спереду. За — ззаду. Біля — збоку, поруч.",
                klasa="klasy 1–3",
                media="cover",
                rule="przed · za · obok",
                rule_ua="перед · за · біля",
            ),
            C(
                "dłuższy / krótszy",
                "довший / коротший",
                "——— dłuższy · — krótszy",
                "Dłuższy — ma większą długość. Krótszy — mniejszą. Porównujemy w tych samych jednostkach.",
                "Довший — має більшу довжину. Коротший — меншу. Порівнюємо в тих самих одиницях.",
                klasa="klasy 1–3",
                media="diagram",
                rule="dłuższy > krótszy",
                rule_ua="довший > коротший",
                nie_pomyl=[],
            ),
            C(
                "cięższy / lżejszy",
                "важчий / легший",
                "⚖️ cięższy > lżejszy",
                "Cięższy — ma większą masę. Lżejszy — mniejszą. Porównujemy na wadze lub „w ręku”.",
                "Важчий — має більшу масу. Легший — меншу. Порівнюємо на вагах або «в руці».",
                klasa="klasy 1–3",
                media="cover",
                rule="cięższy > lżejszy",
                rule_ua="важчий > легший",
                nie_pomyl=[],
            ),
            C(
                "więcej / mniej / tyle samo",
                "більше / менше / порівну",
                "●●●● > ●● · ●●● = ●●●",
                "Więcej — większa liczba. Mniej — mniejsza. Tyle samo — równo (po równo).",
                "Більше — більше число. Менше — менше. Порівну — стільки ж.",
                klasa="klasy 1–3",
                media="diagram",
                rule="więcej · mniej · tyle samo",
                rule_ua="більше · менше · порівну",
                nie_pomyl=[],
            ),
        ],
        [
            R(
                "Najpierw ustal, względem czego porównujesz (siebie, obrazek, drugą rzecz).",
                "Спочатку з'ясуй, відносно чого порівнюєш (себе, малюнок, іншу річ).",
            ),
            R(
                "Prawo/lewo na sobie ≠ zawsze to samo na obrazku — sprawdź!",
                "Право/ліво на собі ≠ завжди те саме на малюнку — перевір!",
            ),
            R(
                "Porównuj w tej samej „jednostce”: długość z długością, ciężar z ciężarem.",
                "Порівнюй у тій самій «одиниці»: довжину з довжиною, вагу з вагою.",
            ),
        ],
    )
