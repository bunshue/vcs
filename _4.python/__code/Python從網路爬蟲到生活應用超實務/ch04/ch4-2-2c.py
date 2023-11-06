from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome("./chromedriver", options=options)
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()