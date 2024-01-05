# -*- coding: utf-8 -*-
"""
政府資料開放平臺 XML格式資料擷取與應用

"""
url="https://apiservice.mol.gov.tw/OdService/download/A17030000J-000047-mHA"

import urllib.request as ur

with ur.urlopen(url) as response:
    get_xml=response.read()
    

from bs4 import BeautifulSoup

data = BeautifulSoup(get_xml,'xml')
field1 = data.find_all('月別')
field2 = data.find_all('上市公司-家數')
field3 = data.find_all('上市公司-資本額')
field4 = data.find_all('上櫃公司-家數')
field5 = data.find_all('上櫃公司-資本額')

csv_str = ""
for i in range(0, len(field1)):
    csv_str += "{},{},{},{},{}\n".\
                format(field1[i].get_text(),\
                       field2[i].get_text(),\
                       field3[i].get_text(),\
                       field4[i].get_text(),\
                       field5[i].get_text())

with open("company.csv", "w") as f:
    story=f.write(csv_str)    #寫入檔案
    
print("XML格式資料已寫入company.csv")
