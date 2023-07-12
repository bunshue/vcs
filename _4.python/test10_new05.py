import sys

filename = 'aaaaa'
msg = 'bbbbb'
sys.stderr.write('紅字打印 : %s: can\'t open: %s\n' % (filename, str(msg)))

data = 'cccccccccccc'
sys.stdout.write(data)

print()


__version__ = 1, 7, 0


def fail(msg):
    out = sys.stderr.write
    out(msg + "\n\n")
    return 0

fail("couldn't open " + filename)


'''
        os.remove(fname)
        os.rename(temp_fname, fname)

'''

llll = ['aa', 'bb', 'cc', 'dd', 'ee']
pppp = llll[2:] #第二項(含)以後的
print(llll)
print(pppp)

table1 = [] #list
table2 = {} #dict
print(type(table1))
print(type(table2))

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
mod = os.path.basename(filename)
print(mod)
print(mod[-3:])

head, tail = os.path.split(filename)
print(head)
print(tail)
tempname = os.path.join(head, '@' + tail)
print(tempname)


curdir = [os.curdir]
print(curdir)

pardir = [os.pardir]
print(pardir)


err = sys.stderr.write
dbg = err
rep = sys.stdout.write

msg = 'cccccc'
usage = 'dddddddddddd'
err(str(msg) + '\n')
err(msg)
err('-i option or file-or-directory missing\n')
err(usage)
err('%s: cannot open: %r\n' % (filename, msg))
err('%s: cannot create: %r\n' % (tempname, msg))


'''
word = word.strip()


        if os.path.isdir(arg):
            if recursedown(arg): bad = 1
        elif os.path.islink(arg):
            err(arg + ': will not process symbolic links\n')
            bad = 1
        else:
            if fix(arg): bad = 1

    dbg('recursedown(%r)\n' % (dirname,))
##  dbg('fix(%r)\n' % (filename,))


'''

sys.stdout = sys.stderr
print('Usage:', os.path.basename(sys.argv[0]), end=' ')
print('[-cdu] [file] ...')
print('-c: print callers per objectfile')
print('-d: print callees per objectfile')
print('-u: print usage of undefined symbols')
print('If none of -cdu is specified, all are assumed.')
print('Use "nm -o" to generate the input (on IRIX: "nm -Bo"),')
print('e.g.: nm -o /lib/libc.a | objgraph')

sys.stdout = sys.stdout
import sysconfig
SRCDIR = sysconfig.get_config_var('srcdir')
print(SRCDIR)

prog = sys.argv[0]
print(prog)
