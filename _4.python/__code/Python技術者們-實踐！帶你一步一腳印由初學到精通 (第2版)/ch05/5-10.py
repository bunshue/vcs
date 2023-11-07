from selenium import webdriver # 匯入 selenium 的 webdriver

browser = webdriver.Chrome() # 建立 Chrome 瀏覽器物件
browser.get('http://www.google.com') # 開啟 Chrome 並連到旗標網站
e1 = browser.find_element_by_tag_name('head')  # 尋找 head 標籤
print(e1.tag_name)  # 輸出 head 確認已找到 (tag_name 屬性為標籤名稱, 詳見下表)
e2 = e1.find_element_by_tag_name('title')  # 在 head 元素中尋找 title 標籤
print(e2.tag_name)  # 輸出 tite 確認已找到
browser.quit()     # 關閉視窗結束驅動