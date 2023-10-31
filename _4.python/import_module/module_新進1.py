
print('------------------------------------------------------------')	#60個
'''
import warnings
warnings.warn('Use importlib.util.find_spec() instead.', DeprecationWarning, stacklevel = 1)

print('建立一組密碼 並將此密碼拷貝至剪貼簿')
import random
import pyperclip
chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'
password = ''
for c in range(20):
   password += random.choice(chars)
print('建立一組密碼:\t%r, 並已拷貝至剪貼簿' %(password))
pyperclip.copy(password)

print('------------------------------------------------------------')	#60個

print('純文字檔的diff')

import difflib

filename1 = 'C:/_git/vcs/_1.data/______test_files1/compare/text_filea.txt'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/compare/text_fileb.txt'

def fcompare(f1name, f2name):
    print('-:', f1name)
    print('+:', f2name)
    f1 = open(f1name)
    f2 = open(f2name)
    if not f1 or not f2:
        return 0

    a = f1.readlines();
    f1.close()
    b = f2.readlines();
    f2.close()
    for line in difflib.ndiff(a, b):
        print(line, end=' ')

ret = fcompare(filename1, filename2)
print('\n\nresult : ', ret)

print('------------------------------------------------------------')	#60個

"""
import win32api, win32con
rc = win32api.MessageBox(0, 'kkkkk', "Installation Error", win32con.MB_ABORTRETRYIGNORE)
if rc == win32con.IDABORT:
    print('1111')
elif rc == win32con.IDIGNORE:
    print('2222')
else:
    print('3333')

"""

print('------------------------------------------------------------')	#60個

import abc
metaclass = abc.ABCMeta
print(metaclass)

print('------------------------------------------------------------')	#60個

import uuid
id = str(uuid.uuid4())
print(id)

import os, uuid
print("uuid = {}".format(str(uuid.uuid4())))

print('------------------------------------------------------------')	#60個

import socket
hostname = socket.gethostname()
print('取得 hostname :', hostname)

import os
import time
path = 'cccc'
print('%s.%s.%s.%s' % (path, int(time.time()),
                       socket.gethostname(),
                       os.getpid()))

print('------------------------------------------------------------')	#60個

import multiprocessing

print(multiprocessing.current_process().name)

print('------------------------------------------------------------')	#60個

from plyer import notification

print('notification 測試')

text = 'Welcome to the United States and have a nice day.'
msg = 'cccccc'
notification.notify(
    title = text,
    message = msg
    )


print('------------------------------------------------------------')	#60個

import keyword
print(keyword.kwlist)

import keyword

keywordLists = ['as', 'while', 'break', 'sse', 'Python']
for x in keywordLists:
    print(f"{x:>8s} {keyword.iskeyword(x)}")

print('------------------------------------------------------------')	#60個

import keyword

print(keyword.kwlist)

""" 檢測按鍵
import keyboard

while True:
    if keyboard.is_pressed('*'):
        print('KKKK')
        continue;
    if keyboard.is_pressed('/'):
        print('SSSS')
        continue;
"""

print('------------------------------------------------------------')	#60個

import locale

print(locale.getpreferredencoding())

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

"""
排序字典
"""
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])




print('------------------------------------------------------------')	#60個

def bin_octal():
    x = 65535
    print(type(bin(x)))
    print(bin(x), oct(x), hex(x))

    # format() function
    print(format(x, 'b'))
    print(format(x, 'o'))
    print(format(x, 'x'))

    print(int('ffff', 16))
    print(int('10011010010', 2))

bin_octal()

print('------------------------------------------------------------')	#60個

import operator

print('統計字數')

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/engnews.txt'
#filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/琵琶行.txt'
with open(filename, "r", encoding="utf-8") as f:
#with open(filename, "r", encoding="big5") as f:    
    data = f.read()
data = data.translate({ord(c):None for c in list("(),.“”")})
data = data.split()
word_freq = dict()
for word in data:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
ordered_freq = sorted(word_freq.items(), key = operator.itemgetter(1), reverse = True)
for w, c in ordered_freq:
    print(w, c)

print('------------------------------------------------------------')	#60個

import transformers
classifier = transformers.pipeline("sentiment-analysis", model="Raychanan/bert-base-chinese-FineTuned-Binary-Best")

text = '食物很好吃, 可惜價位太高, 讓我無法接受'
result = int(classifier(text)[0]['label'].split('_')[1])

if result:
    print("感謝您的評論, 歡迎下次再來!")
else:
    print("不好意思, 造成您不好的感受, 我們一定會改善的。")

print('------------------------------------------------------------')	#60個

print('查找出現次數最多的元素')

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

import collections
word_counts = collections.Counter(words)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]

print('------------------------------------------------------------')	#60個

print('字典串列排序')
rows = [
    {'ename': 'mouse', 'cname': '鼠', 'weight': 3},
    {'ename': 'ox', 'cname': '牛', 'weight': 48},
    {'ename': 'tiger', 'cname': '虎', 'weight': 33},
    {'ename': 'rabbit', 'cname': '兔', 'weight': 8}
]

import operator
rows_by_ename = sorted(rows, key = operator.itemgetter('ename'))
rows_by_weight = sorted(rows, key = operator.itemgetter('weight'))
print(rows_by_ename)
print(rows_by_weight)

rows_by_cename = sorted(rows, key = operator.itemgetter('cname','ename'))
print(rows_by_cename)

'''
print('------------------------------------------------------------')	#60個


