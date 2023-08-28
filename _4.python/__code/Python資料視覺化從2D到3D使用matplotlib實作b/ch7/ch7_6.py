# ch7_6.py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(4,4))
ax.annotate("Annotate",
            xy = (0.2, 0.2),
            xytext = (0.7, 0.8),
            arrowprops = dict(arrowstyle="->",
                              connectionstyle="angle"),
            )
plt.show()



