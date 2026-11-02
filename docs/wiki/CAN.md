# CAN

一种让多个设备在同一条总线上交换消息的通信方式。电脑通常通过 [CAN盒](CAN%E7%9B%92.md) 接入，用 [报文](%E6%8A%A5%E6%96%87.md) 交换数据。

CAN 规定消息怎样传输，但不会统一规定“哪几个字节表示电机温度”。这些含义要看设备协议，例如 [CANopen](CANopen.md) 或厂商自己的协议。这里单独说“经典 CAN”时，指与 [CAN FD](CAN%20FD.md) 对比的传统帧格式。

参考：Kvaser：CAN 教程：`https://kvaser.com/can-protocol-tutorial/`。

## 哪些名词与它有关

[CAN盒](CAN%E7%9B%92.md)、[CANopen](CANopen.md)、[报文](%E6%8A%A5%E6%96%87.md)、[串口](%E4%B8%B2%E5%8F%A3.md)、[Qt](Qt.md)、[CAN FD](CAN%20FD.md)、[SDK](SDK.md)。

[返回名词目录](README.md)
