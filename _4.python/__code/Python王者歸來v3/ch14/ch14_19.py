# ch14_19.py
fn = 'out14_19.txt'
string = 'I love Python.'

with open(fn, 'w', encoding='cp950') as fObj:
    print(fObj.write(string))







