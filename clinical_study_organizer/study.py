import random
import csv
import sqlite3 as db

from clinical_study_organizer.database import Database
from clinical_study_organizer.patient import Patient


class Study:
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
        self.database = None
        self.initialized = False

    def initialize(self):
        self.database = Database("../database/patients.db")

        identity_table = r"CREATE TABLE identity (alias      VARCHAR REFERENCES alias (alias), " \
                         r"id         INTEGER UNIQUE PRIMARY KEY, " \
                         r"last_name  VARCHAR, " \
                         r"first_name VARCHAR);"

        self.database._execute_SQL(identity_table)

        self.initialized = True


def read_patient_list(file_name):
    csv_data = []

    with open(file_name) as csvfile:
        read_csv = csv.reader(csvfile)
        for row in read_csv:
            csv_data.append(row)

    return csv_data


if __name__ == "__main__":
    raw_list = read_patient_list('../database/sample_patient_list.csv')
    study = Study(raw_list[0])
    study.initialize()


