import pandas as pd

print("使用pandas讀取網頁表單");
    
url = 'https://www.tiobe.com/tiobe-index/'
tables = pd.read_html(url, header=0, keep_default_na=False)

print("結果");
print(tables[0])



import pandas as pd

#原物料商品行情
tables = pd.read_html("http://www.stockq.org/market/commodity.php")

n = 1
for table in tables:
    print("第 " + str(n) + " 個表格：")
    print(table.head())
    print()
    n += 1


import pandas as pd

#原物料商品行情
tables = pd.read_html("http://www.stockq.org/market/commodity.php")

print(tables)

'''
table = tables[7]
table = table.drop(table.index[[0,1]])
table.columns = ["商品", "買價", "漲跌", "比例", "台北"]
table.index = range(len(table.index))

print(table)
'''


