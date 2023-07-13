import json
import urllib.parse
import requests
url = "https://udn.com/api/more?page=2&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=6561"
html = requests.get(url).text
data = json.loads(html)


titles = data['lists']
for title in titles:
    print(title['title'])
    print(urllib.parse.urljoin("https://udn.com", title['titleLink']))

import requests
url = "https://ck101.com/forum-3590-1.html?ref=nav"
res = requests.get(url)
print(res)
print(res.text)

import requests
url = "https://ck101.com/forum-3590-1.html?ref=nav"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
res = requests.get(url, headers=headers)
print(res)
print(res.text)

