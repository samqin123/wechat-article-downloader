---
name: wechat-article-downloader
description: "Download WeChat official account articles via MCP remote server. Supports single articles, collections, multiple formats (HTML/MD/PDF/DOCX)."
version: "1.0.0"
triggers:
  - "下载微信文章"
  - "下载公众号文章"
  - "wechat article download"
  - "mp.weixin.qq.com"
  - "appmsgalbum"
  - "公众号合集"
---

# WeChat Article Downloader

通过远程 MCP 服务器下载微信公众号文章。基于 [qiye45/wechatDownload](https://github.com/qiye45/wechatDownload) 项目。

## 架构说明

本机为 Linux 环境，**无法运行** Windows/macOS 版微信桌面客户端，因此：
- ❌ 本地 MCP (`http://127.0.0.1:4545/mcp`) 不可用
- ✅ **始终使用远程 MCP**: `https://changfengbox.top/api/mcp`

远程 MCP 支持的功能：
| 功能 | 工具名 | 状态 |
|------|--------|------|
| 下载单篇文章 | `wechat` | ✅ 可用 |
| 下载合集/专辑 | `wechat_collection` | ✅ 可用 |
| 批量下载公众号全部文章 | `batch_download_articles` | ❌ 需本地 |
| 获取公众号密钥 | `get_public_account_id` | ❌ 需本地 |
| 导出文章元数据CSV | `export_article_data` | ❌ 需本地 |

## MCP 调用方式

### 1. 下载单篇文章

```python
import requests, json

MCP_URL = "https://changfengbox.top/api/mcp"

def call_mcp_tool(tool_name, arguments):
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "id": 1,
        "params": {"name": tool_name, "arguments": arguments}
    }
    resp = requests.post(MCP_URL, json=payload, headers={"Content-Type": "application/json"}, timeout=120)
    return resp.json()

# 下载单篇文章
result = call_mcp_tool("wechat", {
    "url": "https://mp.weixin.qq.com/s/xxxxxxxxxxxx",
    "config": {
        "保存离线网页": True,
        "HTML": True,
        "MD": True,
        "PDF": False,
        "WORD": False,
        "TXT": False,
        "MHTML": False,
        "文件开头添加日期": True
    }
})
```

### 2. 下载合集（appmsgalbum）

```python
result = call_mcp_tool("wechat_collection", {
    "url": "https://mp.weixin.qq.com/mp/appmsgalbum?...",
    "config": {
        "HTML": True,
        "MD": True,
        "PDF": False,
        "WORD": False,
        "文件开头添加日期": True
    }
})
```

## Config 选项说明

| 键 | 类型 | 说明 |
|----|------|------|
| `保存离线网页` | bool | 保存完整离线网页 |
| `HTML` | bool | 保存为 HTML |
| `MD` | bool | 保存为 Markdown |
| `PDF` | bool | 保存为 PDF |
| `WORD` | bool | 保存为 Word (.docx) |
| `TXT` | bool | 保存为纯文本 |
| `MHTML` | bool | 保存为 MHTML |
| `文件开头添加日期` | bool | 文件名前加日期前缀 |

## 常用配置组合

- **研究/存档**: `HTML=True, MD=True, 保存离线网页=True`
- **分享/打印**: `PDF=True, HTML=True`
- **轻量**: `MD=True, TXT=True`

## 文件命名规则

**默认使用文章标题作为文件名**，从 MCP 返回的下载 URL 中自动提取。例如：
- MCP 返回 URL: `.../患者入排筛选太慢我用AI工作流把一个病例匹配到全球150个试验.md`
- 本地保存为: `患者入排筛选太慢我用AI工作流把一个病例匹配到全球150个试验.md`

## Pitfalls

1. **远程 MCP 有延迟**: 首次调用可能需要 5-15 秒，设置 timeout≥120s
2. **合集下载可能很慢**: 文章多时需要耐心等待
3. **返回结果中的链接**: MCP 返回的下载链接有时效性，及时保存
4. **批量下载不可用**: 远程 MCP 不支持批量下载整个公众号，需要本地 Windows/macOS 环境
5. **URL 格式**: 必须是完整的 `mp.weixin.qq.com` 链接
