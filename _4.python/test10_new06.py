import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

text = '王之渙涼州詞黃河遠上白雲間，一片孤城萬仞山。羌笛何須怨楊柳？春風不度玉門關。'
word1 = '春風'
word2 = '白雲'

count1 = text.count(word1)
print(word1, ":", count1, "個")

count2 = text.count(word2)
print(word2, ":", count2, "個")

print(text)

print('將', word1 ,'改成', word2)
text = text.replace(word1, word2)

print(text)

print("------------------------------------------------------------")  # 60個

import pathlib

all_files = sorted(os.listdir('system'))

print(pathlib.Path.cwd())

path1 = pathlib.Path.cwd() / 'system'
print(path1)

for i, _ in enumerate(all_files[:-1]):  #跳過最後一個
    print(i, _)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print('全形 轉 半形')
import unicodedata

text = "「全形１２．３」「全形Ａｂｃ！（＠）」「半形片假名」「圈圈數字①②③」「符號㏊」"

print("全形 :", text)
text = unicodedata.normalize("NFKC", text)
print("半形 :", text)


print("------------------------------------------------------------")  # 60個

import re

text = "這個是、那個是、那個是、哪個是"
word1 = "這.是"
word2 = ".個是"

pattern = re.compile(word1)
count = len(re.findall(pattern, text))
print(word1, ":", count, "個")

pattern = re.compile(word2)
count = len(re.findall(pattern, text))
print(word2, ":", count, "個")


import re

text = "這個是測試資料。"
word1 = ".個是"
word2 = "那個是"

print("置換前 :", text)
pattern = re.compile(word1)
text = re.sub(pattern, word2, text)
print("置換後 :", text)

print("------------------------------------------------------------")  # 60個

import pathlib

filename = "test10_new07.py"
filename = "C:/_git/vcs/_4.python/_data/蘇軾_念奴嬌_赤壁懷古.txt"

try:
    p = pathlib.Path(filename)  # 文字檔案的
    text = p.read_text(encoding="UTF-16")  # 載入文字
    print(text)  # 顯示
except:
    print("程式執行失敗。")  # 出現錯誤時


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
