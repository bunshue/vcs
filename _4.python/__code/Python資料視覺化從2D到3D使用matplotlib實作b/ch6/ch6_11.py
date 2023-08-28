# ch6_11.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure()    # 地理投影圖表 Aitoff
plt.subplot(projection="aitoff")
plt.title("地理投影 = Aitoff",c='b')
plt.grid(True)

plt.figure()    # 地理投影圖表 Hammer
plt.subplot(projection="hammer")
plt.title("地理投影 = Hammer",c='b')
plt.grid(True)

plt.figure()    # 地理投影圖表 Lambert
plt.subplot(projection="lambert")
plt.title("地理投影 = Lambert",c='b')
plt.grid(True)

plt.figure()    # 地理投影圖表 Mollweide
plt.subplot(projection="mollweide")
plt.title("地理投影 = Mollweide",c='b')
plt.grid(True)
plt.show()



