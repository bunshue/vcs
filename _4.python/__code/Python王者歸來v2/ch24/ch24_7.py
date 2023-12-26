# ch24_7.py
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
