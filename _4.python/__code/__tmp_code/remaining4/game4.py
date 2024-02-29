import random

def dragon_tiger():
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    dragon_card = random.choice(cards)
    tiger_card = random.choice(cards)
    print(f"Dragon: {dragon_card}")
    print(f"Tiger: {tiger_card}")
    if cards.index(dragon_card) > cards.index(tiger_card):
        print("Dragon wins!")
    elif cards.index(dragon_card) < cards.index(tiger_card):
        print("Tiger wins!")
    else:
        print("Tie!")

if __name__ == '__main__':
dragon_tiger()