"""
Python自學聖經(第一版) 24~

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個



# ch26\faceRecog1.py

from io import BytesIO
from PIL import Image
from matplotlib import patches
import requests
import matplotlib.pyplot as plt

subscription_key = "你的人臉資源key"
face_base_url = "https://southeastasia.api.cognitive.microsoft.com/face/v1.0/"
face_url = face_base_url + 'detect'
image_url = "https://i.imgur.com/G4cZrJ0.jpg"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}
data    = {'url': image_url}
response = requests.post(face_url, headers=headers, params=params, json=data)
result = response.json()
#print(result)

#框選臉部及顯示部分資訊
image_file = BytesIO(requests.get(image_url).content)
image = Image.open(image_file)
plt.figure(figsize=(8,8))
ax = plt.imshow(image)
for face in result:
     fr = face["faceRectangle"]  #取得臉部坐標
     fa = face["faceAttributes"]  #取得臉部屬性
     origin = (fr["left"], fr["top"])
     p = patches.Rectangle(origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')  #畫出矩形
     ax.axes.add_patch(p)
     plt.text(origin[0], origin[1], "%s, %d"%(fa["gender"], fa["age"]), fontsize=20, weight="bold", va="bottom", color='r')  #顯示資訊
plt.axis("off")

print("------------------------------------------------------------")  # 60個

# ch26\faceVerify1.py

def getFaceId(image_url):  #取得臉部Id
    face_url = face_base_url + 'detect'
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age',
    }
    data    = {'url': image_url}
    response = requests.post(face_url, headers=headers, params=params, json=data)
    faces = response.json()
    return faces[0]['faceId']

def verifyFace(faceid1, faceid2):  #比對臉部是否相同
    face_url = face_base_url + 'verify'
    data    = {
        'faceId1': faceid1,
        'faceId2': faceid2,
    }
    response = requests.post(face_url, headers=headers, json=data)
    result = response.json()
    #print(result)
    if result['isIdentical']== True:  #臉部相同
        return '兩張相片為同一人！'
    else:  #臉部不同
        return '兩張相片為不同人！'  

import requests

subscription_key = "你的人臉資源key"
face_base_url = "https://southeastasia.api.cognitive.microsoft.com/face/v1.0/"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

jengid1 = getFaceId("https://i.imgur.com/JKKvMiP.jpg")  #jeng照片一
jengid2 = getFaceId("https://i.imgur.com/dtusSZ1.jpg")  #jeng照片二
davidid1 = getFaceId("https://i.imgur.com/o4boWWG.jpg")  #david照片
print('傳入相同人員的不同照片：' + verifyFace(jengid1, jengid2))
print('\n傳入不同人員的照片：' + verifyFace(jengid1, davidid1))

print("------------------------------------------------------------")  # 60個

# ch26\imgAnalyze1.py

import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源key"
vision_base_url = "https://southeastasia.api.cognitive.microsoft.com/vision/v2.0/"
analyze_url = vision_base_url + "analyze"
image_url = "https://i.imgur.com/BO7tlY7.jpg"
headers = {'Ocp-Apim-Subscription-Key': subscription_key }
params  = {'visualFeatures': 'Categories,Description,Color'}
data    = {'url': image_url}
response = requests.post(analyze_url, headers=headers, params=params, json=data)
analysis = response.json()
#print(analysis)

#顯示圖片及圖片描述
image_caption = analysis["description"]["captions"][0]["text"]  #取得圖片描述
image = Image.open(BytesIO(requests.get(image_url).content))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)  #顯示圖片描述

print("------------------------------------------------------------")  # 60個

# ch26\imgAnalyze2.py

import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源key"
vision_base_url = "https://southeastasia.api.cognitive.microsoft.com/vision/v2.0/"
analyze_url = vision_base_url + "analyze"
image_path = "street.jpg"  #本機圖片檔路徑
image_data = open(image_path, "rb").read()  #讀取圖片檔
headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
analysis = response.json()
#print(analysis)

#顯示圖片及圖片描述
image_caption = analysis["description"]["captions"][0]["text"]
image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)

print("------------------------------------------------------------")  # 60個

# ch26\landmark1.py

import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源key"
vision_base_url = "https://southeastasia.api.cognitive.microsoft.com/vision/v2.0/"
landmark_analyze_url = vision_base_url + "models/landmarks/analyze"
image_url = "https://i.imgur.com/WNlkY79.jpg"  #台北101
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'model': 'landmarks'}
data    = {'url': image_url}
response = requests.post(landmark_analyze_url, headers=headers, params=params, json=data)
analysis = response.json()
#print(analysis)

if len(analysis["result"]["landmarks"]) > 0:  #如果有地標
    landmark_name = analysis["result"]["landmarks"][0]["name"]  #取得地標名稱
    image = Image.open(BytesIO(requests.get(image_url).content))
    plt.imshow(image)
    plt.axis("off")
    _ = plt.title(landmark_name, size="x-large", y=-0.1)
else:  #未傳回地標
    print("無法辨識地標")
    

print("------------------------------------------------------------")  # 60個

# ch26\landmark2.py

import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源key"
vision_base_url = "https://southeastasia.api.cognitive.microsoft.com/vision/v2.0/"
landmark_analyze_url = vision_base_url + "models/landmarks/analyze"
image_url = "https://i.imgur.com/sx3xwOq.jpg"  #歐巴馬
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'model': 'celebrities'}
data    = {'url': image_url}
response = requests.post(landmark_analyze_url, headers=headers, params=params, json=data)
analysis = response.json()
#print(analysis)

if len(analysis["result"]["celebrities"]) > 0:  #如果有名人
    landmark_name = analysis["result"]["celebrities"][0]["name"]  #取得名人資訊
    image = Image.open(BytesIO(requests.get(image_url).content))
    plt.imshow(image)
    plt.axis("off")
    _ = plt.title(landmark_name, size="x-large", y=-0.1)
else:  #未傳回地標
    print("無法辨識地標")
    

print("------------------------------------------------------------")  # 60個

# ch26\language1.py

import requests

subscription_key = "你的翻譯文字資源key"
trans_base_url = "https://api.cognitive.microsofttranslator.com/"
trans_url = trans_base_url + 'detect?api-version=3.0'
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
while True:
    textinput = input('輸入文句 (直接按 Enter 鍵就結束程式)：')
    if textinput != '':
        data    = [{'text' : textinput}]
        response = requests.post(trans_url, headers=headers, json=data)
        result = response.json()
        print('輸入文句語言：' + result[0]['language'])
        #print(result)
    else:
        break

print("------------------------------------------------------------")  # 60個

# ch26\ocr1.py

import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源key"  #資源key
vision_base_url = "https://southeastasia.api.cognitive.microsoft.com/vision/v2.0/"  #資源端點
ocr_url = vision_base_url + "ocr"  #功能為ocr
image_url = "https://i.imgur.com/ptMvd6w.png"  #遠端圖片
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'language': 'unk', 'detectOrientation': 'true'}  #自動偵測文字類別及方向
data    = {'url': image_url}
response = requests.post(ocr_url, headers=headers, params=params, json=data)
analysis = response.json()
#print(analysis)  #列印結果

#line_infos串列儲存所有文字的坐標
line_infos = []
for region in analysis["regions"]:
    line_infos.append(region["lines"])
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)
#框選所有文字
plt.figure(figsize=(12, 12))
image = Image.open(BytesIO(requests.get(image_url).content))
ax = plt.imshow(image, alpha=0.5)
for word in word_infos:
    bbox = [int(num) for num in word["boundingBox"].split(",")]
    #text = word["text"]
    origin = (bbox[0], bbox[1])
    patch  = Rectangle(origin, bbox[2], bbox[3], fill=False, linewidth=2, color='r')
    ax.axes.add_patch(patch)
plt.axis("off")  #隱藏坐標軸

print("------------------------------------------------------------")  # 60個

# ch26\ocr2.py

import requests
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from PIL import Image
from io import BytesIO

subscription_key = "你的電腦視覺資源key"
vision_base_url = "https://southeastasia.api.cognitive.microsoft.com/vision/v2.0/"
text_recognition_url = vision_base_url + "read/core/asyncBatchAnalyze"
image_url = "https://i.imgur.com/VYLTAUV.jpg"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'mode': 'Handwritten'}
data    = {'url': image_url}
response = requests.post(text_recognition_url, headers=headers, params=params, json=data)

analysis = {}
flag = True  #記錄是否辨識完成,False為辨識完成
while (flag):
    response_final = requests.get(response.headers["Operation-Location"], headers=headers)
    analysis = response_final.json()  #取得回傳值
    #print(analysis)  #顯示回傳值
    if ("recognitionResults" in analysis): flag= False  #回傳值有「recognitionResults」表示完成
    if ("status" in analysis and analysis['status'] == 'Failed'): flag= False  #辨識失敗
    time.sleep(1)  #辨識需時間,每1秒讀一次回傳值

polygons=[]  #取得每列坐標
if ("recognitionResults" in analysis):
    polygons = []
    for line in analysis["recognitionResults"][0]["lines"]:
        polygons.append((line["boundingBox"], line["text"]))

#框選及列印每列文字
plt.figure(figsize=(12, 12))
image = Image.open(BytesIO(requests.get(image_url).content))
ax = plt.imshow(image)
for polygon in polygons:
    vertices = []
    for i in range(0, len(polygon[0]), 2):
        vertices.append((polygon[0][i], polygon[0][i+1]))
    text = polygon[1]  #取得文字
    patch = Polygon(vertices, closed=True, fill=False, linewidth=2, color='r')
    ax.axes.add_patch(patch)
    plt.text(vertices[0][0], vertices[0][1], text, fontsize=20, va="top", color='b')  #列印文字
plt.axis("off")

print("------------------------------------------------------------")  # 60個

# ch26\translate1.py

import requests

subscription_key = "你的翻譯文字資源key"
trans_base_url = "https://api.cognitive.microsofttranslator.com/"
trans_url = trans_base_url + 'translate?api-version=3.0'
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = '&to=en'  #翻譯為英文
while True:
    textinput = input('輸入文句 (直接按 Enter 鍵就結束程式)：')
    if textinput != '':
        data    = [{'text' : textinput}]
        response = requests.post(trans_url, headers=headers, params=params, json=data)
        result = response.json()
        print('翻譯結果：' + result[0]['translations'][0]['text'])
        #print(result)
    else:
        break

print("------------------------------------------------------------")  # 60個

# ch28\Led_Blink.py

from machine import Pin
import time 
 
# DPIO16對應到D0 
led = Pin(16, Pin.OUT)
 
while True:
    led.value(1)   #燈亮
    time.sleep(0.5)#暫停 0.5 秒

    led.value(0)   #燈熄
    time.sleep(0.5)#暫停 0.5 秒
    print("Hello")

print("------------------------------------------------------------")  # 60個

# ch28\main.py

from machine import Pin
import time 
 
# DPIO2對應到D4 
led = Pin(2, Pin.OUT) #D4 內建 Led
 
while True:
    led.value(1)   #燈熄
    time.sleep(0.5)#暫停 0.5 秒

    led.value(0)   #燈亮
    time.sleep(0.5)#暫停 0.5 秒
    print("Hello")

print("------------------------------------------------------------")  # 60個

# ch29\adc_pwm.py

from machine import Pin,ADC,PWM
import time

led = PWM(Pin(2), freq=1000) #DPIO2對應到D4
a0 = ADC(0) 

while True:
  value = a0.read() #讀取A0埠
  print(value)      #顯示轉換後的數值
  led.duty(value)   #亮度
  time.sleep(0.1) 

print("------------------------------------------------------------")  # 60個

# ch29\button.py

from machine import Pin
from time import sleep
 
# DPIO2對應到D4 
ledB = Pin(2, Pin.OUT)  #D4 內建 Led
button = Pin(0, Pin.IN) #GPIO0--D3

while True:
    if button.value()==0: #按下按鈕，燈亮
        ledB.value(0)
    else:  #放開按鈕，燈熄
        ledB.value(1)
    print(button.value())
    sleep(.1)    

print("------------------------------------------------------------")  # 60個

# ch29\buzzer.py

from machine import Pin, PWM
import time

buzzer = PWM(Pin(14, Pin.OUT), duty=900) # D5

def sound(): 
    buzzer.freq(400)
    time.sleep(0.5)
    buzzer.freq(700)
    time.sleep(0.5)

try:
    for i in range(5):
        sound()
    buzzer.deinit()
except:  # CTRL + C 中斷
    buzzer.deinit()
        

print("------------------------------------------------------------")  # 60個

# ch29\led_turn.py

from machine import Pin
import time 

def show_led(led):
    led.value(1)    #燈亮
    time.sleep(0.5) # 停0.5秒
    led.value(0)    #燈熄
 
# GPIO16對應到D0，DPIO14對應到D5，GPIO12對應到D6 
ledR = Pin(16, Pin.OUT)  #D0 紅燈
ledG = Pin(14, Pin.OUT)  #D5 綠燈
ledB = Pin(12, Pin.OUT)  #D6 藍燈
 
while True:
    show_led(ledR) # 紅燈亮
    show_led(ledG) # 綠燈亮
    show_led(ledB) # 藍燈亮
    print("R,G,B")

print("------------------------------------------------------------")  # 60個

# ch29\light_sensor.py

from machine import Pin,ADC
import time

led = Pin(2, Pin.OUT) #DPIO2對應到D4
a0 = ADC(0) 

while True:
  value = a0.read() #讀取A0埠
  print(value)      #顯示轉換後的數值
  if value<600:
      led.value(0)  #開燈
  else:
      led.value(1)  #關燈
  time.sleep(0.1) 

print("------------------------------------------------------------")  # 60個

# ch29\music.py

from machine import Pin, PWM
import time

pitches = {
    'C':261, # D0
    'D':294, # Re
    'E':329, # Mi
    'F':349, # Fa
    'G':392, # So
    'A':440, # La
    'B':493, # Si
    'S':0    # Stop
}

music = (
    ('C',1),('C',1),('G',1),('G',1),('A',1),('A',1),('G',2),
    ('F',1),('F',1),('E',1),('E',1),('D',1),('D',1),('C',2),
    ('G',1),('G',1),('F',1),('F',1),('E',1),('E',1),('D',2),
    ('G',1),('G',1),('F',1),('F',1),('E',1),('E',1),('D',2),
    ('C',1),('C',1),('G',1),('G',1),('A',1),('A',1),('G',2),
    ('F',1),('F',1),('E',1),('E',1),('D',1),('D',1),('C',1)
)

speed=400 # 設定節拍速度
period=10 # 設定每拍停頓時間

buzzer = PWM(Pin(14, Pin.OUT), duty=1000) # D5
try:
    for tone,tempo in music:
        if (tone=="S"):
            buzzer.duty(0) # 靜音
        else:
            buzzer.duty(1000)
            buzzer.freq(pitches[tone])
        time.sleep_ms(tempo*speed)
        print(pitches[tone])
        #以靜音設定每拍間稍為停頓
        buzzer.duty(0)         # 靜音
        time.sleep_ms(period)  # 停頓時間
    buzzer.deinit()
except:  # CTRL + C 中斷
    buzzer.deinit()       

print("------------------------------------------------------------")  # 60個

# ch29\neon.py

from machine import Pin,PWM
import time
import random
 
pwmR = PWM(Pin(13),freq=1000) #D7 紅燈
pwmG = PWM(Pin(14),freq=1000) #D5 綠燈
pwmB = PWM(Pin(12),freq=1000) #D6 藍燈

while True:
    R= random.randint(0,1023) # 產生 0~1023 的亂數
    G= random.randint(0,1023) # 產生 0~1023 的亂數
    B= random.randint(0,1023) # 產生 0~1023 的亂數

    pwmR.duty(R)
    time.sleep(0.1)
    pwmG.duty(G)
    time.sleep(0.1)
    pwmB.duty(B)
    time.sleep(0.1)    
    print(R,G,B)



print("------------------------------------------------------------")  # 60個

# ch29\pwm.py

from machine import Pin, PWM
import time
 
led = PWM(Pin(2),freq=1000) # DPIO2對應到D4 

while True:
    for n in range(1023,-1,-1): #燈漸亮
        led.duty(n)
        time.sleep_ms(5)
    for n in range(1024):      #燈漸熄
        led.duty(n)
        time.sleep_ms(5)
    print("change")

print("------------------------------------------------------------")  # 60個

# ch29\random.py

### Start of file: random.py ###
import os

def getrandbits(k):
    numbytes = (k + 7) // 8
    x = int.from_bytes(os.urandom(numbytes), 'big')
    return x >> (numbytes * 8 - k)

def bit_length(n):
    res = n
    count = 1
    while res>1:
        res = res>>1
        count = count+1
    return count

def randbelow(n):
    k = bit_length(n)
    r = getrandbits(k)
    while r >= n:
        r = getrandbits(k)
    return r

def randrange(start, stop=None, step=1):
    istart = int(start)
    if istart != start:
        raise ValueError("non-integer arg 1 for randrange()")
    if stop is None:
        if istart > 0:
            return randbelow(istart)
        raise ValueError("empty range for randrange()")

    # stop argument supplied.
    istop = int(stop)
    if istop != stop:
        raise ValueError("non-integer stop for randrange()")
    width = istop - istart
    if step == 1 and width > 0:
        return istart + randbelow(width)
    if step == 1:
        raise ValueError("empty range for randrange() (%d,%d, %d)" % (istart, istop, width))

    # Non-unit step argument supplied.
    istep = int(step)
    if istep != step:
        raise ValueError("non-integer step for randrange()")
    if istep > 0:
        n = (width + istep - 1) // istep
    elif istep < 0:
        n = (width + istep + 1) // istep
    else:
        raise ValueError("zero step for randrange()")

    if n <= 0:
        raise ValueError("empty range for randrange()")

    return istart + istep*randbelow(n)

def randint(a, b):
    return randrange(a, b+1)
### End of file random.py ###

print("------------------------------------------------------------")  # 60個

# ch30\dht11.py

from machine import Pin,Timer
import dht,time     

temp,hum=0,0
d = dht.DHT11(Pin(0)) #在D3建立DHT11物件
led = Pin(2, Pin.OUT) #D4內建Led

def readdht(t):
    global temp,hum
    try:
        d.measure()  #重新測量溫溼度
        temp=d.temperature()       #讀取攝氏溫度
        hum=d.humidity()           #讀取相對溼度
        print("溫    度: %3.1f °C" % temp)
        print("相對溼度: %3.1f %% RH" % hum)
    except:
        print('讀取不正常!')  

timer = Timer(1)
timer.init(period=2000, mode=Timer.PERIODIC, callback=readdht)

try:
    while True:
        if temp>24: # 溫度>24度，開燈
            led.value(0)
        else: # 溫度<24度，熄燈
            led.value(1)
        time.sleep(0.1) #暫停 0.1 秒
except:
    timer.deinit()
    print('stopped')  

print("------------------------------------------------------------")  # 60個

# ch30\HCSR04.py

from machine import Pin
import machine,time

echoTimeout = 23200 #等待截止時間
trigPin = Pin(13, mode=Pin.OUT) #觸發腳位 D7
echoPin = Pin(15, mode=Pin.IN)  #回應腳位 D8
trigPin.value(0)

def distance():
    trigPin.value(1) # 送出 10 us 的觸發訊號
    time.sleep_us(10)
    trigPin.value(0)
    # 計算高電位脈衝的時間
    pulseTime = machine.time_pulse_us(echoPin, 1, echoTimeout)
    if pulseTime > 0:
        return pulseTime / 58  # 公分換算
    else:
        return pulseTime  # 傳回 -1或-2

while True:
    cm = distance()
    if cm > 0:
        print('距離:%5.1f 公分' % cm)        
    else:
        print('讀取異常!')        
    time.sleep(1)  
    

print("------------------------------------------------------------")  # 60個

# ch30\timer01.py

from machine import Pin,Timer
import time 

led = Pin(2, Pin.OUT) # DPIO2(D4)內建Led

def show(t):
    toggle=not led.value()    
    led.value(toggle)   #燈閃爍           

timer = Timer(1)
timer.init(period=500, mode=Timer.PERIODIC, callback=show)

try:
    while True:
        for n in range(100):
            print(n)
            time.sleep(0.1)
except:
    timer.deinit()
    print('stopped')

print("------------------------------------------------------------")  # 60個

# ch30\timer02.py

from machine import Pin,Timer
import time 

led = Pin(2, Pin.OUT) # DPIO2(D4)內建Led
timer = Timer(1)
counter=0

def show(t):
    global counter
    counter+=1
    led.value(not led.value())   #燈閃爍
    if counter==10:
        t.deinit()    

timer.init(period=500, mode=Timer.PERIODIC, callback=show)    

try:
    while True:
        pass
except:
    timer.deinit()
    print('stopped')

print("------------------------------------------------------------")  # 60個

# ch31\esp8266_i2c_lcd.py

"""Implements a HD44780 character LCD connected via PCF8574 on I2C.
   This was tested with: https://www.wemos.cc/product/d1-mini.html"""

