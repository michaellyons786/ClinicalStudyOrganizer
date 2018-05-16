import sqlite3 as db


# Written with help of https://docs.python.org/2/library/sqlite3.html
class Database():
    def __init__(self, database_name):
        self.connection = db.connect(database_name)
        self.cursor = self.connection.cursor()

    def _execute_SQL(self, command):
        self.cursor.execute(command)

    def _commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

    def add_raw_patient(self, patient):
        query = "INSERT INTO raw_data VALUES (" + patient.last_name + ", " + patient.first_name + ", " + patient.id + ")"
        self._execute_SQL(query)


