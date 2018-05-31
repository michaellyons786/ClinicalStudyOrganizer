from src.clinical_study_organizer.study import *
from test.fixtures import *
import os
import pytest


def test_initialize(study, database_cursor):
    study.initialize()

    assert(study.initialized == True)
    assert(database_cursor is not None)


def test_add_patients(study, patients):
    study.initialize()
    study.add_patients(patients)

    # todo add function to return all patients from study


def test_study(study):
    query_result = study.get_all_attribute_values(["age", "eye_color"])

    aliases = study.get_all_aliases()
    patient1 = aliases[0][0] # todo fix query result
    patient2 = aliases[len(aliases) - 1][0]
    patient1_attributes = query_result.get_attributes(patient1)
    patient2_attributes = query_result.get_attributes(patient2)

    patient1_identity = study.get_identity(patient1)
    patient2_identity = study.get_identity(patient2)

    patient1_indirect_attributes = study.get_identity_attributes(patient1_identity[0][1])
    patient2_indirect_attributes = study.get_identity_attributes(patient2_identity[0][1])

    assert(query_result.attributes_names[0] == "age")
    assert(patient1_attributes[0] == patient1_indirect_attributes[0][1])
    assert(patient1_attributes[1] == patient1_indirect_attributes[0][3])
    assert(patient2_attributes[0] == patient2_indirect_attributes[0][1])
    assert(patient2_attributes[1] == patient2_indirect_attributes[0][3])

    study.delete_tables()