import time, csv
from selenium import webdriver
from bs4 import BeautifulSoup

keyword = "dog"
url = "http://imgur.com/search?q=" + keyword
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
for x in range(3):
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(3)

soup = BeautifulSoup(driver.page_source, "lxml")
images = soup.find_all("a", class_="image-list-link")
print("圖檔數:", len(images))
with open("imgur_dog.csv", "w+", newline="", encoding="big5") as fp:
    writer = csv.writer(fp)
    writer.writerow(["image-href"])
    for img in images:
        imgUrl = "http:" + img.find("img").get("src")
        writer.writerow([imgUrl])

print("成功建立 imgur_dog.csv 檔...")
driver.quit()
