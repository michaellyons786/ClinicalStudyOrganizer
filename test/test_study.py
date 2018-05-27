from src.clinical_study_organizer.study import *
from os import path

def test_read_patient_list():
    attributes, data = get_attributes()

    assert("Kolbe" in data[0])
    assert("Maycock" in data[19])
    assert("id;INT" in attributes[0])
    assert("eye_color;VARCHAR" in attributes[5])


def test_construct_patient_list():
    test_list = "test_resources/sample_patient_list.csv"
    attributes, data = read_patient_list(test_list)

    noun_list = "test_resources/nounlist.txt"
    patients = construct_patient_list(data, noun_list)

    assert (patients[0].first_name == "Cathi")
    assert (patients[19].first_name == "Oretha")
    assert (patients[0].id == '7698')
    assert (patients[19].id == '5782')


def test_study():
    test_list = "../database/sample_patient_list.csv"
    attributes, data = read_patient_list(test_list)

    study = Study(attributes)


def get_attributes():
    here = path.abspath(path.dirname(__file__))
    print("[DEBUG MI] " + here)

    test_list = here + "test_resources/sample_patient_list.csv"
    attributes, data = read_patient_list(test_list)
    return attributes, data
