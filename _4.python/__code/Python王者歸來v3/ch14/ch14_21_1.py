# ch14_21_1.py
fn = 'out14_21_1.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'a') as file_Obj:
    file_Obj.write(str1 + '\n')
    file_Obj.write(str2 + '\n')



