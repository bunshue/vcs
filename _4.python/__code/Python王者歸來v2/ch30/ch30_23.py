# ch30_23.py
import threading, logging
logging.basicConfig(level=logging.DEBUG)
datalock = threading.Lock()     # Lock物件
datalock.acquire()              # 進入鎖定
logging.debug('Enter locked mode')
datalock.acquire()              # 進入死鎖程式當機
logging.debug('Trying to locked again')
datalock.release()
datalock.release()

