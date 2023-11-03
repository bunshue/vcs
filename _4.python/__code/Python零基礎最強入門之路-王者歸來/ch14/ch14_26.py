# ch14_26.py
fn = 'out14_26.txt'
string = 'I love Python.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(string)

