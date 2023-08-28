def is_prime(x):
    ret = True
    for i in range(2, x):
        if x % i == 0:
            ret = False
            break
    return ret

def main():
    print("以下是100~200之間的所有質數列表：")
    for n in range(100,201):
        if is_prime(n):
            print("{} ".format(n), end="")

if __name__ == "__main__":
    main()