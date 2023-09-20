import matplotlib.pyplot as plt                           

plt.axis([0, 10, 0, 10])
s = ("Welcome to the United States"
    "God bless you"
    "Thanks Got It's Friday")

plt.text(5, 10, s, family='Old English Text MT', style='oblique',
         ha='center',fontsize=15, va='top', wrap=True)
plt.text(5, 1, s, c='b', ha='left', rotation=15, wrap=True)
plt.text(6, 4, s, c='g', ha='left', rotation=15, wrap=True)
plt.text(5, 4, s, c='m', ha='right', rotation=-15, wrap=True)
plt.text(-1, 1, s, c='y', ha='left', rotation=-15, wrap=True)
plt.show()


import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]                                
plt.axis([0, 10, 0, 10])
s1 = ('歡迎來到美國')
plt.text(5, 8, s1, ha='center', fontsize=16, va='top', wrap=True)
s2 = ("Welcome to the United States"
    "God bless you"
    "Thanks Got It's Friday")

plt.text(5, 1, s2, c='b', ha='left', rotation=15, wrap=True)
plt.text(6, 4, s2, c='g', ha='left', rotation=15, wrap=True)
plt.text(5, 4, s2, c='m', ha='right', rotation=-15, wrap=True)
plt.text(-1, 1, s2, c='y', ha='left', rotation=-15, wrap=True)

plt.show()

