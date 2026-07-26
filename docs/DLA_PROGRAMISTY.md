# Mini-słownik matematyki PL–UA — документация для программиста

Стек: **статический HTML + CSS + JS** · генератор контента на **Python 3**  
Поток: данные в `.py` → `build_pages.py` → `pages/*.html`, `index.html`, `book.html`

---

## 1. Быстрый старт

```bash
cd /path/to/MINI_SLOWNIK_MATEMATYKA_PL_UA
python3 build_pages.py
```

Успех: `OK: 60 pages + index + book.html`.

Открыть: `index.html` или `pages/page06.html` (удобнее через локальный сервер, если `file://` режет ресурсы).

**Важно:** `build_pages.py` **перезаписывает** сгенерированный HTML. Ручные правки в `pages/*.html` пропадут — меняйте `.py`, затем собирайте.

---

## 2. Структура репозитория

```
MINI_SLOWNIK_MATEMATYKA_PL_UA/
├── build_pages.py              # генератор HTML
├── pages_data.py               # темы 01–42 + import 43–60 + apply()
├── pages_new_43_60.py          # темы 43–60
├── handbook_enrich.py          # обогащение, PAGE_RULES, CARD_OVERRIDES
├── handbook_overrides_all.py
├── handbook_clear.py           # финальные правки ясности (побеждает)
├── handbook_examples.py
├── handbook_life_complete.py
├── pilot_pages.py              # особые «пилотные» страницы
├── klasa_map.py                # pill «klasy …»
├── curriculum_coverage.py      # карта vs podstawa programowa
├── ai_prompts.py               # промпты к иллюстрациям (комментарии в HTML)
├── figs_map.py / illustrations.py
├── style.css / media.css / script.js
├── index.html / book.html      # генерируются
├── pages/page01.html …         # генерируются
├── assets/
│   ├── logo.svg
│   ├── images/img{NN}_{slot}.png
│   └── icons/
└── docs/
    ├── METODOLOGIA.md
    └── DLA_PROGRAMISTY.md      # этот файл
```

---

## 3. Модель данных

Страница = dict из хелперов `P(...)` / `C(...)` / `R(...)`.

### Поля страницы (главное)

| Поле | Смысл |
|------|--------|
| `n` | номер 1–60 |
| `file` | например `page06.html` |
| `cat` | `A`…`F` (цвет / раздел) |
| `title_pl` / `title_ua` | заголовок |
| `intro_pl` / `intro_ua` | lead |
| `tip_pl` / `tip_ua` | текст блока совы |
| `cards` | список понятий |
| `remember` | правила внизу (`pl`, `ua`, опц. `formula`) |
| `life_pl` / `life_ua` | (после enrich) полоса «W życiu» |
| `mistake_pl` / `mistake_ua` | опц. «Częsty błąd» |

### Поля карточки

| Поле | Смысл |
|------|--------|
| `pl` / `ua` | термин (**ключ override** = `(page_n, pl)`) |
| `visual` | короткий запись / формула |
| `def_pl` / `def_ua` | «Co to jest?» |
| `rule` / `rule_ua` | «Jak w szkole?» |
| `example_pl` / `example_ua` | пример из жизни |
| `klasa` | например `klasy 4–6` |
| `media` | `diagram` / `cover` / `photo` — слот картинки |
| `wide` | опц. `wide-2` / `wide-3` |

---

## 4. Pipeline контента (порядок слоёв)

В конце `pages_data.py`:

```text
PAGES (01–42)
  + build_new_pages()     # 43–60
  → handbook_enrich.apply()
```

Внутри `apply()` (упрощённо):

1. Для каждой карточки — `enrich_card`
2. Override: `CARD_OVERRIDES` ← merge:
   - база в `handbook_enrich.py`
   - `MORE_OVERRIDES` (`handbook_overrides_all.py`)
   - **`CLEAR_FIXES` (`handbook_clear.py`) — последний, побеждает**
3. Без override: лёгкое закрытие коротких определений (`_expand_pair`)
4. Без `rule` — школьная подсказка по умолчанию
5. `attach_examples` + life
6. `resolve_klasa`, `apply_page_meta`, `apply_pilot`

### Куда править текст

