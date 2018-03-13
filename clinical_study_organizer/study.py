import random


class Study():
    def __init__(self):
        self.patients = {}

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


class Patient():
    def __init__(self, last_name, first_name, id, data):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.data = data


def get_alias():
    file = open('../data/nounlist.txt')
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


while True:
    print(get_alias())

