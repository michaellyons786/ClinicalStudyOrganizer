
def construct_patients_attributes(patients):
    queries = []

    for patient in patients:
        alias = "\'" + patient.alias + "\', "
        data = patient.data
        data_string = construct_patient_attributes(data)

        query = "INSERT INTO attributes VALUES (" + \
        alias + \
        data_string + \
        ");"

        queries.append(query)

    return queries


def construct_patients_identities(patients):
    queries = []

    for patient in patients:
        query = "INSERT INTO identity VALUES (\'" + patient.alias + "\', \'" + patient.id + "\', \'" + patient.last_name + "\', \'" + patient.first_name + "\')"
        queries.append(query)

    return queries


def construct_patient_attributes(data):
    patient_data = []

    for value in data:
        patient_data.append("\'" + str(value) + "\', ")

    remove_last_comma(patient_data)

    return "".join(patient_data)


def get_initial_tables(attribute_dictionary):

    attribute_string = construct_attribute_table(attribute_dictionary)

    identity_table = "CREATE TABLE identity (" \
                     "alias      VARCHAR REFERENCES alias (alias),\n" \
                     "id         INT UNIQUE PRIMARY KEY,\n" \
                     "last_name         VARCHAR,\n" \
                     "first_name         VARCHAR" \
                     ");"

    attribute_table = "CREATE TABLE attributes (\n" \
                      "alias    VARCHAR PRIMARY KEY UNIQUE,\n" + \
                      attribute_string + \
                      ");"

    return attribute_table, identity_table


def construct_all_attribute_values(attribute_names):
    return "SELECT alias, " + construct_attributes_select(attribute_names) + " FROM attributes;"


def construct_attribute_table(attribute_dictionary):
    attribute_string_list = []

    for attribute_name in (attribute for attribute in attribute_dictionary if
                           attribute != "id" and attribute != "last_name" and attribute != "first_name"):
        attribute_type = attribute_dictionary[attribute_name]
        attribute_string = attribute_name + " " + attribute_type + ",\n"

        attribute_string_list.append(attribute_string)

    remove_last_comma(attribute_string_list)

    return "".join(attribute_string_list)


def construct_attributes_select(attribute_names):
    query = []

    for attribute in attribute_names:
        line = attribute + ", "
        query.append(line)

    remove_last_comma(query)

    return "".join(query)


def remove_last_comma(string_list):
    string_list[len(string_list) - 1] = string_list[len(string_list) - 1].replace(",", "")