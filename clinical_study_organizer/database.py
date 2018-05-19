import sqlite3 as db


# Written with help of https://docs.python.org/2/library/sqlite3.html
class Database:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None
        self.cursor = None

    def get_data(self, alias):
        query = r"'SELECT * FROM alias WHERE alias = {a}'".format(a = alias)
        self._execute_SQL(query)

    def initialize(self, attribute_dictionary):
        attribute_string = self._get_attribute_string(attribute_dictionary)

        identity_table = "CREATE TABLE identity (" \
                         "alias      VARCHAR REFERENCES alias (alias),\n" \
                         "id         INT UNIQUE PRIMARY KEY,\n" \
                         "last_name         VARCHAR,\n" \
                         "first_name         VARCHAR" \
                         ");"

        attribute_table = "CREATE TABLE attributes (\n" \
                          "alias    VARCHAR PRIMARY KEY UNIQUE,\n" + \
                          attribute_string + \
                          ");"

        print(attribute_table)

        self._execute_SQL(identity_table)
        self._execute_SQL(attribute_table)

    @staticmethod
    def _get_attribute_string(attribute_dictionary):
        attribute_string_list = []

        for attribute_name in (attribute for attribute in attribute_dictionary if attribute != "id" and attribute != "last_name" and attribute != "first_name"):
            attribute_type = attribute_dictionary[attribute_name]
            attribute_string = attribute_name + " " + attribute_type + ",\n"

            attribute_string_list.append(attribute_string)

        attribute_string_list[len(attribute_string_list) - 1] = attribute_string_list[len(attribute_string_list) - 1].replace(",", "")

        return "".join(attribute_string_list)

    def _execute_SQL(self, command):
        self._open()
        self.cursor.execute(command)
        self._close()

    def _open(self):
        self.connection = db.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def _close(self):
        self.connection.commit()
        self.connection.close()

    def add_raw_patient(self, patient):

        query = "INSERT INTO raw_data VALUES (\'" + patient.last_name + "\', \'" + patient.first_name + "\', \'" + patient.id + "\', \'" + patient.alias + "\')"
        self._execute_SQL(query)

        self._close()

    def add_alias_patient(self, patient):
        data = patient.data
        a = data[0]
        b = data[1]
        c = data[2]

        data = a + ', ' + b + ', ' + c

        query = "INSERT INTO raw_data VALUES (\'" + patient.alias + "\', \'" + data + "\')"

        self._execute_SQL(query)

        self._close()



