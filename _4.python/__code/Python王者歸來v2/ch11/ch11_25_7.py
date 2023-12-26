# ch11_25_7.py
def outer():
    b = 10                  # inner所使用的變數值
    def inner(x):
        return 5 * x + b    # 引用第3行的b
    return inner

b = 2
f = outer()
print(f(b))





















