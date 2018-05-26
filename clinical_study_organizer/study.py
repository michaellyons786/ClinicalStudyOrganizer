import csv
import pickle

from clinical_study_organizer.clinical_statistics import *
from clinical_study_organizer.database import Database
from clinical_study_organizer.containers.patient import Patient


class Study:
    def __init__(self, attributes):
        self.attribute_dictionary = self._parse_attributes(attributes)
        self.database = None
        self.initialized = False
        self.anonymized = True

    def initialize(self):
        self.database = Database("../database/patients.db")
        self.database.delete_tables()  # todo delete
        self.database.initialize(self.attribute_dictionary)

        self.initialized = True

    def add_patients(self, patients):
        self.database.add_patients_attributes(patients)
        self.database.add_patients_identities(patients)

    def get_data(self, alias):
        return self.database.get_data(alias)

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


def construct_patient_list(patients):
    patient_list = []

    for row in patients:
        id = row[0]
        last_name = row[1]
        first_name = row[2]
        data = row[3:]
        patient = Patient(id, last_name, first_name, data)
        patient_list.append(patient)

    return patient_list


if __name__ == "__main__":
    attributes, data = read_patient_list('../database/sample_patient_list.csv')
    study = Study(attributes)
    study.initialize()

    patients = construct_patient_list(data)
    study.add_patients(patients)
    info = study.get_all_attribute_values(["age", "eye_color"])

    print(mean(info))

