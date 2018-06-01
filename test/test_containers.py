from sqlite3 import OperationalError

import pytest
import random

from src.clinical_study_organizer.containers.query_result import Query_Result
from src.clinical_study_organizer.containers.query import construct_patients_attributes, construct_patients_identities, \
    get_initial_tables, \
    construct_all_attribute_values, remove_last_comma
from test.fixtures import *


def test_read_patient_list(raw_names_and_data):
    attribute_names = raw_names_and_data[0]
    data = raw_names_and_data[1]

    assert ("Kolbe" in data[0])
    assert ("Maycock" in data[19])
    assert ("id;INT" in attribute_names[0])
    assert ("eye_color;VARCHAR" in attribute_names[5])


def test_construct_patient_list(patients):
    assert (patients[0].first_name == "Cathi")
    assert (patients[19].first_name == "Oretha")
    assert (patients[0].id == '7698')
    assert (patients[19].id == '5782')


def test_construct_patients_attributes(patients, constructed_database_cursor):
    queries = construct_patients_attributes(patients)

    try:
        for query in queries:
            constructed_database_cursor.execute(query)
    except OperationalError:
        pytest.fail("Exception not expected, test failed.")


def test_construct_patients_identities(patients, constructed_database_cursor):
    queries = construct_patients_identities(patients)

    try:
        for query in queries:
            constructed_database_cursor.execute(query)
    except OperationalError:
        pytest.fail("Exception not expected, test failed.")


def test_get_initial_tables(data, raw_database_cursor):
    attribute_table, identity_table = get_initial_tables(data.get_attribute_types())

    try:
        raw_database_cursor.execute(attribute_table)
        raw_database_cursor.execute(identity_table)
    except OperationalError:
        pytest.fail("Exception not expected, test failed.")


def test_construct_all_attribute_values(data, constructed_database_cursor):
    query = construct_all_attribute_values(data.get_alias_attribute_names())

    constructed_database_cursor.execute(query)

    try:
        constructed_database_cursor.execute(query)
    except OperationalError:
        pytest.fail("Exception not expected, test failed.")


def test_remove_last_comma():
    example = ["abba, ", "dabba, ", "bobabba, "]
    remove_last_comma(example)

    assert(example == ["abba, ", "dabba, ", "bobabba "])


def test_query_result_get_aliases(query_result):
    aliases = query_result.get_aliases()

    assert(len(aliases) != 0)


def test_query_result_get_attributes(query_result):

    aliases = query_result.get_aliases()
    alias = random.choice(aliases)

    all_attributes = query_result.get_attributes(alias)

    assert(len(all_attributes) != 0)





