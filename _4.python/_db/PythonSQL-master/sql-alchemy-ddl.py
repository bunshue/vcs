from sqlalchemy import *

engine = create_engine('sqlite:///DevDb.db', echo=True)

db = MetaData()

demo_table = Table(
    'demo_table', db,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('data', String),
)

db.create_all(engine)
