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