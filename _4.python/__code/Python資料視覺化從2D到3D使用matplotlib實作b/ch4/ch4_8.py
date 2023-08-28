# ch4_8.py
import matplotlib.pyplot as plt

plt.fill('time','signal','g',
        data={'time':[0,1,2,3],'signal':[0,1,1,0]})
plt.xlabel('Time')
plt.ylabel('Signal')
plt.show()




