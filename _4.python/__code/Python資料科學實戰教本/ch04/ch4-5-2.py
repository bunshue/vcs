import re
from bs4 import BeautifulSoup

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用正規表達式搜尋文字內容
tag_str = soup.find(text="男 -")
print(tag_str)
regexp = re.compile("男 -")
tag_str = soup.find(text=regexp)
print(tag_str)
print("---------------------")
regexp = re.compile("\w+ -")
tag_list = soup.find_all(text=regexp)
print(tag_list)