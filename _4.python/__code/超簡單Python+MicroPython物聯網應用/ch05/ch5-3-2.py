import os.path as path

fname = path.realpath("ch5-3-2.py")
print(fname)
r = path.split(fname)
print("os.path.split() =", r)
r = path.splitext(fname)
print("os.path.splitext() =", r)
p = path.dirname(fname)
print("p = os.path.dirname() =", p)
f = path.basename(fname)
print("f = os.path.basename() =", f)
r = path.join(p, f)
print("os.path.join(p,f) =", r)
