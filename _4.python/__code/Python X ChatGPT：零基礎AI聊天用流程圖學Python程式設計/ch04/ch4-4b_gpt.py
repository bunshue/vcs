# 輸入三角形的三個邊長a、b、c
a = float(input("請輸入三角形邊長a: "))
b = float(input("請輸入三角形邊長b: "))
c = float(input("請輸入三角形邊長c: "))

# 利用海龍公式計算半周長
s = (a + b + c) / 2

# 利用海龍公式計算三角形面積
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# 輸出結果
print("三角形面積 = ", area)
