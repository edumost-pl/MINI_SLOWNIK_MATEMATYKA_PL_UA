# -*- coding: utf-8 -*-
"""Child-friendly inline SVG illustrations for mini-dictionary cards."""

def svg(inner, w=220, h=100, view=None):
    vb = view or f"0 0 {w} {h}"
    return (
        f'<svg class="fig-svg" viewBox="{vb}" width="100%" height="auto" '
        f'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">{inner}</svg>'
    )

def apples(n=5, filled=None):
    filled = n if filled is None else filled
    parts = []
    for i in range(n):
        x = 18 + i * 38
        color = "#2e9b57" if i < filled else "#d7e0ee"
        parts.append(
            f'<circle cx="{x}" cy="48" r="16" fill="{color}"/>'
            f'<ellipse cx="{x+6}" cy="34" rx="5" ry="8" fill="#7bc96f" opacity=".5"/>'
            f'<path d="M{x} 30 Q{x+4} 18 {x+10} 22" stroke="#5a3a1a" fill="none" stroke-width="2"/>'
        )
    return svg("".join(parts), 20 + n * 38, 90)

def dots_row(n, color="#1e4f9c"):
    parts = []
    for i in range(n):
        parts.append(f'<circle cx="{20+i*28}" cy="50" r="11" fill="{color}"/>')
    return svg("".join(parts), max(40, 10 + n * 28), 90)

def add_dots(a=3, b=5):
    parts = []
    for i in range(a):
        parts.append(f'<circle cx="{18+i*22}" cy="40" r="9" fill="#1e4f9c"/>')
    parts.append(f'<text x="{18+a*22+8}" y="46" font-size="22" font-weight="800" fill="#1e4f9c">+</text>')
    x0 = 18 + a * 22 + 30
    for i in range(b):
        parts.append(f'<circle cx="{x0+i*22}" cy="40" r="9" fill="#e67e22"/>')
    parts.append(f'<text x="{x0+b*22+8}" y="46" font-size="22" font-weight="800" fill="#2e9b57">=</text>')
    x1 = x0 + b * 22 + 36
    for i in range(a + b):
        parts.append(f'<circle cx="{x1+i*18}" cy="40" r="8" fill="#2e9b57"/>')
    return svg("".join(parts), x1 + (a + b) * 18 + 20, 80)

def sub_dots(a=9, b=4):
    parts = []
    for i in range(a):
        col = "#d14f8a" if i >= a - b else "#1e4f9c"
        parts.append(f'<circle cx="{16+i*20}" cy="36" r="8" fill="{col}"/>')
        if i >= a - b:
            parts.append(
                f'<line x1="{8+i*20}" y1="28" x2="{24+i*20}" y2="44" stroke="#fff" stroke-width="3"/>'
            )
    parts.append(f'<text x="16" y="78" font-size="16" font-weight="800" fill="#163a75">{a} − {b} = {a-b}</text>')
    return svg("".join(parts), 16 + a * 20 + 10, 95)

def place_value():
    boxes = []
    labels = [("3", "setki", "сотні", "#1e4f9c"), ("4", "dzies.", "десят.", "#2e9b57"), ("7", "jedn.", "один.", "#e67e22")]
    for i, (d, pl, ua, col) in enumerate(labels):
        x = 20 + i * 70
        boxes.append(
            f'<rect x="{x}" y="12" width="58" height="50" rx="10" fill="{col}"/>'
            f'<text x="{x+29}" y="46" text-anchor="middle" fill="#fff" font-size="26" font-weight="900">{d}</text>'
            f'<text x="{x+29}" y="78" text-anchor="middle" fill="{col}" font-size="11" font-weight="800">{pl}</text>'
            f'<text x="{x+29}" y="92" text-anchor="middle" fill="#5a6a7e" font-size="10">{ua}</text>'
        )
    return svg("".join(boxes), 230, 105)

