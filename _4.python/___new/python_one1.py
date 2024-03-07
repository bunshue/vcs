"""
一本精通 - Python 範例應用大全
"""

import os
import sys
import time
import random

# 有順序

print("------------------------------------------------------------")  # 60個
print("Python 常用標準函式庫")
print("------------------------------------------------------------")  # 60個

import time
from concurrent.futures import ThreadPoolExecutor

a = True  # 定義 a 為 True


def run():
    global a  # 定義 a 是全域變數
    while a:  # 如果 a 為 True
        print(123)  # 不斷顯示 123
        time.sleep(1)  # 每隔一秒


def keyin():
    global a  # 定義 a 是全域變數
    if input() == "a":
        a = False  # 如果輸入的是 a，就讓 a 為 False，停止 run 函式中的迴圈


executor = ThreadPoolExecutor()
e1 = executor.submit(run)
e2 = executor.submit(keyin)
executor.shutdown()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("Python 基礎範例")
print("------------------------------------------------------------")  # 60個

import re

# 要轉換的字串
text = """請 求 您 幫 我 oxxo.studio 去 除 空 白 ok ？
但是要保留換行 可以 嗎 ，(        哈哈哈 )( 啊哈)
統一便利超商 (711) 的括號之間也要有空白喔！
寫作規    範就是這 麼 100% 的龜毛～
"""

# 取得中文字和英文單字的正規表達式
# [a-zA-Z0-9]+ 表示開頭是英文字母後面連接一串字母或數字
regex = re.compile(r"[\u4E00-\u9FFF\uFF00-\uFFFF\u0021-\u002F\n]|[a-zA-Z0-9]+")

# 根據正規表達式，將每個中文字、標點符號和英文單字變成串列
arr = re.findall(regex, text)

# 使用空格合併串列
text = " ".join(arr)
print(text)

"""
請 求 您 幫 我 oxxo . studio 去 除 空 白 ok ？
但 是 要 保 留 換 行 可 以 嗎 ， ( 哈 哈 哈 ) ( 啊 哈 )
統 一 便 利 超 商 ( 711 ) 的 括 號 之 間 也 要 有 空 白 喔 ！
寫 作 規 範 就 是 這 麼 100 % 的 龜 毛 ～
"""


print("------------------------------------------------------------")  # 60個


import re

# 輸入字符串
text = """請 求 您 幫 我 oxxo.studio 去 除 空 白 ok ？
但是要保留換行 可以 嗎 ，(        哈哈哈 )( 啊哈)
統一便利超商 (711) 的括號之間也要有空白喔！
寫作規    範就是這 麼 100% 的龜毛～
"""

regex = re.compile(r"[\u4E00-\u9FFF\uFF00-\uFFFF\u0021-\u002F\n]|[a-zA-Z0-9]+")
arr = re.findall(regex, text)
text = " ".join(arr)

regex = re.compile(r"(?<=[^a-zA-Z0-9\u0021-\u002E])(\x20)(?=[^a-zA-Z0-9\u0021-\u002E])")
text = re.sub(regex, "", text)

regex = re.compile(r"(\x20)(?=[\(\%\uFF00-\uFFFF])")
text = re.sub(regex, "", text)

text = text.replace(" . ", ".")
print(text)

print("------------------------------------------------------------")  # 60個

import time

n = 100
icon = "⋮⋰⋯⋱"  # 建立旋轉的符號清單
for i in range(n + 1):
    print(f"\r{icon[i%4]} {i*100/n}%", end="")
    time.sleep(0.1)


print("------------------------------------------------------------")  # 60個

a = 15  # 新增變數 a，設定金字塔有幾層
b = a * 2 + 1  # 新增變數 b，計算底部有幾個星星
for i in range(1, b, 2):  # 使用 for 迴圈，從 1～b，每隔 2 個一數
    move = round((b - i) / 2) - 1  # 計算星星的位移空白 ( 要將星星都置中 )
    print(f" " * move, end="")  # 印出星星前方的位移空白 ( 不換行 )
    print("*" * i)  # 加上「幾個星星」( 乘以 i )


print("------------------------------------------------------------")  # 60個

a = 15
b = a * 2 + 1
for i in range(1, b, 4):  # 改成 4 個一數，金字塔每一層就會增加 2，高度也會減半
    move = round((b - i) / 2) - 1
    print(f" " * move, end="")
    print("*" * i)


print("------------------------------------------------------------")  # 60個

a = 15  # 新增變數 a，設定金字塔有幾層
for i in range(1, a + 1):  # 使用 for 迴圈，重複指定的層數
    print(" " * (a - i) + "*" * (2 * i - 1))
    # ' ' * (a-i) 表示星星數越少，前面空白越多
    # '*' * (2*i-1) 串接後方星星的數量


print("------------------------------------------------------------")  # 60個

a = 10  # 要產生的金字塔層數
for i in range(1, a + 1):  # 使用 for 迴圈，重複 1～10 ( a+1 ) 的數字
    print(" " * 3 * (a - i), end="")  # 根據不同的層數，讓第一個數字前方增加指定的空白字元 ( 後方不換行 )
    for j in range(1, i + 1):  # 第二層 for 迴圈，重複不同層內的數字
        if j == 1:  # 如果是第一個數字
            print(j, end="")  # 單純印出數字即可 ( 後方不換行 )
        else:  # 如果是第二個以後的數字
            print(f"{j:>3d}", end="")  # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
    for j in range(i - 1, 0, -1):  # 剛剛的 for 迴圈是由小到大，加入另外一個由大到小的迴圈
        print(f"{j:>3d}", end="")  # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
    print("")  # 最後執行換行的 print


print("------------------------------------------------------------")  # 60個

a = 10
for i in range(1, a + 1):
    print(" " * 3 * (a - i), end="")
    for j in range(0, i):  # ragne 改成從 0 開始，因為 2 的 0 次方等於 1
        k = 2**j  # 計算 2 的幾次方
        if k == 1:
            print(k, end="")
        else:
            print(f"{k:>3d}", end="")
    for j in range(i - 2, -1, -1):  # 修改 range，使其最後一位數為 0
        k = 2**j  # 計算 2 的幾次方
        print(f"{k:>3d}", end="")
    print("")


print("------------------------------------------------------------")  # 60個


a = 10  # 要產生的金字塔層數
b = 1  # 提供 while 迴圈停止的依據
while b <= a:  # 如果 b <= a 就讓 while 迴圈繼續
    n = 1  # 設定從 1 開始
    print(" " * 3 * (a - b), end="")  # 根據不同的層數，讓第一個數字前方增加指定的空白字元 ( 後方不換行 )
    while n <= b:  # 第二層 while 迴圈，如果 n <= b 就讓 while 迴圈繼續
        if n == 1:  # 如果是第一個數字
            print(n, end="")  # 單純印出數字即可 ( 後方不換行 )
        else:  # 如果是第二個以後的數字
            print(f"{n:>3d}", end="")  # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
        n = n + 1  # 將 n 增加 1
    while n > 2:  # 剛剛的 while 迴圈是由小到大，加入另外一個由大到小的迴圈
        print(f"{n-2:>3d}", end="")  # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
        n = n - 1  # 將 n 減少 1
    print("")  # 最後執行換行的 print
    b = b + 1  # 將 b 增加 1

print("------------------------------------------------------------")  # 60個

local_table = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 34,
    "J": 18,
    "K": 19,
    "L": 20,
    "M": 21,
    "N": 22,
    "O": 35,
    "P": 23,
    "Q": 24,
    "R": 25,
    "S": 26,
    "T": 27,
    "U": 28,
    "V": 29,
    "W": 32,
    "X": 30,
    "Y": 31,
    "Z": 33,
}
id_number = input("輸入身分證字號：")
check = False  # 新增 check=False 變數，與 while 迴圈搭配
while True:  # 使用 while 迴圈
    id_arr = list(id_number)  # 新增 id_arr 變數，將身分證字號轉換成串列存入
    if len(id_arr) != 10:
        break  # 判斷如果 id_arr 長度不等於 10，就跳出 while 迴圈
    local = str(local_table[id_arr[0]])  # 將對應的二位數字轉換成字串
    check_arr = list(local)  # 將字串轉換成陣列，例如 '10' 會轉換成 ['1','0']
    check_arr[0] = int(check_arr[0])  # 將串列中的第一個項目轉換成數字
    check_arr[1] = int(check_arr[1]) * 9  # 將串列中的第二個項目轉換成數字
    sex = id_arr[1]  # 取得第二碼數字
    if sex != "1" and sex != "2":
        break  # 判斷如果不是 '1' 也不是 '2' 就跳出 while 迴圈
    check_arr.append(int(sex) * 8)  # 將 sex 內容轉換成數字並乘以 8，存入 check_arr 裡
    for i in range(7):  # 使用 for 迴圈，重複七次
        check_arr.append(int(id_arr[i + 2]) * (7 - i))  # 每次重複，按照檢查碼程式，將數字乘以對應的數值
    check_num = 10 - sum(check_arr) % 10  # 計算使用者輸入的檢查碼
    if check_num != int(id_arr[9]):
        break  # 如果檢查碼不相同，跳出 while 迴圈
    check = True  # 如果迴圈都沒有跳出，讓 check 等於 True。
    break  # 結束後跳出迴圈

