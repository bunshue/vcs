# F1750 練習 13

import operator

def most_repeated_letter(word):
    letters = list(set(word))
    letters_count = []
    for letter in letters:
        letters_count.append((letter, word.count(letter)))
    result = sorted(letters_count, key=operator.itemgetter(1))[-1]
    print(f'{result[0]} 重複了 {result[1]} 次')

most_repeated_letter('independence')
