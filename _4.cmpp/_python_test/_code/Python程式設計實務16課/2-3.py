import requests
www = requests.get("https://tw.news.yahoo.com/most-popular/")
print(www.text)
