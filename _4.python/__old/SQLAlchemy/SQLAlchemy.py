"""

"""

import sys

"""

SQLAlchemy
SQLAlchemy是為Python程式語言提供的開源SQL工具包及對象關係對映器（ORM），是在MIT許可證下發行的軟體。




"""

print("------------------------------------------------------------")  # 60個
# 3.7 SQLAlchemy与常用数据库的连接
print("------------------------------------------------------------")  # 60個

# 本节代码需要连接数据库，如果你电脑上没有数据库，运行会报错

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

engine = create_engine('mysql://root:123@127.0.0.1:3306/test?charset=utf8') 

pd.read_sql('select * from data', engine)

pd.read_sql('data',engine)

df = pd.DataFrame([[5, '永辉超市', 11], [6, '华夏幸福', 34]], 
      columns=['ID', 'stockname', 'price'], 
      index=range(2))
print(df)

df.to_sql('data', engine, index=False, if_exists='append')

pd.read_sql('data',engine)

df.to_sql('t_data', engine, index=False, if_exists='append')

pd.read_sql('t_data',engine)

df1 = pd.DataFrame(np.arange(20000).reshape(10000, 2), index=range(10000), columns=['key', 'value'])
r = df1.to_dict('records')

df1.to_sql('f_data', engine, index=False, if_exists='append')
pd.read_sql('f_data', engine).tail()

#下面这两句话就完成了ORM映射，Base.classes.XXXX就是映射的类  
# Base.metadata.tables['XXX']就是相应的表  
Base = automap_base()  
Base.prepare(engine, reflect = True)  
f_data = Base.metadata.tables['f_data']

engine.execute(f_data.insert(), r)  
pd.read_sql('f_data', engine).tail()

 
----------------------------------------------------------------


#讀寫資料庫

from sqlalchemy import create_engine

engine = create_engine('sqlite:///data/aqi/aqi.db')

try:
    engine.execute("DROP TABLE aqi")
except:
    pass

str_cols = ["Position", "City", "Level"]

for df in read_aqi_files("data/aqi/*.csv"):
    for col in str_cols:
        df[col] = df[col].str.decode("utf8")
    df.to_sql("aqi", engine, if_exists="append", index=False)

df_aqi = pd.read_sql("aqi", engine)

df_polluted = pd.read_sql("select * from aqi where PM2_5 > 500", engine)
print(len(df_polluted))




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


