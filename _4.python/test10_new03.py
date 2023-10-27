import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


#! /usr/bin/env python3
"""n2w: 數字轉英文模組, 包含一個num2words函式, 也能獨立執行
獨立執行用法: n2w num
              num: 0~999,999,999,999,999 之間的整數 (可用逗號分隔)
範例: n2w 10,003,103
輸入 10,003,103 後會輸出 ten million three thousand one hundred three
"""

import sys, string, argparse

#數字與英文的對應字典
_1to9dict = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
             '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
             '9': 'nine'}
_10to19dict = {'0': 'ten', '1': 'eleven', '2': 'twelve',
               '3': 'thirteen', '4': 'fourteen', '5': 'fifteen',
               '6': 'sixteen', '7': 'seventeen', '8': 'eighteen', 
               '9': 'nineteen'}
_20to90dict = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
               '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}

#數字位數與數字英文單位的對應串列(list)
_magnitude_list = [(0, ''), (3, ' thousand '), (6, ' million '), 
                  (9, ' billion '), (12, ' trillion '),(15, '')]

#數字轉英文的函式
def num2words(num_string):
    """num2words(num_string): convert number to English words"""
    if num_string == '0':                                             
        return 'zero'
    num_string = num_string.replace(",", "")
    num_length = len(num_string) 
    max_digits = _magnitude_list[-1][0]
    if num_length > max_digits:
        return "Sorry, can't handle numbers with more than  " \
               "{0} digits".format(max_digits)
    num_string = '00' + num_string 
    word_string = ''

    #用迴圈從數字最右邊逐次取三個數字來處理，亦即從右邊三個一組進行轉換
    for mag, name in _magnitude_list:
        if mag >= num_length:
            return word_string
        else:
            hundreds, tens, ones = num_string[-mag-3], \
                 num_string[-mag-2], num_string[-mag-1]               
            if not (hundreds == tens == ones == '0'):                 
                word_string = _handle1to999(hundreds, tens, ones) + \
                                            name + word_string        
                 
#處理1~999的函式
def _handle1to999(hundreds, tens, ones):
    if hundreds == '0':
        return _handle1to99(tens, ones)
    else:
        return _1to9dict[hundreds] + ' hundred ' + _handle1to99(tens, ones)

#處理1~99的函式
def _handle1to99(tens, ones):
    if tens == '0': 
        return _1to9dict[ones]
    elif tens == '1':
        return _10to19dict[ones]
    else:
        return _20to90dict[tens] + ' ' + _1to9dict[ones]

num = '12345678'
#將第一個命令列參數值轉為英文，其餘命令列參數不處理
result = num2words(num)
print("{0} 的英文念法是: {1}".format(num, result))

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
rawdata = '''我
我的
眼睛
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止'''
words = rawdata.split('\n')
def poem():
    n = np.random.randint(2, 8) # 2-8句, 決定有幾句

    for i in range(n):
        m = np.random.randint(1, 6) # 決定每句的長度
        sentence = np.random.choice(words, m, replace=False)
        print(" ".join(sentence))
poem()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



