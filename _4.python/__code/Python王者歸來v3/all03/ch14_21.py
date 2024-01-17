# ch14_21.py
fn = 'out14_21.txt'
str1 = 'I love Python.'
str2 = '洪錦魁著'

with open(fn, 'w', encoding='cp950') as fObj:
    fObj.write(str1)
    fObj.write(str2)







