import requests,re
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import sys
import pyocr
import pyocr.builders

def get_photo():
    global driver
    # 取出 綱頁圖中的驗證圖片，存入 <img_source.png> 檔
    # 請調整解析度

    #台灣高鐵訂票系統
    url = 'http://irs.thsrc.com.tw/IMINT'
    
    driver = requests.Session()   
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()    #全螢幕顯示
    
    # 從 screenshot 中取得驗證碼的圖片
    driver.save_screenshot("img_screenshot.png") 
    element = driver.find_element_by_id('BookingS1Form_homeCaptcha_passCode')
    
    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']
    
    img = Image.open("img_screenshot.png")
    img2 = img.crop((left,top,right,bottom))
    #img2.show()
    img2.save('img_source.png')

def codeocr(offset):
    global result    
    img = cv2.imread("img_source.png")
    dst = cv2.fastNlMeansDenoisingColored(img,None,30,30,7,21) # 去雜點
    ret,thresh = cv2.threshold(dst,127,255,cv2.THRESH_BINARY_INV)  #黑白
    imgarr = cv2.cvtColor(thresh,cv2.COLOR_BGR2GRAY) #灰階    
#    plt.imshow(thresh)
#    plt.show()
    
#    print(imgarr.shape)
    height = imgarr.shape[0]  # 高度
    width = imgarr.shape[1]  # 寬度
    
    start = offset   # 要測試後調整，offset 為左右留的邊界
    end = width-offset 
    
    # 去除回歸曲線
    imgarr[:,start:end] = 0  # 從左邊界起至右邊界止，全部挖空
    imagedata=np.where(imgarr == 255) # 找到所有白色的點
    
    plt.scatter(imagedata[1], height - imagedata[0], s = 100, color = "red", label = "Cluster")
    plt.ylim(0, height)
#    plt.show() # 顯示起始、結束
    
    ploy_reg = PolynomialFeatures(degree = 2) #以二次多項式建立特徵   
    X = np.array([imagedata[1]]) #取得 X座標
    Y = height-imagedata[0]
    X_ = ploy_reg.fit_transform(X.T) #特徵數據轉換
    regr = LinearRegression() #建立線性回歸線
    regr.fit(X_, Y)
    LinearRegression(copy_X = True, fit_intercept = True, n_jobs = 1, normalize = False)
    
    X2 = np.array([[i for i in range(0,width)]])
    X2_ = ploy_reg.fit_transform(X2.T)
#    plt.plot(X2.T, regr.predict(X2_), color = "blue", linewidth = 30) #顯示回歸線
    
    grayimg = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY) 
    for ele in np.column_stack([regr.predict(X2_).round(0), X2[0],] ):
        pos=height-int(ele[0])
        try:
            grayimg[pos-3:pos+3, int(ele[1])] = 255 - grayimg[pos-3:pos + 3, int(ele[1])]
        except IndexError:
            pass
    
    cv2.imwrite("temp.png", grayimg)  #存檔             
    _, inv = cv2.threshold(grayimg, 150, 255, cv2.THRESH_BINARY_INV)  #轉為反相黑白
    for i in range(len(inv)):  #i為每一列
        for j in range(len(inv[i])):  #j為每一行
            if inv[i][j] == 255:  #顏色為白色
                count = 0 
                for k in range(-2, 3):
                    for l in range(-2, 3):
                        try:
                            if inv[i + k][j + l] == 255:  #若是白點就將count加1
                                count += 1
                        except IndexError:
                            pass
                if count <= 6:  #週圍少於等於6個白點
                    inv[i][j] = 0  #將白點去除    
            
    dilation = cv2.dilate(inv, (8, 8), iterations = 1)  #圖形加粗
    cv2.imwrite("final.png", dilation)
    
    #文字辨識 
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    tool = tools[0]  #取得可用工具
    
    result = tool.image_to_string(
        Image.open('final.png'),
        builder=pyocr.builders.TextBuilder()
    )
   
def inputdata(): #輸入資料
    global result,login_sucess,driver
    #填寫資料
    driver.find_element_by_xpath("//option[@value='6']").click() # 起站--台中
    driver.find_element_by_xpath("(//option[@value='5'])[2]").click() # 到站--苗票
    driver.find_element_by_id("trainCon:trainRadioGroup_1").click()  #車廂種類--商務車廂
    sleep(0.5)    
    driver.find_element_by_id("seatRadio0").click()    #座位喜好--無
    driver.find_element_by_id("ToTimePicker").click()  # 去程時間日曆
    driver.find_element_by_xpath("//tr[4]/td[8]").click() # 5月27日   
    driver.find_element_by_name("toTimeTable").click()  #出發
    driver.find_element_by_xpath("//option[@value='1100A']").click() #早上 11:00   
    driver.find_element_by_name("ticketPanel:rows:0:ticketAmount").click()  #票數：全票 1
    driver.find_element_by_xpath("//option[@value='1F']").click()
    sleep(0.5)    
    # 輸入驗證碼
    results=[]
    counter=0
    login_sucess=False
    while len(results)==0 and counter<6: # 如果重複6次仍不成功就放棄
        counter+=1
        print("測試次數=",counter)
        offset=1 # 回歸線曲度從 1~16 測試
        results=[]
        while offset<16:
    #        print("回歸線曲度=",offset)
            offset+=1
            codeocr(offset)  # 文字辨識
            result=result.replace(" ","").strip()
            result=re.findall('[a-zA-Z0-9]*',result)[0]
            if len(result)==4: #如果有4個字元
                results.append(result)
                
        if len(results)>0:
            results=set(results)
            print(results)            
            for key in results:
                print("輸入驗證碼：",key)
                driver.find_element_by_name("homeCaptcha:securityCode").clear()       
                driver.find_element_by_name("homeCaptcha:securityCode").send_keys(key)  #輸入驗證碼      
                driver.find_element_by_id("SubmitButton").click()  # 去開始查詢
                sleep(2)
                login_sucess=False
                try:
                    if driver.find_element_by_class_name("section_title").text!="":  #訂位明細
                        login_sucess=True
                        break
                    else:
                        print("登錄失敗")  
                except:    
                    print("驗證失敗!")
  
# 主程式     
for i in range(1,11): # 每測一次後停 2 秒，重複測10次
    print("\n第",i,"次開啟瀏覽器")
    get_photo()  #取得驗證碼圖片
    sleep(2)
    inputdata() # 輸入資料
    if login_sucess==True:
        break
    else:
        print("關閉第",i,"次開啟的瀏覽器")
        driver.quit()   #關閉瀏覽器並且退出驅動程序
    
if login_sucess==True:
    driver.find_element_by_xpath("//input[@name='SubmitButton']").click() # 按 確認車次 鈕
    sleep(0.5)
    if driver.find_element_by_class_name("table_simple").text!="":  #訂位明細
        soup=BeautifulSoup(driver.page_source,"html.parser")                    
        items=soup.select(".table_simple span")
        for item in items:
            print(item.text,end=" ")
        print() 
    driver.find_element_by_id("idNumber").send_keys("A123456789")    #身分證字號 
    driver.find_element_by_id("mobileInputRadio").click()  # 
    driver.find_element_by_id("mobilePhone").send_keys("0937765432") #行動電話
    driver.find_element_by_id("name2622").send_keys("chiou@e-happy.com.tw") #mail   
    driver.find_element_by_name("agree").click()  #我同意
    #driver.find_element_by_id("isSubmit").click()  # 完成訂位
    sleep(0.5)        
                
                
                
