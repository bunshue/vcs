import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import math

x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,
     5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
sinus = [math.sin(v) for v in x]
cosinus = [math.cos(v) for v in x]

df = pd.DataFrame()
df["x"] = x
df["sin"]= sinus
df["cos"] = cosinus
print(df.head())
df.head().to_html("ch10-3-1a-01.html")
df2 = pd.melt(df, id_vars=['x'], value_vars=['sin', 'cos'])
print(df2.head())
df2.head().to_html("ch10-3-1a-02.html")

sns.set()
sns.relplot(x="x", y="value", kind="scatter", col="variable", data=df2)
plt.show()
