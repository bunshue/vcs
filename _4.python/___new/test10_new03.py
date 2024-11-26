"""


"""

import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個
"""
import glob,cv2

foldername = "animal"
 
#建立測試資料
filenames = glob.glob(foldername + '/*.jpg') + glob.glob(foldername + '/*.png')

for filename in filenames:
    print(filename)



print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

#filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

os.system(filename)  # 用系統內建的程式開啟檔案

"""

print("------------------------------------------------------------")  # 60個

print("統計一串英文字串個字母出現的頻率")

from collections import defaultdict

text = "this is a lion-mouse"

frequency = defaultdict(int)
for symbol in text:
    frequency[symbol] += 1
print(frequency)

heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
print(heap)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

"""
from pathlib import Path

# Version
BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

VERSION_FILE = BASE_DIR.joinpath('data_store', 'cccc.py')
print(VERSION_FILE)

#執行一個檔案
with open(VERSION_FILE) as fp:
    exec(fp.read())

import os
from pathlib import Path
from setuptools import setup, find_packages

import dicom

BASE_DIR = Path(__file__).parent
with open(BASE_DIR / "pydicom" / "_version.py") as f:
    exec(f.read())

with open(BASE_DIR / 'README.md') as f:
    long_description = f.read()


def data_files_inventory():
    root = BASE_DIR / "pydicom" / "data"
    files = [
        f.relative_to(BASE_DIR / "pydicom")
        for f in root.glob("**/*")
        if f.is_file() and f.suffix != ".pyc"
    ]
    return [os.fspath(f) for f in files]





"""

print("------------------------------------------------------------")  # 60個


from pathlib import Path

data_path = Path(__file__).resolve().parent.parent / "data"
print(data_path)


print("------------------------------------------------------------")  # 60個


import pydicom.data
from pydicom.data import get_testdata_file

fname = "693_UNCI.dcm"
fpath = get_testdata_file(fname)
print(fpath)

print("done")

print("------------------------------------------------------------")  # 60個

# UTC时间

import datetime

# 创建一个时间戳（以秒为单位）
timestamp = 22
# 带UTC时区时间
dt_with_timezone = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)
print("带UTC时区时间:", dt_with_timezone)
# 不带UTC时区时间
dt_without_timezone = datetime.datetime.fromtimestamp(timestamp)
print("不带UTC时区时间", dt_without_timezone)

# 时间戳
import time

print(time.time())
print(time.localtime())  # 获取到当前时间的元组
print(time.mktime(time.localtime()))
# 一周的第几天(周一是0,0-6)、一年的第几天(从1开始，1-366)、夏时令(是夏时令1，不是0，未知-1)。

# 字符串和时间转换

# 字符串和时间转换
# 利用time模块的strftime()函数可以将时间戳转换成系统时间。
import time

time_str = time.strftime(("%Y-%m-%d %H:%M:%S"), time.localtime())
print(time_str)

# 可以用strptime函数将日期字符串转换为datetime数据类型，
import datetime

print(datetime.datetime.strptime("2022-01-15", "%Y-%m-%d"))

# 可以用Pandas的to_datetime()函数将日期字符串转换为datetime数据类型。
# to_datetime()函数转化后的时间是精准到时分秒精度的
import pandas as pd

print(pd.to_datetime("2022/01/15"))

# 时间差

# 3. 时间运算--时间差
# 利用datetime将时间类型数据进行转换，然后利用减法运算计算时间的不同之处
# 默认输出结果转换为用（“天”，“秒”）表达
import datetime

delta = datetime.datetime(2022, 1, 16) - datetime.datetime(2021, 1, 1, 9, 15)
print(delta)
print(delta.days)
print(delta.seconds)

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

# Classes and Objects


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"


# Create an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Print the attributes of the instance
print("my_dog name:", my_dog.name)
print("my_dog age:", my_dog.age)

# Call the bark method of the instance
bark_result = my_dog.bark()
print("bark_result:", bark_result)
