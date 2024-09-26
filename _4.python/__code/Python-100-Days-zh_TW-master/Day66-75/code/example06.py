#實例 - 緩存知乎發現上的鏈接和頁面代碼

from hashlib import sha1
from urllib.parse import urljoin

import pickle
import re
import requests
import zlib

from bs4 import BeautifulSoup

def main():
    # 指定種子頁面
    base_url = 'https://www.zhihu.com/'
    seed_url = urljoin(base_url, 'explore')

    # 設置用戶代理(否則訪問會被拒絕)
    headers = {'user-agent': 'Baiduspider'}
    # 通過requests模塊發送GET請求並指定用戶代理
    resp = requests.get(seed_url, headers=headers)
    # 創建BeautifulSoup對象並指定使用lxml作為解析器
    soup = BeautifulSoup(resp.text, 'lxml')
    href_regex = re.compile(r'^/question')
    # 將URL處理成SHA1摘要(長度固定更簡短)
    hasher_proto = sha1()

    # 查找所有href屬性以/question打頭的a標籤
    for a_tag in soup.find_all('a', {'href': href_regex}):
        # 獲取a標籤的href屬性值並組裝完整的URL
        href = a_tag.attrs['href']
        full_url = urljoin(base_url, href)
        # 傳入URL生成SHA1摘要
        hasher = hasher_proto.copy()
        hasher.update(full_url.encode('utf-8'))
        field_key = hasher.hexdigest()
        print(full_url)
        """
        html_page = requests.get(full_url, headers=headers).text
        # 对页面进行序列化和压缩操作
        zipped_page = zlib.compress(pickle.dumps(html_page))
        """

if __name__ == '__main__':
    main()

