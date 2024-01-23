# for/in廻圈配合range()函式做數值累加

total = 0 # 儲存加總結果
count = 0 # 計數器
for count in range(1, 11): # 數值1~10
   total += count          # 將數值累加
   print('累加值', total)   # 觀看累加結果
else:
   print('數值累加完畢...')
   
