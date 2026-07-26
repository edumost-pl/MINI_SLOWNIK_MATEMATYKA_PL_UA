# -*- coding: utf-8 -*-
"""
Mapa pokrycia Mini-słownika względem podstawy programowej matematyki SP (kl. 1–8).
Źródło: MEN / ZPE — treści nauczania (aktualna podstawa, etapy I–II).

Status (po rozbudowie do 60 stron, lipiec 2026):
  covered  — jest osobna strona lub wyraźne hasło
  partial  — jest fragmentarycznie (w innym haśle)
  gap      — brak w słowniku (warto dodać)
  optional — poza wąską podstawą 2024 / uzupełnienie (można mieć)

Słownik: 60 stron · ~359 haseł.
"""

from __future__ import annotations

# (dział PP, temat, klasy, status, gdzie_w_słowniku, uwagi)
CURRICULUM = [
    # ——— I etap: klasy 1–3 ———
    ("I·1–3", "Stosunki przestrzenne (prawo/lewo, pion, poziom, skos)", "1–3", "gap", "—", "Edukacja wczesnoszkolna — opcjonalne hasło"),
    ("I·1–3", "Porównywanie wielkości (dłuższy, cięższy, więcej)", "1–3", "partial", "20, 21", "Jest przy miarach, brak osobnego hasła „porównanie wielkości”"),
    ("I·1–3", "Liczby naturalne 0–1000 (+ wybrane większe)", "1–3", "covered", "01", ""),
    ("I·1–3", "Cyfry, wartość pozycyjna, liczby porządkowe", "1–3", "partial", "01", "Brak osobnego hasła „liczba porządkowa”"),
    ("I·1–3", "Porównywanie i porządkowanie liczb (< = >)", "1–3", "covered", "01", ""),
    ("I·1–3", "Dodawanie i odejmowanie", "1–3", "covered", "04", ""),
    ("I·1–3", "Tabliczka mnożenia", "1–3", "covered", "05", ""),
    ("I·1–3", "Dzielenie (także z resztą)", "1–3", "covered", "06", ""),
    ("I·1–3", "Zegar i upływ czasu", "1–3", "covered", "23", ""),
    ("I·1–3", "Kalendarz", "1–3", "covered", "24", ""),
    ("I·1–3", "Pieniądze (zł, gr)", "1–3", "covered", "26", ""),
    ("I·1–3", "Figury w otoczeniu (rozpoznawanie)", "1–3", "partial", "28, 29", "Jest później; brak osobnej strony „figury wokół nas” dla 1–3"),
    ("I·1–3", "Mierzenie długości / masy (praktyka)", "1–3", "covered", "20, 21", ""),

    # ——— II etap: klasy 4–6 ———
    ("II·4–6", "Liczby naturalne wielocyfrowe, oś liczbowa", "4–6", "covered", "01, 03", ""),
    ("II·4–6", "Zaokrąglanie liczb naturalnych", "4–6", "covered", "01", ""),
    ("II·4–6", "Liczby rzymskie (do 3000)", "4–6", "covered", "02", ""),
    ("II·4–6", "Działania na liczbach naturalnych (+ − × :)", "4–6", "covered", "04, 05, 06", ""),
    ("II·4–6", "Działania pisemne", "4–6", "covered", "43", ""),
    ("II·4–6", "Przemienność, łączność, rozdzielność", "4–6", "covered", "04, 05, 44", ""),
    ("II·4–6", "Kolejność działań", "4–6", "covered", "07", ""),
    ("II·4–6", "Szacowanie wyników", "4–6", "covered", "43", ""),
    ("II·4–6", "Cechy podzielności (2,3,4,5,9,10,100)", "4–6", "partial", "08", "Brak osobnego hasła „przez 100”"),
    ("II·4–6", "Dzielnik, wielokrotność", "4–6", "covered", "08", ""),
    ("II·4–6", "Liczba pierwsza i złożona", "4–6", "covered", "08, 45", ""),
    ("II·4–6", "Rozkład na czynniki pierwsze", "4–6", "covered", "45", ""),
    ("II·4–6", "NWD i NWW", "4–6", "covered", "45", ""),
    ("II·4–6", "Dzielenie z resztą (a = b·q + r)", "4–6", "covered", "06", ""),
    ("II·4–6", "Kwadraty i sześciany liczb naturalnych", "4–6", "covered", "13, 54", ""),
    ("II·4–6", "Liczby całkowite, wartość bezwzględna", "4–6", "covered", "03", ""),
    ("II·4–6", "Ułamki zwykłe — pojęcie, licznik, mianownik", "4–6", "covered", "09", ""),
    ("II·4–6", "Skracanie, rozszerzanie, wspólny mianownik", "4–6", "covered", "10", ""),
    ("II·4–6", "Liczba mieszana ↔ ułamek niewłaściwy", "4–6", "covered", "09", ""),
    ("II·4–6", "Ułamki dziesiętne, zamiany", "4–6", "covered", "11", ""),
    ("II·4–6", "Wyrażenia dwumianowane (2 m 15 cm)", "4–6", "covered", "47", ""),
    ("II·4–6", "Działania na ułamkach zwykłych i dziesiętnych", "4–6", "covered", "12, 11", ""),
    ("II·4–6", "Ułamek danej liczby / całość z części", "4–6", "covered", "46", ""),
    ("II·4–6", "Powiększenie / pomniejszenie o część", "4–6", "covered", "46", ""),
    ("II·4–6", "Proste wyrażenia literowe, proste równania", "4–6", "partial", "17, 19", "Równania „przez zgadywanie” — OK częściowo"),
    ("II·4–6", "Punkt, prosta, półprosta, odcinek", "4–6", "covered", "28", ""),
    ("II·4–6", "Proste / odcinki prostopadłe (⊥)", "4–6", "covered", "48", ""),
    ("II·4–6", "Proste / odcinki równoległe (∥)", "4–6", "covered", "34", ""),
    ("II·4–6", "Odległość punktu od prostej", "4–6", "covered", "48", ""),
    ("II·4–6", "Kąty: pojęcie, miara, rodzaje, kątomierz", "4–6", "covered", "32, 33", ""),
    ("II·4–6", "Kąty przyległe i wierzchołkowe", "4–6", "covered", "34", ""),
    ("II·4–6", "Trójkąty — rodzaje (boki i kąty)", "4–6", "covered", "29", ""),
    ("II·4–6", "Suma kątów w trójkącie (180°)", "4–6", "covered", "49", ""),
    ("II·4–6", "Konstrukcja trójkąta z 3 boków / nierówność trójkąta", "4–6", "covered", "49", ""),
    ("II·4–6", "Czworokąty: kwadrat, prostokąt, romb, równoległobok, trapez", "4–6", "covered", "29", ""),
    ("II·4–6", "Koło i okrąg (środek, r, d, cięciwa)", "4–6", "covered", "30", ""),
    ("II·4–6", "Obwód i pole figur płaskich", "4–6", "covered", "35, 50", ""),
    ("II·4–6", "Jednostki pola (ar, hektar)", "4–6", "covered", "50", ""),
    ("II·4–6", "Bryły: rozpoznawanie, siatki", "4–6", "covered", "36, 51", ""),
    ("II·4–6", "Objętość i pole powierzchni prostopadłościanu", "4–6", "covered", "22, 36, 51", ""),
    ("II·4–6", "Procenty podstawowe (1%, 10%, 25%, 50%)", "4–6", "covered", "15", ""),
    ("II·4–6", "Czas, kalendarz, temperatura, długość, masa", "4–6", "covered", "20–25", ""),
    ("II·4–6", "Skala mapy, prędkość s=v·t", "4–6", "covered", "27", ""),
    ("II·4–6", "Statystyka: dane, tabele, wykresy", "4–6", "covered", "39", ""),
    ("II·4–6", "Zadania tekstowe (strategie)", "4–6", "gap", "—", "Umiejętność, nie hasło — opcjonalna strona metodyczna"),

    # ——— II etap: klasy 7–8 ———
    ("II·7–8", "Potęgi (także o podstawie wymiernej)", "7–8", "covered", "13", ""),
    ("II·7–8", "Potęga potęgi; potęgi o różnych podstawach", "7–8", "covered", "53", ""),
    ("II·7–8", "Notacja wykładnicza a·10ᵏ", "7–8", "covered", "53", ""),
    ("II·7–8", "Pierwiastek kwadratowy", "7–8", "covered", "14", ""),
    ("II·7–8", "Pierwiastek sześcienny", "7–8", "covered", "54", ""),
    ("II·7–8", "Działania na pierwiastkach (wyłączanie/włączanie)", "7–8", "covered", "54", ""),
    ("II·7–8", "Wyrażenia algebraiczne wielu zmiennych", "7–8", "covered", "17", ""),
    ("II·7–8", "Sumy algebraiczne, redukcja", "7–8", "covered", "18", ""),
    ("II·7–8", "Mnożenie sumy przez jednomian; dwumian × dwumian", "7–8", "covered", "55", ""),
    ("II·7–8", "Obliczenia procentowe (wszystkie typy)", "7–8", "covered", "15, 52", ""),
    ("II·7–8", "Równania I stopnia (metoda równań równoważnych)", "7–8", "covered", "19", ""),
    ("II·7–8", "Przekształcanie wzorów (v, s, t, pola…)", "7–8", "partial", "19, 27", "Warto osobne hasło"),
    ("II·7–8", "Proporcjonalność prosta", "7–8", "covered", "16", ""),
    ("II·7–8", "Podział proporcjonalny", "7–8", "covered", "56", ""),
    ("II·7–8", "Kąty przy prostych równoległych", "7–8", "covered", "34", ""),
    ("II·7–8", "Cechy przystawania trójkątów", "7–8", "covered", "58", ""),
    ("II·7–8", "Twierdzenie Pitagorasa", "7–8", "covered", "57", ""),
    ("II·7–8", "Wielokąt foremny", "7–8", "gap", "—", "Pojęcie z PP — krótka strona wystarczy"),
    ("II·7–8", "Pola figur — wzory zaawansowane (romb, trapez)", "7–8", "covered", "35, 50", ""),
    ("II·7–8", "Układ współrzędnych", "7–8", "covered", "38", ""),
    ("II·7–8", "Środek i długość odcinka we współrzędnych", "7–8", "covered", "59", ""),
    ("II·7–8", "Geometria przestrzenna: graniastosłup, ostrosłup — V i P", "7–8", "covered", "36, 51", "Ostrosłup — głównie rozpoznanie; V/P prostopadłościanu i graniastosłupa OK"),
    ("II·7–8", "Kombinatoryka (proste zliczanie)", "7–8", "covered", "41", "Uwaga: zaawansowane metody usunięto w 2024"),
    ("II·7–8", "Prawdopodobieństwo (doświadczenia losowe)", "7–8", "covered", "41", ""),
    ("II·7–8", "Statystyka: średnia; diagramy; wykresy", "7–8", "covered", "39, 40", "Mediana/moda — ponad minimum PP (OK jako rozszerzenie)"),
    ("II·7–8", "Długość okręgu i pole koła (π)", "7–8", "covered", "31", ""),
    ("II·7–8", "Symetria osiowa i środkowa", "7–8", "covered", "37", "Może być po egzaminie 8-klasisty"),
    ("II·7–8", "Symetralna odcinka, dwusieczna kąta", "7–8", "covered", "60", ""),
]

