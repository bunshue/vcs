# ch14_25.py
fn = 'out14_25.txt'
string = 'I love Python.'

with open(fn, 'w') as file_Obj:
    print(file_Obj.write(string))