| Задача | Файл |
|--------|------|
| Новая тема 43+ | `pages_new_43_60.py` |
| Тема 1–42 (скелет) | `pages_data.py` |
| Поправить определение/правило | `handbook_clear.py` (предпочтительно) |
| Пример из жизни | `handbook_life_complete.py` / `handbook_examples.py` |
| Правила внизу страницы | `PAGE_RULES` в `handbook_enrich.py` или `remember` |
| Классы на pill | `klasa_map.py` |

Ключ override: **`(номер_страницы, точная строка card["pl"])`**. Опечатка в `pl` — override не сработает.

---

## 5. Генератор HTML (`build_pages.py`)

Собирает:

- `pages/pageNN.html` — одна тема
- `index.html` — оглавление (категории, поиск)
- `book.html` — все главы для печати/PDF

Каркас страницы:

- `.page-nav` — логотип (`assets/logo.svg`) + Spis + PDF / Książka / prev–next
- `.page-header` — badge категории, заголовок, intro, `.owl-tip`
- `.media--hero` — `assets/images/img{NN}_1.png`
- lead, life-strip, `.cards`, rules, footer
- stub Wordwall в конце карточки

Картинки: даже без файла вставляется `<img src=...>`. Промпты AI — в HTML-комментариях (`ai_prompts.py`).

---

## 6. Фронтенд

| Файл | Роль |
|------|------|
| `style.css` | вёрстка страницы, карточки, нав, сова, print |
| `media.css` | размеры hero / cover / photo / diagram |
| `script.js` | оглавление: фильтр + search; печать |

Print: `.no-print` скрывает нав / сову / Wordwall.

Логотип: заменить `assets/logo.svg` (имя то же) или путь в `build_pages.py`.

---

## 7. Схема картинок

```text
assets/images/img{NN}_{slot}.png
```

- `NN` — номер страницы с нулём (`01`…`60`)
- типично: `1` = hero, `2` = life, дальше — слоты карточек по генератору

---

## 8. Покрытие PP

```bash
python3 curriculum_coverage.py
```

Печатает `covered` / `partial` / `gap` и список дыр.  
Новые темы → обновить статусы в `CURRICULUM`.

---

## 9. Типовые задачи

### Добавить понятие на существующую страницу

1. `C(...)` в источнике страницы.
2. При необходимости — `handbook_clear.py`.
3. `klasa` / `klasa_map.py`.
4. `python3 build_pages.py`.
5. Проверить HTML + картинку слота.

### Добавить страницу 61+

1. Новый `P(...)` (лучше отдельный модуль, как 43–60).
2. Подключить к `PAGES`.
3. Дополнить: life, klasa_map, ai_prompts, curriculum_coverage.
4. Ассеты `img61_*.png`.
5. Build + smoke в `index.html` / `book.html`.

### Поправить только «Jak w szkole»

```python
# handbook_clear.py
(52, "jaki procent?"): T(
    "…def_pl…", "…def_ua…",
    "…rule…", "…rule_ua…",
),
```

затем build.

---

## 10. Ловушки

1. Правка HTML вместо `.py` — изменения сгорят.
2. Ключ `pl` должен **байт-в-байт** совпадать с карточкой.
3. Порядок override: `CLEAR_FIXES` побеждает `MORE_OVERRIDES`.
4. Школьные термины: `półprosta` ≠ `promień`; угол = две **półproste**.
5. UTF-8: держите польские/украинские символы в `.py` без поломки кодировки.

---

## 11. Smoke-чеклист после build

- [ ] Открываются `page01` и последняя страница
- [ ] Логотип в навбаре
- [ ] Owl-tip: PL + UA
- [ ] Hero-картинка / нет критичного 404
- [ ] Карточки: определение / правило / пример
- [ ] `index.html`: фильтр + поиск
- [ ] `book.html`: главы на месте

```bash
python3 -c "from pages_data import PAGES; print(len(PAGES), sum(len(p['cards']) for p in PAGES))"
```

---

## 12. Зависимости

- Python **3.9+**, только stdlib
- `requirements.txt` нет
- Шрифт Nunito с Google Fonts — нужен интернет при первой загрузке страницы

---

## 13. Связанные документы

- Смысл и канон контента: [`METODOLOGIA.md`](./METODOLOGIA.md)
- Карта PP: `curriculum_coverage.py`
