import sys
import os
from stat import ST_MTIME
import importlib.util

# PEP 3147 compatibility (PYC Repository Directories)
cache_from_source = (importlib.util.cache_from_source if sys.implementation.cache_tag
                     else lambda path: path + 'c')

def main():
    foldername = 'C:/_git/vcs/_1.data/______test_files3'
    for dirname in foldername:
        try:
            names = os.listdir(dirname)
        except OSError:
            print('Cannot list directory', repr(dirname))
            continue
        print('Checking ', repr(dirname), '...')
        verbose = 1
        for name in sorted(names):
            if name.endswith('.py'):
                name = os.path.join(dirname, name)
                try:
                    st = os.stat(name)
                except OSError:
                    print('Cannot stat', repr(name))
                    continue
                if verbose:
                    print('Check', repr(name), '...')
                name_c = cache_from_source(name)
                try:
                    with open(name_c, 'rb') as f:
                        magic_str = f.read(4)
                        mtime_str = f.read(4)
                except IOError:
                    print('Cannot open', repr(name_c))
                    continue
                if magic_str != MAGIC:
                    print('Bad MAGIC word in ".pyc" file', end=' ')
                    print(repr(name_c))
                    continue
                mtime = get_long(mtime_str)
                if mtime in {0, -1}:
                    print('Bad ".pyc" file', repr(name_c))
                elif mtime != st[ST_MTIME]:
                    print('Out-of-date ".pyc" file', end=' ')
                    print(repr(name_c))


def get_long(s):
    if len(s) != 4:
        return -1
    return s[0] + (s[1] << 8) + (s[2] << 16) + (s[3] << 24)


if __name__ == '__main__':
    main()
