# print data

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
print("字串 : " + s +", 長度 : "+str(len(s)))   # 要先轉成字串
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


    
print("格式化列印")
print("姓名   座號  國文  數學  英文")
print("%3s  %2d   %3d   %3d  %3d" % ("林大明", 1, 100, 87, 79))
print("%3s  %2d   %3d   %3d  %3d" % ("陳阿中", 2, 74, 88, 100))
print("%3s  %2d   %3d   %3d  %3d" % ("張小英", 11, 82, 65, 8))

