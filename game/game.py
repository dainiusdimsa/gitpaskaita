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

    def filter_by_attributes_game(self):
        attributes = {}
        while True:
            key = input('Ivesk atributus (Spausk ENTER, kad baigtum): ')
            if not key:
                break
            value = input(f'Parasyk {key}: ')
            attributes[key] = value
        self.filter_by_attributes(**attributes)

    def update_by_id(self):
        while True:
            id_num = int(input('Ivesk ID: '))
            new_name = input('Ivesk nauja pavadinima: ')
            try:
                new_price = float(input('Ivesk nauja kaina: '))
            except Exception:
                print('reikia ivesti float')
                continue
            self.update_value(id_num=id_num, new_name=new_name, new_price=new_price)
            break

    def delete_value_game(self):
        id_num = int(input('Ivesk ID: '))
        self.delete_value(id_num=id_num)

    def get_all(self):
        values = self.session.query(Program).all()
        print(values)

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
