# ch7_44.py
print("電影院劃位系統")
sc = [[' ', ' 1', ' 2', ' 3', ' 4'],
      ['A', '□','□','□','□'],
      ['B', '■','□','□','□'],
      ['C', '□','■','■','□'],
      ['D', '□','□','□','□'],
     ]
for seatrow in sc:          # 輸出目前座位表
    for seat in seatrow:
        print(seat, end='  ')
    print()
row = input("請輸入 A - D 排 : ")
r = int(row,16) - 9
col = int(input("請輸入 1 - 4 號 : "))
sc[r][col] = '■'
print("="*60)
for seatrow in sc:          # 輸出最後座位表
    for seat in seatrow:
        print(seat, end='  ')
    print()







