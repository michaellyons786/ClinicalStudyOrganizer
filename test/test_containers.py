from sqlite3 import OperationalError

import pytest

from src.clinical_study_organizer.containers.query import construct_patients_attributes, construct_patients_identities, get_initial_tables, \
    construct_all_attribute_values
from test.fixtures import *


def test_read_patient_list(attributes):
    attribute_names = attributes[0]
    data = attributes[1]

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
        assert(0 == 1) # todo find assertFail


def test_construct_patients_identities(patients, constructed_database_cursor):
    queries = construct_patients_identities(patients)

    try:
        for query in queries:
            constructed_database_cursor.execute(query)
    except OperationalError:
        assert (0 == 1)  # todo find assertFail


def test_get_initial_tables(data, raw_database_cursor):
    attribute_table, identity_table = get_initial_tables(data.get_attribute_types())

    try:
        raw_database_cursor.execute(attribute_table)
        raw_database_cursor.execute(identity_table)
    except OperationalError:
        assert(0 == 1) # todo find assertFail


def test_construct_all_attribute_values(data, constructed_database_cursor):
    query = construct_all_attribute_values(data.get_alias_attribute_names())

    constructed_database_cursor.execute(query)

    try:
        constructed_database_cursor.execute(query)
    except OperationalError:
        assert(0 == 1) # todo find assertFail





