"""
政府資料開放平臺 XML格式資料擷取與應用

"""
url="https://apiservice.mol.gov.tw/OdService/download/A17000000J-000007-yrg"

import urllib.request as ur

with ur.urlopen(url) as response:
    get_xml=response.read()
    

from bs4 import BeautifulSoup

data = BeautifulSoup(get_xml,'xml')
HandlingUnit = data.find_all('辦理單位')
ContactPerson = data.find_all('聯絡人')
DuringTraining = data.find_all('訓練期間')
ContactNumber = data.find_all('聯絡電話')
CourseTitle = data.find_all('課程名稱')


csv_str = ""
for i in range(0, len(HandlingUnit)):
    csv_str += "{},{},{},{},{}\n".\
                format(HandlingUnit[i].get_text(),\
                       ContactPerson[i].get_text(),\
                       ContactNumber[i].get_text(),\
                       DuringTraining[i].get_text(),\
                       CourseTitle[i].get_text())

with open("course_xml.csv", "w") as f:
    story=f.write(csv_str)    #寫入檔案
    
print("XML格式資料擷取與應用,已將資料寫入course_xml.csv")

