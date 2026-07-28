#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Full integrity audit + resource map. Read-only — no project mutations."""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".cursor"}


def iter_files(exts: set[str] | None = None):
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if exts and p.suffix.lower() not in exts:
            continue
        yield p


def resolve_path(html_path: Path, ref: str) -> Path | None:
    ref = ref.strip()
    if not ref:
        return None
    if ref.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None
    if ref.startswith("#"):
        return None
    ref = ref.split("#")[0].split("?")[0]
    if not ref:
        return None
    if ref.startswith(("http://", "https://", "//")):
        return None
    if ref.startswith("/"):
        return ROOT / ref.lstrip("/")
    return (html_path.parent / ref).resolve()


def main() -> dict:
    html_files = sorted(iter_files({".html", ".htm"}))
    css_files = sorted(iter_files({".css"}))
    js_files = sorted(iter_files({".js"}))
    img_files = sorted(
        iter_files({".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico"})
    )
    doc_files = sorted(iter_files({".pdf", ".md", ".csv", ".docx", ".txt"}))
    audio_files = sorted(iter_files({".mp3", ".wav", ".ogg", ".m4a"}))
    video_files = sorted(iter_files({".mp4", ".webm", ".mov"}))
    pages = (
        sorted((ROOT / "pages").glob("page*.html"))
        if (ROOT / "pages").is_dir()
        else []
    )

    href_re = re.compile(r"""\bhref\s*=\s*["']([^"']+)["']""", re.I)
    src_re = re.compile(r"""\bsrc\s*=\s*["']([^"']+)["']""", re.I)
    id_re = re.compile(r"""\bid\s*=\s*["']([^"']+)["']""", re.I)
    class_re = re.compile(r"""\bclass\s*=\s*["']([^"']+)["']""", re.I)
    onclick_re = re.compile(r"""\bonclick\s*=\s*["']([^"']+)["']""", re.I)
    a_tag_re = re.compile(r"""<a\b([^>]*)>""", re.I)

    wordwall_buttons: list[dict] = []
    internal_links: list[dict] = []
    external_links: list[dict] = []
    img_refs: list[dict] = []
    doc_links: list[dict] = []
    all_ids: list[tuple[str, str]] = []
    all_classes: Counter = Counter()
    onclick_handlers: list[dict] = []
    broken_file_links: list[dict] = []
    broken_hash_links: list[dict] = []
    missing_imgs: list[dict] = []
    html_issues: list[dict] = []
    svg_inline = 0
    nav_links: list[dict] = []

    for hf in html_files:
        text = hf.read_text(encoding="utf-8", errors="replace")
        rel = str(hf.relative_to(ROOT))
        svg_inline += len(re.findall(r"<svg\b", text, re.I))

        for m in id_re.finditer(text):
            all_ids.append((rel, m.group(1)))
        for m in class_re.finditer(text):
            for c in m.group(1).split():
                all_classes[c] += 1
        for m in onclick_re.finditer(text):
            onclick_handlers.append({"file": rel, "handler": m.group(1)[:160]})

        for m in a_tag_re.finditer(text):
            attrs = m.group(1)
            class_m = re.search(r"""class\s*=\s*["']([^"']*)["']""", attrs, re.I)
            classes = class_m.group(1) if class_m else ""
            if "wordwall" not in classes.lower():
                continue
            href_m = re.search(r"""href\s*=\s*["']([^"']*)["']""", attrs, re.I)
            href = href_m.group(1) if href_m else ""
            live = bool(href) and href not in ("#", "")
            wordwall_buttons.append(
                {"file": rel, "href": href, "live": live, "classes": classes}
            )

        for kind, rx in (("href", href_re), ("src", src_re)):
            for m in rx.finditer(text):
                ref = m.group(1).strip()
                if not ref:
                    continue
                entry = {"file": rel, "attr": kind, "ref": ref}
                if ref.startswith(("http://", "https://", "//")):
                    external_links.append(entry)
                    continue
                if ref.startswith(("mailto:", "tel:", "javascript:", "data:")):
                    continue
                if ref.startswith("#"):
                    target = ref[1:].split("?")[0]
                    internal_links.append({**entry, "type": "hash"})
                    if target and not re.search(
                        rf"""\bid\s*=\s*["']{re.escape(target)}["']""", text
                    ):
                        broken_hash_links.append(
                            {**entry, "error": f"missing id #{target} in same file"}
                        )
                    continue

                low = ref.lower()
                if any(
                    low.split("#")[0].endswith(x)
                    for x in (
                        ".pdf",
                        ".md",
                        ".csv",
                        ".docx",
                        ".txt",
                        ".html",
                        ".htm",
                    )
                ) or any(k in low for k in ("regulamin", "rodo")):
                    doc_links.append(entry)

                resolved = resolve_path(hf, ref)
                if resolved is None:
                    continue
                try:
                    resolved_rel = str(resolved.relative_to(ROOT))
                except ValueError:
                    resolved_rel = str(resolved)
                internal_links.append({**entry, "resolved": resolved_rel})

                is_img = kind == "src" or any(
                    low.split("#")[0].endswith(x)
                    for x in (
                        ".png",
                        ".jpg",
                        ".jpeg",
                        ".gif",
                        ".webp",
                        ".svg",
                        ".ico",
                    )
                )
                if is_img:
                    img_refs.append({**entry, "resolved": str(resolved)})
                    if not resolved.exists():
                        missing_imgs.append(
                            {"file": rel, "ref": ref, "resolved": str(resolved)}
                        )
                elif not resolved.exists():
                    broken_file_links.append(
                        {
                            **entry,
                            "error": "file not found",
                            "resolved": str(resolved),
                        }
                    )

        if "<html" in text.lower() and "</html>" not in text.lower():
            html_issues.append({"file": rel, "issue": "missing </html>"})
        for m in re.finditer(
            r"""<script[^>]+src=["']([^"']+)["']""", text, re.I
        ):
            src = m.group(1)
            if src.startswith("http"):
                continue
            rp = resolve_path(hf, src)
            if rp is not None and not rp.exists():
                html_issues.append(
                    {"file": rel, "issue": f"missing script {src}"}
                )
        for m in re.finditer(r"""<link[^>]+href=["']([^"']+)["']""", text, re.I):
            href = m.group(1)
            if href.startswith(("http", "data:")):
                continue
            rp = resolve_path(hf, href)
            if rp is not None and not rp.exists():
                html_issues.append(
                    {"file": rel, "issue": f"missing stylesheet/link {href}"}
                )

        for m in re.finditer(
            r"""href=["']([^"']*page\d+\.html[^"']*)["']""", text
        ):
            nav_links.append({"file": rel, "href": m.group(1)})
            rp = resolve_path(hf, m.group(1))
            if rp is not None and not rp.exists():
                broken_file_links.append(
                    {
                        "file": rel,
                        "attr": "href",
                        "ref": m.group(1),
                        "error": "nav target missing",
                        "resolved": str(rp),
                    }
                )

    # JS
    js_class_refs: set[str] = set()
    js_id_refs: set[str] = set()
    js_events: list[dict] = []
    for jf in js_files:
        t = jf.read_text(encoding="utf-8", errors="replace")
        rel = str(jf.relative_to(ROOT))
        for m in re.finditer(
            r"""querySelector(All)?\(\s*['"]([^'"]+)['"]""", t
        ):
            js_events.append(
                {"file": rel, "type": "querySelector", "sel": m.group(2)}
            )
        for m in re.finditer(r"""['"]\.([a-zA-Z_][\w-]*)""", t):
            js_class_refs.add(m.group(1))
        for m in re.finditer(r"""['"]#([a-zA-Z_][\w-]*)""", t):
            js_id_refs.add(m.group(1))
        for m in re.finditer(
            r"""\.addEventListener\(\s*['"](\w+)['"]""", t
        ):
            js_events.append(
                {"file": rel, "type": "addEventListener", "event": m.group(1)}
            )
        for m in re.finditer(
            r"""getElementById\(\s*['"]([^'"]+)['"]""", t
        ):
            js_id_refs.add(m.group(1))
            js_events.append(
                {"file": rel, "type": "getElementById", "id": m.group(1)}
            )
        for m in re.finditer(
            r"""getElementsByClassName\(\s*['"]([^'"]+)['"]""", t
        ):
            js_class_refs.add(m.group(1))
            js_events.append(
                {
                    "file": rel,
                    "type": "getElementsByClassName",
                    "class": m.group(1),
                }
            )

    html_class_set = set(all_classes)
    js_classes_missing_html = sorted(
        c for c in js_class_refs if c not in html_class_set
    )

    within_file_dups = []
    per_file: dict[str, list[str]] = defaultdict(list)
    for f, i in all_ids:
        per_file[f].append(i)
    for f, ids in per_file.items():
        for i, n in Counter(ids).items():
            if n > 1:
                within_file_dups.append({"file": f, "id": i, "count": n})

    assets_root = ROOT / "assets"
    asset_imgs = (
        [
            p
            for p in assets_root.rglob("*")
            if p.is_file()
            and p.suffix.lower()
            in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico"}
        ]
        if assets_root.is_dir()
        else []
    )
    referenced = set()
    for r in img_refs:
        try:
            referenced.add(Path(r["resolved"]).resolve())
        except Exception:
            pass
    orphan_imgs = [
        str(p.relative_to(ROOT))
        for p in asset_imgs
        if p.resolve() not in referenced
    ]

    ww_total = len(wordwall_buttons)
    ww_live = sum(1 for w in wordwall_buttons if w["live"])
    ww_pending = ww_total - ww_live
    missing_unique = sorted({(m["file"], m["ref"]) for m in missing_imgs})

    # Resource map: pages → assets
    page_map = []
    for p in pages:
        text = p.read_text(encoding="utf-8", errors="replace")
        rel = str(p.relative_to(ROOT))
        imgs = sorted(set(src_re.findall(text)))
        ww = [
            w
            for w in wordwall_buttons
            if w["file"] == rel
        ]
        ids = id_re.findall(text)
        page_map.append(
            {
                "file": rel,
                "wordwall_buttons": len(ww),
                "wordwall_live": sum(1 for w in ww if w["live"]),
                "img_refs": len(imgs),
                "ids": ids,
            }
        )

    report = {
        "root": str(ROOT),
        "status": "BASELINE_ONLY — no rebuild applied",
        "counts": {
            "html_files": len(html_files),
            "page_html": len(pages),
            "css_files": len(css_files),
            "js_files": len(js_files),
            "image_files_on_disk": len(img_files),
            "asset_images": len(asset_imgs),
            "audio": len(audio_files),
            "video": len(video_files),
            "docs": len(doc_files),
            "wordwall_buttons": ww_total,
            "wordwall_live": ww_live,
            "wordwall_pending_hash": ww_pending,
            "internal_link_refs": len(internal_links),
            "external_link_refs": len(external_links),
            "doc_link_refs": len(doc_links),
            "img_src_refs": len(img_refs),
            "inline_svg_tags": svg_inline,
            "html_ids": len(all_ids),
            "unique_html_id_names": len({i for _, i in all_ids}),
            "onclick_inline": len(onclick_handlers),
            "js_event_bindings": len(js_events),
            "nav_page_links": len(nav_links),
        },
        "wordwall": {
            "total_buttons": ww_total,
            "live": ww_live,
            "pending": ww_pending,
            "unique_hrefs": sorted({w["href"] for w in wordwall_buttons}),
            "by_file": dict(Counter(w["file"] for w in wordwall_buttons)),
        },
        "integrity": {
            "broken_file_links_count": len(broken_file_links),
            "broken_file_links": broken_file_links[:200],
            "broken_hash_links_count": len(broken_hash_links),
            "broken_hash_links_sample": broken_hash_links[:50],
            "missing_images_count": len(missing_unique),
            "missing_images": [
                {"file": f, "ref": r} for f, r in missing_unique[:300]
            ],
            "html_issues": html_issues,
            "duplicate_ids_within_file": within_file_dups[:100],
            "orphan_asset_images_count": len(orphan_imgs),
            "orphan_asset_images_sample": orphan_imgs[:40],
        },
        "js": {
            "files": [str(p.relative_to(ROOT)) for p in js_files],
            "class_refs": sorted(js_class_refs),
            "id_refs": sorted(js_id_refs),
            "classes_missing_from_html": js_classes_missing_html,
            "events": js_events,
            "onclick_inline": onclick_handlers,
        },
        "resource_map": {
            "css": [str(p.relative_to(ROOT)) for p in css_files],
            "js": [str(p.relative_to(ROOT)) for p in js_files],
            "top_level_html": sorted(
                str(p.relative_to(ROOT))
                for p in ROOT.glob("*.html")
            ),
            "pages": page_map,
            "doc_links_sample": doc_links[:40],
        },
        "baseline_for_rebuild": {
            "pages_before": len(pages),
            "wordwall_buttons_before": ww_total,
            "wordwall_live_before": ww_live,
            "images_on_disk_before": len(img_files),
            "img_refs_before": len(img_refs),
            "internal_links_before": len(internal_links),
            "external_links_before": len(external_links),
            "inline_svg_before": svg_inline,
            "audio_before": len(audio_files),
            "video_before": len(video_files),
        },
        "gate": {
            "rebuild_allowed": False,
            "reason": (
                "Stop for review: integrity baseline captured. "
                "Do not apply rebuild until user confirms AND "
                "broken/missing lists are accepted or fixed."
            ),
        },
    }

    out_json = ROOT / "docs" / "INTEGRITY_BASELINE.json"
    out_json.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return report


