# Filename: pex05_13.py
def DtoS(num,ctype):
    presult=""
    while(num!=0):
        pdata=str(num%ctype)
        presult="".join([pdata,presult])
        num=num//ctype
    return(presult)

pnum = int(input("請輸入要轉換的十進位數字:"))
ptype = int(input("請輸入要轉換的進位系統(2,8):")) 
strl=DtoS(pnum,ptype)
print(strl)