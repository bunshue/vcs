from selenium import webdriver    # 匯入 selenium 的 webdriver 子套件
from time import sleep         # 匯入內建 time 模組的 sleep() 函式 (計時用)
browser = webdriver.Chrome()   # 建立 Chrome 瀏覽器物件
browser.get('http://www.flag.com.tw')  # 開啟 Chrome 並連到旗標網站
sleep(5)                       # 暫停 5 秒
browser.close()                # 關閉網頁(目前分頁)A
