# JS 协作约定

先读 README.md、docs/CURRENT.md 与 docs/ROADMAP.md，再开展任务。使用中文，自然段解释，面向 CAN 与软件开发入门学习，缩写首次出现解释作用。

## 目标

JS 是长期学习、实验和工具集合，承接 CAN/CAN FD、Python、上位机、自动化与 ROS2，未来可以按需求加入仪器适配。职业方向为机器人软件测试开发和应用工具；不擅自转向硬件台架职业路线，不带入无关生活安排。
市场需求决定能力优先级，招聘的学历、地点、薪资口径和时效需核实，不承诺学完对应工资。

## 工作方式

遵循 docs/ORGANIZATION.md。先完成当前最小任务，有代码时再建工程配置；不要一次生成用户无法掌握的大框架。
阅读参考实现是理解依据的入口，公开提交采用独立实现与可公开材料。解释代码、用户独立修改、运行验证和排错均是阶段验收组成。
新增知识写 learning，来源写 resources，实验写 labs，稳定工具写 tools。模板可选，避免重复记录。
收到“先收集/先规划”不擅自扩成软件开发。完成一轮后更新 CURRENT 的真实状态及下一步。

## 验证与边界

未运行、模拟运行、实机运行明确区分。不得编造设备参数、报文或验证结果。未知硬件与环境写待确认。
Windows DLL 不默认支持 Linux/WSL2/Mac；先核实 SDK。ROS2 暂以 Ubuntu 22.04 + Humble 为市场参照，实施前复核版本。
仓库公开，不提交未经授权的公司代码、私有协议、设备配置或原始日志。实际设备运动遵守现场既有许可、限值和停止流程。

## 提交与 AI 署名

每次提交遵守 [提交规范](docs/COMMIT_POLICY.md)，与 44/E2 保持详细说明和 AI 来源可追溯。
标题写具体结果，正文必须有非空 Implemented:、Why:、Verified: 三段，每段至少一条真实说明。
必须有 Generated with <真实执行者>，区分 Codex/GPT、Antigravity（已知时补模型）、Gemini 与 Claude。GPT/Codex 交付最后添加 Co-authored-by: Codex <codex@openai.com>，不擅改现有 Git author/committer。
一个目标默认一个完成后的提交。每个待推送提交分别署名，不用末尾补记代替新提交自身信息。本地执行 bash scripts/setup-git-policy.sh 启用模板与检查；API/connector 交付也要先运行 scripts/check-commit-message.py 校验最终消息，不能以 hook 未执行为由省略。
推送后回读远端 SHA、消息与变更范围；有本地工作副本时检查 git status。仅声明已实际完成的验证。已发布提交不擅自改写历史。