def number_line(vals, mark=None, label=""):
    parts = [
        '<line x1="20" y1="50" x2="200" y2="50" stroke="#1e4f9c" stroke-width="3"/>',
        '<polygon points="200,50 190,44 190,56" fill="#1e4f9c"/>',
    ]
    n = len(vals)
    for i, v in enumerate(vals):
        x = 30 + i * (160 / max(1, n - 1))
        parts.append(f'<circle cx="{x}" cy="50" r="5" fill="#f5c518" stroke="#1e4f9c" stroke-width="2"/>')
        parts.append(f'<text x="{x}" y="72" text-anchor="middle" font-size="12" font-weight="800" fill="#163a75">{v}</text>')
        if mark is not None and v == mark:
            parts.append(f'<circle cx="{x}" cy="50" r="10" fill="none" stroke="#d14f8a" stroke-width="3"/>')
    if label:
        parts.append(f'<text x="110" y="22" text-anchor="middle" font-size="13" font-weight="800" fill="#1e4f9c">{label}</text>')
    return svg("".join(parts), 220, 90)

def compare_syms():
    return svg(
        '<text x="40" y="55" font-size="28" font-weight="900" fill="#2e9b57">3 &lt; 7</text>'
        '<text x="110" y="55" font-size="28" font-weight="900" fill="#1e4f9c">5 = 5</text>'
        '<text x="180" y="55" font-size="28" font-weight="900" fill="#e67e22">9 &gt; 2</text>',
        230, 80,
    )

def even_odd():
    return svg(
        '<rect x="10" y="15" width="95" height="70" rx="12" fill="#e6f7ec"/>'
        '<text x="57" y="40" text-anchor="middle" font-size="13" font-weight="900" fill="#2e9b57">parzyste</text>'
        '<text x="57" y="62" text-anchor="middle" font-size="14" font-weight="800" fill="#163a75">0 2 4 6 8</text>'
        '<rect x="115" y="15" width="95" height="70" rx="12" fill="#fce8f1"/>'
        '<text x="162" y="40" text-anchor="middle" font-size="13" font-weight="900" fill="#d14f8a">nieparzyste</text>'
        '<text x="162" y="62" text-anchor="middle" font-size="14" font-weight="800" fill="#163a75">1 3 5 7 9</text>',
        220, 100,
    )

def fraction_pie(num=1, den=4, color="#e67e22"):
    """Simple pie with den slices, num filled."""
    import math
    parts = [f'<circle cx="70" cy="55" r="42" fill="#fff6d1" stroke="#1e4f9c" stroke-width="2"/>']
    for i in range(den):
        a0 = -math.pi / 2 + 2 * math.pi * i / den
        a1 = -math.pi / 2 + 2 * math.pi * (i + 1) / den
        x0, y0 = 70 + 42 * math.cos(a0), 55 + 42 * math.sin(a0)
        x1, y1 = 70 + 42 * math.cos(a1), 55 + 42 * math.sin(a1)
        large = 1 if (a1 - a0) > math.pi else 0
        fill = color if i < num else "#ffffff"
        if den == 1:
            parts.append(f'<circle cx="70" cy="55" r="42" fill="{color}"/>')
        else:
            parts.append(
                f'<path d="M70 55 L{x0:.1f} {y0:.1f} A42 42 0 {large} 1 {x1:.1f} {y1:.1f} Z" '
                f'fill="{fill}" stroke="#1e4f9c" stroke-width="1.5"/>'
            )
    parts.append(
        f'<text x="160" y="50" text-anchor="middle" font-size="28" font-weight="900" fill="#1e4f9c">{num}</text>'
        f'<line x1="140" y1="58" x2="180" y2="58" stroke="#1e4f9c" stroke-width="3"/>'
        f'<text x="160" y="82" text-anchor="middle" font-size="28" font-weight="900" fill="#1e4f9c">{den}</text>'
    )
    return svg("".join(parts), 210, 110)

