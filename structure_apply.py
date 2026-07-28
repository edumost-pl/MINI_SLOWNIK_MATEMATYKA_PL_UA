# -*- coding: utf-8 -*-
"""
Faza A: przestawienie istniejących tematów (source_n → nowy n).
Obrazy zostają pod starym numerem (asset_n = source_n).
Wordwall idzie za source_n.
"""

# nowy_n: stary_n, nowa_kategoria (litera), cat_pl, cat_ua
# Kolejność listy = kolejność w słowniku po przebudowie.
PHASE_A = [
    # A Liczby i orientacja
    (61, "A", "LICZBY", "ЧИСЛА"),
    (1, "A", "LICZBY", "ЧИСЛА"),
    (2, "A", "LICZBY", "ЧИСЛА"),
    (3, "A", "LICZBY", "ЧИСЛА"),
    # B Działania (+ algebra zostaje w B — bez nowej litery CSS)
    (4, "B", "DZIAŁANIA", "ДІЇ"),
    (5, "B", "DZIAŁANIA", "ДІЇ"),
    (6, "B", "DZIAŁANIA", "ДІЇ"),
    (7, "B", "DZIAŁANIA", "ДІЇ"),
    (43, "B", "DZIAŁANIA", "ДІЇ"),
    (44, "B", "DZIAŁANIA", "ДІЇ"),
    (8, "B", "DZIAŁANIA", "ДІЇ"),
    (45, "B", "DZIAŁANIA", "ДІЇ"),
    (13, "B", "DZIAŁANIA", "ДІЇ"),
    (53, "B", "DZIAŁANIA", "ДІЇ"),
    (14, "B", "DZIAŁANIA", "ДІЇ"),
    (54, "B", "DZIAŁANIA", "ДІЇ"),
    # C Ułamki, %, proporcje
    (9, "C", "UŁAMKI", "ДРОБИ"),
    (10, "C", "UŁAMKI", "ДРОБИ"),
    (11, "C", "UŁAMKI", "ДРОБИ"),
    (12, "C", "UŁAMKI", "ДРОБИ"),
    (46, "C", "UŁAMKI", "ДРОБИ"),
    (15, "C", "UŁAMKI", "ДРОБИ"),
    (52, "C", "UŁAMKI", "ДРОБИ"),
    (16, "C", "UŁAMKI", "ДРОБИ"),
    (56, "C", "UŁAMKI", "ДРОБИ"),
    # Algebra (w filtrze: B Działania)
    (17, "B", "DZIAŁANIA", "ДІЇ"),
    (18, "B", "DZIAŁANIA", "ДІЇ"),
    (55, "B", "DZIAŁANIA", "ДІЇ"),
    (19, "B", "DZIAŁANIA", "ДІЇ"),
    # E Geometria płaska (litera D w UI)
    (28, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (29, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (48, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (32, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (33, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (34, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (49, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (30, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (31, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (35, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (50, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (37, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (60, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (38, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (59, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (58, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (57, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    # Bryły
    (36, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    (51, "D", "GEOMETRIA", "ГЕОМЕТРІЯ"),
    # Miary
    (20, "E", "MIARY", "ВЕЛИЧИНИ"),
    (21, "E", "MIARY", "ВЕЛИЧИНИ"),
    (22, "E", "MIARY", "ВЕЛИЧИНИ"),
    (23, "E", "MIARY", "ВЕЛИЧИНИ"),
    (24, "E", "MIARY", "ВЕЛИЧИНИ"),
    (25, "E", "MIARY", "ВЕЛИЧИНИ"),
    (26, "E", "MIARY", "ВЕЛИЧИНИ"),
    (27, "E", "MIARY", "ВЕЛИЧИНИ"),
    (47, "E", "MIARY", "ВЕЛИЧИНИ"),
    # Dane
    (39, "F", "DANE", "ДАНІ"),
    (40, "F", "DANE", "ДАНІ"),
    (41, "F", "DANE", "ДАНІ"),
    # Powtórzenie
    (42, "F", "DANE", "ДАНІ"),
]


def apply_phase_a(pages: list) -> list:
    """Reorder first 61 topics; leave any extra pages (62+) appended after."""
    by_old = {}
    extras = []
    for p in pages:
        n = int(p["n"])
        if n <= 61 and n not in by_old:
            by_old[n] = p
        elif n > 61:
            extras.append(p)
        else:
            # duplicate old n — keep as extra
            extras.append(p)

    missing = [old for old, *_ in PHASE_A if old not in by_old]
    if missing:
        raise RuntimeError(f"Phase A: missing source pages: {missing}")

    out = []
    for new_i, (old, cat, cat_pl, cat_ua) in enumerate(PHASE_A, start=1):
        p = dict(by_old[old])  # shallow copy
        p["source_n"] = old
        p["asset_n"] = old
        p["n"] = new_i
        p["file"] = f"page{new_i:02d}.html"
        p["cat"] = cat
        p["cat_pl"] = cat_pl
        p["cat_ua"] = cat_ua
        out.append(p)

    # extras keep their n/file; ensure source_n/asset_n
    for p in extras:
        p = dict(p)
        p.setdefault("source_n", p["n"])
        p.setdefault("asset_n", p["n"])
        out.append(p)

    # renumber extras sequentially after 61 if needed
    next_n = len(PHASE_A) + 1
    final = []
    for p in out:
        if int(p["n"]) <= len(PHASE_A) and p.get("source_n") in {x[0] for x in PHASE_A}:
            # already set in loop above for phase A items
            if p["source_n"] in by_old and int(p["n"]) <= 61:
                final.append(p)
                continue
        # For extras that still have old high numbers from builder
        if p.get("_is_extra"):
            p["n"] = next_n
            p["file"] = f"page{next_n:02d}.html"
            next_n += 1
        final.append(p)

    # Simpler: rebuild final cleanly
    final = []
    for new_i, (old, cat, cat_pl, cat_ua) in enumerate(PHASE_A, start=1):
        p = dict(by_old[old])
        p["source_n"] = old
        p["asset_n"] = old
        p["n"] = new_i
        p["file"] = f"page{new_i:02d}.html"
        p["cat"] = cat
        p["cat_pl"] = cat_pl
        p["cat_ua"] = cat_ua
        final.append(p)

    next_n = len(PHASE_A) + 1
    for p in extras:
        p = dict(p)
        p.setdefault("source_n", int(p["n"]))
        p.setdefault("asset_n", int(p.get("asset_n") or p["n"]))
        p["n"] = next_n
        p["file"] = f"page{next_n:02d}.html"
        next_n += 1
        final.append(p)

    return final
