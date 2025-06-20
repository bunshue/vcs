import os
import sys
import random
import chardet  # 檔案編碼格式

print("------------------------------------------------------------")  # 60個

import warnings

warnings.warn(
    "Use importlib.util.find_spec() instead.", DeprecationWarning, stacklevel=1
)

print("建立一組密碼")
import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
password = ""
for c in range(20):
    password += random.choice(chars)
print("建立一組密碼:\t%r" % (password))

print("------------------------------------------------------------")  # 60個

print("純文字檔的diff")

import difflib

filename1 = "C:/_git/vcs/_1.data/______test_files1/compare/text_filea.txt"
filename2 = "C:/_git/vcs/_1.data/______test_files1/compare/text_fileb.txt"


def fcompare(f1name, f2name):
    print("-:", f1name)
    print("+:", f2name)
    f1 = open(f1name)
    f2 = open(f2name)
    if not f1 or not f2:
        return 0

    a = f1.readlines()
    f1.close()
    b = f2.readlines()
    f2.close()
    for line in difflib.ndiff(a, b):
        print(line, end=" ")


ret = fcompare(filename1, filename2)
print("\n\nresult : ", ret)

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

import abc

metaclass = abc.ABCMeta
print(metaclass)

print("------------------------------------------------------------")  # 60個

import uuid

id = str(uuid.uuid4())
print(id)

import uuid

print("uuid = {}".format(str(uuid.uuid4())))

print("------------------------------------------------------------")  # 60個

import socket

hostname = socket.gethostname()
print("取得 hostname :", hostname)

import time

path = "cccc"
print("%s.%s.%s.%s" % (path, int(time.time()), socket.gethostname(), os.getpid()))

print("------------------------------------------------------------")  # 60個

from plyer import notification

print("notification 測試")

text = "Welcome to the United States and have a nice day."
msg = "cccccc"
notification.notify(title=text, message=msg)

print("------------------------------------------------------------")  # 60個

print("列出所有python關鍵字")
import keyword

print(keyword.kwlist)

keywordLists = ["as", "while", "break", "sse", "Python"]
for x in keywordLists:
    print(f"{x:>8s} {keyword.iskeyword(x)}")

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

print("------------------------------------------------------------")  # 60個


def bin_octal():
    x = 65535
    print(type(bin(x)))
    print(bin(x), oct(x), hex(x))

    # format() function
    print(format(x, "b"))
    print(format(x, "o"))
    print(format(x, "x"))

    print(int("ffff", 16))
    print(int("10011010010", 2))


bin_octal()

print("------------------------------------------------------------")  # 60個

import transformers

classifier = transformers.pipeline(
    "sentiment-analysis", model="Raychanan/bert-base-chinese-FineTuned-Binary-Best"
)

text = "食物很好吃, 可惜價位太高, 讓我無法接受"
result = int(classifier(text)[0]["label"].split("_")[1])

if result:
    print("感謝您的評論, 歡迎下次再來!")
else:
    print("不好意思, 造成您不好的感受, 我們一定會改善的。")

print("------------------------------------------------------------")  # 60個

import io


def string_io():
    s = io.StringIO()
    s.write("Hello World\n")
    print("This is a test", file=s)
    # Get all of the data written so far
    print(s.getvalue())

    # Wrap a file interface around an existing string
    s = io.StringIO("Hello\nWorld\n")
    print(s.read(4))
    print(s.read())


string_io()

print("------------------------------------------------------------")  # 60個

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

# tqdm 顯示迴圈或任務的進度條


from tqdm import tqdm

n_samples = [10, 20, 50, 100, 200, 500, 1000, 2000, 3000, 5000, 7500, 10000]

for i in tqdm(n_samples):
    time.sleep(0.5)  # 模擬耗時任務
    print()
    # print(i)

print("------------------------------")  # 30個

from tqdm import tqdm

for i in tqdm(range(10)):
    time.sleep(0.5)  # 模擬耗時任務
    print()

print("------------------------------")  # 30個

# 進度條描述:可以添加一段描述，說明正在處理的內容
for i in tqdm(range(10), desc="處理進度 :"):
    time.sleep(0.5)
    print()

print("------------------------------")  # 30個

# 處理數據集合:可以使用 tqdm 包裝任何可迭代對象
data = [1, 2, 3, 4, 5]
for item in tqdm(data, desc="讀取進度 :"):
    time.sleep(0.5)
    print()

print("------------------------------")  # 30個

# 手動更新進度:適合用於非迴圈任務
from tqdm import tqdm

with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.5)
        pbar.update(10)  # 每次更新進度條 10%
        print()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# dist：經緯度距離
# pip install https://github.com/duboviy/dist/archive/master.zip

import dist

# 台北火車站 25.047778, 121.517222
# 新竹火車站 24.802050, 120.971817

x1 = 25.047778
y1 = 121.517222
x2 = 24.802050
y2 = 120.971817

print(dist.compute(25.0342, 121.5646, 24.9932, 121.3009))
print(dist.compute(x1, y1, x2, y2))

print("------------------------------------------------------------")  # 60個

print("verifyid：驗證身分證字號")

