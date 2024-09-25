
print("------------------------------------------------------------")  # 60個


# twhrtimetable.py
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

print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\Python大數據特訓班(第二版)\ch02\iplookup.py

import requests

# 設定查詢目前IP的api網址
url = 'https://api.ipify.org'
r = requests.get(url)

print('我目前的IP是：', r.text)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python大數據特訓班(第二版)\ch02\loginFacebook.py

from selenium import webdriver

# 設定facebook登入資訊
url = 'https://www.facebook.com/'
email='你的faceook電子郵件'
password='你的faceook密碼'
# 建立瀏覽器物件
driver = webdriver.Chrome()
# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id('email').send_keys(email) #輸入郵件
driver.find_element_by_id('pass').send_keys(password)#輸入密碼
driver.find_element_by_id('loginbutton').click()    # 按登入鈕

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python大數據特訓班(第二版)\ch02\phone_check.py

def isTaiwanPhone(str):
    if len(str) != 11:       # 如果長度不是11
        return False         # 傳回非手機號碼格式
    #檢查11個字元是否符合手機號碼格式
    for i in range(0, 11):    
        if i==4:
            if str[4] != '-':        # 如果第5個字元不是'-'字元
                return False         # 傳回非手機號碼格式
        else: # 如果前4個字或最後6個字出現非數字字元
            if str[i].isdecimal() == False:
                return False     # 傳回非手機號碼格式
    return True                  # 傳回是正確手機號碼格式        

print("0937-123456 是台灣手機號碼：", isTaiwanPhone('0937-123456'))
print("02-12345678 是台灣手機號碼：", isTaiwanPhone('02-12345678'))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python大數據特訓班(第二版)\ch02\timetable.py

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

print("------------------------------------------------------------")  # 60個

