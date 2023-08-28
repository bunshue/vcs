import sys
if len(sys.argv)>1:
    n = int(sys.argv[1])
else:
    print("You need to specify a valid number!")
    exit(1)

lst = [i*2+1 for i in range(n)]
for i in lst:
    print(" "*((lst[-1]-i)//2), end="")
    for k in range(i):
        print("*", end="")
    print()
