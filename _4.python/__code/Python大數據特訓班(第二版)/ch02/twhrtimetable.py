from selenium import webdriver
# 高鐵時刻表查詢網站
url = 'http://www.thsrc.com.tw/tw/TimeTable/SearchResult'
ss='台中站'      #出發站
es='台北站'      #到達站

# 建立瀏覽器物件開啟網站
driver = webdriver.Chrome()
driver.get(url)
#按我同意
driver.find_element_by_xpath("//button[@class='swal2-confirm swal2-styled']").click()
#輸入出發站
driver.find_element_by_id('select_location01').send_keys(ss) 
# #輸入到達站
driver.find_element_by_id('select_location02').send_keys(es)   
#輸入日期
driver.find_element_by_id("Departdate03").click()
driver.find_element_by_xpath("//div[@id='tot-1']/div/div/ul/li/div/div/table/tbody/tr[2]/td[1]").click()
# #輸入時間
driver.find_element_by_id("outWardTime").click()
driver.find_element_by_xpath("//div[@id='tot-1']/div[2]/div/ul/li[2]/div/div/table/tr[3]/td[3]/a/i").click()
driver.find_element_by_id('start-search').click() #按查詢鈕