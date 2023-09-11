import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import os

print('顯示資料夾內的特定格式的檔案')

def is_image(filename):
    f = filename.lower()
    return f.endswith('.png') or f.endswith('.jpg') or \
           f.endswith('.jpeg') or f.endswith('.bmp') or \
           f.endswith('.gif') or '.jpg' in f or f.endswith('.svg')


def find_similar_images(foldername):
    image_filenames = []
    image_filenames += [os.path.join(foldername, path) for path in os.listdir(foldername) if is_image(path)]
    for img in sorted(image_filenames):
        print(img)

foldername = 'C:/_git/vcs/_1.data/______test_files5'
find_similar_images(foldername)



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import keyword
print(keyword.kwlist)

import builtins
print(dir(builtins))

import time
print(time.time())

import time
print(time.localtime())

import time
year, month, day, hour, minute, second, _, _, _ = time.localtime()
print("{}-{}-{} {}:{}:{}".format(year, month, day, hour, minute, second))

import time
print(time.asctime())

import time
print(time.strftime("%Y-%m-%d %H:%M:%S %a"))

import datetime
#當前的日期及時間
print(datetime.datetime.now())

import datetime


today = datetime.datetime.today()
birthday = datetime.datetime(2018,10,27, 17, 0, 0)
print(today - birthday)

from datetime import datetime
now = datetime.now()
print("今天是{}".format(datetime.strftime(now, "%Y-%m-%d")))
date = input("請輸入一個日期（yyyy-mm-dd):")
target = datetime.strptime(date, "%Y-%m-%d")
diff = now-target
print("到今天共經過了{}天。".format(diff.days))


import calendar
print(calendar.month(2018,10))
print(calendar.calendar(2019))


import sys
print(sys.version_info)
print("---")
print(sys.platform)
print("---")
print(sys.argv)
print("---")
print(sys.path)




import os
items = os.listdir()
print(os.path.exists('myprime.py'))
for item in items:
    print(os.path.abspath(item))



import os
fullpath = os.path.abspath('myprime.py')
print(fullpath)
print("os.path.basename:", os.path.basename(fullpath))
print("os.path.dirname:", os.path.dirname(fullpath))
print("os.path.getatime:", os.path.getatime(fullpath))
print("os.path.getmtime:", os.path.getmtime(fullpath))
print("os.path.getctime:", os.path.getctime(fullpath))
print("os.path.getsize:", os.path.getsize(fullpath))
print("os.path.isabs:", os.path.isabs(fullpath))
print("os.path.isfile:", os.path.isfile(fullpath))
print("os.path.isdir:", os.path.isdir(fullpath))
print("os.path.split:", os.path.split(fullpath))
print("os.path.splitdrive:", os.path.splitdrive(fullpath))
print("os.path.splitext:", os.path.splitext(fullpath))




print('------------------------------------------------------------')	#60個

'''

python的日期當中分成
1. date(日期)
2. time(時間)
3. datetime(混合date跟time)
4. timedelta(計算歷時期間的型態)
5. timezone(處理時區資訊的型態)

'''

import datetime

#輸出當前的日期及時間

print(datetime.datetime.now())

print(datetime.datetime.today())

#而如果只想要輸出現在的日期的話則用
print(datetime.date.today())


#而如果要輸出此時準確的時間的話則

import time
print(time.localtime())

#而我們也可以一一拆解

tonow = datetime.datetime.now()
print(tonow.year)
print(tonow.month)
print(tonow.day)

#而我們也可以算今天是今年的第幾天

dts = '20201007'
dt = datetime.datetime.strptime(dts,"%Y%m%d")
another_dts = dts[:4]+"0101"
another_dt = datetime.datetime.strptime(another_dts,"%Y%m%d")
print(int((dt-another_dt).days)+1)


'''
由上可得知datetime.datetime.strptime()這個是將所輸入的dts轉換成日期的格式則格式為後面的年月日，再來取出輸入的西元年加上"0101"後一樣轉換成日期的格式最後將輸入日期減掉設定日期後+1輸出成今天為今年的第幾天
'''

loc_dt = datetime.datetime.today() 
time_del = datetime.timedelta(hours=3) 
new_dt = loc_dt + time_del 
datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
print(loc_dt_format)
print(datetime_format)


