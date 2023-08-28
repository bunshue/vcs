# ch5_7.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"] 
my_kwargs = dict(ha='center', va='center', fontsize=50, c='b')
plt.text(0.5, 0.5, '明志科技大學', **my_kwargs)
plt.show()

