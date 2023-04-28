import hashlib

string = 'lion-mouse'
value = hashlib.md5(string.encode('utf8'))
print(value)

