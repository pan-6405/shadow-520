# Shadowrocket 节点自动更新订阅

## 功能
每天自动抓取 9 个免费订阅源 → 合并去重 → 输出前 300 个节点  
生成 Shadowrocket 可导入的订阅链接。

## 使用步骤
1. 在 GitHub 上新建一个空仓库，例如：Shadowrocket-Node-AutoUpdate
2. 打开仓库 → Add file → Create new file
3. 按顺序创建以下文件并复制内容：
   - scripts/fetch_nodes.py
   - .github/workflows/update.yml
   - README.md
   - output/ios.txt（空文件即可）
4. 保存所有文件
5. 打开 **Actions** → 手动运行一次 workflow
6. 获取最新订阅链接：
