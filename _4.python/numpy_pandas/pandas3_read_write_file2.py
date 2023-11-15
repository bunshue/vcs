import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': ["2","4","4","6"] } 
df = pd.DataFrame(data, index=["A","B","C","D"]) 

df.to_csv("vehicles.csv",index=False,encoding="big5")

df.to_json("vehicles1.json")
df.to_json("vehicles2.json", force_ascii = False)

"""
#匯出DataFrame
df.to_csv(filename)
df.to_json(filename)
df.to_html(filename)
df.to_excel(filename)
df.to_sql(table, con = engine)

#匯入DataFrame
df.read_csv(filename)
df.read_json(filename)
df.read_html(filename)
df.read_excel(filename)
df.read_sql(query, engine)
"""
import pandas as pd

df1 = pd.read_csv("vehicles.csv", encoding="big5")
df2 = pd.read_json("vehicles.json")
print(df1)
print(df2)

