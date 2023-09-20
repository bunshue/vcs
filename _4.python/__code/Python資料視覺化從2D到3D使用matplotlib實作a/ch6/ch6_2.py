import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.figure(figsize=(7,2),facecolor='yellow')
my_kwargs = dict(ha='center',va='center',fontsize=50,c='b')
plt.text(0.5, 0.5, '歡迎來到美國', **my_kwargs)

plt.show()

