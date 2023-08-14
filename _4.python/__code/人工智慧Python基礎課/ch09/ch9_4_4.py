# coding: utf-8
fp = open("temp\\note.txt", "r")
str1 = fp.read(1)
str2 = fp.read(5)
print(str1, str2)
fp.close()
