# 学习

知识笔记、外部资料和参考链接都放这里，不再分开几个入口。新材料先在本页追加标题、链接和“想解决什么”；确有必要再建一篇笔记。

现在先看[从一次读取理解通信](can/first-reading.md)。实际设备与系统条件记在[环境说明](ENVIRONMENT.md)，没有确认的就留待确认。

笔记写清一个问题、自己的理解和例子即可；有来源附链接，有实验则链接labs中的代码。无需套模板。

[名词](words/README.md)：软件、硬件和通信的简短解释，通过普通 Markdown 链接在名词目录内相互跳转。

## 已收集的公开资料

查阅登记：2026-11-02。仅记录公开来源；文档写明支持不等于本项目实测通过。网址可能变更，实施前复核。

| 编号 | 来源 | 用途 | 当前状态 |
|---|---|---|---|
| R001 | [智元 X2：环境与连接](https://x2-aimdk.agibot.com/en/dev/quick_start/prerequisites.html) | 参照 Ubuntu 22.04、Humble 与 SDK 版本匹配要求 | 已查阅，未实测 |
| R002 | [宇树 ROS2 官方项目](https://github.com/unitreerobotics/unitree_ros2) | 了解机器狗/机器人 ROS2 示例及运行环境 | 已查阅，未实测 |
| R003 | [智元 OmniHand SDK](https://github.com/AgibotTech/agillink_omnihand_sdk/blob/main/doc/en/QUICK_START.md) | 普通 SDK 到 Linux ROS2 示例的衔接参照 | 已查阅，未实测 |
| R004 | [ROS2 官方：话题、服务与动作](https://github.com/ros2/ros2_documentation/blob/rolling/source/ROS-Framework/interfaces/Topics-Services-Actions.rst) | 选择持续状态、快速查询、长期任务的接口 | 已查阅，未实测；rolling 文档 |
| R005 | [微软：WSL 网络](https://learn.microsoft.com/en-us/windows/wsl/networking) | 后续局域网与机器人通信条件 | 已查阅，未实测 |
| R006 | [微软：WSL USB](https://learn.microsoft.com/en-us/windows/wsl/connect-usb) | 评估 USB 设备接入；不代表具体 CAN 盒受支持 | 已查阅，未实测 |

以上链接是参考入口，不要求现在读完；转载或复用代码前核对对应许可。可公开附件确有需要时再随主题存放，不整包搬运SDK。
