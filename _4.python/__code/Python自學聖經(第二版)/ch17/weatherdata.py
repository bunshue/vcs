import requests
try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

user_key = "氣象局授權碼"
doc_name = "F-C0032-001"

api_link = "http://opendata.cwb.gov.tw/opendataapi?dataid=%s&authorizationkey=%s" % (doc_name,user_key)
report = requests.get(api_link).text
# print(report)
xml_namespace = "{urn:cwb:gov:tw:cwbcommon:0.1}"
root = et.fromstring(report)
dataset = root.find(xml_namespace + 'dataset')
locations_info = dataset.findall(xml_namespace + 'location')
# 取得 <location> Elements,每個 location 就表示一個縣市資料
location = '高雄市'
target_idx = -1
for idx,ele in enumerate(locations_info):
    locationName = ele[0].text # 取得縣市名
    if locationName == location:  #找到要查詢的縣市
        target_idx = idx
        break
if target_idx != -1:
    show = ''
    tlist = ['天氣狀況', '最高溫', '最低溫', '舒適度', '降雨機率']
    for i in range(5):
        element = locations_info[target_idx][i+1]  #取得weatherElement
        timeblock = element[1] # 取出目前時間點的資料
        data = timeblock[2][0].text
        show = show + tlist[i] + '：' + data + '\n'
    print(show)
else:
    print('無此縣市資料！')
    