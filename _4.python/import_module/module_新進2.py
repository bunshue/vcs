import sys
'''

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

"""
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
"""

print('------------------------------------------------------------')	#60個

"""
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
"""    
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


import math

r = 6371                        # 地球半徑
x1, y1 = 22.2838, 114.1731      # 香港紅磡車站經緯度
x2, y2 = 25.0452, 121.5168      # 台北車站經緯度

d = 6371*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+
                   math.cos(math.radians(x1))*math.cos(math.radians(x2))*
                   math.cos(math.radians(y1-y2)))

print("distance = ", d)



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

'''

print('------------------------------------------------------------')	#60個

print('chardet：檔案編碼格式')

import chardet

filename1 = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/_encoding/2.utf_to_ascii.txt'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/_encoding/3.ascii_to_unicode.txt'

files = [filename1, filename2, filename3]
for f in files:
    text = open(f, 'rb').read()
    codetype = chardet.detect(text)
    print('{} 編碼格式：{}'.format(f, codetype))




print('------------------------------------------------------------')	#60個

import nt
import collections

_ntuple_diskusage = collections.namedtuple('usage', 'total used free')

def disk_usage(path):
    total, free = nt._getdiskusage(path)
    used = total - free
    return _ntuple_diskusage(total, used, free)

foldername = 'C:/_git/vcs/'
du = disk_usage(foldername)
print(du)
print('容量 :', du.total, '個位元組\t', du.total//1024//1024//1024, 'GB')
print('已使用空間 :', du.used, '個位元組\t', du.used//1024//1024//1024, 'GB')
print('可用空間 :', du.free, '個位元組\t', du.free//1024//1024//1024, 'GB')

foldername = 'D:/'
du = disk_usage(foldername)
print(du)
print('容量 :', du.total, '個位元組\t', du.total//1024//1024//1024, 'GB')
print('已使用空間 :', du.used, '個位元組\t', du.used//1024//1024//1024, 'GB')
print('可用空間 :', du.free, '個位元組\t', du.free//1024//1024//1024, 'GB')

print('------------------------------------------------------------')	#60個


import time
import threading
import subprocess
from optparse import OptionParser, SUPPRESS_HELP

def bark(duration):

    _time = time.time
    _sleep = time.sleep
    
    # We give the parent some time to be ready.
    _sleep(1.0)

    start_time = _time()
    end_time = start_time + duration * 2.0
    i = 0
    while _time() < end_time:
        print('b', end = ' ')
        i += 1


bark(0.2)

print('------------------------------------------------------------')	#60個


