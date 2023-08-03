import hashlib
m = hashlib.md5()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
m.digest()
print(m.digest())

#    b'\\xbbd\\x9c\\x83\\xdd\\x1e\\xa5\\xc9\\xd9\\xde\\xc9\\xa1\\x8d\\xf0\\xff\\xe9'


import os

def getuser():
    for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
        print(name)
        user = os.environ.get(name)
        if user:
            print(user)
            return user

print('get user name')
ccc = getuser()
print(ccc)




def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a




a = 28
b = 49
c = gcd(a, b)
print(c)


import sys

def test():
    '''Test program.
    Usage: ftp [-d] [-r[file]] host [-l[dir]] [-d[dir]] [-p] [file] ...

    -d dir
    -l list
    -p password
    '''

    if len(sys.argv) < 2:
        print(test.__doc__)
        sys.exit(0)

test()



