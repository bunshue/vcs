from selenium import webdriver
from time import sleep

url = 'https://irs.thsrc.com.tw/IMINT/'  #高鐵訂票網頁
driver = webdriver.Chrome()
driver.get(url)
sleep(1)  #加入等待

delay = 0.3
driver.find_element_by_id("btn-confirm").click()
sleep(delay)
driver.find_element_by_name("selectStartStation").click()
sleep(delay)
#Select(driver.find_element_by_name("selectStartStation")).select_by_visible_text(u"台北")
driver.find_element_by_xpath("(//option[@value='2'])[1]").click()
sleep(delay)
driver.find_element_by_name("selectDestinationStation").click()
sleep(delay)
#Select(driver.find_element_by_name("selectDestinationStation")).select_by_visible_text(u"台中")
driver.find_element_by_xpath("(//option[@value='7'])[2]").click()
sleep(delay)
driver.find_element_by_id("trainCon:trainRadioGroup_1").click()
sleep(delay)
driver.find_element_by_id("seatRadio1").click()
sleep(delay)
driver.find_element_by_id("bookingMethod_1").click()
