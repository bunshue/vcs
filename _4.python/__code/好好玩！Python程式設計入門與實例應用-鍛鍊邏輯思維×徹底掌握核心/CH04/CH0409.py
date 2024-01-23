# 兩個數值的區間累加

total = 0

count, number = eval(input('輸人兩個數值做區間累加 -> '))
#print('數值', count, end = '')

while count <= number:
   total += count   # 儲存累加值
   print(count, total)
   count += 1       # 計數器
   
else:
   #print(' ~', number, '累計: ', total)
   #print('結束廻圈...')
   pass
   

