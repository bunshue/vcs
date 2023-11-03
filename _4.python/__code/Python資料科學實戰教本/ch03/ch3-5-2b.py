import requests   

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
cookies = { "over18": "1" }
r = requests.get(url, cookies=cookies, headers=headers)
print(r.text)

