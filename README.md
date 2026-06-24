# TreasureChest-
百宝箱啥都有（Danko Peter）

## tool 分支

本分支是综合工具集合，包含 Cluster 测试结果展示、IOC pcap 抓包、WebSocket 数据模拟和 Windows 检查/通知脚本。

### 内容

- `webmod/`：基于 Flask + MySQL + HTML/JavaScript 的 Cluster 历史测试结果展示工具。
  - `flask_web.py`：Web 服务入口。
  - `dbget.py`、`dbget_insert.py`：MySQL 查询、插入和统计辅助代码。
  - `webmod/*.html`：报告页面和模板。
- `pcap_tool/`：IOC pcap 抓包和检索工具。
  - `get_pcap_tool.sh`：通过 `dig ${ioc} @${dns_server}` 触发 IOC 查询，同时用 tcpdump 抓取该时间段 pcap。
  - `search_pcap_tool/search_dir_pcap`：遍历目录内 pcap 文件并按关键字检索。
- `websocket/`：级联 WebSocket 数据模拟工具。
  - `wss_client.py`：创建多个 WebSocket 客户端并周期性发送模拟数据。
  - `data.py`、`mapping_check.py`：模拟数据、设备 ID、节点映射和检查条件。
- `windows_check/`：Windows 检查和通知相关脚本。
  - `sendMail.py`、`sender.py`：邮件/接口通知发送。
  - `try_dir.ahk`：AutoHotkey 辅助脚本。
- `.gitlab-ci.yml`：简单 CI 测试配置。
- `vi_source/`：基础 UE/Nexus SDK 测试脚本。

### 使用示例

启动 Web 展示服务：

```bash
cd webmod
python flask_web.py
```

抓取 IOC 查询 pcap：

```bash
bash pcap_tool/get_pcap_tool.sh ${ioc}
```

### 用途

- 展示 Cluster 历史测试结果。
- 按 IOC 触发 DNS 查询并保存 pcap。
- 在 pcap 目录中批量检索关键流量。
- 模拟多节点 WebSocket 级联上报数据。
- 辅助 Windows 环境检查和邮件/接口通知。