def fraction_bars(num=2, den=5, color="#7b4db8"):
    parts = []
    w = 160 / den
    for i in range(den):
        fill = color if i < num else "#e8f0fb"
        parts.append(
            f'<rect x="{20+i*w}" y="30" width="{w-3}" height="40" rx="6" fill="{fill}" stroke="#163a75" stroke-width="1.5"/>'
        )
    parts.append(
        f'<text x="100" y="90" text-anchor="middle" font-size="18" font-weight="900" fill="#163a75">{num}/{den}</text>'
    )
    return svg("".join(parts), 200, 105)

def decimal_place():
    return svg(
        '<text x="30" y="45" font-size="26" font-weight="900" fill="#1e4f9c">2</text>'
        '<text x="52" y="45" font-size="26" font-weight="900" fill="#e67e22">,</text>'
        '<text x="70" y="45" font-size="26" font-weight="900" fill="#2e9b57">3</text>'
        '<text x="95" y="45" font-size="26" font-weight="900" fill="#7b4db8">7</text>'
        '<text x="120" y="45" font-size="26" font-weight="900" fill="#d14f8a">5</text>'
        '<text x="30" y="70" font-size="10" font-weight="800" fill="#1e4f9c">całk.</text>'
        '<text x="70" y="70" font-size="10" font-weight="800" fill="#2e9b57">0,1</text>'
        '<text x="95" y="70" font-size="10" font-weight="800" fill="#7b4db8">0,01</text>'
        '<text x="120" y="70" font-size="10" font-weight="800" fill="#d14f8a">0,001</text>',
        180, 90,
    )

def percent_bar(p=25):
    return svg(
        f'<rect x="20" y="35" width="180" height="28" rx="8" fill="#e8f0fb"/>'
        f'<rect x="20" y="35" width="{1.8*p}" height="28" rx="8" fill="#e67e22"/>'
        f'<text x="110" y="28" text-anchor="middle" font-size="16" font-weight="900" fill="#163a75">{p}% z całości</text>'
        f'<text x="20" y="82" font-size="12" font-weight="800" fill="#5a6a7e">0%</text>'
        f'<text x="200" y="82" text-anchor="end" font-size="12" font-weight="800" fill="#5a6a7e">100%</text>',
        220, 95,
    )

def shapes_tri_sq():
    return svg(
        '<polygon points="45,75 75,20 105,75" fill="#7b4db8" opacity=".85"/>'
        '<rect x="130" y="25" width="55" height="55" rx="4" fill="#1a9b9b" opacity=".85"/>'
        '<text x="75" y="95" text-anchor="middle" font-size="11" font-weight="800" fill="#163a75">trójkąt</text>'
        '<text x="157" y="95" text-anchor="middle" font-size="11" font-weight="800" fill="#163a75">kwadrat</text>',
        220, 110,
    )

def circle_r():
    return svg(
        '<circle cx="90" cy="55" r="40" fill="#fff6d1" stroke="#7b4db8" stroke-width="3"/>'
        '<circle cx="90" cy="55" r="4" fill="#d14f8a"/>'
        '<line x1="90" y1="55" x2="130" y2="55" stroke="#1e4f9c" stroke-width="3"/>'
        '<text x="108" y="48" font-size="14" font-weight="900" fill="#1e4f9c">r</text>'
        '<text x="170" y="50" font-size="13" font-weight="800" fill="#163a75">d = 2r</text>'
        '<text x="170" y="70" font-size="13" font-weight="800" fill="#7b4db8">środek</text>',
        230, 110,
    )

def angle_right():
    return svg(
        '<path d="M40 80 L40 30 L90 30" fill="none" stroke="#1e4f9c" stroke-width="4" stroke-linecap="round"/>'
        '<rect x="40" y="30" width="14" height="14" fill="none" stroke="#f5c518" stroke-width="3"/>'
        '<text x="110" y="55" font-size="20" font-weight="900" fill="#e67e22">90°</text>'
        '<text x="110" y="78" font-size="13" font-weight="800" fill="#163a75">kąt prosty</text>',
        200, 100,
    )

