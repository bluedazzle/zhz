# coding: utf-8
import fdb
# con = fdb.connect(host='47.104.103.166', port=3050, database='C:/Office/Db/OFFICE.GDB',  user='sysdba', password='masterkey', sql_dialect=1)
# cur = con.cursor()
# cur.execute('SELECT * FROM FUEL_TANKS ORDER BY TANK_ID DESC ROWS 2 TO 10')
# print cur.fetchall()
# con = fdb.connect(host='47.104.103.166', port=3060, database='C:/Program Files/Firebird/Firebird_2_5/examples/empbuild/EMPLOYEE.FDB',  user='sysdba', password='masterkey', sql_dialect=1)

# a = '\xc1\xed\xd2\xbb\xb8\xf6\xb3\xcc\xd0\xf2\xd5\xfd\xd4\xda\xca\xb9\xd3\xc3\xb4\xcb\xce\xc4\xbc\xfe\xa3\xac\xbd\xf8\xb3\xcc\xce\xde\xb7\xa8\xb7\xc3\xce\xca\xa1\xa3'
# print a.decode('gbk')

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, DateTime, create_engine

Base = declarative_base()


class Tag(Base):
    __tablename__ = 'FUEL_TANKS'

    TANK_ID = Column(Integer, primary_key=True)
    TANK_NAME = Column(String)


class FuelPrice(Base):
    __tablename__ = 'FUELPRICES'

    sernum = Column(Integer, primary_key=True)
    item_id = Column(Integer)
    pricelevel1 = Column(Integer)
    pricelevel2 = Column(Integer)


class FuelDayTemperature(Base):
    __tablename__ = 'FUEL_DAY_TEMPERATURE'

    PK_FUEL_DAY_TEMPERATURE = Column(Integer, primary_key=True)
    day_batch_id = Column(Integer, primary_key=True)
    tank_id = Column(Integer)
    read_time = Column(DateTime)



engine = create_engine('firebird+fdb://sysdba:masterkey@47.104.103.166:3050/c:/office/Db/OFFICE.GDB', encoding='gbk')
# engine = create_engine('firebird+fdb://sysdba:masterkey@47.104.103.166:3060/C:/Program Files/Firebird/Firebird_2_5/examples/empbuild/EMPLOYEE.FDB')

DBSession = sessionmaker(bind=engine)

session = DBSession()
res = session.query(Tag).filter(Tag.TANK_ID == '1').all()
# print res
# res = session.query(FuelDayTemperature).all()
# print len(res)
for itm in res:
    print itm.TANK_ID, itm.TANK_NAME.decode('gbk')
    # print itm.day_batch_id, itm.read_time
