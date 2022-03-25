from game.director import Director
from game.jumper import Jumper
from game.magic_word import MagicWord
from game.player_guess import PlayerGuess
import constants

def main():
    word_list = constants.WORD_LIST
    jumper = Jumper()
    magic_word = MagicWord(word_list)
    player_guess = PlayerGuess()
    director = Director()

    director.start_game(jumper, magic_word, player_guess)


if __name__ == "__main__":
    main()