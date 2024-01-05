import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("My Application")
        self.create_menu()
        self.pack()

    def create_menu(self):
        # 建立主功能表
        menubar = tk.Menu(self.master)

        # 建立檔案主功能
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="開啟檔案", command=self.open_file)
        file_menu.add_command(label="儲存檔案", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="結束", command=self.master.quit)
        menubar.add_cascade(label="檔案", menu=file_menu)

        # 建立編輯主功能
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="複製", command=self.copy)
        edit_menu.add_command(label="剪下", command=self.cut)
        edit_menu.add_command(label="貼上", command=self.paste)
        menubar.add_cascade(label="編輯", menu=edit_menu)

        # 建立執行主功能
        run_menu = tk.Menu(menubar, tearoff=0)
        run_menu.add_command(label="執行程式", command=self.run)
        menubar.add_cascade(label="執行", menu=run_menu)

        # 建立線上說明主功能
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="使用說明", command=self.show_help)
        menubar.add_cascade(label="線上說明", menu=help_menu)

        # 設定主功能表
        self.master.config(menu=menubar)

    def open_file(self):
        print("開啟檔案")

    def save_file(self):
        print("儲存檔案")

    def copy(self):
        print("複製")

    def cut(self):
        print("剪下")

    def paste(self):
        print("貼上")

    def run(self):
        print("執行程式")

    def show_help(self):
        print("使用說明")

# 建立主視窗
root = tk.Tk()

# 建立應用程式
app = Application(master=root)

# 執行主迴圈
app.mainloop()
