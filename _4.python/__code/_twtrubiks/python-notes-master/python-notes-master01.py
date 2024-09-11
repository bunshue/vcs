"""


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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# ref. https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass, field


class InventoryItemOLD:
    def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand
        self.total = self.unit_price * self.quantity_on_hand

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', unit_price={self.unit_price}, quantity_on_hand={self.quantity_on_hand}, total={self.total})"


@dataclass(frozen=False)
class InventoryItem:
    """Class for keeping track of an item in inventory."""

    name: str
    unit_price: float
    quantity_on_hand: int = 0
    total: float = field(init=False)

    def __post_init__(self):
        self.total = self.unit_price * self.quantity_on_hand


if __name__ == "__main__":
    print(InventoryItemOLD("twtrubiks", 100, 2))
    print(InventoryItem("twtrubiks", 100, 2))


# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\__call__tutorial.py


class A:
    def __init__(self, data):
        self.__data = data

    def show(self):
        return self.__data

    # If a class defines a __call__ method, then its instances may be invoked as functions.
    def __call__(self):
        return self.show()


if __name__ == "__main__":
    a = A("hello")
    print("a.show():", a.show())
    print("a():", a())
    # a.show() = a()
    print("callable(a):", callable(a))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\__getattr__tutorial.py

"""
ref
https://docs.python.org/3/reference/datamodel.html#object.__getattr__

Called when the default attribute access fails with an AttributeError.

