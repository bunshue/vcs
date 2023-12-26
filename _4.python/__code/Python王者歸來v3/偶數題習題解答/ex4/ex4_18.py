# ex4_18.py
s = eval(input('請輸入數列起始值 : '))
e = eval(input('請輸入數列終點值 : '))
d = eval(input('請輸入數列的差值 : '))
sum = int((s + e) * ((e - s + d) / (2 * d)))
print(f'{s} 到 {e} 差值是 {d} 的數列總和是 {sum}')

