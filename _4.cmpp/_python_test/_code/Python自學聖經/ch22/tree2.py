import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
tree = ET.fromstring(content.text)

item = tree[0].find('item')
print('find 方法：' + item[0].text)

items = tree[0].findall('item')
print('findall 方法：' + items[0][0].text)

items = list(tree.iter(tag='item'))
print('iter 方法：' + items[0][0].text)

