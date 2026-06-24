# TreasureChest-
百宝箱啥都有（Danko Peter）

## shell 分支

本分支用于 load_test 相关的 shell 自动化测试。

### 内容

- `shell_test/testcase.sh`：主测试入口，按测试 case 依次设置日志配置、执行测试并收集结果。
- `shell_test/setlogconfig.bash`：根据 case 名称生成 `logConfig.cfg`，并从日志中提取 throughput 结果。
- `shell_test/download.sh`：从 Jenkins 输出目录下载新版测试二进制。
- `shell_test/L12test.sh`、`shell_test/L2test.sh`：启动 fgw/bgw/app/ue/slim_engine_test 等进程执行链路测试。
- `shell_test/testcase_other.sh`：其他测试 case 的辅助入口。
- `shell_test/unittest.bats`：基于 bats 的 shell 单元测试。
- `shell_test/backupagent/`：appserver throughput 测试、远端触发和结果整理脚本。
- `vi_source/`：基础 UE/Nexus SDK 测试脚本。

### 用途

- 自动下载并替换 load_test 测试程序。
- 批量执行 L1/L2 不同方向的 throughput 测试。
- 自动生成测试配置并启动/停止相关服务进程。
- 收集 fgw、bgw、app、ue 日志中的吞吐结果并整理成测试输出。
