# ch11_46.py
def create_multiplier(multiplier):
    def multiplier_function(number):
        return number * multiplier

    return multiplier_function

# 建立一個將數字乘以2的函數
double_function = create_multiplier(2)

# 使用返回的函數
result = double_function(5)             # 返回值是 10
print(result)                           # 輸出: 10

# 建立一個將數字乘以3的函數
triple_function = create_multiplier(3)

# 使用返回的函數
result = triple_function(5)             # 返回值是 15
print(result)                           # 輸出: 15


