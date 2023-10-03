from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from sql_alchemy.models import Projektas

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()


# Crud
def add_value(projektas: Projektas):
    session.add(projektas)
    session.commit()


# cRud
def get_value_by_id(id):
    value = session.query(Projektas).get(id)
    print(value)


def filter_by_name(name):
    value = session.query(Projektas).filter_by(name=name).all()
    print(value)


# crUd
def update_value(id, new_name):
    value = session.query(Projektas).get(id)
    value.name = new_name
    session.commit()


def delete_value(id):
    value = session.query(Projektas).get(id)
    session.delete(value)
    session.commit()
