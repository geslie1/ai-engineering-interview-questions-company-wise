#!/usr/bin/env python3
"""Check the Chinese edition and local study notes using only the standard library."""

import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "docs" / "zh-CN"
LINK = re.compile(r"\]\(([^)]+)\)")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def links(text):
    return LINK.findall(text)


def answer_rows(text, prefix):
    return [links(line) for line in text.splitlines() if line.startswith(prefix)]


def question_references(text):
    blocks = []
    for line in text.splitlines():
        if line.startswith("- ") and not line.startswith("- ["):
            blocks.append([])
        elif line.startswith("  - ") and blocks:
            blocks[-1].extend(links(line))
    return blocks


def anchors(text):
    explicit = re.findall(r'<a id="([^"]+)"', text)
    require(len(explicit) == len(set(explicit)), "Duplicate explicit anchor")
    result = set(explicit)
    seen = Counter()
    for heading in re.findall(r"^#{1,6} (.+)$", text, re.M):
        heading = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", heading)
        heading = re.sub(r"<[^>]+>", "", heading).strip().lower()
        slug = "".join(
            char for char in heading
            if char in "-_ " or unicodedata.category(char)[0] in "LNM"
        ).replace(" ", "-")
        count = seen[slug]
        seen[slug] += 1
        result.add(slug if count == 0 else f"{slug}-{count}")
    return result


def validate():
    en = (ROOT / "README.md").read_text(encoding="utf-8")
    zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    manifest = json.loads((LIBRARY / "sources.json").read_text(encoding="utf-8"))
    require(manifest["schema_version"] == 1, "Unsupported manifest version")
    sources = manifest["sources"]
    by_url = {source["source_url"]: source for source in sources}
    by_id = {source["id"]: source for source in sources}
    require(len(by_url) == len(by_id) == len(sources), "Duplicate source URL or ID")
    require(len({s["path"] for s in sources}) == len(sources), "Duplicate note path")

    en_answers = answer_rows(en, "  - Answer:")
    zh_answers = answer_rows(zh, "  - 参考答案：")
    original_urls = {url for row in en_answers for url in row}
    require(original_urls == set(by_url), "Manifest differs from English answer sources")
    replacements = {url: "docs/zh-CN/" + item["path"] for url, item in by_url.items()}
    expected_answers = [[replacements[url] for url in row] for row in en_answers]
    require(zh_answers == expected_answers, "Chinese answer order or mapping differs")
    expected_blocks = [
        [replacements.get(url, url) for url in block]
        for block in question_references(en)
    ]
    require(question_references(zh) == expected_blocks, "Question-specific references differ")
    require(re.findall(r"^#+ ", en, re.M) == re.findall(r"^#+ ", zh, re.M),
            "Chinese heading structure differs")
    require(re.findall(r"```\n(.*?)```", en, re.S) == re.findall(r"```\n(.*?)```", zh, re.S),
            "Original fenced content, including license notice, differs")

    index = (LIBRARY / "README.md").read_text(encoding="utf-8")
    index_links = Counter(links(index))
    known_paths = {source["path"] for source in sources}
    actual_paths = {path.name for path in LIBRARY.glob("*.md") if path.name != "README.md"}
    require(known_paths == actual_paths, "Missing or unregistered study notes")
    require(all(path.suffix in (".md", ".json") for path in LIBRARY.rglob("*") if path.is_file()),
            "Unexpected source cache or asset in the study library")
    for source in sources:
        path = Path(source["path"])
        require(path.name == source["path"] and path.suffix == ".md", "Unsafe note path")
        require(index_links[source["path"]] == 1, f"Index entry missing/duplicated: {path}")
        page = (LIBRARY / path).read_text(encoding="utf-8")
        require(page.startswith(f"# {source['title']}\n"), f"Title differs: {path}")
        require(source["source_url"] in links(page), f"Missing original source: {path}")
        require(source["retrieved_at"][:10] in page, f"Missing retrieval date: {path}")
        require("全文翻译" in page and "原作者" in page, f"Missing scope/attribution: {path}")
        require(source["access_status"] in {"readable", "visible_text_only", "transcript_unavailable"},
                f"Unknown reading status: {path}")
        if source["source_type"] == "video":
            require(source["access_status"] == "transcript_unavailable", f"Review video status: {path}")
            require("## 获取状态" in page and "## 原文摘要" not in page and "未取得" in page,
                    f"Unavailable video presented as a summary: {path}")
        else:
            require("## 原文摘要" in page, f"Missing source summary: {path}")
        if source["access_status"] == "visible_text_only":
            require("附图" in page, f"Missing partial-reading disclosure: {path}")
        for section in ("面试解析", "常见误区与边界", "面试追问", "相关阅读"):
            require(f"## {section}\n\n" in page, f"Missing section {section}: {path}")
        require(len(source["related_ids"]) == len(set(source["related_ids"])),
                f"Duplicate related IDs: {path}")
        for related_id in source["related_ids"]:
            require(related_id in by_id and related_id != source["id"], f"Invalid related ID: {path}")
            require(by_id[related_id]["path"] in links(page), f"Missing related note: {path}")

    markdown_files = [ROOT / "README.md", ROOT / "README.zh-CN.md", *LIBRARY.glob("*.md")]
    texts = {path.resolve(): path.read_text(encoding="utf-8") for path in markdown_files}
    anchor_sets = {path: anchors(text) for path, text in texts.items()}
    local_link_count = 0
    for path, text in texts.items():
        for target in links(text):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            local_link_count += 1
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            require(destination.is_relative_to(ROOT), f"Link escapes repository: {path}: {target}")
            require(destination.is_file(), f"Broken local link: {path}: {target}")
            if parsed.fragment:
                require(unquote(parsed.fragment) in anchor_sets.get(destination, set()),
                        f"Broken anchor: {path}: {target}")

    return {
        "result": "PASS",
        "study_notes": len(sources),
        "answer_rows": len(zh_answers),
        "localized_answer_links": sum(map(len, zh_answers)),
        "reading_status": dict(Counter(s["access_status"] for s in sources)),
        "markdown_files_checked": len(markdown_files),
        "local_links_checked": local_link_count,
    }


if __name__ == "__main__":
    try:
        print(json.dumps(validate(), ensure_ascii=False, indent=2))
    except (ValueError, KeyError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