if __name__ == "__main__":
    r = main()
    c = r["counts"]
    i = r["integrity"]
    print("=== INTEGRITY BASELINE (no mutations) ===")
    print(f"pages: {c['page_html']}")
    print(
        f"Wordwall buttons: {c['wordwall_buttons']} "
        f"(live {c['wordwall_live']}, pending# {c['wordwall_pending_hash']})"
    )
    print(f"images on disk: {c['image_files_on_disk']}")
    print(f"img refs: {c['img_src_refs']}")
    print(f"internal links: {c['internal_link_refs']}")
    print(f"external links: {c['external_link_refs']}")
    print(f"inline SVG: {c['inline_svg_tags']}")
    print(f"audio: {c['audio']} | video: {c['video']}")
    print(f"broken file links: {i['broken_file_links_count']}")
    print(f"broken hash links: {i['broken_hash_links_count']}")
    print(f"missing images: {i['missing_images_count']}")
    print(f"HTML issues: {len(i['html_issues'])}")
    print(f"dup ids in file: {len(i['duplicate_ids_within_file'])}")
    print(f"orphan assets: {i['orphan_asset_images_count']}")
    print(f"GATE rebuild_allowed: {r['gate']['rebuild_allowed']}")
    print("Wrote docs/INTEGRITY_BASELINE.json")
    if i["broken_file_links"]:
        print("\n--- Broken file links ---")
        for b in i["broken_file_links"][:30]:
            print(f"  {b['file']}: {b['ref']} -> {b.get('error')}")
    if i["missing_images"]:
        print("\n--- Missing images (sample) ---")
        for m in i["missing_images"][:20]:
            print(f"  {m['file']}: {m['ref']}")
    if i["html_issues"]:
        print("\n--- HTML issues ---")
        for h in i["html_issues"]:
            print(f"  {h}")
