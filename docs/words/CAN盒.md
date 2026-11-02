# CAN盒

电脑接入 [CAN](CAN.md) 总线的硬件适配器，也常被叫作 USB-CAN 适配器。电脑通过它发送和接收 [报文](%E6%8A%A5%E6%96%87.md)，是否支持 [CAN FD](CAN%20FD.md) 要看具体型号。

电脑一侧可能通过 [USB](USB.md) 连接，但程序访问方式并不统一：有的提供 [COM口](COM%E5%8F%A3.md)，有的需要专用 [驱动](%E9%A9%B1%E5%8A%A8.md) 与 [SDK](SDK.md)。CAN 盒也不一定懂 [CANopen](CANopen.md) 或某款电机的命令含义。

参考：Kvaser：打开 CAN 通道：`https://kvaser.com/canlib-webhelp/page_user_guide_chips_channels.htm`。

## 哪些名词与它有关

[上位机](%E4%B8%8A%E4%BD%8D%E6%9C%BA.md)、[Python](Python.md)、[串口](%E4%B8%B2%E5%8F%A3.md)、[COM口](COM%E5%8F%A3.md)、[串口助手](%E4%B8%B2%E5%8F%A3%E5%8A%A9%E6%89%8B.md)、[USB](USB.md)、[驱动](%E9%A9%B1%E5%8A%A8.md)、[CAN](CAN.md)、[CAN FD](CAN%20FD.md)。

[返回名词目录](README.md)
