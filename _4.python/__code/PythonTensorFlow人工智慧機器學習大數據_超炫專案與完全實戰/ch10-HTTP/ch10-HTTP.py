import sys 
import urllib.request as httplib

try:
    url="http://www.powenko.com/download_release/get.php?name=powenko"
    #url="http://data.taipei/opendata/datalist/datasetMeta/download?id=5bc82dc7-f2a2-4351-abc8-c09c8a8d7529&rid=1f1aaba5-616a-4a33-867d-878142cac5c4"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents=reponse.read().decode(reponse.headers.get_content_charset())
        else:  
        	contents=reponse.read()   
        print(contents)
except:
    print("error")

print('------------------------------------------------------------')	#60個

import sys
import urllib.request as httplib

try:

    url="http://data.taipei/opendata/datalist/datasetMeta/download?id=5bc82dc7-f2a2-4351-abc8-c09c8a8d7529&rid=1f1aaba5-616a-4a33-867d-878142cac5c4"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents=reponse.read().decode(reponse.headers.get_content_charset())
        else:  
        	contents=reponse.read()   
        print(contents)
except:
    print("error")   

print('------------------------------------------------------------')	#60個

import sys
import urllib.request as httplib
import urllib

try:
    url="http://www.powenko.com/download_release/post.php"
    values={'name':'powenko','password':123}
    if (sys.version_info < (3, 0)):       # python 2.x
        data = urllib.urlencode(values)
        req = httplib.Request(url, data)
        reponse = httplib.urlopen(req)
        if reponse.code == 200:
            contents=reponse.read()
    else:
        data = urllib.parse.urlencode(values)      # python 3.x
        data = data.encode('utf-8')  # data should be bytes
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            contents = response.read().decode(response.headers.get_content_charset())
    print(contents)
except:
    print("error")   

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch10-HTTP\04XML.py

#!/usr/bin/env python
# -*- coding=utf-8 -*-
from xml.etree import ElementTree
import sys

def print_node(node):
    print("==============================================")
    print("node.attrib:%s" % node.attrib)
    #if node.attrib.has_key("age") > 0 :
    try:
       print("node.attrib['age']:%s" % node.attrib['age'])
    except:
       print("node.attrib['age']:null")
    print("node.tag:%s" % node.tag)
    try:
       print("node.text:%s" % node.text)
    except:
       print("node.text:null")

xml2text="""<?xml version="1.0" encoding="utf-8"?>
<root>
 <person age="18">
    <name>Powen Ko</name>
    <sex>man</sex>
 </person>
 <person age="19" des="hello">
    <name>kiki</name>
    <sex>female</sex>
 </person>
</root>"""


# 加载XML文件（2种方法,一是加载指定字符串，二是加载指定文件）
root = ElementTree.fromstring(xml2text)

# 获取element的方法
# 1 通过getiterator
lst_node = root.getiterator("person")
for node in lst_node:
    print_node(node)

# 2通过 getchildren
if (sys.version_info > (3, 0)):
   print(" No getchildren API")
else:
   lst_node_child = lst_node[0].getchildren()[0]
   print_node(lst_node_child)

# 3 .find方法
node_find = root.find('person')
print_node(node_find)

# 4. findall方法
node_findall = root.findall("person/name")[1]
print_node(node_findall)

print('------------------------------------------------------------')	#60個

import sys 
from xml.etree import ElementTree
import urllib.request as httplib

def print_node(node):
    try:
       print("node.text:%s" % node.text)
    except:
       print("node.text:null")


try:
    url="http://data.taipei/opendata/datalist/datasetMeta/download?id=ece023db-a5f8-4399-97da-f04d7f4009e3&rid=1a2d417e-c121-4a12-835f-97ee6852c4b8"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents=reponse.read().decode(reponse.headers.get_content_charset())
        else:  
            contents=reponse.read()

        print(contents)
        print_node(contents)
        root = ElementTree.fromstring(contents)
        lst_node = root.findall("MAP/PERSON_IN_CHARGE")
        #lst_node = root.findall("MAP/ADDRESS")
        #lst_node = root.findall("MAP/PHO        #lst_node = root.findall("MAP/ADDRESS")
        #lst_node = root.findall("MAP/PHONE")NE")
        for node in lst_node:
            print_node(node)
except:
    print("error")

print('------------------------------------------------------------')	#60個

import sys 
from xml.etree import ElementTree

import urllib.request as httplib

def print_node(node):
    try:
       print("node.text:%s" % node.text)
    except:
       print("node.text:null")

