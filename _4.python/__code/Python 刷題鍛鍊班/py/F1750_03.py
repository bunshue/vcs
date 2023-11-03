# F1750 練習 03

def run_timing():
    total_time = 0.0
    number_of_runs = 0
 
    while True:
        run_time = input('輸入跑 10 公里時間: (直接按 Enter 結束) ')
        if run_time == '':
            break
        try:
            run_time_value = float(run_time)
            total_time += run_time_value
            number_of_runs += 1
        except Exception as e:
            print('產生錯誤:', e)
 
    if number_of_runs > 0:
        average_time = (total_time / number_of_runs)
    else:
        average_time = 0.0
 
    print('跑', number_of_runs, '次的平均時間為', average_time, '分鐘')

run_timing()
