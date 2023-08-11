import os
import sys
import time

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('尋找python程式碼的所在地')

module_name = 'pytube'
code_place = os.path.dirname(__import__(module_name).__file__)
print(code_place)


print('取得相對路徑')
foldername = 'C:/_git/vcs/_1.data/______test_files1/'
fn = os.path.relpath(foldername, code_place)

print(fn)

print('------------------------------')  #30個

def test():
    for x in 'abcde':
        for y in '12345':
            print(y, x, end = ' ')

test()
print('------------------------------')  #30個


ENDMARKER = 0
NAME = 1
NUMBER = 2
STRING = 3
NEWLINE = 4
INDENT = 5
DEDENT = 6
LPAR = 7
RPAR = 8
LSQB = 9
RSQB = 10
PERCENT = 24
LBRACE = 25
RBRACE = 26
EQEQUAL = 27
N_TOKENS = 54
NT_OFFSET = 256

tok_name = {value: name
            for name, value in globals().items()
            if isinstance(value, int) and not name.startswith('_')}

print(type(tok_name))
print(tok_name)


print('------------------------------')  #30個


import os
print(os.name)
print(os.name)
print(os.name)

if os.name == 'nt':
    print('kkk')
    import nt
    if sys.getwindowsversion()[:2] >= (6, 0):
        print('aaa')
    else:
        print('bbb')



print('------------------------------')  #30個

import socket
hostname = socket.gethostname()
print('取得 hostname :', hostname)

path = 'cccc'
print('%s.%s.%s.%s' % (path, int(time.time()),
                       socket.gethostname(),
                       os.getpid()))

print('------------------------------')  #30個


print('------------------------------')  #30個


