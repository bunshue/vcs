# ch19_11.py
x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
mean = sum(x) / len(x)

# 計算變異數
myvar = 0
for v in x:
    myvar += ((v - mean)**2)
myvar = myvar / len(x)
print(f"變異數 : {myvar}")

