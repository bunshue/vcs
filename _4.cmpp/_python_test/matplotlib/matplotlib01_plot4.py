from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\Fonts\SimSun.ttc", size=20)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))

plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.plot(x, z, "b--", label="$cos(x^2)$")

plt.xlabel("Time(s)", fontproperties=font)
plt.ylabel("Amplitude", fontproperties=font)
plt.title(u"中文測試中...", fontproperties=font)

plt.ylim(-1.2, 1.2)
plt.legend()
plt.grid()

plt.show()
