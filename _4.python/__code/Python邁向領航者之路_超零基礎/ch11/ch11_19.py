# ch11_19.py
def my_divmod(x, y):
    # 模擬divmod()
    a = x // y
    b = x % y
    return a, b

x = eval(input('請輸入被除數 : '))
y = eval(input('請輸入除數   : '))
rtn = my_divmod(x, y)
print('回傳多筆資料的形態 : {}'.format(type(rtn)))
print('商 = {},  餘數 = {}'.format(rtn[0], rtn[1]))





