# -*- coding: utf-8 -*-
x = int(input("請輸入小於12的正整數："))
for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(f"{i * j}\t", end="")
    print()

