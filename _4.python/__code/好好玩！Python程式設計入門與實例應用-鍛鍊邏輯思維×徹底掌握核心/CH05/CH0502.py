import math   # 滙入數學模組

radius = int(input('請輸入圓形半徑-> '))

# if/else敘述
if radius < 0:   # 半徑小於零顯示錯誤訊息
    print('輸入錯誤!!')
else:            # 半徑大於零才算出圓面積
    area = radius * radius * math.pi
    print('圓形面積：', area)
