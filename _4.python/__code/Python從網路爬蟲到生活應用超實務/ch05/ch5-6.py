from selenium import webdriver
from bs4 import BeautifulSoup
import time

email_address = "<電子郵件地址>"
password = "<密碼>"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
url = "https://www.facebook.com/"
driver.get(url)

email = driver.find_element_by_css_selector("#email")
email.send_keys(email_address)
time.sleep(0.5)
passwd = driver.find_element_by_css_selector("#pass")
passwd.send_keys(password)
time.sleep(0.5)
button = driver.find_element_by_css_selector("#loginbutton")
button.click()
time.sleep(5)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_title = soup.find("title")
print(tag_title.text)
driver.quit()