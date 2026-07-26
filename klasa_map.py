# -*- coding: utf-8 -*-
"""Mapowanie pojęć → klasy SP (przybliżenie wg podstawy programowej)."""

# Domyślna klasa dla całej strony (nadpisywalna na karcie: klasa=...)
PAGE_KLASA = {
    1: "klasy 1–3",
    2: "klasy 2–4",
    3: "klasy 4–6",
    4: "klasy 1–3",
    5: "klasy 2–3",
    6: "klasy 2–3",
    7: "klasy 4–6",
    8: "klasy 4–6",
    9: "klasy 4–5",
    10: "klasy 4–5",
    11: "klasy 4–6",
    12: "klasy 5–6",
    13: "klasy 5–7",
    14: "klasy 6–7",
    15: "klasy 5–7",
    16: "klasy 6–7",
    17: "klasy 6–7",
    18: "klasy 6–7",
    19: "klasy 6–7",
    20: "klasy 1–3",
    21: "klasy 1–3",
    22: "klasy 2–4",
    23: "klasy 1–3",
    24: "klasy 1–3",
    25: "klasy 2–4",
    26: "klasy 1–3",
    27: "klasy 5–7",
    28: "klasy 1–3",
    29: "klasy 3–5",
    30: "klasy 3–5",
    31: "klasy 6–7",
    32: "klasy 3–5",
    33: "klasy 3–5",
    34: "klasy 6–7",
    35: "klasy 4–6",
    36: "klasy 4–6",
    37: "klasy 3–5",
    38: "klasy 5–7",
    39: "klasy 4–6",
    40: "klasy 5–7",
    41: "klasy 6–8",
    42: "klasy 1–4",
    43: "klasy 3–5",
    44: "klasy 4–5",
    45: "klasy 4–6",
    46: "klasy 4–6",
    47: "klasy 4–5",
    48: "klasy 4–6",
    49: "klasy 4–6",
    50: "klasy 5–7",
    51: "klasy 5–8",
    52: "klasy 6–8",
    53: "klasy 7–8",
    54: "klasy 7–8",
    55: "klasy 7–8",
    56: "klasy 7–8",
    57: "klasy 7–8",
    58: "klasy 7–8",
    59: "klasy 7–8",
    60: "klasy 7–8",
    61: "klasy 1–3",
}

# Precyzyjniejsze nadpisania (nr_strony, hasło_pl) → klasa
CARD_KLASA = {
    (4, "odjemna i odjemnik"): "klasy 2–3",
    (4, "właściwości +"): "klasy 2–4",
    (4, "właściwości −"): "klasy 2–4",
    (12, "+/− ten sam mianownik"): "klasy 4–5",
    (12, "różne mianowniki"): "klasy 5–6",
    (12, "mnożenie"): "klasy 5–6",
    (12, "dzielenie"): "klasy 5–6",
    (12, "odwrotność"): "klasy 5–6",
    (12, "skracanie przed ×"): "klasy 5–6",
}


def resolve_klasa(page_n: int, term_pl: str, card=None) -> str:
    if card and (card.get("klasa") or "").strip():
        return card["klasa"].strip()
    key = (int(page_n), term_pl or "")
    if key in CARD_KLASA:
        return CARD_KLASA[key]
    return PAGE_KLASA.get(int(page_n), "klasy 1–8")
