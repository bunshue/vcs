import pandas as pd

df = pd.DataFrame({'A': ['foo', 'bar', 'baz'],
                   'B': [1, 2, 3]})

df.to_excel('檔案路徑.xlsx', index=False)





