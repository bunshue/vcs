import os
pName = 'C:/pcYah'
if not os.path.exists(pName):
    os.mkdir(pName)
f = open('C:/pcYah/philo.txt', 'w')
f.write('時光不倒帶\n')
f.write('歲月不重來\n')
f.flush()
f.close()
