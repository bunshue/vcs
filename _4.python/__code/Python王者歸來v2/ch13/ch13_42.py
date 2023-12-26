# ch13_42.py
from collections import deque

def palindrome(word):
    wd = deque(word)
    while len(wd) > 1:
        if wd.pop() != wd.popleft():
            return False
    return True

print(palindrome("x"))
print(palindrome("abccba"))
print(palindrome("radar"))
print(palindrome("python"))


















