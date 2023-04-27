filename = 'C:/______test_files2/info.csv'

with open(filename, 'rt') as fp:
    data = fp.readlines()
print(data)


import pprint as pp
import csv
data = list()
with open(filename, 'rt') as fp:
    rows = csv.DictReader(fp)
    print(type(rows))
    for row in rows:
        data.append(dict(row))
pp.pprint(data)


import pprint as pp
import csv
with open(filename, 'rt') as fp:
    rows = csv.DictReader(fp)
    data = [dict(row) for row in rows]
pp.pprint(data)


import pprint as pp
data = list()
with open(filename, 'rt') as fp:
    columns = fp.readline().split(",")
    for item in fp.readlines():
        temp = dict()
        for i, field in enumerate(item.split(",")):
            temp[columns[i].strip()] = field.strip()
        data.append(temp)
pp.pprint(data)
