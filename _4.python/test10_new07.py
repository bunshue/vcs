print('建一個測試list')

class User:
    user_id: int
    first_name: str
    last_name: str

USERS = [(i, f"first_name_{i}", f"last_name_{i}") for i in range(2_0)]

print(type(USERS))
print(USERS)


def show_price(price: float) -> str:
    return "$ {0:,.2f}".format(price)


print(show_price(1000))
#    '$ 1,000.00'

print(show_price(1_250.75))
#    '$ 1,250.75'







