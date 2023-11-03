import pandas as pd
from numpy.random import randint

df = pd.DataFrame(columns=("qty1", "qty2", "qty3"))
for i in range(5):
    df.loc[i] = [randint(-1,1) for n in range(3)]
print(df)
df.to_html("ch8-4-3a-01.html")
print("---------------------------")
df2 = pd.DataFrame(columns=("qty1", "qty2", "qty3"))
for i in range(5):
    s = pd.Series({"qty1":randint(-1,1),"qty2":randint(-1,1),"qty3":randint(-1,1)})
    df2 = df2.append(s, ignore_index=True)
print(df2)
df.to_html("ch8-4-3a-02.html")