import sys
import time

# Timer types
TIMER_TIME_TIME = 'time.time'
TIMER_TIME_PROCESS_TIME = 'time.process_time'
TIMER_TIME_PERF_COUNTER = 'time.perf_counter'
TIMER_TIME_CLOCK = 'time.clock'
TIMER_SYSTIMES_PROCESSTIME = 'systimes.processtime'

# Choose platform default timer
if hasattr(time, 'perf_counter'):
    TIMER_PLATFORM_DEFAULT = TIMER_TIME_PERF_COUNTER
elif sys.platform[:3] == 'win':
    # On WinXP this has 2.5ms resolution
    TIMER_PLATFORM_DEFAULT = TIMER_TIME_CLOCK
else:
    # On Linux this has 1ms resolution
    TIMER_PLATFORM_DEFAULT = TIMER_TIME_TIME

import systimes
print(systimes.SYSTIMES_IMPLEMENTATION)

timer = TIMER_PLATFORM_DEFAULT

print('* using timer: %s' % timer)
if hasattr(time, 'get_clock_info'):
    info = time.get_clock_info(timer[5:])
    print('* timer: resolution=%s, implementation=%s'
          % (info.resolution, info.implementation))

