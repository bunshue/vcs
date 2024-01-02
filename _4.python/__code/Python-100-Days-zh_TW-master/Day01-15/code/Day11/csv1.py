import csv

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/animals.csv'

try:
    with open(filename, encoding = 'utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print('无法打开文件:', filename)
else:
    for item in data:
        print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))
