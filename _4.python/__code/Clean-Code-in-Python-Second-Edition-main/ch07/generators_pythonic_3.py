"""Clean Code in Python - Chapter 7: Generators, Iterators, and Asynchronous Programming

> Idiomatic Iteration

"""
from itertools import tee
from statistics import median


def produce_values(how_many):
    for i in range(1, how_many + 1):
        yield i


def process_purchases(purchases):
    min_, max_, avg = tee(purchases, 3)
    return min(min_), max(max_), median(avg)


def main():
    data = produce_values(7)
    obtained = process_purchases(data)
    assert obtained == (1, 7, 4)


if __name__ == "__main__":
    main()
