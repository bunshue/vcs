import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(6,4), columns=list("ABCD"))
print(df)
df.to_html("ch8-5-3-01.html")
print("---------------------------")
df2 = df.apply(np.cumsum)
print(df2)
df2.to_html("ch8-5-3-02.html")
print("---------------------------")
df3 = df.apply(lambda x: x.max() - x.min())
print(df3)
