# ch5_4.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]                                
plt.axis([0, 10, 0, 10])
s1 = ("明志科技大學是台灣頂尖大學")
plt.text(5, 8, s1, ha='center', fontsize=16, va='top', wrap=True)
s2 = ("Ming-Chi Institute of Technology is a good school in Taiwan."
    "I love this school."
    "The school is located in New Taipei City.")
plt.text(5, 1, s2, c='b', ha='left', rotation=15, wrap=True)
plt.text(6, 4, s2, c='g', ha='left', rotation=15, wrap=True)
plt.text(5, 4, s2, c='m', ha='right', rotation=-15, wrap=True)
plt.text(-1, 1, s2, c='y', ha='left', rotation=-15, wrap=True)
plt.show()













