import pytest
import sqlite3 as db
import os
from containers.data import read_patient_list, construct_patient_list, Data
from containers.query import get_initial_tables
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
def raw_database_cursor(database_location):
    connection = db.connect(database_location)
    cursor = connection.cursor()

    existing_tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='identity';").fetchall()

    if len(existing_tables) != 0:
        cursor.execute("DROP TABLE attributes;")
        cursor.execute("DROP TABLE identity;")

    yield cursor

    connection.close()


@pytest.fixture
def constructed_database_cursor(database_location, data):
    connection = db.connect(database_location)
    cursor = connection.cursor()

    existing_tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='identity';").fetchall()

    if len(existing_tables) != 0:
        cursor.execute("DROP TABLE attributes;")
        cursor.execute("DROP TABLE identity;")

    attribute_table, identity_table = get_initial_tables(data.get_attribute_types())

    cursor.execute(attribute_table)
    cursor.execute(identity_table)

    yield cursor

    connection.close()