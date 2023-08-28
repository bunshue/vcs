# ch7_10.py
import matplotlib.pyplot as plt

plt.subplots(figsize=(4,4))
plt.annotate("wedge",
             xy=(0.2, 0.2),
             xytext=(0.7, 0.8),
             size=20, va="center", ha="center",
             color='b',
             bbox=dict(boxstyle="round4",fc="lightyellow"),
             arrowprops=dict(arrowstyle="wedge",
                             color='g',
                             connectionstyle="arc3,rad=-0.3"),
             )
plt.annotate("wedge",
             xy=(0.2, 0.2),
             xytext=(0.7, 0.8),
             size=20, va="center", ha="center",
             color='b',
             bbox=dict(boxstyle="round4",fc="lightyellow"),
             arrowprops=dict(arrowstyle="wedge",
                             color='m',
                             connectionstyle="arc3,rad=0.3"),
             )
plt.show()



