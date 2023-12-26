# ch15_34.py
import sqlite3

try:
    # 嘗試連接到資料庫
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # 嘗試執行查詢，可能會引發異常
    cursor.execute('SELECT * FROM non_existent_table')
except sqlite3.Error as e:
    # 捕獲並處理 SQLite 特定的異常
    print(f"Database error: {e}")
except Exception as e:
    # 捕獲並處理其他所有異常
    print(f"Exception occurred: {e}")
finally:
    # 確保資料庫連接被關閉
    conn.close()


