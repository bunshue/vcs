"""
SQLAlchemy
SQLAlchemy是為Python程式語言提供的開源SQL工具包及對象關係對映器（ORM）
"""

import sys
import sqlite3
import numpy as np
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

print("------------------------------------------------------------")  # 60個

db_filename = "../sqlite/data/animals.sqlite"

# engine = create_engine("sqlite:///%s" % db_filename, echo=False) # 預設為不顯示詳細訊息
engine = create_engine("sqlite:///%s" % db_filename)
df = pd.read_sql("table01", engine)
print(df)

# Read from SQL Query
df = pd.read_sql("SELECT * FROM table01", engine)
print(df)

# Read from Database Table
df = pd.read_sql_table("table01", engine)
print(df)

# Read from SQL Query using read_sql_query()
df = pd.read_sql_query("SELECT * FROM table01", engine)
print(df)

# Write DataFrame to SQL Table
# NG pd.to_sql('myDf', engine)

# sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("先建立sqlite資料庫")

conn = sqlite3.connect("datafile.db")
cursor = conn.cursor()

# 建立表單 weather
cursor.execute(
    """CREATE TABLE IF NOT EXISTS weather (id integer primary key, state text, state_code text,
              year_text text, year_code text, avg_max_temp real,  max_temp_count integer, 
              max_temp_low real, max_temp_high real,
              avg_min_temp real, min_temp_count integer,
              min_temp_low real, min_temp_high real,
              heat_index real, heat_index_count integer, 
              heat_index_low real, heat_index_high real,
              heat_index_coverage text)
              """
)
conn.commit()
conn.close()

print("使用sqlalchemy連線到 sqlite資料庫")

db_filename = "datafile.db"
engine = create_engine("sqlite:///%s" % db_filename)
""" NG
metadata = MetaData(engine)
weather  = Table('weather', metadata, 
                Column('id', Integer, primary_key=True),
                Column("state", String),
                Column("state_code", String),
                Column("year_text", String ),
                Column("year_code", String), 
                Column("avg_max_temp", Float),
                Column("max_temp_count", Integer),
                Column("max_temp_low", Float),
                Column("max_temp_high", Float),
                Column("avg_min_temp", Float), 
                Column("min_temp_count", Integer),
                Column("min_temp_low", Float), 
                Column("min_temp_high", Float),
                Column("heat_index", Float), 
                Column("heat_index_count", Integer),
                Column("heat_index_low", Float), 
                Column("heat_index_high", Float),
                Column("heat_index_coverage", String)
                )
Session = sessionmaker(bind=engine)
session = Session()
result = session.execute(select([weather]))
for row in result:
    print(row)
"""

print("------------------------------------------------------------")  # 60個

# SQLAlchemy

db_filename = "datafile.db"
engine = create_engine("sqlite:///%s" % db_filename)
""" NG
metadata = MetaData(engine)
people  = Table('people', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String),
                Column('count', Integer),
                )
Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)

people_ins = people.insert().values(name='Bob', count=1)
print(str(people_ins))
# 'INSERT INTO people (name, count) VALUES (?, ?)'
session.execute(people_ins)

# <sqlalchemy.engine.result.ResultProxy object at 0x7f126c6dd438>

session.commit()

session.execute(people_ins, [
    {'name': 'Jill', 'count':15},
    {'name': 'Joe', 'count':10}
    ])

#<sqlalchemy.engine.result.ResultProxy object at 0x7f126c6dd908>

session.commit()

result = session.execute(select([people]))
for row in result:
    print(row)
"""

"""
(1, 'Bob', 1)
(2, 'Jill', 15)
(3, 'Joe', 10)
"""

"""
result = session.execute(select([people]).where(people.c.name == 'Jill'))
for row in result:
    print(row)

# (2, 'Jill', 15)

result = session.execute(people.update().values(count=20).where(people.c.name == 'Jill'))
session.commit()
result = session.execute(select([people]).where(people.c.name == 'Jill'))
for row in result:
    print(row)

# (2, 'Jill', 20)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class People(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    count = Column(Integer)

results = session.query(People).filter_by(name='Jill')
for person in results:
    print(person.id, person.name, person.count)

# 2 Jill 20

new_person = People(name='Jane', count=5)
session.add(new_person)
session.commit()

results = session.query(People).all()
for person in results:
    print(person.id, person.name, person.count)
"""

"""
1 Bob 1
2 Jill 20
3 Joe 10
4 Jane 5
"""
"""
jill = session.query(People).filter_by(name='Jill').first()
print(jill.name)
# 'Jill'

jill.count = 22
session.add(jill)
session.commit()
results = session.query(People).all()
for person in results:
    print(person.id, person.name, person.count)

"""

"""
1 Bob 1
2 Jill 22
3 Joe 10
4 Jane 5
"""

"""
jane = session.query(People).filter_by(name='Jane').first()
session.delete(jane)
session.commit()
jane = session.query(People).filter_by(name='Jane').first()
print(jane)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 3.7 SQLAlchemy与常用数据库的连接
print("------------------------------------------------------------")  # 60個

# 本节代码需要连接数据库，如果你电脑上没有数据库，运行会报错

# engine = create_engine("mysql://root:123@127.0.0.1:3306/test?charset=utf8")

db_filename = "datafile.db"
engine = create_engine("sqlite:///%s" % db_filename)
engine = create_engine("sqlite:///data/aqi/aqi.db")

db_filename = "../sqlite/data/animals.sqlite"
engine = create_engine("sqlite:///%s" % db_filename)

pd.read_sql("select * from table01", engine)

pd.read_sql("table01", engine)

df = pd.DataFrame(
    [[5, "永辉超市", 11], [6, "华夏幸福", 34]],
    columns=["ID", "stockname", "price"],
    index=range(2),
)
print(df)

print("aaaaaaaaaaa1")
df.to_sql("animals", engine, index=False, if_exists="append")

print("aaaaaaaaaaa2")
pd.read_sql("animals", engine)

print("aaaaaaaaaaa3")
df.to_sql("t_data", engine, index=False, if_exists="append")

print("aaaaaaaaaaa4")
pd.read_sql("t_data", engine)

print("aaaaaaaaaaa5")
df1 = pd.DataFrame(
    np.arange(20000).reshape(10000, 2), index=range(10000), columns=["key", "value"]
)

print("aaaaaaaaaaa6")
r = df1.to_dict("records")

print("aaaaaaaaaaa7")
df1.to_sql("f_data", engine, index=False, if_exists="append")

print("aaaaaaaaaaa8")
pd.read_sql("f_data", engine).tail()

print("aaaaaaaaaaa9")

# 下面这两句话就完成了ORM映射，Base.classes.XXXX就是映射的类
# Base.metadata.tables['XXX']就是相应的表
Base = automap_base()
Base.prepare(engine, reflect=True)
f_data = Base.metadata.tables["f_data"]

print("aaaaaaaaaaa10")

# NG engine.execute(f_data.insert(), r)

cc = pd.read_sql("f_data", engine).tail()
print(cc)

print("kkkkkkkkkkkkkkk")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀寫資料庫

engine = create_engine("sqlite:///data/aqi/aqi.db")

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
