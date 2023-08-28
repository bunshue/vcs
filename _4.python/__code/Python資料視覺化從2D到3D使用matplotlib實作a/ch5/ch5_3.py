# ch5_3.py
import matplotlib.pyplot as plt                           

plt.axis([0, 10, 0, 10])
s = ("Ming-Chi Institute of Technology is a good school in Taiwan."
    "I love this school."
    "The school is located in New Taipei City.")

plt.text(5, 10, s, family='Old English Text MT', style='oblique',
         ha='center',fontsize=15, va='top', wrap=True)
plt.text(5, 1, s, c='b', ha='left', rotation=15, wrap=True)
plt.text(6, 4, s, c='g', ha='left', rotation=15, wrap=True)
plt.text(5, 4, s, c='m', ha='right', rotation=-15, wrap=True)
plt.text(-1, 1, s, c='y', ha='left', rotation=-15, wrap=True)
plt.show()











