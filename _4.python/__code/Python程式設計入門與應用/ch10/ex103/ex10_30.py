# Filename: ex10_30.py
import tkinter as tk
import tkinter.messagebox as tkmessagebox
import tkinter.filedialog as tkfiledialog
import tkinter.font as tkfont
def Cal():
    options = {}
    options['filetypes'] = [("allfiles","*"),("text","*.txt")]
    options['initialdir'] = "c:\\"
    options['multiple'] = False
    options['title'] = "開啟分析檔案"
    fs = tkfiledialog.askopenfile(**options)    
    if fs:
        f = open(fs.name,'r')
        fc = f.readlines()
        f.close()
        fo = open('output.txt','w')
        fo.write("試題分析結果\n")
        pitem = int(fc[0][0:3])
        fo.write('題數:'+str(pitem)+'\n')
        pmiss = fc[0][4:5]
        fo.write('缺失:'+pmiss+'\n')
        pomit = fc[0][6:7]
        fo.write('遺漏:'+pomit+'\n')
        pid   = int(fc[0][8:10])
        fo.write('ID長度:'+str(pid)+'\n')
        pans  = fc[1]
        fo.write('答案:'+pans)
        pnum  = len(fc)-2
        fo.write('人數:'+str(pnum)+'\n')        
        psitem = []
        for j in range(0, pitem, 1):
            psitem.append(0)
        for i in range(0,pnum, 1):            
            for j in range(0,pitem, 1):                
                if (fc[2+i][pid+j]==pans[j]):                    
                    psitem[j] = psitem[j]+1                
        for j in range(0, pitem):
            fo.write('第'+str(j+1).rjust(2,'0')+'題，難度值p='+str(round(psitem[j]/pnum,2)).ljust(4,'0')+'\n')
        fo.close()
        tkmessagebox.showinfo(title="試題分析", message="分析完成")
    else:   
	     print ("沒有選擇檔案")
def View():
    options = {}
    options['filetypes'] = [("allfiles","*")]
    options['initialdir'] = "c:\\"
    options['multiple'] = False
    options['title'] = "開啟分析檔案"
    fs = tkfiledialog.askopenfile(**options)    
    if fs:        
        f = open(fs.name,'r')
        fc= f.readlines()
        f.close()
        ptext = tk.Text(win, width=800, height=600)        
        for i in range(0, len(fc), 1):
            ptext.insert(tk.INSERT, fc[i])        
        ptext.pack()
        ptext.config(state=tk.DISABLED)       
    else:   
	     print ("沒有選擇檔案")
def About():
    tkmessagebox.showinfo(title="關於我們", message="程式設計者:屏東大學教育學系陳新豐")
def Exit():
    win.destroy() 
def main():
    global win    
    win = tk.Tk()
    win.geometry("800x600")
    win.title("試題與測驗分析程式")
    default_font = tkfont.nametofont('TkDefaultFont')
    default_font.configure(size=15)
    menubar = tk.Menu(win)
    win.config(menu=menubar)
    menu_file = tk.Menu(menubar, tearoff = 0)
    menu_cal  = tk.Menu(menubar, tearoff = 0)
    menu_help = tk.Menu(menubar, tearoff = 0)    
    menubar.add_cascade(label='檔案', menu=menu_file)
    menubar.add_cascade(label='計算', menu=menu_cal)
    menubar.add_cascade(label='Help', menu=menu_help)
    menu_file.add_command(label='結束', command=Exit)
    menu_cal.add_command(label='計算', command=Cal)
    menu_cal.add_command(label='檢視', command=View)    
    menu_help.add_command(label='關於', command=About)
    win.mainloop()
main()