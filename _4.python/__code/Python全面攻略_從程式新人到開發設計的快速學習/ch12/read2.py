import os
fName = 'C:/pcYah/score.txt'
if os.path.isfile(fName):
    f = open(fName, 'r')
    str1 = f.readline()
    print(str1)
    str2 = f.readline(4)
    print(str2)
    print(f.read())
    f.close()
else:
    print(None)
