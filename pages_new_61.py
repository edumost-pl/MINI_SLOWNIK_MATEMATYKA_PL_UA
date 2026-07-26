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
                "Na sobie: prawa ręka, lewa noga. Na obrazku: od strony, którą widzisz.",
                "На собі: права рука, ліва нога. На малюнку: з боку, який бачиш.",
                klasa="klasy 1–3",
                media="diagram",
            ),
            C(
                "góra / dół",
                "вгору / вниз",
                "↑ góra · ↓ dół",
                "Góra — ku niebu / dachowi. Dół — ku podłodze / ziemi.",
                "Вгору — до неба / даху. Вниз — до підлоги / землі.",
                klasa="klasy 1–3",
                media="diagram",
            ),
            C(
                "przed / za / obok",
                "перед / за / біля",
                "przed · za · obok",
                "Przed = bliżej Ciebie. Za = dalej, z tyłu. Obok = z boku.",
                "Перед = ближче до тебе. За = далі, ззаду. Біля = збоку.",
                klasa="klasy 1–3",
                media="cover",
            ),
            C(
                "dłuższy / krótszy",
                "довший / коротший",
                "——— dłuższy · — krótszy",
                "Porównujemy długość: kredka, linijka, szalik — która rzecz jest dłuższa?",
                "Порівнюємо довжину: олівець, лінійка, шарф — яка річ довша?",
                klasa="klasy 1–3",
                media="diagram",
            ),
            C(
                "cięższy / lżejszy",
                "важчий / легший",
                "⚖️ cięższy > lżejszy",
                "Porównujemy masę: książka bywa cięższa od piórnika.",
                "Порівнюємо масу: книжка буває важча за пенал.",
                klasa="klasy 1–3",
                media="cover",
            ),
            C(
                "więcej / mniej / tyle samo",
                "більше / менше / порівну",
                "●●●● > ●● · ●●● = ●●●",
                "Ile jest? Więcej, mniej, czy tyle samo — jak cukierki w dwóch miseczkach.",
                "Скільки є? Більше, менше чи порівну — як цукерки в двох мисочках.",
                klasa="klasy 1–3",
                media="diagram",
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
