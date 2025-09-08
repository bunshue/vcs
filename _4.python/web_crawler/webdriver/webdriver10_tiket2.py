from selenium import webdriver
from PIL import Image

# 取出 綱頁圖中的驗證圖片，存入 <img_source.png> 檔
# 請調整解析度

url = "https://irs.thsrc.com.tw/IMINT"  # 台灣高鐵訂票系統

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()  # 全螢幕顯示

driver.save_screenshot("tmp_img_screenshot.png")  # 存圖

element = driver.find_element_by_id("BookingS1Form_homeCaptcha_passCode")

left = element.location["x"]
top = element.location["y"]
right = element.location["x"] + element.size["width"]
bottom = element.location["y"] + element.size["height"]

img = Image.open("tmp_img_screenshot.png")

img2 = img.crop((left, top, right, bottom))
img2.save("tmp_img_source.png")
