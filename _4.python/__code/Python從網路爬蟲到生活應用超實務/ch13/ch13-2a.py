import pandas as pd
import twder

df = pd.DataFrame(twder.now_all()).transpose()
df.columns = ["時間","現金(買)","現金(賣)",
              "即期(買)","即期(賣)"]
print(df.head())