from lcd_api import LcdApi
from machine import I2C
from time import sleep_ms

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

# Defines shifts or masks for the various LCD line attached to the PCF8574

MASK_RS = 0x01
MASK_RW = 0x02
MASK_E = 0x04
SHIFT_BACKLIGHT = 3
SHIFT_DATA = 4


class I2cLcd(LcdApi):
    """Implements a HD44780 character LCD connected via PCF8574 on I2C."""

    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.i2c.writeto(self.i2c_addr, bytearray([0]))
        sleep_ms(20)   # Allow LCD time to powerup
        # Send reset 3 times
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        sleep_ms(5)    # need to delay at least 4.1 msec
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        sleep_ms(1)
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        sleep_ms(1)
        # Put LCD into 4 bit mode
        self.hal_write_init_nibble(self.LCD_FUNCTION)
        sleep_ms(1)
        LcdApi.__init__(self, num_lines, num_columns)
        cmd = self.LCD_FUNCTION
        if num_lines > 1:
            cmd |= self.LCD_FUNCTION_2LINES
        self.hal_write_command(cmd)

    def hal_write_init_nibble(self, nibble):
        """Writes an initialization nibble to the LCD.

        This particular function is only used during initialization.
        """
        byte = ((nibble >> 4) & 0x0f) << SHIFT_DATA
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))

    def hal_backlight_on(self):
        """Allows the hal layer to turn the backlight on."""
        self.i2c.writeto(self.i2c_addr, bytearray([1 << SHIFT_BACKLIGHT]))

    def hal_backlight_off(self):
        """Allows the hal layer to turn the backlight off."""
        self.i2c.writeto(self.i2c_addr, bytearray([0]))

    def hal_write_command(self, cmd):
        """Writes a command to the LCD.

        Data is latched on the falling edge of E.
        """
        byte = ((self.backlight << SHIFT_BACKLIGHT) | (((cmd >> 4) & 0x0f) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))
        byte = ((self.backlight << SHIFT_BACKLIGHT) | ((cmd & 0x0f) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))
        if cmd <= 3:
            # The home and clear commands require a worst case delay of 4.1 msec
            sleep_ms(5)

    def hal_write_data(self, data):
        """Write data to the LCD."""
        byte = (MASK_RS | (self.backlight << SHIFT_BACKLIGHT) | (((data >> 4) & 0x0f) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))
        byte = (MASK_RS | (self.backlight << SHIFT_BACKLIGHT) | ((data & 0x0f) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))

