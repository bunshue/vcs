"""
整理python檔案

1. 檢查檔案編碼格式
2. 轉換為utf-8格式
3. 簡中轉正中

"""

import os
import sys
import time
import random

import glob

import chardet  # 檔案編碼格式

print("------------------------------------------------------------")  # 60個

filenames = glob.glob("*")
for filename in filenames:
    text = open(filename, "rb").read()
    codetype = chardet.detect(text)
    # print(type(codetype))
    # print(codetype['encoding'])
    # print('{} 編碼格式：{}'.format(filename, codetype))

    # 印出不是utf-8格式的檔案名稱
    if not codetype["encoding"] == "utf-8":
        print("不是utf-8格式\t{} 編碼格式：{}".format(filename, codetype))

print("------------------------------------------------------------")  # 60個
