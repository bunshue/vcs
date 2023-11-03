from bs4 import BeautifulSoup

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有文字內容串列
tag_str_list = tag_div.find_all(text=True)
print(tag_str_list)
# 找出指定的文字內容串列
tag_str_list = tag_div.find_all(text=["20", "40"])
print(tag_str_list)

