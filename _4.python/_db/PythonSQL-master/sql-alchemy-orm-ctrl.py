from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from datetime import datetime

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

    def __init__(self, name, version, author, date, remark):
        self.name = name
        self.version = version
        self.author = author
        self.date = date
        self.remark = remark

    def __str__(self):
        return """
        app_id => {},
        app_name => {},
        app_version => {},
        app_author => {},
        app_date => {},
        app_remark => {}
        """.format(self.id, self.name, self.version, self.author, self.date, self.remark)


Session = sessionmaker(bind=engine)
session = Session()

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
    result = session.query(AppInfo).all()
    for row in result:
        print(row)

    ctrl = input(appDesc)
    if ctrl == "0":
        isRun = False
    elif ctrl == "1":
        appInfo = AppInfo('App', '1.0.1', 'DevAuth',
                          datetime(2021, 11, 8, 12, 30, 10), 'App-v1.0.1')
        session.add(appInfo)
        session.commit()
    elif ctrl == "2":
        row_id = input("id = ? ")
        appInfo = session.query(AppInfo).filter_by(id=row_id).first()
        appInfo.name = "AppNew"
        appInfo.version = "1.0.2"
        appInfo.remark = "App-v1.0.2"
        session.commit()
    elif ctrl == "3":
        row_id = input("id = ? ")
        appInfo = session.query(AppInfo).filter_by(id=row_id).first()
        session.delete(appInfo)
        session.commit()
