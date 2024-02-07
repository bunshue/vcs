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





print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

