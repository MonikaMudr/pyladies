from random import randrange
from util import tah

def tah_pocitace(pole, symbol):
    delka = len(pole)

    while True:
        try:
            index = randrange(0, delka)
            return tah(pole, index, symbol)
        except ValueError:
            pass