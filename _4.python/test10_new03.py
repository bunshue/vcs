import os

target = 'https://tw.appledaily.com/new/realtime/{}'

for page in range(1, 11):
    url = target.format(page)
    print(url)

'''
filename = 'C:/_git/vcs/_1.data/______test_files2/news_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.json';
with open(filename, "w", encoding = 'utf-8') as fp:
    print(filename + " is dumping...")
    json.dump(titles, fp)
'''

base_dir = os.path.dirname(os.path.abspath(__file__))

print(base_dir)

