import os
import sys
import platform

print("== %s %s (%s) ==" % (
    platform.python_implementation(),
    platform.python_version(),
    platform.python_build()[0],
))

# Processor identification often has repeated spaces
cpu = ' '.join(platform.processor().split())
print("== %s %s on '%s' ==" % (
    platform.machine(),
    platform.system(),
    cpu,
))
print()


print('------------------------------')  #30個

print('* using %s %s' % (
    getattr(platform, 'python_implementation', lambda:'Python')(),
    ' '.join(sys.version.split())))



print('------------------------------')  #30個




print('------------------------------')  #30個







print('------------------------------')  #30個







print('------------------------------')  #30個








