import pandas as pd
import twder

usd = twder.past_six_month("USD") 
df = pd.DataFrame(usd)
df.columns = ["時間","現金(買)","現金(賣)",
              "即期(買)","即期(賣)"]
df.set_index("時間" , inplace=True)
print(df.head())

