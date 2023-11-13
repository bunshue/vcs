# F1750 練習 36

TAX_RATE = {
    0: 0.1,
    10000: 0.2,
    50000: 0.3,
    100000: 0.4,
    500000: 0.5
    }

def find_tax_rage(amount):
    result = 0.0
    for income, rate in TAX_RATE.items():
        if amount >= income:
            result = rate
    return result

def calculate_tax(amount):
    return amount * find_tax_rage(amount)

