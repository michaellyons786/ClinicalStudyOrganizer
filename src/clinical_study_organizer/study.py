import csv
import pickle

from src.clinical_study_organizer.database import Database


class Study:
    def __init__(self, data, database_location="../../database/patients.db"):
        self.attribute_types = data.get_attribute_types()
        self.attribute_names = data.get_alias_attribute_names()
        self.database = None
        self.database_location = database_location
        self.initialized = False
        self.anonymized = True

    def initialize(self):
        self.database = Database(self.database_location)
        if len(self.database.is_initialized()) != 0: # todo fix
            self.delete_tables()

        self.database.initialize(self.attribute_types)
        self.initialized = True

    def add_patients(self, patients):
        self.database.add_patients(patients)

    def get_data(self, alias):
        return self.database.get_alias_data(alias)

    def delete_tables(self):
        self.database.delete_tables()

    def get_alias(self, id):
        if type(id) != 'str':
            id = str(id)

        return self.database.get_alias(id)

    def get_identity_attributes(self, id):
        if type(id) != 'str':
            id = str(id)

        return self.database.get_identity_attributes(id)

    def get_identity(self, alias):
        self.anonymized = False
        return self.database.get_alias_identity(alias)

    def get_all_aliases(self):
        return self.database.get_all_aliases()

    def get_all_attribute_values(self, attribute_names):
        return self.database.get_all_attribute_values(attribute_names)

    @staticmethod
    def load(file_name):
        return pickle.load(open(file_name, 'rb'))

    def save(self, file_name):
        pickle.dump(self, open(file_name, 'wb'))

