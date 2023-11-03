# F1750 練習 34

def word_filter(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    with open(filename, 'r') as f:
        words = ([word.replace('.', '')
                  for line in f
                      for word in line.split()
                      if len(set(word) & vowels) >= 3])
    return words

print(word_filter(r'.\data\text2.txt'))
