# break敘述中斷廻圈的執行
print('數值：', end ='')
result = 0
for x in range(1, 11):
    result = x**2
    #如果result的值大於就中斷廻圈的執行
    if result > 20:
        break
    print(result, end = ', ')
