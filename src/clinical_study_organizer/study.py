import csv
import pickle

from src.clinical_study_organizer import database as db
from src.clinical_study_organizer.containers import patient as p


class Study:
    def __init__(self, attributes, database_location="../../database/patients.db"):
        self.attribute_dictionary = self._parse_attributes(attributes)
        self.database = None
        self.database_location = database_location
        self.initialized = False
        self.anonymized = True

    def initialize(self):
        self.database = db.Database(self.database_location)
        if len(self.database.is_initialized()) != 0: # todo fix
            self.delete_tables()

        self.database.initialize(self.attribute_dictionary)
        self.initialized = True

    def add_patients(self, patients):
        self.database.add_patients_attributes(patients)
        self.database.add_patients_identities(patients)

    def get_data(self, alias):
        return self.database.get_data(alias)

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
        return self.database.get_identity(alias)

    def get_all_aliases(self):
        return self.database.get_all_aliases()

    def get_all_attribute_values(self, attributes):
        return self.database.get_all_attribute_values(attributes)

    @staticmethod
    def _parse_attributes(attributes):
        attribute_dictionary = {}

        for attribute in attributes:
            attribute = attribute.split(';')
            attribute_name = attribute[0]
            attribute_type = attribute[1]

            attribute_dictionary[attribute_name] = attribute_type

        return attribute_dictionary

    @staticmethod
    def load(file_name):
        return pickle.load(open(file_name, 'rb'))

    def save(self, file_name):
        pickle.dump(self, open(file_name, 'wb'))


def read_patient_list(file_name):
    csv_data = []

    with open(file_name) as csvfile:
        read_csv = csv.reader(csvfile, skipinitialspace=True)
        for row in read_csv:
            csv_data.append(row)

    attributes = csv_data[0]
    data = csv_data[1:]

    return attributes, data


def construct_patient_list(patients, noun_list):
    patient_list = []

    for row in patients:
        id = row[0]
        last_name = row[1]
        first_name = row[2]
        data = row[3:]
        patient = p.Patient(id, last_name, first_name, data, noun_list)
        patient_list.append(patient)


    return patient_list


if __name__ == "__main__":
    attributes, data = read_patient_list('../../database/sample_patient_list.csv')
    study = Study(attributes)
    study.initialize()

    patients = construct_patient_list(data, "C:\\Users\\Michael\\AnacondaProjects\\ClinicalStudyOrganizer\\test\\test_resources\\nounlist.txt")
    study.add_patients(patients)
    info = study.get_all_attribute_values(["age", "eye_color"])

    study.delete_tables()

    # print(mean(info))

