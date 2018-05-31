from sqlite3 import OperationalError

import pytest

from containers.query import construct_patients_attributes, construct_patients_identities
from src.clinical_study_organizer.containers import *
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


def test_construct_patients_attributes(patients, database_cursor):
    queries = construct_patients_attributes(patients)

    try:
        for query in queries:
            database_cursor.execute(query)
    except OperationalError:
        assert(0 == 1) # todo find assertFail


def test_construct_patients_identities(patients, database_cursor):
    queries = construct_patients_identities(patients)

    try:
        for query in queries:
            database_cursor.execute(query)
    except OperationalError:
        assert (0 == 1)  # todo find assertFail
