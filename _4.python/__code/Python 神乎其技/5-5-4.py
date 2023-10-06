# 5-5-4 LifoQueue - 可用於多執行緒的堆疊 (2)

import threading, queue, time

source = ['吃飯', '睡覺', '寫程式', '散步', '聽音樂', '打牌', '玩電動']
threads_num = 3

q = queue.LifoQueue()
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