print("------------------------------------------------------------")  # 60個

# ch31\i2cscan.py

from machine import Pin,I2C
i2c = I2C(scl=Pin(13), sda=Pin(12), freq=100000)
print(i2c.scan())


print("------------------------------------------------------------")  # 60個

# ch31\lcd_api.py

"""Provides an API for talking to HD44780 compatible character LCDs."""

import time

class LcdApi:
    """Implements the API for talking with HD44780 compatible character LCDs.
    This class only knows what commands to send to the LCD, and not how to get
    them to the LCD.

    It is expected that a derived class will implement the hal_xxx functions.
    """

    # The following constant names were lifted from the avrlib lcd.h
    # header file, however, I changed the definitions from bit numbers
    # to bit masks.
    #
    # HD44780 LCD controller command set

    LCD_CLR = 0x01              # DB0: clear display
    LCD_HOME = 0x02             # DB1: return to home position

    LCD_ENTRY_MODE = 0x04       # DB2: set entry mode
    LCD_ENTRY_INC = 0x02        # --DB1: increment
    LCD_ENTRY_SHIFT = 0x01      # --DB0: shift

    LCD_ON_CTRL = 0x08          # DB3: turn lcd/cursor on
    LCD_ON_DISPLAY = 0x04       # --DB2: turn display on
    LCD_ON_CURSOR = 0x02        # --DB1: turn cursor on
    LCD_ON_BLINK = 0x01         # --DB0: blinking cursor

    LCD_MOVE = 0x10             # DB4: move cursor/display
    LCD_MOVE_DISP = 0x08        # --DB3: move display (0-> move cursor)
    LCD_MOVE_RIGHT = 0x04       # --DB2: move right (0-> left)

    LCD_FUNCTION = 0x20         # DB5: function set
    LCD_FUNCTION_8BIT = 0x10    # --DB4: set 8BIT mode (0->4BIT mode)
    LCD_FUNCTION_2LINES = 0x08  # --DB3: two lines (0->one line)
    LCD_FUNCTION_10DOTS = 0x04  # --DB2: 5x10 font (0->5x7 font)
    LCD_FUNCTION_RESET = 0x30   # See "Initializing by Instruction" section

    LCD_CGRAM = 0x40            # DB6: set CG RAM address
    LCD_DDRAM = 0x80            # DB7: set DD RAM address

    LCD_RS_CMD = 0
    LCD_RS_DATA = 1

    LCD_RW_WRITE = 0
    LCD_RW_READ = 1

    def __init__(self, num_lines, num_columns):
        self.num_lines = num_lines
        if self.num_lines > 4:
            self.num_lines = 4
        self.num_columns = num_columns
        if self.num_columns > 40:
            self.num_columns = 40
        self.cursor_x = 0
        self.cursor_y = 0
        self.backlight = True
        self.display_off()
        self.backlight_on()
        self.clear()
        self.hal_write_command(self.LCD_ENTRY_MODE | self.LCD_ENTRY_INC)
        self.hide_cursor()
        self.display_on()

    def clear(self):
        """Clears the LCD display and moves the cursor to the top left
        corner.
        """
        self.hal_write_command(self.LCD_CLR)
        self.hal_write_command(self.LCD_HOME)
        self.cursor_x = 0
        self.cursor_y = 0

    def show_cursor(self):
        """Causes the cursor to be made visible."""
        self.hal_write_command(self.LCD_ON_CTRL | self.LCD_ON_DISPLAY |
                               self.LCD_ON_CURSOR)

    def hide_cursor(self):
        """Causes the cursor to be hidden."""
        self.hal_write_command(self.LCD_ON_CTRL | self.LCD_ON_DISPLAY)

    def blink_cursor_on(self):
        """Turns on the cursor, and makes it blink."""
        self.hal_write_command(self.LCD_ON_CTRL | self.LCD_ON_DISPLAY |
                               self.LCD_ON_CURSOR | self.LCD_ON_BLINK)

    def blink_cursor_off(self):
        """Turns on the cursor, and makes it no blink (i.e. be solid)."""
        self.hal_write_command(self.LCD_ON_CTRL | self.LCD_ON_DISPLAY |
                               self.LCD_ON_CURSOR)

    def display_on(self):
        """Turns on (i.e. unblanks) the LCD."""
        self.hal_write_command(self.LCD_ON_CTRL | self.LCD_ON_DISPLAY)

    def display_off(self):
        """Turns off (i.e. blanks) the LCD."""
        self.hal_write_command(self.LCD_ON_CTRL)

    def backlight_on(self):
        """Turns the backlight on.

        This isn't really an LCD command, but some modules have backlight
        controls, so this allows the hal to pass through the command.
        """
        self.backlight = True
        self.hal_backlight_on()

    def backlight_off(self):
        """Turns the backlight off.

        This isn't really an LCD command, but some modules have backlight
        controls, so this allows the hal to pass through the command.
        """
        self.backlight = False
        self.hal_backlight_off()

    def move_to(self, cursor_x, cursor_y):
        """Moves the cursor position to the indicated position. The cursor
        position is zero based (i.e. cursor_x == 0 indicates first column).
        """
        self.cursor_x = cursor_x
        self.cursor_y = cursor_y
        addr = cursor_x & 0x3f
        if cursor_y & 1:
            addr += 0x40    # Lines 1 & 3 add 0x40
        if cursor_y & 2:
            addr += 0x14    # Lines 2 & 3 add 0x14
        self.hal_write_command(self.LCD_DDRAM | addr)

    def putchar(self, char):
        """Writes the indicated character to the LCD at the current cursor
        position, and advances the cursor by one position.
        """
        if char != '\n':
            self.hal_write_data(ord(char))
            self.cursor_x += 1
        if self.cursor_x >= self.num_columns or char == '\n':
            self.cursor_x = 0
            self.cursor_y += 1
            if self.cursor_y >= self.num_lines:
                self.cursor_y = 0
            self.move_to(self.cursor_x, self.cursor_y)

    def putstr(self, string):
        """Write the indicated string to the LCD at the current cursor
        position and advances the cursor position appropriately.
        """
        for char in string:
            self.putchar(char)

    def custom_char(self, location, charmap):
        """Write a character to one of the 8 CGRAM locations, available
        as chr(0) through chr(7).
        """
        location &= 0x7
        self.hal_write_command(self.LCD_CGRAM | (location << 3))
        self.hal_sleep_us(40)
        for i in range(8):
            self.hal_write_data(charmap[i])
            self.hal_sleep_us(40)
        self.move_to(self.cursor_x, self.cursor_y)

    def hal_backlight_on(self):
        """Allows the hal layer to turn the backlight on.

        If desired, a derived HAL class will implement this function.
        """
        pass

    def hal_backlight_off(self):
        """Allows the hal layer to turn the backlight off.

        If desired, a derived HAL class will implement this function.
        """
        pass

    def hal_write_command(self, cmd):
        """Write a command to the LCD.

        It is expected that a derived HAL class will implement this
        function.
        """
        raise NotImplementedError

    def hal_write_data(self, data):
        """Write data to the LCD.

        It is expected that a derived HAL class will implement this
        function.
        """
        raise NotImplementedError

    def hal_sleep_us(self, usecs):
        """Sleep for some time (given in microseconds)."""
        time.sleep_us(usecs)

