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
    return random.choice(last_name)[0] + ', ' + random.choice(first_name)[0]


def get_id(id_list):
    id = random.choice(range(10000))

    while id in id_list:
        id = random.choice(range(10000))

        id_list.add(id)

    return id


def get_age():
    return str(random.randint(18, 40))


def get_height():
    return str(random.randint(145, 200))


def get_eye_color():
    colors = ['blue', 'green', 'gray', 'brown']
    return random.choice(colors)


n = 20
attribute_names = "id;INT, last_name;VARCHAR, first_name;VARCHAR, age;INT, height;INT, eye_color;VARCHAR"
first_names = open_CSV('CSV_Database_of_First_Names.csv')
last_names = open_CSV('CSV_Database_of_Last_Names.csv')

file = open("sample_patient_list.csv", "w")

id_list = []

file.write(attribute_names + '\n')

for _ in range(n):
    id = str(get_id(id_list))
    name = create_name(first_names, last_names)
    age = get_age()
    height = get_height()
    eye_color = get_eye_color()

    file.write(id + ", " + name + ", " + age + ", " + height + ", " + eye_color + '\n')

file.close()





