try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.parse('data.xml') # 從檔案載入並解析 XML資料

print('tree資料型別：', type(tree)) # <class 'xml.etree.ElementTree.ElementTree'>
root = tree.getroot()
print('root資料型別：', type(root)) # <class 'xml.etree.ElementTree.Element'>
print('根目錄標籤：' + root.tag)    # data
print('根目錄屬性：' + str(root.attrib)) # {'名稱': 'e-happy'}