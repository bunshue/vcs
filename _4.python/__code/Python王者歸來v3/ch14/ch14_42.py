# ch14_42.py
with open('app.log', 'a') as log_file:
    log_file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - 工作項目 1\n')


