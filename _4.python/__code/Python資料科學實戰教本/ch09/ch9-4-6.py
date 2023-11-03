import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
df = pd.DataFrame({"x":x, "y":y})
df.plot(kind="scatter", x="x", y="y", 
        title="Sin(x)")
plt.show()

