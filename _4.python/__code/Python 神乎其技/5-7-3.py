# 5-7-3 PriorityQueue - 可用於多執行緒的 heapq

import threading, queue, time

source = ['2-吃飯', '1-睡覺', '3-寫程式', '7-散步', '5-聽音樂', '6-打牌', '4-玩電動']
threads_num = 3

q = queue.PriorityQueue()
for item in source:
    q.put(item)

def worker():
    print('執行緒開始')
    while True:
        item = q.get()
        if item == 'STOP':
            print('執行緒結束')
            break
        print('處理資料:', item)
        time.sleep(0.01)
        q.task_done()


threads = []
for _ in range(threads_num):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

for _ in range(threads_num):
    q.put('STOP')

for t in threads:
    t.join()

print('主程式結束')
