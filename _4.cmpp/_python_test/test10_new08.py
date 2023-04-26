
import sys

err = sys.stderr.write

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


import sys, os, time, difflib, argparse
from datetime import datetime, timezone

path = 'C:/_git/vcs/_4.cmpp/_python_test'
t1 = datetime.fromtimestamp(os.stat(path).st_mtime, timezone.utc)

print(t1)

t2 = t1.astimezone().isoformat()

print(t2)


filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/human2.jpg'

print(filename)


print('file: %s' % filename)
print('file: %r' % filename)

'''
print('一種寫入檔案的方法')
filename = 'tmp.txt'

fp = open(filename,'w')
print('[OPTIONS]', file=fp)
print('Auto Index=Yes', file=fp)
print('Binary TOC=No', file=fp)
print('Binary Index=Yes', file=fp)
print('Compatibility=1.1', file=fp)
print('Error log file=ErrorLog.log', file=fp)
print('Display compile progress=Yes', file=fp)
print('Full-text search=Yes', file=fp)
print('Default window=main', file=fp)
print('', file=fp)  #寫一個空白列
print('[WINDOWS]', file=fp)
print('main=,"' + '","'
+ '","","",,,,,0x23520,222,0x1046,[10,10,780,560],'
'0xB0000,,,,,,0', file=fp)
print('', file=fp)
print('[FILES]', file=fp)
print('', file=fp)
fp.close()
'''

#usage()


def usage(msg=None):
    if msg is None:
        msg = __doc__
    print(msg, file=sys.stderr)


msg = 'adfkajdfad;jlfkjl'
usage(msg)


