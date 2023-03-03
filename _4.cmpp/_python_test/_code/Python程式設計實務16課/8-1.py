# _*_ coding: utf-8 _*_
# 程式 8-1.py (Python 3 version)

fp = open("zop.txt", "r")
zops = fp.readlines()
fp.close()
i=1
print("The Zen of Python")
for zen in zops:
    print("Zen {}: {}".format(i, zen),end="")
    i += 1
