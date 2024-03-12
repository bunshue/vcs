import os
import sys
import time
import random

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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
