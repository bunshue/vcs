import requests
import re

url = 'https://www.youtube.com/watch?v=36asE86iGmQ'

html = requests.get(url)

#取得包含/watch的內容
res1 = re.findall(r'/watch[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', html.text)

print(res1)

