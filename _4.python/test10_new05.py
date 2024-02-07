import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

# The card suit characters:
HEARTS   = chr(9829)  # Character 9829 is '♥'
DIAMONDS = chr(9830)  # Character 9830 is '♦'
SPADES   = chr(9824)  # Character 9824 is '♠'
CLUBS    = chr(9827)  # Character 9827 is '♣'
# A list of chr() codes is at https://inventwithpython.com/chr


for _ in range(20):
    suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])
    print(suit, end = " ")
print()


def getRandomCard():
    rank = random.choice(list('23456789JQKA') + ['10'])
    suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])
    return (rank, suit)

cc = getRandomCard()
print(cc)



print("------------------------------------------------------------")  # 60個

#宣告迷宮陣列
MAZE= [[1,1,1,1,1,1,1,1,1,1,1,1], \
       [1,0,0,0,1,1,1,1,1,1,1,1], \
       [1,1,1,0,1,1,0,0,0,0,1,1], \
       [1,1,1,0,1,1,0,1,1,0,1,1], \
       [1,1,1,0,0,0,0,1,1,0,1,1], \
       [1,1,1,0,1,1,0,1,1,0,1,1], \
       [1,1,1,0,1,1,0,1,1,0,1,1], \
       [1,1,1,1,1,1,0,1,1,0,1,1], \
       [1,1,0,0,0,0,0,0,1,0,0,1], \
       [1,1,1,1,1,1,1,1,1,1,1,1]]

print('[迷宮的路徑(0的部分)]')
for i in range(10):
    for j in range(12):
        print(MAZE[i][j],end='')
    print()

print('------------------------------------------------------------')	#60個



move = "   aaa     , bbb   , ccc   ,   ddd    "
n1, n2, n3, n4 = move.split(",")

print(n1.strip(), end='|\n')
print(n2.strip(), end='|\n')
print(n3.strip(), end='|\n')
print(n4.strip(), end='|\n')

print('------------------------------------------------------------')	#60個

print('assert的語法')

# Set up the constants:
SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR', 'MRS. FEATHERTOSS', 'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE', 'JAR OF PICKLES', 'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY', 'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300  # 300 seconds (5 minutes) to solve the game.

# First letters and longest length of places are needed for menu display:
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

# Basic sanity checks of the constants:
assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
# First letters must be unique:
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

