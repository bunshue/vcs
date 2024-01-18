# ch24_1.py
from selenium import webdriver

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
print(type(browser))





#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch24\ch24_2.py

# ch24_2.py
from selenium import webdriver

dirverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(dirverPath)
print(type(browser))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch24\ch24_3.py

# ch24_3.py
from selenium import webdriver

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://aaa.24ht.com.tw'
browser.get(url)                # 網頁下載至瀏覽器


            


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch24\ch24_4.py

# ch24_4.py
from selenium import webdriver

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://aaa.24ht.com.tw'
browser.get(url)                # 網頁下載至瀏覽器

print(f"網頁標題內容是 = {browser.title}")

tag1 = browser.find_element_by_id('author')             # 傳回<h1>
print(f"\n標籤名稱 = {tag1.tag_name}, 內容是 = {tag1.text}")

print()
tag2 = browser.find_elements_by_id('content')           # 傳回<h1>
for i in range(len(tag2)):
    print(f"標籤名稱 = {tag2[i].tag_name}, 內容是 = {tag2[i].text}")

print()
tag3 = browser.find_elements_by_tag_name('p')           # 傳回<p>
for i in range(len(tag3)):
    print(f"標籤名稱 = {tag3[i].tag_name}, 內容是 = {tag3[i].text}")

print()
tag4 = browser.find_elements_by_tag_name('img')         # 傳回<img>
for i in range(len(tag4)):
    print(f"標籤名稱 = {tag4[i].tag_name}, 內容是 = {tag4[i].get_attribute('src')}")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch24\ch24_5.py

# ch24_5.py
from selenium import webdriver
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'https://deepwisdom.com.tw'
browser.get(url)                # 網頁下載至瀏覽器

eleLink = browser.find_element_by_link_text('深智數位緣起')
print(type(eleLink))            # 列印eleLink資料類別
time.sleep(5)                   # 暫停5秒
eleLink.click()                 








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch24\ch24_6.py

# ch24_6.py
from selenium import webdriver
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://www.google.com'
browser.get(url)                        # 網頁下載至瀏覽器

txtBox = browser.find_element_by_name('q')
txtBox.send_keys('明志科技大學')        # 輸入表單資料
time.sleep(5)                           # 暫停5秒
txtBox.submit()                         # 送出表單










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch24\ch24_7.py

# ch24_7.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://www.mcut.edu.tw'
browser.get(url)                    # 網頁下載至瀏覽器

ele = browser.find_element_by_tag_name('body')
time.sleep(3)
ele.send_keys(Keys.PAGE_DOWN)       # 網頁捲動到下一頁
time.sleep(3)
ele.send_keys(Keys.END)             # 網頁捲動到最底端
time.sleep(3)
ele.send_keys(Keys.PAGE_UP)         # 網頁捲動到上一頁
time.sleep(3)
ele.send_keys(Keys.HOME)            # 網頁捲動到最上端









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch24\ch24_8.py

# ch24_8.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'https://deepwisdom.com.tw'
browser.get(url)                    # 網頁下載至瀏覽器

time.sleep(3)
browser.refresh()                   # 更新網頁
time.sleep(3)
browser.quit()                      # 關閉網頁









print("------------------------------------------------------------")  # 60個



