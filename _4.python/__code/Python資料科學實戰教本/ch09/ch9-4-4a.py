import matplotlib.pyplot as plt
import pandas as pd

usage = {"os": ["Windows","Mac OS","Linux","Chrome OS","BSD"],
         "percentage": [88.78, 8.21, 2.32, 0.34, 0.02]}

df = pd.DataFrame(usage, 
                  columns=["percentage"],
                  index=usage["os"])
print(df)
df.to_html("ch9-4-4.html")
df.plot(kind="bar")
plt.show()