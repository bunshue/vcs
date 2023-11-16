# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"


from opencc import OpenCC
text1=u"我去过清华大学和交通大学，打印机、光盘、内存。"
text2=u"我去過清華大學和交通大學，印表機、光碟、記憶體。"

openCC = OpenCC('s2t')   
line = openCC.convert(text1) 
print("      "+text1)
print("s2t  :"+line)
line =openCC.set_conversion('s2twp')
line = openCC.convert(text1)
print("s2twp:"+line)

line =openCC.set_conversion('t2s')
line = openCC.convert(text2) 
print("      "+text2)
print("t2s  :"+line)
line =openCC.set_conversion('tw2sp')
line = openCC.convert(text2)
print("tw2sp:"+line)
