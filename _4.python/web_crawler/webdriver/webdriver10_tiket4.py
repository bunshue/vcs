import time
from selenium import webdriver
from PIL import Image
from simshow import simshow  #以 pip install simple-imshow 安裝模組

delay = 0.3

url = 'https://irs.thsrc.com.tw/IMINT'		#台灣高鐵訂票系統

driver = webdriver.Chrome()
driver.maximize_window()    #全螢幕顯示

driver.get(url)
time.sleep(delay)  #加入等待

driver.find_element_by_id("btn-confirm").click()
time.sleep(delay)

driver.save_screenshot('tem.png')  #擷取螢幕後存檔
captchaid = driver.find_element_by_id('BookingS1Form_homeCaptcha_passCode')  #驗證碼圖形id
#取得圖形位置
x1 = captchaid.location['x']
y1 = captchaid.location['y']
x2 = x1 + captchaid.size['width']
y2 = y1 + captchaid.size['height']
image1 = Image.open('tem.png')  #讀取螢幕圖形
image2 = image1.crop((x1, y1, x2, y2))  #擷取驗證碼圖形
image2.save('captcha.png')  #圖形存檔
simshow(image2)  #顯示圖形
captchatext = input('輸入驗證碼：')  

driver.find_element_by_name("selectStartStation").click()
time.sleep(delay)

driver.find_element_by_xpath("(//option[@value='2'])[1]").click()
time.sleep(delay)

driver.find_element_by_name("selectDestinationStation").click()
time.sleep(delay)

driver.find_element_by_xpath("(//option[@value='7'])[2]").click()
time.sleep(delay)

driver.find_element_by_id("seatRadio1").click()
time.sleep(delay)

driver.find_element_by_id("ToTimePicker").click()
time.sleep(delay)

driver.find_element_by_xpath("//tbody/tr[3]/td[3]").click()
time.sleep(delay)

driver.find_element_by_name("toTimeTable").send_keys("\n")
time.sleep(delay)

driver.find_element_by_xpath("(//option[@value='800A'])[1]").click()
time.sleep(delay)

driver.find_element_by_name("homeCaptcha:securityCode").send_keys("\n")
time.sleep(delay)

driver.find_element_by_name("homeCaptcha:securityCode").clear()
time.sleep(delay)

driver.find_element_by_name("homeCaptcha:securityCode").send_keys(captchatext)
time.sleep(delay)

driver.find_element_by_id("SubmitButton").click()
time.sleep(delay)

driver.find_element_by_xpath("(//input[@name='TrainQueryDataViewPanel:TrainGroup'])[3]").click()
time.sleep(delay)

driver.find_element_by_name("SubmitButton").click()
time.sleep(delay)

driver.find_element_by_id("idNumber").click()
time.sleep(delay)

driver.find_element_by_id("idNumber").clear()
time.sleep(delay)

driver.find_element_by_id("idNumber").send_keys("身分證字號")
time.sleep(delay)

driver.find_element_by_id("mobileInputRadio").click()
time.sleep(delay)

driver.find_element_by_id("mobilePhone").click()
time.sleep(delay)

driver.find_element_by_id("mobilePhone").clear()
time.sleep(delay)

driver.find_element_by_id("mobilePhone").send_keys("0922735901")
time.sleep(delay)

driver.find_element_by_name("agree").click()
time.sleep(delay)

#driver.find_element_by_id("isSubmit").click()
print('完成訂票！')
