# ch14_31.py
zenofPython = '''Beautiful is better than ugly.
Explicit is better than implicits.
Simple is better than complex.
Flat is better than nested.
Sparse is better than desse.
Readability counts.
Special cases aren't special enough to break the rules.
...
...
By Tim Peters'''

fn = 'out14_31.txt'
size = len(zenofPython)
offset = 0
chunk = 100
with open(fn, 'w') as file_Obj:
    while True:
        if offset > size:
            break
        print(file_Obj.write(zenofPython[offset:offset+chunk]))
        offset += chunk



