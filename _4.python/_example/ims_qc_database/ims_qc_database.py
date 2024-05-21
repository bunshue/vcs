#同一個資料庫內 可以放多個table table名稱不同即可


"""
把原始資料.csv檔放在某個資料夾內

這個轉換程式去那個資料夾內撈.csv檔案

每撈一個檔案，分析裡面的資料，就匯出至excel檔，

匯出至excel檔時，由csv資料找到年月日與各站別，決定輸出檔案之檔名

要先檢查檔案是否存在，若不存在，則要寫檔頭，否則直接輸出資料至excel檔即可。

匯出資料完畢後，將此.csv檔移到別的資料夾


"""


print('------------------------------------------------------------')	#60個
print('準備工作')

import os
import sys
import csv
import time
import openpyxl
import tkinter as tk
import tkinter as tk
from tkinter.filedialog import askopenfile #tk之openFileDialog
from tkinter.filedialog import asksaveasfile #tk之saveFileDialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

flag_debug_mode = True

# 建立csv二維串列資料
all_data = [
]

list_stage402 = list()
list_stage403 = list()
list_stage404 = list()
list_stage405 = list()
list_stage406 = list()
list_stage407 = list()
list_stage408 = list()
list_stage409 = list()

choice = []

stage_no = [
'402除菌區', '403包裝區', '404組裝區', '405燒機測試區',
'406電信測試區', '407原料除菌區', '408清洗區', '409無塵室'
]

list_room_list = [
'list_stage402', 'list_stage402', 'list_stage402', 'list_stage402',
'list_stage402', 'list_stage402', 'list_stage402', 'list_stage402'
]

stage = -1
tablename = ''

dummy_data = 'abcd'
count = 0

print('------------------------------------------------------------')	#60個

#公用副程式

#清除記憶體內的資料
def clear_all_data():
    global all_data
    all_data = [
    ]

    
print('------------------------------------------------------------')	#60個

def process_csv_file1(filename, source):
    global stage
    global tablename
    
    print("aaa :", filename)
    filename = filename.replace(source+"\\", "")
    print("bbb :", filename)

    print("ccc :", filename)

    #year_month_day_data = filename
   
    if filename.startswith('402除菌區') == True:
        print('402除菌區')
        stage = 402
        tablename = 'Room402'
    elif filename.startswith('403包裝區') == True:
        print('403包裝區')
        stage = 403
        tablename = 'Room403'
    elif filename.startswith('404組裝區') == True:
        print('404組裝區')
        stage = 404
        tablename = 'Room404'
    elif filename.startswith('405燒機測試區') == True:
        print('405燒機測試區')
        stage = 405
        tablename = 'Room405'
    elif filename.startswith('406電信測試區') == True:
        print('406電信測試區')
        stage = 406
        tablename = 'Room406'
    elif filename.startswith('407原料除菌區') == True:
        print('407原料除菌區')
        stage = 407
        tablename = 'Room407'
    elif filename.startswith('408清洗區') == True:
        print('408清洗區')
        stage = 408
        tablename = 'Room408'
    elif filename.startswith('409無塵室') == True:
        print('409無塵室')
        stage = 409
        tablename = 'Room409'
    else:
        print('第XXXXXXXXX站')
        stage = 0
    if stage == 0:
        print('不合法的csv檔 : ', filename, ',\t跳過')

def save_data_in_list(datas):
    #print(type(datas))
    data_length = len(datas)
    if stage == 1:
        #print('第1站')
        length = len(list_stage01)
        if length == 0:
            list_stage01.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage01.append(datas[i])
    else:
        print('第XXXXXXXXX站')

def save_data_in_list2(datas):
    #print(type(datas))
    data_length = len(datas)
    if stage == 402:
        print('第402站')
        length = len(list_stage402)
        if length == 0:
            list_stage402.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage402.append(datas[i])
    elif stage == 8:
        #print('第8站')
        length = len(list_stage08)
        if length == 0:
            list_stage08.append(datas[0])   #print('加入檔頭')
        for i in range(1, data_length):
            list_stage08.append(datas[i])
    else:
        print('第XXXXXXXXX站')

