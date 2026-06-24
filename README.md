# TreasureChest-
百宝箱啥都有（Danko Peter）

## batch_do 分支

本分支用于多机批量处理和测试环境运维自动化。

### 内容

- `auto_tool/batch_do`：按主机列表批量执行操作，包含 tap 网卡配置、pcap 回放任务下发、tcpreplay 修复、hotfix 脚本下发等。
- `auto_tool/hosts_do`、`auto_tool/hosts_doX`：读取主机列表后，通过 SSH/SCP 批量复制并执行指定脚本。
- `auto_tool/cron.sh`：定时遍历 pcap 文件并通过 `tcpreplay` 回放到 tap 网卡。
- `auto_tool/auto_hotfix_edit`、`auto_tool/auto_hotfix_edit_only`：hotfix 版本检测、MySQL 记录处理和版本文件调整脚本。
- `auto_tool/add_tap0/`、`auto_tool/add_tap0X/`：tap 虚拟网卡相关配置脚本。
- `auto_tool/git_backup`、`auto_tool/git_add`：工具目录备份和提交辅助脚本。
- `auto_tool/backup_authorized_keys`、`auto_tool/add_key`：SSH key 备份和下发辅助脚本。

### 用途

- 对多台测试机批量下发脚本并执行维护任务。
- 批量配置 tap 虚拟网卡和 pcap 回放环境。
- 自动处理测试环境中的 hotfix 升级/回退准备工作。
- 备份自动化工具和主机 SSH 配置。
