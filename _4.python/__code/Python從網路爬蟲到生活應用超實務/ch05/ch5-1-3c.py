import requests
from bs4 import BeautifulSoup 

url = "https://fchart.github.io/Elements.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
tags_li = soup.find_all("li", class_="response", limit=3)
print(tags_li)

