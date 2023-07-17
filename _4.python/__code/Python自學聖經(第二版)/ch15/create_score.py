import pandas as pd
import numpy as np

tem = []
for i in range(3): tem.append(i+1)
df = pd.DataFrame(np.random.randint(40,101,size=(3,3)), columns=['英文','社會','公民'])
#df = pd.DataFrame(np.random.randint(40,101,size=(3,4)), columns=['國文','數學','自然','社會'])
df.insert(0, '座號', tem)
df.to_csv('score2_6.csv', index=False)