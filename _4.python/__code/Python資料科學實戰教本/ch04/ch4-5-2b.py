import re
from bs4 import BeautifulSoup

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用正規表達式搜尋URL網址
url_regexp = re.compile("^http:")
tag = soup.find(href=url_regexp)
print(tag["href"], tag.text)
print("---------------------")
tag_list = soup.find_all(href=url_regexp)
for tag in tag_list:
    print(tag["href"], tag.text)