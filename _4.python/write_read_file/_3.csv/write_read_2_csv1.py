"""
csv檔 逗號分隔值(comma-seperated values)

預設使用','分隔, 也可以使用其他分隔符號
csv_writer = csv.writer(csvFile, delimiter='\t') # 建立Writer物件, 使用TAB區分項目 不使用逗號
csv_writer = csv.writer(csvfile, delimiter=',')
csv_writer = csv.writer(csvfile, delimiter="\t")  # 建立Writer物件
csv_reader = csv.reader(csvfile, delimiter="\t")  # 建立reader物件使用 '\t' 當分隔符號

先寫後讀

1. csv_writer = csv.writer() + writerows()

2. csv_dict_writer = csv.DictWriter() + writerows()

3. csv.reader()

4. csv.DictReader()

5. pandas(搬走)

6. 應用範例

7. 其他 & 新進

csv常用的方法(4)

reader()	讀取CSV檔案 串列形式
writer()	寫入CSV檔案 串列形式
DictReader()	讀取CSV檔案 字典形式
DictWriter()	寫入CSV檔案 字典形式

"""
print("------------------------------------------------------------")  # 60個

import sys
import csv
import random
import pathlib
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個
print("1. csv_writer = csv.writer() + writerow() + writerows()")
print("------------------------------------------------------------")  # 60個

print("寫入CSV檔 一維/2維 串列資料")

# 寫入一維串列資料  writerow(list_1d)
# 寫入二維串列資料  writerows(list_2d)

filename = "tmp_write_read_csv01.csv"

print("建立 一維串列資料")
animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列

print("建立 二維串列資料")
csv_data = [
    ["中文名", "英文名", "體重", "全名"],
    ["鼠", "mouse", 3, "米老鼠"],
    ["牛", "ox", 48, "班尼牛"],
    ["虎", "tiger", 33, "跳跳虎"],
    ["兔", "rabbit", 8, "彼得兔"],
]

# 開啟輸出的 csv 檔案
# with open(filename, 'w', encoding='utf-8', newline='') as csvfile:  # 開啟csv檔案
with open(filename, "w+", newline="") as csvfile:  # 開啟csv檔案
    # 建立 csv 檔寫入物件
    csv_writer = csv.writer(csvfile)  # 建立Writer物件, 建立 CSV 檔寫入器

    # 寫入欄位名稱
    csv_writer.writerow(("中文名", "英文名", "體重", "全名"))

    # 寫入一維串列資料 當做標題
    csv_writer.writerow(["中文名", "英文名", "體重"])

    # 寫入一維串列資料
    csv_writer.writerow(animals)

    # 寫入一維串列資料
    csv_writer.writerows(np.array(animals))
    
    # 寫入資料 writerow (一次一列資料, 寫入一維串列)
    csv_writer.writerow(["鼠", "mouse", 3, "米老鼠"])
    csv_writer.writerow(("鼠", "mouse", 3, "米老鼠"))
    csv_writer.writerow(("牛", "ox", 48, "班尼牛"))
    csv_writer.writerow(("虎", "tiger", 33, "跳跳虎"))
    csv_writer.writerow(["兔", "rabbit", 8, "彼得兔"])
    
    # 寫入資料 writerows (一次多列資料, 寫入二維串列)

    print("寫入CSV檔 二維串列資料 一次寫入")
    # 寫入二維串列資料
    csv_writer.writerows(csv_data)

    print("寫入CSV檔 二維串列資料 一次寫一行(row)")
    for line in csv_data:
        csv_writer.writerow(line)

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("2. csv_dict_writer = csv.DictWriter() + writerows()")
print("------------------------------------------------------------")  # 60個

print("寫入CSV檔 DictWriter")

filename = "tmp_write_read_csv02.csv"

with open(filename, "w", newline="") as csvfile:  # 開啟csv檔案
    # 定義欄位
    fieldnames = ["中文名", "英文名", "體重", "全名"]

    csv_dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # 建立Writer物件

    # 寫入欄位名稱
    csv_dict_writer.writeheader()
    # 寫入資料, 將 dictionary 寫入 csv 檔
    csv_dict_writer.writerow({"中文名": "鼠", "英文名": "mouse", "體重": 3, "全名": "米老鼠"})
    csv_dict_writer.writerow({"中文名": "牛", "英文名": "ox", "體重": 48, "全名": "班尼牛"})
    csv_dict_writer.writerow({"中文名": "虎", "英文名": "tiger", "體重": 33, "全名": "跳跳虎"})
    csv_dict_writer.writerow({"中文名": "兔", "英文名": "rabbit", "體重": 8, "全名": "彼得兔"})

print("寫入檔案 " + filename + " 完成, 檔案 :", filename)

print("------------------------------------------------------------")  # 60個

