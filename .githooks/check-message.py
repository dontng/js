#!/usr/bin/env python3
"""Validate JS commit messages; usable by hooks and API-based publishers."""
import re
import sys
from pathlib import Path

AGENTS = ("Codex", "GPT", "Antigravity", "Gemini", "Claude")
HEADINGS = ("Implemented:", "Why:", "Verified:")

def validate(message):
    lines = [line.rstrip() for line in message.replace("\r\n", "\n").splitlines()
             if not line.lstrip().startswith("#")]
    text = "\n".join(lines).strip()
    lines = text.splitlines()
    errors = []
    if not lines or not re.match(r"^[a-z][a-z0-9_-]*(?:\([^()\n]+\))?: \S.+", lines[0]):
        errors.append("标题须为 <area>: <具体完成结果>，可使用 scope。")
    elif re.search(r"(?:^|: )\s*(?:update|fix|changes|更新|修改)\s*$", lines[0], re.I):
        errors.append("标题不能只写 update/fix/changes/更新/修改。")
    positions = []
    for heading in HEADINGS:
        hits = [i for i, line in enumerate(lines) if line == heading]
        if len(hits) != 1:
            errors.append(f"{heading} 必须且只能出现一次。")
        else:
            positions.append(hits[0])
    if len(positions) == 3 and positions != sorted(positions):
        errors.append("正文顺序应为 Implemented、Why、Verified。")
    for i, heading in enumerate(HEADINGS):
        if lines.count(heading) != 1:
            continue
        start = lines.index(heading) + 1
        end = next((n for n in range(start, len(lines))
                    if lines[n] in HEADINGS or lines[n].startswith(
                        ("Generated with ", "Co-authored-by:", "Co-Authored-By:"))), len(lines))
        bullets = [line for line in lines[start:end] if re.match(r"^[-*] +\S", line)]
        if not bullets or all(re.fullmatch(r"[-*] +(TODO|TBD|待填|\.\.\.|<.*>)", b, re.I) for b in bullets):
            errors.append(f"{heading} 至少需要一条真实说明，不能只留占位符。")
    generated = [line for line in lines if line.startswith("Generated with ")]
    if len(generated) != 1:
        errors.append("须有一条 Generated with <执行者>。")
    else:
        who = generated[0][len("Generated with "):]
        if not any(who == agent or (who.startswith(agent + " (") and who.endswith(")"))
                   for agent in AGENTS):
            errors.append("执行者须为 Codex、GPT、Antigravity、Gemini 或 Claude；括号可补充已知模型。")
        if who == "Codex" or who.startswith("Codex (") or who == "GPT" or who.startswith("GPT ("):
            if not re.search(r"^Co-[Aa]uthored-[Bb]y: Codex <(?:codex|noreply)@openai\.com>$", text, re.M):
                errors.append("GPT/Codex 交付须包含 Codex 协作署名。")
    if re.search(r"\b(TODO|TBD)\b|<待填[^>]*>", text, re.I):
        errors.append("正式提交中仍有未填写的模板占位符。")
    return errors

def main():
    if len(sys.argv) != 2:
        print("用法: python .githooks/check-message.py <提交信息文件>", file=sys.stderr)
        return 2
    errors = validate(Path(sys.argv[1]).read_text(encoding="utf-8-sig"))
    if errors:
        print("\n".join("- " + error for error in errors), file=sys.stderr)
        return 1
    print("JS commit message: OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
