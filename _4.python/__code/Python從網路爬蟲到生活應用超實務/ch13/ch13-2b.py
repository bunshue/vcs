import pandas as pd
import twder

print(twder.now("USD")) 
print(twder.now("JPY"))

df = pd.DataFrame(twder.past_day("USD"))
df.columns = ["時間","現金(買)","現金(賣)",
              "即期(買)","即期(賣)"]
df.set_index("時間" , inplace=True)
print(df.head())