# TreasureChest-
百宝箱啥都有（Danko Peter）

## dev 分支

本分支用于 appserver/load test 日志分析、数据统计和测试报告生成。

### 内容

- `app_sh/AppLog.py`：解析 app/UE 相关日志，提取关键流程和 UE 事件时间。
- `app_sh/MonApp.py`、`app_sh/MonAppPro.py`：分析 appserver 测试日志，生成吞吐、连接数、proxy 耗时等指标数据。
- `app_sh/DygraphData.py`：按正则解析日志行，处理时间格式和数据入库/导出。
- `app_sh/Static.py`：统计工具，包含平均值、标准差、分位数等数据处理逻辑。
- `app_sh/ReportTemplet*.py`、`ReportIfram.py`、`ReportMap.py`：生成 HTML 报表和图表页面。
- `app_sh/dep_css_js/`：dygraph 及报表页面依赖的 CSS/JavaScript 静态资源。
- `app_sh/app_host/`：样例 app 日志数据。
- `app_sh/shell_con.py`：测试环境进程控制和 shell 命令封装。
- `vi_source/`：基础 UE/Nexus SDK 测试脚本。

### 用途

- 从 appserver/load test 日志中提取性能指标。
- 生成 CSV 数据和 HTML 图表报告。
- 对吞吐、L2 连接数、proxy 请求耗时等指标做统计分析。
- 辅助回放和分析测试环境中的 app/UE 行为。
