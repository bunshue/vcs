def GetMax(ary):
    maxNum = ary[0];
    index=0
    for i in range(len(ary)):
        if (maxNum < ary[i]) :
            index = i
            maxNum = ary[index]
    return index
            

listName=["阿才肉乾","恐龍餅乾","快樂汽水","天天豆干"]
listPrice=[70, 230, 400, 240]    

for i in range(len(listName)):
    print("%s %d" %(listName[i], listPrice[i]))
print()
n = GetMax(listPrice)
print("最貴產品：%s, 單價：%d" %(listName[n], listPrice[n]))

