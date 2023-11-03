def fun1(obj, price):
    obj = 'Microwave'
    print('函數內部修改字串及串列資料')
    print('物品名稱:', obj)
    #新增價格
    price.append(12000)
    print('物品售價:', price)

obj1 = 'TV'  #未呼叫函數前的字串
price1 = [24000, 18000, 35600] #未呼叫函數前的串列
print('函數呼叫前預設的字串及串列')
print('物品名稱:', obj1)
print('物品售價:', price1)
fun1(obj1, price1)

print('函數內部被修改過字串及串列:')
print('名字:', obj1) #字串內容沒變
print('分數:', price1) #串列內容已改變
