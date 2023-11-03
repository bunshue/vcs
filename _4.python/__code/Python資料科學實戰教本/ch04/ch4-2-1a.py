import requests
from bs4 import BeautifulSoup

r = requests.get("https://fchart.github.io/ML/Surveys.html")
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
print(soup)