def process_csv_file2(filename):
    global stage
    global tablename

    #with open(filename, newline = '') as csvfile:
    with open(filename, encoding = 'big5') as csvfile:
        rows = csv.reader(csvfile)  # 讀取 csv 檔案內容
        datas = list(rows)    #將資料轉成list

    length = len(datas)
    #print('len = ', length)

    save_data_in_list(datas)

    #print(datas)
    data_column = len(datas[0])
    #print('data_column = ', data_column)

    for row in datas:
        for i in range(0, len(row)):
            row[i] = row[i].strip()

    '''
    cnt = 0
    for row in datas:
        print(row)
        print(type(row))
        #print(len(row))
        cnt += 1
        if cnt == 3:
            break
    '''

def process_csv_file3(filename):
    global stage
    global tablename

    print("process_csv_file3")
    print(filename)
    print(tablename)

    #with open(filename, newline = '') as csvfile:
    with open(filename, encoding = 'utf_16_le') as csvfile:
        rows = csv.reader(csvfile, delimiter="\t")  # 讀取 csv 檔案內容
        datas = list(rows)    #將資料轉成list

    length = len(datas)
    print('len = ', length)

    save_data_in_list2(datas)

    print(datas)
    data_column = len(datas[0])
    print('data_column = ', data_column)

    for row in datas:
        for i in range(0, len(row)):
            row[i] = row[i].strip()

    '''
    cnt = 0
    for row in datas:
        print(row)
        print(type(row))
        #print(len(row))
        cnt += 1
        if cnt == 3:
            break
    '''

def precheck_csv_data():
    print('預先檢查這些csv檔案是否皆可用')
    
    #1. 無舊資料
    #2. 有舊資料 要考慮序號是否
    #3. 第一站資料必定要先存在
    
    import os, time, glob, sys, shutil

    source_dir = 'QC/csv'
    target_dir = 'QC/csv_old'

    if flag_debug_mode == True:
        source_dir = 'QC_debug/csv'
        target_dir = 'QC_debug/csv_old'

    #準備輸出資料夾 若不存在, 則建立
    if not os.path.exists(target_dir):
            os.mkdir(target_dir)
            #os.makedirs(target_dir, exist_ok = True)

    #尋找檔案
    import glob
    print('111尋找目前目錄下之 *.csv')
    files = glob.glob(source_dir + "/*.csv") 
    for filename in files:
        print(filename)
        stage = 0
        tablename = 'table00'
        #process_csv_file1(filename)
        if stage != 0:
            print('繼續')
            #process_csv_file2(filename)
            #若能正確處理完畢, 再搬到old資料夾
            #shutil.move(filename, target_dir)

    #message = "匯入生產資料 完成"
    #print(message)
    #text1.insert('end', message)
    
def precheck_data_base():
    print('匯入資料庫時要預先檢查這個新的資料庫資料是否皆可用')
    
def import_csv_data():
    global stage
    global tablename

    import os, time, glob, sys, shutil

    source_dir = 'QC/csv'
    target_dir = 'QC/csv_old'

    if flag_debug_mode == True:
        source_dir = 'QC_debug/csv'
        target_dir = 'QC_debug/csv_old'

    #準備輸出資料夾 若不存在, 則建立
    if not os.path.exists(target_dir):
            os.mkdir(target_dir)
            #os.makedirs(target_dir, exist_ok = True)

    #尋找檔案
    import glob
    print('222尋找目前目錄下之 *.csv')
    print((source_dir + "/*.csv"))
    files = glob.glob(source_dir + "/*.csv") 
    for filename in files:
        print(filename)
        stage = 0
        tablename = 'table00'
        process_csv_file1(filename, source_dir)
        if stage != 0:
            print('繼續')
            process_csv_file3(filename)
            #若能正確處理完畢, 再搬到old資料夾
            #shutil.move(filename, target_dir)

    message = "匯入生產資料 完成"
    print(message)
    text1.insert('end', message)

