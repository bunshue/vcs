def mogura(r):
    m = ""
    n = ""
    for i in range(8):
        ana = "."
        if i==r:
            ana = "O"
        m = m + " _" + ana + "_ "
        n = n + " [" + str(i) + "] "
    print(m)
    print(n)

print("以參數1呼叫mogura()函數")
mogura(1)
print("")
print("以參數5呼叫mogura()函數")
mogura(5)
