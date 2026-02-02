# ch4_10.py
import pandas as pd
import numpy as np
name = ['Frank', 'Peter', 'John']
score = ['first', 'second', 'final']
df = pd.DataFrame(np.random.randint(60,100,size=(3,3)),
                  columns=name,
                  index=score)
print(df)






