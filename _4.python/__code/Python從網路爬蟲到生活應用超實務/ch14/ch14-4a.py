import requests

date = "20200820"
url = "https://www.twse.com.tw/fund/T86?response=csv&date={}&selectType=ALL"
r = requests.get(url.format(date))
content = r.content
csv_file = open("three_major.csv", "wb")
csv_file.write(content)
csv_file.close()