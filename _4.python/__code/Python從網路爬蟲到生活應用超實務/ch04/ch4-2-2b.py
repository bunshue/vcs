import requests 

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

cookies = { "over18": "1" }
r = requests.get(url, cookies=cookies)
print(r.text)




