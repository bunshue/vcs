from selenium import webdriver
from PIL import Image
from time import sleep

url="http://irs.thsrc.com.tw/IMINT"
driver=webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.find_element_by_id("btn-confirm").click()
sleep(0.3)
driver.save_screenshot("wholepage.png")
element=driver.find_element_by_id('header')  #取得網頁元素
#取得網頁元素位置
left=element.location['x']
top=element.location['y']
right=element.location['x'] + element.size['width']
bottom=element.location['y'] + element.size['height']

img=Image.open("wholepage.png")
img2=img.crop((left,top,right,bottom))
img2.save('crop.png')
