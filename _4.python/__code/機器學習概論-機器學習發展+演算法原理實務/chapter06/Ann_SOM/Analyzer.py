if __name__ == "__main__":
    import csv

    reader = csv.reader(file(r"/Users/alexander/temp/data1mt10000.csv", "rb"))
    lastPositions = list()
    i = 0
    maxLastPosition = 0
    maxI = 0
    for row in reader:
        # print i
        i += 1
        lastChange = 0
        if i == 1:
            print(len(row))
        for position in range(len(row) - 1):
            if row[position] != row[position + 1]:
                lastChange = position
        lastPositions.append(lastChange)
        if maxLastPosition < lastChange:
            maxLastPosition = lastChange
            maxI = i
    print(maxLastPosition)
    print(maxI)

    w = csv.writer(file(r"/Users/alexander/temp/lastChangePositions.csv", "wb"))
    w.writerow(lastPositions)
