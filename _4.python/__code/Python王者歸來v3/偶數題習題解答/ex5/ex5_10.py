# ex5_10.py
a, b, c, d, e, f = eval(input("請輸入線性方程式的係數 : "))
flag = a*d - b*c

if flag == 0:
    print("此線性方程式沒有解答")
else:
    x = (e*d - b*f) / (a*d - b*c)
    y = (a*f - e*c) / (a*d - b*c)
    print(f"{x = :6.4f},    {y = :6.4f}")







    


    







