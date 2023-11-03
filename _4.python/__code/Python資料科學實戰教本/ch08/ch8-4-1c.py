import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(5, 1500, size=(2,3)))
print(df)
df.to_html("ch8-4-1c-01.html")
print("---------------------------")
# 取得與更新整個DataFrame
print(df[df > 800])
df[df > 800].to_html("ch8-4-1c-02.html")
print("---------------------------")
df[df > 800] = df - 100
print(df)
df.to_html("ch8-4-1c-03.html")