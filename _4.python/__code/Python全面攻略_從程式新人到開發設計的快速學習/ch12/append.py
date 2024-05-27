import os
pName = 'C:/pcYah'
if not os.path.exists(pName):
    os.mkdir(pName)
f = open('C:/pcYah/philo.txt', 'a')
f.write('珍惜每一天\n')
f.flush()
f.close()