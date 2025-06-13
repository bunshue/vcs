"""
Python自學聖經(第二版) 12

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# csv_write_dict.py

import csv
with open('tmp_test3.csv', 'w', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['姓名', '身高', '體重']

    # 將 dictionary 寫入 csv 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入欄位名稱
    writer.writeheader()
    # 寫入資料
    writer.writerow({'姓名': 'Chiou', '身高': 170, '體重': 65})
    writer.writerow({'姓名': 'David', '身高': 183, '體重': 78})

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
"""
# LinkGoogleSheet.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac

# 設定金鑰檔路徑及驗證範圍
auth_json = 'pythonconnectgsheet1-273500-e6ce04448957.json'
gs_scopes = ['https://spreadsheets.google.com/feeds']
# 連線資料表
cr = sac.from_json_keyfile_name(auth_json, gs_scopes)
gs_client = gspread.authorize(cr) 
# 開啟資料表
spreadsheet_key = '1lBlHPDYqwnQNiJrz-8nqPEd5H6Q4w0PaKasrrjojCNI' 
sheet = gs_client.open_by_key(spreadsheet_key)
# 開啟工作簿
wks = sheet.sheet1
# 清除所有內容
wks.clear() 
# 新增列
listtitle=["姓名","電話"]
wks.append_row(listtitle)  # 標題
listdata=["chiou","0937-1234567"]
wks.append_row(listdata)   # 資料內容

print("------------------------------------------------------------")  # 60個

