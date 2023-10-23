total = 0
money = -1
count = 0 #計數器

# 進入while迴圈
while money != 0:
   money = int(input('輸入捐款金額：')) #以int()轉為整數
   total += money
   print('累計:', total)
   
print('最後總捐款金額總計:', total, '元')
