from bs4 import BeautifulSoup

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有<li>子孫標籤
tag_list = tag_div.find_all("li")
for tag in tag_list:
    print(tag.text.replace("\n", ""))
# 沒有使用遞迴來找出所有<li>標籤
tag_list = tag_div.find_all("li", recursive=False)
print(tag_list)

