from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL="https://www.momoshop.com.tw/search/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(URL+"searchShop.jsp?keyword=NBA")
print("-----------------------------")
print(driver.title)
html = driver.page_source
fp = open("NBA.html", "w", encoding="utf8")
fp.write(html)
print("寫入檔案NBA.html...")
fp.close()
driver.quit()
 