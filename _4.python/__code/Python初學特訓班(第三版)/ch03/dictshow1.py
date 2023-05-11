dict1={"林小明":85, "曾山水":93, "鄭美麗":67}
dict1["黃明品"] = 71
dict1["陳莉莉"] = 98
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("%s 的成績為 %d 分" % (listkey[i], listvalue[i]))
