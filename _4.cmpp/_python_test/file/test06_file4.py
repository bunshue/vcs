#!/usr/bin/python
# -*- coding: UTF-8 -*-    #告訴Python直譯器檔案編碼為UTF-8

#filename = raw_input('檔名：')
filename = "TestFileR.txt" 
f = open(filename, 'r')
b_str = f.read()
f.close()

print(b_str)

#print(b_str.decode('utf-8')) # 這是什麼？
#print(b_str.decode('utf-8').encode('utf-8')) # 這是什麼？
