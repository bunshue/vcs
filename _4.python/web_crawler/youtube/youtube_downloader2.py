'''
使用 requests / BeautifulSoup 做 YouTube下載

'''

print('------------------------------------------------------------')	#60個
print('準備工作')

import re
import requests
from bs4 import BeautifulSoup

#下載資料夾
foldername = 'D:/_git/vcs/_1.data/______test_files2/youtube_download'

#準備輸出資料夾 若不存在, 則建立
if not os.path.exists(foldername):
    os.mkdir(foldername)

# 超好用的10個Win10小技巧，學會讓你事半功倍！ | 零度解說
url = 'https://www.youtube.com/watch?v=36asE86iGmQ'

print('------------------------------------------------------------')	#60個
print('Youtube 測試 1')

html = requests.get(url)

#取得包含/watch的內容
res1 = re.findall(r'/watch[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', html.text)

print('連線到某youtube影片, 抓取此頁面的所有影片連結')
print('共有', len(res1), '個連結')
print(res1)

print('------------------------------------------------------------')	#60個
print('Youtube 測試 2')

videourlList = []

html = requests.get(url)
res1 = re.findall(r'/watch[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', html.text)  #取得包含/watch的內容
for temurl in res1:
    if 'list=' and 'index=' in temurl:  #必須包含list=及index=
        if temurl not in videourlList:  #如果串列中不存在就加入串列
            videourlList.append(temurl)
print(videourlList)

print('------------------------------------------------------------')	#60個
print('Youtube 測試 3')

videourlList = []  #儲存所有影片網址的串列
urltext = '/watch?v=hGRplpwjbr0&list=PL316wRwpvsnHZprsPfXM8yPzyZ41bvuWl'  #黑豹預告片
baseurl = 'https://www.youtube.com'
html = requests.get(baseurl + urltext)
soup = BeautifulSoup(html.text, 'html.parser')
res1 = soup.find_all('a')
for res in res1:
    temurl = baseurl + res.get('href')
    if('&index=' in temurl):
        videourlList.append(temurl)
print(videourlList)

print('\n\nYoutube 測試 作業完成\n')
