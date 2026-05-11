def sum_to_n(start, stop):
    s = 0
    for i in range(start, stop+1):
        s += i
    print("從n加到n = " + str(s))

m = 5
sum_to_n(1, 5)
sum_to_n(2, m + 2)
