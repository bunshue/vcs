#字符串轉 md5 工具

import tkinter as tk
import hashlib
import time

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #設置窗口
    def set_init_window(self):
        self.init_window_name.title("文本處理工具_v1.2")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160為窗口大小，+10 +10 定義窗口彈出時的默認展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色見：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虛化，值越小虛化程度越高
        #標簽
        self.init_data_label = tk.Label(self.init_window_name, text="待處理數據")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = tk.Label(self.init_window_name, text="輸出結果")
        self.result_data_label.grid(row=0, column=12)

        #文本框
        self.init_data_Text = tk.Text(self.init_window_name, width=67, height=35)  #原始數據錄入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = tk.Text(self.init_window_name, width=70, height=49)  #處理結果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)

        #按鈕
        self.str_trans_to_md5_button = tk.Button(self.init_window_name, text = "字符串轉MD5", bg = "lightblue", width = 10, command = self.str_trans_to_md5)  # 調用內部方法  加()為直接調用
        self.str_trans_to_md5_button.grid(row=1, column=11)


    #功能函數
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0, tk.END).strip().replace("\n","").encode()
        #print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #輸出到界面
                self.result_data_Text.delete(1.0, tk.END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0, tk.END)
                self.result_data_Text.insert(1.0,"字符串轉MD5失敗")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")


    #獲取當前時間
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志動態打印
    def write_log_to_Text(self,logmsg):
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #換行
        print(logmsg_in)
        
window = tk.Tk()              #實例化出一個父窗口
ZMJ_PORTAL = MY_GUI(window)
# 設置根窗口默認屬性
ZMJ_PORTAL.set_init_window()

window.mainloop()