if check == False:  # while 迴圈結束後，如果 check 等於 Fasle，表示身分證字號錯誤
    print("身分證字號格式錯誤")
else:
    print("身分證字號正確")


print("------------------------------------------------------------")  # 60個


local_table = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 34,
    "J": 18,
    "K": 19,
    "L": 20,
    "M": 21,
    "N": 22,
    "O": 35,
    "P": 23,
    "Q": 24,
    "R": 25,
    "S": 26,
    "T": 27,
    "U": 28,
    "V": 29,
    "W": 32,
    "X": 30,
    "Y": 31,
    "Z": 33,
}
while True:  # 新增 while 迴圈，就可以重複輸入
    id_number = input("輸入身分證字號：")
    check = False
    while True:
        try:  # 使用 try
            id_arr = list(id_number)
            if len(id_arr) != 10:
                break
            local = str(local_table[id_arr[0]])
            check_arr = list(local)
            check_arr[0] = int(check_arr[0])
            check_arr[1] = int(check_arr[1]) * 9
            sex = id_arr[1]
            if sex != "1" and sex != "2":
                break
            check_arr.append(int(sex) * 8)
            for i in range(7):
                check_arr.append(int(id_arr[i + 2]) * (7 - i))
            check_num = 10 - sum(check_arr) % 10
            if check_num != int(id_arr[9]):
                break
            check = True
            break
        except:  # 使用 except，如果發生例外狀況，跳出迴圈
            break

    if check == False:
        print("身分證字號格式錯誤")
    else:
        print("身分證字號正確")


print("------------------------------------------------------------")  # 60個

table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}  # 轉換對照表
roman = [i for i in input()]  # 將輸入的羅馬數字變成串列
r = roman[::-1]  # 反轉串列
output = table[r[0]]  # 讓 output 先等於第一個數字
for i in range(1, len(r)):  # 從第二個數字開始依序取到最後一個數字
    if table[r[i]] < table[r[i - 1]]:  # 如果後面數字比較小
        output = output - table[r[i]]  # 讓 output 減去後面的數字
    else:
        output = output + table[r[i]]  # 如果後面數字比較大，讓 output 加上後面的數字
print(output)

# 輸入 IVMVIIMVVMVM 就會得到 3994

print("------------------------------------------------------------")  # 60個


num_table = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"],
]  # 建立對照表
num = int(input())  # 將輸入的文字轉換成數字
output = ""  # 設定輸出的 output 字串
for i in num_table:  # 依序判斷對照表中每個數字
    a = divmod(num, i[0])  # 取得商 ( a[0] ) 和餘數 ( a[1] )
    if a[0] != 0:  # 如果 a[0] 不為 0
        num = a[1]  # 取得餘數繼續往下除
        output = output + i[1] * a[0]  # 組合字串
print(output)

print("------------------------------------------------------------")  # 60個
print("Python 實際應用")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

import glob
import os

images = glob.glob("./demo/*")
print(images)

n = 1  # 設定名稱從 1 開始
for i in images:
    os.rename(i, f"./demo/img-{n:03d}.jpg")  # 改名時，使用字串格式化的方式進行三位數補零
    n = n + 1  # 每次重複時將 n 增加 1


print("------------------------------------------------------------")  # 60個

from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
screen = QtWidgets.QApplication.desktop()
width = screen.width()
height = screen.height()
print(width, height)


print("------------------------------------------------------------")  # 60個

socket.socket(family, type, proto)
# family：IPv4 本機、IPv4 網路、IPv6 網路。
# type：使用 TCP 或 UDP 方式。
# protocol: 串接協定 ( 通常預設 0 )。


print("------------------------------------------------------------")  # 60個

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
print(ip)
s.close()


print("------------------------------------------------------------")  # 60個

import requests

ip = requests.get("https://api.ipify.org").text

print(ip)


print("------------------------------------------------------------")  # 60個

import socket

hostname = "google.com"
print(socket.gethostbyname(hostname))


print("------------------------------------------------------------")  # 60個

import os

hostname = "google.com"
response = os.system("ping -c 3 -i 1 " + hostname)
print(response)

response = os.popen(f"ping -c 3 -i 1 {hostname}").read()
print(response)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("Python 網路爬蟲")
print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code001.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "要爬的網址"
# 假的 headers 資訊
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
}
# 加入 headers 資訊
web = requests.get(url, headers=headers)
web.encoding = "utf8"
print(web.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code002.py

# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver

# 假的 headers 資訊
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
# 加入 headers 資訊
opt.add_argument("--user-agent=%s" % user_agent)
driver = webdriver.Chrome("./chromedriver", options=opt)
driver.get("要爬的網址")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code003.py

# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
    },
)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code004.py

# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("爬取的網址")
# 從載入後的動態網頁裡，找到指定的元素
imgCount = driver.find_element(By.CSS_SELECTOR, "CSS 選擇器")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code005.py_

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

submitBtn = driver.find_element(By.CSS_SELECTOR, "#submitBtn")
actions = ActionChains(driver)
# 滑鼠先移到 submitBtn 上，然後再點擊 submitBtn
actions.move_to_element(submitBtn).click(submitBtn)
actions.perform()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code006.py

# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from time import sleep

submitBtn = driver.find_element(By.CSS_SELECTOR, "#submitBtn")
sleep(1)  # 等待一秒
submitBtn.click()
sleep(0.5)  # 等待 0.5 秒
submitBtn.click()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code007.py

# Copyright © https://steam.oxxostudio.tw

import requests

