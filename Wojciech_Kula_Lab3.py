# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:33:36 2020

@author: wkula
"""

#%% Prepare the environment
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Pamiętać o dodaniu odwołania do bazy danych
#db_string = "postgres://postgres:postgres@localhost:5432/Example"
db_string = "postgres://postgres:postgres@localhost:5432/postgres"

engine = create_engine(db_string)

Base = declarative_base()

#%% Exercise

import pandas as pd
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

data = pd.read_csv('C:/Users/wkula/Uczelnia/Databases/houses_to_rent.csv')

class House(Base):
    __tablename__ = 'houses'
    id = Column(Integer, primary_key=True)
    city = Column(Integer)
    area = Column(Integer)
    rooms = Column(Integer)
    bathroom = Column(Integer)
    parking_spaces = Column(Integer)
    floor = Column(String(20))
    animal = Column(String(20))
    furniture = Column(String(20))
    hoa = Column(String(20))
    rent_amount = Column(String(20))
    property_tax = Column(String(20))
    fire_insurance = Column(String(20))
    total = Column(String(20))
    
    def __repr__(self):
        return "<Houses(id='{0}', city={1}, area={2}, rooms={3}, bathroom={4}, parking spaces={5}, floor={6}, animal={7}, furniture={8}, hoa={9}, rent amount={10}, property tax={11}, fire insurance={12}, total={13})>".format(self.id, self.city, self.area, self.rooms, self.bathroom, self.parking_spaces, self.floor, self.animal, self.furniture, self.hoa, self.rent_amount, self.property_tax, self.fire_insurance, self.total)
    
    
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for d in data.values:
    NextHouse = House(city = d[1], area = d[2], rooms = d[3], bathroom = d[4],
                      parking_spaces = d[5], floor = d[6], animal = d[7], furniture = d[8],
                      hoa = d[9], rent_amount = d[10], property_tax = d[11],
                      fire_insurance = d[12], total = d[13])
    session.add(NextHouse)

session.commit()

#%% Database check

from sqlalchemy import select, MetaData, Table

metadata = MetaData()
table_name = "houses"
table = Table(table_name, metadata, autoload=True, autoload_with=engine)

stmt = select([table])
print(stmt)
results = engine.execute(stmt).fetchall()
for data in results[:20]:
    print(data)

#%% Creating tables structure

from sqlalchemy import Column, Integer, String, Date

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String())
    born_date = Column(Date)
    
    def __repr__(self):
        return "<authors(id='{0}', name={1}, surname={2}, born_date={3})>".format(
                self.id, self.name, self.surname, self.born_date)

from sqlalchemy import ForeignKey

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    id_author = Column(Integer, ForeignKey('authors.id'))
    original_title = Column(String, nullable = False)
    publication_date = Column(Integer, nullable = False)
    original_language = Column(String(), nullable = False)
    
#Create full schema
Base.metadata.create_all(engine)

#Create only table
#Base.__table__.create(engine)

#%%Another method of a table schema declaration
#Skip durring normal use
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import Table, MetaData

USER = Table('users', MetaData(bind=engine), Column('id', Integer, primary_key = True), Column('name', String(20)))
USER.create(engine)

#%%Session and adding data to table

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

author1 = Author(name = 'William', surname = 'Shakespeare', born_date = '26.04.1564')
author2 = Author(name = 'Albert', surname = 'Camus', born_date = '7.11.1913')

session.add(author1)
session.add(author2)

session.commit()






    