csvfile = open("tmp_write_read_csv03.csv", "w", newline="")
# 建立writer物件，同時指定欄位名稱
csv_dict_writer = csv.DictWriter(csvfile, fieldnames=["中文名", "英文名", "體重"])
csv_dict_writer.writeheader()  # 寫入欄位名稱
csv_dict_writer.writerow({"中文名": "鼠", "英文名": "mouse", "體重": 3})

# 寫入兩筆產品記錄到csv檔中
csv_dict_writer.writerow({"中文名": "牛", "英文名": "ox", "體重": 48})

csvfile.close()

print("------------------------------------------------------------")  # 60個

filename = "tmp_write_read_csv04.csv"
with open(filename, "w", newline="") as csvfile:  # 開啟csv檔案
    fields = ["中文名", "英文名", "體重"]
    csv_dict_writer = csv.DictWriter(csvfile, fieldnames=fields)  # 建立Writer物件

    csv_dict_writer.writeheader()  # 寫入標題
    csv_dict_writer.writerow({"中文名": "鼠", "英文名": "mouse", "體重": "3"})
    csv_dict_writer.writerow({"中文名": "牛", "英文名": "ox", "體重": "48"})

print("------------------------------------------------------------")  # 60個

# 定義串列,元素是字典
dictList = [
    {"中文名": "鼠", "英文名": "mouse", "體重": "3"},
    {"中文名": "牛", "英文名": "ox", "體重": "48"},
]

filename = "tmp_write_read_csv05.csv"
with open(filename, "w", newline="", encoding="utf-8") as csvfile:  # 開啟csv檔案
    fields = ["中文名", "英文名", "體重"]
    csv_dict_writer = csv.DictWriter(csvfile, fieldnames=fields)  # 建立Writer物件
    csv_dict_writer.writeheader()  # 寫入標題
    for line in dictList:  # 寫入內容
        csv_dict_writer.writerow(line)

print("------------------------------------------------------------")  # 60個

# 寫 暫存

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("3. csv.reader()")
print("------------------------------------------------------------")  # 60個

filename = "data/animals.csv"

# 讀取方法相同 印出資料方法1
#with open(filename, newline="") as csvfile:  # 開啟csv檔案
with open(filename, 'r', encoding='utf-8') as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)  # 讀取 csv 檔案內容
    # 以迴圈讀取每一列
    for line in csv_reader:
        print(line)

# 讀取方法相同 印出資料方法2, 完整地讀取每一個元素
#with open(filename, newline="") as csvfile:  # 開啟csv檔案
with open(filename, 'r', encoding='utf-8') as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)  # 讀取 csv 檔案內容

    list_data = list(csv_reader)  # 將資料轉成串列
    length = len(list_data)
    data_column = len(list_data[0])
    print("data_column = ", data_column)
    for line in list_data:
        print(line)

print("------------------------------------------------------------")  # 60個

filename = "data/animals.csv"

#with open(filename) as csvfile:  # 開啟csv檔案
#with open(filename, encoding="utf-8") as csvfile:  # 開啟csv檔案
with open(filename, "r", encoding="UTF-8-sig") as csvfile:  # 開啟csv檔案
    for line in csvfile:
        print(line)

with open(filename, "r", encoding="UTF-8-sig") as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)  # 讀檔案建立Reader物件
    list_data = list(csv_reader)  # 將資料轉成串列
    print(list_data)
    for line in list_data:  # 將二維串列list_data 逐列印出
        print(line)

print("------------------------------------------------------------")  # 60個

print('測試 readline() 與 readlines()')

filename = "data/animals.csv"

with open(filename, "rt", encoding="UTF-8-sig") as csvfile:  # 開啟csv檔案
    print("readline() 讀出1行")
    cc = csvfile.readline() 
    print(cc)
    print("readline() 讀出1行")
    cc = csvfile.readline()
    print(cc)
    print("readlines() 從目前位置讀到檔尾 => 一維串列")
    cc = csvfile.readlines()
    print(cc)

print("------------------------------------------------------------")  # 60個

filename = "data/animals_big5.csv"

with open(filename) as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    headerRow = next(csv_reader)  # 讀取文件下一列
    print(headerRow)
    for i, header in enumerate(headerRow):
        print(i, header)
    for line in csv_reader:
        print(line[0], line[1], line[2], line[3])

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("4. csv.DictReader()")
print("------------------------------------------------------------")  # 60個

filename = "data/animals_big5.csv"

list_data = list()
with open(filename, newline="") as csvfile:  # 開啟csv檔案
    csv_dict_reader = csv.DictReader(csvfile)  # 讀取 csv 檔內容，將每一列轉成 dictionary
    # 以迴圈讀取每一列
    for line in csv_dict_reader:  # 列出DictReader各列內容
        print(line)
        list_data.append(dict(line))

print(type(list_data))
print(len(list_data))
print(list_data)

print("------------------------------------------------------------")  # 60個

filename = "data/animals_big5.csv"

