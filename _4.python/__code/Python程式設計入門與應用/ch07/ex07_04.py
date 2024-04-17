# Filename: ex07_04.py
# 循序搜尋
pdata = [128,246,732,945,489,242,647,819,935,767]
no = int(input("請輸入搜尋的編號(3位數字):"))
isfound=False
for i in range(len(pdata)):
    if (pdata[i]==no):
        isfound=True
        break
if (isfound==True):
    print("第%d個編號，編號為%d:"%(i+1,pdata[i]))
else:
    print("無此數字!")
print("共比對%d次"%(i+1))