# ch4_15.py
h = int(input("請輸入頭的數量："))
f = int(input("請輸入腳的數量："))
chicken = int(f / 2 - h)
rabbit = int(2 * h - f / 2)
print('雞有 {} 隻, 兔有 {} 隻'.format(chicken, rabbit))


