import csv

csvFile = open("test.csv", 'w+', newline='')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('column1', 'column2', 'column3'))
    writer.writerow((1,2,3))
    writer.writerow((4,5,6))
    writer.writerow((7,8,9))
    writer.writerow(('a','b','c'))
    writer.writerow(('lion','mouse','cat','dog'))
finally:
    csvFile.close()
