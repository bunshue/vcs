"""在檔頭用註解寫的字1
在檔頭用註解寫的字2
在檔頭用註解寫的字3
在檔頭用註解寫的字4
在檔頭用註解寫的字5
"""

import sys

def usage(msg = ''):
    print(__doc__ % globals())
    if msg:
        print(msg)

usage()


print()
print(globals())
print()

print('__doc__ : 檔頭的註解')
print(__doc__)

string = 'this is a lion-mouse'

print('%s' % string, file=sys.stderr)


print(string)





import sys

def test():
    print('檔頭註解')
    print(__doc__)
    usage("at least one file argument is required")
    print()
    print()
    msg = 'aaaaa'
    sys.stderr.write("%s: extra file arguments ignored\n" % msg)
    sys.stderr.write("can't open: %s\n" % msg)
    
def usage(msg):
    sys.stderr.write("%s: %s\n" % (sys.argv[0], msg))
    sys.stderr.write("Usage: %s [-m] warnings\n" % sys.argv[0])
    sys.stderr.write("Try `%s -h' for more information.\n" % sys.argv[0])

def chop(line):
    if line.endswith("\n"):
        return line[:-1]
    else:
        return line

test()






import os
import sys

err = sys.stderr.write
dbg = err
rep = sys.stdout.write

def usage():
    progname = sys.argv[0]
    err('Usage: ' + progname +
              ' [-c] [-r] [-s file] ... file-or-directory ...\n')
    err('\n')
    err('-c           : substitute inside comments\n')
    err('-r           : reverse direction for following -s options\n')
    err('-s substfile : add a file of substitutions\n')
    err('\n')
    err('Each non-empty non-comment line in a substitution file must\n')
    err('contain exactly two words: an identifier and its replacement.\n')
    err('Comments start with a # character and end at end of line.\n')
    err('If an identifier is preceded with a *, it is not substituted\n')
    err('inside a comment even when -c is specified.\n')




usage()

filename = 'aaaaa'
msg = 'lion-mouse'
dbg('fix(%r)\n' % (filename,))
err(filename + ': cannot open: ' + str(msg) + '\n')
err('%s:%r: warning: overriding: %r %r\n' % (filename, 123, 'aaa', 'bbb'))
err('%s:%r: warning: previous: %r\n' % (filename, 456, 'ccc'))


dbg('recursedown(%r)\n' % (filename,))
'''
names = os.listdir(dirname)
err(dirname + ': cannot list directory: ' + str(msg) + '\n')
if name in (os.curdir, os.pardir): continue
'''



        

def _format_size(size, sign):
    for unit in ('B', 'KiB', 'MiB', 'GiB', 'TiB'):
        if abs(size) < 100 and unit != 'B':
            # 3 digits (xx.x UNIT)
            if sign:
                return "%+.1f %s" % (size, unit)
            else:
                return "%.1f %s" % (size, unit)
        if abs(size) < 10 * 1024 or unit == 'TiB':
            # 4 or 5 digits (xxxx UNIT)
            if sign:
                return "%+.0f %s" % (size, unit)
            else:
                return "%.0f %s" % (size, unit)
        size /= 1024


name = 'david'
size = 123456
count = 17

text = ("%s: size=%s, count=%i"
        % (name,
           _format_size(size, False),
           count))

average = size / count
text += ", average=%s" % _format_size(average, False)

print(text)


print('------------------------------')  #30個



ascii = [chr(c) for c in range(127)] # 7-bit ASCII
for char in ascii:
    print(char, end = '')


print('------------------------------')  #30個



print('------------------------------')  #30個

print('------------------------------')  #30個

def msg(str):
    sys.stderr.write(str + '\n')

longlist = '-l'
filename = 'test01_io.py'

sts = os.system('ls ' + longlist + ' ' + filename)
if sts:
    msg('"ls -l" exit status: ' + repr(sts))

sts = os.system('ls ' + filename)
if sts:
    msg('"ls -l" exit status: ' + repr(sts))

sts = os.system('dir')
if sts:
    msg('"ls -l" exit status: ' + repr(sts))
else:
    print(sts)


print('------------------------------')  #30個




print('------------------------------')  #30個




print('------------------------------')  #30個



print('------------------------------')  #30個








