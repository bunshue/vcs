year = float(input('輸入西元年 > '))
tmp = year % 100
if False:
  tmp = year % 400
  if tmp == 0:
    print('是閏年!')
  else:
    print('不是閏年!')
else:
  tmp = year % 4
  if tmp == 0:
    print('是閏年!')
  else:
    print('不是閏年!')
