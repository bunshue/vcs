import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個


x1 = np.linspace(-5, 5, 101)
y1 = np.sin(x1)

fig, ax = plt.subplots()
ax.set_title("Sin")
ax.set_xlabel("rad")
ax.plot(x1, y1)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)


plt.show()


print('------------------------------------------------------------')	#60個

