import requests
import re

# 超好用的10個Win10小技巧，學會讓你事半功倍！ | 零度解說
url = 'https://www.youtube.com/watch?v=36asE86iGmQ'

html = requests.get(url)

#取得包含/watch的內容
res1 = re.findall(r'/watch[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', html.text)

print('連線到某youtube影片, 抓取此頁面的所有影片連結')
print('共有', len(res1), '個連結')
print(res1)

