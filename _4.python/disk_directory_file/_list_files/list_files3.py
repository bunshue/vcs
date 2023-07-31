import os
import sys

def process(filename, listnames):
    print('process : ', filename)
    if os.path.isdir(filename):
        return processdir(filename, listnames)
    try:
        print(filename)
    except IOError as msg:
        sys.stderr.write("Can't open: %s\n" % msg)
        return 1

def processdir(dir, listnames):
    print('processdir : ', dir)
    try:
        names = os.listdir(dir)
    except OSError as msg:
        sys.stderr.write("Can't list directory: %s\n" % dir)
        return 1
    files = []
    for name in names:
        print(name)
        fn = os.path.join(dir, name)
        print(fn)
        if os.path.normcase(fn).endswith(".py") or os.path.isdir(fn):
            files.append(fn)
    files.sort(key=os.path.normcase)
    exit = None
    for fn in files:
        x = process(fn, listnames)
        exit = exit or x
    return exit

foldername = 'C:/_git/vcs/_1.data/______test_files5'
listnames = 1  # or 1
x = process(foldername, listnames)
print(x)