# Zrealizowane strony 43–60 (wcześniej: PROPOSED_NEW_PAGES)
IMPLEMENTED_PAGES_43_60 = [
    {"n": 43, "title_pl": "Działania pisemne i szacowanie"},
    {"n": 44, "title_pl": "Rozdzielność mnożenia"},
    {"n": 45, "title_pl": "NWD, NWW i rozkład na czynniki"},
    {"n": 46, "title_pl": "Ułamek liczby i całość z części"},
    {"n": 47, "title_pl": "Wyrażenia dwumianowane"},
    {"n": 48, "title_pl": "Proste prostopadłe i odległość"},
    {"n": 49, "title_pl": "Suma kątów w trójkącie"},
    {"n": 50, "title_pl": "Pole rombu i trapezu; ar, ha"},
    {"n": 51, "title_pl": "Graniastosłup, siatki, pole powierzchni"},
    {"n": 52, "title_pl": "Obliczenia procentowe — wszystkie typy"},
    {"n": 53, "title_pl": "Notacja wykładnicza i potęga potęgi"},
    {"n": 54, "title_pl": "Pierwiastek sześcienny i działania na √"},
    {"n": 55, "title_pl": "Mnożenie wyrażeń algebraicznych"},
    {"n": 56, "title_pl": "Podział proporcjonalny"},
    {"n": 57, "title_pl": "Twierdzenie Pitagorasa"},
    {"n": 58, "title_pl": "Przystawanie trójkątów"},
    {"n": 59, "title_pl": "Środek i długość odcinka"},
    {"n": 60, "title_pl": "Symetralna i dwusieczna"},
]

