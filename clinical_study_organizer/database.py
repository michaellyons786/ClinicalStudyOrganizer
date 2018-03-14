import sqlite3 as db


# Written with help of https://docs.python.org/2/library/sqlite3.html
class Database():
    def __init__(self, database_name):
        self.connection = db.connect(database_name)
        self.cursor = self.connection.cursor()

    def execute_SQL(self, command):
        self.cursor.execute(command)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
