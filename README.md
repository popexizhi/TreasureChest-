# TreasureChest-
百宝箱啥都有（Danko Peter）

## vi 分支

本分支用于保存 Vim 配置，并保留基础 UE/Nexus SDK 测试脚本。

### 内容

- `.vimrc`：Vim 基础配置。
  - tab 宽度设置为 4。
  - 启用空格缩进。
  - 启用自动缩进。
  - 显示光标列。
  - 显示行号。
- `vi_source/get_host.vi`：用于把 host 列表文本转换成 Python 风格列表变量的 Vim 脚本。
- `vi_source/get_host.sh`、`vi_source/sta.sh`：配合 `get_host.vi` 生成 host 列表、复制 UE 代码并启动客户端。
- `vi_source/uecode/`：基础 UE/Nexus SDK 测试代码。

### 用途

- 备份个人 Vim 编辑器配置。
- 使用 Vim 脚本辅助生成测试 host 列表。
- 保留基础 UE 客户端批量启动和 L2 测试脚本。
