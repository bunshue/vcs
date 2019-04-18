x = 3              # an integer stored (in variable x)
f = 3.1415926      # a floating real point (in variable f)
name = "Python"    # a string
big = 358315791   # long, a very large number
z = complex(2,3)   # (2+3i)  a complex number. consists of real and imaginary part.
 
print(x)
print(f)
print(name)
print(big)
print(z)


s = "Hello Python"
print(s)      # prints whole string
print(s[0])   # prints "H"
print(s[1]) # prints "e"

print(s[0:2]) # prints "He"
print(s[2:4]) # prints "ll"
print(s[6:])  # prints "Python"

print(3/2)

s = "Hello Python"

print(s + ' ' + s) # print concatenated string.

#置換
print(s.replace('Hello','Thanks')) # print a string with a replaced word

#轉成大寫
# convert string to uppercase
s = s.upper()
print(s)

#轉成小寫 
# convert to lowercase
s = s.lower()
print(s)



#list

l = [ "Drake", "Derp", "Derek", "Dominique" ]
 
print(l)     # prints all elements
print(l[0])  # print first element
print(l[1])  # prints second element

#排序
l = [ "Drake", "Derp", "Derek", "Dominique" ]
 
print(l)     # prints all elements
l.sort()    # sorts the list in alphabetical order
print(l)     # prints all elements







