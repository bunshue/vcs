# print data

print('字符串格式化操作')
print('My name is %s and weight is %d kg!' % ('David', 82) )
#可用%c %s %d %u %x %X %f

print("打印各種數值")

x = 3              # an integer stored (in variable x)
f = 3.1415926      # a floating real point (in variable f)
name = "Python"    # a string
big = 358315791   # long, a very large number
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
print("%10s" % money, end="")
print("%10s" % money, end="")
print("%10s" % money, end="")
print("%10s" % money, end="")
print("%10s" % money, end="")


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


import sys

print('有顏色的打印訊息', file = sys.stderr)

print('%s: %s, line %d, column %d' % (
'aaaa', 'bbbb', 123, 456),
file=sys.stderr)

print((
'*** %(file)s:%(lineno)s: 發生錯誤在 "%(token)s"'
) % {
'token': '函數名',
'file': '檔案',
'lineno': '行號'
}, file=sys.stderr)


infile = 'aaaaaaa'
lno = 1234
print('Syntax error on %s:%d' % (infile, lno), 'before:', file=sys.stderr)


print("aaaaaa", file=sys.stdout)


print(__doc__, file=sys.stderr)

print("(%s:%s)" % (sys.exc_info()[0], sys.exc_info()[1]))



cmd = '%s "%s" %s' % (sys.executable, 'aaaa', 'bbbb')
print(cmd)





ver_string = "%d.%d" % (sys.version_info[0], sys.version_info[1])
root_key_name = "Software\\Python\\PythonCore\\" + ver_string
print(sys.version_info)
print(ver_string)
print(root_key_name)

