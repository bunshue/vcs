# ch14_22.py
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

fn = 'out14_22.txt'
size = len(zenofPython)
offset = 0
chunk = 100                         # 每次寫入的單位
with open(fn, 'w', encoding='cp950') as fObj:
    while True:
        if offset > size:
            break
        print(fObj.write(zenofPython[offset:offset+chunk]))
        offset += chunk




