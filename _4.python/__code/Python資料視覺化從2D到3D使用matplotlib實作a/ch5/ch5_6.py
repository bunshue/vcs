import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"] 
s = '歡迎來到美國'
s1 = 'Welcome to the United States'
plt.text(0.1, 0.2, s, size=20,
         ha="left", va="center",
         bbox=dict(boxstyle="square",
                   ec='g',
                   fc='lightgreen',
                   )
         )
plt.text(0.1, 0.4, s, size=20,
         ha="left", va="center",
         bbox=dict(boxstyle="sawtooth",
                   ec='y',
                   fc='lightgreen',
                   )
         )
plt.text(0.1, 0.6, s, size=20,
         ha="left", va="center",
         bbox=dict(boxstyle="Roundtooth",
                   ec='y',
                   fc='lightgreen',
                   )
         )
plt.text(0.6, 0.2, s, size=20,
         ha="left", va="center",
         bbox=dict(boxstyle="DArrow",
                   ec='y',
                   fc='lightgreen',
                   )
         )
plt.text(0.6, 0.4, s, size=20,
         ha="left", va="center",
         bbox=dict(boxstyle="LArrow",
                   ec='y',
                   fc='lightgreen',
                   )
         )
plt.text(0.6, 0.6, s, size=20,
         ha="left", va="center",
         bbox=dict(boxstyle="RArrow",
                   ec='y',
                   fc='lightgreen',
                   )
         )
plt.text(0.1, 0.8, s1, size=18,
         ha="left", va="center",
         bbox=dict(boxstyle="Square",
                   ec='y',
                   fc='lightgreen',
                   )
         )
plt.show()

