"""


"""

import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個
'''
math.sqrt(25)

from math import sqrt
sqrt(25)    # no longer have to reference the module

from math import cos, floor

# import all functions in a module (generally discouraged)
# from os import *

# show all functions in math module
content = dir(math)

###############################################################################
# Basic operations
# ----------------
#

# Numbers
10 + 4          # add (returns 14)
10 - 4          # subtract (returns 6)
10 * 4          # multiply (returns 40)
10 ** 4         # exponent (returns 10000)
10 / 4          # divide (returns 2 because both types are 'int')
10 / float(4)   # divide (returns 2.5)
5 % 4           # modulo (returns 1) - also known as the remainder

10 / 4          # true division (returns 2.5)
10 // 4         # floor division (returns 2)


# Boolean operations
# comparisons (these return True)
5 > 3
5 >= 3
5 != 3
5 == 5

# boolean operations (these return True)
5 > 3 and 6 > 3
5 > 3 or 5 < 3
not False
False or not False and True     # evaluation order: not, and, or


###############################################################################
# Data types
# ----------
#

# determine the type of an object
type(2)         # returns 'int'
type(2.0)       # returns 'float'
type('two')     # returns 'str'
type(True)      # returns 'bool'
type(None)      # returns 'NoneType'

# check if an object is of a given type
isinstance(2.0, int)            # returns False
isinstance(2.0, (int, float))   # returns True

# convert an object to a given type
float(2)
int(2.9)
str(2.9)

# zero, None, and empty containers are converted to False
bool(0)
bool(None)
bool('')    # empty string
bool([])    # empty list
bool({})    # empty dictionary

# non-empty containers and non-zeros are converted to True
bool(2)
bool('two')
bool([2])


###############################################################################
# Lists
# ~~~~~
#
# Different objects categorized along a certain ordered sequence, lists
# are ordered, iterable, mutable (adding or removing objects changes the
# list size), can contain multiple data types.


# create an empty list (two ways)
empty_list = []
empty_list = list()

# create a list
simpsons = ['homer', 'marge', 'bart']

# examine a list
simpsons[0]     # print element 0 ('homer')
len(simpsons)   # returns the length (3)

# modify a list (does not return the list)
simpsons.append('lisa')                 # append element to end
simpsons.extend(['itchy', 'scratchy'])  # append multiple elements to end
simpsons.insert(0, 'maggie')            # insert element at index 0 (shifts everything right)
simpsons.remove('bart')                 # searches for first instance and removes it
simpsons.pop(0)                         # removes element 0 and returns it
del simpsons[0]                         # removes element 0 (does not return it)
simpsons[0] = 'krusty'                  # replace element 0

# concatenate lists (slower than 'extend' method)
neighbors = simpsons + ['ned','rod','todd']

# find elements in a list
'lisa' in simpsons
simpsons.count('lisa')      # counts the number of instances
simpsons.index('itchy')     # returns index of first instance

# list slicing [start:end:stride]
weekdays = ['mon','tues','wed','thurs','fri']
weekdays[0]         # element 0
weekdays[0:3]       # elements 0, 1, 2
weekdays[:3]        # elements 0, 1, 2
weekdays[3:]        # elements 3, 4
weekdays[-1]        # last element (element 4)
weekdays[::2]       # every 2nd element (0, 2, 4)
weekdays[::-1]      # backwards (4, 3, 2, 1, 0)

# alternative method for returning the list backwards
list(reversed(weekdays))

# sort a list in place (modifies but does not return the list)
simpsons.sort()
simpsons.sort(reverse=True)     # sort in reverse
simpsons.sort(key=len)          # sort by a key

# return a sorted list (but does not modify the original list)
sorted(simpsons)
sorted(simpsons, reverse=True)
sorted(simpsons, key=len)

# create a second reference to the same list
num = [1, 2, 3]
same_num = num
same_num[0] = 0         # modifies both 'num' and 'same_num'

# copy a list (three ways)
new_num = num.copy()
new_num = num[:]
new_num = list(num)

# examine objects
id(num) == id(same_num) # returns True
id(num) == id(new_num)  # returns False
num is same_num         # returns True
num is new_num          # returns False
num == same_num         # returns True
num == new_num          # returns True (their contents are equivalent)

# conatenate +, replicate *
[1, 2, 3] + [4, 5, 6]
["a"] * 2 + ["b"] * 3


###############################################################################
# Tuples
# ~~~~~~
#
# Like lists, but their size cannot change: ordered, iterable, immutable,
# can contain multiple data types
#

# create a tuple
digits = (0, 1, 'two')          # create a tuple directly
digits = tuple([0, 1, 'two'])   # create a tuple from a list
zero = (0,)                     # trailing comma is required to indicate it's a tuple

# examine a tuple
digits[2]           # returns 'two'
len(digits)         # returns 3
digits.count(0)     # counts the number of instances of that value (1)
digits.index(1)     # returns the index of the first instance of that value (1)

# elements of a tuple cannot be modified
# digits[2] = 2       # throws an error

# concatenate tuples
digits = digits + (3, 4)

# create a single tuple with elements repeated (also works with lists)
(3, 4) * 2          # returns (3, 4, 3, 4)

# tuple unpacking
bart = ('male', 10, 'simpson')  # create a tuple


###############################################################################
# Strings
# ~~~~~~~
#
# A sequence of characters, they are iterable, immutable
#

# create a string
s = str(42)         # convert another data type into a string
s = 'I like you'

# examine a string
s[0]                # returns 'I'
len(s)              # returns 10

# string slicing like lists
s[:6]               # returns 'I like'
s[7:]               # returns 'you'
s[-1]               # returns 'u'

# basic string methods (does not modify the original string)
s.lower()           # returns 'i like you'
s.upper()           # returns 'I LIKE YOU'
s.startswith('I')   # returns True
s.endswith('you')   # returns True
s.isdigit()         # returns False (returns True if every character in the string is a digit)
s.find('like')      # returns index of first occurrence (2), but doesn't support regex
s.find('hate')      # returns -1 since not found
s.replace('like','love')    # replaces all instances of 'like' with 'love'

# split a string into a list of substrings separated by a delimiter
s.split(' ')        # returns ['I','like','you']
s.split()           # same thing
s2 = 'a, an, the'
s2.split(',')       # returns ['a',' an',' the']

# join a list of strings into one string using a delimiter
stooges = ['larry','curly','moe']
' '.join(stooges)   # returns 'larry curly moe'

# concatenate strings
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4       # returns 'The meaning of life is 42'
s3 + ' ' + str(42)  # same thing

# remove whitespace from start and end of a string
s5 = '  ham and cheese  '
s5.strip()          # returns 'ham and cheese'

# string substitutions: all of these return 'raining cats and dogs'
'raining %s and %s' % ('cats','dogs')                       # old way
'raining {} and {}'.format('cats','dogs')                   # new way
'raining {arg1} and {arg2}'.format(arg1='cats',arg2='dogs') # named arguments

# string formatting
# more examples: http://mkaz.com/2012/10/10/python-string-format/
'pi is {:.2f}'.format(3.14159)      # returns 'pi is 3.14'



###############################################################################
# Strings 2/2
# ~~~~~~~~~~~

###############################################################################
# Normal strings allow for escaped characters
#

print('first line\nsecond line')

###############################################################################
# raw strings treat backslashes as literal characters
#

print(r'first line\nfirst line')

###############################################################################
# Sequence of bytes are not strings, should be decoded before some operations
#
s = b'first line\nsecond line'
print(s)

print(s.decode('utf-8').split())


###############################################################################
# Dictionaries
# ~~~~~~~~~~~~
#
# Dictionaries are structures which can contain multiple data types, and
# is ordered with key-value pairs: for each (unique) key, the dictionary
# outputs one value. Keys can be strings, numbers, or tuples, while the
# corresponding values can be any Python object. Dictionaries are:
# unordered, iterable, mutable
#

# create an empty dictionary (two ways)
empty_dict = {}
empty_dict = dict()

# create a dictionary (two ways)
family = {'dad':'homer', 'mom':'marge', 'size':6}
family = dict(dad='homer', mom='marge', size=6)

# convert a list of tuples into a dictionary
list_of_tuples = [('dad','homer'), ('mom','marge'), ('size', 6)]
family = dict(list_of_tuples)

# examine a dictionary
family['dad']       # returns 'homer'
len(family)         # returns 3
family.keys()       # returns list: ['dad', 'mom', 'size']
family.values()     # returns list: ['homer', 'marge', 6]
family.items()      # returns list of tuples:
                    #   [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
'mom' in family     # returns True
'marge' in family   # returns False (only checks keys)

# modify a dictionary (does not return the dictionary)
family['cat'] = 'snowball'              # add a new entry
family['cat'] = 'snowball ii'           # edit an existing entry
del family['cat']                       # delete an entry
family['kids'] = ['bart', 'lisa']       # value can be a list
family.pop('dad')                       # removes an entry and returns the value ('homer')
family.update({'baby':'maggie', 'grandpa':'abe'})   # add multiple entries

# accessing values more safely with 'get'
family['mom']                       # returns 'marge'
family.get('mom')                   # same thing
try:
    family['grandma']               # throws an error
except  KeyError as e:
    print("Error", e)

family.get('grandma')               # returns None
family.get('grandma', 'not found')  # returns 'not found' (the default)

# accessing a list element within a dictionary
family['kids'][0]                   # returns 'bart'
family['kids'].remove('lisa')       # removes 'lisa'

# string substitution using a dictionary
'youngest child is %(baby)s' % family   # returns 'youngest child is maggie'


###############################################################################
# Sets
# ~~~~
#
# Like dictionaries, but with unique keys only (no corresponding values).
# They are: unordered, iterable, mutable, can contain multiple data types
# made up of unique elements (strings, numbers, or tuples)
#

# create an empty set
empty_set = set()

# create a set
languages = {'python', 'r', 'java'}         # create a set directly
snakes = set(['cobra', 'viper', 'python'])  # create a set from a list

# examine a set
len(languages)              # returns 3
'python' in languages       # returns True

# set operations
languages & snakes          # returns intersection: {'python'}
languages | snakes          # returns union: {'cobra', 'r', 'java', 'viper', 'python'}
languages - snakes          # returns set difference: {'r', 'java'}
snakes - languages          # returns set difference: {'cobra', 'viper'}

# modify a set (does not return the set)
languages.add('sql')        # add a new element
languages.add('r')          # try to add an existing element (ignored, no error)
languages.remove('java')    # remove an element

try:
    languages.remove('c')       # try to remove a non-existing element (throws an error)
except  KeyError as e:
    print("Error", e)

languages.discard('c')      # removes an element if present, but ignored otherwise
languages.pop()             # removes and returns an arbitrary element
languages.clear()           # removes all elements
languages.update('go', 'spark') # add multiple elements (can also pass a list or set)

# get a sorted list of unique elements from a list
sorted(set([9, 0, 2, 1, 0]))    # returns [0, 1, 2, 9]

###############################################################################
# Execution control statements
# ----------------------------
#

###############################################################################
# Conditional statements
# ~~~~~~~~~~~~~~~~~~~~~~

x = 3
# if statement
if x > 0:
    print('positive')

# if/else statement
if x > 0:
    print('positive')
else:
    print('zero or negative')

# if/elif/else statement
if x > 0:
    print('positive')
elif x == 0:
    print('zero')
else:
    print('negative')

# single-line if statement (sometimes discouraged)
if x > 0: print('positive')

# single-line if/else statement (sometimes discouraged)
# known as a 'ternary operator'
sign = 'positive' if x > 0 else 'zero or negative'


###############################################################################
# Loops
# ~~~~~
#
# Loops are a set of instructions which repeat until termination
# conditions are met. This can include iterating through all values in an
# object, go through a range of values, etc
#

# range returns a list of integers
range(0, 3)     # returns [0, 1, 2]: includes first value but excludes second value
range(3)        # same thing: starting at zero is the default
range(0, 5, 2)  # returns [0, 2, 4]: third argument specifies the 'stride'

# for loop
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(fruits[i].upper())

# alternative for loop (recommended style)
for fruit in fruits:
    print(fruit.upper())

# use range when iterating over a large sequence to avoid actually creating the integer list in memory
v = 0
for i in range(10 ** 6):
    v += 1


###############################################################################
# List comprehensions, iterators, etc.
# ------------------------------------
#
# List comprehensions
# ~~~~~~~~~~~~~~~~~~~
#
# Process which affects whole lists without iterating through loops. For
# more:
# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
#

# for loop to create a list of cubes
nums = [1, 2, 3, 4, 5]
cubes = []
for num in nums:
    cubes.append(num**3)

# equivalent list comprehension
cubes = [num**3 for num in nums]    # [1, 8, 27, 64, 125]

# for loop to create a list of cubes of even numbers
cubes_of_even = []
for num in nums:
    if num % 2 == 0:
        cubes_of_even.append(num**3)

# equivalent list comprehension
# syntax: [expression for variable in iterable if condition]
cubes_of_even = [num**3 for num in nums if num % 2 == 0]    # [8, 64]

# for loop to cube even numbers and square odd numbers
cubes_and_squares = []
for num in nums:
    if num % 2 == 0:
        cubes_and_squares.append(num**3)
    else:
        cubes_and_squares.append(num**2)

# equivalent list comprehension (using a ternary expression)
# syntax: [true_condition if condition else false_condition for variable in iterable]
cubes_and_squares = [num**3 if num % 2 == 0 else num**2 for num in nums]    # [1, 8, 9, 64, 25]

# for loop to flatten a 2d-matrix
matrix = [[1, 2], [3, 4]]
items = []
for row in matrix:
    for item in row:
        items.append(item)

# equivalent list comprehension
items = [item for row in matrix
              for item in row] # [1, 2, 3, 4]

# set comprehension
fruits = ['apple', 'banana', 'cherry']
unique_lengths = {len(fruit) for fruit in fruits}   # {5, 6}

# dictionary comprehension
fruit_lengths = {fruit:len(fruit) for fruit in fruits} # {'apple': 5, 'banana': 6, 'cherry': 6}

simpsons = {'Homer': 45, 'Marge': 45, 'Bart': 10, 'Lisa': 10}

simpsons_older = {k.upper(): v + 1 for k, v in simpsons.items()}
print(simpsons_older)


###############################################################################
# Exercice: count words in a sentence
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


quote = """Tick-tow
our incomes are like our shoes; if too small they gall and pinch us
but if too large they cause us to stumble and to trip
"""

count = {word: 0 for word in set(quote.split())}
for word in quote.split():
    count[word] += 1

# iterate through two things at once (using tuple unpacking)
family = {'dad': 'homer', 'mom': 'marge', 'size': 6}
for key, value in family.items():
    print(key, value)

# use enumerate if you need to access the index value within the loop
for index, fruit in enumerate(fruits):
    print(index, fruit)

# for/else loop
for fruit in fruits:
    if fruit == 'banana':
        print("Found the banana!")
        break   # exit the loop and skip the 'else' block
    else:
        # this block executes ONLY if the for loop completes without hitting
        # 'break'
        print("Can't find the banana")

# while loop
count = 0
while count < 5:
    print("This will print 5 times")
    count += 1      # equivalent to 'count = count + 1'

###############################################################################
# Exceptions handling
# ~~~~~~~~~~~~~~~~~~~
#

dct = dict(a=[1, 2], b=[4, 5])

key = 'c'
try:
    dct[key]
except:
    print("Key %s is missing. Add it with empty value" % key)
    dct['c'] = []

print(dct)

###############################################################################
# Functions
# ---------
#
# Functions are sets of instructions launched when called upon, they can
# have multiple input values and a return value
#

# define a function with no arguments and no return values
def print_text():
    print('this is text')

# call the function
print_text()

# define a function with one argument and no return values
def print_this(x):
    print(x)

# call the function
print_this(3)       # prints 3
n = print_this(3)   # prints 3, but doesn't assign 3 to n
                    # because the function has no return statement

def add(a, b):
    return a + b

add(2, 3)

add("deux", "trois")

add(["deux", "trois"], [2, 3])

# define a function with one argument and one return value
def square_this(x):
    return x ** 2

# include an optional docstring to describe the effect of a function
def square_this(x):
    """Return the square of a number."""
    return x ** 2

# call the function
square_this(3)          # prints 9
var = square_this(3)    # assigns 9 to var, but does not print 9

# default arguments
def power_this(x, power=2):
    return x ** power

power_this(2)    # 4
power_this(2, 3) # 8

# use 'pass' as a placeholder if you haven't written the function body
def stub():
    pass

# return two values from a single function
def min_max(nums):
    return min(nums), max(nums)

# return values can be assigned to a single variable as a tuple
nums = [1, 2, 3]
min_max_num = min_max(nums)         # min_max_num = (1, 3)

# return values can be assigned into multiple variables using tuple unpacking
min_num, max_num = min_max(nums)    # min_num = 1, max_num = 3


###############################################################################
# Regular expression
# ------------------
#

import re

# 1. Compile regular expression with a patetrn
regex = re.compile("^.+(sub-.+)_(ses-.+)_(mod-.+)")

###############################################################################
# 2. Match compiled RE on string
#
# Capture the pattern ```anyprefixsub-<subj id>_ses-<session id>_<modality>```

strings = ["abcsub-033_ses-01_mod-mri", "defsub-044_ses-01_mod-mri", "ghisub-055_ses-02_mod-ctscan"]
print([regex.findall(s)[0] for s in strings])

###############################################################################
# Match methods on compiled regular expression
#
# +------------------+----------------------------------------------------------------------------+
# | Method/Attribute | Purpose                                                                    |
# +==================+============================================================================+
# | match(string)    | Determine if the RE matches at the beginning of the string.                |
# +------------------+----------------------------------------------------------------------------+
# | search(string)   | Scan through a string, looking for any location where this RE matches.     |
# +------------------+----------------------------------------------------------------------------+
# | findall(string)  | Find all substrings where the RE matches, and returns them as a list.      |
# +------------------+----------------------------------------------------------------------------+
# | finditer(string) | Find all substrings where the RE matches, and returns them as an iterator. |
# +------------------+----------------------------------------------------------------------------+

###############################################################################
# 2. Replace compiled RE on string

regex = re.compile("(sub-[^_]+)") # match (sub-...)_
print([regex.sub("SUB-", s) for s in strings])

regex.sub("SUB-", "toto")

###############################################################################
# Remove all non-alphanumeric characters in a string

re.sub('[^0-9a-zA-Z]+', '', 'h^&ell`.,|o w]{+orld')

# Get the current working directory
cwd = os.getcwd()
print(cwd)

# Set the current working directory
os.chdir(cwd)

import tempfile

tmpdir = tempfile.gettempdir()

# Join paths
mytmpdir = os.path.join(tmpdir, "foobar")


###############################################################################
# Create a directory

os.makedirs(os.path.join(tmpdir, "foobar", "plop", "toto"), exist_ok=True)

# list containing the names of the entries in the directory given by path.
os.listdir(mytmpdir)

###############################################################################
# File input/output
# ~~~~~~~~~~~~~~~~~
#

filename = os.path.join(mytmpdir, "myfile.txt")
print(filename)

# Write
lines = ["Dans python tout est bon", "Enfin, presque"]

## write line by line
fd = open(filename, "w")
fd.write(lines[0] + "\n")
fd.write(lines[1]+ "\n")
fd.close()

## use a context manager to automatically close your file
with open(filename, 'w') as f:
    for line in lines:
        f.write(line + '\n')

# Read
## read one line at a time (entire file does not have to fit into memory)
f = open(filename, "r")
f.readline()    # one string per line (including newlines)
f.readline()    # next line
f.close()

## read one line at a time (entire file does not have to fit into memory)
f = open(filename, 'r')
f.readline()    # one string per line (including newlines)
f.readline()    # next line
f.close()

## read the whole file at once, return a list of lines
f = open(filename, 'r')
f.readlines()   # one list, each line is one string
f.close()

## use list comprehension to duplicate readlines without reading entire file at once
f = open(filename, 'r')
[line for line in f]
f.close()

## use a context manager to automatically close your file
with open(filename, 'r') as f:
    lines = [line for line in f]


WD = os.path.join(tmpdir, "foobar")

for dirpath, dirnames, filenames in os.walk(WD):
    print(dirpath, dirnames, filenames)


###############################################################################
# glob, basename and file extension

import tempfile
import glob

tmpdir = tempfile.gettempdir()

filenames = glob.glob(os.path.join(tmpdir, "*", "*.txt"))
print(filenames)

# take basename then remove extension
basenames = [os.path.splitext(os.path.basename(f))[0] for f in filenames]
print(basenames)


###############################################################################
# shutil - High-level file operations
#

import shutil

src = os.path.join(tmpdir, "foobar",  "myfile.txt")
dst = os.path.join(tmpdir, "foobar",  "plop", "myfile.txt")
print("copy %s to %s" % (src, dst))

shutil.copy(src, dst)

print("File %s exists ?" % dst, os.path.exists(dst))

src = os.path.join(tmpdir, "foobar",  "plop")
dst = os.path.join(tmpdir, "plop2")
print("copy tree %s under %s" % (src, dst))

try:
    shutil.copytree(src, dst)

    shutil.rmtree(dst)

    shutil.move(src, dst)
except (FileExistsError, FileNotFoundError) as e:
    pass

###############################################################################
# Command execution with subprocess
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# - For more advanced use cases, the underlying Popen interface can be used directly.
# - Run the command described by args.
# - Wait for command to complete
# - return a CompletedProcess instance.
# - Does not capture stdout or stderr by default. To do so, pass PIPE for the stdout and/or stderr arguments.

print("------------------------------------------------------------")  # 60個

import subprocess

# doesn't capture output
p = subprocess.run(["ls", "-l"])
print(p.returncode)

# Run through the shell.
subprocess.run("ls -l", shell=True)

# Capture output
out = subprocess.run(["ls", "-a", "/"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# out.stdout is a sequence of bytes that should be decoded into a utf-8 string
print(out.stdout.decode('utf-8').split("\n")[:5])

import threading

def list_append(count, sign=1, out_list=None):
    if out_list is None:
        out_list = list()
    for i in range(count):
        out_list.append(sign * i)
        sum(out_list) # do some computation
    return out_list

size = 10000   # Number of numbers to add

out_list = list() # result is a simple list
thread1 = threading.Thread(target=list_append, args=(size, 1, out_list, ))
thread2 = threading.Thread(target=list_append, args=(size, -1, out_list, ))

startime = time.time()
# Will execute both in parallel
thread1.start()
thread2.start()
# Joins threads back to the parent process
thread1.join()
thread2.join()
print("Threading ellapsed time ", time.time() - startime)

print(out_list[:10])

###############################################################################
# Multiprocessing
#

import multiprocessing

# Sharing requires specific mecanism
out_list1 = multiprocessing.Manager().list()
p1 = multiprocessing.Process(target=list_append, args=(size, 1, None))
out_list2 = multiprocessing.Manager().list()
p2 = multiprocessing.Process(target=list_append, args=(size, -1, None))

startime = time.time()
p1.start()
p2.start()
p1.join()
p2.join()
print("Multiprocessing ellapsed time ", time.time() - startime)

# print(out_list[:10]) is not availlable

import multiprocessing

size = int(size / 100)   # Number of numbers to add

# Sharing requires specific mecanism
out_list = multiprocessing.Manager().list()
p1 = multiprocessing.Process(target=list_append, args=(size, 1, out_list))
p2 = multiprocessing.Process(target=list_append, args=(size, -1, out_list))

startime = time.time()

p1.start()
p2.start()

p1.join()
p2.join()

print(out_list[:10])

print("Multiprocessing with shared object ellapsed time ", time.time() - startime)

# Full FTP features with ftplib
import ftplib
ftp = ftplib.FTP("ftp.cea.fr")
ftp.login()
ftp.cwd('/pub/unati/people/educhesnay/pystatml')
ftp.retrlines('LIST')

fd = open(os.path.join(tmpdir, "README.md"), "wb")
ftp.retrbinary('RETR README.md', fd.write)
fd.close()
ftp.quit()

# File download urllib
import urllib.request
ftp_url = 'ftp://ftp.cea.fr/pub/unati/people/educhesnay/pystatml/README.md'
urllib.request.urlretrieve(ftp_url, os.path.join(tmpdir, "README2.md"))

import sys
sys.path.append("path_to_parent_python_module")


class Shape2D:
    def area(self):
        raise NotImplementedError()

# __init__ is a special method called the constructor


# Inheritance + Encapsulation
class Square(Shape2D):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2


class Disk(Shape2D):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


shapes = [Square(2), Disk(3)]

# Polymorphism
print([s.area() for s in shapes])

s = Shape2D()
try:
    s.area()
except NotImplementedError as e:
    print("NotImplementedError", e)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

###############################################################################
# Style guide for Python programming
# ----------------------------------
#
# See `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_
#
# - Spaces (four) are the preferred indentation method.
# - Two blank lines for top level function or classes definition.
# - One blank line to indicate logical sections.
# - Never use: ``from lib import *``
# - Bad: ``Capitalized_Words_With_Underscores``
# - Function and Variable Names: ``lower_case_with_underscores``
# - Class Names: ``CapitalizedWords`` (aka: ``CamelCase``)


###############################################################################
# Documenting
# -----------
#
# See `Documenting Python <https://realpython.com/documenting-python-code//>`_
# Documenting = comments + docstrings (Python documentation string)
#
# - `Docstrings <https://www.datacamp.com/community/tutorials/docstrings-python>`_
#   are use as documentation for the class, module, and packages.
#   See it as "living documentation".
# - Comments are  used to explain non-obvious portions of the code. "Dead documentation".
#
# Docstrings for functions (same for classes and methods):

def my_function(a, b=2):
    """
    This function ...

    Parameters
    ----------
    a : float
        First operand.
    b : float, optional
        Second operand. The default is 2.

    Returns
    -------
    Sum of operands.

    Example
    -------
    >>> my_function(3)
    5
    """
    # Add a with b (this is a comment)
    return a + b

print(help(my_function))

print("------------------------------------------------------------")  # 60個

def calc(a, b, op='add'):
    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    else:
        print('valid operations are add and sub')


# call the function
calc(10, 4, op='add')   # returns 14
calc(10, 4, 'add')      # also returns 14: unnamed arguments are inferred by position
calc(10, 4)             # also returns 14: default for 'op' is 'add'
calc(10, 4, 'sub')      # returns 6
calc(10, 4, 'div')      # prints 'valid operations are add and sub'

a, b, op = 2, 3, "+"


def calc2(a, b, op='+'):
    st = "%.f %s %.f" % (a, op, b)
    return eval(st)


calc2(3, 3, "+")


def remove_adjacent_duplicates(original_list):
    new_list = []
    new_list.append(original_list[0])
    for num in original_list[1:]:
        if num != new_list[-1]:
            new_list.append(num)
    return new_list

remove_adjacent_duplicates([1, 2, 2, 3, 2])

def remove_duplicates(original_list):
    new_list = []
    for num in original_list:
        if num not in new_list:
            new_list.append(num)
    return new_list

remove_duplicates([3, 2, 2, 1, 2])

# or this solution mights modify the order

def remove_duplicates(original_list):
    return(list(set(original_list)))

remove_duplicates([3, 2, 2, 1, 2])


bsd_4clause = """
XXXXXXXX
XXXXXXXX
"""

import tempfile

tmpfilename = os.path.join(tempfile.gettempdir(),
                       "bsd.txt")

fd = open(tmpfilename, "w")
fd.write(bsd_4clause)
fd.close()

fd = open(tmpfilename, "r")

count = dict()
for line in fd:
    line = line.lower()
    for word in line.split():
        if not word in count:
            count[word] = 1
        else:
            count[word] += 1

print(count)

"""
Comment to deal with missing import of urllib2

import urllib2
url = "https://www.gnu.org/licenses/gpl-3.0.txt"
f = urllib2.urlopen(url)
content = f.read()
f.close()
content = content.replace("\n", " ")
content = content.lower()
c = content.split(' ')
print(len(c))
from collections import Counter
print(Counter(c))
"""


class Employee:
    def __init__(self, name, years_of_service):
        self.name = name
        self.years_of_service = years_of_service

    def salary(self):
        return 1500 + 100 * self.years_of_service


class Manager(Employee):
    def salary(self):
        return 2500 + 120 * self.years_of_service


samples = [Employee("lucy", 3),
           Employee("john", 1),
           Manager('julie', 3),
           Manager('paul', 1)]

employees = {e.name: e for e in samples}

employees.keys()

df = pd.DataFrame([[name, obj.salary()] for name, obj in employees.items()],
             columns=['name', 'salary'])

[[name, employees[name].salary()] for name
      in employees]

sum([e.salary() for e in employees.values()]) / len(employees)
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# count_words

"""
./count_words.py -i /tmp/bsd.txt
"""

import os
import os.path
import argparse
import re
import pandas as pd

if __name__ == "__main__":
    # parse command line options
    output = "word_count.csv"
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input',
                        help='list of input files.',
                        nargs='+', type=str)
    parser.add_argument('-o', '--output',
                        help='output csv file (default %s)' % output,
                        type=str, default=output)
    options = parser.parse_args()

    if options.input is None :
        parser.print_help()
        raise SystemExit("Error: input files are missing")
    else:
        filenames = [f for f in options.input if os.path.isfile(f)]

    # Match words
    #regex = re.compile("[^ \t\n\r\f\v,\._></\(\)\[\]']+")
    regex = re.compile("[a-zA-Z]+")

    count = dict()
    for filename in filenames:
        # Debug purpose
        # filename = '/tmp/licence.txt'
        fd = open(filename, "r")
        for line in fd:
            for word in regex.findall(line.lower()):
                if not word in count:
                    count[word] = 1
                else:
                    count[word] += 1

    fd = open(options.output, "w")

    # Do it manually
    """
    with open(options.output, 'w') as f:
        f.write(",".join(["word", "count"]) + '\n')
        for k, val in count.items():
            f.write(",".join([k, val]) + '\n')
    """

    # Pandas
    df = pd.DataFrame([[k, count[k]] for k in count], columns=["word", "count"])
    df.to_csv(options.output, index=False)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# replace

"""
./replace.py -i /tmp/brainvol/data/* -p wm -r WM
"""

import os
import os.path
import argparse
import re
import shutil

if __name__ == "__main__":

    # parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='list of input files or root directory', nargs='+', type=str)
    parser.add_argument('--backup', action='store_true', help='save backup .bak file')
    parser.add_argument('--noaction', action='store_true', help='dry run')
    parser.add_argument('-p', '--pattern', help='list of input files or root directory', type=str)
    parser.add_argument('-r', '--replacement', help='list of input files or root directory', type=str)

    options = parser.parse_args()

    if options.input is None or options.pattern is None:
        parser.print_help()
        raise SystemExit("Error: files are missing")

    if options.replacement is None :
        options.replacement = ""

    if len(options.input) == 1 and os.path.isdir(options.input[0]):
        filenames = [os.path.join(curdir, file) \
             for curdir, subdirs, files in os.walk(options.input[0]) for file in files]
    else:
        filenames = [f for f in options.input if os.path.isfile(f)]


    regex = re.compile(options.pattern)

    for filename in filenames:
        lines = ""
        touch = False
        with open(filename, 'r') as infile:
            try:
                for line in infile:
                    if len(regex.findall(line)) > 0:
                        touch = True
                        line = regex.sub(options.replacement, line)
                        # print(line)
                    lines += line
            except Exception as e:
                print(filename, ":", e)

        if touch and not options.noaction:
            shutil.copy(filename, filename + ".bak")
            with open(filename, 'w') as f:
                f.write(lines)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
