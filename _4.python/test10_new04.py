import time
import os
import sys
import itertools
import threading
import subprocess
from optparse import OptionParser, SUPPRESS_HELP

def bark(duration):

    _time = time.time
    _sleep = time.sleep
    
    # We give the parent some time to be ready.
    _sleep(1.0)

    start_time = _time()
    end_time = start_time + duration * 2.0
    i = 0
    while _time() < end_time:
        print('b', end = ' ')
        i += 1


bark(0.2)


print('------------------------------')  #30個



import sys
import time
import platform
CALIBRATION_LOOPS = 10
calibration_loops = range(CALIBRATION_LOOPS)

print(type(calibration_loops))
print(calibration_loops)


MILLI_SECONDS = 1e3
MICRO_SECONDS = 1e6
PERCENT = 100
LINE = 79
MIN_TEST_RUNTIME = 1e-3


name = 'david'
min_time = 11.11
avg_time = 22.22
op_avg = 33.33
min_overhead = 44.44
total_min_time = 55.55
total_avg_time = 66.66
other_min_time = 77.77
warp = 88.88
min_diff = 99.99
other_avg_time = 12.34
avg_diff =  23.45
overhead_times = 34.56
overhead_times = 45.67
eff_time = 56.78
abs_time = 67.89
min_overhead = 78.90

print('%30s:  %5.0fms  %5.0fms  %6.2fus  %7.3fms' % \
      (name,
       min_time * MILLI_SECONDS,
       avg_time * MILLI_SECONDS,
       op_avg * MICRO_SECONDS,
       min_overhead *MILLI_SECONDS))
print('-' * LINE)
print('Totals:                        '
      ' %6.0fms %6.0fms' %
      (total_min_time * MILLI_SECONDS,
       total_avg_time * MILLI_SECONDS,
       ))
print()

print('%30s: %5.0fms %5.0fms %7s %5.0fms %5.0fms %7s' % \
      (name,
       min_time * MILLI_SECONDS,
       other_min_time * MILLI_SECONDS * warp / warp,
       min_diff,
       avg_time * MILLI_SECONDS,
       other_avg_time * MILLI_SECONDS * warp / warp,
       avg_diff))

'''
print('%30s:  %6.3fms  %6.3fms' % \
      (name,
       min(overhead_times) * MILLI_SECONDS,
       max(overhead_times) * MILLI_SECONDS))
'''

print('    %5.0fms    %5.0fms %7.3fms' % \
      (eff_time * MILLI_SECONDS,
       abs_time * MILLI_SECONDS,
       min_overhead * MILLI_SECONDS))

i = 123
print(' Round %-25i  effective   absolute  overhead' % (i+1))

print('%30s:' % name, end=' ')


print('Calib. prep time     = %.6fms' % (
    total_min_time * MILLI_SECONDS))


# Name of the benchmark
name = '%04i-%02i-%02i %02i:%02i:%02i' % \
       (time.localtime(time.time())[:6])

print(name)


print('------------------------------')  #30個


print('------------------------------')  #30個



# Ring bell
sys.stderr.write('\007')


__version__ = '2.1'

print('-' * LINE)
print('PYBENCH %s' % __version__)
print('-' * LINE)


print('------------------------------')  #30個





print('------------------------------')  #30個



