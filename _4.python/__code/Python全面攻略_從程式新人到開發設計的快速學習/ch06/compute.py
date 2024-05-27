# -*- coding: utf-8 -*-

def compute(r):
    return (4 / 3 * 3.1416 * r * r * r)

radius = int(input("請輸入球半徑(公分) :"))
volume = compute(radius)
print(f"球半徑 = {radius}公分  球體積 = {volume}立方公分")