Note that if the attribute is found through the normal mechanism,
__getattr__() is not called.
"""


class A:
    def __init__(self, name: str):
        self.name = name

    def __getattribute__(self, item: str):
        return object.__getattribute__(self, item)

    def __getattr__(self, name: str) -> str:
        return name


a = A("twtrubiks")
print(a.aaa)  # trigger __getattr__
print(getattr(a, "aaa"))  # trigger __getattr__

print(a.name)  # not trigger __getattr__
print(getattr(a, "name"))  # not trigger __getattr__

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\__getitem__tutorial.py

"""
ref
https://docs.python.org/3/reference/datamodel.html#object.__getitem__
https://docs.python.org/3/reference/datamodel.html#object.__setitem__
"""


class A:
    def __init__(self):
        self.my_dict = {
            "a": 1,
            "b": 2,
        }

    def __getitem__(self, key):
        return self.my_dict[key]

    def __setitem__(self, key, value):
        self.my_dict[key] = value


a = A()
print(a["a"])
print(a["b"])
a["c"] = 3
print(a["c"])

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\__iter__tutorial.py


class Product(object):
    def __init__(self):
        self.products = [
            {"id": 1, "count": 1, "price": 10},
            {"id": 2, "count": 2, "price": 20},
            {"id": 3, "count": 3, "price": 30},
            {"id": 4, "count": 4, "price": 40},
        ]

    def __iter__(self):
        for product in self.products:
            product["total"] = product["count"] * product["price"]
            yield product


if __name__ == "__main__":
    p = Product()
    for result in p:
        print(result)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\__len__tutorial.py


class Product(object):
    def __init__(self):
        self.items = [
            {"id": 1, "value": 10},
            {"id": 2, "value": 20},
            {"id": 3, "value": 30},
            {"id": 4, "value": 40},
        ]

    def __len__(self):
        return sum(item["value"] for item in self.items)


if __name__ == "__main__":
    data = "test"
    print("data.__str__(): {}".format(data.__len__()))
    print("len(data): {}".format(len(data)))
    product = Product()
    print("len(product): {}".format(len(product)))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\__new__tutorial.py


class A:
    def __new__(cls, *args, **kwargs):
        print("__new__")
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __init__(self):
        print("__init__")


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass


if __name__ == "__main__":
    a = A()
    # output
    # __new__
    # __init__

    s1 = Singleton()
    s2 = Singleton()
    print(id(s1) == id(s2))

print("------------------------------------------------------------")  # 60個


class Person(object):
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return "{first} {last} is {age} years old".format(**self.__dict__)


if __name__ == "__main__":
    data = 22
    print("data.__str__(): {}".format(data.__str__()))
    print("type: {}".format(type(data.__str__())))
    person = Person("twt", "rubiks", 20)
    print("person: {}".format(person))

print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\assert_tutorial.py


def ex1():
    x = "hello"

    # returns True, then nothing happens
    assert x == "hello"

    # raise AssertionError
    assert x == "world"


def ex2():
    x = "hello"
    assert x == "world", "x should be 'hello'"


if __name__ == "__main__":
    ex1()
    # ex2()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\attribute_obj.py


class Person(object):
    name = "twtrubiks"


if __name__ == "__main__":
    p = Person()
    print("Before Set: {}".format(p.name))

    # The setattr() method sets the value of given attribute of an object.
    # setattr(object, name, value)
    setattr(p, "name", "rubiks")
    print("After Set: {}".format(p.name))

    # The getattr() method returns the value of the named attribute of an object
    # getattr(object, name[, default])
    # default (Optional) - value that is returned when the named attribute is not found
    print("The age is: {}".format(getattr(p, "age", "default_20")))
    # print('The age is:'.format(p.age))  # error

    # creates a new attribute
    setattr(p, "age", 18)
    print("After Set afe: {}".format(getattr(p, "age", "default_20")))

    # The hasattr() method returns true if an object has the given named attribute and false if it does not.
    # hasattr(object, name)
    print("Person has name?: {}".format(hasattr(p, "name")))
    print("Person has salary?: {}".format(hasattr(p, "salary")))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\built-in-functions_tutorial.py

# Built-in Functions
# ref. https://docs.python.org/3.6/library/functions.html

if __name__ == "__main__":
    a = list(range(10))
    print(a)
    """
    ref. https://docs.python.org/3.6/library/functions.html#all
    Return True if all elements of the iterable are true (or if the iterable is empty)
    """
    print("all(a)", all(a))
    print("all([])", all([]))  # all([]) returns True

    """
    ref. https://docs.python.org/3.6/library/functions.html#any
    Return True if any element of the iterable is true. If the iterable is empty, return False.
    """
    print("any(a)", any(a))
    print("any([])", any([]))  # any([]) returns False

    """
    ref. https://docs.python.org/3.6/library/functions.html#zip
    Make an iterator that aggregates elements from each of the iterables.
    """
    x = [1, 2, 3]
    y = [4, 5, 6]
    zipped = zip(x, y)
    print(list(zipped))

    """
    ref. https://docs.python.org/3.6/library/functions.html#sum
    """
    print("sum(a)", sum(a))

    """
    ref. https://docs.python.org/3.6/library/functions.html#max
    """
    print("max(a)", max(a))

    my_dict = {2: 1, 3: 0}

    # dict get max key
    print("dict get max key:", max(my_dict))

    # dict get max value
    print("dict get max value:", max(my_dict, key=my_dict.get))

    """
    ref. https://docs.python.org/3.6/library/functions.html#min
    """
    print("min(a)", min(a))

    """
    ref. https://docs.python.org/3/library/functions.html#ord
    """
    print(ord("a"))
    print(ord("D"))

    """
    ref. https://docs.python.org/3/library/functions.html#ord
    """
    print(chr(97))
    print(chr(100))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\bytesio_tutorial.py

# https://docs.python.org/3/library/io.html#binary-i-o

# StringIO 只能是 str，如果要操作 bytes data 就要使用 BytesIO

from io import BytesIO


def tutorial_1():
    # BytesIO 實作在內存 ( 記憶體 ram )中讀寫 bytes
    f = BytesIO()
    # 寫入的不是 str , 而是經過 utf-8 編碼的 bytes
    f.write("中文".encode("utf-8"))
    print(f.getvalue())
    f.close()  # 釋放記憶體


def tutorial_2():
    f = BytesIO(b"\xe4\xb8\xad\xe6\x96\x87")
    result = f.read()
    print(result)
    print(result.decode("utf-8"))


def main():
    tutorial_1()
    # tutorial_2()


if __name__ == "__main__":
    main()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\check_is_in_list.py

if __name__ == "__main__":
    # check is target in list
    target = "test"
    if target in ["test", "yo", "soso"]:
        print("{} in list".format(target))
    else:
        print("{} not in list".format(target))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\classmethod_tutorial.py

# ref. https://www.programiz.com/python-programming/methods/built-in/classmethod

# Static method vs Class method
# Static method knows nothing about the class and just deals with the parameters.
# Class method works with the class since its parameter is always the class itself.

from datetime import date


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    def display(self):
        print(self._name + "'s age is: " + str(self._age))


class Person2:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @staticmethod
    def from_fathers_age(name, father_age, father_person_age_diff):
        return Person2(name, date.today().year - father_age + father_person_age_diff)

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    def display(self):
        print(self._name + "'s age is: " + str(self._age))


class Man(Person2):
    sex = "Male"


def main():
    # tutorial 1
    person = Person("Adam", 19)
    person.display()

    person1 = Person.from_birth_year("John", 1985)
    person1.display()

    # tutorial 2
    man = Man.from_birth_year("John", 1985)
    print(isinstance(man, Man))
    man.display()

    man1 = Man.from_fathers_age("John", 1965, 20)
    print(isinstance(man1, Man))
    man1.display()


if __name__ == "__main__":
    main()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\compare_list_difference.py

# compare_list_difference

if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [2, 0, 4, 6, 7]
    """
    # ex_1  list_1 - list_2 => {1, 3, 5}
    """
    ex_1 = set(list_1) - set(list_2)
    print("ex_1", ex_1)
    """
    # ex_2  list_1 - list_2 => { 0, 1, 3, 5, 6, 7 }
    ref. https://docs.python.org/3/library/stdtypes.html#frozenset.symmetric_difference
    """
    ex_2 = set(list_1).symmetric_difference(list_2)
    print("ex_2", ex_2)
    """
    # ex_3  list_1 and list_2 duplicate => {2, 4}
    ref. https://docs.python.org/3/library/stdtypes.html#frozenset.intersection
    """
    ex_3 = set(list_1).intersection(set(list_2))
    print("ex_3", ex_3)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\context_manager_tutorial.py

from contextlib import contextmanager


@contextmanager
def my_context():
    # do things in enter  ( __enter__ )
    yield
    # do things post  ( __exit__ )


@contextmanager
def tag(name):
    print("<{}>".format(name))
    yield "HIHI~"
    print("</{}>".format(name))


@contextmanager
def elapsed_time(name=""):
    start_time = time.time()
    yield
    end_time = time.time() - start_time
    print(name, "{:.2f}".format(end_time))


@contextmanager
def try_catch():
    try:
        yield "okok"
    except Exception as e:
        print("e=%s" % str(e))
    finally:
        print("stop")


if __name__ == "__main__":
    # tutorial_1
    with tag("h1") as data:
        print("hello")
        print(data)

    # tutorial_2
    # with tag('h1'), tag('p'):
    #     print('hello')

    # tutorial_3
    # with elapsed_time('block'):
    #     time.sleep(2)

    # tutorial_4
    # with try_catch() as data:
    #     print(data)
    #     source = 1/0


print("------------------------------------------------------------")  # 60個

import copy

if __name__ == "__main__":
    """
    ref. https://docs.python.org/3.6/library/copy.html

    """
    origin_list = [1, 2, [3, 4]]
    copy1 = copy.copy(origin_list)  # shallow copy
    copy2 = copy.deepcopy(origin_list)  # deep (recursive) copy
    print(copy1 == copy2)
    print(copy1 is copy2)
    origin_list[2][0] = "yoyo"
    print("origin_list:", origin_list)
    print("copy1:", copy1)
    print("copy2:", copy2)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\counter_tutorial.py

from collections import Counter


def ex1():
    c = Counter(["eggs", "ham", "eggs"])
    print("c[bacon]:", c["bacon"])
    print("c[eggs]:", c["eggs"])
    print("c:", c)


def ex2():
    cnt = Counter()
    for word in ["red", "blue", "red", "green", "blue", "blue"]:
        cnt[word] += 1
    print(cnt)


def method_elements():
    c = Counter(a=4, b=2, c=0, d=-2)
    show = sorted(c.elements())
    print(show)
    print("c.values():", c.values())
    print("sum:", sum(c.values()))


def method_most_common():
    show = Counter("abracadabra").most_common(3)
    print(show)


def patterns():
    c = Counter(a=2, b=-4, c=0)
    print("+c:", +c)
    print("-c:", -c)
    # +c  # remove zero and negative counts


def method_subtract():
    c = Counter(a=4, b=2, c=0, d=-2)
    d = Counter(a=1, b=2, c=3, d=4)
    c.subtract(d)
    print("c:", c)


if __name__ == "__main__":
    ex1()
    ex2()
    method_elements()
    method_most_common()
    patterns()
    method_subtract()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\datetime_tutorial.py

from datetime import datetime, date, timedelta, time as dtime
from calendar import monthrange

if __name__ == "__main__":
    start_date = date(2017, 3, 1)
    end_date = date(2017, 3, 2)
    print(type(start_date))
    print("start_date: {}".format(start_date))
    # total_seconds()
    total_time = (end_date - start_date).total_seconds()
    print("total_time: {}".format(total_time))

    # timedelta
    print("timedelta : {}".format(timedelta(hours=28)))

    now = datetime.now()
    print("now: {}".format(now))
    yestoday = now - timedelta(days=1)
    print("yestoday: {}".format(yestoday))

    # datetime.combine
    combine_time = datetime.combine(date(2017, 3, 1), dtime(18, 23, 50))
    print("combine_time: {}".format(combine_time))
    combine_time_2 = datetime.combine(date(2017, 3, 1), dtime.max)
    print("combine_time_2: {}".format(combine_time_2))

    # strftime ref. http://strftime.org/
    DATETIME_FORMAT = "%m/%d/%Y %I:%M %p"
    format_time = combine_time.strftime(DATETIME_FORMAT)
    print("type: {}".format(type(format_time)))
    print("method 1 :format_time: {}".format(format_time))
    print("method 2 :format_time: {:%m/%d/%Y %I:%M %p}".format(combine_time))
    print("method 3 :format_time: {:{}}".format(combine_time, DATETIME_FORMAT))

    # monthrange(year, month)
    # Returns weekday of first day of the month and number of days in month, for the specified year and month.
    first_day, num_days = monthrange(2017, 4)
    # 0-6 ~ Mon-Sun
    print("first_day: {}".format(first_day))
    # number of days in month
    print("num_days: {}".format(num_days))

    # isocalendar
    today = date.today()
    print("today:", today)
    print(today.isocalendar())
    print(today.isocalendar()[1])  # 第幾周

    # datetime -> timestamp(10-digit)
    # time.mktime(t)
    # Its argument is the struct_time or full 9-tuple and it returns a floating point number,
    # for compatibility with time().
    timestamp = time.mktime(now.timetuple())
    print("timestamp : {}".format(timestamp))

    # timestamp(10-digit) -> datetime
    datetime_date = datetime.fromtimestamp(timestamp)
    print("datetime : {}".format(datetime_date))

    # millisecond-precise timestamp(13-digit) -> datetime
    timestamp = 1671094228814  # 13-digit
    datetime_date = datetime.fromtimestamp(int(timestamp) / 1000)
    print("datetime : {}".format(datetime_date))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\decimal_tutorial.py

# ref.
# https://docs.python.org/3.9/library/decimal.html

import decimal

# python3
# Solve the accuracy problem


def exmaple_1():
    print(decimal.Decimal(3.499))
    print(decimal.Decimal("3.499"))  # It is recommended to use str.


def exmaple_2():
    float_a = 1.0
    float_b = 0.8
    print("float_a-float_b = ", float_a - float_b)


def exmaple_2_fix():
    decimal_a = decimal.Decimal("1.0")
    decimal_b = decimal.Decimal("0.8")
    print("float_decimal-float_decimal = ", decimal_a - decimal_b)


def exmaple_3():
    print(round(1.5))
    print(round(2.5))


def exmaple_3_fix():
    # ROUND_HALF_UP is the same as Python 2.X's old behavior.
    print(
        decimal.Decimal("1.5").quantize(
            decimal.Decimal("1."), rounding=decimal.ROUND_HALF_UP
        )
    )
    print(
        decimal.Decimal("2.5").quantize(
            decimal.Decimal("1."), rounding=decimal.ROUND_HALF_UP
        )
    )


def exmaple_4():
    # ROUND_HALF_UP is the same as Python 2.X's old behavior.
    print(
        decimal.Decimal(3.501).quantize(
            decimal.Decimal("1."), rounding=decimal.ROUND_HALF_UP
        )
    )
    print(
        decimal.Decimal("3.501").quantize(
            decimal.Decimal("1."), rounding=decimal.ROUND_HALF_UP
        )
    )
    print(
        decimal.Decimal(3.4999).quantize(
            decimal.Decimal("1."), rounding=decimal.ROUND_HALF_UP
        )
    )
    print(
        decimal.Decimal("3.4999").quantize(
            decimal.Decimal("1."), rounding=decimal.ROUND_HALF_UP
        )
    )


def exmaple_5():
    print(
        decimal.Decimal(3.501).quantize(
            decimal.Decimal("1."), rounding=decimal.ROUND_DOWN
        )
    )
    print(
        decimal.Decimal("3.501").quantize(
            decimal.Decimal("1."), rounding=decimal.ROUND_DOWN
        )
    )
    print(
        decimal.Decimal(3.4999).quantize(
            decimal.Decimal("1."), rounding=decimal.ROUND_DOWN
        )
    )
    print(
        decimal.Decimal("3.4999").quantize(
            decimal.Decimal("1."), rounding=decimal.ROUND_DOWN
        )
    )


def exmaple_6():
    a = 1.0 - 0.8
    print(decimal.Decimal(a))
    print(
        decimal.Decimal(a).quantize(decimal.Decimal("1."), rounding=decimal.ROUND_DOWN)
    )


if __name__ == "__main__":
    exmaple_1()
    # exmaple_2()
    # exmaple_2_fix()
    # exmaple_3()
    # exmaple_3_fix()
    # exmaple_4()
    # exmaple_5()
    # exmaple_6()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\decorator_inspect.py


import inspect


def autovacuum(method):
    assert method.__name__.startswith("_"), (
        "%s: autovacuum methods must be private" % method.__name__
    )
    method._autovacuum = True
    return method


class A:
    @autovacuum
    def _gc_file_store_A(self):
        print("run _gc_file_store_A")


class B:
    # @autovacuum
    def _gc_file_store_B(self):
        print("run _gc_file_store_B")


def is_autovacuum(func):
    """Return whether ``func`` is an autovacuum method."""
    return callable(func) and getattr(func, "_autovacuum", False)


class AutoVacuum:
    my_data = [A(), B()]

    def _run_vacuum_cleaner(self):
        """
        Perform a complete database cleanup by safely calling every
        ``@api.autovacuum`` decorated method.
        """
        for model in self.my_data:
            cls = type(model)
            for attr, func in inspect.getmembers(cls, is_autovacuum):
                print("work")
                func(model)
                print("attr:", attr)
                print("func:", func)


AutoVacuum()._run_vacuum_cleaner()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\decorator_lib.py

from functools import wraps
from decorator import decorator

# decorator (https://github.com/micheles/decorator)
# pip3 install decorator


@decorator
def func_log_use_lib(func, *args, **kw):
    print("call", func.__name__)
    result = func(*args, **kw)
    print("end", func.__name__)
    return result


# 原生 decorator
def func_log(func):
    @wraps(func)
    def wrapped():
        print("call", func.__name__)
        func()
        print("end", func.__name__)

    return wrapped


@func_log
def hello_log():
    print("hello")


@func_log_use_lib
def hello_log_use_lib():
    print("hello")


if __name__ == "__main__":
    hello_log()
    hello_log_use_lib()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\decorator_tutorial.py

from functools import wraps


# tutorial decorator with argument
def decorator(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        func(*args, **kwargs)

    return wrapped


def bold(func):
    @wraps(func)
    def wrapper():
        print("<b> level one")
        func()
        print("</b>")

    return wrapper


def italic(func):
    @wraps(func)
    def wrapper():
        print("<i> level two")
        func()
        print("</i>")

    return wrapper


@bold
@italic
def sandwich(data="my sandwich"):
    print(data)


@italic
@bold
def sandwich_worse(data="my sandwich worse"):
    print(data)


def elapsed_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(func.__name__, end_time)
        return res

    return wrapper


@elapsed_time
def elapsed_time_tutorial():
    time.sleep(2)


# function log
def func_log(func):
    @wraps(func)
    def wrapped():
        print("call", func.__name__)
        func()
        print("end", func.__name__)

    return wrapped


@func_log
def hello_log():
    print("hello")


# top function exception
def sub_command(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except IndexError:
            print("help_string")
        except Exception as e:
            print("please contact us:", e)

    return wrapped


@sub_command
def git_status():
    print("git_status")


if __name__ == "__main__":
    # tutorial_1
    sandwich()

    # The order is important
    # sandwich_worse()

    # tutorial_2
    # elapsed_time_tutorial()

    # tutorial_3
    # hello_log()

    # tutorial_4
    # git_status()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\defaultdict_tutorial.py

# defaultdict means that if a key is not found in the dictionary,
# then instead of a KeyError being thrown, a new entry is created.
# The type of this new entry is given by the argument of defaultdict.

from collections import defaultdict


def ex1():
    # For the first example, default items are created using int(), which will return the integer object 0.
    int_dict = defaultdict(int)
    print("int_dict[3]", int_dict[3])  # print int(), thus 0
    # For the second example, default items are created using list(), which returns a new empty list object.
    list_dict = defaultdict(list)
    print("list_dict[test]", list_dict["ok"])  # print list(), thus []
    # default
    dic_list = defaultdict(lambda: "test")
    dic_list["name"] = "twtrubiks"
    print("dic_list[name]", dic_list["name"])
    print("dic_list[sex]", dic_list["sex"])


def ex2_letter_frequency(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


if __name__ == "__main__":
    ex1()
    print(ex2_letter_frequency("sentence"))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\dict.fromkeys_tutorial.py

if __name__ == "__main__":
    """
    dictionary.fromkeys(sequence[, value])
    """
    seq = ("name", "age", "sex")

    dict_1 = dict.fromkeys(seq)
    print("dict_1", dict_1)
    dict_2 = dict.fromkeys(seq, 10)
    print("dict_2", dict_2)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\dictionary_get.py

# dict.get(key, default=None)


def example_1():
    # tuple 可以當作 dict 的 key
    my_dict_1 = {(1, 2): 5, (3, 4): 6, (5, 6): 7}
    print(my_dict_1[(1, 2)])

    # equal
    my_dict_2 = {1: {2: 5}}
    print(my_dict_2[1][2])


if __name__ == "__main__":
    dict_data = {"Name": "twtrubiks", "Age": 18}

    # dict common use
    print('dict["Name"] : {}'.format(dict_data["Name"]))

    # if key does not exist in dict --> error
    # print('dict["Name"] : {}'.format(dict_['height']))  # error

    # if key does not exist in dict --> use dict.get(key, default=None)
    print('dict["Name"] : {}'.format(dict_data.get("height", "default height")))

    # dict.pop
    print("dict_data: {}".format(dict_data))
    pop_data = dict_data.pop("Name", None)
    print("pop_data: {} from dict_data".format(pop_data))
    print("dict_data: {}".format(dict_data))

    numbers = [1, 2, 3]
    my_dict = {number: number * 2 for number in numbers}
    print(my_dict)  # {1: 2, 2: 4, 3: 6}
    example_1()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\dictionary_update.py

# dict.update([other])

if __name__ == "__main__":
    """
    The update() method adds element(s) to the dictionary if the key is not in the dictionary.
    If the key is in the dictionary, it updates the key with the new value.

    If update() is called without passing parameters, the dictionary remains unchanged.
    """

    # If the key is in the dictionary, it updates the key with the new value.
    dict_data = {"Name": "twtrubiks", "Age": 18}
    dict_data_update = {"Age": 20}
    dict_data.update(dict_data_update)
    print("dict_data :", dict_data)

    # if the key is not in the dictionary, adds element(s) to the dictionary
    dict_data_2 = {"Name": "twtrubiks", "Age": 18}
    dict_data_2.update({"color": "blue"})
    print("dict_data_2 :", dict_data_2)
    dict_data_2.clear()  # clear dict data
    print("dict_data_2 :", dict_data_2)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\dictionary_using_items.py

if __name__ == "__main__":
    # common way
    # dictory = {"first_name": "Alfred", "last_name": "Hitchcock"}
    #
    # for key in dictory:
    #     print("{} = {}".format(key, dictory[key]))

    # preferred way using items()
    dictionary = {"first_name": "twt", "last_name": "rubiks"}

    for key, val in dictionary.items():
        print("{} = {}".format(key, val))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\division_operators_tutorial.py

# division operators
# python3

print("5/2:", 5 / 2)
print("5//2:", 5 // 2)


print("5/3:", 5 / 3)
print("5//3:", 5 // 3)


print("5/5:", 5 / 5)
print("5//5:", 5 // 5)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\eafp.py

# LBYL: Look Before You Leap
# EAFP: Easier to Ask for Forgiveness than Permission -> python

if __name__ == "__main__":
    # violates EAFP coding style
    if os.path.exists("file.txt"):
        os.unlink("file.txt")

    # correspond EAFP coding style
    try:
        os.unlink("file.txt")
    # raised when file does not exist
    except OSError:
        pass

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\Enum_tutorial.py

from enum import Enum


class Color(Enum):
    red = 1
    green = 2
    blue = 3


def example_1():
    print("Color.red:", Color.red)
    print("repr(Color.red):", repr(Color.red))
    print("Color(1):", Color(1))
    member = Color.red
    print("member.name:", member.name)
    print("member.value:", member.value)


def example_2():
    animal = Enum("Animal", "ant bee cat dog")  # <1>
    # is equivalent to
    # >>> class Animal(Enum):
    # ...     ant = 1
    # ...     bee = 2
    # ...     cat = 3
    # ...     dog = 4
    print("animal:", animal)
    print("animal.ant:", animal.ant)
    print("animal.ant.value:", animal.ant.value)
    print("list(animal):", list(animal))


if __name__ == "__main__":
    example_1()
    example_2()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\enumerate_tutorial.py

if __name__ == "__main__":
    # The enumerate() method adds counter to an iterable and returns it (the enumerate object).
    # enumerate(iterable, start=0)
    number_list = ["a", "b", "c", "d", "e"]
    for index, value in enumerate(number_list, start=1):
        print("index: {} value: {}".format(index, value))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\escape_tutorial.py

# ref. https://docs.python.org/3/library/html.html
import html.parser

if __name__ == "__main__":
    test = '123>ss<see1&sd2"'
    escaped = html.escape(test, quote=True)
    print("escaped:", escaped)

    unescaped = html.unescape(test)
    print("unescaped:", unescaped)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\filter.py


def fn(x):
    return x if x > 3 else None


if __name__ == "__main__":
    # the filter() method filters the given iterable with the help of
    # a function that tests each element in the iterable to be true or not.
    # filter(function, iterable)
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = filter(fn, seq)
    print("result: {}".format(result))

    # lambda often used in like filter(), map() and reduce().
    items = filter(lambda x: x > 3, seq)
    print("result_lambda: {}".format(items))

    # filter object  (ref. map.py Compare the difference)
    data = [
        {"key": "a", "value": 1},
        {"key": "b", "value": 2},
        {"key": "c", "value": 3},
        {"key": "d", "value": 4},
        {"key": "e", "value": 4},
    ]
    data_items = filter(lambda x: x["value"] >= 3, data)
    print("data_items: {}".format(data_items))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\format.py

from datetime import datetime

# ref.  https://pyformat.info/
if __name__ == "__main__":
    print("%s %s" % ("one", "two"))  # old method
    print("{} {}".format("one", "two"))
    print("{0} {1}".format("one", "two"))
    print("{1} {0}".format("one", "two"))

    print("{:.2}".format(0.87666))
    print("{:.2%}".format(0.873))

    print("{:>10}".format("test"))
    print("{:.5}".format("abcdefgh"))

    print("{:d}".format(42))
    # print('{:d}'.format('42')) # error

    print("{:f}".format(3.141592653589793))
    print("{:.2f}".format(3.141592653589793))  # rounded to two decimal place
    # print('{:d}'.format(3.141592653589793)) # error
    print("{:0,}".format(31234.14159))  # Format with commas
    print(
        "{:0,.2f}".format(31234.14159)
    )  # rounded to two decimal place + Format with commas
    print("{:07d}".format(10))  # -> 0000010

    data_dic = {"first": "TWT", "last": "rubiks"}
    print("%(first)s %(last)s" % data_dic)  # old method
    print("{first} {last}".format(**data_dic))

    data = [4, 8, 15, 16, 23, 42]
    print("{d[4]} {d[5]}".format(d=data))

    # datetime format
    print("{:%Y-%m-%d %H:%M}".format(datetime(2017, 2, 3, 4, 5)))
    DATETIME_FORMAT = "%Y-%m-%d %H:%M"
    print("{:{}}".format(datetime(2017, 2, 3, 4, 5), DATETIME_FORMAT))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\freezegun_tutorial.py

# freezegun (https://github.com/spulec/freezegun)
# pip3 install freezegun

from freezegun import freeze_time
from datetime import datetime


# Decorator
@freeze_time("2021-10-10")
def example_1():
    assert datetime.now() == datetime(2021, 10, 10)


# Context manager
def example_2():
    assert datetime.now() != datetime(2021, 10, 10)
    with freeze_time("2021-10-10"):
        assert datetime.now() == datetime(2021, 10, 10)
    assert datetime.now() != datetime(2021, 10, 10)


# Raw use
def example_3():
    freezer = freeze_time("2021-10-10 10:00:00")
    freezer.start()
    assert datetime.now() == datetime(2021, 10, 10, 10, 0, 0)
    freezer.stop()
    assert datetime.now() != datetime(2021, 10, 10, 10, 0, 0)


# tick argument
@freeze_time("2021-10-10", tick=True)
def example_4():
    print(datetime.now())  # 2021-10-10 00:00:00
    time.sleep(5)
    assert datetime.now() > datetime(2021, 10, 10)
    print(datetime.now())  # 2021-10-10 00:00:05


# auto_tick_seconds
@freeze_time("2021-10-10", auto_tick_seconds=15)
def example_5():
    print(datetime.now())  # 2021-10-10 00:00:00
    print(datetime.now())  # 2021-10-10 00:00:15


if __name__ == "__main__":
    example_1()
    # example_2()
    # example_3()
    # example_4()
    # example_5()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\function_default.py

# REF.
# http://blog.thedigitalcatonline.com/blog/2015/02/11/default-arguments-in-python/#.WPg_61OGPwc


def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default


def get_test(iterable, default="yo"):
    return "{} {}".format(iterable, default)


if __name__ == "__main__":
    print(get_test("t1"))
    print(get_test("t1", "t2"))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\functools_partial_tutorial.py

from functools import partial

from operator import mul


def link_string(x, y):
    print("{}_{}".format(x, y))


def example_1():
    result = partial(link_string, y="data")
    result("test_1")
    result("test_2")


def example_1_2():
    # x = 'data'
    result = partial(link_string, "data")
    result("test_1")
    result("test_2")


def example_2():
    ten_times = partial(mul, 10)
    print(ten_times(8))
    print(ten_times(10))
    print(list(map(ten_times, range(1, 5))))


if __name__ == "__main__":
    example_1()
    # example_1_2()
    # example_2()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\groupby_tutorial.py

from itertools import groupby

"""
ref. https://docs.python.org/3.6/library/itertools.html#itertools.groupby

