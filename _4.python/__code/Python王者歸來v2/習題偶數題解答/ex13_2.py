# ex13_2.py
import MyMath

# 使用者輸入
print("請輸入運算")
print("1:加法")
print("2:減法")
print("3:乘法")
print("4:除法")
op = int(input("輸入1/2/3/4: "))
a = int(input("a = "))
b = int(input("b = "))

# 程式運算
if op == 1:
    print("a + b = ", MyMath.add(a, b))   # 輸出a-b字串和結果
elif op == 2:
    print("a - b = ", MyMath.sub(a, b))   # 輸出a-b字串和結果
elif op == 3:
    print("a * b = ", MyMath.mul(a, b))   # 輸出a*b字串和結果
elif op == 4:
    print("a / b = ", MyMath.div(a, b))   # 輸出a/b字串和結果
else:
    print("運算方法輸入錯誤")


