"""
新的


"""

import os
import re
import sys


print("------------------------------------------------------------")  # 60個

# tree1.py

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

xml = """\
<?xml version="1.0"?>
<data 名稱="e-happy">
    <person 姓名="David">
        <身高>183</身高>
    </person>
</data>
"""

root = ET.fromstring(xml)  # 從字串載入並解析 XML資料
print("資料型別：", type(root))  # <class 'xml.etree.ElementTree.Element'>
print("根目錄標籤：" + root.tag)  # data
print("根目錄屬性：" + str(root.attrib))  # {'名稱': 'e-happy'}
print("根目錄值：" + str(root.text))  # 空字串
print("屬性內容：" + str(root.get("名稱")))  # e-happy
root.set("名稱", "文淵閣工作室")
print("屬性內容：" + str(root.get("名稱")))  # 文淵閣工作室

print("------------------------------------------------------------")  # 60個

# tree2.py

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.parse("data/data.xml")  # 從檔案載入並解析 XML資料

print("tree資料型別：", type(tree))  # <class 'xml.etree.ElementTree.ElementTree'>
root = tree.getroot()
print("root資料型別：", type(root))  # <class 'xml.etree.ElementTree.Element'>
print("根目錄標籤：" + root.tag)  # data
print("根目錄屬性：" + str(root.attrib))  # {'名稱': 'e-happy'}

print("------------------------------------------------------------")  # 60個

# xml_append.py

import xml.etree.cElementTree as ET

xml = """\
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
"""

root = ET.fromstring(xml)  # 從字串載入並解析 XML資料
person = ET.Element("person")  # 建立標籤 person
person.attrib = {"姓名": "Tsjeng"}  # 設定 person 標籤的屬性和資料
# 建立 person 的標籤，並新增屬性和資料
tall = ET.SubElement(person, "身高")
tall.text = "176"
hobby = ET.SubElement(person, "興趣")
hobby.text = "圍棋"
root.append(person)
print(root[2].get("姓名"))  # Tsjeng

print("------------------------------------------------------------")  # 60個

# xml_edit.py

import xml.etree.cElementTree as ET


def pretty_xml(element, indent, newline, level=0):
    if element:  # 判斷element是否有子元素
        if (element.text is None) or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = (
                newline
                + indent * (level + 1)
                + element.text.strip()
                + newline
                + indent * (level + 1)
            )
    temp = list(element)  # 將element轉成list
    for subelement in temp:
        if temp.index(subelement) < (
            len(temp) - 1
        ):  # 如果不是list的最後一個元素，表示下一行是同級别元素的起始，缩排應一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最後一個元素， 表示下一行是母元素的结束，缩排應該少一個
            subelement.tail = newline + indent * level
        pretty_xml(subelement, indent, newline, level=level + 1)  # 對子元素進行遞迴操作


xml = """\
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
"""

root = ET.fromstring(xml)  # 從字串載入並解析 XML資料
root[0].set("姓名", "鮭魚")
hobby = root[0].find("興趣")
hobby.text = "跑馬拉松"

root.remove(root[1])  # 刪除 root[1]
pretty_xml(root, "\t", "\n")  # xml資料縮排

tree = ET.ElementTree(root)  # 建立tree物件，寫入檔案
tree.write("tmp_newdata2.xml", encoding="UTF-8")

print("------------------------------------------------------------")  # 60個

# xml_insert.py

import xml.etree.cElementTree as ET

xml = """\
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
"""


def pretty_xml(element, indent, newline, level=0):
    if element:  # 判斷element是否有子元素
        if (element.text is None) or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = (
                newline
                + indent * (level + 1)
                + element.text.strip()
                + newline
                + indent * (level + 1)
            )
    temp = list(element)  # 將element轉成list
    for subelement in temp:
        if temp.index(subelement) < (
            len(temp) - 1
        ):  # 如果不是list的最後一個元素，表示下一行是同級别元素的起始，缩排應一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最後一個元素， 表示下一行是母元素的结束，缩排應該少一個
            subelement.tail = newline + indent * level
        pretty_xml(subelement, indent, newline, level=level + 1)  # 對子元素進行遞迴操作


root = ET.fromstring(xml)  # 從字串載入並解析 XML資料
person = ET.Element("person")  # 建立標籤 person
person.attrib = {"姓名": "Tsjeng"}  # 設定 person 標籤的屬性和資料
# 建立 person 的標籤，並新增屬性和資料
tall = ET.SubElement(person, "身高")
tall.text = "176"
hobby = ET.SubElement(person, "興趣")
hobby.text = "圍棋"
root.insert(0, person)
print(root[0].get("姓名"))  # Tsjeng

pretty_xml(root, "\t", "\n")  # xml資料縮排
# 建立tree物件，寫入檔案
tree = ET.ElementTree(root)
tree.write("tmp_newdata.xml", encoding="UTF-8")

print("------------------------------------------------------------")  # 60個

# xml_read.py

import xml.etree.cElementTree as ET

xml = """\
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
"""

root = ET.fromstring(xml)  # 從字串載入並解析 XML資料

person = root.find("person")
print("find 方法：" + person[0].text)  # 183

persons = root.findall("person")
print("findall 方法：" + persons[1][1].text)  # 籃球

persons = list(root.iter(tag="person"))  # iter 方法
for person in persons:
    print("tag:{}  attrib:{}".format(person.tag, person.attrib))
    tall = person.find("身高").text
    hobby = person.find("興趣").text
    print("身高：{} 興趣：{}".format(tall, hobby))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
