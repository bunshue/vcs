# ch14_28.py
fn = 'out14_28.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(str1)
    file_Obj.write(str2)



