import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def get_current():
    ret = {}
    content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
    tree = ET.fromstring(content.text)  #解析XML
    items = list(tree.iter(tag='item'))  #取得item標籤內容
    title = items[0][0].text  #期別
    ret['title'] = title + '月'
    ptext = items[0][2].text  #中獎號碼
    ptext = ptext.replace('<p>','')
    plist = ptext.split('</p>')  
    for i in range(len(plist)-1):
        tlist = plist[i].split('：')
        ret[tlist[0]] = tlist[1]
    return ret




