filename = 'C:/______test_files2/menu.xml'

import xml.etree.ElementTree as ET

tree = ET.ElementTree(file = filename) # 讀取xml檔案，獲取tree物件
root = tree.getroot() # 獲取root物件
print(root.tag) #列印root物件的tag屬性('menu')

#遍歷root物件child子節點列印tag與attrib屬性
for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
    #遍歷child節點的子節點列印tag與attrib屬性
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)

print(len(root)) # 菜單選項的數目
print(len(root[0])) # 早餐選項的數目



filename = 'C:/______test_files2/country_data.xml'

tree = ET.parse(filename) # 解析xml檔，回傳ElementTree物件。
root = tree.getroot() #獲得根節點
#列印根節點標籤名
print("coutry_data.xml的根節點："+root.tag)
# 列印根節點的屬性和屬性值
print("根節點標籤裡的屬性和屬性值："+str(root.attrib))
# 遍歷獲取子節點的標籤、屬性和屬性值
for child in root:
    print(child.tag, child.attrib)
# 獲取country標籤下的子標籤的內容
print("排名:"+root[0][0].text,"國內生產總值:"+root[0][2].text,)
# 把所有neighbor標籤找出來，並列印出標籤的屬性和屬性值。
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
# 使用findall()方法把滿足條件的標籤找出來反覆運算
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name,rank)



filename = 'C:/______test_files2/country_data.xml'

output_filename1 = 'C:/______test_files3/country_data_out1.xml'
output_filename2 = 'C:/______test_files3/country_data_out2.xml'

import xml.etree.ElementTree as ET
tree = ET.parse(filename) #解析xml檔，回傳ElementTree物件
root = tree.getroot() #獲得根節點
# 遍歷修改標籤，包括增加屬性和屬性值、修改屬性值、刪除標籤
for rank in root.iter("rank"):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set("updated","yes")
# 利用write()方法創建檔，並把xml寫入新的檔，同時指定寫入內容的編碼
tree.write(output_filename1, encoding="utf-8")


import xml.etree.ElementTree as ET
tree = ET.parse(filename) #解析xml檔，回傳ElementTree物件
root = tree.getroot() #獲得根節點
# 遍歷獲得滿足條件的元素，並使用remove()指定刪除
for country in root.findall('country'):
    rank=int(country.find("rank").text)
    if rank > 50:
        root.remove(country)
tree.write(output_filename2, encoding="utf-8")
# 利用write()方法創建檔，並把xml寫入新的檔，指定寫入內容的編碼




