from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute('innerHTML'))
soup = BeautifulSoup(tag_ol.get_attribute('innerHTML'), "lxml")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()