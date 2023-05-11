import requests
import re

videourlList = []

# 超好用的10個Win10小技巧，學會讓你事半功倍！ | 零度解說
url = 'https://www.youtube.com/watch?v=36asE86iGmQ'

html = requests.get(url)
res1 = re.findall(r'/watch[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', html.text)  #取得包含/watch的內容
for temurl in res1:
    if 'list=' and 'index=' in temurl:  #必須包含list=及index=
        if temurl not in videourlList:  #如果串列中不存在就加入串列
        videourlList.append(temurl)
print(videourlList)

