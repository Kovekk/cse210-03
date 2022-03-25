class Director:
    """satisfy python."""

    def __init__(self):
        self._letters_known = []

    def start_game(self, jumper, magic_word, player_guess):
        magic_word.print_self(self._letters_known)
        jumper.print_self()
        while True:
            self._do_inputs(player_guess)
            self._do_updates(magic_word, player_guess, jumper)
            self._do_outputs(magic_word, jumper)
            if jumper.is_dead() == True or magic_word.is_guessed(self._letters_known) == True:
                break
        print(f"Thanks for playing! The word was {magic_word.get_word()}")

    def _do_inputs(self, player_guess):
        player_guess.make_guess()

    def _do_updates(self, magic_word, player_guess, jumper):
        letter_guessed = player_guess.get_guess()
        if letter_guessed in magic_word.get_word():
            self._letters_known.append(letter_guessed)
        else: jumper.lose_life()

    def _do_outputs(self, magic_word, jumper):
        print()
        magic_word.print_self(self._letters_known)
        print()
        jumper.print_self()
        print()

