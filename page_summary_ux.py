# -*- coding: utf-8 -*-
"""
Dolne bloki strony EduMost:
  1) Częste błędy — ❌ → ✅
  2) Najważniejsze pojęcia, reguły i wzory — ściąga 5–8 pozycji
Prezentacja z istniejącej treści (remember, mistake, karty) — bez zmiany UX.
"""
from __future__ import annotations

import re
from html import escape as esc

from card_ux import nie_pomyl, present_card, _strip_html, _sentences


def _short(s: str, n: int = 72) -> str:
    s = _strip_html(s)
    if len(s) <= n:
        return s
    return s[: n - 1].rsplit(" ", 1)[0] + "…"


_SKIP_MISTAKE = re.compile(
    r"\(PL\)|\(UA\)|patrz przykłady|na oko|zgaduj|pytaj nauczyciela|"
    r"porównaj blok|sprawdź regułę / wzór|mieszam podobne nazwy|"
    r"liceum|ліцей|punkt procentowy",
    re.I,
)

_META_CARD = {"przykłady", "przykład", "w życiu", "znaki", "elementy", "krok po kroku"}

_CHEAT_SKIP = re.compile(
    r"pytaj nauczyciela|na oko|powtórz kart|zgaduj|wokół siebie|dach, drzwi|"
    r"rozpoznaj w otoczeniu|to start|wiesz, co oznacza|co oznacza każda|"
    r"liceum|ліцей|wzór do zapamiętania|wzór egzaminacyjny|"
    r"sprawdź znaczenie każdej|формула для|patrz przykłady|"
    r"\(PL\)|\(UA\)|najpierw znajdź|sprawdź jednostkami|"
    r"nazwij:|cel: niewiadoma",
    re.I,
)


def _parse_mistake_text(pl: str) -> list[tuple[str, str]]:
    """Spróbuj wyciągnąć pary błąd/poprawnie z akapitu mistake_pl."""
    pl = _strip_html(pl)
    if not pl:
        return []
    pairs: list[tuple[str, str]] = []

    # „Mylą A z/ze B” / „mylą A z B lub C”
    for m in re.finditer(
        r"[Mm]yl[ąa]\s+(.+?)\s+(?:z|ze)\s+(.+?)(?:\.|;|$)",
        pl,
    ):
        a = _short(m.group(1), 36)
        rest = m.group(2)
        parts = re.split(r"\s+(?:lub|albo|czy)\s+(?:z|ze)?\s*", rest)
        for part in parts[:2]:
            b = _short(re.split(r",|;", part)[0], 36)
            b = re.sub(r"^(z|ze)\s+", "", b, flags=re.I)
            # „stożkiem” → „stożek” (prosta normalizacja końcówek)
            b = re.sub(r"(kiem|kiem)$", "k", b)
            b = re.sub(r"iem$", "", b) if b.endswith("iem") else b
            b = re.sub(r"ą$", "a", b)
            if a and b and len(b) > 1:
                pairs.append((f"{a} = {b}", f"{a} ≠ {b}"))

    # „zapominają o X” / „zapominają, że Y”
    for m in re.finditer(r"zapominaj[ąa](?:\s+o)?\s+(.+?)(?:\.|;|$)", pl, flags=re.I):
        frag = _short(m.group(1), 48)
        if frag:
            pairs.append((f"Bez: {frag}", frag))

    for m in re.finditer(
        r"(?:pisz[ąa]|myśl[ąa]|mówi[ąa]|bior[ąa]|traktuj[ąa])\s+(.+?)\s+(?:zamiast|jak)\s+(.+?)(?:\.|;|$)",
        pl,
        flags=re.I,
    ):
        pairs.append((_short(m.group(1), 40), _short(m.group(2), 40)))

    for m in re.finditer(
        r"([^.;]+?)\s+(?:to nie to samo co|≠)\s+([^.;]+)",
        pl,
        flags=re.I,
    ):
        a, b = _short(m.group(1), 36), _short(m.group(2), 36)
        pairs.append((f"{a} = {b}", f"{a} ≠ {b}"))

    # „A to nie B” (bez „i nie C” w środku — bierz pierwsze B)
    for m in re.finditer(
        r"([^.;]+?)\s+to nie\s+([^.;]+?)(?:\s+i nie\s+|\.|$)",
        pl,
        flags=re.I,
    ):
        a, b = _short(m.group(1), 36), _short(m.group(2), 36)
        if a and b and "≠" not in a:
            pairs.append((f"{a} = {b}", f"{a} ≠ {b}"))

    for m in re.finditer(
        r"nie\s+([^,—;]+?)(?:\s*[—,]\s*|\s+tylko\s+)([^.;]+)",
        pl,
        flags=re.I,
    ):
        pairs.append((_short(m.group(1), 40), _short(m.group(2), 40)))

    for m in re.finditer(
        r"([^.;]+?)\s+to\s+([^,;]+),\s*nie\s+([^.;]+)",
        pl,
        flags=re.I,
    ):
        ctx, good, bad = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
        pairs.append((f"{_short(ctx, 20)} → {bad}", f"{_short(ctx, 20)} → {good}"))

    out, seen = [], set()
    for w, r in pairs:
        if _SKIP_MISTAKE.search(w) or _SKIP_MISTAKE.search(r):
            continue
        key = (w.lower(), r.lower())
        if key in seen or not w or not r:
            continue
        seen.add(key)
        out.append((w, r))
    return out[:5]


