class PlayerGuess:
    
    # def __init__(self):
    #     self._player_guess = ""

    def execute(self, secret_word):
        self.player_guess = ""

    def make_guess(self):
        self.player_guess = ""
        while len(self.player_guess) != 1:
            self.player_guess = input("Guess a letter [a-z]: ")
            if self.player_guess.isalpha() == False:
                print("Your guess contains characters that are not letters. Guess again.")
                continue
            if len(self.player_guess) != 1:
                print("Your guess contains more than one letter. Guess again.")
                continue
            self.player_guess = self.player_guess.lower()

    def get_guess(self):
        return self.player_guess