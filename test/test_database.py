import random

from test.fixtures import *


def test_database_initialization(database, data):
    database.initialize(data.get_attribute_types())

    assert(database.is_initialized())


def test_database_delete_tables(database, raw_database_cursor, data):
    database.initialize(data.get_attribute_types())
    database.delete_tables()

    tables = raw_database_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='identity';").fetchall()

    assert(len(tables) == 0)


def test_database_add_patients(database, patients, raw_database_cursor, data):
    database.initialize(data.get_attribute_types())
    database.add_patients(patients)

    alias_list = raw_database_cursor.execute("SELECT * FROM attributes").fetchall()
    identity_list = raw_database_cursor.execute("SELECT * FROM identity").fetchall()


    assert(alias_list[0][3] == 'brown')
    assert(alias_list[19][2] == 179)
    assert (identity_list[0][1] == 7698)
    assert (identity_list[19][3] == "Oretha")


def test_database_get_alias_data(database, patients, data):
    database.initialize(data.get_attribute_types())
    database.add_patients(patients)
    aliases = database.get_all_aliases()
    alias = random.choice(aliases)

    alias_data = database.get_alias_data(alias)

    assert(alias_data[0] == alias)
    assert (patient_value_exists(alias_data[1], patients))


def test_database_get_alias_identity(database, patients, data):
    database.initialize(data.get_attribute_types())
    database.add_patients(patients)
    aliases = database.get_all_aliases()
    alias = aliases[0]

    id_data = database.get_alias_identity(alias)

    assert(id_data[0] == alias)
    assert(patient_value_exists(id_data[1], patients))


def test_database_get_alias(database, data, patients):
    database.initialize(data.get_attribute_types())
    database.add_patients(patients)
    id = 1652
    alias = database.get_alias(id)

    assert(len(alias) != 0)


def test_database_get_identity_attributes(database, data, patients):
    database.initialize(data.get_attribute_types())
    database.add_patients(patients)
    id = 1652
    aliases = database.get_all_aliases()
    id_data = database.get_identity_attributes(id)

    assert(id_data[0] in aliases)
    assert(id_data[1] == 36)
    assert(id_data[3] == 'blue')


def test_database_get_all_attribute_values(database, data, patients):
    database.initialize(data.get_attribute_types())
    database.add_patients(patients)
    attribute_names = ['eye_color', 'age']
    results = database.get_all_attribute_values(attribute_names)
    aliases = database.get_all_aliases()
    alias = aliases[0]

    assert(len(results.get(alias)) != 0)



def patient_value_exists(value, patients):

    for patient in patients:
        value = str(value)
        if value in patient.data or value == patient.alias or value == patient.id or value == patient.first_name or value == patient.last_name:
            return True

    return False
