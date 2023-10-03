import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///projektai.db')
Base = declarative_base()


class Projektas(Base):
    __tablename__ = 'projektas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column("Pavadinimas", String, default='Knyga')
    price = Column("Kaina", Float)
    is_or_not = Column('Yra', Boolean)
    created_date = Column("Sukūrimo data", DateTime, default=datetime.datetime.now)

    def __init__(self, name, price, is_or_not):
        self.name = name
        self.price = price
        self.is_or_not = is_or_not

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"


Base.metadata.create_all(engine)