cookies = {"over18": "1"}
# 加入 Cookies 資訊
web = requests.get("https://www.ptt.cc/bbs/Gossiping/index.html", cookies=cookies)
print(web.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code008.py

# Copyright © https://steam.oxxostudio.tw

import requests

# 建立 Proxy List
proxy_ips = [
    "80.93.213.213:3136",
    "191.241.226.230:53281",
    "207.47.68.58:21231",
    "176.241.95.85:48700",
]
# 依序執行 get 方法
for ip in proxy_ips:
    try:
        result = requests.get(
            "https://www.google.com", proxies={"http": "ip", "https": ip}
        )
        print(result.text)
    except:
        print(f"{ip} invalid")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code009.py

# Copyright © https://steam.oxxostudio.tw

import requests

web = requests.get("https://water.taiwanstat.com/")  # 使用 get 方法
print(web.text)  # 讀取並印出 text 屬性


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code010.py

# Copyright © https://steam.oxxostudio.tw

import requests

web = requests.get("https://water.taiwanstat.com/")  # 使用 get 方法
web.encoding = "utf-8"  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼
print(web.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code011.py

# Copyright © https://steam.oxxostudio.tw

import requests

web = requests.get(
    "https://data.kcg.gov.tw/dataset/6f29f6f4-2549-4473-aa90-bf60d10895dc/resource/30dfc2cf-17b5-4a40-8bb7-c511ea166bd3/download/lightrailtraffic.json"
)
print(web.json())


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code012.py

# Copyright © https://steam.oxxostudio.tw

import requests

# 設定參數
params = {"name": "oxxo", "age": "18"}
# 加入參數
web = requests.get(
    "https://script.google.com/macros/s/AKfycbw5PnzwybI_VoZaHz65TpA5DYuLkxIF-HUGjJ6jRTOje0E6bVo/exec",
    params=params,
)
print(web.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code013.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = "https://water.taiwanstat.com/"
web = requests.get(url)  # 取得網頁內容
soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
title = soup.title  # 取得 title
print(title)  # 印出 title ( 台灣水庫即時水情 )


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code014.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = "https://water.taiwanstat.com/"
web = requests.get(url)
# soup = BeautifulSoup(web.text, "html.parser")  # 使用 html.parser 解析器
soup = BeautifulSoup(web.text, "html5lib")  # 使用 html5lib 解析器
title = soup.title
print(title)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code015.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = "https://www.iana.org/domains/"
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")

print(soup.select("#logo"))  # 搜尋 id 為 logo 的 tag 內容
print("\n----------\n")

print(soup.find_all("div", id="logo"))  # 搜尋所有 id 為 logo 的 div
print("\n----------\n")

divs = soup.find_all("div")  # 搜尋所有的 div
print(divs[1])  # 取得搜尋到的第二個項目 ( 第一個為 divs[0] )
print("\n----------\n")

# 從搜尋到的項目裡，尋找父節點裡所有的 li
print(divs[1].find_parent().find_all("li"))
print("\n----------\n")

# 從搜尋到的項目裡，尋找父節點裡所有 li 的第三個項目，找到他後方同層的所有 li
print(divs[1].find_parent().find_all("li")[2].find_next_siblings())
print("\n----------\n")

# 從搜尋到的項目裡，尋找父節點裡所有 li 的第三個項目，找到他前方同層的所有 li
print(divs[1].find_parent().find_all("li")[2].find_previous_siblings())


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code016.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = "https://www.iana.org/domains/"
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")

print(soup.find_all("a"))  # 等同於下方的 soup('a')
print(soup("a"))  # 等同於上方的 find_all('a')


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code017.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = "https://www.iana.org/domains/"
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")
print(soup.find_all("a"))  # 找出所有 a tag
print(soup.find_all("a", string="Domains"))  # 找出內容字串為 Domains 的 a tag
print(soup("a", limit=2))  # 找出前兩個 a tag

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code018.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = "https://www.iana.org/domains/"
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")
print(soup.find("a").get_text())  # 輸出第一個 a tag 的內容
print(soup.find("a")["href"])  # 輸出第一個 a tag 的 href 屬性內容


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code019.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = "https://water.taiwanstat.com/"
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")
reservoir = soup.select(".reservoir")  # 取得所有 class 為 reservoir 的 tag
for i in reservoir:
    print(
        i.find("div", class_="name").get_text(), end=" "
    )  # 取得內容的 class 為 name 的 div 文字
    print(i.find("h5").get_text(), end=" ")  # 取得內容 h5 tag 的文字
    print()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code020.py

# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")  # 指向 chromedriver 的位置
driver.get("https://www.google.com")  # 打開瀏覽器，開啟網頁


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code021.py

# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # 使用 Select 對應下拉選單
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://example.oxxostudio.tw/python/selenium/demo.html")  # 開啟範例網址
a = driver.find_element(By.ID, "a")  # 取得 id 為 a 的網頁元素 ( 按鈕 A )
b = driver.find_element(By.CLASS_NAME, "btn")  # 取得 class 為 btn 的網頁元素 ( 按鈕 B )
c = driver.find_element(By.CSS_SELECTOR, ".test")  # 取得 class 為 test 的網頁元素 ( 按鈕 C )
d = driver.find_element(By.NAME, "dog")  # 取得屬性 name 為 dog 的網頁元素 ( 按鈕 D )
h1 = driver.find_element(By.TAG_NAME, "h1")  # 取得 tag h1 的網頁元素
link1 = driver.find_element(By.LINK_TEXT, "我是超連結，點擊會開啟 Google 網站")  # 取得指定超連結文字的網頁元素
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Google")  # 取得超連結文字包含 Google 的網頁元素
select = Select(
    driver.find_element(By.XPATH, "/html/body/select")
)  # 取得 html > body > select 這個網頁元素

a.click()  # 點擊 a
print(a.text)  # 印出 a 元素的內容
time.sleep(0.5)
b.click()  # 點擊 b
print(b.text)  # 印出 b 元素的內容
time.sleep(0.5)
c.click()  # 點擊 c
print(c.text)  # 印出 c 元素的內容
time.sleep(0.5)
d.click()  # 點擊 d
print(d.text)  # 印出 d 元素的內容
time.sleep(0.5)
select.select_by_index(2)  # 下拉選單選擇第三項 ( 第一項為 0 )
time.sleep(0.5)
h1.click()  # 點擊 h1
time.sleep(0.5)
link1.click()  # 點擊 link1
time.sleep(0.5)
link2.click()  # 點擊 link2
print(link2.get_attribute("href"))  # 印出 link2 元素的 href 屬性


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code022.py

# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome("./chromedriver")
driver.get("https://example.oxxostudio.tw/python/selenium/demo.html")
a = driver.find_element(By.ID, "a")
add = driver.find_element(By.ID, "add")
a.click()  # 點擊按鈕 A，出現 a 文字
sleep(1)
add.click()  # 點擊 add 按鈕，出現 數字 1
add.click()  # 點擊 add 按鈕，出現 數字 2
sleep(1)
add.click()  # 點擊 add 按鈕，出現 數字 3
sleep(1)
add.click()  # 點擊 add 按鈕，出現 數字 4


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code022-1.py

# Copyright © https://steam.oxxostudio.tw


# 下方的程式使用「ActionChains」的方式，結果與上述的執行結果相同。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("./chromedriver")
driver.get("https://example.oxxostudio.tw/python/selenium/demo.html")
a = driver.find_element(By.ID, "a")
add = driver.find_element(By.ID, "add")
actions = ActionChains(driver)  # 使用 ActionChains 的方式
actions.click(a).pause(1)  # 點擊按鈕 A，出現 a 文字後，暫停一秒
actions.double_click(add).pause(1).click(add).pause(1).click(add)
# 連點 add 按鈕，等待一秒後再次點擊，等待一秒後再次點擊
actions.perform()  # 執行儲存的動作

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code023.py

# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("./chromedriver")
driver.get("https://example.oxxostudio.tw/python/selenium/demo.html")
a = driver.find_element(By.ID, "a")
show = driver.find_element(By.ID, "show")
actions = ActionChains(driver)
actions.click(show).send_keys(["1", "2", "3", "4", "5"])  # 輸入 1～5 的鍵盤值 ( 必須是字串 )
actions.pause(1)  # 等待一秒
actions.click(a)  # 點擊按鈕 A
actions.pause(1)  # 等待一秒
actions.send_keys_to_element(show, ["A", "B", "C", "D", "E"])  # # 輸入 A～E 的鍵盤值
actions.perform()  # 送出動作


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code024.py

# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver")
driver.get("https://example.oxxostudio.tw/python/selenium/demo.html")
body = driver.find_element(By.TAG_NAME, "body")
a = driver.find_element(By.ID, "a")
b = driver.find_element(By.CLASS_NAME, "btn")
c = driver.find_element(By.CSS_SELECTOR, ".test")
d = driver.find_element(By.NAME, "dog")
link1 = driver.find_element(By.LINK_TEXT, "我是超連結，點擊會開啟 Google 網站")
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Google")

print(a.id)
print(b.text)
print(c.tag_name)
print(d.size)
print(link1.get_attribute("href"))
print(link2.get_attribute("target"))
body.screenshot("./test.png")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code025.py

# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep

driver = webdriver.Chrome("./chromedriver")
driver.get(
    "https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html"
)

sleep(1)
driver.execute_script("window.scrollTo(0, 500)")  # 捲動到 500px 位置
sleep(1)
driver.execute_script("window.scrollTo(0, 2500)")  # 捲動到 2500px 位置
sleep(1)
driver.execute_script("window.scrollTo(0, 0)")  # 捲動到 0px 位置

h1 = driver.find_element(By.TAG_NAME, "h1")
h3 = driver.find_element(By.TAG_NAME, "h3")
script = """
  let h1 = arguments[0];
  let h3 = arguments[1];
  alert(h1, h3)
"""
driver.execute_script(script, h1, h3)  # 執行 JavaScript，印出元素
sleep(2)
Alert(driver).accept()  # 點擊提示視窗的確認按鈕，關閉提示視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code026.py

# Copyright © https://steam.oxxostudio.tw

import requests

web = requests.get("https://www.ptt.cc/bbs/Gossiping/index.html")
print(web.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code027.py

# Copyright © https://steam.oxxostudio.tw

import requests

web = requests.get(
    "https://www.ptt.cc/bbs/Gossiping/index.html", cookies={"over18": "1"}
)  # 加入 Cookies 資訊
print(web.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code028.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/"
web = requests.get(
    "https://www.ptt.cc/bbs/Gossiping/index.html", cookies={"over18": "1"}
)
soup = BeautifulSoup(web.text, "html.parser")
titles = soup.find_all("div", class_="title")  # 取得 class 為 title 的 div 內容
for i in titles:
    if i.find("a") != None:  # 判斷如果不為 None
        print(i.find("a").get_text())  # 取得 div 裡 a 的內容，使用 get_text() 取得文字
        print(url + i.find("a")["href"], end="\n\n")  # 使用 ['href'] 取得 href 的屬性


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code029.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/"
web = requests.get(
    "https://www.ptt.cc/bbs/Gossiping/index.html", cookies={"over18": "1"}
)
web.encoding = "utf-8"  # 避免中文亂碼
soup = BeautifulSoup(web.text, "html.parser")
titles = soup.find_all("div", class_="title")
output = ""  # 建立 output 變數
for i in titles:
    if i.find("a") != None:
        # 將資料一次記錄到 output 變數裡
        output = (
            output + i.find("a").get_text() + "\n" + url + i.find("a")["href"] + "\n\n"
        )
print(output)

f = open(
    "/content/drive/MyDrive/Colab Notebookstest.txt", "w"
)  # 建立並開啟純文字文件 ( Colab 才需要 )
f.write(output)  # 將資料寫入檔案裡
f.close()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code030.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

web = requests.get(
    "https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html", cookies={"over18": "1"}
)  # 傳送 Cookies 資訊後，抓取頁面內容
soup = BeautifulSoup(web.text, "html.parser")  # 使用 BeautifulSoup 取得網頁結構
imgs = soup.find_all("img")  # 取得所有 img tag 的內容
for i in imgs:
    print(i["src"])  # 印出 src 的屬性


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code031.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

web = requests.get(
    "https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html", cookies={"over18": "1"}
)
soup = BeautifulSoup(web.text, "html.parser")
imgs = soup.find_all("img")
name = 0  #  設定圖片編號
for i in imgs:
    print(i["src"])
    jpg = requests.get(i["src"])  # 使用 requests 讀取圖片網址，取得圖片編碼
    f = open(
        f"/content/drive/MyDrive/Colab Notebooks/download/test_{name}.jpg", "wb"
    )  # 使用 open 設定以二進位格式寫入圖片檔案
    f.write(jpg.content)  # 寫入圖片的 content
    f.close()  # 寫入完成後關閉圖片檔案
    name = name + 1  # 編號增加 1


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code032.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

web = requests.get(
    "https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html", cookies={"over18": "1"}
)
soup = BeautifulSoup(web.text, "html.parser")
imgs = soup.find_all("img")
name = 0
for i in imgs:
    print(i["src"])
    jpg = requests.get(i["src"])
    f = open(f"content/drive/MyDrive/Colab Notebooks/download/test_{name}.jpg", "wb")
    f.write(jpg.content)
    f.close()
    name = name + 1


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code033.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor  # 加入 concurrent.futures 內建函式庫

web = requests.get(
    "https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html", cookies={"over18": "1"}
)
soup = BeautifulSoup(web.text, "html.parser")
imgs = soup.find_all("img")
name = 0
img_urls = []  # 根據爬取的資料，建立一個圖片名稱與網址的空串列
for i in imgs:  # 修改 for 迴圈內容
    img_urls.append([i["src"], name])  # 將圖片網址與編號加入串列中
    name = name + 1  # 編號增加 1


def download(url):  # 編輯下載函式
    print(url)  # 印出網址
    jpg = requests.get(url[0])  # 使用 requests.get 取得圖片資訊
    f = open(f"download/test_{url[1]}.jpg", "wb")  # 將圖片開啟為二進位格式 ( 請自行修改存取路徑 )
    f.write(jpg.content)  # 存取圖片
    f.close()


executor = ThreadPoolExecutor()  # 建立非同步的多執行緒的啟動器
with ThreadPoolExecutor() as executor:
    executor.map(download, img_urls)  # 同時下載圖片


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code034.py

# Copyright © https://steam.oxxostudio.tw

import requests

# 2022/12 時氣象局有修改了 API 內容，將部份大小寫混合全改成小寫，因此程式碼也跟著修正
url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"
data = requests.get(url)  # 使用 get 方法透過空氣品質指標 API 取得內容
data_json = data.json()  # 將取得的檔案轉換為 JSON 格式
for i in data_json["records"]:  # 依序取出 records 內容的每個項目
    print(i["county"] + " " + i["sitename"], end="，")  # 印出城市與地點名稱
    print("AQI:" + i["aqi"], end="，")  # 印出 AQI 數值
    print("空氣品質" + i["status"])  # 印出空氣品質狀態


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code035.py

# Copyright © https://steam.oxxostudio.tw

import requests
import csv
import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 針對 Colab 改變路徑
csvfile = open("csv-aqi.csv", "w")  # 建立空白並可寫入的 CSV 檔案
csv_write = csv.writer(csvfile)  # 設定 csv_write 為寫入

url = "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON"
data = requests.get(url)
data_json = data.json()
output = [["county", "sitename", "aqi", "空氣品質"]]  # 設定 output 變數為二維串列，第一筆資料為開頭
for i in data_json["records"]:
    # 依序將取得的資料加入 output 中
    output.append([i["county"], i["sitename"], i["aqi"], i["status"]])
print(output)
csv_write.writerows(output)  # 多行寫入 CSV


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code036.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "一般天氣預報 - 今明 36 小時天氣預報 JSON 連結"
data = requests.get(url)  # 取得 JSON 檔案的內容為文字
data_json = data.json()  # 轉換成 JSON 格式
location = data_json["cwbopendata"]["dataset"]["location"]  # 取出 location 的內容
for i in location:
    print(f"{i}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code037.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "一般天氣預報 - 今明 36 小時天氣預報 JSON 連結"
data = requests.get(url)  # 取得 JSON 檔案的內容為文字
data_json = data.json()  # 轉換成 JSON 格式
location = data_json["cwbopendata"]["dataset"]["location"]
for i in location:
    city = i["locationName"]  # 縣市名稱
    wx8 = i["weatherElement"][0]["time"][0]["parameter"]["parameterName"]  # 天氣現象
    maxt8 = i["weatherElement"][1]["time"][0]["parameter"]["parameterName"]  # 最高溫
    mint8 = i["weatherElement"][2]["time"][0]["parameter"]["parameterName"]  # 最低溫
    ci8 = i["weatherElement"][3]["time"][0]["parameter"]["parameterName"]  # 舒適度
    pop8 = i["weatherElement"][4]["time"][0]["parameter"]["parameterName"]  # 降雨機率
    print(f"{city}未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code038.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "你的氣象觀測資料 JSON 網址"
data = requests.get(url)
data_json = data.json()
location = data_json["cwbopendata"]["location"]
for i in location:
    name = i["locationName"]  # 測站地點
    city = i["parameter"][0]["parameterValue"]  # 城市
    area = i["parameter"][2]["parameterValue"]  # 行政區
    print(city, area, name)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code039.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "你的氣象觀測資料 JSON 網址"
data = requests.get(url)
data_json = data.json()
location = data_json["cwbopendata"]["location"]
for i in location:
    name = i["locationName"]  # 測站地點
    city = i["parameter"][0]["parameterValue"]  # 城市
    area = i["parameter"][2]["parameterValue"]  # 行政區
    temp = i["weatherElement"][3]["elementValue"]["value"]  # 氣溫
    humd = round(
        float(i["weatherElement"][4]["elementValue"]["value"]) * 100, 1
    )  # 相對濕度
    r24 = i["weatherElement"][6]["elementValue"]["value"]  # 累積雨量

    print(city, area, name, f"{temp} 度", f"相對濕度 {humd}%", f"累積雨量 {r24}mm")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code040.py_

import requests

url = "你的氣象觀測資料 JSON 網址"
data = requests.get(url)
data_json = data.json()
location = data_json["cwbopendata"]["location"]
weather = {}  # 新增一個 weather 字典
for i in location:
    name = i["locationName"]
    city = i["parameter"][0]["parameterValue"]
    area = i["parameter"][2]["parameterValue"]
    temp = i["weatherElement"][3]["elementValue"]["value"]
    humd = round(float(i["weatherElement"][4]["elementValue"]["value"]) * 100, 1)
    r24 = i["weatherElement"][6]["elementValue"]["value"]
    msg = f"{temp} 度，相對濕度 {humd}%，累積雨量 {r24}mm"  # 組合成天氣描述
    try:
        weather[city][name] = msg  # 記錄地區和描述
    except:
        weather[city] = {}  # 如果每個縣市不是字典，建立第二層字典
        weather[city][name] = msg  # 記錄地區和描述

show = ""
for i in weather:
    show = show + i + ","  # 列出可輸入的縣市名稱
show = show.strip(",")  # 移除結尾逗號
a = input(f"請輸入下方其中一個縣市\n( {show} )\n")  # 讓使用者輸入縣市名稱

show = ""
for i in weather[a]:
    show = show + i + ","  # 列出可輸入的地點名稱
show = show.strip(",")  # 移除結尾逗號
b = input(f"請輸入{a}的其中一個地點\n( {show} )\n")  # 讓使用者輸入觀測地點名稱
print(f"{a}{b}，{weather[a][b]}。")  # 顯示結果

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code041.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "https://rate.bot.com.tw/xrt/flcsv/0/day"  # 牌告匯率 CSV 網址
rate = requests.get(url)  # 爬取網址內容
rate.encoding = "utf-8"  # 調整回應訊息編碼為 utf-8，避免編碼不同造成亂碼
rt = rate.text  # 以文字模式讀取內容
rts = rt.split("\n")  # 使用「換行」將內容拆分成串列
for i in rts:  # 讀取串列的每個項目
    try:  # 使用 try 避開最後一行的空白行
        a = i.split(",")  # 每個項目用逗號拆分成子串列
        print(a[0] + ": " + a[12])  # 取出第一個 ( 0 ) 和第十三個項目 ( 12 )
    except:
        break


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code042.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "https://invoice.etax.nat.gov.tw/index.html"
web = requests.get(url)  # 取得網頁內容
web.encoding = "utf-8"  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼
print(web.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code043.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "https://invoice.etax.nat.gov.tw/index.html"
web = requests.get(url)  # 取得網頁內容
web.encoding = "utf-8"  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼

from bs4 import BeautifulSoup

soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
td = soup.select(".container-fluid")[0].select(".etw-tbiggest")  # 取出中獎號碼的位置
ns = td[0].getText()  # 特別獎
n1 = td[1].getText()  # 特獎
# 頭獎，因為存入串列會出現 /n 換行符，使用 [-8:] 取出最後八碼
n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]]
print(ns)
print(n1)
print(n2)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code044.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "https://invoice.etax.nat.gov.tw/index.html"
web = requests.get(url)  # 取得網頁內容
web.encoding = "utf-8"  # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼

from bs4 import BeautifulSoup

soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
td = soup.select(".container-fluid")[0].select(".etw-tbiggest")  # 取出中獎號碼的位置
ns = td[0].getText()  # 特別獎
n1 = td[1].getText()  # 特獎
# 頭獎，因為存入串列會出現 /n 換行符，使用 [-8:] 取出最後八碼
n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]]

while True:
    try:
        # 對獎程式
        num = input("輸入你的發票號碼：")
        if num == ns:
            print("對中 1000 萬元！")
        if num == n1:
            print("對中 200 萬元！")
        for i in n2:
            if num == i:
                print("對中 20 萬元！")
                break
            if num[-7:] == i[-7:]:
                print("對中 4 萬元！")
                break
            if num[-6:] == i[-6:]:
                print("對中 1 萬元！")
                break
            if num[-5:] == i[-5:]:
                print("對中 4000 元！")
                break
            if num[-4:] == i[-4:]:
                print("對中 1000 元！")
                break
            if num[-3:] == i[-3:]:
                print("對中 200 元！")
                break
    except:
        break


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code045.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = "https://tw.stock.yahoo.com/quote/2330"  # 台積電 Yahoo 股市網址
web = requests.get(url)  # 取得網頁內容
soup = BeautifulSoup(web.text, "html.parser")  # 轉換內容
title = soup.find("h1")  # 找到 h1 的內容
a = soup.select(".Fz(32px)")[0]  # 找到第一個 class 為 Fz(32px) 的內容
b = soup.select(".Fz(20px)")[0]  # 找到第一個 class 為 Fz(20px) 的內容
s = ""  # 漲或跌的狀態
try:
    # 如果 main-0-QuoteHeader-Proxy id 的 div 裡有 C($c-trend-down) 的 class
    # 表示狀態為下跌
    if soup.select("#main-0-QuoteHeader-Proxy")[0].select(".C($c-trend-down)")[0]:
        s = "-"
except:
    try:
        # 如果 main-0-QuoteHeader-Proxy id 的 div 裡有 C($c-trend-up) 的 class
        # 表示狀態為上漲
        if soup.select("#main-0-QuoteHeader-Proxy")[0].select(".C($c-trend-up)")[0]:
            s = "+"
    except:
        # 如果都沒有包含，表示平盤
        s = "-"

print(f"{title.get_text()} : {a.get_text()} ( {s}{b.get_text()} )")  # 印出結果


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code046.py

# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# 建立要抓取的股票網址清單
stock_urls = [
    "https://tw.stock.yahoo.com/quote/2330",
    "https://tw.stock.yahoo.com/quote/0050",
    "https://tw.stock.yahoo.com/quote/2317",
    "https://tw.stock.yahoo.com/quote/6547",
]


# 將剛剛的抓取程式變成「函式」
def getStock(url):
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    title = soup.find("h1")
    a = soup.select(".Fz(32px)")[0]
    b = soup.select(".Fz(20px)")[0]
    s = ""
    try:
        if soup.select("#main-0-QuoteHeader-Proxy")[0].select(".C($c-trend-down)")[0]:
            s = "-"
    except:
        try:
            if soup.select("#main-0-QuoteHeader-Proxy")[0].select(".C($c-trend-up)")[0]:
                s = "+"
        except:
            state = ""
    print(f"{title.get_text()} : {a.get_text()} ( {s}{b.get_text()} )")


executor = ThreadPoolExecutor()  # 建立非同步的多執行緒的啟動器
with ThreadPoolExecutor() as executor:
    executor.map(getStock, stock_urls)  # 開始同時爬取股價


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code047.py

# Copyright © https://steam.oxxostudio.tw

import requests

webUrl = requests.get("https://today.line.me/tw/v2/article/oqay0ro")  # get 文章網址
# 取得文章的原始碼後，使用 split 字串拆分的方式，拆解出 articleId
article_id = webUrl.text.split("<script>")[1].split('id:"article:')[1].split(":")[0]
print(article_id)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code047-1.py

# Copyright © https://steam.oxxostudio.tw

import requests

webUrl = requests.get("https://today.line.me/tw/v2/article/oqay0ro")  # get 文章網址
# 取得文章的原始碼後，使用 split 字串拆分的方式，拆解出 articleId
article_id = webUrl.text.split("<script>")[1].split('id:"article:')[1].split(":")[0]
print(article_id)

# 使用 requests get 留言物件
comment = requests.get(
    f"https://today.line.me/webapi/comment/list?articleId={article_id}&sort=POPULAR&direction=DESC&country=TW&limit=30&pivot=0&postType=Article"
)
json = comment.json()  # 取得內容後，轉換成 json 格式
num = int(json["result"]["comments"]["count"])  # 取得文章的總數
print(num)  # 印出文章總數

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code048.py

# Copyright © https://steam.oxxostudio.tw

import requests

webUrl = requests.get("https://today.line.me/tw/v2/article/oqay0ro")
article_id = webUrl.text.split("<script>")[1].split('id:"article:')[1].split(":")[0]
print(article_id)

commentUrl = requests.get(
    f"https://today.line.me/webapi/comment/list?articleId={article_id}&sort=POPULAR&direction=DESC&country=TW&limit=30&pivot=0&postType=Article"
)
json = commentUrl.json()
num = int(json["result"]["comments"]["count"])
print(num)


# 定義函式，給予一個參數
def getComment(n):
    # 使用字串格式化的方式，讓網址會根據不同的參數而有所不同
    commentUrl = requests.get(
        f"https://today.line.me/webapi/comment/list?articleId={article_id}&sort=POPULAR&direction=DESC&country=TW&limit=30&pivot={n}&postType=Article"
    )
    json = commentUrl.json()  # 取得對應網址的 json 內容
    comments = json["result"]["comments"]["comments"]  # 取得該網址下所有留言
    for i in comments:
        # 印出留言者名稱以及留言內容
        print("<" + i["displayName"] + ">\n" + i["contents"][0]["extData"]["content"])
        print("----------------")


for i in range(0, num, 30):
    getComment(i)  # 從 0 開始，每隔 30 筆取一次

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code049.py

# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome("./chromedriver", options=opt)
# 清空 window.navigator
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
    },
)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code050.py

# Copyright © https://steam.oxxostudio.tw

driver.get("https://twitter.com")
sleep(2)
driver.execute_script(f"window.scrollTo(0, 200)")  # 自動往下捲動 200px
login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')  # 取得登入按鈕
login.click()  # 點擊登入按鈕


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code051.py

# Copyright © https://steam.oxxostudio.tw

sleep(2)  # 等待兩秒，讓網頁載入完成
# 取得輸入 email 的輸入框
username = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
username.send_keys("你的 email")  # 輸入 email
print("輸入 email 完成")
# 取得畫面上所有按鈕 ( 使用 elements )
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "下一步" or i.text == "Next":
        i.click()  # 如果按鈕是「下一步」或「Next」就點擊
        print("點擊下一步")
        break


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code052.py

# Copyright © https://steam.oxxostudio.tw

sleep(2)  # 等待兩秒頁面載入後繼續
try:
    check = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="on"]')
    check.send_keys("你的帳號")  # 輸入帳號
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for i in buttons:
        if i.text == "下一步" or i.text == "Next":
            i.click()  # 如果按鈕是「下一步」或「Next」就點擊
            print("驗證使用者帳號，點擊下一步")
            break
    sleep(2)  # 等待兩秒頁面載入後繼續
except:
    print("ok")
    sleep(2)  # 如果沒有出現安全性畫面，等待兩秒頁面載入後繼續


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code053.py

# Copyright © https://steam.oxxostudio.tw

pwd = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
pwd.send_keys("你的密碼")
print("輸入密碼")
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "登入" or i.text == "Log in":
        i.click()
        print("點擊登入")
        break


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code054.py

# Copyright © https://steam.oxxostudio.tw

sleep(2)
textbox = driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
textbox.send_keys("Hello World!I am Robot~ ^_^")  # 在輸入框輸入文字
print("輸入文字")
sleep(1)
imgInput = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="fileInput"]')
imgInput.send_keys("/Users/oxxo/Desktop/oxxo.png")  # 提供圖片絕對路徑，上傳圖片
print("上傳圖片")
sleep(1)
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "推文" or i.text == "Tweet":
        i.click()  # 點擊推文按鈕
        print("推文完成")
        break
