# 发布《孙学实操攻略》到 GitHub

- 公开仓库：[AIPMAndy/sunxue-practical-guide](https://github.com/AIPMAndy/sunxue-practical-guide)
- 在线阅读：[孙学实操攻略](https://aipmandy.github.io/sunxue-practical-guide/)
- 全文文章：[图文阅读页](https://aipmandy.github.io/sunxue-practical-guide/article.html)

GitHub Pages 使用 `main` 分支的根目录 `/`，后续推送会自动触发部署。根目录 `.nojekyll` 保留静态文件的原有路径。`.github/workflows/check.yml` 在推送和 Pull Request 时检查内容、内部链接与首页脚本。

## 本地验证

```bash
python3 scripts/check_content.py
node scripts/check_ui_syntax.js
python3 -m http.server 8000
```

本地服务启动后打开 `http://localhost:8000/`。也可下载整个仓库，解压后双击 `index.html` 离线使用。

## 更新后验收

1. 确认 GitHub Actions 的内容检查和 Pages 部署均成功。
2. 打开在线首页、全文、练习、Prompt、模板、历史与来源页，确认图片及链接可用。
3. 勾选七天打卡任务，刷新后应保留记录；清空后刷新仍应为 0 项。
4. 用手机检查导航、图片和正文宽度。

浏览器打卡记录仅保存在本机。公众号粘贴是另一条发布流程，仍需在公众号编辑器和手机预览中额外检查。
