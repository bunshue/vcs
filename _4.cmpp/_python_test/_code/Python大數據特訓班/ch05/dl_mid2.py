import requests
import re

videourlList = []

url = 'https://www.youtube.com/watch?v=hGRplpwjbr0&list=PL316wRwpvsnHZprsPfXM8yPzyZ41bvuWl'
html = requests.get(url)
res1 = re.findall(r'/watch[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', html.text)  #取得包含/watch的內容
for temurl in res1:
    if 'list=' and 'index=' in temurl:  #必須包含list=及index=
        videourlList.append(temurl)
print(videourlList)
