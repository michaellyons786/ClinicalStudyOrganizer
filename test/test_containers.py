from sqlite3 import OperationalError

import pytest
import random

from src.clinical_study_organizer.containers.patient import get_unique_second_word, get_alias, Patient
from src.clinical_study_organizer.containers.query_result import Query_Result
from src.clinical_study_organizer.containers.query import construct_patients_attributes, construct_patients_identities, \
    get_initial_tables, \
    construct_all_attribute_values, remove_last_comma
from test.fixtures import *
from src.clinical_study_organizer.containers.data import construct_noun_list, parse_attribute_names, remove_id_names


# ----------------------QUERY-------------------------------
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


# ----------------------QUERY_RESULT-------------------------------
def test_query_result_get_aliases(query_result):
    aliases = query_result.get_aliases()

    assert(len(aliases) != 0)


def test_query_result_get_attributes(query_result):

    aliases = query_result.get_aliases()
    alias = random.choice(aliases)

    all_attributes = query_result.get_attributes(alias)

    assert(len(all_attributes) != 0)


# ----------------------PATIENT-------------------------------
def test_get_unique_second_word():
    test_words = ['abba', 'babba', 'cabba']
    first_word = random.choice(test_words)

    for _ in range(100):
        second_word = get_unique_second_word(first_word, test_words)
        assert(first_word != second_word)


def test_get_alias():
    test_words = ['abba', 'babba', 'cabba']

    alias = get_alias(test_words)
    assert(len(alias) != 0)
    assert(test_words[0] in alias or test_words[1] in alias or test_words[2] in alias)


def test_patient():
    patient = Patient(32, "johnson", "john", [3, 4, 5], ["ab", "ba"])

    assert(patient.id == 32)
    assert(patient.last_name == "johnson")
    assert(patient.first_name == "john")
    assert(patient.data == [3, 4, 5])
    assert("ab" in patient.alias and "ba" in patient.alias)


# ----------------------DATA-------------------------------
def test_data(data):
    assert(data.identity_attribute_names[0] == "id")
    assert(data.alias_attribute_names[0] == "age")
    assert(data.attribute_types["id"] == "INT")
    assert(data.patients[0].id == "7698")


def test_construct_noun_list(noun_list_location):
    nouns = construct_noun_list(noun_list_location)

    assert(type(nouns) == list)
    assert(len(nouns) == 4551)


def test_parse_attribute_names(raw_names_and_data):
    raw_names = raw_names_and_data[0]
    attribute_names, attribute_types = parse_attribute_names(raw_names)

    assert(attribute_names[0] == "id")
    assert(attribute_names[5] == "eye_color")
    assert(attribute_types["id"] == "INT")
    assert(attribute_types["eye_color"] == "VARCHAR")


def test_construct_patient_list(patients):
    assert (patients[0].first_name == "Cathi")
    assert (patients[19].first_name == "Oretha")
    assert (patients[0].id == '7698')
    assert (patients[19].id == '5782')


def test_read_patient_list(raw_names_and_data):
    attribute_names = raw_names_and_data[0]
    data = raw_names_and_data[1]

    assert ("Kolbe" in data[0])
    assert ("Maycock" in data[19])
    assert ("id;INT" in attribute_names[0])
    assert ("eye_color;VARCHAR" in attribute_names[5])


def test_remove_id_names(raw_names_and_data):
    attribute_names, _ = parse_attribute_names(raw_names_and_data[0])
    ids = ["id", "last_name", "first_name"]
    attribute_names = remove_id_names(attribute_names, ids)

    assert("id" not in attribute_names)
    assert("last_name" not in attribute_names)
    assert("first_name" not in attribute_names)
    assert(len(attribute_names) != 0)




