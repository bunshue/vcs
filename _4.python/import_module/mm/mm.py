from random import randint, randrange


# 產生某個區間的整數亂數
def numRand(x, y):
    cout = 1  # 計數器
    while cout <= 10:
        number = randint(x, y)
        print(number, end=" ")
        cout += 1
    print()


# 將產生以append()方法加至List
def numRand2(x, y):
    cout = 1
    result = []  # 存放亂數
    while cout <= 10:
        number = randint(x, y)
        result.append(number)
        cout += 1
    return result


def say_hello():
    print("hello")


# Dummy data
sales_data = {
    "Product A": 100,
    "Product B": 200,
    "Product C": 600,
    "Product D": 400,
    "Product E": 500,
}

inventory_data = {
    "Product A": 150,
    "Product B": 75,
    "Product C": 100,
    "Product D": 125,
    "Product E": 150,
}

product_data = {"A": 10, "B": 40, "C": 30, "D": 20, "E": 50}

sales_year_data = {2018: 5000, 2019: 17500, 2020: 10000, 2021: 7500, 2022: 15000}

inventory_month_data = {
    "Jan": 200,
    "Feb": 300,
    "Mar": 800,
    "Apr": 1300,
    "May": 600,
    "Jun": 900,
    "Jul": 700,
    "Aug": 900,
    "Sep": 1000,
    "Oct": 300,
    "Nov": 450,
    "Dec": 1300,
}


def show():
	print('I am a moudle!')
name = 'mmmm mymodule.py'


