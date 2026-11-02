#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
chmod +x .githooks/commit-msg
git config --local core.hooksPath .githooks
git config --local commit.template .gitmessage
echo "JS 提交模板与 commit-msg 检查已为当前本地仓库启用。"