def merge_stage_data0(list_stage):
    
    length = len(list_stage)

    if length >= 0:
        #print('list_stage 資料長度 : ', length)
        data_column = len(list_stage[0])
        #print('data_column = ', data_column)

        #檔頭
        columns = list(list_stage[0])    #將資料轉成list
        for data in columns:
            all_data[0].append(data)

        #資料內容
        for i in range(1, length):
            if len(list_stage[i]) <= 0:
                continue
            
            columns = list(list_stage[i])    #將資料轉成list

            sn_new = columns[1]

            all_data_length = len(all_data)
            for index in range(1, all_data_length):
                #print(all_data[index][1])
                if all_data[index][1] == sn_new:
                    break;

            for data in columns:
                all_data[index].append(data)

        #缺資料的要補滿
        all_data_columns_length = len(all_data[0])
        #print('資料總寬度 : ', all_data_columns_length)
        #print(all_data_columns_length)

        all_data_length = len(all_data)

        for i in range(1, all_data_length):
            #print('i = ', i, 'len = ', len(all_data[i]))
            if len(all_data[i]) < all_data_columns_length:
                for j in range(0, all_data_columns_length - len(all_data[i])):
                    all_data[i].append('')

    
def merge_stage_data():
    print('merge_stage_data')

    #print('第1站')
    length = len(list_stage402)
    print('list_stage402 資料長度 : ', length)
    if length >= 0:
        for i in range(0, length):
            all_data.append(list_stage402[i])
            
    length = len(all_data)
    print('aaaa = all_data 資料長度 : ', length)
   

def show_info():
    print('show_info')
    length = len(all_data)
    print('資料長度 : ', length)
    print('目前選取的內容 : ')
    str = "選擇："
    for i in range(0, len(choice)):
        if(choice[i].get() == 1):
            str = str + stage_no[i] + " "
    print(str)


    length = len(list_stage01)
    print('第1站 資料長度: ', length)

def show_list_stage():
    print('第1站')
    print(list_stage01)
    print('第2站')
    print(list_stage02)


def show_all_data():

    length = len(all_data)
    print('all_data 資料長度 : ', length)
    for i in range(0, length):
        print(all_data[i])

def export_data():
    global all_data
    length = len(all_data)
    print('資料長度 : ', length)
    if length == 0:
        message = '無資料, 離開'
        print(message)
        text1.insert('end', message)
        main_message2.set(message)
        return
    else:
        # 開啟輸出的 csv 檔案
        filename_w = '匯出資料範例.csv'
        with open(filename_w, 'w', newline = '') as csvfile:
            # 建立 csv 檔寫入物件
            writer = csv.writer(csvfile)

            # 寫入二維串列資料
            writer.writerows(all_data)

        message = '匯出資料 完成'
        #print(message)
        #text1.insert('end', message)

def export_data_to_excel():
    """ tbd
    print('aaaaaa')
    for i in range(0, len(list_room_list)):
        print(list_room_list[i], '長度 : ', len(list_room_list[i]))
    """


    length = len(list_stage402)
    print(length)
    if length > 0:
        for _ in list_stage402:
            print(_)

    print(list_stage402[0])
    print(list_stage402[1])
    print(type(list_stage402[1]))
    print(list_stage402[1][0])
    print(list_stage402[1][1])

    
    global all_data
    length = len(all_data)
    print('資料長度 : ', length)
    if length == 0:
        message = '無資料, 離開'
        print(message)
        text1.insert('end', message)
        main_message2.set(message)
    else:
        # 開啟輸出的 csv 檔案
        """
    
        filename_w = '匯出資料範例.csv'
        with open(filename_w, 'w', newline = '') as csvfile:
            # 建立 csv 檔寫入物件
            writer = csv.writer(csvfile)

            # 寫入二維串列資料
            writer.writerows(all_data)

        """
        message = '匯出資料 完成'
        print(message)
        text1.insert('end', message)

        print('a')
        workbook = openpyxl.Workbook()  # 建立空白的Excel活頁簿物件
        # 取得第 0 個工作表
        sheet = workbook.worksheets[0]

        print('b')

        # 修改工作表的名稱
        sheet.title = "Animal"

        # 以儲存格位置寫入資料
        sheet['A1'] = '中文名'
        sheet['B1'] = '英文名'
        sheet['C1'] = '體重'
        sheet['D1'] = '全名'

        # 以串列寫入資料
        animal01 = ['鼠', 'mouse', '3']
        animal02 = ['牛', 'ox', '48']
        animal03 = ['虎', 'tiger', '33']
        animal04 = ['兔', 'rabbit', '8']
        sheet.append(animal01)  # 逐筆添加到最後一列
        sheet.append(animal02)  # 逐筆添加到最後一列
        sheet.append(animal03)  # 逐筆添加到最後一列
        sheet.append(animal04)  # 逐筆添加到最後一列
        print('c')

        #設定格式
        #sheet = workbook["Animal"]
        sheet["A1"].fill = openpyxl.styles.PatternFill(fill_type="solid", fgColor="FFFF00")  # 設定 f1 儲存格的背景樣式
        sheet["B1"].font = openpyxl.styles.Font(name="Arial", color="ff0000", size=30, bold=True)  # 設定 g1 儲存格的文字樣式
        sheet["C1"].font = openpyxl.styles.Font(name="Arial", color="00ff00", size=30, bold=True)  # 設定 g1 儲存格的文字樣式
        sheet["D1"].font = openpyxl.styles.Font(name="Arial", color="0000ff", size=30, bold=True)  # 設定 g1 儲存格的文字樣式
        print('d')

        filename_w = 'tmp_excel_openpyxl01.xlsx'
        workbook.save(filename_w)  # 儲存檔案
        print("建立 xlsx OK, 檔案 : " + filename_w)





