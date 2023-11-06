from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tags = soup.select("#video-title")
links = []
for tag in tags:
    href = tag["href"]
    if href:
        links.append(href)
        print(href)
print(len(links))
driver.quit()