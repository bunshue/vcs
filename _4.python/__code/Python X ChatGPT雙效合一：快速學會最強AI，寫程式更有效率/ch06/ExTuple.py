tupleData = ()
listData = []

print("\n\n")

strFieldName = str(input("請輸入不可修改欄位名稱(逗號為分隔索引位置；頓號則為放置在同一個索引位置)："))
strFieldData = str(input("請輸入欄位對應資料(逗號為分隔索引位置；頓號則為放置在同一個索引位置)："))

for i in range(len(strFieldName.split(","))):
    listData.append(strFieldName.split(",")[i])
    
for j in range(len(strFieldData.split(","))):
    x = 0

    if len(listData)%2 == 0:
        x = len(listData) - 1
    else:
        x = len(listData) + 1
        
    listData.insert(x, [strFieldData.split(",")[j] for x in range(1)])
    
listToTuple = tuple(listData)
print("\n")
print("list轉換tuple：", listToTuple)
