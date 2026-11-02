# BRS

Bit Rate Switch，速率切换。在 [CAN FD](CAN%20FD.md) 报文中，它表示是否切换到配置好的数据阶段速率；调试软件里所说的“FD 加速”常指这个功能，仍应核对软件说明。

例如仲裁阶段配置 1 Mbit/s、数据阶段配置 5 Mbit/s，启用 BRS 后数据阶段可以用后者。它不是整条操作都快五倍，也不是电机每秒运动脉冲数；界面显示“PPS”时，应另查该字段的定义。

参考：Kvaser：CAN FD 教程：`https://kvaser.com/can-fd-protocol-tutorial/`。

## 哪些名词与它有关

[CAN FD](CAN%20FD.md)。

[返回名词目录](README.md)
