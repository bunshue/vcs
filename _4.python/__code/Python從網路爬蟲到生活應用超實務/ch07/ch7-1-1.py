import requests
from bs4 import BeautifulSoup

url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
span = soup.find('span', class_="current")
print(span.text)
print(span.get("aria-label"))