from verifyid import verifyid

verify = verifyid.IdentyNumber()

veri = verify.check_identy_number("A189229579")
print("A189229579 驗證結果：{}".format(veri))
veri = verify.check_identy_number("a189229579")
print("a189229579 驗證結果：{}".format(veri))
veri = verify.check_identy_number("A123456780")
print("A123456780 驗證結果：{}".format(veri))

city = verify.get_city("A189229579")
print("A189229579 城市：{}".format(city))
city = verify.get_city("P123456789".upper())
print("P123456789 城市：{}".format(city))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("chardet：檔案編碼格式")

import chardet  # 檔案編碼格式

filename1 = "C:/_git/vcs/_1.data/______test_files1/poetry2.txt"
filename2 = (
    "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/_encoding/2.utf_to_ascii.txt"
)
filename3 = (
    "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/_encoding/3.ascii_to_unicode.txt"
)

files = [filename1, filename2, filename3]
for f in files:
    text = open(f, "rb").read()
    codetype = chardet.detect(text)
    print("檔案 :", f)
    print("編碼格式 :", codetype)
    print("讀取文件")
    with open(f, "rb") as fp:
        content = fp.read()
        cod = chardet.detect(content)["encoding"]
        print("編碼格式 :", cod)
        # cc = content.decode(cod)
        # print(cc)

print("------------------------------")  # 30個

filename = "C:/_git/vcs/_4.python/ml/text/data/中文文本分类数据集/test/C3-Art/C3-Art0002.txt"
f = open(filename, encoding="gb2312")
a = f.read()
f.close()
print(a)

text = open(filename, "rb").read()
codetype = chardet.detect(text)
print(codetype)

cod = chardet.detect(text)["encoding"]
print(cod)
print(text.decode(cod))

print("------------------------------")  # 30個

"""
整理python檔案

1. 檢查檔案編碼格式
2. 轉換為utf-8格式
3. 簡中轉正中

"""

import time
import random
import glob


filenames = glob.glob("*.txt")
for filename in filenames:
    print("檔案 :", filename)
    text = open(filename, "rb").read()  # 要用 rb
    codetype = chardet.detect(text)
    # print(type(codetype))
    # print(codetype['encoding'])
    # print('{} 編碼格式：{}'.format(filename, codetype))

    # 印出不是utf-8格式的檔案名稱
    if not codetype["encoding"] == "utf-8":
        print("非utf-8格式, 編碼格式：{}".format(codetype))
    else:
        print("utf-8格式\n")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("查找wikipedia上的資料...")
import wikipedia

wikipedia.set_lang("zh")
search_pattern = "獅子"
summary = wikipedia.summary(search_pattern, sentences=1)
print(summary)

wikipedia.set_lang("zh")
wikipedia.summary("柔道")

# python wiki_sample.py
# python try_sys.py 想查詢的關鍵字
# python wiki_sample_final.py 柔道

print("------------------------------------------------------------")  # 60個

print("將檔案移到資源回收筒")

import send2trash

filename = "picture1cccc.jpg"
send2trash.send2trash(filename)

print("------------------------------------------------------------")  # 60個

import pygal.maps.world

worldMap = pygal.maps.world.World()  # 建立世界地圖物件
worldMap.title = "Populations in China/Japan/Thailand"  # 世界地圖標題
worldMap.add("Asia", {"cn": 1262645000, "jp": 126870000, "th": 63155029})  # 標記人口資訊
worldMap.add("Europe", {"fr": 60762406, "se": 1011781, "sz": 7184798})  # 標記人口資訊
worldMap.add("Africa", {"cd": 49626496, "eg": 67649043, "za": 44000833})  # 標記人口資訊
worldMap.add(
    "North America", {"us": 282162848, "mx": 99959895, "ca": 30770661}
)  # 標記人口資訊
worldMap.render_to_file("tmp_world_map.svg")  # 儲存地圖檔案

print("------------------------------------------------------------")  # 60個

print("全形 轉 半形")
import unicodedata

text = "「全形１２．３」「全形Ａｂｃ！（＠）」「半形片假名」「圈圈數字①②③」「符號㏊」"

print("全形 :", text)
text = unicodedata.normalize("NFKC", text)
print("半形 :", text)

print("------------------------------------------------------------")  # 60個

# 將兩個數值以decimal型別來處理

import decimal

num1 = decimal.Decimal("0.5534")
num2 = decimal.Decimal("0.427")
num3 = decimal.Decimal("0.37")
print("相加", num1 + num2 + num3)
print("相減", num1 - num2 - num3)
print("相乘", num1 * num2 * num3)
print("相除", num1 / num2)

print("------------------------------------------------------------")  # 60個

import pathlib

print(pathlib.Path.cwd())

print("------------------------------------------------------------")  # 60個

import easygui

# easygui.msgbox(msg="AAAAAAAAAAAAAA", title="標題",ok_button="按這裡，繼續")

# easygui.buttonbox(msg="選出一個你喜歡的人物", title="標題",choices=("AAA","BBB","CCC","DDD","EEE"))

easygui.enterbox(msg="請輸入你想說的話", title="標題", default="預設內容")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
