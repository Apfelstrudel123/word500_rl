from data_loader import loadData
from game import Game
from colorama import Back, Style

path_len_2 = "./data/words_len_2.csv"
path_len_5 = "./data/words_len_5_cleaned.csv"

data = loadData(path_len_5)

game = Game(data, verbose=False)

while not game.finished:
    prompt = "Enter word (" + str(game.getRemainingAttempts()) + " attempts remaining): "
    inp = input(prompt)
    valid, n_red, n_yellow, n_green = game.evalWord(inp)
    if valid:
        print(inp, Back.RED, n_red, Back.YELLOW, n_yellow, Back.GREEN, n_green, Style.RESET_ALL)