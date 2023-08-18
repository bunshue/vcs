# ch9_23.py
# key在字典內
fruits = {'Apple':20, 'Orange':25}
ret_value = fruits.setdefault('Orange')
print("Value = ", ret_value)
print("fruits字典", fruits)
ret_value = fruits.setdefault('Orange',100)
print("Value = ", ret_value)
print("fruits字典", fruits)


