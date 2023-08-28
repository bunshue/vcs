# ch23_10.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
fig = plt.figure()
x = np.arange(10)
y = 3 * np.cos(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)

plt.errorbar(x,y + 3,yerr=yerr,label='誤差條使用預設')
plt.errorbar(x,y + 2,yerr=yerr,uplims=True,label='uplims=True')
plt.errorbar(x,y + 1,yerr=yerr,uplims=True,lolims=True,
             label='uplims, lolims = True')
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x,y,yerr=yerr,uplims=upperlimits,lolims=lowerlimits,
             label='同時有uplims和lolims = True')
plt.legend(loc='lower left')
plt.xticks(np.arange(0,10))
plt.title('誤差條的綜和應用',fontsize=16,color='b')
plt.show()


      
