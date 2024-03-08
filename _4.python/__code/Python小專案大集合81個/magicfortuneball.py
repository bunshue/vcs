import random, time

def slowSpacePrint(text, interval=0.05):
    """Slowly display text with spaces in between each letter and
    lowercase letter i's."""
    for character in text:
        if character == 'I':
            # I's are displayed in lowercase for style:
            print('i ', end='', flush=True)
        else:
            # All other characters are displayed normally:
            print(character + ' ', end='', flush=True)
        time.sleep(interval)
    print()  # Print two newlines at the end.
    print()


# Prompt for a question:
slowSpacePrint('MAGIC FORTUNE BALL, BY AL SWEiGART')
time.sleep(0.2)
slowSpacePrint('ASK ME YOUR YES/NO QUESTION.')
input('> ')

# Display a brief reply:
replies = [
    'LET ME THINK ON THIS...',
    'AN INTERESTING QUESTION...',
    'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
    'YOU MAY WANT TO SIT DOWN FOR THIS...',
]
slowSpacePrint(random.choice(replies))

# Dramatic pause:
slowSpacePrint('.' * random.randint(4, 12), 0.2)

# Give the answer:
slowSpacePrint('I HAVE AN ANSWER...', 0.2)
time.sleep(1)

answers = [
    '鼠',
    '牛',
    '虎',
    '兔',
    '龍',
    '蛇',
]
slowSpacePrint(random.choice(answers), 0.05)

