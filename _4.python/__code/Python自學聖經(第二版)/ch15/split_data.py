import pandas as pd
import numpy as np

df1 = pd.read_csv('titanic.csv')
df2 = df1[['row.names','pclass','survived','name','age','embarked']]
df2.to_csv('titanic1.csv', index=False)
df3 = df1[['row.names','home.dest','room','ticket','boat','sex']]
df3.to_csv('titanic2.csv', index=False)
