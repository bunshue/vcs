from selenium import webdriver
import time

url = "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&jobcatExpansionType=1&order=12&asc=0&page=6&mode=s&jobsource=2018indexpoc"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
print(len(driver.page_source))
for x in range(5):
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(3)
    print(x+1, len(driver.page_source))
driver.quit()