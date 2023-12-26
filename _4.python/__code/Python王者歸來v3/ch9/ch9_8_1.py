# ch9_8_1.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
var_dict = input("請輸入要刪除的變數 : ")
if var_dict in locals():    # 檢查變數是否存在
    print(f"{var_dict} 變數存在")
    del fruits
    print(f"刪除 {var_dict} 變數成功")
else:
    print(f"{var_dict} 變數不存在")


   
