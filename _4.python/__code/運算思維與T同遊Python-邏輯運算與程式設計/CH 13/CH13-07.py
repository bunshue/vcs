#CH13-07  指令：round
k = 0.05
for i in range(1, 10):
    i = k+i/10 
    j= round(i, 1)
    print(i, j)
print('+')

