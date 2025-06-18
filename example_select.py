#!/usr/bin/env python3

import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from lxml import etree

def get_all_namew(base_url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    page_nums = range(0,5)
    for page_num in page_nums:
        url = urljoin(base_url, f'page/{page_num}')
        #print(f"正在获取第 {page_num} 页数据: {url}")
        try:
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()  # 检查请求是否成功
        except requests.RequestException as e:
            print(f"请求失败: {e}")
        soup = BeautifulSoup(response.text, "html.parser")
        names = soup.select('#post-panel > div.blog-post > div > div.post-meta.wrapper-lg > h2 > a')
        for name in names:
            print(name.get_text())
        #links = soup.select('a')
        #html = etree.HTML(response.text)
        #names = html.xpath('//*[@id="post-panel"]/div[1]/div[1]/div[2]/h2/a/text()')
        #with open('limbopro.txt', 'w', encoding='utf-8') as f:
        #    for link in links:
        #        href = link.get('href')
        #        if href and 'www.yinfans.me' in href:
        #            #print(f"{link.get_text().strip()}")
        #            f.write(f"{href}\n")

if __name__ == "__main__":
    base_url = 'https://limbopro.com/'
    get_all_namew(base_url)