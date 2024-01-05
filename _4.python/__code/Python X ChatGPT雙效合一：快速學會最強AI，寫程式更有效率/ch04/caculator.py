a=float(input("請輸入a:"))
b=float(input("請輸入b:"))
op_key=input("請輸入+,-,*,/鍵：")#輸入字元並存入變數op_key
if op_key=='+': #如果op_key等於'+'
    print("{} {} {} = {}".format(a, op_key, b, a+b))
elif op_key=='-': #如果op_key等於'-'
    print("{} {} {} = {}".format(a, op_key, b, a-b))
elif op_key=='*': #如果op_key等於'*'
    print("{} {} {} = {}".format(a, op_key, b, a*b))
elif op_key=='/': #如果op_key等於'/'
    print("{} {} {} = {}".format(a, op_key, b, a/b))
else: #如果op_key不等於 + - * / 任何一個
    print("運算式有誤")
