from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
tags = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for tag in tags:
    href = tag.get_attribute('href')
    links.append(href)
print(len(links))

wait = WebDriverWait(driver, 10)
for link in links:
    driver.get(link)
    num = link.strip('https://www.youtube.com/watch?v=')
    title = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,"div#container > h1"))).text
    description =  wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,"div#description"))).text
    print("編號:", num)
    print("名稱:", title.strip())
    print("描述:", description.strip())
    print("---------------------------")
driver.quit()