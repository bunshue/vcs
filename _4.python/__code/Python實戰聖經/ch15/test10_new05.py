import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

print('barcode產生器')

#pip install python-barcode

import barcode
from barcode.writer import ImageWriter

print(barcode.PROVIDED_BARCODES)

EAN = barcode.get_barcode_class('ean13')

text = '123456789012'   #EAN僅能用數字, 必為12碼
#存svg檔
ean = EAN(text)
ean.save('ean13_barcode') 
#存png檔
ean = EAN(text, writer=ImageWriter())
ean.save('ean13_barcode')


print('------------------------------------------------------------')	#60個

print('qrcode：qrcode產生器')

import qrcode
import qrcode.image.svg

text = '港町十三番地'
#存png檔
img = qrcode.make(text)
img.save('my_qrcode.png')
#存svg檔
img = qrcode.make(text, image_factory=qrcode.image.svg.SvgPathImage)
img.save('my_qrcode.svg')


qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(text)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="blue")
img.save('my_qrcode2.png')


print('------------------------------------------------------------')	#60個

'''
print('schedule：定時執行任務')

import schedule


schedule.clear()

cnt = 0

def job():
    global cnt
    print('工作示範, ', cnt)
    cnt += 1
    if cnt == 10:
        print('結束工作')#尚有問題
        schedule.clear()
        #schedule.cancel_job()


schedule.every(3).seconds.do(job)
# schedule.every(3).minutes.do(job)
# schedule.every(3).hours.do(job)
# schedule.every(3).days.do(job)
# schedule.every(3).weeks.do(job)

# schedule.every().minute.at(":43").do(job)
# schedule.every().hour.at(":53").do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().wednesday.at("13:15").do(job)

# schedule.every(5).to(10).seconds.do(job)  #每隔5至10秒執行一次,亂數決定

while True:
    schedule.run_pending()


print('kkkkkk')
'''

print('------------------------------------------------------------')	#60個

'''
print('tqdm：進度條')

from tqdm import tqdm 
from tqdm import trange 
from time import sleep

for i in tqdm(range(1000)): 
    sleep(0.01)

for i in trange(1000): 
    sleep(0.01)

tlist = tqdm(["a", "b", "c", "d"]) 
for char in tlist: 
    print(char)
    tlist.set_description("處理串列元素……")
    sleep(0.5)
'''    
print('------------------------------------------------------------')	#60個

#dist：經緯度距離
#pip install https://github.com/duboviy/dist/archive/master.zip

import dist

#台北火車站 25.047778, 121.517222
#新竹火車站 24.802050, 120.971817

x1 = 25.047778
y1 = 121.517222
x2 = 24.802050
y2 = 120.971817

print(dist.compute(25.0342, 121.5646, 24.9932, 121.3009))
print(dist.compute(x1, y1, x2, y2))


print('------------------------------------------------------------')	#60個

print('chardet：檔案編碼格式')

import chardet

files = ['test1.txt', 'test2.txt', 'googlecomment.csv']
for f in files:
    text = open(f, 'rb').read()
    codetype = chardet.detect(text)
    print('{} 編碼格式：{}'.format(f, codetype))
    
print('------------------------------------------------------------')	#60個

print('verifyid：驗證身分證字號')

from verifyid import verifyid

verify = verifyid.IdentyNumber()

veri = verify.check_identy_number("A189229579")
print('A189229579 驗證結果：{}'.format(veri))
veri = verify.check_identy_number("a189229579")
print('a189229579 驗證結果：{}'.format(veri))
veri = verify.check_identy_number("A123456780")
print('A123456780 驗證結果：{}'.format(veri))

city = verify.get_city("A189229579")
print('A189229579 城市：{}'.format(city))
city = verify.get_city("P123456789".upper())
print('P123456789 城市：{}'.format(city))


print('------------------------------------------------------------')	#60個

print('cnlunardate：農曆日期')

#pip install cnlunardate
from cnlunardate import cnlunardate
from datetime import date

year = 2023  #@param {type:'slider', min:1950, max:2020}
month = 2  #@param {type:'slider', min:1, max:12}
try:
    cnlunardate(year, month, 1, True)
    print('農曆 {} 年 {} 月「是」閏月。'.format(year, month))
except:
    print('農曆 {} 年 {} 月「不是」閏月。'.format(year, month))
    
print(cnlunardate.fromsolardate(date(1974, 9, 24))) 
print(cnlunardate.fromsolardate(date(2006, 3, 11))) 
print(cnlunardate.fromsolardate(date(2023, 9, 20)))


print(cnlunardate(2017, 9, 1).tosolardate())
print(cnlunardate(2017, 6, 10, True).tosolardate())
print(cnlunardate(2017, 6, 10, False).tosolardate())

print(cnlunardate(2017, 6, 1, False).toordinal())

n1 = cnlunardate(2017, 6, 1, False).toordinal()
n2 = cnlunardate(2015, 10, 12, False).toordinal()
print(n1 - n2)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



