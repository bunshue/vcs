# ex5_2.py
r = 20
x, y  = eval(input("請輸入點座標 : "))

if dist := (x * x + y * y) ** 0.5 > r:
    print(f"點座標 {str(x)}, {str(y)} 不在圓內部")
else:
    print(f"點座標 {str(x)}, {str(y)} 在圓內部")



