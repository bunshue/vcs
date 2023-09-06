
card_types = ['黑桃', '紅心', '梅花', '方塊']
card_numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = list()
for card_type in card_types:
    for card_number in card_numbers:
        deck.append((card_type,card_number))
print(deck)



import random
card_types = ['黑桃', '紅心', '梅花', '方塊']
card_numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = list()
for card_type in card_types:
    for card_number in card_numbers:
        deck.append((card_type,card_number))    
random.shuffle(deck)
cards = deck[0:5]
print(cards)



import random
card_types = ['黑桃', '紅心', '梅花', '方塊']
card_numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = list()
for card_type in card_types:
    for card_number in card_numbers:
        deck.append((card_type,card_number))
random.shuffle(deck)
cards = deck[0:5]    
print("你的牌是：")
for i in range(5):
    print("#{}:{}\t{}".format(i, cards[i][0], cards[i][1]))

changed = input("請輸入你想要換的牌（用空白隔開）：")
changed_index = changed.split()
card_top = 5
for i in range(len(changed_index)):
    cards[int(changed_index[i])] = deck[card_top]
    card_top += 1
for i in range(5):
    print("#{}:{}\t{}".format(i, cards[i][0], cards[i][1]))
    
    
import operator
card_types = ['黑桃', '紅心', '梅花', '方塊']
card_numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = list()
for card_type in card_types:
    for card_number in card_numbers:
        deck.append((card_type,card_number))
random.shuffle(deck)
cards = deck[0:5]    
print("你的牌是：")
for i in range(5):
    print("#{}:{}\t{}".format(i, cards[i][0], cards[i][1]))
    
    
changed = input("請輸入你想要換的牌（用空白隔開）：")
changed_index = changed.split()
card_top = 5
for i in range(len(changed_index)):
    cards[int(changed_index[i])] = deck[card_top]
    card_top += 1
cards.sort(key = operator.itemgetter(1))
for i in range(5):
    print("#{}:{}\t{}".format(i, cards[i][0], cards[i][1]))




import random
card_type = ['Heart', 'Spade', 'Diamond', 'Club']
deck = [i for i in range(52)]
random.shuffle(deck)
print("你得到的5張牌是：")
for i in range(5):
    print(card_type[deck[i]//13], end="")
    print("\t", deck[i]%13+1)