def _mistakes_from_cards(page: dict) -> list[tuple[str, str]]:
    """Z bloków „Nie pomyl” na kartach — odwróć do typowego błędu."""
    pairs: list[tuple[str, str]] = []
    for c in page.get("cards") or []:
        term = (c.get("pl") or "").strip().lower()
        if term in _META_CARD:
            continue
        for a, b in nie_pomyl(c):
            if not a or not b:
                continue
            if _SKIP_MISTAKE.search(a) or _SKIP_MISTAKE.search(b):
                continue
            if a.lower().startswith("mylę ") or "sprawdź definic" in b.lower():
                continue
            if "coś innego" in a.lower() or "coś innego" in b.lower():
                continue
            if "≠" in a or "≠" in b:
                left = a.replace("≠", "=") if "≠" in a else b.replace("≠", "=")
                right = a if "≠" in a else b
                pairs.append((_short(left, 42), _short(right, 42)))
                continue
            if "→" in a and "→" in b:
                a_l, a_r = [x.strip() for x in a.split("→", 1)]
                b_l, b_r = [x.strip() for x in b.split("→", 1)]
                if a_l and a_r and b_r and a_r != b_r:
                    pairs.append((f"{a_l} = {b_r}", f"{a_l} = {a_r}"))
                continue
            if "=" in a and "=" in b and "→" not in a:
                a_l, a_r = [x.strip() for x in a.split("=", 1)]
                b_l, b_r = [x.strip() for x in b.split("=", 1)]
                if a_l and b_r and a_r != b_r:
                    pairs.append((f"{a_l} = {b_r}", a))
                continue
            if len(a) <= 40 and len(b) <= 40 and not a.startswith("="):
                # pomiń pary typu „X” / „nie Y” (słabo czytelne jako ❌→✅)
                if b.lower().startswith("nie ") or a.lower().startswith("nie "):
                    continue
                pairs.append((f"{a} = {b}", f"{a} ≠ {b}"))
    out, seen = [], set()
    for w, r in pairs:
        w, r = _short(w, 44), _short(r, 44)
        if not w or not r or w.lower() == r.lower():
            continue
        if w.startswith("=") or r.startswith("="):
            continue
        if _SKIP_MISTAKE.search(w) or _SKIP_MISTAKE.search(r):
            continue
        key = (w.lower(), r.lower())
        if key in seen:
            continue
        seen.add(key)
        out.append((w, r))
        if len(out) >= 5:
            break
    return out


def _mistakes_from_remember(page: dict) -> list[tuple[str, str]]:
    """Z reguł typu „A ≠ B” w remember (tylko z spacjami wokół ≠ — nie b≠0)."""
    pairs = []
    for r in page.get("remember") or []:
        for text in (r.get("pl") or "", r.get("formula") or ""):
            text = _strip_html(text)
            if " ≠ " not in text:
                continue
            for m in re.finditer(r"([^≠;.]{2,40}?)\s+≠\s+([^≠;.]{2,40})", text):
                left = m.group(1).strip().rstrip(".")
                right = m.group(2).strip().rstrip(".")
                # pomiń fragmenty wzorów typu „b ≠ 0”
                if re.fullmatch(r"[a-zA-Z]\s*", left) and re.fullmatch(r"\d+\s*", right):
                    continue
                if left and right and not _SKIP_MISTAKE.search(left + right):
                    pairs.append((f"{left} = {right}", f"{left} ≠ {right}"))
    return pairs


def mistake_pairs(page: dict) -> list[tuple[str, str]]:
    """2–5 par ❌ błąd → ✅ poprawnie."""
    pairs = _parse_mistake_text(page.get("mistake_pl") or "")
    if len(pairs) < 2:
        for w, r in _mistakes_from_cards(page):
            if (w.lower(), r.lower()) not in {(x.lower(), y.lower()) for x, y in pairs}:
                pairs.append((w, r))
            if len(pairs) >= 5:
                break
    if len(pairs) < 2:
        for w, r in _mistakes_from_remember(page):
            if (w.lower(), r.lower()) not in {(x.lower(), y.lower()) for x, y in pairs}:
                pairs.append((w, r))
            if len(pairs) >= 5:
                break

    cleaned = []
    for w, r in pairs:
        if _SKIP_MISTAKE.search(w) or _SKIP_MISTAKE.search(r):
            continue
        if w.startswith("=") or len(w) < 3:
            continue
        cleaned.append((w, r))
    pairs = cleaned

    if len(pairs) < 2:
        cards = [c for c in (page.get("cards") or []) if (c.get("pl") or "").lower() not in _META_CARD]
        if len(cards) >= 2:
            a = (cards[0].get("pl") or "").strip()
            b = (cards[1].get("pl") or "").strip()
            if a and b:
                pairs = [
                    (f"{a} = {b}", f"{a} ≠ {b}"),
                    (f"Zła definicja: {a}", f"Sprawdź kartę: {a}"),
                ]
        elif cards:
            a = (cards[0].get("pl") or page.get("title_pl") or "pojęcie").strip()
            pairs = [
                (f"Zły wzór przy: {a}", f"Sprawdź kartę: {a}"),
                (f"Zła jednostka / znak przy: {a}", "Porównaj przykłady na karcie"),
            ]
        else:
            title = page.get("title_pl") or "temat"
            pairs = [
                (f"Mylę pojęcia z tematu: {title}", "Sprawdź definicje na kartach"),
                ("Zły wzór lub jednostka", "Sprawdź ściągę na dole strony"),
            ]
    return pairs[:5]


