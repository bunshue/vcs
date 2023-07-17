import pandas as pd
url = 'https://www.tiobe.com/tiobe-index/'
tables = pd.read_html(url, header=0, keep_default_na=False)
print(tables[0])