import random
import csv
import sqlite3 as db

from clinical_study_organizer.database import Database
from clinical_study_organizer.patient import Patient


class Study:
    def __init__(self, attributes):
        self.attribute_dictionary = self._parse_attributes(attributes)
        self.database = None
        self.initialized = False

    def initialize(self):
        self.database = Database("../database/patients.db")
        self.database.delete_tables() # todo delete
        self.database.initialize(self.attribute_dictionary)

        self.initialized = True

    def _parse_attributes(self, attributes):
        attribute_dictionary = {}

        for attribute in attributes:
            attribute = attribute.split(';')
            attribute_name = attribute[0]
            attribute_type = attribute[1]

            attribute_dictionary[attribute_name] = attribute_type

        return attribute_dictionary


def read_patient_list(file_name):
    csv_data = []

    with open(file_name) as csvfile:
        read_csv = csv.reader(csvfile, skipinitialspace=True)
        for row in read_csv:
            csv_data.append(row)

    return csv_data


if __name__ == "__main__":
    raw_list = read_patient_list('../database/sample_patient_list.csv')
    study = Study(raw_list[0])
    study.initialize()


