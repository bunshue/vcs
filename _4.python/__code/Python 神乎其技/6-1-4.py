# 6-1-4 走訪 dict 鍵與值

emails = {
    'Bob': 'bob@office.com',
    'Alice': 'aloce@office.com',
    }

for name, email in emails.items():
    print(f'{name} -> {email}')