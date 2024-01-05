url="https://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx?FOTT=Xml"

import urllib.request as ur

with ur.urlopen(url) as response:
    get_xml=response.read()
    

from bs4 import BeautifulSoup

data = BeautifulSoup(get_xml,'xml')
field1 = data.find_all("交易日期")
field2 = data.find_all("種類代碼")
field3 = data.find_all("作物代號")
field4 = data.find_all("作物名稱")
field5 = data.find_all("市場代號")
field6 = data.find_all("市場名稱")
field7 = data.find_all("上價")
field8 = data.find_all("中價")
field9 = data.find_all("下價")
fieldA = data.find_all("平均價")
fieldB = data.find_all("交易量")

csv_str = ""
for i in range(0, len(field1)):
    csv_str += "{},{},{},{},{},{},{},{},{},{},{}\n".\
                format(field1[i].get_text(),\
                       field2[i].get_text(),\
                       field3[i].get_text(),\
                       field4[i].get_text(),\
                       field5[i].get_text(),\
                       field6[i].get_text(),\
                       field7[i].get_text(),\
                       field8[i].get_text(),\
                       field9[i].get_text(),\
                       fieldA[i].get_text(),\
                       fieldB[i].get_text())

with open("product.csv", "w") as f:
    result=f.write(csv_str)    #寫入檔案
    
print("資料已寫入product.csv")
