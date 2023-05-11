dict1={"林小明":85, "曾山水":93, "鄭美麗":67}
dict1["黃明品"] = 71
dict1["陳莉莉"] = 98
listitem = dict1.items()
for name, score in listitem:
    print("%s 的成績為 %d 分" % (name, score))
