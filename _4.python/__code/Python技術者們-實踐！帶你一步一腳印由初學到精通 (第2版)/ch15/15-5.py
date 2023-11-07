import requests

response = requests.get(' https://zh.wikipedia.org/zh-tw/愛因斯坦')
if response.status_code == 200:
	print(response.text)
