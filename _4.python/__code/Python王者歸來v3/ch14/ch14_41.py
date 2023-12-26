# ch14_41.py
with open('backup.csv', 'w') as file:
    for data in database_data:
        file.write(','.join(data) + '\n')



