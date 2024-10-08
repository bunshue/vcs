from clockdeco import clock


@clock
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print([fib(n) for n in range(5)])