sleep(1)
driver.close()  # 關閉瀏覽器視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch16\code055.py

# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
opt.add_argument("--headless")
opt.add_argument("--user-agent=%s" % user_agent)
driver = webdriver.Chrome("./chromedriver", options=opt)
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
    },
)
driver.get("https://twitter.com")
sleep(2)
driver.execute_script(f"window.scrollTo(0, 200)")
login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
login.click()
sleep(2)
username = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
username.send_keys("你的 email")
print("輸入 email 完成")
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "下一步" or i.text == "Next":
        i.click()
        print("點擊下一步")
        break
sleep(2)
try:
    check = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="on"]')
    check.send_keys("你的帳號")
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for i in buttons:
        if i.text == "下一步" or i.text == "Next":
            i.click()
            print("驗證使用者帳號，點擊下一步")
            break
    sleep(2)
except:
    print("ok")
    sleep(2)
pwd = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
pwd.send_keys("你的密碼")
print("輸入密碼")
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "登入" or i.text == "Log in":
        i.click()
        print("點擊登入")
        break
sleep(2)
textbox = driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
textbox.send_keys("Hello World!I am Robot~ ^_^")
print("輸入文字")
sleep(1)
imgInput = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="fileInput"]')
imgInput.send_keys("/Users/oxxo/Desktop/oxxo.png")
print("上傳圖片")
sleep(1)
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "推文" or i.text == "Tweet":
        i.click()
        print("推文完成")
        break