try:
    url="http://data.taipei/opendata/datalist/datasetMeta/download?id=ece023db-a5f8-4399-97da-f04d7f4009e3&rid=1a2d417e-c121-4a12-835f-97ee6852c4b8"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents=reponse.read().decode(reponse.headers.get_content_charset())
        else:  
            contents=reponse.read()

        print(contents)
        print_node(contents)
        root = ElementTree.fromstring(contents)
        #lst_node = root.findall("MAP/PERSON_IN_CHARGE")
        #lst_node = root.findall("MAP/ADDRESS")
        #lst_node = root.findall("MAP/PHONE")
        #for node in lst_node:
        #    print_node(node)

        MAP = root.findall("MAP")
        for root3 in MAP:
            # print_node(node)
            ADDRESS = root3.findall("ADDRESS")
            LAT = root3.findall("LAT")
            LON = root3.findall("LON")
            print("ADDRESS:%s   LAT:%s  LON:%s " % (ADDRESS[0].text, LAT[0].text,LON[0].text))


except:
    print("error")

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch10-HTTP\05HTTP_GET_XML_OpenData-weather.py

#!/usr/bin/env python
# -*- coding=utf-8 -*-
from xml.etree import ElementTree
import sys

import sys
from xml.etree import ElementTree
import urllib.request as httplib

def print_node(node):
    try:
       print("node.text:%s" % node.text)
    except:
       print("node.text:null")


try:
    url="http://data.taipei/opendata/datalist/datasetMeta/download?id=ece023db-a5f8-4399-97da-f04d7f4009e3&rid=1a2d417e-c121-4a12-835f-97ee6852c4b8"
    url = "http://data.taipei/opendata/datalist/datasetMeta/download?id=5bc82dc7-f2a2-4351-abc8-c09c8a8d7529&rid=1f1aaba5-616a-4a33-867d-878142cac5c4"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents=reponse.read().decode(reponse.headers.get_content_charset())
        else:
            contents=reponse.read()

        contents = contents.replace('<cwbopendata xmlns="urn:cwb:gov:tw:cwbcommon:0.1">', '<cwbopendata>')
        #print(contents)
        #print_node(contents)
        root = ElementTree.fromstring(contents)
        #lst_node = root.findall("MAP/PERSON_IN_CHARGE")
        #lst_node = root.findall("MAP/ADDRESS")

        node_find = root.find('sender')
        print_node(node_find)


        lst_node = root.findall("dataset/locations/location/locationName")
        for node in lst_node:
            print_node(node)

        lst_node = root.findall("dataset/locations/location/weatherElement/time/elementValue/value")
        for node in lst_node:
            print_node(node)



        root2 = root.findall("dataset/locations/location")
        for root3 in root2:
            #print_node(node)
            root3_locationName = root3.findall("locationName")
            root3_dataTime = root3.findall("weatherElement/time/dataTime")
            root3_value= root3.findall("weatherElement/time/elementValue/value")
            print("地區:%s   溫度:%s  時間:%s " % (root3_locationName[0].text,root3_value[0].text,root3_dataTime[0].text))


except:
    print("error")

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch10-HTTP\06JSON.py

#!/usr/bin/env python
# coding=utf8
import json

data = {
    'name' : 'Powen Ko',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)
print(json_str)
data = json.loads(json_str)
print(data)
print(data['name'])

with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)


print('------------------------------------------------------------')	#60個

import json
import sys
import urllib.request as httplib
import ssl
import urllib.request

url="https://parks.taipei/parks/api/"

req=httplib.Request(url)
try:
    context = ssl._create_unverified_context()
    reponse = httplib.urlopen(url, context=context)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
                contents=reponse.read().decode(reponse.headers.get_content_charset())
                contents=contents.replace("\r\n", "")
                print(contents)
        else:  
                contents=reponse.read()   
        data = json.loads(contents)
        for data2 in data:
            print(data2['pm_name'],data2['pm_location'])
except:                                                                 #  處理網路連線異常
    print("error")   

print('------------------------------------------------------------')	#60個

"""
Mac 的使用者　如果出現　SSL Certificate Error
請執行以下的程式，HTTPS 就能工作
/Applications/python 3.6/Install Certificates.command
"""

import json
import sys
import urllib.request as httplib
import ssl

context = ssl._create_unverified_context()

url="http://data.taipei/opendata/datalist/datasetMeta/download?id=ea732fb5-4bec-4be7-93f2-8ab91e74a6c6&rid=bf073841-c734-49bf-a97f-3757a6013812"
url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
req=httplib.Request(url)
try:
    reponse = httplib.urlopen(req, context=context)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents = reponse.read();
        else:
            contents = reponse.read()
        data = json.loads(contents)
        print(data["retVal"]["2001"]["sna"])
        for x in range(2001,2100):
            print(data["retVal"][str(x)]["sna"])
except:                                                                 #  處理網路連線異常
    print("error")   

print('------------------------------------------------------------')	#60個



