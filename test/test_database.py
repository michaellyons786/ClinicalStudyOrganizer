from test.fixtures import *


def test_database_initialization(database, data):
    database.initialize(data.get_attribute_types())

    assert(database.is_initialized())


def test_database_delete_tables(database, raw_database_cursor, data):
    database.initialize(data.get_attribute_types())

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