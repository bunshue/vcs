from bs4 import BeautifulSoup
import re
from selenium import webdriver

url = "https://www.bloomberg.com/quote/CCMP:IND"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
soup = BeautifulSoup(driver.page_source, "lxml")
regex = re.compile('^companyName.*')
name_box = soup.find("h1", class_= regex)
name = name_box.text
print(name)
price_box = soup.find("span", attrs={"class":re.compile("^priceText.*")})
price = price_box.text
print(price)
driver.quit()