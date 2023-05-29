import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://data.epa.gov.tw/'

driver = webdriver.Chrome()
driver.maximize_window()    #全螢幕顯示

driver.get(url)

driver.find_element_by_id('Keyword').send_keys("aqi" + Keys.RETURN) # 輸入 aqi 後按 Enter
time.sleep(1)  # 必須加入等待，否則會有誤動作

driver.find_element_by_link_text("空氣品質指標(AQI)").click()  # 點選 空氣品質指標(AQI) 鈕
time.sleep(3)  # 必須加入等待，否則會有誤動作

driver.find_element_by_link_text("JSON").click() # 下載 JSON
time.sleep(3)  # 必須加入等待，否則會有誤動作

driver.find_element_by_link_text("XML").click() # 下載 XML
time.sleep(3)  # 必須加入等待，否則會有誤動作

driver.find_element_by_link_text("CSV").click() # 下載 CSV

driver.close()  #關閉瀏覽器
