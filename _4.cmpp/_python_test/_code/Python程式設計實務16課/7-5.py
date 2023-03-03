# 7-5.py (Python 3 version)

for i in range(2,7,4):
    for j in range(1,10):
        print("{}x{}={:>2}    ".format(i, j, i*j), end="")
        print("{}x{}={:>2}    ".format(i+1, j, (i+1)*j), end="")
        print("{}x{}={:>2}    ".format(i+2, j, (i+2)*j), end="")
        print("{}x{}={:>2}    ".format(i+3, j, (i+3)*j))
    print()
