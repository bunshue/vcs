import sys

def getsuffix(filename):
    name, sep, suff = filename.rpartition('.')
    return sep + suff if sep else ''



def main():
    files = sys.argv[1:]
    suffixes = {}
    for filename in files:
        suff = getsuffix(filename)
        suffixes.setdefault(suff, []).append(filename)
    for suff, filenames in sorted(suffixes.items()):
        print(repr(suff), len(filenames))




