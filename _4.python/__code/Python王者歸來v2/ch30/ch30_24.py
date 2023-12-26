# ch30_24.py
import threading, logging
logging.basicConfig(level=logging.DEBUG)
datalock = threading.RLock()    # RLock物件
datalock.acquire()              # 進入鎖定
logging.debug('Enter locked mode')
datalock.acquire()              # 不會進入死結
logging.debug('Trying to locked again')
datalock.release()
datalock.release()

