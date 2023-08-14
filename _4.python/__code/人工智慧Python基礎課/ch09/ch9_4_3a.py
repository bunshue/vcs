# coding: utf-8
fp = open("temp\\note.txt", "r")
lst1 = fp.readlines()
print(lst1)
for line in lst1:
    print(line, end="")
fp.close()