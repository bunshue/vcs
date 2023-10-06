# 5-6-3 multiprocessing.Queue - 給多核運算用的佇列

import multiprocessing, time


def worker(queue):
    print('process 開始')
    while True:
        item = queue.get()
        if item == 'STOP':
            print('process 結束')
            break
        print('處理資料:', item)
        time.sleep(0.01)


if __name__ == '__main__':
    
    source = ['吃飯', '睡覺', '寫程式', '散步', '聽音樂', '打牌', '玩電動']
    process_num = 3
    
    q = multiprocessing.Queue()
    for item in source:
        q.put(item)
    
    processes = []
    for _ in range(process_num):
        p = multiprocessing.Process(target=worker, args=(q,))
        p.start()
        processes.append(p)
    
    for _ in range(process_num):
        q.put('STOP')
    
    for p in processes:
        p.join()
    
    print('主程式結束')