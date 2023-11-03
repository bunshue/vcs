import pandas as pd

# 匯入CSV格式的檔案
df = pd.read_csv("dists2.csv", encoding="utf8")
print(df)
df.to_html("ch8-2-2a-01.html")
print("---------------------------")
# 匯入JSON格式的檔案
df2 = pd.read_json("dists.json")
print(df2)
df.to_html("ch8-2-2a-02.html")