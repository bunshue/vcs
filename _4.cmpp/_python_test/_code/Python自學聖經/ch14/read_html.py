import pandas as pd

print("讀取網頁表單");
    
url = 'https://www.tiobe.com/tiobe-index/'
tables = pd.read_html(url, header=0, keep_default_na=False)

print("結果");
print(tables[0])
