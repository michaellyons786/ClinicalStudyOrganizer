import pytest
from src.clinical_study_organizer.study import Study, read_patient_list, construct_patient_list
import os


@pytest.fixture
def study(database_location, attributes, patients):
    study = Study(attributes[0], database_location)
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

@pytest.fixture
def database_location():
    here = os.path.abspath(os.path.dirname(__file__))
    database_location = here + "/test_resources/test.db"
    return database_location