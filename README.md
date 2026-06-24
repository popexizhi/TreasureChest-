# TreasureChest-
百宝箱啥都有（Danko Peter）

## attack-tool 分支

本分支用于备份和保存测试过程中使用的攻击/网络测试工具及编译结果。

### 内容

- `lcx/`：lcx 端口转发/代理相关二进制工具，包含 Linux 与 Windows 版本。
- `nc/`：netcat/nc 相关二进制工具，包含 Linux 与 Windows 版本。
- `tool-bind_cpu/`：CPU 绑定和压测小工具。
  - `bind_one.c`：创建线程并绑定到指定 CPU 核心，持续执行计算用于 CPU 压力测试。
  - `bind_one`：对应编译产物。

### 用途

- 保存常用网络测试工具的不同平台版本。
- 备份攻击模拟、连通性测试、端口转发测试中使用的二进制文件。
- 提供简单 CPU 绑定压测程序，用于验证 CPU 亲和性或制造单核负载。

