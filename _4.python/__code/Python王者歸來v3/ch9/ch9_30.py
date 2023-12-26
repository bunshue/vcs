# ch9_30.py
# key在字典內
my_dict = {'apple': 1, 'banana': 2}

# 使用 setdefault() 獲取 'apple' 的值
value1 = my_dict.setdefault('apple', 0)
print(value1)  

# 使用 setdefault() 獲取 'orange' 的值
value2 = my_dict.setdefault('orange', 3)
print(value2)  

# 輸出更新後的字典
print(my_dict)  


