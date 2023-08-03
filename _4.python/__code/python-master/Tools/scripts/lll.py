import sys, os

def lll(dirname):
    for name in os.listdir(dirname):
        if name not in (os.curdir, os.pardir):
            full = os.path.join(dirname, name)
            if os.path.islink(full):
                print(name, '->', os.readlink(full))


foldername
lll(arg)

