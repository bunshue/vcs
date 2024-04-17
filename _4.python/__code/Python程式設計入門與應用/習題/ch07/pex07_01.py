# Filename: pex07_01.py
pnum = ["055","816","292","891","491","437"]
pno = input("請輸入中獎者的號碼：")
pisfound=False
for i in range(len(pnum)):
    if (pnum[i]==pno):
        pisfound=True
        break
if (pisfound==True):
    print("中獎者的號碼為：",pnum[i])
else:
    print("抱歉，無此中獎號碼!")