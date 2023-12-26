# ch12_22.py
def getMax(x, y):
    '''文件字串實例
建議x, y是整數
這個函數將傳回較大值'''
    if int(x) > int(y):
        return x
    else:
        return y

print(getMax(2, 3))         # 列印較大值
print(getMax.__doc__)       # 列印文件字串docstring