'''
由上可得知我們也可以調整時差，將我們現在的時間加上3小時的時差並將其輸出出來，一開始我們將抓出本地的時間並且將變數time_del宣告為時差差三個小時，最後將其相加就變成有時差三個小時最後將其指定格式後輸出，而以此類推我們也可以將時差晚三個小時
'''


loc_dt = datetime.datetime.today() 
time_del = datetime.timedelta(hours=3) 
new_dt = loc_dt - time_del 
datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
print(loc_dt_format)
print(datetime_format)













print('------------------------------------------------------------')	#60個

import codecs
import contextlib
import io
import locale
import sys
import unittest
import warnings
import encodings


all_unicode_encodings = [
    "ascii",
    "big5",
    "big5hkscs",
    "charmap",
    "cp037",
    "cp1006",
    "cp1026",
    "cp1125",
    "cp1140",
    "cp1250",
    "cp1251",
    "cp1252",
    "cp1253",
    "cp1254",
    "cp1255",
    "cp1256",
    "cp1257",
    "cp1258",
    "cp424",
    "cp437",
    "cp500",
    "cp720",
    "cp737",
    "cp775",
    "cp850",
    "cp852",
    "cp855",
    "cp856",
    "cp857",
    "cp858",
    "cp860",
    "cp861",
    "cp862",
    "cp863",
    "cp864",
    "cp865",
    "cp866",
    "cp869",
    "cp874",
    "cp875",
    "cp932",
    "cp949",
    "cp950",
    "euc_jis_2004",
    "euc_jisx0213",
    "euc_jp",
    "euc_kr",
    "gb18030",
    "gb2312",
    "gbk",
    "hp_roman8",
    "hz",
    "idna",
    "iso2022_jp",
    "iso2022_jp_1",
    "iso2022_jp_2",
    "iso2022_jp_2004",
    "iso2022_jp_3",
    "iso2022_jp_ext",
    "iso2022_kr",
    "iso8859_1",
    "iso8859_10",
    "iso8859_11",
    "iso8859_13",
    "iso8859_14",
    "iso8859_15",
    "iso8859_16",
    "iso8859_2",
    "iso8859_3",
    "iso8859_4",
    "iso8859_5",
    "iso8859_6",
    "iso8859_7",
    "iso8859_8",
    "iso8859_9",
    "johab",
    "koi8_r",
    "koi8_u",
    "latin_1",
    "mac_cyrillic",
    "mac_greek",
    "mac_iceland",
    "mac_latin2",
    "mac_roman",
    "mac_turkish",
    "palmos",
    "ptcp154",
    "punycode",
    "raw_unicode_escape",
    "shift_jis",
    "shift_jis_2004",
    "shift_jisx0213",
    "tis_620",
    "unicode_escape",
    "utf_16",
    "utf_16_be",
    "utf_16_le",
    "utf_7",
    "utf_8",
]

print(type(all_unicode_encodings))
    
for encoding in all_unicode_encodings:
    name = codecs.lookup(encoding).name
    print(name)

for encoding in all_unicode_encodings:
    reader = codecs.getreader(encoding)
    print(reader)

for encoding in all_unicode_encodings:
    decoder = codecs.getdecoder(encoding)

for encoding in all_unicode_encodings:
    encoder = codecs.getencoder(encoding)


ALL_CJKENCODINGS = [
# _codecs_cn
    'gb2312', 'gbk', 'gb18030', 'hz',
# _codecs_hk
    'big5hkscs',
# _codecs_jp
    'cp932', 'shift_jis', 'euc_jp', 'euc_jisx0213', 'shift_jisx0213',
    'euc_jis_2004', 'shift_jis_2004',
# _codecs_kr
    'cp949', 'euc_kr', 'johab',
# _codecs_tw
    'big5', 'cp950',
# _codecs_iso2022
    'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004',
    'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr',
]



for enc in ALL_CJKENCODINGS:
    code = '# coding: {}\n'.format(enc)
    print(code)


print('------------------------------------------------------------')	#60個


ticks = time.time() #至今的tick數
print(ticks)

localtime = time.localtime(ticks)   #傳回時間元組
print(type(localtime))
print(localtime)

print('年 :', localtime[0])
print('月 :', localtime[1])
print('日 :', localtime[2])
print('時 :', localtime[3])
print('分 :', localtime[4])
print('秒 :', localtime[5])

#asctime() #傳回時間元組的日期時間字串
formattime = time.asctime(time.localtime(ticks))
print(formattime)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



