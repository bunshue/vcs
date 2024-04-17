# Filename: pex05_06.py
pnum = int(input("請輸入要轉換的十進位數字:"))
presult=""
while(pnum!=0):
    pdata=str(pnum%2)
    presult="".join([pdata,presult])
    pnum=pnum//2
print("轉換為二進位數字為:%s"%presult)