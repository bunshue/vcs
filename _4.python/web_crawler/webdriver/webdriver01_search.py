print("在 google / youtube / yahoo / 維基百科 輸入搜尋字串, 並存圖")

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 建立瀏覽器物件
driver = webdriver.Chrome()  # 使用Chrome
# driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)  # 設定視窗位置
driver.set_window_size(800, 600)  # 設定視窗大小
# driver.maximize_window()    #全螢幕顯示

search_word = "獅子"

print("------------------------------------------------------------")  # 60個
print("在 google 輸入搜尋字串")

url = "https://www.google.com/"
driver.get(url)  # 開啟網址
time.sleep(3)

"""
Copy element 或 Copy outerHTML
<textarea class="gLFyf" jsaction="paste:puy29d;" id="APjFqb" maxlength="2048" name="q" rows="1"
aria-activedescendant="" aria-autocomplete="both" aria-controls="Alh6id" aria-expanded="false"
aria-haspopup="both" aria-owns="Alh6id" autocapitalize="off" autocomplete="off" autocorrect="off"
autofocus="" role="combobox" spellcheck="false" title="Google 搜尋" type="search" value="" aria-label="搜尋"
data-ved="0ahUKEwjBkLT1_7L_AhWhrVYBHSArAb0Q39UDCAY" style=""></textarea>
"""

# 使用 class, ok
# txt = driver.find_element(By.CLASS_NAME, 'gLFyf') # 取得 class 為 xxxx 的網頁元素 ( TextArea )
# 使用 id, ok
# txt = driver.find_element(By.ID, 'APjFqb')        # 取得 id 為 xxxx 的網頁元素 ( TextArea )
# 使用 name, ok
txt = driver.find_element(By.NAME, "q")  # 取得屬性 name 為 xxxx 的網頁元素 ( TextArea )

txt.send_keys(search_word)
time.sleep(2)

txt.clear()
search_word = "老虎"
txt.send_keys(search_word)
time.sleep(2)

txt.send_keys(Keys.RETURN)
time.sleep(4)
driver.save_screenshot("screenshot_google.png")  # 存圖
time.sleep(1)

print("------------------------------------------------------------")  # 60個
print("在 youtube 輸入搜尋字串")

url = "https://www.youtube.com/"
driver.get(url)  # 開啟網址
time.sleep(3)

"""
Copy element 或 Copy outerHTML
<input id="search" autocapitalize="none" autocomplete="off" autocorrect="off"
name="search_query" tabindex="0" type="text" spellcheck="false" placeholder="搜尋"
aria-label="搜尋" role="combobox" aria-haspopup="false" aria-autocomplete="list"
dir="ltr" class="ytd-searchbox" style="outline: none;">
"""

# 使用 class, fail
# txt = driver.find_element(By.CLASS_NAME, 'ytd-searchbox') # 取得 class 為 xxxx 的網頁元素 ( TextArea )
# 使用 id, fail
# txt = driver.find_element(By.ID, 'search')        # 取得 id 為 xxxx 的網頁元素 ( TextArea )
# 使用 name, ok
txt = driver.find_element(
    By.NAME, "search_query"
)  # 取得屬性 name 為 xxxx 的網頁元素 ( TextArea )

txt.send_keys(search_word)
time.sleep(2)
txt.send_keys(Keys.RETURN)
time.sleep(4)
driver.save_screenshot("screenshot_youtube.png")  # 存圖
time.sleep(1)

print("------------------------------------------------------------")  # 60個
print("在 yahoo 輸入搜尋字串")

url = "https://tw.yahoo.com/?p=us"
driver.get(url)  # 開啟網址
time.sleep(3)

"""
Copy element 或 Copy outerHTML
<input type="text" id="header-search-input" aria-autocomplete="both"
aria-label="" placeholder="基隆民宿" data-term-type="revenue" autocapitalize="off" autocomplete="off"
class="Bgc(#fff) Bd Bdrsbstart(4px) Bdc(#b0b0b0) Bdendw(0)  Bdrststart(4px) Bxsh(n) Bxz(bb) D(b) Fz(18px) H(inh) M(0) O(0)  W(100%) Bdc($c-fuji-blue-1-c):f Bdc(#949494):h Bdrsbend(4px) Bdrstend(4px) Pstart(10px) Pend(110px) Pos(r) Z(2)"
name="p" role="combobox" data-rapid_p="2" data-v9y="1">

"""

# 使用 class, fail
# txt = driver.find_element(By.CLASS_NAME, 'ytd-searchbox') # 取得 class 為 xxxx 的網頁元素 ( TextArea )
# 使用 id, ok
txt = driver.find_element(
    By.ID, "header-search-input"
)  # 取得 id 為 xxxx 的網頁元素 ( TextArea )
# 使用 name, ok
# txt = driver.find_element(By.NAME, 'p')             # 取得屬性 name 為 xxxx 的網頁元素 ( TextArea )

txt.send_keys(search_word)
time.sleep(2)
txt.send_keys(Keys.RETURN)
time.sleep(4)
driver.save_screenshot("screenshot_yahoo.png")  # 存圖
time.sleep(1)

print("------------------------------------------------------------")  # 60個
print("在 維基百科 輸入搜尋字串")

url = "https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5"
driver.get(url)  # 開啟網址
time.sleep(3)

"""
Copy element 或 Copy outerHTML
<input class="vector-search-box-input" type="search" name="search"
placeholder="搜尋維基百科" aria-label="搜尋維基百科" autocapitalize="sentences"
title="搜尋維基百科[alt-shift-f]" accesskey="f" id="searchInput" autocomplete="off">
"""

# 使用 class, ok
txt = driver.find_element(
    By.CLASS_NAME, "vector-search-box-input"
)  # 取得 class 為 xxxx 的網頁元素 ( TextArea )
# 使用 id, ok
# txt = driver.find_element(By.ID, 'searchInput')        # 取得 id 為 xxxx 的網頁元素 ( TextArea )
# 使用 name, ok
# txt = driver.find_element(By.NAME, 'search')             # 取得屬性 name 為 xxxx 的網頁元素 ( TextArea )

txt.send_keys(search_word)
time.sleep(2)
txt.send_keys(Keys.RETURN)
time.sleep(4)
driver.save_screenshot("screenshot_wiki.png")  # 存圖
time.sleep(1)

print("------------------------------------------------------------")  # 60個
print("完成")

"""
print('準備關閉瀏覽器')
for i in range(0, 10):
    print(i, '秒')	# 0~9
    time.sleep(1)

#print('關閉瀏覽器')
#driver.close()  #關閉瀏覽器

print('關閉瀏覽器並且退出驅動程序')
driver.quit()   #關閉瀏覽器並且退出驅動程序
"""
