import random
import csv


class Study:
    def __init__(self, attribute_names):
        self.patients = {}
        self.attribute_names = attribute_names

    def add_patients(self, patients):
        for patient in patients:
            self.add_patient(patient)

    def add_patient(self, patient):
        alias = self._ensure_no_duplicate_alias(get_alias())
        self.patients[alias] = patient

    def _ensure_no_duplicate_alias(self, alias):
        while self.patients.get(alias, 'empty') != 'empty':
            alias = get_alias()
        return alias


def get_alias():
    file = open('../data/nounlist.txt')  # todo make dynamic
    words = []
    for line in file:
        words.append(line)

    first = random.choice(words).replace('\n', '')
    second = ensure_no_duplicate_noun(first, first, words)

    return first + '_' + second


def ensure_no_duplicate_noun(first, second, words):
    while second == first:
        second = random.choice(words).replace('\n', '')
    return second


def read_patient_list(file_name):
    csv_data = []

    with open(file_name) as csvfile:
        read_csv = csv.reader(csvfile)
        for row in read_csv:
            csv_data.append(row)

    return csv_data

if __name__ == "__main__":
    raw_list = read_patient_list('../data/sample_patient_list.csv')
    study = Study(raw_list[0])
    raw_list.pop(0)
    study.add_patients(raw_list)
