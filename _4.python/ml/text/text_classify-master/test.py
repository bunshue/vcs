# encoding='utf-8'
import sys
import os
import jieba
import chardet


# with open('C3-Art0002.txt') as file:
# 	content = file.read()
# 	print(chardet.detect(content))
# 	cod=chardet.detect(content)['encoding']
# 	print(cod)
# 	print(content.decode(cod))

f = open("C3-Art0002.txt", encoding="utf-8")
a = f.read()
f.close()
print(a)
