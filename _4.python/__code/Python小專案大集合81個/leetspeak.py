import random

def englishToLeetspeak(message):
    """Convert the English string in message and return leetspeak."""
    # Make sure all the keys in `charMapping` are lowercase.
    charMapping = {
    'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
    'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
    'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
    'v': ['\\/']}
    leetspeak = ''
    for char in message:
        print(char.lower())
        if char.lower() in charMapping and random.random() <= 0.3:
            possibleLeetReplacements = charMapping[char.lower()]
            print("aaaaa :", possibleLeetReplacements)
            leetReplacement = random.choice(possibleLeetReplacements)
            print("bbbbb :", leetReplacement)
            leetspeak = leetspeak + leetReplacement
        else:
            leetspeak = leetspeak + char
    return leetspeak

print('駭客語')
english = "AAAAAAAAAA"
print()
leetspeak = englishToLeetspeak(english)
print(leetspeak)


