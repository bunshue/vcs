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