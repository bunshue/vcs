from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

engine = create_engine('sqlite:///DevDb.db', echo=False)
Base = declarative_base()


class AppInfo(Base):
    __tablename__ = 'app_info'
    id = Column('id', Integer, primary_key=True)
    name = Column(String)
    version = Column(String)
    author = Column(String)
    date = Column(Integer)
    remark = Column(String)


Session = sessionmaker(bind=engine)
session = Session()
result = session.query(AppInfo).all()

for row in result:
    print(type(row))
    print("id => ", row.id)
    print("name => ", row.name)
