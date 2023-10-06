# 5-3-12 用 __slots__ 讓物件瘦身並加速

from dataclasses import dataclass

@dataclass
class Car:
    
    color: str
    mileage: float
    automatic: bool


@dataclass
class CarWithSlots:
    
    __slots__ = ['color', 'mileage', 'automatic']
    
    color: str
    mileage: float
    automatic: bool


car1 = Car('紅', 1234.0, True)
car2 = CarWithSlots('紅', 1234.0, True)


# pysize from https://github.com/bosswissam/pysize/blob/master/pysize.py

import sys
import inspect

def get_size(obj, seen=None):
    """Recursively finds size of objects in bytes"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if hasattr(obj, '__dict__'):
        for cls in obj.__class__.__mro__:
            if '__dict__' in cls.__dict__:
                d = cls.__dict__['__dict__']
                if inspect.isgetsetdescriptor(d) or inspect.ismemberdescriptor(d):
                    size += get_size(obj.__dict__, seen)
                break
    if isinstance(obj, dict):
        size += sum((get_size(v, seen) for v in obj.values()))
        size += sum((get_size(k, seen) for k in obj.keys()))
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum((get_size(i, seen) for i in obj))
        
    if hasattr(obj, '__slots__'): # can have __slots__ with __dict__
        size += sum(get_size(getattr(obj, s), seen) for s in obj.__slots__ if hasattr(obj, s))
        
    return size


print(get_size(car1), 'bytes')
print(get_size(car2), 'bytes')