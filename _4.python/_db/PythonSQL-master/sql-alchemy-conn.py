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

sql = demo_table.select()

print("sql => ", str(sql), '\n')

result = conn.execute(sql)

print("result type => ", type(result), '\n')

for row in result:
    print(type(row))
    demo_id, demo_name, demo_data = row
    print("id => ", demo_id)
    print("name => ", demo_name)

print("\n---\n")

print("sql: select * from demo_table where id = 1 => \n")
sql = demo_table.select().where(demo_table.c.id == 1)
result = conn.execute(sql)
for row in result:
    demo_id, demo_name, demo_data = row
    print("id => ", demo_id)
    print("name => ", demo_name)

print("\n---\n")

print("sql_text: select * from demo_table where id = 1 => \n")



sql_text = text(
    "select * from demo_table where id = :app_id")

result = conn.execute(sql_text, app_id='1').fetchall()
print(result)
