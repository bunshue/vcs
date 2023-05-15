import time
import datetime


def my_time(func):
    def wrapper():
        start_time = time.time()
        func()
        times = time.time() - start_time
        print('execution time: {}'.format(datetime.timedelta(seconds=times)))

    return wrapper