sleep(1)
driver.close()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("Python 網頁服務與應用")
print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code001.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask  # 載入 Flask

app = Flask(__name__)  # 建立 app 變數為 Flask 物件，__name__ 表示目前執行的程式


@app.route("/")  # 使用函式裝飾器，建立一個路由 ( Routes )，可針對主網域 / 發出請求
def home():  # 發出請求後會執行 home() 的函式
    return "<h1>hello world</h1>"  # 執行函式後會回傳特定的網頁內容


app.run()  # 執行


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code002.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["POST"])
def home():
    return "<h1>hello world</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code003.py

# Copyright © https://steam.oxxostudio.tw

import requests

web = requests.post("http://127.0.0.1:5000/")  # 使用 post 方法
print(web.text)  # 讀取並印出 text 屬性


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code004.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


app.run(host="0.0.0.0", port=5555)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code005.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/ok")
def ok():
    return "<h1>ok</h1>"


@app.route("/yes")
def yes():
    return "<h1>yes</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code006.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/<msg>")  # 加入 <msg> 讀取網址
def ok(msg):  # 加入參數
    return f"<h1>{msg}</h1>"  # 使用變數


app.run()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code007.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/<path:msg>")  # 加入 path: 轉換成「路徑」的類型
def ok(msg):
    return f"<h1>{msg}</h1>"


