# ch14_9.py
fn = 'out14_9.txt'
string = 'I love Python.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(string)

