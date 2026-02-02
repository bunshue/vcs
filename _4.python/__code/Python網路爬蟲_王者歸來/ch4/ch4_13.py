# ch4_13.py
import pandas as pd

course = ['Chinese', 'English', 'Math', 'Natural', 'Society']
x = pd.read_csv("out4_12a.csv",index_col=0)
y = pd.read_csv("out4_12b.csv",names=course)
print(x)
print(y)







