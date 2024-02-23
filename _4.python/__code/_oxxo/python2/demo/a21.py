# encoding:UTF-8
from selenium import webdriver
import time
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')  # 不會開啟瀏覽器

driver = webdriver.Chrome(
    '/Users/oxxo/Documents/oxxo/practice/python/chromedriver', chrome_options=options)  # 設定 chromedriver 路徑
driver.get('https://www.dinbendon.net/do/login')  # 前往這個網址

# 輸入使用者 id
user = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[1]/td[2]/input')
user.send_keys('XXX')

# 輸入使用者密碼
pwd = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[2]/td[2]/input')
pwd.send_keys('XXX')

# 取得驗證碼訊息
checkquestion = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[1]')
check = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[2]/input')

# 計算驗證碼
checktext = checkquestion.text
print(checktext)
a = int(re.findall(r'\d+',checktext)[0])   # 使用正則表達式提取數字
b = int(re.findall(r'\d+',checktext)[1])
result = a+b
print(result)
check.send_keys(result)  # 輸入驗證碼

# 點擊按鈕
btn = driver.find_element_by_xpath(
    ' //*[@id="signInPanel_signInForm"]/table/tbody/tr[5]/td[2]/input[1]')
btn.click()

time.sleep(1)

# 抓取第一筆便當名稱，加入例外處理
try:
    menu = driver.find_element_by_xpath(
        '//*[@id="inProgressBox_inProgressOrders_0"]/td[2]/div[1]/a/span[2]')

    print(menu.text)
except:
    print('找不到便當名稱')

driver.close()
