# F1750 練習 48

def word_generator(filename, max_words):
    index = 0
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                if index >= max_words:
                    return
                yield word.replace('.', '')
                index += 1

ten_words = word_generator(r'.\data\text2.txt', 10)

for word in ten_words:
    print(word)
