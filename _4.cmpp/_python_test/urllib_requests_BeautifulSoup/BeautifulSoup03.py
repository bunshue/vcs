import requests
from bs4 import BeautifulSoup


print("使用 BeautifulSoup 分析網頁")

url = 'https://oldsiao.neocities.org/'
response = requests.get(url)
#print(response.text)

sp = BeautifulSoup(response.text, 'html.parser')

print("標題")
print(sp.title)
print("標題文字")
print(sp.title.text)

#尋找指定標籤find()、find_all()

print("尋找標籤「<div>」")
print(sp.find("div"))

print("尋找標籤「<title>」")
print(sp.find_all("title"))

import requests
from bs4 import BeautifulSoup

'''
# 題問說明
question_description = "[1]牡羊座 [2]金牛座 [3]雙子座 [4]巨蟹座 [5]獅子座 [6]處女座 [7]天秤座 [8]天蠍座 [9]射手座 [10]摩羯座 [11]水瓶座 [12]雙魚座，請選擇星座(僅能填數字):"

# 限制填寫內容為數字
while True:
    ans_data = input(question_description)
    # ans_data為數字且數值介於1~12
    if ans_data.isdigit() == True and int(ans_data) > 0 and int(ans_data) < 13:
        break
    else:
        pass
'''
    
url = 'https://oldsiao.neocities.org/'
print(url)

response = requests.get(url)

# 設定讀取編碼(預設 UTF-8)
response.encoding = 'UTF-8'

# 檢查 HTTP 回應碼是否為 200
if response.status_code == requests.codes.ok:
    sp = BeautifulSoup(response.text, 'html.parser')
    print("使用 BeautifulSoup 分析網頁")
    print("標題")
    print(sp.title)
    print("標題文字")
    print(sp.title.text)

