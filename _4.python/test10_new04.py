import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個


import sys, os, time
from stat import *

secs_per_year = 365.0 * 24.0 * 3600.0   # Scale factor
now = time.time()                       # Current time, for age computations

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
    
st = os.lstat(filename)

itime = ST_MTIME
#itime = ST_CTIME
anytime = st[itime]
size = st[ST_SIZE]
age = now - anytime
byteyears = float(size) * float(age) / secs_per_year

print(filename.ljust(50), end=' ')
print(repr(int(byteyears)).rjust(8))

print()

print(filename.ljust(60), end=' ')
print(repr(int(byteyears)).rjust(8))


print('------------------------------------------------------------')	#60個



import os
import sys

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'


short_filename = os.path.basename(filename)

print(short_filename)

cache_dir = os.path.dirname(filename)
print(cache_dir)

head, tail = short_filename[:-3], short_filename[-3:]
print(head)
print(tail)



print('------------------------------------------------------------')	#60個



import sys
import os
    
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

canonic = os.path.abspath(filename)
print(canonic)

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
canonic = os.path.normcase(filename)
print(canonic)

print('------------------------------------------------------------')	#60個


import datetime

text = '2012-09-20'
y = datetime.datetime.strptime(text, '%Y-%m-%d')
z = datetime.datetime.now()
diff = z - y
print(diff)

print(z)
nice_z = datetime.datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)


text = '2012-09-20'
year_s, mon_s, day_s = text.split('-')
ttt = datetime.datetime(int(year_s), int(mon_s), int(day_s))
print(ttt)



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('計算字數')

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename1 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/alice.txt'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/siddhartha.txt'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/moby_dick.txt'
filename4 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/little_women.txt'

filenames = [filename1, filename2, filename3, filename4]

filename = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'

for filename in filenames:
    count_words(filename)

print('------------------------------------------------------------')	#60個


print('統計一個檔案的字數')

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


print('------------------------------------------------------------')	#60個



