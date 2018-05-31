from src.clinical_study_organizer.study import *
from test.fixtures import *
import os
import pytest


def test_initialize(study, raw_database_cursor):
    study.initialize()

    assert(study.initialized == True)
    assert(raw_database_cursor is not None)


def test_add_patients(study, patients):
    study.initialize()
    study.add_patients(patients)

    # todo add function to return all patients from study