def button00Click():
    print('你按了 匯入生產資料')
    import_csv_data()
    merge_stage_data()

def button01Click():
    print('你按了 匯出至Excel檔案')
    export_data_to_excel()

def button02Click():
    print('你按了 xxx')
   
def button03Click():
    print('你按了 匯入生產資料並將資料加入資料庫')
    print('done')

def button04Click():
    print('你按了 匯入資料庫 TBD')

def button05Click():
    print('你按了 匯出生產資料')
    export_data()

def button10Click():
    print('你按了button10')
    show_info()
    
def button11Click():
    print('你按了button11')
    precheck_csv_data()

def button12Click():
    print('你按了button12')
    show_list_stage()
    show_all_data()

def button13Click():
    print('你按了button13')
    window.destroy()

def button14Click():
    print('你按了button14')
    set_data()

def button15Click():
    print('你按了button15')
    clear_text1()

def set_data():
    '''
    print('set_data')
    #回傳結果
    mesg = text1.get("1.0","end")
    mesg= mesg + dummy_data
    print(mesg)
    text1.insert('end', mesg)
    '''
    global count
    count = count + 1
    message = '  次數' + str(count)
    text1.insert('end', message)

def clear_text1():
    text1.delete(1.0, 'end')
    # 執行 clear 函式時，清空內容

def choose():
    str = "選擇："
    for i in range(0, len(choice)):
        if(choice[i].get() == 1):
            str = str + stage_no[i] + " "
    print(str)
    msg.set(str)


filename = "402除菌區數據紀錄_211214_000000.csv"
            
year_month_day_data = filename[-17:-11]

print(year_month_day_data)

year = filename[-17:-15]
month = filename[-15:-13]
day = filename[-13:-11]

print(int(year)+2000)
print(month)
print(day)



window = tk.Tk()

main_message1 = tk.StringVar()
main_message2 = tk.StringVar()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W)+'x'+str(H)
#size = str(W)+'x'+str(H)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print('{0:d}x{1:d}+{2:d}+{3:d}'.format(W, H, x_st, y_st))

# 設定主視窗標題
window.title('環境溫 / 濕度管制紀錄表 資料庫')

# 設定主視窗之背景色
#window.configure(bg = "#7AFEC6")

icon_filename = 'C:/_git/vcs/_1.data/______test_files1/_material/ims.ico'
window.iconbitmap(icon_filename)   # 更改圖示

x_st = 50
y_st = 50
dx = 120
dy = 80
w = 12
h = 3

button00 = tk.Button(window, width = w, height = h, command = button00Click, text = '匯入生產資料')
button00.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)

