tupleBookId=("A001", "A002", "A003")
dictBook={"A001":["木偶奇遇記",199], 
          "A002":["三隻小豬",120],"A003":["白雪公主",99]}
print("書號\t書名\t單價")
print("========================")

for key in list(tupleBookId):
    print(key, end="\t")
    for col in dictBook[key]:
        print(col, end="\t")
    print()
        