def angles_types():
    return svg(
        # ostry
        '<path d="M30 70 L30 30 L70 55" fill="none" stroke="#2e9b57" stroke-width="3"/>'
        '<text x="40" y="90" font-size="11" font-weight="800" fill="#2e9b57">&lt;90°</text>'
        # prosty
        '<path d="M100 70 L100 30 L140 30" fill="none" stroke="#1e4f9c" stroke-width="3"/>'
        '<rect x="100" y="30" width="10" height="10" fill="none" stroke="#f5c518" stroke-width="2"/>'
        '<text x="110" y="90" font-size="11" font-weight="800" fill="#1e4f9c">90°</text>'
        # rozwarty
        '<path d="M170 70 L170 40 L210 70" fill="none" stroke="#e67e22" stroke-width="3"/>'
        '<text x="180" y="90" font-size="11" font-weight="800" fill="#e67e22">&gt;90°</text>',
        230, 105,
    )

def coords():
    return svg(
        '<line x1="20" y1="80" x2="160" y2="80" stroke="#1e4f9c" stroke-width="2"/>'
        '<line x1="40" y1="100" x2="40" y2="15" stroke="#1e4f9c" stroke-width="2"/>'
        '<polygon points="160,80 152,75 152,85" fill="#1e4f9c"/>'
        '<polygon points="40,15 35,23 45,23" fill="#1e4f9c"/>'
        '<text x="165" y="85" font-size="14" font-weight="900" fill="#1e4f9c">X</text>'
        '<text x="28" y="18" font-size="14" font-weight="900" fill="#1e4f9c">Y</text>'
        '<circle cx="100" cy="40" r="6" fill="#e67e22"/>'
        '<text x="110" y="38" font-size="13" font-weight="800" fill="#163a75">(3, 2)</text>'
        '<line x1="100" y1="40" x2="100" y2="80" stroke="#e67e22" stroke-dasharray="3 2"/>'
        '<line x1="40" y1="40" x2="100" y2="40" stroke="#e67e22" stroke-dasharray="3 2"/>',
        200, 110,
    )

def bar_chart():
    bars = [(40, 50, "#1e4f9c"), (70, 80, "#2e9b57"), (100, 35, "#e67e22"), (130, 65, "#7b4db8")]
    parts = ['<line x1="25" y1="90" x2="160" y2="90" stroke="#5a6a7e" stroke-width="2"/>']
    for x, h, c in bars:
        parts.append(f'<rect x="{x}" y="{90-h}" width="22" height="{h}" rx="4" fill="{c}"/>')
    return svg("".join(parts), 180, 110)

def thermometer():
    return svg(
        '<rect x="90" y="15" width="18" height="70" rx="9" fill="#e8f0fb" stroke="#1e4f9c" stroke-width="2"/>'
        '<circle cx="99" cy="90" r="16" fill="#d14f8a"/>'
        '<rect x="93" y="45" width="12" height="40" rx="6" fill="#d14f8a"/>'
        '<text x="130" y="40" font-size="14" font-weight="900" fill="#1e4f9c">+20°C</text>'
        '<text x="130" y="70" font-size="14" font-weight="900" fill="#d14f8a">−5°C</text>',
        200, 115,
    )

def clock():
    return svg(
        '<circle cx="70" cy="55" r="40" fill="#fff" stroke="#1e4f9c" stroke-width="3"/>'
        '<line x1="70" y1="55" x2="70" y2="30" stroke="#163a75" stroke-width="3" stroke-linecap="round"/>'
        '<line x1="70" y1="55" x2="95" y2="55" stroke="#e67e22" stroke-width="3" stroke-linecap="round"/>'
        '<circle cx="70" cy="55" r="4" fill="#f5c518"/>'
        '<text x="130" y="50" font-size="16" font-weight="900" fill="#163a75">3:00</text>'
        '<text x="130" y="72" font-size="12" font-weight="800" fill="#5a6a7e">1 h = 60 min</text>',
        210, 110,
    )

