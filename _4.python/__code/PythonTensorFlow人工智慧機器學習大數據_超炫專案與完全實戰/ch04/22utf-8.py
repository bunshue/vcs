#!/usr/bin/env
# -*- coding:utf-8  -*-
__author__ = "Powen Ko, www.powenko.com"

try:            #python 3.x
   name= input("名字:")
   print(" 你好! " + name)
except:         #python 2.x
   name= raw_input("名字:").decode("utf-8")
   nameutf8 = unicode(name).encode('utf-8')
   print(" 你好! " + nameutf8)
