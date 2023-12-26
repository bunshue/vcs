# ch9_31.py
person = {'name':'John'}
print("原先字典內容", person)

# 'age'鍵不存在
age = person.setdefault('age')
print(f"增加age鍵 {person}")
print(f"age = {age}")
# 'sex'鍵不存在
sex = person.setdefault('sex', 'Male')
print(f"增加sex鍵 {person}")
print(f"sex = {sex}")



