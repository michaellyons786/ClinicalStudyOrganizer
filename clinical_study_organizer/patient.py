import random


class Patient:
    def __init__(self, last_name, first_name, id, data):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.data = data
        self.alias = self.get_alias()

    def get_alias(self):
        file = open('../data/nounlist.txt')  # todo make dynamic
        words = []
        for line in file:
            words.append(line)

        first_word = random.choice(words).replace('\n', '')
        second_word = self._ensure_no_duplicate_noun(first_word, words)

        return first_word + '_' + second_word

    def _ensure_no_duplicate_noun(self, first_word, words):
        second_word = random.choice(words).replace('\n', '')

        while second_word == first_word:
            second_word = random.choice(words).replace('\n', '')
        return second_word