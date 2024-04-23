
print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter.filedialog import asksaveasfilename    # 導入文件保存對話框函數
 
def generate_report():
    # 生成報告的函數, 從文本框中獲取報告內容
    report_content = text_report.get("1.0", tk.END)
    # 打開一個對話框讓使用者選擇保存報告的路徑
    file_path = asksaveasfilename(
        defaultextension=".txt",                    # 預設副檔名為.txt
        filetypes=[("Text documents", ".txt")],     # 文件類型過濾
    )
    # 如果使用者選擇了文件路徑, 則將報告內容寫入文件
    if file_path:
        with open(file_path, "w") as file:
            file.write(report_content)

root = tk.Tk()
root.title("報告生成器")                             # 視窗標題
text_report = tk.Text(root)                 # 建立文字區域用於編輯報告內容
text_report.pack()                          # 將文本區域添加到視窗中
# 建一個按鈕，點擊時會呼叫generate_report()函數
button_generate = tk.Button(root, text="生成報告", command=generate_report)
button_generate.pack()                      # 將按鈕添加到視窗中
root.mainloop()

print("------------------------------------------------------------")  # 60個


import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)


save_dir = open_file_dialog()

print(save_dir)

 

window.mainloop()



print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


