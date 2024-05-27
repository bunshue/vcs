import os
pName = 'c:/pcYah'
if not os.path.exists(pName):
    os.mkdir(pName)
f = open('c:/pcYah/data1.txt', 'w')
f.close()