def money():
    return svg(
        '<rect x="30" y="25" width="70" height="40" rx="8" fill="#2e9b57"/>'
        '<text x="65" y="52" text-anchor="middle" fill="#fff" font-size="16" font-weight="900">1 zł</text>'
        '<circle cx="140" cy="45" r="22" fill="#f5c518" stroke="#e67e22" stroke-width="3"/>'
        '<text x="140" y="50" text-anchor="middle" font-size="12" font-weight="900" fill="#163a75">100 gr</text>',
        190, 90,
    )

def power():
    return svg(
        '<text x="40" y="60" font-size="36" font-weight="900" fill="#1e4f9c">2</text>'
        '<text x="62" y="38" font-size="20" font-weight="900" fill="#e67e22">3</text>'
        '<text x="90" y="58" font-size="22" font-weight="800" fill="#5a6a7e">= 2×2×2 = 8</text>',
        230, 85,
    )

def root():
    return svg(
        '<text x="30" y="60" font-size="36" font-weight="900" fill="#1e4f9c">√</text>'
        '<text x="58" y="60" font-size="28" font-weight="900" fill="#2e9b57">9</text>'
        '<line x1="55" y1="32" x2="85" y2="32" stroke="#1e4f9c" stroke-width="3"/>'
        '<text x="100" y="58" font-size="24" font-weight="800" fill="#5a6a7e">= 3</text>'
        '<text x="160" y="58" font-size="16" font-weight="800" fill="#e67e22">bo 3²=9</text>',
        230, 85,
    )

def equation():
    return svg(
        '<rect x="20" y="25" width="180" height="50" rx="12" fill="#e8f0fb"/>'
        '<text x="110" y="58" text-anchor="middle" font-size="22" font-weight="900" fill="#163a75">x + 5 = 12</text>'
        '<text x="110" y="95" text-anchor="middle" font-size="16" font-weight="800" fill="#2e9b57">x = 7</text>',
        220, 110,
    )

def balance():
    return svg(
        '<line x1="30" y1="40" x2="190" y2="40" stroke="#163a75" stroke-width="4"/>'
        '<line x1="110" y1="40" x2="110" y2="85" stroke="#163a75" stroke-width="4"/>'
        '<polygon points="110,85 95,100 125,100" fill="#1e4f9c"/>'
        '<rect x="35" y="20" width="40" height="20" rx="4" fill="#2e9b57"/>'
        '<rect x="145" y="20" width="40" height="20" rx="4" fill="#e67e22"/>'
        '<text x="55" y="35" text-anchor="middle" fill="#fff" font-size="12" font-weight="900">x</text>'
        '<text x="165" y="35" text-anchor="middle" fill="#fff" font-size="12" font-weight="900">7</text>',
        220, 110,
    )

def cube():
    return svg(
        '<path d="M50 70 L50 30 L90 15 L130 30 L130 70 L90 85 Z" fill="#c9b6e8" stroke="#7b4db8" stroke-width="2"/>'
        '<path d="M50 30 L90 45 L130 30 M90 45 L90 85" fill="none" stroke="#7b4db8" stroke-width="2"/>'
        '<text x="160" y="50" font-size="14" font-weight="800" fill="#163a75">sześcian</text>'
        '<text x="160" y="70" font-size="13" font-weight="800" fill="#7b4db8">V = a³</text>',
        230, 110,
    )

def symmetry():
    return svg(
        '<line x1="110" y1="15" x2="110" y2="95" stroke="#f5c518" stroke-width="3" stroke-dasharray="4 3"/>'
        '<polygon points="50,70 90,25 90,70" fill="#1e4f9c" opacity=".8"/>'
        '<polygon points="170,70 130,25 130,70" fill="#1e4f9c" opacity=".8"/>'
        '<text x="110" y="108" text-anchor="middle" font-size="11" font-weight="800" fill="#e67e22">oś / вісь</text>',
        220, 115, "0 0 220 120",
    )

