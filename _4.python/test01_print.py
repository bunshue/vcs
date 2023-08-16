"""在檔頭用註解寫的字1
在檔頭用註解寫的字2
在檔頭用註解寫的字3
在檔頭用註解寫的字4
在檔頭用註解寫的字5
"""

'''

各種 print 技巧 與 字串處理

'''

print('-' * 70)	#70個
print('------------------------------------------------------------')	#60個

print('字符串格式化操作')
print('My name is %s and weight is %d kg!' % ('David', 82) )
#可用%c %s %d %u %x %X %f

print("打印各種數值")

x = 3              # an integer stored (in variable x)
f = 3.1415926      # a floating real point (in variable f)
name = "Python"    # a string
big = 358315791    # long, a very large number
z = complex(2,3)   # (2+3i)  a complex number. consists of real and imaginary part.
 
#print("整數 : " + x) fail
print(x)    #整數
print(f)    #浮點數
print(name) #字串
print(big)  #很大的數
print(z)    #複數

print("打印數字")
a, b = 2, 3
print(a, b)
a, b = b, a
print(a, b)

s = "Hello Python"
print("字串 : " + s + ", 長度 : " + str(len(s)))   # 要先轉成字串
print("第0字元 " + s[0])     # prints "H"
print("第1字元 " + s[1])     # prints "e"

print("第0~2字元 " + s[0:2])   # prints "He"
print("第2~4字元 " + s[2:4])   # prints "ll"
print("第6以後字元 " + s[6:])    # prints "Python"

print(7/3)

print('------------------------------------------------------------')	#60個

s = "Hello Python"
print(s + ' ' + s) # print concatenated string.

print("轉成大寫");
# convert string to uppercase
s1 = s.upper()
print(s1)

print("轉成小寫");
# convert to lowercase
s2 = s.lower()
print(s2)

print("找出字串位置");
p = s.find("Python")
print(p)

print("置換");
s4 = s.replace("Python", "Perl")
print(s4)


print("List測試");

list = [ "Louisiana", "Iowa", "Ohio", "Nevada" ]
 
print("list 長度 : "+ str(len(list)))

print("list全部內容");
print(list)     # prints all elements
print("list第0個內容");
print(list[0])  # print first element
print("list第1個內容");
print(list[1])  # prints second element

print("排序");
list = [ "Louisiana", "Iowa", "Ohio", "Nevada" ]

print("排序前, list全部內容"); 
print(list)     # prints all elements
list.sort()    # sorts the list in alphabetical order
print("排序後, list全部內容"); 
print(list)     # prints all elements

print('list測試')
#建立一個list
moneytotal=[]
i=0
while i < 17:
  moneytotal.append(0)
  i=i+1

print("moneytotal list 長度 : "+ str(len(moneytotal)))

print('------------------------------------------------------------')	#60個
    
print("格式化列印")
print("姓名   座號  國文  數學  英文")
print("%3s  %2d   %3d   %3d  %3d" % ("林大明", 1, 100, 87, 79))
print("%3s  %2d   %3d   %3d  %3d" % ("陳阿中", 2, 74, 88, 100))
print("%3s  %2d   %3d   %3d  %3d" % ("張小英", 11, 82, 65, 8))

print("格式化列印")
sentence = 'This is a lion-mouse'
print('直接列印, 靠左對齊')
print(sentence)
print('40格 靠右對齊')
print("%40s" % sentence)
print("%40s" % 'This is a lion-mouse')

print("不換行, 接著印")
money = 123.456
print("%10s" % money, end = "")
print("%10s" % money, end = "")
print("%10s" % money, end = "")
print("%10s" % money, end = "")
print("%10s" % money, end = "")


print("四捨五入")
money = 123.456789123456789
print('直接列印')
print("%20s" % money)
print("四捨五入到小數點以下第2位")
print("%20s" % round(money, 2))

pi = 3.14159265358979323846
print("圓周率 四捨五入到小數點以下第6位 : ", format(pi, ".6f"))
print("圓周率 四捨五入到整數 : ", round(pi))

byteyears = 1234
print(repr(int(byteyears)).rjust(8))


'''
print(format(i * j, '4d'), end = '')
print()# Jump to the new line
'''


var1 = 'Hello World!'
var2 = "Python Programming"

print('var1[0]: ', var1[0])
print('var2[1:5]: ', var2[1:5])

print('------------------------------------------------------------')	#60個

import sys

print('有顏色的打印訊息', file = sys.stderr)

print('%s: %s, line %d, column %d' % (
'aaaa', 'bbbb', 123, 456),
file = sys.stderr)

print((
'*** %(file)s:%(lineno)s: 發生錯誤在 "%(token)s"'
) % {
'token': '函數名',
'file': '檔案',
'lineno': '行號'
}, file = sys.stderr)


infile = 'aaaaaaa'
lno = 1234
print('Syntax error on %s:%d' % (infile, lno), 'before:', file = sys.stderr)

print("aaaaaa", file = sys.stdout)

print(__doc__, file = sys.stderr)

print("(%s:%s)" % (sys.exc_info()[0], sys.exc_info()[1]))

cmd = '%s "%s" %s' % (sys.executable, 'aaaa', 'bbbb')
print(cmd)

ver_string = "%d.%d" % (sys.version_info[0], sys.version_info[1])
root_key_name = "Software\\Python\\PythonCore\\" + ver_string
print(sys.version_info)
print(ver_string)
print(root_key_name)

