
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

'''
import win32api, win32con
rc = win32api.MessageBox(0, 'kkkkk', "Installation Error", win32con.MB_ABORTRETRYIGNORE)
if rc == win32con.IDABORT:
    print('1111')
elif rc == win32con.IDIGNORE:
    print('2222')
else:
    print('3333')

'''

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


print('------------------------------------------------------------')	#60個

import csv

data = [
    ['姓名', '身高', '體重'],
    ['王小明', 174, 56],
    ['林小華', 185, 80],
    ['陳小強', 168, 60] ]

with open('p-data.csv', 'w', encoding='utf-8', newline='') as fp:
    csvwriter = csv.writer(fp)
    csvwriter.writerows(data)
    
print("done")

import csv

data = [
    ['王小明', 174, 56],
    ['林小華', 185, 80],
    ['陳小強', 168, 60] ]

with open('p-data2.csv', 'w', encoding='utf-8', newline='') as fp:
    csvwriter = csv.writer(fp)
    csvwriter.writerow(['姓名', '身高', '體重'])
    csvwriter.writerows(data)
print("done")
        
print('------------------------------------------------------------')	#60個

from fractions import Fraction

p = Fraction(22, 7)
print('分數的使用 :', p)
print('分數的使用 : {}'.format(p))
print('分數的使用 : {}'.format(float(p)))

print('------------------------------------------------------------')	#60個



from plyer import notification

print('------------------------------------------------------------')	#60個

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

''' 檢測按鍵
import keyboard

while True:
    if keyboard.is_pressed('*'):
        print('KKKK')
        continue;
    if keyboard.is_pressed('/'):
        print('SSSS')
        continue;
'''

print('------------------------------------------------------------')	#60個

import locale

print(locale.getpreferredencoding())

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


