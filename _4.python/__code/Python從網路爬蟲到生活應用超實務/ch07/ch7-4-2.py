from bs4 import BeautifulSoup
from selenium import webdriver
import time, json

url = "https://www.momoshop.com.tw/search/searchShop.jsp?keyword=nike NBA&searchType=1&curPage=1&_isFuzzy=0&showType=chessboardType"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)

items = []
count = 1
page = 1
while True:
    print("抓取: 第" + str(page) + "頁 網路資料中...")
    page = page + 1
    soup = BeautifulSoup(driver.page_source, "lxml")
    tag_ul = soup.select_one("div.listArea > ul")
    tag_lis = tag_ul.find_all("li")
    for tag_li in tag_lis:
        title = tag_li.find("h3", class_="prdName")
        price = tag_li.find("span", class_="price").find("b")
        items.append({"id": count,
                      "title": title.text,
                      "price": price.text})  
        print("已經擷取:", count, "筆") 
        count = count + 1

    btn_css = "div.pageArea.topPage > dl > dd > a"    
    button = driver.find_elements_by_css_selector(btn_css)
    if button[len(button)-1].text == "下一頁":
        button[len(button)-1].click()
    else:
        break
    time.sleep(10)    
driver.quit()

with open("momo_items.json", "w", encoding="utf-8") as fp:
    json.dump(items,fp,indent=2,sort_keys=True,ensure_ascii=False)