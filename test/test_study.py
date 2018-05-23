from clinical_study_organizer.study import read_patient_list, construct_patient_list, Study


def test_read_patient_list():
    test_list = "../database/sample_patient_list.csv"
    attributes, data = read_patient_list(test_list)

    assert("Kolbe" in data[0])
    assert("Maycock" in data[19])
    assert("id;INT" in attributes[0])
    assert("eye_color;VARCHAR" in attributes[5])

def test_construct_patient_list():
    test_list = "../database/sample_patient_list.csv"
    attributes, data = read_patient_list(test_list)

    patients = construct_patient_list(data)

    assert (patients[0].first_name == "Cathi")
    assert (patients[19].first_name == "Oretha")
    assert (patients[0].id == '7698')
    assert (patients[19].id == '5782')

def test_study():
    test_list = "../database/sample_patient_list.csv"
    attributes, data = read_patient_list(test_list)

    study = Study(attributes)
