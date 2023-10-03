from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from game.program_model import Program


class DbGame:
    def __init__(self, url='sqlite:///game.db'):
        self.engine = create_engine(url)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    # Crud - CREATE
    def add_value(self, project: Program):
        self.session.add(project)
        self.session.commit()

    # Kaip i lentele irasyti daugiau eiluciu vienu metodu:
    def add_values(self, projects: list):
        self.session.add_all(projects)
        self.session.commit()

    # cRud - READ
    def get_value_by_id(self, id_num):
        value = self.session.query(Program).get(id_num)
        print(value)

    # cRud - READ
    def filter_by_name(self, name):
        value = self.session.query(Program).filter_by(name=name).all()
        print(value)

    # crUd - UPDATE
    def update_value(self, id_num, new_name, new_price):
        value = self.session.query(Program).get(id_num)
        value.name = new_name
        value.price = new_price
        self.session.commit()

    # cruD - DELETE
    def delete_value(self, id_num):
        value = self.session.query(Program).get(id_num)
        self.session.delete(value)
        self.session.commit()

    # Osvaldo HiTech:
    def filter_by_attributes(self, **kwargs):
        query = self.session.query(Program)
        for key, value in kwargs.items():
            query = query.filter(getattr(Program, key) == value)
        result = query.all()
        print(result)
