import sys



#練習 36 所得稅計算模組

# 以下為模組 \data\income_tax.py 的內容：

TAX_RATE = {
    0: 0.1,
    10000: 0.2,
    50000: 0.3,
    100000: 0.4,
    500000: 0.5
    }

def find_tax_rage(amount):
    result = 0.0
    for income, rate in TAX_RATE.items():
        if amount >= income:
            result = rate
    return result

def calculate_tax(amount):
    return amount * find_tax_rage(amount)

# 匯入 \data 下的模組

import sys

sys.path.append(r'.\data')

# 主程式

from income_tax import calculate_tax

print(calculate_tax(77000))



print('------------------------------------------------------------')	#60個




#練習 37 函式選單模組

# 以下為 \data\menu.py 檔的內容：

def menu(**options):
    def menu_selector():
        option_string = '/'.join(options)
        while True:
            choice = input(f'選擇項目 ({option_string}): ')
            if choice in options:
                return options[choice]
                break
            print('選項不存在!')
    return menu_selector

# 匯入 \data 下的模組

import sys

sys.path.append(r'.\data')

# 主程式
from menu import menu

def func_a():
    return '執行函式 A'

def func_b():
    return '執行函式 B'

def func_x():
    return '執行函式 X'

my_menu = menu(a=func_a, b=func_b, x=func_x)

func = my_menu()
print(func())

print('------------------------------------------------------------')	#60個