#開啟資料庫按鈕
#button01 = tk.Button(window, width = w, height = h, command = button01Click, text = '開啟資料庫')
#button01.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button01_text = tk.StringVar()
#button01 = tk.Button(window, textvariable = button01_text, command = lambda:button01Click(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
button01 = tk.Button(window, textvariable = button01_text, width = w, height = h, command = lambda:button01Click())
#button01 = tk.Button(window, command = xxxxxxx, text='選取檔案')
button01_text.set("匯出至Excel檔案")

button02 = tk.Button(window, width = w, height = h, command = button02Click, text = '讀取資料庫資料')
button02.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button03 = tk.Button(window, width = w, height = h, command = button03Click, text = '匯入生產資料\n將資料加入資料庫')
button03.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button04 = tk.Button(window, width = w, height = h, command = button04Click, text = '匯入資料庫')
button04.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button05 = tk.Button(window, width = w, height = h, command = button05Click, text = '匯出生產資料')
button05.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button00.place(x = x_st + dx * 0, y = y_st + dy * 0)
button01.place(x = x_st + dx * 1, y = y_st + dy * 0)
button02.place(x = x_st + dx * 2, y = y_st + dy * 0)
button03.place(x = x_st + dx * 3, y = y_st + dy * 0)
button04.place(x = x_st + dx * 4, y = y_st + dy * 0)
button05.place(x = x_st + dx * 5, y = y_st + dy * 0)

if flag_debug_mode == True:
    button10 = tk.Button(window, width = w, height = h, command = button10Click, text = '檢查資料\n匯出excel')
    button10.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
    button11 = tk.Button(window, width = w, height = h, command = button11Click, text = '檢查csv/db')
    button11.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
    button12 = tk.Button(window, width = w, height = h, command = button12Click, text = '顯示記憶體資料')
    button12.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
    button13 = tk.Button(window, width = w, height = h, command = button13Click, text = '關閉視窗')
    button13.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
    button14 = tk.Button(window, width = w, height = h, command = button14Click, text = 'Send Data')
    button14.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
    button15 = tk.Button(window, width = w, height = h, command = button15Click, text = 'Clear')
    button15.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)

    button10.place(x = x_st + dx * 0, y = y_st + dy * 1)
    button11.place(x = x_st + dx * 1, y = y_st + dy * 1)
    button12.place(x = x_st + dx * 2, y = y_st + dy * 1)
    button13.place(x = x_st + dx * 3, y = y_st + dy * 1)
    button14.place(x = x_st + dx * 4, y = y_st + dy * 1)
    button15.place(x = x_st + dx * 5, y = y_st + dy * 1)

font_size = 20

# 加入 Label
label_message1 = tk.Label(window, font=("標楷體", font_size), fg = 'red', textvariable = main_message1)
label_message1.pack()
label_message1.place(x = 5, y = 0 + 10)
main_message1.set('')

label_message2 = tk.Label(window, font=("標楷體", font_size), fg = 'red', textvariable = main_message2)
label_message2.pack()
label_message2.place(x = 5 + W * 3 / 4, y = 0 + 10)
main_message2.set('')

msg = tk.StringVar()
label1 = tk.Label(window, text = '選擇顯示站別：')
label1.pack()
label1.place(x = x_st + dx * 0, y = y_st + dy * 2 - 20)
label2 = tk.Label(window, fg = 'red', textvariable = msg)
label2.pack()
label2.place(x = x_st + dx * 0, y = y_st + dy * 2 + 80)

# 加入 Checkbutton
dx2 = dx * 4 / 4   #為了微調距離用
for i in range(0, len(stage_no)):
    item = tk.IntVar()
    choice.append(item)
    item = tk.Checkbutton(window, text = stage_no[i], variable = choice[i], command = choose)
    item.pack()
    item.place(x = x_st + dx2 * (i % 6), y = y_st + dy * 2 + int(i / 6) * 25)

# 加入 Text
text1 = tk.Text(window, width = 100, height = 30)  # 放入多行輸入框
text1.pack()
text1.place(x = x_st + dx * 0, y = y_st + dy * 3 + 50)

message = "匯入生產資料"
main_message1.set(message)

window.mainloop()


"""

    print('新建資料庫, 清除記憶體資料')
    clear_all_data()

    button01_text.set("開啟資料庫")
    print('開啟資料庫, 清除記憶體資料')
    clear_all_data()


"""

