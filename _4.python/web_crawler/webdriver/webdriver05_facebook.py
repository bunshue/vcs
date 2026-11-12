import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# 設定facebook登入資訊
url = "https://www.facebook.com/"
email = "你的faceook電子郵件"
password = "你的faceook密碼"

driver = webdriver.Chrome()  # 使用Chrome
# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id("email").send_keys(email)  # 輸入郵件
driver.find_element_by_id("pass").send_keys(password)  # 輸入密碼
driver.find_element_by_id("loginbutton").click()  # 按登入鈕
driver.find_element_by_name("login").click()  # 按登入鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 設定facebook登入資訊
url = "https://www.facebook.com/"
email = "你的faceook電子郵件"
password = "你的faceook密碼"

# 取消 Alert
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(chrome_options=chrome_options)  # 使用Chrome

# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)

# 執行自動登入動作
driver.find_element_by_id("email").send_keys(email)  # 輸入郵件
driver.find_element_by_id("pass").send_keys(password)  # 輸入密碼
driver.find_element_by_name("login").click()  # 按登入鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 你的資訊
url = "https://www.facebook.com/"
email = "YOUR EMAIL"
password = "YOUR PASSWORD"

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()  # 全螢幕顯示

# 進入Facebook登入畫面
driver.get(url)

# 填入帳號密碼，並送出
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("login").click()

# 等待10秒
time.sleep(10)

driver.quit()  # 關閉瀏覽器並且退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 你的資訊
url = "https://www.facebook.com/"
email = "YOUR EMAIL"
password = "YOUR PASSWORD"

# 防止跳出通知
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options
)

driver.maximize_window()  # 全螢幕顯示

# 進入Facebook登入畫面
driver.get(url)

# 填入帳號密碼，並送出
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("login").click()

# 登入後等待10秒
time.sleep(10)

driver.quit()  # 關閉瀏覽器並且退出驅動程序


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 你的資訊
url = "https://www.facebook.com/"
email = "YOUR EMAIL"
password = "YOUR PASSWORD"

# 防止跳出通知
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options
)

driver.maximize_window()  # 全螢幕顯示

# 進入Facebook登入畫面
driver.get(url)

# 填入帳號密碼，並送出
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("login").click()

time.sleep(5)

# 進入木棉花專頁
driver.get("https://www.facebook.com/emuse.com.tw")

time.sleep(5)

# 往下滑3次，讓Facebook載入文章內容
for x in range(3):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("scroll")
    time.sleep(5)

root = BeautifulSoup(driver.page_source, "html.parser")

# 定位文章標題
titles = root.find_all(
    "div", class_="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q"
)
for title in titles:
    # 定位每一行標題
    posts = title.find_all("div", dir="auto")
    # 如果有文章標題才印出
    if len(posts) != 0:
        for post in posts:
            print(post.text)

    print("-" * 30)

# 建立資料夾
if not os.path.exists("images"):
    os.mkdir("images")

# 下載圖片
images = root.find_all(
    "img",
    class_=[
        "i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm bixrwtb6",
        "i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm",
    ],
)
if len(images) != 0:
    for index, image in enumerate(images):
        img = requests.get(image["src"])
        with open(f"images/img{index+1}.jpg", "wb") as file:
            file.write(img.content)
        print(f"第 {index+1} 張圖片下載完成!")

# 等待5秒
time.sleep(5)

driver.quit()  # 關閉瀏覽器並且退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

email_address = "<電子郵件地址>"
password = "<密碼>"

driver = webdriver.Chrome()  # 使用Chrome

driver.implicitly_wait(10)
url = "https://www.facebook.com/"
driver.get(url)

email = driver.find_element_by_css_selector("#email")
email.send_keys(email_address)

time.sleep(0.5)

passwd = driver.find_element_by_css_selector("#pass")
passwd.send_keys(password)

time.sleep(0.5)

button = driver.find_element_by_css_selector("#loginbutton")
button.click()

time.sleep(5)

soup = BeautifulSoup(driver.page_source, "lxml")
tag_title = soup.find("title")
print(tag_title.text)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# loginFacebook.py

# 設定facebook登入資訊
url = "https://www.facebook.com/"
email = "你的faceook電子郵件"
password = "你的faceook密碼"

driver = webdriver.Chrome()  # 使用Chrome

# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id("email").send_keys(email)  # 輸入郵件
driver.find_element_by_id("pass").send_keys(password)  # 輸入密碼
driver.find_element_by_id("loginbutton").click()  # 按登入鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 登入 facebook

# 會出現 Alert 視窗
url = "https://www.facebook.com/"
email = "您的 Email 帳號"
password = "您的密碼"
driver = webdriver.Chrome()

# 取消 Alert
url = "https://www.facebook.com/"
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# 設定facebook登入資訊
url = "https://www.facebook.com/"
email = "你的faceook電子郵件"
password = "你的faceook密碼"

# 建立瀏覽器物件
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Chrome()    #使用Chrome
# driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)  # 設定視窗位置
driver.set_window_size(800, 600)  # 設定視窗大小
driver.maximize_window()  # 全螢幕顯示

driver.get(url)

# 執行自動登入動作
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys(email)

time.sleep(3)  # 必須加入等待，否則會有誤動作

driver.find_element_by_id("pass").clear()
driver.find_element_by_id("pass").send_keys(password)

driver.find_element_by_id("loginbutton").click()  # 按 登入 鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
