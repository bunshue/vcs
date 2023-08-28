# ch10_13.py
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(nrows=2, ncols=2)
x =np.linspace(0, 2*np.pi, 200)
N = 20
for i in range(N):   
    axs[0,0].plot(x,i*np.sin(x),color=plt.cm.hsv(i/N))    
    axs[0,1].plot(x,i*np.sin(x),color=plt.cm.rainbow(i/N))    
    axs[1,0].plot(x,i*np.sin(x),color=plt.cm.cool(i/N))    
    axs[1,1].plot(x,i*np.sin(x),color=plt.cm.hot(i/N))    
axs[0,0].set_title('hsv')
axs[0,1].set_title('rainbow')
axs[1,0].set_title('cool')
axs[1,1].set_title('hot')
plt.tight_layout()
plt.show()


