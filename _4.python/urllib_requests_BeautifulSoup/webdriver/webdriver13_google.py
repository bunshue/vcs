url = 'https://www.google.com/'

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 建立瀏覽器物件
driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
#driver.maximize_window()    #全螢幕顯示

driver.get(url)  # 開啟範例網址

time.sleep(3)

search_word = 'lion mouse'

'''
Copy element 或 Copy outerHTML
<textarea class="gLFyf" jsaction="paste:puy29d;" id="APjFqb" maxlength="2048" name="q" rows="1"
aria-activedescendant="" aria-autocomplete="both" aria-controls="Alh6id" aria-expanded="false"
aria-haspopup="both" aria-owns="Alh6id" autocapitalize="off" autocomplete="off" autocorrect="off"
autofocus="" role="combobox" spellcheck="false" title="Google 搜尋" type="search" value="" aria-label="搜尋"
data-ved="0ahUKEwjBkLT1_7L_AhWhrVYBHSArAb0Q39UDCAY" style=""></textarea>
'''

# 使用 class
# txt = driver.find_element(By.CLASS_NAME, 'gLFyf') # 取得 class 為 xxxx 的網頁元素 ( TextArea )
# 使用 id
# txt = driver.find_element(By.ID, 'APjFqb')        # 取得 id 為 xxxx 的網頁元素 ( TextArea )
# 使用 name
txt = driver.find_element(By.NAME, 'q')             # 取得屬性 name 為 q 的網頁元素 ( TextArea )

txt.send_keys(search_word)

time.sleep(2)

txt.send_keys(Keys.RETURN)


print('完成')
