import random   # 滙入亂數模組

# 使用三元運算子 X if C else Y
number = random.randint(0, 9) # 產生 0~9 數字
guess = eval(input('輸入一個0~9數字來猜一猜-> '))
print(f'數字{guess}猜對了' # 利用逗號來形成兩行
      if number == guess else '猜錯了')
