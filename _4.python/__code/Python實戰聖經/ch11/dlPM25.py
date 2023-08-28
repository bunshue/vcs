from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

url = 'https://data.epa.gov.tw/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

driver.find_element_by_id('field-main-search').send_keys("aqi" + Keys.RETURN) # 輸入 aqi 後按 Enter
sleep(2)  #加入等待
driver.find_element_by_link_text("空氣品質指標(AQI)").click()  # 點選 空氣品質指標(AQI) 鈕
sleep(2) 
driver.find_element_by_xpath('//*[@id="dataset-resources"]/div/table/tbody/tr/td[1]/a').click()  # 點選 空氣品質指標(AQI) 鈕
sleep(2) 
driver.find_element_by_link_text("JSON").click() # 下載 JSON
sleep(3)
driver.find_element_by_link_text("XML").click() # 下載 XML
sleep(3)
driver.find_element_by_link_text("CSV").click() # 下載 CSV
sleep(3)

driver.quit()