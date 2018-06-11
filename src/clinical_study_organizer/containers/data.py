import csv

from src.clinical_study_organizer.containers.patient import Patient


class Data():
    def __init__(self, file_name, noun_list_location):
        raw_attribute_names, data = read_patient_list(file_name)
        attribute_names, attribute_types = parse_attribute_names(raw_attribute_names)

        self.identity_attribute_names = ['id', 'last_name', 'first_name']
        self.alias_attribute_names = remove_id_names(attribute_names, self.identity_attribute_names)
        self.attribute_types = attribute_types
        self.patients = construct_patient_list(data, noun_list_location)

    def get_alias_attribute_names(self):
        return self.alias_attribute_names

    def get_identity_attribute_names(self):
        return self.identity_attribute_names

    def get_attribute_types(self):
        return self.attribute_types

    def get_patients(self):
        return self.patients


def remove_id_names(attribute_names, identity_names):

    for id_name in identity_names:
        attribute_names.remove(id_name)

    return attribute_names


def read_patient_list(file_name):
    csv_data = []

    with open(file_name) as csvfile:
        read_csv = csv.reader(csvfile, skipinitialspace=True)
        for row in read_csv:
            csv_data.append(row)

    raw_attribute_names = csv_data[0]
    raw_data = csv_data[1:]

    return raw_attribute_names, raw_data


def construct_patient_list(raw_data, noun_list_location):
    patient_list = []
    noun_list = construct_noun_list(noun_list_location)

    for row in raw_data:
        id = row[0]
        last_name = row[1]
        first_name = row[2]
        data = row[3:]
        patient = Patient(id, last_name, first_name, data, noun_list)
        patient_list.append(patient)

    return patient_list


def parse_attribute_names(raw_names):
    attribute_types = {}
    attribute_names = []

    for row in raw_names:
        row = row.split(';')
        attribute_name = row[0]
        attribute_names.append(attribute_name)
        attribute_type = row[1]

        attribute_types[attribute_name] = attribute_type

    return attribute_names, attribute_types


def construct_noun_list(noun_list_location):
    file = open(noun_list_location)
    noun_list = []

    for row in file:
        noun_list.append(row.replace("\n", ""))

    return noun_list
