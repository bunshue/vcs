"""
python-data01

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
#Dates and Times

from datetime import datetime, date, time

year = 2015
month = 1
day = 20
hour = 7
minute = 28
second = 15

dt = datetime(year, month, day, hour, minute, second)

cc = dt.hour, dt.minute, dt.second
print(cc)

cc = dt.date()
print(cc)

#Extract the equivalent time object:

cc = dt.time()
print(cc)

cc = dt.replace(minute=0, second=0)
print(cc)

#strftime

cc = dt.strftime('%m/%d/%Y %H:%M')
print(cc)

#strptime

cc = datetime.strptime('20150120', '%Y%m%d')
print(cc)

#timedelta

dt_now = datetime.now()

delta = dt_now - dt
print(delta)

#datetime.timedelta(6, 40171, 885211)

cc = dt + delta
print(cc)

#datetime.datetime(2015, 1, 26, 18, 37, 46, 885211)



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import re


class TransformUtil:

    @classmethod
    def remove_punctuation(cls, value):
        """Removes !, #, and ?.
        """        
        return re.sub('[!#?]', '', value) 

    @classmethod
    def clean_strings(cls, strings, ops): 
        """General purpose method to clean strings.

        Pass in a sequence of strings and the operations to perform.
        """        
        result = [] 
        for value in strings: 
            for function in ops: 
                value = function(value) 
            result.append(value) 
        return result


# %%file tests/test_transform_util.py
#from nose.tools import assert_equal
#from ..transform_util import TransformUtil


class TestTransformUtil():

    states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', \
          'FlOrIda', 'south carolina##', 'West virginia?']
    
    expected_output = ['Alabama',
                       'Georgia',
                       'Georgia',
                       'Georgia',
                       'Florida',
                       'South Carolina',
                       'West Virginia']
    
    def test_remove_punctuation(self):
        assert_equal(TransformUtil.remove_punctuation('!#?'), '')
        
    def test_map_remove_punctuation(self):
        # Map applies a function to a collection
        output = map(TransformUtil.remove_punctuation, self.states)
        assert_equal('!#?' not in output, True)

    def test_clean_strings(self):
        clean_ops = [str.strip, TransformUtil.remove_punctuation, str.title] 
        output = TransformUtil.clean_strings(self.states, clean_ops)
        assert_equal(output, self.expected_output)

strings = ['foo', 'bar,', 'baz', 'f', 'fo', 'b', 'ba']
strings.sort(key=lambda x: len(list(x)))
print(strings)

#Closures

def my_decorator(fun):
    def myfun(*params, **kwparams):
        do_something()
        fun(*params, **kwparams)
    return myfun


def make_closure(x):
    def closure():
        print('Secret value is: %s' % x)
    return closure

closure = make_closure(7)
closure()

#Keep track of arguments passed:

def make_watcher():
    dict_seen = {}
    
    def watcher(x):
        if x in dict_seen:
            return True
        else:
            dict_seen[x] = True
            return False
        
    return watcher

watcher = make_watcher()
seq = [1, 1, 2, 3, 5, 8, 13, 2, 5, 13]
[watcher(x) for x in seq]

#[False, True, False, False, False, False, False, True, True, True]

print("------------------------------------------------------------")  # 60個

def foo(func, arg, *args, **kwargs):
    print('arg: %s', arg)
    print('args: %s', args)
    print('kwargs: %s', kwargs)
    
    print('func result: %s', func(args))

foo(sum, "foo", 1, 2, 3, 4, 5)

print("------------------------------------------------------------")  # 60個

#Currying

def add_numbers(x, y):
    return x + y

add_seven = lambda y: add_numbers(7, y)
cc = add_seven(3)
print(cc)


from functools import partial
add_five = partial(add_numbers, 5)
cc = add_five(2)
print(cc)

#Generators

def squares(n=5):
    for x in range(1, n + 1):
        yield x ** 2

# No code is executed
gen = squares()

# Generator returns values lazily
for x in squares():
    print(x)

#Generator Expressions

#A generator expression is analogous to a comprehension. A list comprehension is enclosed by [], a generator expression is enclosed by ():

gen = (x ** 2 for x in range(1, 6))
for x in gen:
    print(x)

#itertools

import itertools
first_letter = lambda x: x[0]
strings = ['foo', 'bar', 'baz']
for letter, gen_names in itertools.groupby(strings, first_letter):
    print(letter, list(gen_names))

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#Logging in Python

import logging
import time
 
from logging.handlers import RotatingFileHandler
 
#----------------------------------------------------------------------
def create_rotating_log(path):
    """
    Creates a rotating log
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
 
    # add a rotating handler
    handler = RotatingFileHandler(path, maxBytes=20,
                                  backupCount=5)
    logger.addHandler(handler)
 
    for i in range(10):
        logger.info("This is test log line %s" % i)
        time.sleep(1.5)
 
log_file = "test.log"
create_rotating_log(log_file)

#Logging with TimedRotatingFileHandler

#The following code snippet is taken from here.

import logging
import time
 
from logging.handlers import TimedRotatingFileHandler
 
#----------------------------------------------------------------------
def create_timed_rotating_log(path):
    """"""
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
 
    # Rotate log based on when parameter:
    # second (s)
    # minute (m)
    # hour (h)
    # day (d)
    # w0-w6 (weekday, 0=Monday)
    # midnight
    handler = TimedRotatingFileHandler(path,
                                       when="m",
                                       interval=1,
                                       backupCount=5)
    logger.addHandler(handler)
 
    for i in range(20):
        logger.info("This is a test!")
        time.sleep(1.5)
 
log_file = "timed_test.log"
create_timed_rotating_log(log_file)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
