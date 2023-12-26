# ch9_8_2.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
var = input("請輸入要刪除的字典變數 : ")
if var in locals():
    var = eval(var)
    if isinstance(var, dict):
        print(f"'fruits' 字典變數存在")
        del fruits
        print(f"刪除字典變數成功")
    else:
        print(f"字典變數不存在")
else:
    print(f"{var} 變數不存在")

   
