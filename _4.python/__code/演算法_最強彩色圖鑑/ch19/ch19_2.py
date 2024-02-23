# ch19_2.py
from collections import deque

def palindrome(word):
    wd = deque(word)
    while len(wd) > 1:
        if wd.pop() != wd.popleft():
            return False
    return True

print('x      是回文 : ', palindrome("x"))
print('abccba 是回文 : ', palindrome("abccba"))
print('radar  是回文 : ', palindrome("radar"))
print('python 是回文 : ', palindrome("python"))








 









