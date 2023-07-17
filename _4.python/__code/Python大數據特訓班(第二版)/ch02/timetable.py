from selenium import webdriver
# 高鐵時刻表查詢網站
url = 'http://www.thsrc.com.tw/tw/TimeTable/SearchResult'
ss='台中站'      #出發站
es='台北站'      #到達站
dd='2020/03/26' #日期 
dt='09:00'      #時間
# 建立瀏覽器物件
driver = webdriver.Chrome()
## 最大化視窗後開啟facebook網站
#driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id('StartStation').send_keys(ss) #輸入郵件
driver.find_element_by_id('EndStation').send_keys(es)#輸入密碼密碼
driver.find_element_by_id("DepartueSearchDate").click()
driver.find_element_by_id('DepartueSearchDate').send_keys(dd)#輸入
driver.find_element_by_id("DepartueSearchTime").click()
driver.find_element_by_id('DepartueSearchTime').send_keys(dt)#輸入密碼
driver.find_element_by_id('SearchButton').click()    # 按登入鈕

#
#driver.find_element_by_id("StartStation").click()
#Select(driver.find_element_by_id("StartStation")).select_by_visible_text(u"台中站")
#driver.find_element_by_id("StartStation").click()
#driver.find_element_by_id("EndStation").click()
#Select(driver.find_element_by_id("EndStation")).select_by_visible_text(u"台北站")
#driver.find_element_by_id("EndStation").click()
#driver.find_element_by_id("DepartueSearchDate").click()
#driver.find_element_by_link_text("26").click()
#driver.find_element_by_id("DepartueSearchTime").click()
#Select(driver.find_element_by_id("DepartueSearchTime")).select_by_visible_text("09:00")
#driver.find_element_by_id("DepartueSearchTime").click()
#driver.find_element_by_id("SearchButton").click()
#import requests
#import json
#
#url = 'http://www.thsrc.com.tw/tw/TimeTable/Search'
#
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)                         Chrome/73.0.3683.86 Safari/537.36'
#}
#
#form_data = {
#    'StartStationName':'南港站',
#    'EndStationName':'台南站',
#    'SearchType':'S',
#    'StartStation':'2f940836-cedc-41ef-8e28-c2336ac8fe68',
#    'EndStation':'9c5ac6ca-ec89-48f8-aab0-41b738cb1814',
#    'DepartueSearchDate':'2019/04/02',
#    'DepartueSearchTime':'09:00',
#    'DepartueTrainCode':'',
#    'DestinationSearchDate':'',
#    'DestinationSearchTime':'',
#    'DiscountType':''
#}
#
#res = requests.post(url, headers=headers, data=form_data)
#
#jsdata = res.json()
#
##print(jsdata['data'])
#jsdata