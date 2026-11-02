# 提交信息与 AI 署名

本规则沿用 dontng/44 的详细三段正文与 dontng/e2 的 AI 署名、单目标提交约定。适用于本地 Git、GitHub 网页、API/connector 和 PR；换交付方式不免除署名。

## 每次提交必须说明什么

采用下面格式，标题与正文可用中文。标题准确写结果，正文写具体变更、目的与实际验证，不填“update”“修复一些问题”等空话。

```text
docs: 统一 JS 的提交署名与交付说明

Implemented:
- 新增提交规范、模板与检查入口，并同步协作说明。

Why:
- 从提交记录追溯实际执行者、修改目的与验证边界。

Verified:
- 写明实际运行的检查及结果，未实机验证的内容如实说明。

Generated with Codex
Co-authored-by: Codex <codex@openai.com>
```

## 执行者怎样区分

| 实际执行环境 | Generated with 行 |
|---|---|
| GPT/Codex 在本项目中的交付 | Generated with Codex（也可用 GPT 标明真实环境） |
| Antigravity，模型不明确 | Generated with Antigravity |
| Antigravity，确知使用 Gemini | Generated with Antigravity (Gemini) |
| Antigravity，确知使用 Claude | Generated with Antigravity (Claude) |
| Gemini 直接执行 | Generated with Gemini |
| Claude 直接执行 | Generated with Claude |

平台与模型不能混为一谈。不得把 Antigravity 一律认定为 Gemini，也不能因为材料引用了其他 AI 就把它写成执行者。多方真实参与时，在正文说明各自承担部分，由最终交付者填写 Generated with；模型具体版本未知就不猜。

GPT/Codex 的协作署名沿用 44：Co-authored-by: Codex <codex@openai.com>；E2 使用的 noreply@openai.com 也可接受。其他执行者使用自身已有的真实署名配置，不凭空编造邮箱，不保留模板中的 Codex 冒充其贡献。

使用 GitHub connector 时，GitHub 通常将用户记录为 author/committer，保留这一身份，通过 Generated with 与协作署名记录 AI。使用本地 Git 时保留已有用户配置，不擅自改成其他 AI 的身份。

## 提交和推送的边界

一个用户目标默认一份完整、可读、可回滚的 commit；先完成编辑、范围审查和校验再提交。用户要求分批交付或新增独立目标时按实际拆分。
每个待推送的新提交都应带详细信息与署名，不能只在最后一条补一句替前面所有提交署名。不得宣称运行了未执行的验证。

## 本地启用

在克隆后的仓库根目录执行：

```bash
bash scripts/setup-git-policy.sh
```

启用 .gitmessage 模板与 .githooks/commit-msg。需要 Python 3；本地配置不随克隆自动启用，每个工作副本分别执行。模板必须填写真实内容后才能提交。

通过 GitHub API/connector 提交时，本地 hook 不会执行，交付者须先把最终提交信息写入文件，运行同一检查器：

```bash
python3 scripts/check-commit-message.py /path/to/commit-message.txt
```

检查器验证格式和署名，不验证内容真实性，不是服务端强制保护。推送后核对远端 SHA、最终消息和变更文件；若有本地工作副本，再执行 git status 确认范围与残留。

## 历史记录

本仓库已按用户授权清理历史文件中的非必要个人背景。历史版本仍保留各阶段的项目成果与 AI 交付署名；不在公开文档列出清理前提交的定位信息或被移除内容。

## 对照来源

- [44 的提交规范](https://github.com/dontng/44/blob/main/AGENTS.md)
- [E2 的提交约定](https://github.com/dontng/e2/blob/main/AGENTS.md)