string1 = 'abcde'
print('%s\t%-40s\t' % (string1, string1), end = ' ')

num = 123
print('%d %s - %s\t%s' % (num, string1, string1, string1))

print('Error: %s' % string1, file = sys.stderr)

debug = False #debug訊息之開關

print('------------------------------------------------------------')	#60個

def print_debug(msg):
    if debug: print(msg)

print_debug("%s: permission denied: %s" % (string1, string1))


err = sys.stderr.write
dbg = err
rep = sys.stdout.write

err('AAAAA')
dbg('BBBBB')
rep('CCCCC')

#err(str(msg) + '\n')

err('-i option or file-or-directory missing\n')

print('------------------------------------------------------------')	#60個


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

usage()

def usage(msg = None):
    if msg is None:
        msg = __doc__
    print(msg, file = sys.stderr)

msg = 'adfkajdfad;jlfkjl'
usage(msg)

#print("Serving {} on port {}, control-C to stop".format(path, port))


def usage3(msg):
    sys.stderr.write("%s: %s\n" % (sys.argv[0], msg))
    sys.stderr.write("Usage: %s [-l] file ...\n" % sys.argv[0])
    sys.stderr.write("Try `%s -h' for more information.\n" % sys.argv[0])

msg = 'aaaa'
usage3(msg)

print('恢復正常顯示')

import sys

filename = 'aaaaa'
msg = 'bbbbb'
sys.stderr.write('紅字打印 : %s: can\'t open: %s\n' % (filename, str(msg)))

data = 'cccccccccccc'
sys.stdout.write(data)

print()

print('恢復正常顯示')

print('------------------------------------------------------------')	#60個


import time

copyright = '1990-%s, Python Software Foundation' % time.strftime('%Y')

print(copyright)

print('------------------------------------------------------------')	#60個


model = 'aaaa'
year = '2023'
mileage = 1234
money = 123456

message = "{:<10}({}年式)，{:>10,}KM，售價：{:>10,}元"

print(message.format(model, year, mileage, money))


print('------------------------------------------------------------')	#60個


testno = 20
s ='abc'
fmt = 'def'
result = 'hij'
err = 'mnp'
sys.stdout.write("xfmt%d  format  %s  '%s'  ->  \"%s\"\n" % (testno, s, fmt, result))
sys.stdout.write("xfmt%d  format  %s  '%s'  ->  '%s'\n" % (testno, s, fmt, result))
sys.stderr.write("%s  %s  %s\n" % (err, s, fmt))



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


print('------------------------------------------------------------')	#60個


'''
ascii = [chr(c) for c in range(127)] # 7-bit ASCII
for char in ascii:
    print(char, end = '')
'''

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

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


print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'


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



print('------------------------------------------------------------')	#60個




import sys
def errprint(*args):
    sep = ""
    for arg in args:
        sys.stderr.write(sep + str(arg))
        sep = " "
    sys.stderr.write("\n")


msg = 'this is a lion-mouse'
errprint(msg)
print(msg)




print('------------------------------------------------------------')	#60個


def output(string = '', end = '\n'):
    sys.stdout.write(string + end)


def output(*strings):
    for s in strings:
        sys.stdout.write(str(s) + "\n")


pos = 'abcd'
output("Lexical error at position %s" % pos)




print('------------------------------------------------------------')	#60個




def fail(msg):
    out = sys.stderr.write
    out(msg + "\n\n")
    return 0

filename = 'ccccc'
fail("couldn't open " + filename)







print('------------------------------------------------------------')	#60個


arg = 'abcdefg'
sys.stderr.write("Can't find %s\n" % arg)




print('------------------------------------------------------------')	#60個

import sys

usage = """Usage: %s [-cd] paths...
    -c: recognize Python source files trying to compile them
    -d: debug output""" % sys.argv[0]

print('msgsssssss', file = sys.stderr)
print(usage, file = sys.stderr)




print('------------------------------------------------------------')	#60個

filename1 = 'C:/_git/vcs/_1.data/______test_files1/aaaaa.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/bbbbb.jpg'

print("Copied %s to %s" % (filename1, filename2))


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print(filename)

print('file: %s' % filename)
print('file: %r' % filename)





print('------------------------------------------------------------')	#60個


import sys

def test():
    '''Test program.
    Usage: ftp [-d] [-r[file]] host [-l[dir]] [-d[dir]] [-p] [file] ...

    -d dir
    -l list
    -p password
    '''

    if len(sys.argv) < 2:
        print(test.__doc__)
        #sys.exit(0)

test()





print('------------------------------------------------------------')	#60個


print("Best:", end = ' ', file = sys.stderr)



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個








print('------------------------------------------------------------')	#60個


def log(message):
    sys.stderr.write('log: %s\n' % str(message))

def log_info(message, type='info'):
    ignore_log_types = frozenset(['warning'])
    if type not in ignore_log_types:
        print('%s: %s' % (type, message))

log('uncaptured python exception, closing channel')

log_info('uncaptured python exception, closing channel %s (%s:%s %s)'
         % ('aaaa', 'bbbb', 'pppp', 'qqqq' ), 'error')

log_info('unhandled incoming priority event', 'warning')
log_info('unhandled read event', 'warning')

print('------------------------------------------------------------')	#60個




import os
sys.stdout = sys.stderr
print('Usage:', os.path.basename(sys.argv[0]), end = ' ')
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

print('不能 恢復正常顯示')


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



