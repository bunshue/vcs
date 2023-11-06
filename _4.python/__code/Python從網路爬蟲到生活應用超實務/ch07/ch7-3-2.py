from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://rent.housefun.com.tw/region/еxе_ел/?cid=0000"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)

soup = BeautifulSoup(driver.page_source, "lxml")
div = soup.find("div", id="SearchContent")
items = div.find_all("article")
print(len(items))
for item in items:
    title = item.find("h3", class_="title").find("a")
    if title: print(title.text)
    address = item.find("address", class_="addr")
    if address: print(address.text.strip())
    price = item.find("span", class_="infos num")
    if price: print(price.text)
    print("-------------------")
driver.quit()
