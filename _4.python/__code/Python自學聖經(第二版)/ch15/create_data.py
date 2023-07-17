import pandas as pd
import numpy as np

def c_item(x):
  if x<2: return '筆電'
  elif x<7: return '冰箱'
  else: return '電視'

def s_item(x):
  if x<5: return '張三安'
  elif x<7: return '李四友'
  else: return '王五信'

df = pd.DataFrame({'業務員':np.random.randint(0,10,size = 100),
          '商品':np.random.randint(0,10,size = 100),
          '數量':np.random.randint(30,300,size = 100),
          '價格':np.random.randint(100,200,size = 100)})
df['商品'] = df['商品'].map(c_item)
df['業務員'] = df['業務員'].map(s_item)
df['價格'] = df['價格'].map(lambda x: x*100)

df.to_csv('sale.csv', index=False)