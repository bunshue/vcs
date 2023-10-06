# 2-1-1 用 assert 在開發階段協助除錯

shoes = {'name': '潮鞋', 'price': 149}

def apply_discount(product, discount):
    price = product['price'] * discount
    assert 0 <= price <= product['price']
    return price


print(apply_discount(shoes, 0.75))

print(apply_discount(shoes, -0.5))