#!/usr/bin/env python
# -*- coding=utf-8 -*-
from xml.etree import ElementTree
import sys


#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Powen Ko, www.powenko.com"

import sys
from xml.etree import ElementTree
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x


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
