import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://www.google.com"
# url = 'https://www.gmail.com'
mail_address = "XXXXXXX"
password = "XXXXXXX"

# 建立瀏覽器物件
# driver = webdriver.Chrome()    #使用Chrome
driver = webdriver.Firefox()  # 使用Firefox
driver.set_window_position(0, 0)  # 設定視窗位置
driver.set_window_size(800, 600)  # 設定視窗大小
# driver.maximize_window()    #全螢幕顯示

driver.get(url)

driver.find_element(By.CLASS_NAME, "gb_Md").click()  # 按右上角的 登入 鈕


driver.find_element(By.NAME, "identifier").send_keys(mail_address)  # 輸入 帳號

time.sleep(2)  # 必須加入等待，否則會有誤動作

driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()  # 按 下一步 鈕

time.sleep(2)  # 必須加入等待，否則會有誤動作

"""
driver.find_element_by_xpath("//input[@type='password']").send_keys(password)  # 輸入 密碼
time.sleep(2)  # 必須加入等待，否則會有誤動作

driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()  # 按 繼續 鈕  
time.sleep(3)  # 必須加入等待，否則會有誤動作
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "http://www.google.com"
# url = 'https://www.gmail.com'
mail_address = "XXXXXXX"
password = "XXXXXXX"

# driver = webdriver.Firefox();
driver = webdriver.Chrome()

driver.maximize_window()  # 全螢幕顯示

driver.get(url)
#
driver.find_element_by_id("gb_70").click()  # 按右上角的 登入 鈕

driver.find_element_by_id("identifierId").send_keys(email_address)  # 輸入 帳號
time.sleep(2)  # 必須加入等待，否則會有誤動作
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()  # 按 繼續 鈕
time.sleep(2)  # 必須加入等待，否則會有誤動作

driver.find_element_by_xpath("//input[@type='password']").send_keys(password)  # 輸入 密碼
time.sleep(2)  # 必須加入等待，否則會有誤動作
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()  # 按 繼續 鈕
time.sleep(3)  # 必須加入等待，否則會有誤動作

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "http://www.google.com"
# url = 'https://www.gmail.com'
mail_address = "XXXXXXX"
password = "XXXXXXX"

# driver = webdriver.Firefox();
driver = webdriver.Chrome()

driver.get(url)
# username = driver.find_element_by_id('identifierId');
username = driver.find_element("name", "identifierId")
username.send_keys(mail_address)

driver.find_elements_by_class_name("RveJvd.snByac")[1].click()
time.sleep(2)
# password not entered in username field
password = driver.find_element_by_class_name("whsOnd.zHQkBf")

password.send_keys(password)
driver.find_elements_by_class_name("RveJvd.snByac")[0].click()

# end login, start composing

time.sleep(5)
# wait for sign in
driver.find_element_by_class_name("T-I.J-J5-Ji.T-I-KE.L3").click()
to = driver.find_element_by_class_name("textarea#:lo.vO")
# incorrect
to.send_keys("EMAIL")
# subject = driver.find_element_by_id(':l6');
subject = driver.find_element("name", ":l6")

subject.send_keys("IP Address changed")
# content = driver.find_element_by_id(':m9');
content = driver.find_element("name", ":m9")

content.send_keys("Test Test\n")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