app.run()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code008.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask, request  # 載入了 request

app = Flask(__name__)


@app.route("/")
def home():
    print(request.args)  # 使用 request.args
    return "<h1>hello world</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code009.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def home():
    print(request.form)  # 使用 request.form
    return "<h1>hello world</h1>"


app.run()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code009-1.py

# Copyright © https://steam.oxxostudio.tw

import requests

data = {"name": "oxxo", "age": "18"}
web = requests.post("http://127.0.0.1:5000/", data=data)  # 發送 POST 請求
print(web.text)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code010.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = request.args.get("name")
    return render_template("test.html", name=name)


app.run()


print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code011.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask, request, render_template  # 載入 render_template

app = Flask(__name__)


@app.route("/")
def home():
    name = request.args.get("name")
    return render_template("test.html", name=name)  # 使用網頁樣板，並傳入參數


app.run()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code012.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask

app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return f"<h1>hello {name}</h1>"


app.run()

"""

from google.colab import drive
drive.mount('/content/drive', force_remount=True)

!mkdir -p /drive
#umount /drive
!mount --bind /content/drive/My\ Drive /drive
!mkdir -p /drive/ngrok-ssh
!mkdir -p ~/.ssh


----

!mkdir -p /drive/ngrok-ssh
%cd /drive/ngrok-ssh
!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip -O ngrok-stable-linux-amd64.zip
!unzip -u ngrok-stable-linux-amd64.zip
!cp /drive/ngrok-ssh/ngrok /ngrok
!chmod +x /ngrok




"""


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code015.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route("/<name>")
def home(name):
    return f"<h1>hello {name}</h1>"


app.run()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code016.py

# Copyright © https://steam.oxxostudio.tw


def hello_world(request):
    request_json = request.get_json()
    print(request.args)  # 讀取 GET 方法參數
    print(request.form)  # 讀取 POST 方法參數
    print(request.path)  # 讀取網址
    print(request.method)  # 讀取叫用方法
    if request.args and "message" in request.args:
        return request.args.get("message")
    elif request_json and "message" in request_json:
        return request_json["message"]
    else:
        return f"Hello World!"


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code018.py

# Copyright © https://steam.oxxostudio.tw


def hello_world(request):
    request_json = request.get_json()
    print(request.args)  # 讀取 GET 方法參數
    print(request.form)  # 讀取 POST 方法參數
    print(request.path)  # 讀取網址
    print(request.method)  # 讀取叫用方法

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Max-Age": "3600",
    }

    return ("Hello World!", 200, headers)  # 回傳同意跨域的 header


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code019.py

# Copyright © https://steam.oxxostudio.tw

import smtplib

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("你的信箱", "你的密碼")
from_addr = "你的信箱"
to_addr = "收件人信箱"
msg = "Subject:title\nHello\nWorld!"
status = smtp.sendmail(from_addr, to_addr, msg)
if status == {}:
    print("郵件傳送成功！")
else:
    print("郵件傳送失敗...")
smtp.quit()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code020.py

# Copyright © https://steam.oxxostudio.tw

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("你好呀！這是用 Python 寄的信～", "plain", "utf-8")  # 郵件內文
msg["Subject"] = "test測試"  # 郵件標題
msg["From"] = "oxxo"  # 暱稱或是 email
msg["To"] = "oxxo.studio@gmail.com"  # 收件人 email
msg["Cc"] = "oxxo.studio@gmail.com, XXX@gmail.com"  # 副本收件人 email ( 開頭的 C 大寫 )
msg["Bcc"] = "oxxo.studio@gmail.com, XXX@gmail.com"  # 密件副本收件人 email

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("你的信箱", "你的密碼")
status = smtp.send_message(msg)  # 改成 send_message
if status == {}:
    print("郵件傳送成功！")
else:
    print("郵件傳送失敗！")
smtp.quit()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code021.py_

import smtplib
from email.mime.text import MIMEText

html = """
<h1>hello</h1>
<div>這是 HTML 的內容</div>
<div style="color:red">紅色的字</div>
"""

mail = MIMEText(html, "html", "utf-8")  # plain 換成 html，就能寄送 HTML 格式的信件
mail["Subject"] = "html 的信"
mail["From"] = "oxxo"
mail["To"] = "oxxo.studio@gmail.com"

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("你的信箱", "你的密碼")
status = smtp.send_message(mail)
print(status)
smtp.quit()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code022.py

# Copyright © https://steam.oxxostudio.tw

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

