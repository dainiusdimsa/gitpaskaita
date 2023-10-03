from game.db_management_game import DbGame
from game.program_model import Program
from sql_alchemy.constants import print_menu


class Game(DbGame):

    def create_value(self):
        name = input('Ivesk pavadinima: ')
        price = int(input('Ivesk kaina: '))
        project = Program(name=name, price=price)
        self.add_value(project=project)

    def read_value_by_id(self):
        id_num = int(input('Ivesk ID: '))
        self.get_value_by_id(id_num=id_num)

    def filter_by_name_game(self):
        name = input('Filtruoti pagal pavadinima: ')
        self.filter_by_name(name=name)

    # !!!!!!!BLOGAI!!!!!!!:
    def filter_by_attributes_game(self):
        name = input('Filtruoti pagal pavadinima: ')
        price = input('Filtruoti pagal kaina: ')
        self.filter_by_attributes(name=name, price=price)
    # !!!!!!!!!!!!!!!!!!!!!

    def update_by_id(self):
        id_num = int(input('Ivesk ID: '))
        new_name = input('Ivesk nauja pavadinima: ')
        new_price = input('Ivesk nauja kaina: ')
        self.update_value(id_num=id_num, new_name=new_name, new_price=new_price)

    def delete_value_game(self):
        id_num = int(input('Ivesk ID: '))
        self.delete_value(id_num=id_num)

    def get_all(self):
        value = self.session.query(Program).all()
        print(value)

    def run(self):
        while True:
            print(print_menu)
            try:
                value = int(input('Pasirinkite veiksma: '))
                if value == 8:
                    print('Programa uzdaryta')
                    break
                data_crud = {
                    1: self.create_value,
                    2: self.read_value_by_id,
                    3: self.filter_by_name_game,
                    4: self.filter_by_attributes_game,
                    5: self.update_by_id,
                    6: self.delete_value_game,
                    7: self.get_all,
                }
                data_crud[value]()
            except ValueError:
                print('KLAIDA: Pasirinkite numeri')
