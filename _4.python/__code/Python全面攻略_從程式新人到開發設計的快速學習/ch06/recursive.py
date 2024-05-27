# -*- coding: utf-8 -*-
def fib(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))
    
i = int(input("請輸入欲顯示到第幾個費波南希係數："))
for x in range(1, i + 1):
    print(f"\t{fib(x)}", end = "")

