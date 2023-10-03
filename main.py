from game.db_management_game import DbGame
from game.game import Game


from sql_alchemy.db_management import DbManage
from sql_alchemy.models import Projektas

# fields = Projektas(name='Lova', price=1000, is_or_not=True)
# fields_2 = [
#     Projektas(name='Vaza', price=150, is_or_not=True),
#     Projektas(name='Staliukas', price=250, is_or_not=False),
#     Projektas(name='Fotelis', price=350, is_or_not=True),
# ]

# db = DbManage()
# db = DbGame()

# db.add_value(project=fields)
# db.add_values(projects=fields_2)
# db.get_value_by_id(id_num=2)
# db.filter_by_name(name='Dainius')
# db.update_value(id_num=2, new_name='Andrius', new_price=25)
# db.delete_value(id_num=5)
# db.filter_by_attributes(name='Kede', price=50)

game = Game()

# game.create_value()
# game.read_value_by_id()
# game.filter_by_id()
# game.filter_by_attributes_game()
# game.update_by_id()
# game.delete_value()
# game.get_all()

game.run()
