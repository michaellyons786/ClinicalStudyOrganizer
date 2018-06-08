import sqlite3 as db

# Written with help of https://docs.python.org/2/library/sqlite3.html
from src.clinical_study_organizer.containers.query_result import Query_Result
from src.clinical_study_organizer.containers.query import get_initial_tables, construct_patients_attributes, \
    construct_patients_identities, construct_all_attribute_values


class Database:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None
        self.cursor = None

    def initialize(self, attribute_dictionary):
        attribute_table, identity_table = get_initial_tables(attribute_dictionary)
        self._execute_SQL([identity_table, attribute_table])

    def delete_tables(self):
        self._execute_SQL(["DROP TABLE attributes;", "DROP TABLE identity;"])

    def add_patients_attributes(self, patients):
        self._execute_SQL(construct_patients_attributes(patients))

    def add_patients_identities(self, patients):
        queries = construct_patients_identities(patients)
        self._execute_SQL(queries)

    def get_data(self, alias):
        query = "SELECT * FROM attributes WHERE alias = \'{a}\';".format(a=alias)
        return self._query_database(query)

    def get_identity(self, alias):
        query = "SELECT * FROM identity WHERE alias = \'{a}\';".format(a=alias)
        return self._query_database(query)

    def get_alias(self, id):
        query = "SELECT alias FROM identity WHERE id = {i};".format(i=id)
        return self._query_database(query)

    def get_identity_attributes(self, id):
        alias = self.get_alias(id)[0][0] # todo fix
        return self.get_data(alias)

    def get_all_aliases(self):
        query = "SELECT alias FROM attributes;"
        return self._query_database(query)

    def get_all_attribute_values(self, attribute_names):
        query_string = construct_all_attribute_values(attribute_names)

        return Query_Result(self._query_database(query_string), attribute_names)

    def is_initialized(self):
        results = self._query_database("SELECT name FROM sqlite_master WHERE type='table' AND name='identity';")

        if len(results) != 0:
            return True
        else:
            return False

    def _execute_SQL(self, commands):
        self._open()
        for command in commands:
            self.cursor.execute(command)
        self._close()

    def _query_database(self, query, attributes=None):
        self._open()
        self.cursor.execute(query)
        info = self.cursor.fetchall()
        self._close()

        return info

    def _open(self):
        self.connection = db.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def _close(self):
        self.connection.commit()
        self.connection.close()




