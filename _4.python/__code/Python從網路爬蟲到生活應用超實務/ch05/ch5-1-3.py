import requests
from bs4 import BeautifulSoup 

url = "https://fchart.github.io/Elements.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
tag = soup.select_one("h2")
print("h2: ", tag.text)
tags = soup.select("b")
print("b: ", tags[0].text)
tag = soup.select_one("#q2")
tag2 = tag.select_one("b")
print("b: ", tag2.text)
tags = soup.select(".response")
print("li: ", tags[0].text)
print("li: ", tags[1].text)

