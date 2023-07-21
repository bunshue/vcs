import abc
import hashlib
import uuid

def compute_checksum(input, length=None):
    input = input or ''
    s = hashlib.sha1(input.encode('utf-8')).hexdigest()
    if length:
        s = s[:length]
    return s

metaclass=abc.ABCMeta
print(metaclass)

id = str(uuid.uuid4())
print(id)
    
input = 'cat-dog'
output = 'lion-mouse'
computed = compute_checksum(output, 20)
print(computed)

computed = "output={} input={}".format(compute_checksum(output, 16), compute_checksum(input, 16))

print(computed)


import sys
if sys.version_info.major < 3 or sys.version_info.minor < 3:
    sys.exit("Error: clinic.py requires Python 3.3 or greater.")






