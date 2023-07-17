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