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
