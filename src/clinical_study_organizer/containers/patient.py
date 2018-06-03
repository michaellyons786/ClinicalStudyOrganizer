import random


class Patient:
    def __init__(self, id, last_name, first_name, data, noun_list):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.data = data
        self.alias = get_alias(noun_list)

    def __repr__(self):
        return self.id + " " + self.first_name + " " + self.last_name


def get_unique_second_word(first_word, words):
    second_word = random.choice(words)

    while second_word == first_word:
        second_word = random.choice(words)

    return second_word


def get_alias(noun_list):
    first_word = random.choice(noun_list)
    second_word = get_unique_second_word(first_word, noun_list)

    return first_word + '_' + second_word