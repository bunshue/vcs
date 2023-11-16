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
