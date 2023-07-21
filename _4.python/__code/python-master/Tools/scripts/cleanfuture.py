import __future__
import tokenize
import os
import sys

dryrun  = 0
recurse = 0
verbose = 0

def errprint(*args):
    strings = map(str, args)
    msg = ' '.join(strings)
    if msg[-1:] != '\n':
        msg += '\n'
    sys.stderr.write(msg)

def main():
    import getopt
    global verbose, recurse, dryrun
    try:
        opts, args = getopt.getopt(sys.argv[1:], "drv")
    except getopt.error as msg:
        errprint(msg)
        return
    for o, a in opts:
        if o == '-d':
            dryrun += 1
        elif o == '-r':
            recurse += 1
        elif o == '-v':
            verbose += 1
    if not args:
        errprint("Usage:", __doc__)
        return
    for arg in args:
        check(arg)

def check(file):
    if os.path.isdir(file) and not os.path.islink(file):
        if verbose:
            print("listing directory", file)
        names = os.listdir(file)
        for name in names:
            fullname = os.path.join(file, name)
            if ((recurse and os.path.isdir(fullname) and
                 not os.path.islink(fullname))
                or name.lower().endswith(".py")):
                check(fullname)
        return

                errprint("Skipping file %r; can't parse line %d:\n%s" %
                         (self.fname, srow, line))