itertools.groupby(iterable, key=None)

"""
if __name__ == "__main__":
    things = [
        ("apple", "bear"),
        ("cherry", "bear"),
        ("banana", "duck"),
        ("cherry", "bear"),
        ("banana", "cactus"),
        ("cherry", "bear"),
        ("cherry", "bear"),
        ("apple", "speed boat"),
        ("apple", "school bus"),
    ]

    # Generally, the iterable needs to already be sorted on the same key function.  important!!
    things = sorted(things, key=lambda x: x[0])

    for key, group in groupby(things, lambda x: x[0]):
        print("key", key)
        print("group", list(group))
        print("==================")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\groupby_tutorial_find_consecutive_numbers.py

# ref. https://docs.python.org/3.0/library/itertools.html#examples
from itertools import groupby
from operator import itemgetter

"""
seqs=[1,6,7,8,10,11]
index   value    (index-value)
  0      1          -1
  1      6          -5
  2      7          -5
  3      8          -5
  4      10         -6
  5      11         -6

[6,7,8]  [10,11]
"""

data = [1, 6, 7, 8, 10, 11]

for key, group in groupby(enumerate(data), lambda x: x[0] - x[1]):
    g = list(map(itemgetter(1), group))  # method_1
    # g = list(map(lambda x: x[1], group)) # method_2
    print("consecutive numbers", g)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\is_integer_tutorial.py

# ref. https://docs.python.org/3.6/library/stdtypes.html#float.is_integer

import unittest

"""
float.is_integer()
Return True if the float is an integer
"""


def check_is_integer(number):
    result = float(number).is_integer()
    return result


class TestCase(unittest.TestCase):
    def test_case_1(self):
        result = check_is_integer(-2.00)
        self.assertTrue(result)

    def test_case_2(self):
        result = check_is_integer(12.00000)
        self.assertTrue(result)

    def test_case_3(self):
        result = check_is_integer(-3.1)
        self.assertFalse(result)

    def test_case_4(self):
        result = check_is_integer(1.100)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\isdigit.py

if __name__ == "__main__":
    # The isdigit() method returns True if all characters in a string are digits. If not, it returns False.
    # True if all characters in the string are digits.
    # False if at least one character is not a digit.
    s = "28212"
    print(s.isdigit())

    # contains alphabets and spaces
    s = "Mo3 nicaG el l22er"
    print(s.isdigit())

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\isinstance.py

if __name__ == "__main__":
    # The isinstance() function checks if the object (first argument)
    # is an instance or subclass of classinfo class (second argument).

    # isinstance(object, classinfo)
    # object - object to be checked
    # classinfo - class, type, or tuple of classes and types

    class Foo(object):
        a = 5

    fooInstance = Foo()

    print("instance of Foo? {}".format(isinstance(fooInstance, Foo)))

    numbers = [1, 2, 3]

    is_list = isinstance(numbers, list)
    print("instance of list? {}".format(is_list))

    is_dic = isinstance(numbers, dict)
    print("instance of dict? {}".format(is_dic))

    is_dic_or_list = isinstance(numbers, (dict, list))
    print("instance of dict or list? {}".format(is_dic_or_list))

    is_int = isinstance(numbers, int)
    print("instance of int? {}".format(is_int))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\itemgetter_tutorial.py

# ref. https://docs.python.org/3/library/operator.html#operator.itemgetter

from operator import itemgetter

# Basic tutorial
seqs = [1, 2, 3, 4]
x = itemgetter(1)
print("x:", x)
value = x(seqs)
print("value == x(seqs) == seqs[1]:", value)
xs = itemgetter(1, 3)
value2 = xs(seqs)
print("value2:", value2)

# Example of using itemgetter() to retrieve specific fields from a tuple record
inventory = [("apple", 3), ("banana", 2), ("pear", 5), ("orange", 1)]
getcount = itemgetter(1)
print("list(map(getcount, inventory)):", list(map(getcount, inventory)))
print("sorted(inventory, key=getcount):", sorted(inventory, key=getcount))

print("------------------------------------------------------------")  # 60個

from collections.abc import Iterable, Iterator


# The iter() method returns an iterator for the given object.

# The syntax of iter() method is
# iter(object[, sentinel])


# The iterator protocol
# Any class that provides an __iter__ method is iterable;
# that method must return an Iterator instance that will cover
# all the elements in that class.
# Since an iterator is already looping over elements,
# its __iter__ function traditionally return itself.

# Iterable - __iter__  (for in), iter(Iterable) -> Iterator
# Iterator - __next__ + __iter__


class PrintNumber:
    def __init__(self, max_number):
        self.max_number = max_number

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num >= self.max_number:
            raise StopIteration
        self.num += 1
        return self.num


def example_1():
    print_mum = PrintNumber(3)

    print_mum_iter = iter(print_mum)

    # prints '1'
    print(next(print_mum_iter))

    # prints '2'
    print(next(print_mum_iter))

    # prints '3'
    print(next(print_mum_iter))

    # raises StopIteration
    print(next(print_mum_iter))


class CapitalIterable:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)


class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self


def example_2():
    iterable = CapitalIterable("the aa bb cc dd")
    print("isinstance(iterable,Iterable):", isinstance(iterable, Iterable))
    iterator = iter(iterable)
    print("isinstance(iterator,Iterator):", isinstance(iterator, Iterator))
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

    for i in iterable:
        print(i)


if __name__ == "__main__":
    example_1()
    # example_2()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\itertools_islice_tutorial.py

# https://docs.python.org/3.7/library/itertools.html#itertools.islice
from itertools import islice

"""
itertools.islice(iterable, start, stop[, step])

