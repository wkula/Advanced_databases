# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:08:57 2020

@author: wkula
"""
from sqlalchemy import create_engine, MetaData, Table
db_string = "postgresql://wbauer_adb:adb2020@pgsql-196447.vipserv.org:5432/wbauer_adb"
db = create_engine(db_string)

print(db.table_names())
metadata = MetaData()
table_name = "category"
table = Table(table_name, metadata, autoload=True, autoload_with=db)
print(repr(table))
print(table.columns.keys())

from sqlalchemy import select, func
stmt = select([table])
print(stmt)
results = db.execute(stmt).fetchmany(size=20)
print(results)
print()

stmt = stmt.where(table.c.category_id == 11)
results = db.execute(stmt).fetchmany()
print(results)

#%%1. Script to connection with database
from sqlalchemy import create_engine, MetaData, Table, select, or_
db_string = "postgresql://wbauer_adb:adb2020@pgsql-196447.vipserv.org:5432/wbauer_adb"
db = create_engine(db_string)

#%%2. Based on information_schema, present how to explore the relationships between the tables:

# i. staff and country
"""
staff is related with address via address_id
address is related with citi via citi_id
city is related with country via countr id
"""
# ii. actor, language, and film
"""
actor is related with film via film_actor which stores relationships betwen them (actor_id, film_id)
language is related with film via language_id
"""

#%%3. How many categories of films we have in the rental
metadata = MetaData()
category = Table("category", metadata, autoload=True, autoload_with=db)
film_category = Table("film_category", metadata, autoload=True, autoload_with=db)
film = Table("film", metadata, autoload=True, autoload_with=db)
inventory = Table("inventory", metadata, autoload=True, autoload_with=db)
rental = Table("rental", metadata, autoload=True, autoload_with=db)

stmt = select([func.count(category.c.category_id.distinct())])
stmt = stmt.where(category.c.category_id == film_category.c.category_id)
stmt = stmt.where(film_category.c.film_id == film.c.film_id)
stmt = stmt.where(film.c.film_id == inventory.c.film_id)
stmt = stmt.where(inventory.c.inventory_id == rental.c.inventory_id)

print(stmt)

results = db.execute(stmt).fetchall()
print(results)

#%%4. Display list of categories with limit 2
stmt = select([category])
results = db.execute(stmt).fetchmany(size=2)
print(results)
for result in results:
    print(result.name)

#%%5. Find the oldest and youngest film in rental
stmt = select([film.c.title, func.min(film.c.release_year)]).group_by(film.c.title)
stmt = stmt.where(film.c.film_id == inventory.c.film_id)
stmt = stmt.where(inventory.c.inventory_id == rental.c.inventory_id)

results = db.execute(stmt).fetchmany(size=1)
print("Youngest film:", results)

stmt = select([film.c.title, func.max(film.c.release_year)]).group_by(film.c.title)
stmt = stmt.where(film.c.film_id == inventory.c.film_id)
stmt = stmt.where(inventory.c.inventory_id == rental.c.inventory_id)

results = db.execute(stmt).fetchmany(size=1)
print("Oldest film:", results)

#%%6. Find all actor with a name: Olympia, Julia, Ellen. 
actor = Table("actor", metadata , autoload=True, autoload_with=db)
stmt = select([actor])
stmt = stmt.where(or_(actor.c.first_name == 'Olympia', actor.c.first_name == 'Julia', actor.c.first_name == 'Ellen'))
results = db.execute(stmt).fetchall()
print(results)
    
#How can you check correction of your query?
print(stmt)