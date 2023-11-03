from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '/html/body/ol')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(By.XPATH, '//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()