html = """
<h1>hello</h1>
<div>這是 HTML 的內容</div>
<div style="color:red">紅色的字</div>
"""
msg = MIMEMultipart()  # 使用多種格式所組成的內容
msg.attach(MIMEText(html, "html", "utf-8"))  # 加入 HTML 內容
# 使用 python 內建的 open 方法開啟指定目錄下的檔案
with open("/content/drive/MyDrive/Colab Notebooks/meme.jpg", "rb") as file:
    img = file.read()
attach_file = MIMEApplication(img, Name="meme.jpg")  # 設定附加檔案圖片
msg.attach(attach_file)  # 加入附加檔案圖片

msg["Subject"] = "附件是一張搞笑的圖"
msg["From"] = "oxxo"
msg["To"] = "oxxo.studio@gmail.com"

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("oxxo.studio@gmail.com", "你申請的應用程式密碼")
status = smtp.send_message(msg)
print(status)
smtp.quit()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code024.py

# Copyright © https://steam.oxxostudio.tw

import requests

web = requests.get("你的應用程式網址")
print(web.json())

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code026.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "你的應用程式網址"
name = "工作表1"
row = 2
web = requests.get(f"{url}?name={name}&row={row}")
print(web.json())
name = "工作表2"
web = requests.get(f"{url}?name={name}")
print(web.json())


print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code028.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "部署的網址"

params = {"name": "工作表1", "top": "true", "data": "[123,456,789]"}

web = requests.get(url=url, params=params)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code029.py

# Copyright © https://steam.oxxostudio.tw

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=R93ce4FZGbc")  # baby shark 的音樂
print(yt.title)  # 影片標題
print(yt.length)  # 影片長度 ( 秒 )
print(yt.author)  # 影片作者
print(yt.channel_url)  # 影片作者頻道網址
print(yt.thumbnail_url)  # 影片縮圖網址
print(yt.views)  # 影片觀看數

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code030.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=R93ce4FZGbc")
print("download...")
yt.streams.filter().get_highest_resolution().download(filename="baby_shart.mp4")
# 下載最高畫質影片，如果沒有設定 filename，則以原本影片的 title 作為檔名
print("ok!")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code031.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=R93ce4FZGbc")
print("download...")
yt.streams.filter().get_by_resolution("360p").download(filename="oxxostudio_360p.mp4")
# 下載 480p 的影片畫質
print("ok!")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code032.py

# Copyright © https://steam.oxxostudio.tw

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=R93ce4FZGbc")
print(yt.streams.all())


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code033.py

# Copyright © https://steam.oxxostudio.tw

from pytube import YouTube


def onProgress(stream, chunk, remains):
    total = stream.filesize  # 取得完整尺寸
    percent = (total - remains) / total * 100  # 減去剩餘尺寸 ( 剩餘尺寸會抓取存取的檔案大小 )
    print(f"下載中… {percent:05.2f}", end="\r")  # 顯示進度，\r 表示不換行，在同一行更新


print("download...")
yt = YouTube(
    "https://www.youtube.com/watch?v=R93ce4FZGbc", on_progress_callback=onProgress
)
yt.streams.filter().get_highest_resolution().download(filename="oxxostudio.mp4")
# on_progress_callback 參數等於 onProgress 函式
print()
print("ok!")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code034.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=R93ce4FZGbc")
print("download...")
yt.streams.filter().get_audio_only().download(filename="oxxostudio.mp3")
# 儲存為 mp3
print("ok!")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code035.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用

from pytube import YouTube
from bs4 import BeautifulSoup

yt = YouTube("https://www.youtube.com/watch?v=R93ce4FZGbc")
print(yt.captions)  # 取得所有語系
caption = yt.captions.get_by_language_code("en")  # 取得英文語系
xml = caption.xml_captions  # 將語系轉換成 xml
# print(xml)


def xml2srt(text):
    soup = BeautifulSoup(text)  # 使用 BeautifulSoup 轉換 xml
    ps = soup.findAll("p")  # 取出所有 p tag 內容

    output = ""  # 輸出的內容
    num = 0  # 每段字幕編號
    for i, p in enumerate(ps):
        try:
            a = p["a"]  # 如果是自動字幕，濾掉有 a 屬性的 p tag
        except:
            try:
                num = num + 1  # 每段字幕編號加 1
                text = p.text  # 取出每段文字
                t = int(p["t"])  # 開始時間
                d = int(p["d"])  # 持續時間

                h, tm = divmod(t, (60 * 60 * 1000))  # 轉換取得小時、剩下的毫秒數
                m, ts = divmod(tm, (60 * 1000))  # 轉換取得分鐘、剩下的毫秒數
                s, ms = divmod(ts, 1000)  # 轉換取得秒數、毫秒

                t2 = t + d  # 根據持續時間，計算結束時間
                if t2 > int(ps[i + 1]["t"]):
                    t2 = int(ps[i + 1]["t"])  # 如果時間算出來比下一段長，採用下一段的時間
                h2, tm = divmod(t2, (60 * 60 * 1000))  # 轉換取得小時、剩下的毫秒數
                m2, ts = divmod(tm, (60 * 1000))  # 轉換取得分鐘、剩下的毫秒數
                s2, ms2 = divmod(ts, 1000)  # 轉換取得秒數、毫秒

                output = output + str(num) + "\n"  # 產生輸出的檔案，\n 表示換行
                output = (
                    output
                    + f"{h:02d}:{m:02d}:{s:02d},{ms:03d} --> {h2:02d}:{m2:02d}:{s2:02d},{ms2:03d}"
                    + "\n"
                )
                output = output + text + "\n"
                output = output + "\n"
            except:
                pass

    return output


# print(xml2srt(xml))
with open("oxxostudio.srt", "w") as f1:
    f1.write(xml2srt(xml))  # 儲存為 srt

print("ok!")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code036.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用

from pytube import Playlist

playlist = Playlist(
    "https://www.youtube.com/watch?v=mOPRaLPh-YU&list=PL9ACDjBMkp9wViVmgpYweGkNqh62pHspF"
)
# 讀取影片清單
print(playlist.video_urls)  # 印出清單結果
"""
['https://www.youtube.com/watch?v=mOPRaLPh-YU',
 'https://www.youtube.com/watch?v=wARhTJH1fJI',
 'https://www.youtube.com/watch?v=WLjePGUCRqc']
"""


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code037.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用

from pytube import Playlist, YouTube

playlist = Playlist(
    "https://www.youtube.com/watch?v=mOPRaLPh-YU&list=PL9ACDjBMkp9wViVmgpYweGkNqh62pHspF"
)
print("download...")
for i in playlist.video_urls:
    print(i)
    yt = YouTube(i)  # 讀取影片
    yt.streams.filter().get_highest_resolution().download()  # 下載為最高畫質影片
print("ok!")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code038.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "https://notify-api.line.me/api/notify"
token = "剛剛複製的權杖"
headers = {"Authorization": "Bearer " + token}  # 設定權杖
data = {"message": "測試一下！"}  # 設定要發送的訊息
data = requests.post(url, headers=headers, data=data)  # 使用 POST 方法


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code039.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "https://notify-api.line.me/api/notify"
token = "剛剛複製的權杖"
headers = {"Authorization": "Bearer " + token}
data = {"message": "測試一下！", "stickerPackageId": "446", "stickerId": "1989"}
data = requests.post(url, headers=headers, data=data)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code040.py

# Copyright © https://steam.oxxostudio.tw

import requests

url = "https://notify-api.line.me/api/notify"
token = "剛剛複製的權杖"
headers = {"Authorization": "Bearer " + token}
data = {
    "message": "測試一下！",
    "imageThumbnail": "https://steam.oxxostudio.tw/downlaod/python/line-notify-demo.png",
    "imageFullsize": "https://steam.oxxostudio.tw/downlaod/python/line-notify-demo.png",
}
data = requests.post(url, headers=headers, data=data)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code041.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()  # 轉換成 dict 格式
    print(req)
    reText = req["queryResult"]["fulfillmentText"]  # 取得回覆文字
    print(reText)
    return {"fulfillmentText": f"{reText} ( webhook )", "source": "webhookdata"}


app.run()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code042.py

# Copyright © https://steam.oxxostudio.tw

from flask import Flask, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # 連結 ngrok


@app.route("/")
def home():
    return "<h1>hello world</h1>"


@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()
    print(req)
    reText = req["queryResult"]["fulfillmentText"]
    print(reText)
    return {"fulfillmentText": f"{reText} ( webhook )", "source": "webhookdata"}


app.run()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code043.py

# Copyright © https://steam.oxxostudio.tw


def webhook(request):
    try:
        req = request.get_json()
        reText = req["queryResult"]["fulfillmentText"]
        return {"fulfillmentText": f"{reText} ( webhook )", "source": "webhookdata"}
    except:
        print(request.args)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code044.py

