# F1750 練習 31

def pl_word(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

def pl_file(filename):
    with open(filename, 'r') as f:
        return ' '.join([pl_word(word.lower().replace('.', ''))
                         for line in f
                         for word in line.split()])

print(pl_file(r'.\data\text2.txt'))
