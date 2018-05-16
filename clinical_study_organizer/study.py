import random
import csv

from clinical_study_organizer.database import Database
from clinical_study_organizer.patient import Patient


class Study:
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names


def read_patient_list(file_name):
    csv_data = []

    with open(file_name) as csvfile:
        read_csv = csv.reader(csvfile)
        for row in read_csv:
            csv_data.append(row)

    return csv_data

if __name__ == "__main__":
    raw_list = read_patient_list('../data/sample_patient_list.csv')
    study = Study(raw_list[0])

    database = Database(r"M:\sqlite\SQLiteStudio\databases\patients.db")

    patient_row = raw_list[1]
    patient_data = [patient_row[3], patient_row[4], patient_row[5]]
    patient = Patient(patient_row[0], patient_row[1], patient_row[2], patient_data)

    database.add_alias_patient(patient)


