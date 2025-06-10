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
tree.write("newdata2.xml", encoding="UTF-8")
