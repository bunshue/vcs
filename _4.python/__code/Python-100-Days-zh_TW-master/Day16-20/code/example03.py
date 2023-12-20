from contextlib import contextmanager
from time import perf_counter

import time

def do_something():
    time.sleep(1.2345)

@contextmanager
def timer():
    try:
        start = perf_counter()
        yield
    finally:
        end = perf_counter()
        print(f'{end - start}秒')

for _ in range(10):
    with timer():
        print('執行工作')
        do_something()