import pprint as pp

list_data = list()
with open(filename, "rt") as csvfile:  # 開啟csv檔案
    csv_dict_reader = csv.DictReader(csvfile)  # 讀取 csv 檔內容，將每一列轉成 dictionary
    for line in csv_dict_reader:  # 列出DictReader各列內容
        list_data.append(dict(line))
pp.pprint(list_data)

print("------------------------------------------------------------")  # 60個

filename = "data/animals_big5.csv"

# with open(filename, newline="", encoding="utf-8") as csvfile:  # 開啟csv檔案
with open(filename) as csvfile:  # 開啟csv檔案
    csv_dict_reader = csv.DictReader(csvfile)  # 讀取 csv 檔內容，將每一列轉成 dictionary
    for line in csv_dict_reader:  # 列出DictReader各列內容
        print(line)
        #print(line["中文名"], line["英文名"])

print("------------------------------------------------------------")  # 60個

from io import StringIO

# 本地檔案
filename = "data/animals_big5.csv"

print("讀取一個本地csv檔案 : " + filename)

# 讀取本地檔案
data = open(filename).read()

csvfile = StringIO(data)

csv_reader = csv.reader(csvfile)  # 讀取 csv 檔案內容

for line in csv_reader:
    print(line[0] + line[1] + line[2] + line[3])

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("6. 應用範例")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("7. 其他 & 新進")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

"""


        self.load_rules(os.path.join(os.path.dirname(__file__), '..',
                                     'susp-ignored.csv'))


            self.warn('[%s:%d] "%s" found in "%-.120s"' %
                      (self.docname, lineno, issue, text))

應該重複
with open(filename, "r") as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    for line in csv_reader:
        print(line)

csvfile = pathlib.Path(filename).open(encoding="UTF-8")
csvfile = pathlib.Path(filename).open(encoding="UTF-8")

with pathlib.Path(filename).open(encoding="big5") as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile)
    for line in csv_reader:
        print(line)

csvfile = open(filename, "w", newline="")

# 以附加模式開啟檔案
csvfile=open(filename, 'a', newline='') 

with open(filename, "w", newline="", encoding="utf-8") as csvfile:
with open(filename, "w+", newline="") as csvfile:
with open(filename, "w", newline="", encoding="utf-8") as csvfile:
with open(filename, 'w', newline='') as csvfile:
with open(filename, "w", newline="") as csvfile:
with open(filename, 'w') as csvfile:
with open(filename, 'w', newline='', encoding="big5") as csvfile:
with open(filename, 'w', newline = '') as csvfile:

csvfile = open(filename, 'a')
writer = csv.writer(csvfile, dialect)


    for line in list_data:
        print("%-20s%-20s%-10s%-20s" % (line[0], line[1], line[2], line[3]))



    with open(passwd_filename, "r") as csvfile1,
    open(csv_filename, "w", newline="") as csvfile2:
        csv_reader = csv.reader(csvfile1, delimiter=":")
        csv_writer = csv.writer(csvfile2, delimiter="\t", lineterminator="\n")
        for line in csv_reader:
            csv_writer.writerow([line[0], line[2]])



"""



"""
with open(filename_r, 'r') as csvfile:  # 開啟csv檔案
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    print(header)
    # get number of columns
    #array = header.split(',')
    first_item = header[0]
    for line in csv_reader:
        print(','.join(line))
        print(line[2])
"""

print("------------------------------------------------------------")  # 60個

filename = "data/新竹縣日出日落2024.csv" #格式是 UTF-16LE BOM

list_data = list()
list_data_sun_rise = list()
list_data_sun_fall = list()

with open(filename, encoding="utf-16le") as csvfile:  # 開啟csv檔案
    csv_dict_reader = csv.DictReader(csvfile)  # 讀取 csv 檔內容，將每一列轉成 dictionary
    cnt = 0
    # 以迴圈讀取每一列
    for line in csv_dict_reader:  # 列出DictReader各列內容
        #print(line)
        list_data.append(dict(line))
        list_data_sun_rise.append(line["日出時刻"])
        list_data_sun_fall.append(line["日沒時刻"])

        #print(line["中文名"], line["英文名"])

print(type(list_data))
print(len(list_data))


sys.exit()

"""
cnt = 0
for dd in list_data:
    #print(dd)
    print(dd["地點"])
    print(dd["日出時刻"])
    print(dd["日沒時刻"])
    cnt += 1
    if cnt > 10:
        break
"""


#print(list_data_sun_rise)
print(max(list_data_sun_rise))
print(min(list_data_sun_rise))
print()
#print(list_data_sun_fall)
print(max(list_data_sun_fall))
print(min(list_data_sun_fall))
print()


#地點,日期,天文曙光始,航海曙光始,民用曙光始,日出時刻,方位,過中天,仰角,日沒時刻,方位,民用暮光終,航海暮光終,天文暮光終
