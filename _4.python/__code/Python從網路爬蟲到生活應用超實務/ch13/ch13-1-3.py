import pandas as pd

def split_name(name):
    pos = name.find(')')
    return pd.Series({
        '"幣別"': name[0:pos].strip() + ")"
    }) 
df = pd.read_csv("xrt.csv",encoding="big5")
df = df.drop(df.index[[0,1]])
df = df.iloc[:,0:5]
df.columns = ["幣別","現金(買)",
               "現金(賣)","即期(買)",
               "即期(賣)"]
df["幣別"] = df["幣別"].apply(split_name)
df.to_csv("xrt2.csv",index=False,encoding="big5")
print(df.head())     

