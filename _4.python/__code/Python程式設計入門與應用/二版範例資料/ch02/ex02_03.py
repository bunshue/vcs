# Filename: ex02_03.py
# coding=utf-8
# input 輸入命令
pvalue = int(input("請輸入半徑:"))
result1 = pvalue*pvalue*3.14
result2 = 2*pvalue*3.14
print("當半徑為%d時，圓面積為%6.2f，圓周長為%6.2f"%(pvalue, result1, result2))