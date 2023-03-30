import pandas as pd
data = pd.read_json("out.json", typ='series')

print(data)