Make an iterator that returns selected elements from the iterable. 
If start is non-zero, then elements from the iterable are skipped until 
start is reached. Afterward, elements are returned consecutively unless 
step is set higher than one which results in items being skipped. 
If stop is None, then iteration continues until the iterator is exhausted, 
if at all; otherwise, it stops at the specified position.  
"""
if __name__ == "__main__":
    # islice('ABCDEFG', 2)  --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G

    print(tuple(islice("ABCDEFG", 2)))  # --> A B
    print(list(islice("ABCDEFG", 2, 4)))  # --> C D

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\itertools_tee_tutorial.py

# https://docs.python.org/3.7/library/itertools.html#itertools.tee
from itertools import tee

"""
itertools.tee(iterable, n=2)
Return n independent iterators from a single iterable.
"""
if __name__ == "__main__":
    print(
        tee([1, 2, 3, 4])
    )  # (<itertools._tee object at 0x02EDA508>, <itertools._tee object at 0x02EDD1E8>)
    iter1, iter2 = tee([1, 2, 3, 4])
    print(next(iter1))
    print(next(iter1))
    print(next(iter2))
    print(list(iter1))
    print(list(iter2))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\itertools_tutorial.py

import itertools
import operator


def example_1():
    # itertools.count(start=0, step=1)
    gen_1 = itertools.count(1, 2)
    print(next(gen_1))
    print(next(gen_1))
    print(next(gen_1))
    print(next(gen_1))
    print(next(gen_1))


def example_2():
    # it produces a generator that consumes
    # another generator and stops when a given predicate evaluates to False .
    # So we can combine the two and write this:
    gen_2 = itertools.takewhile(lambda n: n < 5, itertools.count(0, 1))
    print(list(gen_2))


def my_key(c):
    return c.lower() in "abcde"


def example_3():
    print(list(filter(my_key, "AbXHJsuaiqm")))
    print(list(itertools.filterfalse(my_key, "AbXHJsuaiqm")))


def example_4():
    # dropwhile(predicate, it)
    # Consumes it skipping items while predicate computes truthy, then
    # yields every remaining item (no further checks are made)
    print(list(itertools.dropwhile(my_key, "AbXHJsuaiqm")))


def example_5():
    # takewhile(predicate, it)
    # Yields items while predicate computes truthy, then stops and
    # no further checks are made
    print(list(itertools.takewhile(my_key, "AbXHJsuaiqm")))


def example_6():
    # compress(it, selector_it)
    # Consumes two iterables in parallel; yields items from it whenever the
    # corresponding item in selector_it is truthy
    print(list(itertools.compress("abcdefg", (1, 0, 1, 1, 0, 1))))


def example_7():
    # accumulate(p [,func])
    # p0, p0+p1, p0+p1+p2
    print(list(itertools.accumulate([1, 2, 3, 4, 5])))
    print(list(itertools.accumulate([9, 4, 2, 0, 5, 8], min)))
    print(list(itertools.accumulate([1, 0, 9, 2, 10], max)))
    print(list(itertools.accumulate([1, 2, 3, 4, 5], operator.mul)))


def example_8():
    # enumerate(iterable, start=0)
    print(list(enumerate("abcdefg", 0)))


def example_9():
    # Yield all items from it1 , then from it2 etc., seamlessly
    # chain(it1, ..., itN)
    print(list(itertools.chain("abcdef", range(8))))


def example_10():
    # zip_longest(it1, ...,itN, fillvalue=None)
    print(list(itertools.zip_longest("ab", range(6))))
    print(list(itertools.zip_longest("ab", range(6), fillvalue="@")))


def example_11():
    print(list(itertools.product("ab", range(3))))  # 3*2 = 6(tuple)

    data = [1, 2, 3, 4]
    print(list(itertools.product("ab", data)))  # 4*2 = 8(tuple)

    print(list(itertools.product("abc", repeat=2)))

    print(list(itertools.product(range(2), repeat=4)))


def example_12():
    cy = itertools.cycle("abc")
    for _ in range(10):
        print(next(cy))


def example_13():
    rp = itertools.repeat("b")  # forever. b
    for _ in range(10):
        print(next(rp))

    print(list(itertools.repeat("c", 4)))  # repeat 4 times


def example_14():
    print(list(itertools.combinations("ABCD", 2)))
    print(list(itertools.combinations_with_replacement("ABCD", 2)))


def example_15():
    print(list(itertools.permutations("ABCD", 2)))


if __name__ == "__main__":
    # example_1()
    # example_2()
    # example_3()
    # example_4()
    # example_5()
    # example_6()
    # example_7()
    # example_8()
    # example_9()
    # example_10()
    # example_11()
    # example_12()
    # example_13()
    # example_14()
    example_15()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\join.py

if __name__ == "__main__":
    # The join() is a string method which returns a string concatenated with the elements of an iterable.
    numList = ["1", "2", "3", "4"]
    seperator = ", "
    print(seperator.join(numList))

    num_int = [1, 2, 3, 4]
    # print(seperator.join(num_int)) # error
    print(seperator.join(str(x) for x in num_int))

    numTuple = ("1", "2", "3", "4")
    print(seperator.join(numTuple))

    seq = {"Python", "Java", "Ruby"}
    s = "->->"
    print(s.join(seq))

print("------------------------------------------------------------")  # 60個


def everything(*args):
    for count, thing in enumerate(args):
        print("{0}. {1}".format(count, thing))


# **kwargs allows you to handle named arguments that you have not defined in advance
def table_things(**kwargs):
    print("apple: {}".format(kwargs.get("apple", "default")))
    for name, value in kwargs.items():
        print("{0} = {1}".format(name, value))


def print_three_things(a, b, c):
    print("a = {0}, b = {1}, c = {2}".format(a, b, c))


if __name__ == "__main__":
    everything("apple", "banana", "cabbage")
    table_things(apple="fruit", cabbage="vegetable")
    my_list = ["aardvark", "baboon", "cat"]
    print_three_things(*my_list)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\lambda.py


def show_max(m, n):
    return m if m > n else n


if __name__ == "__main__":
    # anonymous functions
    # often used in like filter(), map() and reduce(). ref. filter.py  map.py

    # common def
    print("show_max:{}".format(show_max(100, 5)))  # show 100 (common def)

    # lambda
    show_lambda = lambda m, n: m if m > n else n  # but PEP-8 recommend use def
    print("show_lambda:{}".format(show_lambda(100, 5)))  # show 100 (lambda)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\list_tutorial.py

if __name__ == "__main__":
    data_list = ["a", "e", "i", "o", "i", "u"]

    # element 'i' is searched
    index = data_list.index("i")

    # index is printed
    print("The index of e: {}".format(index))

    # list remove
    del data_list[0]
    print("data_list:", data_list)
    data_list.remove("e")
    print("data_list:", data_list)

    # apply
    target_sort = ["2", "1", "3", "8", "0"]
    oringin = ["0", "1", "2", "3", "8"]
    result = sorted(oringin, key=lambda x: target_sort.index(x))
    print(result)

    # reverse - method 1
    demo_list = [5, 4, 3, 2, 1]
    demo_list.reverse()
    print("demo_list", demo_list)
    # reverse - method 2
    demo_list_2 = [5, 4, 3, 2, 1]
    print("demo_list_2[::-1]", demo_list_2[::-1])

print("------------------------------------------------------------")  # 60個


def contains_magic_number(list1, magic_number):
    for i in list1:
        if i == magic_number:
            print("This list contains the magic number")
            # if not add break , will run more meaningless loop
            break
        else:
            print("This list does NOT contain the magic number")


if __name__ == "__main__":
    contains_magic_number(range(10), 3)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\map_tutorial.py

if __name__ == "__main__":
    # The map() function applies a given function to each item of an iterable (list, tuple etc.)
    # and returns a list of the results.

    # tutorial_1
    numbers = (1, 2, 3, 4)
    # lambda often used in like filter(), map() and reduce().
    result = map(lambda x: x * x, numbers)
    print("result: {}".format(result))

    # filter object  (ref. filter.py Compare the difference)
    data = [
        {"key": "a", "value": 1},
        {"key": "b", "value": 2},
        {"key": "c", "value": 3},
        {"key": "d", "value": 4},
        {"key": "e", "value": 4},
    ]

    data_items = map(lambda x: x["value"], data)
    print("data_items: {}".format(data_items))
    print("data_items_distinct: {}".format(set(data_items)))

    # tutorial_2
    str_num = "1,2,3,4,5,6,7,8,9,10,11"
    int_seqs = list(map(int, str_num.split(",")))  # python3
    # int_seqs = map(int, str_num.split(','))  # python2
    print(isinstance(int_seqs, list))
    for seq in int_seqs:
        print(isinstance(seq, int))
        print(seq)

    # tutorial_3
    pattern = "abcidkeujaddcsjb"
    print(list(map(pattern.find, pattern)))


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\MappingProxyType_tutorial.py

# ref.
# https://docs.python.org/3/library/types.html#types.MappingProxyType

####
# class types.MappingProxyType(mapping)¶
#    Read-only proxy of a mapping.
#     It provides a dynamic view on the mapping’s entries,
#     which means that when the mapping changes, the view reflects these changes.
###

from types import MappingProxyType

d = {"a": "A"}
d_proxy = MappingProxyType(d)
print(d_proxy)  # mappingproxy({a: 'A'})
print(d_proxy["a"])  # 'A'

# d_proxy['b'] = 'B'
# # Exception has occurred: TypeError
# #'mappingproxy' object does not support item assignment

d["b"] = "B"
print(d)  # {'a': 'A', 'b': 'B'}
print(d_proxy)  # {'a': 'A', 'b': 'B'}
print(d_proxy["b"])  # B

print("------------------------------------------------------------")  # 60個

if __name__ == "__main__":
    """
    https://docs.python.org/3/library/math.html
    """

    # 無條件進位到整數
    print(math.ceil(2.00001))

    # 無條件捨去到整數
    print(math.floor(2.99999))

    # 無條件進位到小數點第2位
    print(math.ceil(2.55 * 10) / 10)

    # 無條件進位到小數點第2位
    print(math.ceil(2.54 * 10) / 10)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\methodcaller_tutorial.py

# ref.
# https://docs.python.org/3/library/operator.html#operator.methodcaller

from operator import methodcaller


def example_1():
    s = "a b c d e"
    upcase = methodcaller("upper")
    print(upcase(s))

    # Equivalent
    print(s.upper())


class A:
    def fun_2(self, data_1, data_2):
        print("{} + {}".format(data_1, data_2))

    def example_3(self):
        fun_3_case = methodcaller("fun_2", "data_3_1", "data_3_2")
        fun_3_case(self)


def example_2():
    a_obj = A()
    fun_2_case = methodcaller("fun_2", "data_1", "data_2")
    fun_2_case(a_obj)

    # Equivalent
    a_obj.fun_2("data_1", "data_2")


def example_3():
    a3_obj = A()
    a3_obj.example_3()


if __name__ == "__main__":
    example_1()
    # example_2()
    # example_3()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\namedtuple_tutorial.py

from collections import namedtuple


class NetworkAddressClass(object):
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port


if __name__ == "__main__":
    print("=== use namedtuple ===")
    NetworkAddress = namedtuple("NetworkAddress", ["hostname", "port"])  # write 1
    # NetworkAddress = namedtuple('NetworkAddress', 'hostname port') # write 2
    print(
        "NetworkAddress._fields", NetworkAddress._fields
    )  # _fields is a tuple with the field names of the class

    a = NetworkAddress("localhost", 3306)
    print("a.hostname:", a.hostname)
    print("a.port:", a.port)
    # a.port = 80  # error , tuple read only

    network_address_data = ("hello", 1234)
    na_1 = NetworkAddress._make(network_address_data)  # write 1
    na_2 = NetworkAddress(*network_address_data)  # write 2
    print("na_1", na_1)
    print("na_2", na_2)

    # _asdict() return a collections.OrderedDict
    # That can be used to produce a nice display of data
    print("na_1._asdict()", na_1._asdict())

    print("=== use class ===")
    b = NetworkAddressClass("localhost", 3306)
    print("b.hostname:", b.hostname)
    print("b.port:", b.port)
    b.port = 80

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\nested_loop_tutorial.py

if __name__ == "__main__":
    """
    common write method
    """
    results = []
    for i in range(10):
        for j in range(i):
            results.append((i, j))
    print("results", results)

    """
        better write method 1
    """

    results = [(i, j) for i in range(10) for j in range(i)]
    print("results", results)

print("------------------------------------------------------------")  # 60個

# An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
from collections import OrderedDict

if __name__ == "__main__":
    order_dic = OrderedDict()
    order_dic["a"] = "A"
    order_dic["b"] = "B"
    order_dic["c"] = "C"
    order_dic["d"] = "D"
    order_dic["e"] = "E"

    for k, v in order_dic.items():
        print(k, v)

    # https://docs.python.org/3/library/collections.html#collections.OrderedDict.popitem
    # last=True -> LIFO
    # last=False -> FIFO

    print(order_dic.popitem(last=True))  # -> ('e', 'E')

    print(order_dic.popitem(last=False))  # -> ('a', 'A')

    # https://docs.python.org/3/library/collections.html#collections.OrderedDict.move_to_end
    # last=True   -> The item is moved to the right end
    # last=False  -> The item is moved to the beginning

    print("origin:", order_dic)  # OrderedDict([('b', 'B'), ('c', 'C'), ('d', 'D')])
    order_dic.move_to_end("b", last=True)
    print(order_dic)  # OrderedDict([('c', 'C'), ('d', 'D'), ('b', 'B')])
    order_dic.move_to_end("b", last=False)
    print(order_dic)  # OrderedDict([('b', 'B'), ('c', 'C'), ('d', 'D')])

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\parse_dateutil.py

from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime

if __name__ == "__main__":
    """
    ref. http://dateutil.readthedocs.io/en/stable/parser.html
    """
    print(parse("2017/4  /4 4:00:00 PM "))
    print(parse("2017/4  -4 16:00:00  "))

    """
    ref. https://dateutil.readthedocs.io/en/stable/relativedelta.html
    """
    now = datetime.now()
    now_plus_1_month = now + relativedelta(months=+1)
    now_minus_1_month = now + relativedelta(months=-1)
    print("now", now)
    print("now_plus_1_month", now_plus_1_month)
    print("now_minus_1_month", now_minus_1_month)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\pathlib_tutorial.py

from pathlib import Path


def demo1():
    path_1 = Path("/twtrubiks") / Path("hello")
    print(path_1)  # PosixPath('/twtrubiks/hello')
    print(str(path_1))

    path_2 = Path("/twtrubiks") / "hello" / "world"
    print(path_2)

    path_3 = Path("/twtrubiks") / "hello" / Path("world")
    print(path_3)

    path_4 = Path("/twtrubiks").joinpath("test1", "test2/test3")
    print(path_4)

    path_5 = Path("/twtrubiks", "test2", "test3")
    print(path_5)

    print("絕對路徑:", path_5.absolute())

    print("比對路徑:")
    if Path("/twtrubiks") == Path("hello"):
        print("相同")
    else:
        print("不相同")

    print("命令列上 執行位置路徑:", Path(__file__))

    print("目前路徑:", Path.cwd())
    print("home 路徑:", Path.home())

    # 擁有者
    print("擁有者:", Path.cwd().owner())


def demo2():
    path = Path(Path.cwd(), "myfile.txt")
    if path.exists():
        print("已存在")
    else:
        print("不存在, 建立檔案")
        path.touch()
        print("已經建立")
        print("是否存在:", path.exists())
        # path.unlink() # 刪除路徑檔案


def demo3():
    path = Path(Path.cwd(), "myfile.txt")
    print("path.resolve():", path.resolve())
    print(path.name)
    print("檔名:", path.stem)
    print("副檔名:", path.suffix)
    print("is_file:", path.is_file())
    print("is_dir:", path.is_dir())
    print("is_symlink:", path.is_symlink())
    print("檔案大小:", path.stat())
    print("檔案大小:", path.stat().st_size)  # bytes
    print("取出全部副檔名:", Path("test.tar.bz1").suffixes)


def demo4():
    # 簡單檔案讀寫
    path = Path(Path.cwd(), "myfile.txt")
    print("讀檔:", path.read_text())

    path.write_text("Hello")
    print("讀檔:", path.read_text())

    with path.open("w") as f:
        f.write("Hello 123")
    print("讀檔:", path.read_text())


def demo5():
    # 走訪某資料夾內的所有檔案與資料夾
    my_path = Path.cwd()
    for f in Path(my_path).iterdir():
        print(f.name)


def demo6():
    print("查看上層目錄")
    path = Path("/twtrubiks/a1/a2/a3/test.py")
    print(path.parent)
    print(path.parent.parent)

    print("查看全部上層目錄")
    for path in path.parents:
        print(path.parent)


def demo7():
    path = Path.cwd()
    data = list(Path(path).glob("*.py"))
    print("路徑下全部有 .py 結尾的檔案:", data)


def demo8():
    # https://docs.python.org/3/library/pathlib.html#pathlib.Path.expanduser
    """
    Return a new path with expanded ~ and ~user constructs, as returned by os.path.expanduser().
    If a home directory cant be resolved, RuntimeError is raised.
    """
    p = Path("~/hello/test123")
    print(p.expanduser())


def demo9():
    # https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.with_suffix
    path = Path(Path.cwd(), "test.json")
    print("with_suffix")
    print(path)
    print(path.with_suffix(""))
    print(path.with_suffix(".py"))
    print(path.with_suffix(".zip"))

    # https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.with_name
    path = Path.cwd()
    print("with_name")
    print(path)
    print(path.with_name("test.py"))
    print(path.with_name("a123.222"))


def demo10():
    path = Path.cwd()
    n_path = path / Path("p1/p2/p3/test.py")
    print("階層建立資料夾:")
    n_path.mkdir(parents=True)


if __name__ == "__main__":
    demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    # demo6()
    # demo7()
    # demo8()
    # demo9()
    # demo10()


print("------------------------------------------------------------")  # 60個


class Square(object):
    def __init__(self, length):
        self._length = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @length.deleter
    def length(self):
        del self._length


if __name__ == "__main__":
    r = Square(5)
    print("length", r.length)  # automatically calls getter
    r.length = 6  # automatically calls setter
    print("length", r.length)
    del r.length
    # print('length', r.length)  # -> AttributeError: 'Square' object has no attribute '_length'

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\queue_tutorial.py

from queue import Queue

# Queue is thread-safe.

# if the operation cannot successfully complete because the queue is either empty (cant get) or full ( cant put).
# The default behavior is to block or idly wait until the Queue object has data or room available to
# complete the operation.
# You can have it raise exceptions instead by passing the block=False parameter.
# Or you can have it wait a defined amount of time before raising an exception by passing a timeout parameter


def fifo_ex():
    # FIFO
    lineup = Queue(maxsize=3)
    # lineup.get(block=False)
    lineup.put(1)
    lineup.put(2)
    lineup.put(3)
    # lineup.put(4, timeout=1)
    print("lineup.full():", lineup.full())
    print(lineup.get())
    print(lineup.get())
    print(lineup.get())
    print("lineup.empty():", lineup.empty())


def lifo_ex():
    # LIFO, also called stacks ()
    # Applicable situation - concurrent
    # why not use list
    from queue import LifoQueue

    stack = LifoQueue(maxsize=3)
    stack.put(1)
    stack.put(2)
    stack.put(3)
    # stack.put(4, block=False)
    print(stack.get())
    print(stack.get())
    print(stack.get())
    # stack.get(timeout=1)


def priority_queue_ex():
    # data structure - heap
    # Applicable situation - product recommendation
    from queue import PriorityQueue

    pq = PriorityQueue()
    pq.put((5, "c"))
    pq.put((2, "a"))
    pq.put((1, "b"))
    pq.put((4, "d"))
    while not pq.empty():
        print(pq.get())


def priority_queue_ex_2():
    from queue import PriorityQueue

    pq = PriorityQueue()
    pq.put((-5, "c"))
    pq.put((-2, "a"))
    pq.put((-1, "b"))
    pq.put((-4, "d"))
    while not pq.empty():
        print(pq.get())


if __name__ == "__main__":
    fifo_ex()
    # lifo_ex()
    # priority_queue_ex()
    # priority_queue_ex_2()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\raise_an_exception_from_function_call.py

# If a function that is supposed to return a given type (e.g. list, tuple, dict)
# suddenly returns something else (e.g. None) the caller of that function will always
# need to check the type of the return value before proceeding. This makes for confusing
# and complex code. If the function is unable to produce the supposed return value
# it is better to raise an exception that can be caught by the caller instead.

# exceptions.Exception  REF. https://docs.python.org/3.4/library/exceptions.html#exceptions.Exception


# Anti-pattern
def get_secret_code_anti_pattern(password):
    if password != "bicycle":
        return None
    else:
        return "42"


# Raise an exception when an error is encountered or a precondition is unsatisfied
def get_secret_code(password):
    if password != "bicycle":
        raise ValueError
    else:
        return "42"


if __name__ == "__main__":
    # Anti-pattern
    secret_code_anti_pattern = get_secret_code_anti_pattern("unicycle")

    if secret_code_anti_pattern is None:
        print("Wrong password. (Anti-pattern) ")
    else:
        print("The secret code is {}".format(secret_code_anti_pattern))

    # Raise an exception when an error is encountered or a precondition is unsatisfied
    try:
        secret_code = get_secret_code("unicycle")
        print("The secret code is {}".format(secret_code))
    except ValueError as e:
        print("Wrong password.")
        print(isinstance(e, ValueError))  # e belong ValueError
        print(isinstance(e, Warning))  # e does not belong Warning

print("------------------------------------------------------------")  # 60個

import re

"""
ref.
https://docs.python.org/3/library/re.html 
http://www.runoob.com/python/python-reg-expressions.html
https://goo.gl/cPmofe

