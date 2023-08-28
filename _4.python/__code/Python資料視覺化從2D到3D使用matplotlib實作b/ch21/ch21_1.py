# ch21_1.py
import matplotlib.pyplot as plt

fig, ax = plt.subplots() 
ax.broken_barh([(50, 30), (100, 20)], 
               (10, 5))   
ax.set_xlabel('x-value') 
ax.set_ylabel('y-value') 
ax.grid(True)  
ax.set_title('Broken_barh()',fontsize=16,color='b') 
plt.show()


      
