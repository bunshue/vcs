# 九九乘法表的雙重迴圈
for i in range(1,10):
    for j in range (1,10):
        print('{0}*{1}={2:2d}  '.format(i,j,i*j), sep='\t',end='')
        if j>=7:
            break #設定跳出的條件
    print('\n-------------------------------------------------------\n')
