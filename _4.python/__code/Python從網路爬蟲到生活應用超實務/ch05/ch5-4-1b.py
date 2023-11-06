import requests

url = "https://www.momoshop.com.tw/main/Main.jsp"
r = requests.get(url)
print(r.status_code)
print(r.text)
