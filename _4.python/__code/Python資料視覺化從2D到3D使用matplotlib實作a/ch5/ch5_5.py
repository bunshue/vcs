import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"] 
s1 = "歡迎來到美國"
plt.text(0.7, 0.7, s1, size=30, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec='g',
                   fc='lightgreen',
                   )
         )
s2 = "美利堅合眾國"
plt.text(0.5, 0.35, s2, size=20, ha="right", va="top",
         bbox=dict(boxstyle="circle",
                   ec='y',
                   fc='lightyellow',
                   )
         )

plt.show()
