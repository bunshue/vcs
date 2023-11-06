from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()