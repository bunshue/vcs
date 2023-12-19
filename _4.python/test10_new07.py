import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python-100-Days-zh_TW-master\Day01-15\code\Day09\clock.py

from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

'''
if __name__ == '__main__':
    main()
'''

from abc import ABCMeta, abstractmethod
from math import pi


class Shape(object, metaclass=ABCMeta):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def perimeter(self):
        return 2 * pi * self._radius

    def area(self):
        return pi * self._radius ** 2

    def __str__(self):
        return '我是一个圆'


class Rect(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __str__(self):
        return '我是一个矩形'


if __name__ == '__main__':
    shapes = [Circle(5), Circle(3.2), Rect(3.2, 6.3)]
    for shape in shapes:
        print(shape)
        print('周长:', shape.perimeter())
        print('面积:', shape.area())

print("------------------------------------------------------------")  # 60個



