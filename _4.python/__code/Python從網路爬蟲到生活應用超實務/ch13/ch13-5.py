import datetime
import pandas as pd
import time
from monthlyReport import get_monthly_report

data = []
now = datetime.datetime.now()
year = now.year
month = now.month - 1
if month == 0: 
    month = 12
    year -= 1

for i in range(12):
    print("爬取月營收的月份: ", year,"/", month)
    try:
        key = "%d-%d-01"%(year, month)
        m_df = get_monthly_report(0, year, month)
        m_df.index = m_df["公司代號"]
        item_df = pd.DataFrame({key: m_df["當月營收"]}).transpose()
        data.append(item_df) 
    except Exception:
        print("錯誤: 月營收資料爬取錯誤...")
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    time.sleep(10)

df = pd.concat(data)
df.index = pd.to_datetime(df.index)
df = df.sort_index()
print(df.head())
df.to_csv("monthlysales.csv")