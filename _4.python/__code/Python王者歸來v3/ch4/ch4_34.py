# ch4_34.py
starting = 1
ending = 100
d = 1                       # 等差數列的間距
sum = int((starting + ending) * (ending - starting + d) / (2 * d))
print(f'1 到 100的總和是 {sum}')

