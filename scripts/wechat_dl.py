#!/usr/bin/env python3
"""
WeChat Article Downloader - MCP Client
Usage:
  python wechat_dl.py <article_url> [--format html,md,pdf] [--output ./output]
  python wechat_dl.py --collection <collection_url> [--format html,md]
"""
import requests
import json
import sys
import os
import argparse
from datetime import datetime

MCP_URL = "https://changfengbox.top/api/mcp"
TIMEOUT = 120

FORMAT_MAP = {
    "html": "HTML",
    "md": "MD",
    "pdf": "PDF",
    "word": "WORD",
    "docx": "WORD",
    "txt": "TXT",
    "mhtml": "MHTML",
}

def call_mcp(tool_name, arguments):
    payload = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "id": 1,
        "params": {"name": tool_name, "arguments": arguments}
    }
    resp = requests.post(MCP_URL, json=payload,
                         headers={"Content-Type": "application/json"},
                         timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.json()

def build_config(formats, add_date=True):
    config = {"保存离线网页": True, "文件开头添加日期": add_date}
    for key in FORMAT_MAP.values():
        config[key] = False
    for f in formats:
        key = FORMAT_MAP.get(f.lower())
        if key:
            config[key] = True
    # Default: at least HTML + MD
    if not any(config[k] for k in ["HTML", "MD", "PDF", "WORD", "TXT", "MHTML"]):
        config["HTML"] = True
        config["MD"] = True
    return config

def extract_title_from_url(url):
    """从 MCP 返回的下载 URL 中提取文章标题作为文件名"""
    import urllib.parse
    decoded = urllib.parse.unquote(url)
    # 取文件名部分（去掉路径和扩展名）
    basename = os.path.basename(decoded)
    name, _ = os.path.splitext(basename)
    return name if name else None

def download_file(remote_url, output_dir):
    """下载远程文件到本地，返回本地路径"""
    resp = requests.get(remote_url, timeout=30)
    resp.raise_for_status()
    # 从 URL 提取文件名
    title = extract_title_from_url(remote_url)
    ext = os.path.splitext(remote_url.split("?")[0])[1] or ".md"
    filename = f"{title}{ext}" if title else f"download{ext}"
    local_path = os.path.join(output_dir, filename)
    # 检测编码
    for enc in ['utf-8', 'gbk', 'gb2312', 'latin-1']:
        try:
            text = resp.content.decode(enc)
            break
        except:
            continue
    with open(local_path, 'w', encoding='utf-8') as f:
        f.write(text)
    return local_path, filename

def download_article(url, formats=("html", "md"), output_dir="./wechat-downloads"):
    os.makedirs(output_dir, exist_ok=True)
    config = build_config(formats)
    print(f"[*] Downloading article: {url}")
    print(f"[*] Config: {json.dumps(config, ensure_ascii=False)}")
    result = call_mcp("wechat", {"url": url, "config": config})
    # 解析返回的下载链接并下载到本地
    try:
        content = result.get("result", {}).get("content", [])
        for item in content:
            data = json.loads(item.get("text", "{}"))
            for dl_url in data.get("urls", []):
                local_path, filename = download_file(dl_url, output_dir)
                print(f"[*] Saved: {local_path}")
                return local_path, filename
    except Exception as e:
        print(f"[!] Parse error: {e}")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return None, None

def download_collection(url, formats=("html", "md"), output_dir="./wechat-downloads"):
    os.makedirs(output_dir, exist_ok=True)
    config = build_config(formats)
    print(f"[*] Downloading collection: {url}")
    print(f"[*] Config: {json.dumps(config, ensure_ascii=False)}")
    result = call_mcp("wechat_collection", {"url": url, "config": config})
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result

def main():
    parser = argparse.ArgumentParser(description="WeChat Article Downloader via MCP")
    parser.add_argument("url", nargs="?", help="Article URL (mp.weixin.qq.com)")
    parser.add_argument("--collection", "-c", help="Collection URL (appmsgalbum)")
    parser.add_argument("--format", "-f", default="html,md", help="Formats: html,md,pdf,word,txt,mhtml")
    parser.add_argument("--output", "-o", default="./wechat-downloads", help="Output directory")
    args = parser.parse_args()

    formats = tuple(args.format.split(","))

    if args.collection:
        download_collection(args.collection, formats, args.output)
    elif args.url:
        download_article(args.url, formats, args.output)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
