from sqlalchemy import *

engine = create_engine('sqlite:///DevDb.db', echo=False)

conn = engine.connect()
db = MetaData()

demo_table = Table(
    'demo_table', db,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('data', String),
)


appDesc = """
Please input action code :

1 - Insert Data
2 - Update Data
3 - Delect Date
--- --- ---
0 - exit

"""
isRun = True

while(isRun):
    sql = demo_table.select()
    result = conn.execute(sql)

    for row in result:
        print(row)

    ctrl = input(appDesc)
    if ctrl == "0":
        isRun = False
    elif ctrl == "1":
        sql = demo_table.insert().values(name='App', data="text")
        conn.execute(sql)
    elif ctrl == "2":
        row_id = input("row_id = ? ")
        sql = demo_table.update().values(
            name='AppNew', data="new text").where(demo_table.c.id == row_id)
        conn.execute(sql)
    elif ctrl == "3":
        row_id = input("row_id = ?")
        sql = demo_table.delete().where(demo_table.c.id == row_id)
        conn.execute(sql)