# Copyright © https://steam.oxxostudio.tw

import os
import google.cloud.dialogflow_v2 as dialogflow
from flask import Flask, request

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow_key.json"  # 剛剛下載的金鑰 json
project_id = "XXXX"  # dialogflow 的 project id
language = "zh-TW"  # 語系
session_id = "oxxostudio"  # 自訂義的 session id


def dialogflowFn(text):
    session_client = dialogflow.SessionsClient()  # 使用 Token 和 dialogflow 建立連線
    session = session_client.session_path(project_id, session_id)  # 連接對應專案
    text_input = dialogflow.types.TextInput(text=text, language_code=language)  # 設定語系
    query_input = dialogflow.types.QueryInput(text=text_input)  # 根據語系取得輸入內容
    try:
        response = session_client.detect_intent(
            session=session, query_input=query_input
        )  # 連線 Dialogflow 取得回應資料
        print("input:", response.query_result.query_text)
        print("intent:", response.query_result.intent.display_name)
        print("reply:", response.query_result.fulfillment_text)
        return response.query_result.fulfillment_text  # 回傳回應的文字
    except:
        return "error"


app = Flask(__name__)


@app.route("/")
def home():
    text = request.args.get("text")  # 取得輸入的文字
    reply = dialogflowFn(text)  # 取得 Dialogflow 回應的文字
    return reply


app.run()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code045.py

# Copyright © https://steam.oxxostudio.tw

import os
import google.cloud.dialogflow_v2 as dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow_key.json"  # 金鑰 json
project_id = "XXXX"  # dialogflow 的 project id
language = "zh-TW"  # 語系
session_id = "oxxostudio"  # 自訂義的 session id


def dialogflowFn(text):
    session_client = dialogflow.SessionsClient()  # 使用 Token 和 dialogflow 建立連線
    session = session_client.session_path(project_id, session_id)  # 連接對應專案
    text_input = dialogflow.types.TextInput(text=text, language_code=language)  # 設定語系
    query_input = dialogflow.types.QueryInput(text=text_input)  # 根據語系取得輸入內容
    try:
        response = session_client.detect_intent(
            session=session, query_input=query_input
        )  # 連線 Dialogflow 取得回應資料
        print("input:", response.query_result.query_text)
        print("intent:", response.query_result.intent.display_name)
        print("reply:", response.query_result.fulfillment_text)
        return response.query_result.fulfillment_text  # 回傳回應的文字
    except:
        return "error"


def webhook(request):
    try:
        # req = request.get_json()
        text = request.args.get("text")
        return dialogflowFn(text)
    except:
        print(request.args)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code046.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)  # 初始化，第二個參數作用在負責使用者登入資訊，通常設定為 None
fdb.put("/", "oxxo", 123)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code047.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.put("/test", "oxxo", 123)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code048.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.put("/", "oxxo", {"apple": 100, "orange": 200})


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code048-1.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.put("/", "oxxo", [123, 456, 789])

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code049.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.post("/", 123)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code050.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.post("/oxxo", 123)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code051.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.post("/", {"apple": 100, "orange": 200})

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code052.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
result = fdb.get("/", "oxxo")
print(result)  # 123

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code053.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
result = fdb.get("/fruit", "apple")
print(result)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code054.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
result = fdb.get("/", None)
print(result)  # {'fruit': {'apple': 100, 'orange': 200}, 'oxxo': 123}
print(result["fruit"]["apple"])  # 100

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code055.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.delete("/", "oxxo")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code056.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)
fdb.delete("/", None)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code056-1.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase
import time

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)

for i in range(10):
    fdb.put("/", f"a{i}", time.time())

for i in range(10):
    fdb.put_async("/", f"b{i}", time.time())

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code057.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)


def oxxo_callback(response):
    print("ok")


fdb.put_async("/", "oxxo", 123, oxxo_callback)  # ok

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code058.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase
import time

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)

for i in range(10):
    fdb.post("/", time.time())

for i in range(10):
    fdb.post_async("/", time.time())

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code059.py

# Copyright © https://steam.oxxostudio.tw

from firebase import firebase

url = "https://XXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)


def oxxo_callback(response):
    print("ok")


fdb.post_async("/", 123, oxxo_callback)  # ok

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code060.py

# Copyright © https://steam.oxxostudio.tw

import openai

openai.api_key = "你的 API Key"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="講個笑話來聽聽",
    max_tokens=128,
    temperature=0.5,
)

completed_text = response["choices"][0]["text"]
print(completed_text)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code062.py

# Copyright © https://steam.oxxostudio.tw

import openai

openai.api_key = "你的 API KEY"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=128,
    temperature=0.5,
    messages=[
        {"role": "user", "content": "我叫做 oxxo"},
        {"role": "assistant", "content": "原來你是 oxxo 呀"},
        {"role": "user", "content": "請問我叫什麼名字？"},
    ],
)
print(response.choices[0].message.content)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code063.py

# Copyright © https://steam.oxxostudio.tw

import openai

openai.api_key = "你的 API Key"

messages = ""
while True:
    msg = input("me > ")
    messages = f"{messages}{msg}\n"  # 將過去的語句連接目前的對話，後方加上 \n 可以避免標點符號結尾問題
    response = openai.Completion.create(
        model="text-davinci-003", prompt=messages, max_tokens=128, temperature=0.5
    )

    ai_msg = response["choices"][0]["text"].replace("\n", "")
    print("ai > " + ai_msg)
    messages = f"{messages}\n{ai_msg}\n\n"  # 合併 AI 回應的話


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code064.py

# Copyright © https://steam.oxxostudio.tw

import openai

openai.api_key = "你的 API Key"

messages = []
while True:
    msg = input("me > ")
    messages.append({"role": "user", "content": msg})  # 添加 user 回應
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", max_tokens=128, temperature=0.5, messages=messages
    )
    ai_msg = response.choices[0].message.content.replace("\n", "")
    messages.append({"role": "assistant", "content": ai_msg})  # 添加 ChatGPT 回應
    print(f"ai > {ai_msg}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code065.py

# Copyright © https://steam.oxxostudio.tw

import openai

openai.api_key = "你的 API Key"

from firebase import firebase

url = "https://XXXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)  # 初始化 Firebase Realtime database
chatgpt = fdb.get("/", "chatgpt")  # 取的 chatgpt 節點的資料

if chatgpt == None:
    messages = ""  # 如果節點沒有資料，訊息內容設定為空
else:
    messages = chatgpt  # 如果節點有資料，使用該資料作為歷史聊天記錄

while True:
    msg = input("me > ")
    if msg == "!reset":
        message = ""
        fdb.delete("/", "chatgpt")  # 如果輸入 !reset 就清空歷史紀錄
        print("ai > 對話歷史紀錄已經清空！")
    else:
        messages = f"{messages}{msg}\n"  # 在輸入的訊息前方加上歷史紀錄
        response = openai.Completion.create(
            model="text-davinci-003", prompt=messages, max_tokens=128, temperature=0.5
        )

        ai_msg = response["choices"][0]["text"].replace("\n", "")  # 取得 ChatGPT 的回應
        print("ai > " + ai_msg)
        messages = f"{messages}\n{ai_msg}\n\n"  # 在訊息中加入 ChatGPT 的回應
        fdb.put("/", "chatgpt", messages)  # 更新資料庫資料


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch17\code066.py

# Copyright © https://steam.oxxostudio.tw

import openai

openai.api_key = "你的 API Key"

from firebase import firebase

url = "https://XXXXXXXXXXX.firebaseio.com"
fdb = firebase.FirebaseApplication(url, None)  # 初始化 Firebase Realtimr database
chatgpt = fdb.get("/", "chatgpt")  # 讀取 chatgpt 節點中所有的資料

if chatgpt == None:
    messages = []  # 如果沒有資料，預設訊息為空串列
else:
    messages = chatgpt  # 如果有資料，訊息設定為該資料

while True:
    msg = input("me > ")
    if msg == "!reset":
        fdb.delete("/", "chatgpt")  # 如果輸入 !reset 就清空 chatgpt 的節點內容
        messages = []
        print("ai > 對話歷史紀錄已經清空！")
    else:
        messages.append({"role": "user", "content": msg})  # 將輸入的訊息加入歷史紀錄的串列中
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", max_tokens=128, temperature=0.5, messages=messages
        )
        ai_msg = response.choices[0].message.content.replace("\n", "")  # 取得回應訊息
        messages.append({"role": "assistant", "content": ai_msg})  # 將回應訊息加入歷史紀錄串列中
        fdb.put("/", "chatgpt", messages)  # 更新 chatgpt 節點內容
        print(f"ai > {ai_msg}")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
