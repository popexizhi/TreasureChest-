# TreasureChest-
百宝箱啥都有（Danko Peter）

## webmod 分支

本分支用于展示 Cluster 历史测试结果，技术栈为 Flask + MySQL + HTML/JavaScript。

### 内容

- `webmod/flask_web.py`：Flask Web 服务入口。
  - `/cluter_list/<list_name>`：返回测试报告列表页面。
  - `/cluter_test/<report_name>`：按报告名称返回测试数据 JSON。
- `webmod/dbget.py`：连接 MySQL 并读取 Cluster 测试报告数据。
- `webmod/dbget_insert.py`：测试结果入库和历史数据统计辅助代码。
- `webmod/dbget_test.py`：数据库读取测试脚本。
- `webmod/webmod/index.html`：报告列表展示页面。
- `webmod/webmod/cluster_test_report_template.html`：单个测试报告模板。
- `webmod/webmod/proxy.html`：proxy 相关展示页面。
- `webmod/webmod/lib/`：页面依赖的 CSS、图片和静态资源。
- `webmod/testdata/`：测试数据样例。
- `vi_source/`：基础 UE/Nexus SDK 测试脚本。

### 启动方式

```bash
cd webmod
python flask_web.py
```

### 用途

- 从 MySQL 读取 Cluster 历史测试结果。
- 展示测试报告列表。
- 按报告名称查看测试项和测试值。
- 提供简单 HTML 页面用于测试数据查看和结果对比。
