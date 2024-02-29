import random, sys

# Set up the constants:
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'


def getBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    while True:  # Keep asking until they enter a valid amount.
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue  # If the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # Player entered a valid bet.


def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Add the numbered cards.
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))  # Add the face and ace cards.
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    # Show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are
    worth 11 or 1 (this function picks the most suitable ace value)."""
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0]  # card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):  # Face cards are worth 10 points.
            value += 10
        else:
            value += int(rank)  # Numbered cards are worth their number.

    # Add the value for the aces:
    value += numberOfAces  # Add 1 per ace.
    for i in range(numberOfAces):
        # If another 10 can be added without busting, do so:
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', '']  # The text to display on each row.

    for i, card in enumerate(cards):
        rows[0] += ' ___  '  # Print the top line of the card.
        if card == BACKSIDE:
            # Print a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front:
            rank, suit = card  # The card is a tuple data structure.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Print each row on the screen:
    for row in rows:
        print(row)

"""
# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
"""


money = 5000

# Let the player enter their bet for this round:
print('Money:', money)
#bet = getBet(money)
bet = 20

# Give the dealer and player two cards from the deck each:
deck = getDeck()
dealerHand = [deck.pop(), deck.pop()]
playerHand = [deck.pop(), deck.pop()]

# Handle player actions:
print('Bet:', bet)

for _ in range(3):
    displayHands(playerHand, dealerHand, False)
    print()

    # Check if the player has bust:
    if getHandValue(playerHand) > 21:
        break

"""
    if move in ('H', 'D'):
        # Hit/doubling down takes another card.
        newCard = deck.pop()
        rank, suit = newCard
        print('You drew a {} of {}.'.format(rank, suit))
        playerHand.append(newCard)

        if getHandValue(playerHand) > 21:
            # The player has busted:
            continue
"""

# Show the final hands:
displayHands(playerHand, dealerHand, True)

playerValue = getHandValue(playerHand)
dealerValue = getHandValue(dealerHand)
# Handle whether the player won, lost, or tied:
if dealerValue > 21:
    print('Dealer busts! You win ${}!'.format(bet))
    money += bet
elif (playerValue > 21) or (playerValue < dealerValue):
    print('You lost!')
    money -= bet
elif playerValue > dealerValue:
    print('You won ${}!'.format(bet))
    money += bet
elif playerValue == dealerValue:
    print('It\'s a tie, the bet is returned to you.')



print('\n\n')


