import tkinter as tk

# 創建視窗
root = tk.Tk()

# 創建一個標籤(Label)物件，並設定其文字為「陳會安」
label = tk.Label(root, text="陳會安")

# 將標籤(Label)物件放置於視窗中央
label.pack(expand=True, fill="both")

# 啟動視窗主迴圈
root.mainloop()
