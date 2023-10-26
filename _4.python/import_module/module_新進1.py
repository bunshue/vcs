
print('------------------------------------------------------------')	#60個

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


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


