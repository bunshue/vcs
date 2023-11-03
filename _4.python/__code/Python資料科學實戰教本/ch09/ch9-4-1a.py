import matplotlib.pyplot as plt
import pandas as pd

data = [100, 110, 150, 170, 190, 200, 220]
weekday = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
s = pd.Series(data, index=weekday)
s.plot()
plt.show()