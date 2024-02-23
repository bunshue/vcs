# ch19_2.py
from collections import deque

def palindrome(word):
    return word == word[::-1]

wd = input("請輸入字串 : ")
print('{} 是回文 : {}'.format(wd, palindrome(wd)))




















