# ch14_24.py
fn = 'out14_24.txt'
string = 'I love Python.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(string)