# LinkGoogleSheet'''''.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac
# 設定金鑰檔路徑及驗證範圍
auth_json = 'PythonConnectGsheet1-6a6086d149c5.json'
gs_scopes = ['https://spreadsheets.google.com/feeds']
# 連線資料表
cr = sac.from_json_keyfile_name(auth_json, gs_scopes)
gs_client = gspread.authorize(cr) 
# 開啟資料表
spreadsheet_key = '1OihpM657yWo1lc3RjskRfZ8m75dCPwL1IPwoDXSvyzI' 
sheet = gs_client.open_by_key(spreadsheet_key)
# 開啟工作簿
wks = sheet.sheet1
# 清除所有內容
wks.clear() 
# 新增列
listtitle=["姓名","電話"]
wks.append_row(listtitle)  # 標題
listdata=["chiou","0937-1234567"]
wks.append_row(listdata)  # 資料內容
"""
print("------------------------------------------------------------")  # 60個

# tree1.py

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

xml='''\
<?xml version="1.0"?>
<data 名稱="e-happy">
    <person 姓名="David">
        <身高>183</身高>
    </person>
</data>
'''

root = ET.fromstring(xml) # 從字串載入並解析 XML資料
print('資料型別：', type(root))   # <class 'xml.etree.ElementTree.Element'>
print('根目錄標籤：' + root.tag)  #data
print('根目錄屬性：' + str(root.attrib))   # {'名稱': 'e-happy'}
print('根目錄值：' + str(root.text))       # 空字串
print('屬性內容：' + str(root.get('名稱'))) # e-happy
root.set('名稱','文淵閣工作室')
print('屬性內容：' + str(root.get('名稱'))) # 文淵閣工作室

print("------------------------------------------------------------")  # 60個

# tree2.py

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.parse('data/data.xml') # 從檔案載入並解析 XML資料

print('tree資料型別：', type(tree)) # <class 'xml.etree.ElementTree.ElementTree'>
root = tree.getroot()
print('root資料型別：', type(root)) # <class 'xml.etree.ElementTree.Element'>
print('根目錄標籤：' + root.tag)    # data
print('根目錄屬性：' + str(root.attrib)) # {'名稱': 'e-happy'}

print("------------------------------------------------------------")  # 60個

# xml_append.py

import xml.etree.cElementTree as ET

xml='''\
<?xml version="1.0"?>
<data 名稱="e-happy">
    <person 姓名="David">
        <身高>183</身高>
		<興趣>長跑</興趣>
    </person>
    <person 姓名="Chiou">
        <身高>170</身高>
		<興趣>籃球</興趣>
    </person>
</data>
'''

root = ET.fromstring(xml) # 從字串載入並解析 XML資料
person = ET.Element("person")      # 建立標籤 person
person.attrib = {"姓名": "Tsjeng"} # 設定 person 標籤的屬性和資料
# 建立 person 的標籤，並新增屬性和資料
tall = ET.SubElement(person, "身高")
tall.text = "176"
hobby = ET.SubElement(person, "興趣")
hobby.text = "圍棋"
root.append(person)
print(root[2].get('姓名'))         # Tsjeng

print("------------------------------------------------------------")  # 60個

# xml_edit.py

import xml.etree.cElementTree as ET

def pretty_xml(element, indent, newline, level=0):
    if element:  # 判斷element是否有子元素    
        if (element.text is None) or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
    temp = list(element)  # 將element轉成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最後一個元素，表示下一行是同級别元素的起始，缩排應一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最後一個元素， 表示下一行是母元素的结束，缩排應該少一個   
            subelement.tail = newline + indent * level
        pretty_xml(subelement, indent, newline, level=level + 1)  # 對子元素進行遞迴操作

xml='''\
<?xml version="1.0"?>
<data 名稱="e-happy">
    <person 姓名="David">
        <身高>183</身高>
		<興趣>長跑</興趣>
    </person>
    <person 姓名="Chiou">
        <身高>170</身高>
		<興趣>籃球</興趣>
    </person>
</data>
'''
        
root = ET.fromstring(xml) # 從字串載入並解析 XML資料
root[0].set('姓名','鮭魚')
hobby=root[0].find('興趣')
hobby.text = "跑馬拉松"

root.remove(root[1])         # 刪除 root[1]
pretty_xml(root, '\t', '\n') # xml資料縮排

tree = ET.ElementTree(root)  # 建立tree物件，寫入檔案
tree.write("tmp_newdata2.xml", encoding="UTF-8")

print("------------------------------------------------------------")  # 60個

# xml_insert.py

import xml.etree.cElementTree as ET

xml='''\
<?xml version="1.0"?>
<data 名稱="e-happy">
    <person 姓名="David">
        <身高>183</身高>
		<興趣>長跑</興趣>
    </person>
    <person 姓名="Chiou">
        <身高>170</身高>
		<興趣>籃球</興趣>
    </person>
</data>
'''

def pretty_xml(element, indent, newline, level=0):
    if element:  # 判斷element是否有子元素    
        if (element.text is None) or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
    temp = list(element)  # 將element轉成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最後一個元素，表示下一行是同級别元素的起始，缩排應一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最後一個元素， 表示下一行是母元素的结束，缩排應該少一個   
            subelement.tail = newline + indent * level
        pretty_xml(subelement, indent, newline, level=level + 1)  # 對子元素進行遞迴操作

root = ET.fromstring(xml) # 從字串載入並解析 XML資料
person = ET.Element("person")      # 建立標籤 person
person.attrib = {"姓名": "Tsjeng"} # 設定 person 標籤的屬性和資料
# 建立 person 的標籤，並新增屬性和資料
tall = ET.SubElement(person, "身高")
tall.text = "176"
hobby = ET.SubElement(person, "興趣")
hobby.text = "圍棋"
root.insert(0,person)
print(root[0].get('姓名'))        # Tsjeng

pretty_xml(root, '\t', '\n')      # xml資料縮排
# 建立tree物件，寫入檔案
tree = ET.ElementTree(root)
tree.write("tmp_newdata.xml", encoding="UTF-8")

print("------------------------------------------------------------")  # 60個

# xml_read.py

import xml.etree.cElementTree as ET

xml='''\
<?xml version="1.0"?>
<data 名稱="e-happy">
    <person 姓名="David">
        <身高>183</身高>
		<興趣>長跑</興趣>
    </person>
    <person 姓名="Chiou">
        <身高>170</身高>
		<興趣>籃球</興趣>
    </person>
</data>
'''

root = ET.fromstring(xml) # 從字串載入並解析 XML資料

person=root.find('person') 
print("find 方法：" + person[0].text)        # 183

persons = root.findall('person')
print("findall 方法：" + persons[1][1].text) # 籃球

persons=list(root.iter(tag='person'))        # iter 方法
for person in persons:
    print("tag:{}  attrib:{}" .format(person.tag,person.attrib))
    tall=person.find('身高').text
    hobby=person.find('興趣').text
    print("身高：{} 興趣：{}" .format(tall,hobby))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


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
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
