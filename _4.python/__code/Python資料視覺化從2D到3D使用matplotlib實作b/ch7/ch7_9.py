# ch7_9.py
import matplotlib.pyplot as plt

plt.subplots(figsize=(4,4))
plt.annotate("fancy",
             xy=(0.2, 0.2),
             xytext=(0.7, 0.8),
             size=20, va="center", ha="center",
             color='b',
             bbox=dict(boxstyle="round4",fc="lightyellow"),
             arrowprops=dict(arrowstyle="fancy",
                             color='g',
                             connectionstyle="arc3,rad=-0.3"),
             )
plt.show()



