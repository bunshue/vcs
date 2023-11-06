from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=65"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
soup = BeautifulSoup(driver.page_source, "lxml")
span = soup.select_one("span.tem-C.is-active")
print(span.text)
driver.quit()
