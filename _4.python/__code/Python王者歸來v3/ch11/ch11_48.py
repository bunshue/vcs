# ch11_48.py
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()    # 獲取函數開始執行的時間
        result = func(*args, **kwargs)      # 調用原始函數
        end_time = time.perf_counter()      # 獲取函數結束執行的時間
        duration = end_time - start_time    # 計算函數執行時間
        print(f'{func.__name__} 執行需 : {duration:.7f} 秒')
        return result
    return wrapper

@timing_decorator
def slow_function(duration):
    time.sleep(duration)                    # 使函數暫停指定的秒數

# 調用裝飾器函數
slow_function(3)            # 輸出 slow_function 執行需 : 3.000xxxx 秒


