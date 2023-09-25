import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
tree = ET.fromstring(content.text)

print('根目錄標籤：' + tree.tag)
print('根目錄屬性：' + str(tree.attrib))
print('根目錄值：' + str(tree.text))