使用 re module 之前，先思考一下你的問題是否可以用其他方法解決，
像是 replace , split , translate
"""

if __name__ == "__main__":
    """
    re.sub(pattern, repl, string, count=0, flags=0)
    """

    # ex1. 符合 "a", "b", 或 "c" 中的任意一個字
    str_ex1 = "1a2b3c4d"
    num = re.sub(r"[abc]", "", str_ex1)
    print("num:", num)

    # ex2. 符合 "a", "b", 或 "c" 中的任意一個字, a 到 c 區間
    # str_ex2 = "1a2b3c4d"
    # num = re.sub(r'[a-c]', "", str_ex2)
    # print('num:', num)

    # ex1 和 ex2 功能相同

    # ex3. 符合小寫英文字母
    # str_ex3 = "1a2b3c4dABC"
    # num = re.sub(r'[a-z]', "", str_ex3)
    # print('num:', num)

    # ex4. [^5] 將符合除了 "5" 之外的任意字
    # str_ex4 = "1a2b3c4dABC55"
    # num = re.sub(r'[^5]', "", str_ex4)
    # print('num:', num)

    # ex5. [abc$] 將符合 "a" , "b" , "c" , "$"
    # str_ex5 = "d1abs$"
    # num = re.sub(r'[abc$]', "", str_ex5)
    # print(num)

    """
    非常重要的字符為反斜槓 "\" ，
    如果你需要匹配 "[" 或 \"""，你可以在它們之前用"\"來取消它們的特殊意義： \[ 或 \"。
    
    這類特殊字符都可以包含在一個字符類中。如 [\s,.] 字符類將匹配任何空白字符或 "," 或 "."
    """

    # ex6_1
    # str_ex6_1 = "swedaf\"gb"
    # print(str_ex6_1)
    # num = re.sub(r"\"", "", str_ex6_1)
    # print(num)

    # ex6_2
    # str_ex6_2 = "swedaf[gb"
    # print(str_ex6_2)
    # num = re.sub(r'\[', "", str_ex6_2)
    # print(num)

    """
    \d  匹配任何十進制數；它相當於類 [0-9]。
    \D  匹配任何非數字字符；它相當於類 [^0-9]。
    \s  匹配任何空白字符；它相當於類  [ "t"n"r"f"v]。 
    \S  匹配任何非空白字符；它相當於類 [^ "t"n"r"f"v]。 
    \w  匹配任何字母數字字符；它相當於類 [a-zA-Z0-9_]。
    \W  匹配任何非字母數字字符；它相當於類 [^a-zA-Z0-9_]。
    """

    """
    正則表達式通常在 Python 中都用這種 raw 字符表示。
    在字符前加個 "r" 反斜槓就不會被任何特殊方式處理，
    所以 r"\n" 就是包含"\" 和 "n" 的兩個字，
    而 "\n" 則是一個字，表示一個換行。
    """
    # ex7_1
    # print("\n")
    # print("len:", len("\n"))
    # ex7_2
    # print(r"\n")
    # print("len:", len(r"\n"))
    # ex7_3  符合 \section
    # str_ex7_3 = "aaa\sectionbc"
    # print('origin:', str_ex7_3)
    # num = re.sub(r'\\section', "", str_ex7_3)
    # print('new:', num)

    """        
    match()	    決定 RE 是否在字符串剛開始的位置匹配
    search()	掃瞄字符串，找到這個 RE 匹配的位置
    findall()	找到 RE 匹配的所有子串，並把它們作為一個列表返回
    finditer()	找到 RE 匹配的所有子串，並把它們作為一個迭代器返回
    
    如果沒有匹配到的話，match() 和 search() 將返回 None。
    如果成功的話，就會返回一個 `MatchObject` 實例。
    
    """

    """
    re.match
    re.match(pattern, string, flags=0)
    """
    # ex8_1 回傳 None
    # '+' 的意思是 「一個或更多的重複次數」
    # num = re.match(r'[a-z]+', '')
    # print(num)
    # ex8_2 回傳一個 MatchObject
    # num = re.match(r'[a-z]+', 's')
    # print(num)

    """
    group()	返回被 RE 匹配的字符串
    start()	返回匹配開始的位置
    end()	返回匹配結束的位置
    span()	返回一個元組包含匹配 (開始,結束) 的位置
    """
    # ex9_1
    # num = re.match('[a-z]+', 's123')
    # print('num.group()', num.group())
    # print('num.start()', num.start())
    # print('num.end()', num.end())
    # print('num.span()', num.span())

    # ex9_2
    # p = re.compile('[a-z]+')
    # print(p.match('::: message'))
    # m = p.search('::: message')
    # print('m.group()', m.group())
    # print('m.span()', m.span())

    """     
    m = re.compile(pattern)
    result = m.match(string)
    # 等同與
    result = re.match(pattern, string)
    """

    # ex10
    # p = re.compile('\d+')
    # m = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
    # print(m)

    # ex11_1
    # m = re.match(r'From\s+', 'Fromage amk')
    # print(m)
    # ex11_2
    # m1 = re.match(r'From\s+', 'From age amk')
    # print(m1)

    """
    DOTALL,     S	使 . 匹配包括換行在內的所有字符
    IGNORECASE, I	使匹配對大小寫不敏感
    LOCALE,     L	做本地化識別（locale-aware）匹配
    MULTILINE,  M	多行匹配，影響 ^ 和 $
    VERBOSE,    X	能夠使用 REs 的 verbose 狀態，使之被組織得更清晰易懂
    """
    # ex12
    # 符合不分大小寫英文字母 輸出會空的 IGNORECASE
    # str1 = 'dasAWAa'
    # num = re.sub(r'[a-z]', "", str1, flags=re.I)
    # print('output:', num)

    # ex13
    # |  可選項，或者 "or" 操作符
    # m = re.findall(r'From|amk', 'Fromage amkdasd')
    # print(m)

    # ^ 匹配行首
    # ex14
    # m = re.findall(r'^From', 'Fromage amkdasd')
    # print(m)

    # 匹配行尾，行尾被定義為要麼是字符串尾
    # ex15
    # m = re.findall('13$', '{blo3ck}13')
    # print(m)
    # p.s 匹配一個 "$"，使用 "$ 或將其包含在字符類中，如[$],請參考範例 ex5

    #  \b 單詞邊界。這是個零寬界定符（zero-width assertions）只用以匹配單詞的詞首和詞尾。
    # 下面的例子只匹配 "class" 整個單詞；而當它被包含在其他單詞中時不匹配。
    # ex16_1
    # m = re.findall(r'class\b', 'no class at all')
    # print('output:', m)
    # ex16_2
    # m1 = re.findall(r'class\b', 'no classat all')
    # print('output:', m1)

    #  \B 另一個零寬界定符（zero-width assertions），它正好同 \b 相反，
    # 只在當前位置不在單詞邊界時匹配。
    # ex17_1
    # m = re.findall(r'class\B', 'no class at all')
    # print('output:', m)
    # ex17_2
    # m1 = re.findall(r'class\B', 'no classat all')
    # print('output:', m1)

    """
    split()	將字符串在 RE 匹配的地方分片並生成一個列表，
    sub()	找到 RE 匹配的所有子串，並將其用一個不同的字符串替換
    subn()	與 sub() 相同，但返回新的字符串和替換次數
    """
    # \W  匹配任何非字母數字字符；它相當於類 [^a-zA-Z0-9_]。
    # ex18_1
    # m = re.split(r'[T]', 'This is a test, short and sweet, of split().')
    # print(m)
    # ex18_2
    # m = re.split(r'\W+', 'This is a test, short and sweet, of split().')
    # print(m)

    # sub(replacement, string[, count = 0])
    # ex19_1
    # num = re.sub(r'[abc$]', "", 'd1as$')
    # print(num)
    # ex19_2
    # m = re.sub(r'blue|white|red', '', 'blue socks and red shoe')
    # print(m)

    """
    match() vs search()
    match() 函數只檢查 RE 是否在字符串開始處匹配，而 search() 則是掃瞄整個字符串。
    記住，match() 只報告一次成功的匹配，它將從 0 處開始；
    如果匹配不是從 0 開始的，match() 將不會報告它。
    """
    # ex20_1
    # print(re.match('super', 'superstition').span())
    # print(re.match('super', 'insuperable'))
    # # ex20_2
    # print(re.search('super', 'superstition').span())
    # print(re.search('super', 'insuperable'))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\reduce_use_for_loop_tutorial_1.py


