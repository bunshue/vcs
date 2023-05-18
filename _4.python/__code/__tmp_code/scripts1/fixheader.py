import sys

def process(filename):
    try:
        f = open(filename, 'r')
    except IOError as msg:
        sys.stderr.write('%s: can\'t open: %s\n' % (filename, str(msg)))
        return
    data = f.read()
    f.close()
    if data[:2] != '/*':
        sys.stderr.write('%s does not begin with C comment\n' % filename)
        return
    try:
        f = open(filename, 'w')
    except IOError as msg:
        sys.stderr.write('%s: can\'t write: %s\n' % (filename, str(msg)))
        return
    sys.stderr.write('Processing %s ...\n' % filename)
    magic = 'Py_'
    for c in filename:
        if ord(c)<=0x80 and c.isalnum():
            magic = magic + c.upper()
        else: magic = magic + '_'
    sys.stdout = f
    print('#ifndef', magic)
    print('#define', magic)
    print('#ifdef __cplusplus')
    print('extern "C" {')
    print('#endif')
    print()
    f.write(data)
    print()
    print('#ifdef __cplusplus')
    print('}')
    print('#endif')
    print('#endif /*', '!'+magic, '*/')



foldername = 'C:/_git/vcs/_4.cmpp/_python_test/_code/使用Python搜刮網路資料的12堂實習課'
for filename in foldername:
    process(filename)



