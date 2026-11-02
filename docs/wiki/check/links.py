#!/usr/bin/env python3
"""Read-only checker for this wiki's simple inline Markdown convention."""
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)")
BACK = "## 哪些名词与它有关"


def prose(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    text = LINK.sub(" ", text)
    return "\n".join(line for line in text.splitlines()
                     if not line.startswith(("#", "参考：")))


def inspect(root):
    root = root.resolve()
    pages = {p.stem: p for p in sorted(root.glob("*.md")) if p.name != "README.md"}
    texts = {name: p.read_text(encoding="utf-8") for name, p in pages.items()}
    index = root / "README.md"
    index_text = index.read_text(encoding="utf-8") if index.exists() else ""
    errors, hints = [], []
    if not index.exists():
        errors.append("缺少 README.md 名词目录")
    # A pending term is a plain bullet under the explicit pending heading.
    pending_section = re.search(r"^## 待解释\s*\n(.*?)(?=^## |\Z)",
                                index_text, re.M | re.S)
    pending = []
    if pending_section:
        pending = re.findall(r"^- ([^\n]+)$", pending_section[1], re.M)
    for name in pending:
        if name in pages:
            errors.append(f"待解释列表中的 {name} 已有页面，请整理状态")
    outgoing = {}
    for name, text in {**texts, "README": index_text}.items():
        targets = set()
        if re.search(r"\[\[[^\]]+\]\]", text):
            errors.append(f"{name}.md: 请使用普通 Markdown 链接")
        for _, raw in LINK.findall(text):
            url = urlsplit(raw)
            decoded = unquote(url.path)
            target = (root / decoded).resolve()
            if url.scheme or url.netloc or target.parent != root:
                errors.append(f"{name}.md: 链接越出名词页范围: {raw}")
            elif url.query or url.fragment:
                errors.append(f"{name}.md: 请直接链接到名词文件: {raw}")
            elif target.suffix != ".md" or not target.is_file():
                errors.append(f"{name}.md: 失效链接: {raw}")
            else:
                targets.add(target.stem)
        outgoing[name] = targets
    ready = set()
    for name, text in texts.items():
        body = text.split(BACK)[0]
        # Structural minimum only; does not establish factual accuracy.
        if len(re.sub(r"\s", "", prose(body))) < 20:
            errors.append(f"{name}.md: 解释内容不足，不能只放标题或占位")
        else:
            ready.add(name)
        if name not in outgoing.get("README", set()):
            errors.append(f"{name}.md: 名词目录缺少入口")
        if "README" not in outgoing[name]:
            errors.append(f"{name}.md: 缺少返回名词目录的链接")
        for _, raw in LINK.findall(body):
            target = Path(unquote(urlsplit(raw).path)).stem
            if target in pages and name not in outgoing.get(target, set()):
                errors.append(f"{name}.md → {target}.md: 缺少反向链接")
    # Longest-first matching avoids reporting CAN inside CAN FD or CAN盒.
    if ready:
        pattern = re.compile("|".join(
            (r"(?<![A-Za-z0-9_])" if term[0].isascii() else "")
            + re.escape(term)
            + (r"(?![A-Za-z0-9_])" if term[-1].isascii() else "")
            for term in sorted(ready, key=lambda t: (-len(t), t))))
        for name, text in texts.items():
            body = prose(text.split(BACK)[0])
            seen = {m.group() for m in pattern.finditer(body)} - {name} - outgoing[name]
            for term in sorted(seen):
                hints.append(f"{name}.md: 正文出现“{term}”但没有在该处链接（人工核对）")
    return len(pages) + len(pending), len(ready), pending, errors, hints


def main():
    total, ready, pending, errors, hints = inspect(ROOT)
    print(f"收录名词：{total} 个；有解释内容：{ready} 个；待解释：{len(pending)} 个")
    print(f"链接或结构错误：{len(errors)} 处；待核对的未链接提及：{len(hints)} 处")
    for message in errors:
        print("错误：" + message)
    for message in hints:
        print("提示：" + message)
    print("检查只衡量文件与链接结构，不表示内容正确或本人已经掌握。")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
