# 2-6-2 指派運算式 := (Python 3.8+) (2)

prices = [120, 150, 190, 130, 110, 90, 160]

def discount(price):
    return price * 0.79


new_prices = [new_p for p in prices if (new_p := discount(p)) >= 100]
print(new_prices)