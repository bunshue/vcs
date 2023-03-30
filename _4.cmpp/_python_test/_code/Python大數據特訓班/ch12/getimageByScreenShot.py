from selenium import webdriver
from PIL import Image # pillow 安裝 Anaconda 時已自動安裝

# 取出 綱頁圖中的驗證圖片，存入 <img_source.png> 檔
# 請調整解析度
url="http://irs.thsrc.com.tw/IMINT"
driver=webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.save_screenshot("img_screenshot.png") 
element=driver.find_element_by_id('BookingS1Form_homeCaptcha_passCode')

left=element.location['x']
top=element.location['y']
right=element.location['x'] + element.size['width']
bottom=element.location['y'] + element.size['height']

img=Image.open("img_screenshot.png")
img2=img.crop((left,top,right,bottom))
img2.save('img_source.png')