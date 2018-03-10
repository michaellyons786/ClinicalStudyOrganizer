import csv
import random


def open_CSV(file):
    csv_data = []

    with open(file) as csvfile:
        read_csv = csv.reader(csvfile)
        for row in read_csv:
            csv_data.append(row)

    return csv_data


def create_name(first_name, last_name):
    return random.choice(last_name)[0] + ', ' + random.choice(first_name)[0] + ', '


def get_id(id_list):
    id = random.choice(range(1000000))

    while id in id_list:
        id = random.choice(range(1000000))

        id_list.add(id)

    return id

n = 500
attribute_names = "last_name, first_name, id"
first_names = open_CSV('CSV_Database_of_First_Names.csv')
last_names = open_CSV('CSV_Database_of_Last_Names.csv')

file = open("sample_patient_list.csv", "w")

id_list = []

file.write(attribute_names + '\n')

for _ in range(n):
    id = str(get_id(id_list))
    file.write(create_name(first_names, last_names) + id + '\n')

file.close()





