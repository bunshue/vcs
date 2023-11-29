import sys
from selenium import webdriver

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
tags = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for tag in tags:
    href = tag.get_attribute('href')
    if href:
        links.append(href)
        print(href)
print(len(links))
driver.quit()

print('------------------------------------------------------------')	#60個

from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tags = soup.select("#video-title")
links = []
for tag in tags:
    href = tag["href"]
    if href:
        links.append(href)
        print(href)
print(len(links))
driver.quit()

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)

for x in range(5):
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    time.sleep(5)

tags = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for tag in tags:
    href = tag.get_attribute('href')
    if href:
        links.append(href)
print(len(links))

df = pd.DataFrame(columns=["id", "title", "description"])
wait = WebDriverWait(driver, 10)
for link in links:
    driver.get(link)
    num = link.strip('https://www.youtube.com/watch?v=')
    title = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,"div#container > h1"))).text
    description =  wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,"div#description"))).text
    df.loc[len(df)] = [num, title, description]
    
print(df.head())    
df.to_csv("YouTube.csv",index=False,encoding="utf-8")
driver.quit()

print('------------------------------------------------------------')	#60個