def multiply_grid():
    parts = []
    for r in range(3):
        for c in range(4):
            parts.append(
                f'<rect x="{30+c*28}" y="{15+r*28}" width="24" height="24" rx="5" fill="#2e9b57"/>'
            )
    parts.append('<text x="160" y="55" font-size="16" font-weight="900" fill="#163a75">3×4=12</text>')
    return svg("".join(parts), 230, 105)

def divide_groups():
    parts = []
    colors = ["#1e4f9c", "#e67e22", "#2e9b57"]
    for g in range(3):
        x0 = 25 + g * 65
        parts.append(f'<rect x="{x0}" y="20" width="55" height="50" rx="10" fill="#e8f0fb" stroke="{colors[g]}" stroke-width="2"/>')
        for i in range(4):
            parts.append(f'<circle cx="{x0+15+(i%2)*22}" cy="{35+(i//2)*18}" r="7" fill="{colors[g]}"/>')
    parts.append('<text x="110" y="95" text-anchor="middle" font-size="14" font-weight="900" fill="#163a75">12 : 3 = 4</text>')
    return svg("".join(parts), 220, 110)

def order_ops():
    return svg(
        '<rect x="10" y="20" width="48" height="36" rx="8" fill="#1e4f9c"/>'
        '<text x="34" y="44" text-anchor="middle" fill="#fff" font-size="12" font-weight="900">()</text>'
        '<text x="68" y="44" font-size="18" fill="#5a6a7e">→</text>'
        '<rect x="85" y="20" width="48" height="36" rx="8" fill="#7b4db8"/>'
        '<text x="109" y="44" text-anchor="middle" fill="#fff" font-size="12" font-weight="900">aⁿ</text>'
        '<text x="143" y="44" font-size="18" fill="#5a6a7e">→</text>'
        '<rect x="160" y="20" width="48" height="36" rx="8" fill="#2e9b57"/>'
        '<text x="184" y="44" text-anchor="middle" fill="#fff" font-size="12" font-weight="900">× :</text>'
        '<text x="110" y="80" text-anchor="middle" font-size="13" font-weight="800" fill="#e67e22">na końcu + −</text>',
        230, 95,
    )

def roman():
    return svg(
        '<text x="20" y="45" font-size="18" font-weight="900" fill="#1e4f9c">I V X L C D M</text>'
        '<text x="20" y="72" font-size="13" font-weight="800" fill="#5a6a7e">1 5 10 50 100 500 1000</text>',
        230, 90,
    )

def integers_axis():
    return number_line(["−3", "−2", "−1", "0", "1", "2", "3"], mark="0", label="oś liczbowa")

def speed():
    return svg(
        '<path d="M30 70 Q80 20 130 70" fill="none" stroke="#1a9b9b" stroke-width="4"/>'
        '<polygon points="130,70 118,62 122,78" fill="#e67e22"/>'
        '<text x="150" y="45" font-size="16" font-weight="900" fill="#163a75">v = s/t</text>'
        '<text x="150" y="68" font-size="12" font-weight="800" fill="#5a6a7e">km/h</text>',
        230, 95,
    )

def pie_stats():
    return svg(
        '<circle cx="70" cy="55" r="40" fill="#1e4f9c"/>'
        '<path d="M70 55 L70 15 A40 40 0 0 1 105 80 Z" fill="#f5c518"/>'
        '<path d="M70 55 L105 80 A40 40 0 0 1 40 85 Z" fill="#2e9b57"/>'
        '<text x="150" y="45" font-size="13" font-weight="800" fill="#1e4f9c">wykres</text>'
        '<text x="150" y="65" font-size="13" font-weight="800" fill="#163a75">kołowy</text>',
        220, 110,
    )

def dice_prob():
    return svg(
        '<rect x="40" y="25" width="55" height="55" rx="10" fill="#fff" stroke="#1e4f9c" stroke-width="3"/>'
        '<circle cx="55" cy="40" r="5" fill="#163a75"/>'
        '<circle cx="80" cy="40" r="5" fill="#163a75"/>'
        '<circle cx="55" cy="65" r="5" fill="#163a75"/>'
        '<circle cx="80" cy="65" r="5" fill="#163a75"/>'
        '<circle cx="67" cy="52" r="5" fill="#163a75"/>'
        '<text x="120" y="50" font-size="16" font-weight="900" fill="#e67e22">P = 1/6</text>'
        '<text x="120" y="72" font-size="12" font-weight="800" fill="#5a6a7e">kostka</text>',
        220, 100,
    )

