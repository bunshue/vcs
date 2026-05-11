str1 = 'welcome to python' 
print("str1 = " + str1)
str2 = 'Welcome to Python'
print("str2 = " + str2)
str3 = 'This is a test.'
print("str3 = " + str3)
s = str1.capitalize()
print("str1.capitalize() = " + s)
s = str2.lower()
print("str2.lower() = " + s)
s = str1.upper()
print("str1.upper() = " + s)
s = str1.title()
print("str1.title() = " + s)
s = str2.swapcase()
print("str2.swapcase() = " + s)
s = str3.replace('is', 'was')
print("str3.replace('is', 'was') = " + s)
str4 = "Tom,Bob,Mary,Joe,John"
lst1 = str4.split(",")
print(lst1)
str5 = "23\n52\n44\n78"
lst2 = str5.split("\n")
print(lst2)
lst3 = str5.splitlines()
print(lst3)

