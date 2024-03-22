import os
import sys
import time
import random
'''
print("------------------------------------------------------------")  # 60個

print('enumerate 的用法')

print('字串轉串列')
animal_string = "鼠牛虎兔龍蛇馬羊猴雞狗豬"
animal_list = list(animal_string)

for i, ani in enumerate(animal_list):
    print(i, ani)

print("------------------------------------------------------------")  # 60個

print('字串轉串列')
animal_string = "鼠牛虎兔龍蛇馬羊猴雞狗豬"
animal_list = list(animal_string)

print(type(animal_list))

print('字串切片 slicing')

n = 3
m = 9

print('第n個')
cc = animal_list[n]
print(cc)
print('第n個 到 第m-1個')
cc = animal_list[n:m]
print(cc)
print('第n個 到 最後一個')
cc = animal_list[n:]
print(cc)
print('第0個 到 第m-1個')
cc = animal_list[:m]
print(cc)
print('全部')
cc = animal_list[:]
print(cc)
print('反相')
cc = animal_list[::-1]
print(cc)

print("------------------------------------------------------------")  # 60個

"""
import os
import sys

def usage(msg):
    sys.stdout = sys.stderr
    print("Error:", msg)
    print("Use ``%s -h'' for help" % sys.argv[0])

prefix = 'aaaa'
exec_prefix = 'bbbb'
binlib = 'kkkk'
incldir = 'qqqq'

check_dirs = [prefix, exec_prefix, binlib, incldir]
for dir in check_dirs:
    if not os.path.exists(dir):
        usage('needed directory %s not found' % dir)
    if not os.path.isdir(dir):
        usage('%s: not a directory' % dir)

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
    
base = os.path.basename(filename)
base, ext = os.path.splitext(base)

dirname = os.path.dirname(filename)
print(dirname)
"""

print("------------------------------------------------------------")  # 60個

"""
# 如果檔案在目前工作目錄下可以省略路徑
print(os.path.getsize("ch14_1.py"))
print(os.path.getsize("D:\\Python\\ch14\\ch14_1.py"))

print("------------------------------------------------------------")  # 60個


print(os.listdir("D:\\Python\\ch14"))
print(os.listdir("."))                  # 這代表目前工作目錄

print("------------------------------------------------------------")  # 60個

totalsizes = 0
print("列出D:\\Python\\ch14工作目錄的所有檔案")
for file in os.listdir('D:\\Python\\ch14'):
    print(file)
    totalsizes += os.path.getsize(os.path.join('D:\\Python\\ch14', file))

print("全部檔案大小是 = ", totalsizes)
"""

print("------------------------------------------------------------")  # 60個


import datetime
now = datetime.datetime.now() # current date and time

date_time = now.strftime('%Y年%m月%d日, %H:%M:%S')
print("現在時間 :", date_time)

print("------------------------------------------------------------")  # 60個



import random

NUM_DIGITS = 10

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


secretNum = getSecretNum()
print(secretNum)

print("------------------------------------------------------------")  # 60個

import time
currentTime = time.asctime()

print("時間 :", currentTime)


entrySecond = time.time()
print("時間 :", entrySecond)



print("------------------------------------------------------------")  # 60個

print("檔案或資料夾存在 = ", os.path.exists('ch14'))
print("檔案或資料夾存在 = ", os.path.exists('C:\\_git\\vcs\\_1.data\\______test_files3'))
print("檔案或資料夾存在 = ", os.path.exists('ch14_4.py'))
print(" --- ")

print("是絕對路徑 = ", os.path.isabs('ch14_4.py'))
print("是絕對路徑 = ", os.path.isabs('C:\\_git\\vcs\\_1.data\\______test_files3\\ch14_4.py'))
print(" --- ")

print("是資料夾 = ", os.path.isdir('C:\\_git\\vcs\\_1.data\\______test_files3\\ch14_4.py'))
print("是資料夾 = ", os.path.isdir('C:\\_git\\vcs\\_1.data\\______test_files3'))
print(" --- ")

print("是檔案 = ", os.path.isfile('C:\\_git\\vcs\\_1.data\\______test_files3\\ch14_4.py'))
print("是檔案 = ", os.path.isfile('C:\\_git\\vcs\\_1.data\\______test_files3'))

print("------------------------------------------------------------")  # 60個

newdir = 'C:\\_git\\vcs\\_1.data\\______test_files3'

currentdir = os.getcwd()
print("列出目前工作資料夾 ", currentdir)

# 如果newdir不存在就建立此資料夾
if os.path.exists(newdir):
    print("已經存在 %s " % newdir)
else:
    os.mkdir(newdir)
    print("建立 %s 資料夾成功" % newdir)

# 將目前工作資料夾改至newdir
os.chdir(newdir)
print("列出最新工作資料夾 ", os.getcwd())

# 將目前工作資料夾返回
os.chdir(currentdir)
print("列出返回工作資料夾 ", currentdir)

print("------------------------------------------------------------")  # 60個

files = ['ch14_1.py', 'ch14_2.py', 'ch14_3.py']
for file in files:
    print(os.path.join('C:\\_git\\vcs\\_1.data\\______test_files3', file))   

print("------------------------------------------------------------")  # 60個

import glob

print("方法1:列出指定目錄的所有檔案")
for file in glob.glob('C:\\_git\\vcs\\_1.data\\______test_files3\*.*'):
    print(file)
    
print("方法2:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_1*.py'):
    print(file)
    
print("方法3:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_2*.*'):
    print(file)

print("------------------------------------------------------------")  # 60個

for dirName, sub_dirNames, fileNames in os.walk('oswalk'):
    print("目前工作目錄名稱:   ", dirName)
    print("目前子目錄名稱串列: ", sub_dirNames)
    print("目前檔案名稱串列:   ", fileNames, "\n")

print("------------------------------------------------------------")  # 60個

msg = "CIA Mark told CIA Linda that the secret USB had given to CIA Peter"
print("CIA最後出現位置: ", msg.rfind("CIA",0,len(msg)))
print("CIA最後出現位置: ", msg.rfind("CIA"))
'''

print("------------------------------------------------------------")  # 60個

'''
import re
import requests
import bs4

# 馬丁路德 I have a dream
url = 'http://www.analytictech.com/mb021/mlk.htm'
page = requests.get(url)
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text, 'html.parser')
p_elems = [element.text for element in soup.find_all('p')]

speech = ' '.join(p_elems)  # 將段落內容串在一起

# 修正錯字、刪除多餘的空格、移除非字母內容
speech = speech.replace(')mowing', 'knowing')
speech = re.sub('\s+', ' ', speech) 
speech_edit = re.sub('[^a-zA-Z]', ' ', speech)
speech_edit = re.sub('\s+', ' ', speech_edit)

print(speech_edit)
'''
print("------------------------------------------------------------")  # 60個

name = '荀彧'
money = 120

print('%s: %.2f元' % (name, money))

print('------------------------------------------------------------')	#60個

str1 = "Welcome to the United States and have a nice day"

list1 = str1.split()
print(list1)

str2 = "-".join(list1)
print(str2) 



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
