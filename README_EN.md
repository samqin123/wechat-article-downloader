# WeChat Article Downloader

This toolkit is a simplified version based on the [qiye45/wechatDownload](https://github.com/qiye45/wechatDownload) project, designed to help patients and families quickly download and save WeChat public account articles related to pancreatic disease information.

Special thanks to the original author [qiye45/wechatDownload](https://github.com/qiye45/wechatDownload) ❤️ for the original creation. Please support/fork/star the original project!

## Simplified Architecture Overview

- Removed dependency on local MCP service - this toolkit can be deployed directly to Lobster/Hermes.

**Note for Linux environments:** Since Linux cannot run the WeChat desktop client for Windows/macOS:
- ❌ Local MCP (`http://127.0.0.1:4545/mcp`) is **NOT available**
- ✅ **Always use remote MCP**: `https://changfengbox.top/api/mcp`

## Supported Features

| Feature | Tool Name | Status |
|---------|-----------|--------|
| Download single article | `wechat` | ✅ Available |
| Download collection/album | `wechat_collection` | ✅ Available |

## Deprecated Features (not adapted for general user needs)

| Feature | Tool Name | Status |
|---------|-----------|--------|
| Batch download all articles from public account | `batch_download_articles` | ❌ Requires local setup |
| Get public account key | `get_public_account_id` | ❌ Requires local setup |
| Export article metadata to CSV | `export_article_data` | ❌ Requires local setup |

---

**Special thanks to the Xiaoyibao and Xiaoxbao communities for their ❤️ contributions!**

## Installation and Usage

For detailed instructions and the complete feature-rich original version, please visit the [original project](https://github.com/qiye45/wechatDownload).

## License

For license information, please refer to the original project.
