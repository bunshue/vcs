from random import choice

pokerkind = ["♠", "♥", "♦", "♣"]
pokerpoint = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def poker():
    return choice(pokerkind) + choice(pokerpoint)
