from src.clinical_study_organizer.study import *
import os
import pytest


def test_read_patient_list(attributes):
    attribute_names = attributes[0]
    data = attributes[1]

    assert("Kolbe" in data[0])
    assert("Maycock" in data[19])
    assert("id;INT" in attribute_names[0])
    assert("eye_color;VARCHAR" in attribute_names[5])

def test_construct_patient_list(patients):

    assert (patients[0].first_name == "Cathi")
    assert (patients[19].first_name == "Oretha")
    assert (patients[0].id == '7698')
    assert (patients[19].id == '5782')

def test_study(study):
    query_result = study.get_all_attribute_values(["age", "eye_color"])

    aliases = study.get_all_aliases()
    patient1 = aliases[0][0] # todo fix query result
    patient2 = aliases[len(aliases) - 1][0]
    patient1_attributes = query_result.get_attributes(patient1)
    patient2_attributes = query_result.get_attributes(patient2)

    patient1_identity = study.get_identity(patient1)
    patient2_identity = study.get_identity(patient2)

    patient1_indirect_attributes = study.get_identity_attributes(patient1_identity[0][1])
    patient2_indirect_attributes = study.get_identity_attributes(patient2_identity[0][1])

    assert(query_result.attributes_names[0] == "age")
    assert(patient1_attributes[0] == patient1_indirect_attributes[0][1])
    assert(patient1_attributes[1] == patient1_indirect_attributes[0][3])
    assert(patient2_attributes[0] == patient2_indirect_attributes[0][1])
    assert(patient2_attributes[1] == patient2_indirect_attributes[0][3])

    study.delete_tables()

def get_database_location():
    here = os.path.abspath(os.path.dirname(__file__))
    database_location = here + "/test_resources/test.db"
    return database_location


@pytest.fixture
def study():
    database_location = get_database_location()
    study = Study(attributes, database_location)
    study.initialize()
    study.add_patients(patients)
    return study


@pytest.fixture
def attributes():
    here = os.path.abspath(os.path.dirname(__file__))
    test_list = here + "/test_resources/sample_patient_list.csv"
    return read_patient_list(test_list)


@pytest.fixture
def patients(attributes):
    here = os.path.abspath(os.path.dirname(__file__))
    noun_list = here + "/test_resources/nounlist.txt"
    patients = construct_patient_list(attributes[1], noun_list)
    return patients