def length_ruler():
    return svg(
        '<rect x="20" y="40" width="180" height="28" rx="4" fill="#fff6d1" stroke="#1e4f9c" stroke-width="2"/>'
        + "".join(
            f'<line x1="{20+i*18}" y1="40" x2="{20+i*18}" y2="{55 if i%5 else 68}" stroke="#163a75" stroke-width="2"/>'
            for i in range(11)
        )
        + '<text x="110" y="90" text-anchor="middle" font-size="13" font-weight="800" fill="#163a75">cm</text>',
        220, 105,
    )

def volume_box():
    return svg(
        '<path d="M40 75 L40 40 L80 25 L120 40 L120 75 L80 90 Z" fill="#e4f7f7" stroke="#1a9b9b" stroke-width="2"/>'
        '<path d="M40 40 L80 55 L120 40 M80 55 L80 90" fill="none" stroke="#1a9b9b" stroke-width="2"/>'
        '<text x="145" y="50" font-size="14" font-weight="900" fill="#163a75">V=a·b·c</text>'
        '<text x="145" y="72" font-size="12" font-weight="800" fill="#1a9b9b">1 l = 1000 ml</text>',
        230, 110,
    )

def perimeter_area():
    return svg(
        '<rect x="30" y="25" width="90" height="55" fill="#e8f0fb" stroke="#1e4f9c" stroke-width="3"/>'
        '<text x="75" y="58" text-anchor="middle" font-size="12" font-weight="900" fill="#1e4f9c">POLE</text>'
        '<text x="140" y="40" font-size="12" font-weight="800" fill="#e67e22">obwód = dookoła</text>'
        '<text x="140" y="62" font-size="12" font-weight="800" fill="#2e9b57">pole = wewnątrz</text>',
        250, 100,
    )

def mix_number():
    return svg(
        '<text x="40" y="55" font-size="32" font-weight="900" fill="#1e4f9c">1</text>'
        '<text x="70" y="42" font-size="20" font-weight="900" fill="#e67e22">3</text>'
        '<line x1="60" y1="50" x2="90" y2="50" stroke="#e67e22" stroke-width="3"/>'
        '<text x="75" y="72" font-size="20" font-weight="900" fill="#e67e22">4</text>'
        '<text x="110" y="55" font-size="20" font-weight="800" fill="#5a6a7e">= 7/4</text>',
        200, 90,
    )

def prop_line():
    return svg(
        '<line x1="30" y1="85" x2="160" y2="85" stroke="#5a6a7e" stroke-width="2"/>'
        '<line x1="40" y1="90" x2="40" y2="20" stroke="#5a6a7e" stroke-width="2"/>'
        '<line x1="40" y1="85" x2="150" y2="25" stroke="#e67e22" stroke-width="3"/>'
        '<circle cx="90" cy="58" r="5" fill="#1e4f9c"/>'
        '<text x="165" y="40" font-size="13" font-weight="900" fill="#e67e22">y = k·x</text>',
        230, 105,
    )

