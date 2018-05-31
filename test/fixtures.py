import pytest
import sqlite3 as db
import os
from containers.data import read_patient_list, construct_patient_list, Data
from src.clinical_study_organizer.study import Study


@pytest.fixture
def study(database_location, data):
    study = Study(data, database_location)
    return study


@pytest.fixture
def data(test_list, noun_list):
    return Data(test_list, noun_list)


@pytest.fixture
def attributes(test_list):
    return read_patient_list(test_list)


@pytest.fixture
def patients(attributes, noun_list):
    return construct_patient_list(attributes[1], noun_list)


@pytest.fixture
def database_location():
    here = os.path.abspath(os.path.dirname(__file__))
    return here + "/test_resources/test.db"


@pytest.fixture
def noun_list():
    here = os.path.abspath(os.path.dirname(__file__))
    return  here + "/test_resources/nounlist.txt"


@pytest.fixture
def test_list():
    here = os.path.abspath(os.path.dirname(__file__))
    return here + "/test_resources/sample_patient_list.csv"


@pytest.fixture
def database_cursor(database_location):
    connection = db.connect(database_location)
    cursor = connection.cursor()

    yield cursor

    connection.close()
