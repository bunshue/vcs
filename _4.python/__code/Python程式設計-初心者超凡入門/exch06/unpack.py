info = [['C程式設計','朱大峰','480'],
        ['Python程式設計','吳志明','500'],
        ['Java程式設計','許伯如','540']]

for(book, author,price) in info:
    print('%10s %3s'%(book,author),' 書籍訂價:',price)