def cheat_items(page: dict) -> list[str]:
    """5–8 krótkich pozycji ściągi (wzór / reguła / pojęcie)."""
    items: list[str] = []
    seen: set[str] = set()

    def add(s: str) -> None:
        s = _strip_html(s)
        if not s or s in {"…", "—", "..."}:
            return
        if _CHEAT_SKIP.search(s):
            return
        if s.startswith("…"):
            return
        s = re.sub(r"\s+", " ", s).strip()
        if len(s) > 90:
            s = _sentences(s, 1)
            if len(s) > 90:
                s = s[:87].rsplit(" ", 1)[0] + "…"
        key = s.lower()
        if key in seen:
            return
        seen.add(key)
        items.append(s)

    for r in page.get("remember") or []:
        formula = (r.get("formula") or "").strip()
        pl = (r.get("pl") or "").strip()
        if formula and not _CHEAT_SKIP.search(formula):
            add(formula)
        elif pl and not _CHEAT_SKIP.search(pl):
            if "co oznacza" not in pl.lower() and "що означає" not in pl.lower():
                add(_sentences(pl, 1))

    for c in page.get("cards") or []:
        term = (c.get("pl") or "").strip().lower()
        if term in _META_CARD:
            continue
        ux = present_card(c)
        zap = ux.get("zap_pl") or ""
        if zap and len(zap) <= 70:
            add(zap)
        elif zap:
            add(_sentences(zap, 1))
        for a, b in nie_pomyl(c)[:1]:
            if not a or not b:
                continue
            if _SKIP_MISTAKE.search(a) or _SKIP_MISTAKE.search(b):
                continue
            if "≠" in (a + b):
                add(a if "≠" in a else b)
            elif len(a) < 28 and len(b) < 28:
                add(f"{a} ≠ {b}")
        if len(items) >= 8:
            break

    if len(items) < 5:
        for c in page.get("cards") or []:
            term = (c.get("pl") or "").strip()
            vis = _strip_html(c.get("visual") or "")
            if term.lower() in _META_CARD:
                continue
            if term and vis and len(vis) <= 48:
                add(f"{term}: {vis}")
            elif term:
                add(term)
            if len(items) >= 5:
                break

    while len(items) < 5:
        t = (page.get("title_pl") or "Temat").strip()
        add(t)
        add(_sentences(page.get("intro_pl") or t, 1))
        break

    # pad still short
    i = 0
    cards = page.get("cards") or []
    while len(items) < 5 and i < len(cards):
        add((cards[i].get("pl") or "").strip())
        i += 1

    return items[:8]


def render_mistake_section(page: dict) -> str:
    pairs = mistake_pairs(page)
    rows = []
    for wrong, right in pairs:
        rows.append(
            '<div class="mb-pair">'
            f'<div class="mb-wrong"><span class="mb-ico" aria-hidden="true">❌</span> '
            f'<span class="mb-lab">Błąd</span> <span class="mb-txt">{esc(wrong)}</span></div>'
            '<div class="mb-arrow" aria-hidden="true">↓</div>'
            f'<div class="mb-right"><span class="mb-ico" aria-hidden="true">✅</span> '
            f'<span class="mb-lab">Poprawnie</span> <span class="mb-txt">{esc(right)}</span></div>'
            "</div>"
        )
    body = "\n      ".join(rows)
    return f'''
    <section class="mistake-box mistake-box--ux" aria-label="Częste błędy">
      <div class="mistake-head">⚠ Częste błędy <span class="ua">Часті помилки</span></div>
      <div class="mistake-body mistake-body--ux">
      {body}
      </div>
    </section>'''


def render_cheat_section(page: dict) -> str:
    items = cheat_items(page)
    lis = "\n        ".join(
        f'<li><span class="cheat-n">{i}</span><span class="cheat-txt">{esc(t)}</span></li>'
        for i, t in enumerate(items, 1)
    )
    return f'''
    <section class="remember rules-box cheat-box" aria-label="Najważniejsze pojęcia, reguły i wzory">
      <div class="remember-head rules-head">
        <span class="rules-badge">ŚCIĄGA</span>
        <div class="rules-head-text">
          <strong>⭐ Najważniejsze pojęcia, reguły i wzory</strong>
          <span class="ua">Найважливіші поняття, правила та формули</span>
        </div>
      </div>
      <ol class="cheat-list">
        {lis}
      </ol>
    </section>'''
