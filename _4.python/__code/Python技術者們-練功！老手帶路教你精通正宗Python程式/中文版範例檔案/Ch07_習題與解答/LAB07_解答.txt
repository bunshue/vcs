moby_words = []
with open('moby_01_clean.txt') as infile:
    for word in infile:
        if word.strip():
            moby_words.append(word.strip())
        
word_count = {}
for word in moby_words:
    count = word_count.setdefault(word, 0)
    count += 1
    word_count[word] += 1
    
word_list = list(word_count.items())
word_list.sort(key=lambda x: x[1])

print("Most common words:")
for word in reversed(word_list[-5:]):
    print(word)

print("\nLeast common words:")
for word in word_list[:5]:
    print(word)
