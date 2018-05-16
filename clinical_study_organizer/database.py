import sqlite3 as db


# Written with help of https://docs.python.org/2/library/sqlite3.html
class Database:
    def __init__(self, database_name):
        self.connection = db.connect(database_name)
        self.cursor = self.connection.cursor()

    def _execute_SQL(self, command):
        self.cursor.execute(command)

    def _commit(self):
        self.connection.commit()

    def _close(self):
        self.connection.close()

    def add_raw_patient(self, patient):

        query = "INSERT INTO raw_data VALUES (\'" + patient.last_name + "\', \'" + patient.first_name + "\', \'" + patient.id + "\', \'" + patient.alias + "\')"
        self._execute_SQL(query)

        self._commit()
        self._close()

    def add_alias_patient(self, patient):
        data = patient.data
        a = data[0]
        b = data[1]
        c = data[2]

        data = a + ', ' + b + ', ' + c

        query = "INSERT INTO raw_data VALUES (\'" + patient.alias + "\', \'" + data + "\')"

        self._execute_SQL(query)

        self._commit()
        self._close()



