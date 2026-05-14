本技能包基于 [qiye45/wechatDownload](https://github.com/qiye45/wechatDownload) 项目简化而成，方便患者/家属快速下载和保存，胰腺病情资料中的公众号文章。

于此也特别感谢作者[qiye45/wechatDownload](https://github.com/qiye45/wechatDownload)❤️ 原创，请支持/fork/star！

## 简化架构说明

- 放弃了本地MCP服务，本技能包可以直接发给龙虾/hermes部署。
  
Linux 环境，**无法运行** Windows/macOS 版微信桌面客户端，因此：
- ❌ 本地 MCP (`http://127.0.0.1:4545/mcp`) 不可用
- ✅ **始终使用远程 MCP**: `https://changfengbox.top/api/mcp`

- 支持功能：
| 功能 | 工具名 | 状态 |
|------|--------|------|
| 下载单篇文章 | `wechat` | ✅ 可用 |
| 下载合集/专辑 | `wechat_collection` | ✅ 可用 |

- 其它放弃能力（不适配病友大众需求）
| 批量下载公众号全部文章 | `batch_download_articles` | ❌ 需本地 |
| 获取公众号密钥 | `get_public_account_id` | ❌ 需本地 |
| 导出文章元数据CSV | `export_article_data` | ❌ 需本地 |


感谢小胰宝和小x宝社区的❤️贡献！