def number_add(num):
    return num + 1


if __name__ == "__main__":
    """
    common write method
    """
    item_list = [0, 1, 2, 3]
    result = []
    for item in item_list:
        new_item = number_add(item)
        result.append(new_item)
    print("result", result)

    """
    better write method 1
    """
    result = [number_add(item) for item in item_list]
    print("result", result)

    """
    better write method 2
    """
    # result2 = map(int, str_num.split(','))  # python2
    result = list(map(lambda x: number_add(x), item_list))
    print("result", result)

    # tuple
    result = tuple(map(lambda x: number_add(x), item_list))
    print("result tuple", result)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\reduce_use_for_loop_tutorial_2.py


def process_item(item_new):
    item_new += 1
    result_new = item_new * item_new
    return result_new


if __name__ == "__main__":
    """
    common write method
    """
    results = []
    item_list = [0, 1, 2, 3, 4]
    for item in item_list:
        item += 1
        result = item * item
        results.append(result)
    print("results", results)

    """
    better write method 1
    """
    results = [process_item(item) for item in item_list]
    print("results", results)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\remove_trailing_zeros_tutorial.py

# ref. https://docs.python.org/3.6/library/decimal.html

import decimal
import unittest


# ref. `to_integral` identical to the `to_integral_value`
# Round to the nearest integer

