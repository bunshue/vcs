# -*- coding: utf-8 -*-
i = int(input("請輸入2020年1月1日是星期幾？"))
print("Sun.\tMon.\tTue.\tWed.\tThu.\tFri.\tSat.")
print("\t" * i, end='')
for x in range(1, 31 + 1):
    print(f"{x}\t", end='')
    if(i < 6):
        i += 1
    else:
        print()
        i = 0
