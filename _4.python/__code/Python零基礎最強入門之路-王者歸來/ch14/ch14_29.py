# ch14_29.py
fn = 'out14_29.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(str1)
    file_Obj.write(str2)