import io

def string_io():
    s = io.StringIO()
    s.write('Hello World\n')
    print('This is a test', file=s)
    # Get all of the data written so far
    print(s.getvalue())

    # Wrap a file interface around an existing string
    s = io.StringIO('Hello\nWorld\n')
    print(s.read(4))
    print(s.read())

string_io()

print('------------------------------------------------------------')	#60個


#算體重總和
# 5-4-3 Counter - 多重集合 (計數器)

from collections import Counter

inventory = Counter()

loot = {'寶劍':1, '麵包':3}
inventory.update(loot)

print(inventory)

more_loot = {'寶劍', '金幣'}
inventory.update(more_loot)

print(inventory)

yet_more_loot = ['麵包', '麵包', '藥草']
inventory.update(yet_more_loot)

print(inventory)

print('鍵種類 =', len(inventory))

print('值總和 =', sum(inventory.values()))


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

print('查找wikipedia上的資料...')
import wikipedia

wikipedia.set_lang('zh')
search_pattern = '獅子'
summary = wikipedia.summary(search_pattern, sentences=1)
print(summary)

print('------------------------------------------------------------')	#60個


import shelve
book = shelve.open("addresses")

book['167'] = ('邱大熊', '0912-345678', '台北市忠孝路1號')
book['928'] = ('陳小天', '0987-654321', '新竹市中山路2號')
book.close()


import shelve
book = shelve.open("addresses")

print(book['167'] )
book.close()

print('------------------------------------------------------------')	#60個

import pathlib
path = pathlib.Path('test10_new06.py')
abs_path = path.resolve()
print(abs_path)
new_path = str(abs_path) + ".old"
print(new_path)



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('defaultdict 容器')
from collections import defaultdict

lst = ['foo', 'bar', 'pop', 'foo', 'bar', 'foo']

d = defaultdict(int)

for item in lst:
    d[item] += 1

print(d)

from collections import defaultdict

prices = [
  ['apple', 50],
  ['banana', 120],
  ['grape', 500],
  ['apple', 70],
  ['banana', 150],
  ['banana', 700]
]

fruits = defaultdict(list)

for name, price in prices:
    fruits[name].append(price)

for name, prices in fruits.items():
    print(name, prices)

print('------------------------------------------------------------')	#60個


#4-4-2 Counter 容器

from collections import Counter

lst = ['foo', 'bar', 'pop', 'foo', 'bar', 'foo']

c = Counter(lst)

print(c)

for item, counter in c.items():
    print(item, '出現', counter, '次')

print('出現最多次的項目:', c.most_common(1))

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

