# 新增
def fnCreate():
    uid = input("編號：")
    if uid in dictProduct:
        print('編號重複，無法新增產品記錄')
        return   
    name = input("品名：")
    price = int(input("單價："))
    newProduct = {uid:[name,price]}
    dictProduct.update(newProduct)
    print("產品新增成功!")
# 修改
def fnUpdate():
    uid = input("編號：")
    if uid not in dictProduct:
        print('無此編號，無法修改產品記錄')
        return   
    name = input("品名：")
    price = int(input("單價："))
    dictProduct[uid]=[name,price]
    print(dictProduct)
    print("產品修改成功!")
# 刪除
def fnDelete():
    uid = input("編號：")
    if uid not in dictProduct:
        print('無此編號，無法刪除產品記錄')
        return 
    dictProduct.pop(uid)
    print("產品刪除成功!")    
# 依編號查詢產品
def fnGetProductById():
    uid = input("編號：")
    if uid not in dictProduct:
        print('查無此編號')
        return     
    print("編號\t品名\t單價")
    print("%s\t%s\t%d" %(uid, dictProduct[uid][0], dictProduct[uid][1]))
# 將所有產品列出
def fnGetProductList():
    print("編號\t品名\t單價")
    listKey = dictProduct.keys()
    for uid in listKey:
        print("%s\t%s\t%d" %(uid, dictProduct[uid][0], dictProduct[uid][1]))
      
# 主程式
dictProduct={}
print("======= DTC產品管理系統 =======")
while True:
   option=int(input('系統功能->1.新增 2.修改 3.刪除 4.查詢 5.產品列表 其他.離開：'))
   if option==1:
       fnCreate()
   elif option==2:
       fnUpdate()
   elif option==3:
       fnDelete()
   elif option==4:
       fnGetProductById()
   elif option==5:
       fnGetProductList()
   else:
       print("離開系統")
       break;