# ref.  `normalize(x)` Reduces x to its simplest form.


def remove_trailing_zeros(**kwargs):
    number = kwargs.get("number")
    number = decimal.Decimal(str(number))

    if number == number.to_integral_value():
        result = number.to_integral_value()
    else:
        result = number.normalize()
    return result


class TestCase(unittest.TestCase):
    def test_case_1(self):
        result = remove_trailing_zeros(number=0.00)
        self.assertEqual(result, decimal.Decimal("0"))

    def test_case_2(self):
        result = remove_trailing_zeros(number=3.02)
        self.assertEqual(result, decimal.Decimal("3.02"))

    def test_case_3(self):
        result = remove_trailing_zeros(number=1.10)
        self.assertEqual(result, decimal.Decimal("1.1"))

    def test_case_4(self):
        result = remove_trailing_zeros(number=1.00)
        self.assertEqual(result, decimal.Decimal("1"))


if __name__ == "__main__":
    unittest.main()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\repr_tutorial.py

# repr
# Return a string representing the object as the developer wants to see it.

# str
# Return a string representing the object as the user wants to see it.


class A:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return "{} {}".format(self._x, self._y)

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({})".format(class_name, self)


a = A(1, 2)
print("str(a)", str(a))
print("repr(a)", repr(a))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\rjust_ljust_tutorial.py

"""
https://docs.python.org/3/library/stdtypes.html#str.rjust
https://docs.python.org/3/library/stdtypes.html#str.ljust
"""

my_str = "hello"
print(my_str.rjust(10, "0"))

print(my_str.ljust(12, "7"))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\set_tutorial.py

if __name__ == "__main__":
    """
    ref. https://docs.python.org/3/tutorial/datastructures.html#sets
    A set is an unordered collection with no duplicate elements
    """
    # set_seqs = {'a', 'b'} # set
    # dict_seqs = {} # dict
    set_seqs = set()
    set_seqs.add("test1")
    set_seqs.add("test2")
    print("set_seqs:", set_seqs)
    set_seqs.add("test1")
    print("set_seqs:", set_seqs)

    """
    remove(elem)
        Remove element elem from the set. Raises KeyError if elem is not contained in the set.
    """
    set_seqs.remove("test1")
    print("set_seqs:", set_seqs)
    # set_seqs.remove('test1') ## Raises KeyError

    """
    discard(elem)
        Remove element elem from the set if it is present.
    """
    set_seqs.discard("test1")
    print("set_seqs:", set_seqs)

    set_1 = {"a", "b", "c", "d"}
    set_2 = {"d", "e", "f", "g"}
    print("All: {}".format(set_1.union(set_2)))
    print("Both: {}".format(set_1.intersection(set_2)))
    print("Either but not both: {}".format(set_1.symmetric_difference(set_2)))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\setdefault_tutorial.py

# The method setdefault() is similar to get(),
# but will set dict[key]=default if key is not already in dict.

# dict.setdefault(key, default=None)

# setdefault does it all with a single lookup.


def ex1():
    dict_data = {"Name": "twtrubiks", "Age": 18}
    print("Name: {}".format(dict_data.setdefault("Name", None)))
    print("Sex: {}".format(dict_data.setdefault("Sex", None)))
    print("dict_data: {}".format(dict_data))
    print("Likes: {}".format(dict_data.setdefault("Likes", [])))
    print("dict_data: {}".format(dict_data))


def ex2_letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies


# equal ex2_letter_frequency
def ex2_1_letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1
    return frequencies


if __name__ == "__main__":
    ex1()
    # print(ex2_letter_frequency('sentence'))
    # print(ex2_1_letter_frequency('sentence'))

print("------------------------------------------------------------")  # 60個


#  Create utility function as a static method
class Dates:
    def __init__(self, date):
        self._date = date

    def get_date(self):
        return self._date

    @staticmethod
    def to_dash_date(date):
        return date.replace("/", "-")


# How inheritance works with static method?
class DatesWithSlashes(Dates):
    def get_date(self):
        return Dates.to_dash_date(self._date)


def main():
    # tutorial 1
    date = Dates("15-12-2016")
    date_from_birthday = "15/12/2016"
    date_with_dash = Dates.to_dash_date(date_from_birthday)

    if date.get_date() == date_with_dash:
        print("Equal")
    else:
        print("Unequal")

    # tutorial 2
    date2 = Dates("15-12-2016")
    date_with_slash = DatesWithSlashes("15/12/2016")

    if date2.get_date() == date_with_slash.get_date():
        print("Equal")
    else:
        print("Unequal")


if __name__ == "__main__":
    main()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\str_find_tutorial.py

# ref. https://docs.python.org/3/library/stdtypes.html#str.find

# str.find(sub[, start[, end]])

if __name__ == "__main__":
    data = "hello 123 456 789"
    target = "456"
    print("data.find(target)", data.find(target))

    # Return -1 if it is not found.
    print("data.find(target, 11)", data.find(target, 11))

print("------------------------------------------------------------")  # 60個


from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits

if __name__ == "__main__":
    print("ascii_letters:", ascii_letters)
    print("ascii_lowercase:", ascii_lowercase)
    print("ascii_uppercase:", ascii_uppercase)
    print("digits:", digits)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\stringio_tutorial.py

# https://docs.python.org/3/library/io.html#io.StringIO

# 讀寫文件不一定是文件, 也可以是存在內存 ( 記憶體 ram )
# StringIO 就是在 Ram 中讀寫 str

from io import StringIO


def tutorial_1():
    f = StringIO()
    f.write("hello")
    f.write(" ")
    f.write("world!")
    print(f.getvalue())

    # Close object and discard memory buffer
    f.close()  # 釋放記憶體
    # print(f.getvalue()) # .getvalue() will now raise an exception.


def tutorial_2():
    # 讀取 StringIO
    f = StringIO("Hello!\nHi!\nGoodbye!")
    while True:
        s = f.readline()
        if s == "":
            break
        print(s.strip())


def main():
    tutorial_1()
    # tutorial_2()


if __name__ == "__main__":
    main()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\strtobool_tutorial.py

from distutils.util import strtobool

if __name__ == "__main__":
    # Convert String to Boolean
    """
    Convert a string representation of truth to true (1) or false (0).
    True values are 'y', 'yes', 't', 'true', 'on', and '1';
    false valuesare 'n', 'no', 'f', 'false', 'off', and '0'.
    Raises ValueError if 'val' is anything else.
    """
    # print(bool('true'))  # -->error
    # print(bool('True'))  # -->error
    # print(bool('false'))  # -->error
    # print(bool('False'))  # -->error
    # print(bool('0'))  # -->error

    print(strtobool("true"))
    print(strtobool("True"))
    print(strtobool("False"))
    print(strtobool("on"))
    print(strtobool("n"))
    print(strtobool("y"))
    print(strtobool("0"))
    print(strtobool("1"))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\translate_tutorial.py

# ref. https://docs.python.org/3/library/stdtypes.html

if __name__ == "__main__":
    """
    str.translate(table[, deletechars]);
    """
    # tutorial_1
    intab_1 = "abc"
    outtab_1 = "def"
    # make translation table
    trantab_1 = str.maketrans(intab_1, outtab_1)
    value_1 = "aabbcc"
    print("tutorial_1:", value_1.translate(trantab_1))

    # tutorial_2
    intab_2 = "abc"
    outtab_2 = "def"
    # make translation table and remove "2" this character
    trantab_2 = str.maketrans(intab_2, outtab_2, "2")
    value_2 = "2aabb123cc2"
    print("tutorial_2:", value_2.translate(trantab_2))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\try_finally_tutorial.py


def base_example_1():
    try:
        print("run_1")
    except Exception:
        print("Exception")
    finally:
        print("other code")


def example_1():
    try:
        print("run_1")
    except Exception:
        print("Exception")
        return "re Exception"
    finally:
        print("other code")


def example_1_except():
    try:
        1 / 0
    except Exception:
        print("Exception")
        return "re Exception"
    finally:
        print("other code")


def example_2_diff():
    try:
        print("run_1")
    except Exception:
        print("Exception")
        return "re Exception"

    print("other code")


def example_2_diff_except():
    try:
        1 / 0
    except Exception:
        print("Exception")
        return "re Exception"

    print("other code")


def example_file():
    # better with as statement
    myfile = open("test.txt", "w")

    try:
        # 1/0
        myfile.write("data")  # raises Exception
    except Exception:
        print("Exception")
    finally:
        print("close file")
        myfile.close()  # has run


if __name__ == "__main__":
    print(base_example_1())

    # print(example_1())
    # print(example_1_except()) # -> has print("other code") ## important

    # print(example_2_diff())
    # print(example_2_diff_except()) # -> no print("other code")

    # example_file()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\unicodedata_tutorial.py

# ref. https://docs.python.org/3.6/library/unicodedata.html
import unicodedata


def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")


if __name__ == "__main__":
    a = unicodedata.category("A")  # 'L'etter, 'u'ppercase
    print("a:", a)
    b = unicodedata.category("\r")  # carriage return Cc : control character
    print("b:", b)
    c = unicodedata.category("\t")  # tab  Cc : control character
    print("c:", c)
    d = unicodedata.category("\v")  # vertical tabulation.  Cc : control character
    print("d:", d)
    demo = "\tA\rB\v"
    print("demo:", demo)
    print("remove_control:", remove_control_characters(demo))

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\user_defined_exceptions_tutorial.py