# Catalog used by build
FIGS = {
    "apples5": lambda: apples(5),
    "digits": lambda: svg(
        "".join(
            f'<rect x="{10+i*20}" y="30" width="18" height="28" rx="4" fill="#1e4f9c"/>'
            f'<text x="{19+i*20}" y="50" text-anchor="middle" fill="#fff" font-size="12" font-weight="900">{i}</text>'
            for i in range(10)
        ),
        220, 90,
    ),
    "place_value": place_value,
    "even_odd": even_odd,
    "compare": compare_syms,
    "round_line": lambda: number_line([40, 45, 50, 55, 60], mark=50, label="47 → 50"),
    "prev_next": lambda: number_line([8, 9, 10], mark=9, label="poprzednik · następnik"),
    "order": lambda: number_line([1, 2, 3, 4, 5, 6], label="od najmniejszej"),
    "roman": roman,
    "integers": integers_axis,
    "add_dots": lambda: add_dots(3, 5),
    "sub_dots": lambda: sub_dots(9, 4),
    "mul_grid": multiply_grid,
    "div_groups": divide_groups,
    "order_ops": order_ops,
    "frac_pie": lambda: fraction_pie(1, 4),
    "frac_bars": lambda: fraction_bars(2, 5),
    "mix": mix_number,
    "decimal": decimal_place,
    "frac_add": lambda: fraction_bars(3, 5, "#2e9b57"),
    "percent": lambda: percent_bar(25),
    "power": power,
    "root": root,
    "prop": prop_line,
    "equation": equation,
    "balance": balance,
    "ruler": length_ruler,
    "thermo": thermometer,
    "clock": clock,
    "money": money,
    "speed": speed,
    "volume": volume_box,
    "shapes": shapes_tri_sq,
    "circle": circle_r,
    "angle": angle_right,
    "angles": angles_types,
    "coords": coords,
    "cube": cube,
    "symmetry": symmetry,
    "peri_area": perimeter_area,
    "bars": bar_chart,
    "pie_chart": pie_stats,
    "dice": dice_prob,
    "abs": lambda: number_line(["−5", "0", "5"], mark="0", label="|−5|=5"),
    "mass": lambda: svg(
        '<ellipse cx="80" cy="55" rx="35" ry="20" fill="#c9b6e8"/><rect x="70" y="20" width="20" height="35" fill="#7b4db8"/>'
        '<text x="140" y="50" font-size="14" font-weight="900" fill="#163a75">1 kg = 1000 g</text>',
        230, 90,
    ),
    "calendar": lambda: svg(
        '<rect x="40" y="20" width="90" height="70" rx="8" fill="#fff" stroke="#1a9b9b" stroke-width="3"/>'
        '<rect x="40" y="20" width="90" height="18" fill="#1a9b9b"/>'
        '<text x="85" y="34" text-anchor="middle" fill="#fff" font-size="11" font-weight="900">VII</text>'
        '<text x="85" y="68" text-anchor="middle" font-size="22" font-weight="900" fill="#163a75">18</text>'
        '<text x="150" y="55" font-size="12" font-weight="800" fill="#5a6a7e">7 dni = tydzień</text>',
        240, 105,
    ),
    "scale_map": lambda: svg(
        '<rect x="30" y="25" width="100" height="60" rx="6" fill="#e6f7ec" stroke="#2e9b57" stroke-width="2"/>'
        '<text x="80" y="55" text-anchor="middle" font-size="14" font-weight="900" fill="#163a75">1 : 100 000</text>'
        '<text x="150" y="50" font-size="12" font-weight="800" fill="#5a6a7e">mapa</text>'
        '<text x="150" y="68" font-size="12" font-weight="800" fill="#5a6a7e">→ teren</text>',
        230, 100,
    ),
    "parallel": lambda: svg(
        '<line x1="30" y1="30" x2="160" y2="30" stroke="#1e4f9c" stroke-width="3"/>'
        '<line x1="30" y1="70" x2="160" y2="70" stroke="#1e4f9c" stroke-width="3"/>'
        '<line x1="70" y1="15" x2="110" y2="85" stroke="#e67e22" stroke-width="3"/>'
        '<text x="175" y="55" font-size="14" font-weight="900" fill="#1e4f9c">a ∥ b</text>',
        230, 100,
    ),
    "signs": lambda: svg(
        '<text x="20" y="55" font-size="24" font-weight="900" fill="#1e4f9c">+ − × : = &lt; &gt; √ % π</text>',
        240, 80,
    ),
}


def render_fig(key: str) -> str:
    fn = FIGS.get(key)
    if not fn:
        return ""
    return f'<div class="fig">{fn()}</div>'
