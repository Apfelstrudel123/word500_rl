from data_loader import loadData
from game import Game
from colorama import Back, Style
import random

path_len_2 = "./data/words_len_2.csv"
path_len_5 = "./data/words_len_5_cleaned.csv"

NUM_EPOCHS = 10
NUM_GAMES = 10

data = loadData(path_len_5)

for i in range(NUM_GAMES):
    game = Game(data, verbose=True)
    while not game.finished:
        action = random.choice(data)
        valid, n_red, n_yellow, n_green = game.evalWord(action)
        if valid:
            print(action, Back.RED, n_red, Back.YELLOW, n_yellow, Back.GREEN, n_green, Style.RESET_ALL)