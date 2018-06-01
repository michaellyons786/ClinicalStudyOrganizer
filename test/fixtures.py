import pytest
import sqlite3 as db
import os

from src.clinical_study_organizer.containers.query_result import Query_Result
from src.clinical_study_organizer.containers.data import read_patient_list, construct_patient_list, Data
from src.clinical_study_organizer.containers.query import get_initial_tables, construct_patients_attributes, \
    construct_patients_identities, construct_all_attribute_values
from src.clinical_study_organizer.study import Study


@pytest.fixture
def study(database_location, data):
    study = Study(data, database_location)
    return study


@pytest.fixture
def data(test_list, noun_list):
    return Data(test_list, noun_list)


@pytest.fixture
def raw_names_and_data(test_list):
    return read_patient_list(test_list)


@pytest.fixture
def patients(raw_names_and_data, noun_list):
    return construct_patient_list(raw_names_and_data[1], noun_list)


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
def populated_database_cursor(constructed_database_cursor, patients):
    patients_queries = construct_patients_attributes(patients)
    aliases_queries = construct_patients_identities(patients)


    execute_SQL_commands(patients_queries, constructed_database_cursor)
    execute_SQL_commands(aliases_queries, constructed_database_cursor)


    return constructed_database_cursor


@pytest.fixture
def query_result(data, populated_database_cursor):
    query = construct_all_attribute_values(data.get_alias_attribute_names())
    result = populated_database_cursor.execute(query).fetchall()

    return Query_Result(result, data.get_alias_attribute_names)


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


def execute_SQL_commands(queries, cursor):
    for query in queries:
        cursor.execute(query)

