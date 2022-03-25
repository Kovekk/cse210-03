import random

class MagicWord:
    """satisfy python."""

    def __init__(self, word_list):
        self._word_list = word_list
        self._word = ""
        self.randomize_word()

    def randomize_word(self):
        self._word = self._word_list[random.randint(0, len(self._word_list) - 1)]

    def print_self(self, letters_known):
        output = ""
        for letter in self._word:
            if letter in letters_known:
                output = output + letter + " "
            else: output = output + "_ "
        print(output)

    def get_word(self):
        return self._word

    def is_guessed(self, letters_known):
        for letter in self._word:
            if letter not in letters_known:
                return False
        return True
