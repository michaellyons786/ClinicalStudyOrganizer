from src.clinical_study_organizer.study import *
import os

def test_read_patient_list():
    attributes, data = get_attributes()

    assert("Kolbe" in data[0])
    assert("Maycock" in data[19])
    assert("id;INT" in attributes[0])
    assert("eye_color;VARCHAR" in attributes[5])


def test_construct_patient_list():
    attributes, data = get_attributes()
    patients = get_patients(data)

    assert (patients[0].first_name == "Cathi")
    assert (patients[19].first_name == "Oretha")
    assert (patients[0].id == '7698')
    assert (patients[19].id == '5782')

def test_study():
    attributes, data = get_attributes()
    patients = get_patients(data)

    study = set_up_study(attributes, patients)

    query_result = study.get_all_attribute_values(["age", "eye_color"])

    assert(query_result.attributes_names[0] == "age")

    study.delete_tables()


def set_up_study(attributes, patients):
    database_location = get_database_location()
    study = Study(attributes, database_location)
    study.initialize()
    study.add_patients(patients)
    return study


def get_database_location():
    here = os.path.abspath(os.path.dirname(__file__))
    database_location = here + "/test_resources/test.db"
    return database_location


def get_attributes():
    here = os.path.abspath(os.path.dirname(__file__))
    test_list = here + "/test_resources/sample_patient_list.csv"
    return read_patient_list(test_list)


def get_patients(data):
    here = os.path.abspath(os.path.dirname(__file__))
    noun_list = here + "/test_resources/nounlist.txt"
    patients = construct_patient_list(data, noun_list)
    return patients
