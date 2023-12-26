# ch7_42.py
chicken = 0
while True:
    rabbit = 35 - chicken                       # 頭的總數
    if 2 * chicken + 4 * rabbit == 100:         # 腳的總數
        print(f'雞有 {chicken} 隻, 兔有 {rabbit} 隻')
        break
    chicken += 1




