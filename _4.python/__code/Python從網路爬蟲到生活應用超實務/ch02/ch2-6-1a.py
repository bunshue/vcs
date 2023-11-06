import csv

csvfile = "pl2.csv"
lst1 = [["Python","Cuido van Rossum",1991,".py"],
        ["Java","James Gosling",1995,".java"],
        ["C++","Bjarne Stroustrup",1983,".cpp"]]
with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["程式語言","開發者","上市年","副檔名"])
    for row in lst1:
        writer.writerow(row)

