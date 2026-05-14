# WeChat Article Downloader

**Language Selection | 语言选择 | Выбор языка:**

[中文](#中文) | [English](#english) | [Русский](#русский)

---

## 中文

本技能包基于 [qiye45/wechatDownload](https://github.com/qiye45/wechatDownload) 项目简化而成，方便患者/家属快速下载和保存，胰腺病情资料中的公众号文章。

于此也特别感谢作者[qiye45/wechatDownload](https://github.com/qiye45/wechatDownload)❤️ 原创，请支持/fork/star！

### 简化架构说明

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

---

## English

This skill package is a simplified version based on the [qiye45/wechatDownload](https://github.com/qiye45/wechatDownload) project, making it convenient for patients/families to quickly download and save WeChat official account articles related to pancreatic disease information.

We also extend special thanks to the author of [qiye45/wechatDownload](https://github.com/qiye45/wechatDownload)❤️ for the original creation. Please support/fork/star!

### Simplified Architecture Overview

- Abandoned local MCP service; this skill package can be deployed directly to Lobster/Hermes.

In a Linux environment, **unable to run** WeChat desktop clients for Windows/macOS, therefore:
- ❌ Local MCP (`http://127.0.0.1:4545/mcp`) is unavailable
- ✅ **Always use remote MCP**: `https://changfengbox.top/api/mcp`

- Supported Features:
| Feature | Tool Name | Status |
|---------|-----------|--------|
| Download single article | `wechat` | ✅ Available |
| Download collection/series | `wechat_collection` | ✅ Available |

- Other abandoned capabilities (not suitable for general patient needs):
| Batch download all articles from official account | `batch_download_articles` | ❌ Local required |
| Get official account key | `get_public_account_id` | ❌ Local required |
| Export article metadata CSV | `export_article_data` | ❌ Local required |

Thanks to the ❤️ contributions from the Xiaoyibao and Xiaoxbao community!

---

## Русский

Этот пакет навыков является упрощенной версией проекта [qiye45/wechatDownload](https://github.com/qiye45/wechatDownload), позволяющей пациентам/семьям быстро загружать и сохранять статьи официального аккаунта WeChat, связанные с информацией о заболевании поджелудочной железы.

Мы также выражаем особую благодарность автору [qiye45/wechatDownload](https://github.com/qiye45/wechatDownload)❤️ за оригинальное создание. Пожалуйста, поддержите/форк/звезду!

### Упрощенное описание архитектуры

- Отказался от локального MCP-сервиса; этот пакет навыков можно развертывать непосредственно на Lobster/Hermes.

В окружении Linux **невозможно запустить** клиентов WeChat для Windows/macOS, следовательно:
- ❌ Локальный MCP (`http://127.0.0.1:4545/mcp`) недоступен
- ✅ **Всегда используйте удаленный MCP**: `https://changfengbox.top/api/mcp`

- Поддерживаемые функции:
| Функция | Имя инструмента | Статус |
|---------|-----------------|--------|
| Загрузить одну статью | `wechat` | ✅ Доступно |
| Загрузить коллекцию/серию | `wechat_collection` | ✅ Доступно |

- Другие отброшенные возможности (не подходит для общих потребностей пациентов):
| Массовая загрузка всех статей с официального аккаунта | `batch_download_articles` | ❌ Требуется локально |
| Получить ключ официального аккаунта | `get_public_account_id` | ❌ Требуется локально |
| Экспортировать метаданные статей в CSV | `export_article_data` | ❌ Требуется локально |

Спасибо ❤️ вкладам сообщества Xiaoyibao и Xiaoxbao!
