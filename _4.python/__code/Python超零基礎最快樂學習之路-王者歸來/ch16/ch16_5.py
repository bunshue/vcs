# ch16_5.py
def sequentialSearch(nDict):
    for i in nDict.keys():
        if i == key:            # 找到了
            return i            # 傳回索引值
    return -1                   # 找不到傳回-1

employee = {19:'John',
            32:'Tom',
            28:'Kevin',
            99:'Curry',
            10:'Peter',
           }
key = int(input("請輸入得獎號碼 : "))
rtn = sequentialSearch(employee)
if rtn != -1:
    print("得獎者是 : ", employee[rtn])
else:
    print("我們小組沒人獲獎")





        





