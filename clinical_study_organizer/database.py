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
        attribute_string = self._get_attribute_table(attribute_dictionary)

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

        self._execute_SQL([identity_table, attribute_table])

    def delete_tables(self):
        self._execute_SQL(["DROP TABLE attributes;", "DROP TABLE identity;"])


    def _execute_SQL(self, commands):
        self._open()
        for command in commands:
            self.cursor.execute(command)
        self._close()

    def _open(self):
        self.connection = db.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def _close(self):
        self.connection.commit()
        self.connection.close()

    def add_patients_attributes(self, patients):
        queries = []

        for patient in patients:
            alias = "\'" + patient.alias + "\', "
            data = patient.data
            data_string = self._construct_patient_data(data)

            query = "INSERT INTO attributes VALUES (" + \
            alias + \
            data_string + \
            ");"

            queries.append(query)

        self._execute_SQL(queries)

    def add_patients_identities(self, patients):
        queries = []

        for patient in patients:
            query = "INSERT INTO identity VALUES (\'" + patient.alias + "\', \'" + patient.id + "\', \'" + patient.last_name + "\', \'" + patient.first_name + "\')"
            queries.append(query)

        self._execute_SQL(queries)
        
    @staticmethod
    def _construct_patient_data(data):
        patient_data = []
        
        for value in data:
            patient_data.append("\'" + str(value) + "\', ")

        remove_last_comma(patient_data)
        
        return "".join(patient_data)

    @staticmethod
    def _get_attribute_table(attribute_dictionary):
        attribute_string_list = []

        for attribute_name in (attribute for attribute in attribute_dictionary if
                               attribute != "id" and attribute != "last_name" and attribute != "first_name"):
            attribute_type = attribute_dictionary[attribute_name]
            attribute_string = attribute_name + " " + attribute_type + ",\n"

            attribute_string_list.append(attribute_string)

        remove_last_comma(attribute_string_list)

        return "".join(attribute_string_list)


def remove_last_comma(string_list):
    string_list[len(string_list) - 1] = string_list[len(string_list) - 1].replace(",", "")



