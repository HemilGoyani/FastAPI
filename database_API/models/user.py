from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

users = Table('users',meta,
              Column('id',Integer,primary_key=True),
              Column('name',String(20)),
              Column('address',String(255)),
              Column('password',String(255))
              )