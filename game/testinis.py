import sqlite3

def __init__(self, url='sqlite:///game.db'):
    super().__init__(url)
    self.url = url
    self.connection = sqlite3.connect(self.url)
    self.cursor = self.connection.cursor()

    # sql uzklausos paleidimas:


def __run_sql_query(self, sql_query):
    self.cursor.execute(sql_query)
    self.connection.commit()

def get_all(self):
    sql_query = """
        SELECT *
        FROM game;
        """
    self.__run_sql_query(sql_query=sql_query)