# ref. https://docs.python.org/3/tutorial/errors.html

# a common practice is to create a base class for exceptions defined by that module,
# and subclass that to create specific exception classes for different error conditions


class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


if __name__ == "__main__":
    try:
        raise InputError(expression="expression", message="This is InputError")
    except InputError as e:
        print("e.expression:", e.expression)
        print("e.message:", e.message)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\using_a_mutable_default_value_as_an_argument.py

# Passing mutable lists or dictionaries as default arguments to a function can have unforeseen consequences.
# Usually when a programmer uses a list or dictionary as the default argument to a function,
# the programmer wants the program to create a new list or dictionary every time that the function is called.
# However, this is not what Python does. The first time that the function is called,
# Python creates a persistent object for the list or dictionary. Every subsequent time the function is called,
# Python uses that same persistent object that was created from the first call to the function.


# ref.
# https://docs.quantifiedcode.com/python-anti-patterns/correctness/mutable_default_value_as_argument.html


# error Anti-pattern
# Be careful with mutable default arguments
def append_anti_pattern(number, number_list=[]):  # if use pycharm , will warn you
    number_list.append(number)
    print(number_list)
    return number_list


def append(number, number_list=None):
    if not number_list:
        number_list = []
    number_list.append(number)
    print(number_list)
    return number_list


if __name__ == "__main__":
    print("error Anti-pattern:")
    append_anti_pattern(5)  # expecting: [5], actual: [5]
    append_anti_pattern(7)  # expecting: [7], actual: [5, 7]
    append_anti_pattern(2)  # expecting: [2], actual: [5, 7, 2]
    print("right:")
    append(5)  # expecting: [5]
    append(7)  # expecting: [7]
    append(2)  # expecting: [2]

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\weakref_tutorial.py

# ref.
# https://docs.python.org/3/library/weakref.html#finalizer-objects
# https://docs.python.org/3/library/weakref.html#module-weakref

# A primary use for weak references is to implement caches or mappings holding large objects,
# where it’s desired that a large object not be kept alive solely
# because it appears in a cache or mapping.

# for garbage collector(GC)

import weakref


class Object:
    pass


def example_1():
    twtrubiks = Object()
    weakref.finalize(twtrubiks, print, "You killed twtrubiks!")
    del twtrubiks


def callback(x, y, z):
    print("hello")
    return x + y + z


def example_2():
    obj = Object()
    f = weakref.finalize(obj, callback, 1, 2, 3)
    print("f()", f())


def example_3():
    # With WeakValueDictionary garbage collection can reclaim the object
    # when there are no other references to it.

    class Foo(object):
        pass

    A = Foo()
    B = weakref.ref(A)
    # B = A
    # <weakref at 0x108b43958; to 'Foo' at 0x108b2f468>
    del A
    print(B)
    # <weakref at 0x108b43958; dead>


if __name__ == "__main__":
    example_1()
    # example_2()
    # example_3()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\with_as_tutorial.py


class Demo_1:
    def __enter__(self):
        print("__enter__")
        return "hello enter"

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__")
        if exc_type is ZeroDivisionError:
            print("Please DO NOT divide by zero!")
            return None


class Demo_2:
    def __enter__(self):
        print("__enter__")
        return "hello enter"

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__")
        if exc_type is ZeroDivisionError:
            print("Please DO NOT divide by zero!")
            return True


def example_1():
    with Demo_1() as data:
        print("data:", data)
        1 / 0
        print("example_1")


def example_better():
    with Demo_2() as data:
        print("data:", data)
        1 / 0
        print("example_1")


if __name__ == "__main__":
    # example_1()
    example_better()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\yield_from_tutorial.py

# Using yield from allows us to avoid having to deal with unexpected exceptions,
# let us focus on the implementation of business code.


def demo(n):
    i = 0
    while i < n:
        yield i
        i += 1


def test_yield_from(n):
    print("test_yield_from start")
    yield from demo(n)
    # 相當於下面
    # for item in demo(n):
    #     yield item
    print("test_yield_from end")


def example_1():
    for i in test_yield_from(3):
        print(i)


def return_yield():
    yield from (i for i in range(5))


def example_2():
    result = return_yield()
    print(next(result))
    print(next(result))


def chain_old(*iterables):
    for it in iterables:
        for i in it:
            yield i


def chain(*iterables):
    for it in iterables:
        yield from it


def example_3():
    s = "ABC"
    t = tuple(range(3))
    show = list(chain(s, t))
    print(show)


if __name__ == "__main__":
    example_1()
    example_2()
    example_3()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\yield_tutorial.py


# yield occurs and the generator pauses.
def common_func(max_number):
    print("create counter")
    counter = 0
    while counter < max_number:
        print(counter)
        print("counter +1")
        counter += 1


def yield_func(max_number):
    print("create counter")
    counter = 0
    while counter < max_number:
        yield counter
        print("counter +1")
        counter += 1


def example_1():
    num = yield_func(5)
    print(next(num))
    # print(next(num))
    # print(next(num))
    for n in num:
        print("n:", n)


def yield_step():
    print("step 1")
    yield 1
    print("step 2")
    yield 2
    print("step 3")
    yield 3


def example_2():
    test = yield_step()
    print(next(test))
    print(next(test))


def return_list():
    return [i for i in range(5)]


def return_yield():
    yield from (i for i in range(5))


def example_3():
    # yield only traversing once
    common_var = return_list()
    yield_var = return_yield()
    print("c1 in common_var")
    for c1 in common_var:
        print("c1:", c1)

    print("y1 in yield_var")
    for y1 in yield_var:
        print("y1:", y1)

    print("c2 in common_var")
    for c2 in common_var:
        print("c2:", c2)

    print("y2 in yield_var")  # not show
    for y2 in yield_var:
        print("y2:", y2)


if __name__ == "__main__":
    example_1()
    # example_2()
    # example_3()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\zip_tutorial.py

# The zip() function take iterables (can be zero or more),
# makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples.

# zip(*iterables)

if __name__ == "__main__":
    # tutorial 1
    numbers = [1, 2, 3]
    letters = ["A", "B", "C"]
    numbers_3 = ["a", "b", "c"]

    for numbers_value, letters_value in zip(numbers, letters):
        print(numbers_value, letters_value)

    for numbers_value, letters_value, v3 in zip(numbers, letters, numbers_3):
        print(numbers_value, letters_value, v3)

    # tutorial 2
    numberList = [1, 2, 3]
    strList = ["one", "two", "three"]
    result = zip(numberList, strList)
    resultSet = set(result)
    print(resultSet)

    #  Unzipping the Value Using zip()
    numberList_org, strList_org = zip(*resultSet)
    print("numberList_org =", numberList_org)
    print("strList_org =", strList_org)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\zipfile_tutorial.py


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


import pickle


class A:
    def __reduce__(self):
        return os.system, ("ls",)


payload = pickle.dumps(A())
pickle.loads(payload)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\__str__tutorial.py


# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\convert_class_object_to_json.py

import json


class Stock:
    def __init__(self, num, date):
        self.num = num
        self.date = date
        self.push_date = ["5/3"]


# create object
stock = Stock("2222", "2/3")

# convert to JSON string
json_str = json.dumps(stock.__dict__)

print(json_str)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\convert_json_to_class_object.py

import json


class User:
    def __init__(self, name):
        self.name = name


class Stock:
    def __init__(self, num, date, user):
        self.num = num
        self.date = date
        self.user = user


# create object
user = User("twtrubiks")
stock = Stock("2222", "2/3", user)

# convert to JSON string
json_str = json.dumps(stock, default=lambda o: o.__dict__)
print(json_str)

json_data = json.loads(json_str)
stock_obj = Stock(**json_data)
print(stock_obj)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\copy_tutorial.py


import json

if __name__ == "__main__":
    load_data = """
    {
    "maps": [
        {
            "id": "blabla",
            "iscategorical": "0"
        },
        {
            "id": "blabla",
            "iscategorical": "0"
        }
    ],
    "masks": {
        "id": "twtrubiks"
    },
    "om_points": "value",
    "parameters": {
        "id": "valore"
    }
}
    """
    data = json.loads(load_data)
    print("data[maps]: {}".format(data["maps"]))
    print("data[masks][id]: {}".format(data["masks"]["id"]))

    data_dump = json.dumps(data)
    print("json.dumps:", data_dump)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\kwargs.py

# You would use *args when you're not sure how many arguments might be passed to
# your function, i.e. it allows you pass an arbitrary number of arguments to your function


# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\logging_tutorial.py

import logging

"""
ref. https://docs.python.org/3/library/logging.html
Level , DEBUG < INFO < WARNING < ERROR < CRITICAL
"""


def ex1():
    # logging.basicConfig(level=logging.DEBUG)
    # will print 'warning message' , 'error message', because the default level is WARNING
    logging.warning("warning message")
    logging.error("error message")
    logging.debug("I told you so - debug")
    logging.info("I told you so - info")


def ex2():
    logging.error("test")
    log1 = logging.getLogger("ma_app")
    log2 = logging.getLogger()
    log1.warning("I told you")
    log2.warning("warning message")


def ex3():
    # will print all message , because the level is DEBUG
    format_log = "%(asctime)s %(levelname)s:%(message)s"
    logging.basicConfig(filename="example.log", format=format_log, level=logging.DEBUG)
    # logging.basicConfig(format=format_log, level=logging.DEBUG)
    logging.debug("This message should go to the log file")
    logging.info("So should this")
    logging.warning("And this, too")


def ex4():
    # multiple-handlers-and-formatter
    logger = logging.getLogger("my_app")
    logger.setLevel(logging.DEBUG)

    log_file = "my_test_logger.log"
    f_log = logging.FileHandler(log_file, mode="w")
    f_log.setLevel(logging.ERROR)

    c_log = logging.StreamHandler()
    c_log.setLevel(logging.DEBUG)

    format_log = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    f_log.setFormatter(format_log)
    c_log.setFormatter(format_log)

    logger.addHandler(f_log)
    logger.addHandler(c_log)

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")


if __name__ == "__main__":
    # ex1()
    # ex2()
    # ex3()
    ex4()

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\loop_if_else_break.py

import pickle

if __name__ == "__main__":
    data = {
        "a": [1, 2.0, 3, 4 + 6j],
        "b": ("character string", b"byte string"),
        "c": {None, True, False},
    }

    with open("data.pickle", "wb") as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

    with open("data.pickle", "rb") as f:
        # The protocol version used is detected automatically, so we do not
        # have to specify it.
        data_new = pickle.load(f)
    print("data_new:", data_new)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_twtrubiks\python-notes-master\property_decorator.py


from random import choice, sample

if __name__ == "__main__":
    num_seqs = range(20)
    print("num_seqs", list(num_seqs))
    print("choice(num_seqs)", choice(num_seqs))
    print("choice(num_seqs)", choice(num_seqs))

    print(sample(num_seqs, 3))
    print(sample(num_seqs, 3))
    print(sample(num_seqs, 5))
    print(sample(num_seqs, 5))

print("------------------------------------------------------------")  # 60個
