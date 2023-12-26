# ch15_35.py
try:
    # 嘗試打開一個不存在的檔案
    with open('non_existent_file.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    # 如果文件不存在, 捕獲異常
    print("The file was not found")
except IOError:
    # 處理 I/O 錯誤, 例如:讀取錯誤
    print("An I/O error occurred")


