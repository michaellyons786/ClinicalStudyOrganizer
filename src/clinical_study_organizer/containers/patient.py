import random


class Patient:
    def __init__(self, id, last_name, first_name, data, noun_list):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.data = data
        self.alias = self.get_alias(noun_list)

    def get_alias(self, noun_list):
        file = open(noun_list)  # todo make dynamic
        words = []
        for line in file:
            words.append(line)

        first_word = random.choice(words).replace('\n', '')
        second_word = ensure_no_duplicate_noun(first_word, words)

        return first_word + '_' + second_word

    def __repr__(self):
        return self.id + " " + self.first_name + " " + self.last_name


def ensure_no_duplicate_noun(first_word, words):
    second_word = random.choice(words).replace('\n', '')

    while second_word == first_word:
        second_word = random.choice(words).replace('\n', '')
    return second_word