print("------------------------------------------------------------")  # 60個

# ch31\lcd01.py

from esp8266_i2c_lcd import I2cLcd
from machine import I2C,Pin

# GPIO 12-D6,GPIO 13-D7
i2c = I2C(scl=Pin(13), sda=Pin(12), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.clear()

lcd.move_to(0, 0)  #(0,0) 位置
lcd.putstr("Hello World!") 

print("------------------------------------------------------------")  # 60個

# ch31\lcd02.py

from esp8266_i2c_lcd import I2cLcd
from machine import I2C,Pin

# GPIO 12-D6,GPIO 13-D7
i2c = I2C(scl=Pin(13), sda=Pin(12), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.clear()

lcd.move_to(2, 0)  #(0,2) 位置
lcd.putstr("R=100")
lcd.putchar(chr(0xF4)) #Ω

lcd.move_to(2, 1)  #(1,2) 位置
lcd.putstr("T=25") 
lcd.putchar(chr(0xDF)) #°
lcd.putchar("C") #C

print("------------------------------------------------------------")  # 60個

# ch31\main.py

from esp8266_i2c_lcd import I2cLcd
from machine import I2C,Pin,ADC
from time import sleep

# GPIO 12-D6,GPIO 13-D7
DEFAULT_I2C_ADDR = 0x27 # 位址
A0 = ADC(0) # 讀取 A0 埠

i2c = I2C(scl=Pin(13), sda=Pin(12), freq=100000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
lcd.clear()

while True:
  A0_value = A0.read() #讀取A0埠
  print(A0_value)      #顯示轉換後的數值  

  lcd.move_to(0, 0)    #(0,0) 位置
  lcd.putstr("A0=" + str(A0_value)  + "   ") 
  sleep(0.5)

print("------------------------------------------------------------")  # 60個

# ch32\boot.py

# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc

# 連線基地台
SSID='自已的SSID'
PASSWORD='自已的密碼'
def do_connect():
    sta = network.WLAN(network.STA_IF) # Station
    if not sta.isconnected():
        print('正在連線中...')
        sta.active(True) #啟用 STA 模式
        sta.connect(SSID, PASSWORD) #連線基地台
        # 等侯連線
        while not sta.isconnected():
            pass
    print('連線成功!')
    #print(sta.ifconfig()) # 顯示網址、網路遮罩、閘道器和 DNS

#import webrepl
#webrepl.start()
gc.collect()

print("------------------------------------------------------------")  # 60個

# ch32\eHappy.py

import urequests
import network
import time

SSID='自己的SSID'
PASSWORD='自己的密碼'
def do_connect():
    sta = network.WLAN(network.STA_IF) # Station
    if not sta.isconnected():
        print('正在連線中...')
        sta.active(True) #啟用 STA 模式
        sta.connect(SSID, PASSWORD) #連線基地台
        # 等侯連線
        while not sta.isconnected():
            pass
    print('連線成功!')
    #print(sta.ifconfig()) # 顯示網址、網路遮罩、閘道器和 DNS
              
do_connect() # 連線基地台
r=urequests.get("http://www.e-happy.com.tw")
r.encoding='utf-8'
time.sleep(3)
print("下載完畢!")
if (r.status_code==200):
    print(r.raw.read(100))

print("------------------------------------------------------------")  # 60個

# ch32\http_request.py

import network
import socket

SSID='自己的SSID'
PASSWORD='自己的密碼'
def do_connect():
    sta = network.WLAN(network.STA_IF) # Station
    if not sta.isconnected():
        print('正在連線中...')
        sta.active(True) #啟用 STA 模式
        sta.connect(SSID, PASSWORD) #連線基地台
        # 等侯連線
        while not sta.isconnected():
            pass
    print('連線成功!')
              
do_connect() # 連線基地台

httpRequest = b'''\
GET /{path} HTTP/1.1
Host:{host}
User-Agent: D1-mini

'''

url = 'http://micropython.org/ks/test.html'
_, _, host, path = url.split('/', 3)
addr = socket.getaddrinfo(host, 80)[0][-1]
s = socket.socket()
s.connect(addr)
s.send(httpRequest.format(path=path, host=host))

while True:
    data = s.recv(128) #接收訊息
    if data:
        print(data.decode('utf8'), end='')
    else:
        break

s.close()

print("------------------------------------------------------------")  # 60個

# ch32\https_request.py

import network
import socket
import ussl

SSID='自己的SSID'
PASSWORD='自己的密碼'
def do_connect():
    sta = network.WLAN(network.STA_IF) # Station
    if not sta.isconnected():
        print('正在連線中...')
        sta.active(True) #啟用 STA 模式
        sta.connect(SSID, PASSWORD) #連線基地台
        # 等侯連線
        while not sta.isconnected():
            pass
    print('連線成功!')
              
do_connect() # Connect to network

httpRequest = b'''\
GET /{path} HTTP/1.0
Host:{host}
User-Agent: D1-mini

'''

url = 'https://micropython.org/ks/test.html'
_, _, host, path = url.split('/', 3)
addr = socket.getaddrinfo(host, 443)[0][-1] #埠號 443
s = socket.socket()
s.connect(addr)
s = ussl.wrap_socket(s) #加密
s.write(httpRequest.format(path=path, host=host)) #傳送加密訊息

while True:
    data = s.read(128) #接收訊息
    if data:
        print(data.decode('utf8'), end='')
    else:
        break
s.close()

print("------------------------------------------------------------")  # 60個

# ch32\main.py

import urequests # 不可使用 requests
import time

r=urequests.get("http://www.e-happy.com.tw")
r.encoding='utf-8'
time.sleep(3)
print("下載完畢!")
if (r.status_code==200):
    print(r.raw.read(100))


print("------------------------------------------------------------")  # 60個

# ch32\Station.py

import network

SSID='自己的SSID'
PASSWORD='自己的密碼'
sta = network.WLAN(network.STA_IF)

if not sta.isconnected():
    print('正在連線中...')
    sta.active(True) #啟用 STA 模式
    sta.connect(SSID, PASSWORD) #連線基地台
    # 等侯連線
    while not sta.isconnected():
        pass
print('連線成功!')
print(sta.ifconfig()) # 顯示網址、網路遮罩、閘道器和 DNS

print("------------------------------------------------------------")  # 60個

# ch33\Server_ReadA0.py

from machine import ADC
import network
import socket

SSID='自己的SSID'
PASSWORD='自己的密碼'
HOST = '0.0.0.0'
PORT = 80
def do_connect():
    global HOST
    sta = network.WLAN(network.STA_IF) # Station
    if not sta.isconnected():
        print('正在連線中...')
        sta.active(True) #啟用 STA 模式
        sta.connect(SSID, PASSWORD) #連線基地台
        # 等侯連線
        while not sta.isconnected():
            pass
    print('連線成功!')
    HOST = sta.ifconfig()[0]
              
do_connect() # 連線基地台

httpResponse = b"""\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>D1 mini Server</title>
</head>
<body>
  光線強度: {value}<br>
</body>
</html>
"""

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)
print('{} 伺服器在 {} 埠建立！'.format(HOST, PORT))

A0 = ADC(0)

while True:
    client, addr = s.accept()
    value = A0.read() # 讀取 A0
    print("光線強度:{}" .format(value))
    client.send(httpResponse.format(value=value))    
    client.close()
    print()

print("------------------------------------------------------------")  # 60個

# ch33\webserver.py

import network
import socket

SSID='自己的SSID'
PASSWORD='自己的密碼'
HOST = '0.0.0.0'
PORT = 80
def do_connect():
    global HOST
    sta = network.WLAN(network.STA_IF) # Station
    if not sta.isconnected():
        print('正在連線中...')
        sta.active(True) #啟用 STA 模式
        sta.connect(SSID, PASSWORD) #連線基地台
        # 等侯連線
        while not sta.isconnected():
            pass
    print('連線成功!')
    HOST = sta.ifconfig()[0]
              
do_connect() # 連線基地台

httpResponse = b"""\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
    <head >
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>MicroPython</h1>
        歡迎光臨 D1 mini Server!
    </body>
</html>
"""

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(10)
print('{} 伺服器在 {} 埠建立！'.format(HOST, PORT))

while True:
    client, addr = s.accept()
    print("客戶端位址：", addr)
    
    req = client.recv(1024) #接收請求
    print("HTTP Request:")
    print(req)
    client.send(httpResponse) #回應請求
    client.close()
    print()

print("------------------------------------------------------------")  # 60個







print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