# Opcjonalne uzupełnienia (niekrytyczne względem PP)
OPTIONAL_REMAINING = [
    {"title_pl": "Stosunki przestrzenne (prawo/lewo…)", "klasy": "1–3", "priorytet": "niski"},
    {"title_pl": "Zadania tekstowe — strategie", "klasy": "4–6", "priorytet": "średni (metodyka)"},
    {"title_pl": "Wielokąt foremny", "klasy": "7–8", "priorytet": "niski"},
    {"title_pl": "Podzielność przez 100", "klasy": "4–5", "priorytet": "niski (dopisek do s. 08)"},
    {"title_pl": "Przekształcanie wzorów", "klasy": "7–8", "priorytet": "średni"},
    {"title_pl": "Liczba porządkowa / figury wokół nas", "klasy": "1–3", "priorytet": "niski"},
]

# Legacy alias (puste — wszystko z listy wdrożone)
PROPOSED_NEW_PAGES = []


def summary():
    from collections import Counter

    c = Counter(row[3] for row in CURRICULUM)
    return {
        "total": len(CURRICULUM),
        "covered": c["covered"],
        "partial": c["partial"],
        "gap": c["gap"],
        "optional": c.get("optional", 0),
        "pages_dict": 60,
        "implemented_43_60": len(IMPLEMENTED_PAGES_43_60),
        "optional_remaining": len(OPTIONAL_REMAINING),
        "proposed_pages": 0,
    }


if __name__ == "__main__":
    s = summary()
    print(
        f"Tematy PP: {s['total']} | covered {s['covered']} | partial {s['partial']} | gap {s['gap']}"
    )
    print(f"Pokrycie covered+partial: {100*(s['covered']+s['partial'])/s['total']:.0f}%")
    print(f"Strony 43–60 wdrożone: {s['implemented_43_60']}")
    print("\n=== LUKI (gap) ===")
    for row in CURRICULUM:
        if row[3] == "gap":
            print(f"  [{row[2]}] {row[1]} — {row[5]}")
    print("\n=== CZĘŚCIOWE (partial) ===")
    for row in CURRICULUM:
        if row[3] == "partial":
            print(f"  [{row[2]}] {row[1]} → {row[4]} — {row[5]}")
