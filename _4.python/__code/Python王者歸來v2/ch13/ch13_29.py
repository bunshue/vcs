# ch13_29.py
import keyword

keywordLists = ['as', 'while', 'break', 'sse', 'Python']
for x in keywordLists:
    print(f"{x:>8s} {keyword.iskeyword(x)}")




