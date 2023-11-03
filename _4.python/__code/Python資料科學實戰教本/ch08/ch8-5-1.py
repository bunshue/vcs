import pandas as pd
import numpy as np

df = pd.DataFrame({"名稱" : ["客戶A", "客戶B", "客戶A", "客戶B",
                             "客戶A", "客戶B", "客戶A", "客戶A"],
                   "編號" : ["訂單1", "訂單1", "訂單2", "訂單3",
                             "訂單2", "訂單2", "訂單1", "訂單3"],
                   "數量" : np.random.randint(1,5,size=8),
                   "售價" : np.random.randint(150,500,size=8)})

print(df)
df.to_html("ch8-5-1-01.html")
print("---------------------------")
print(df.groupby("名稱").sum())
df.groupby("名稱").sum().to_html("ch8-5-1-02.html")
print("---------------------------")
print(df.groupby(["名稱","編號"]).sum())
df.groupby(["名稱","編號"]).sum().to_html("ch8-5-1-03.html")