# ch9_32.py
person = {'name':'John'}
print("原先字典內容", person)

# 'age'鍵不存在
age = person.setdefault('age')
print("增加age鍵 ", person)
print("age = ", age)

# 'sex'鍵不存在
sex = person.setdefault('sex', 'Male')
print("增加sex鍵 ", person)
print("sex = ", sex)



