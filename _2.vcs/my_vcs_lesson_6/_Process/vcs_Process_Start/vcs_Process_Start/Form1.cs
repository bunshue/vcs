using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;       //for Process
using System.Runtime.InteropServices;   //for DllImport

/*
準備中

//呼叫系統內建小鍵盤     fail
//Process.Start("" + Environment.SystemDirectory + "/osk.exe");
//Process.Start("osk.exe");
//Win10不可用 或許可以用在舊版的Windows

//開啟檔案 由預設程式開啟
//Process.Start(@"D:\_git\vcs\_1.data\______test_files1\my_text_file.txt");

//開啟程式
//Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL");

//呼叫外部的Exe文件
//Process.Start(textBox1.Text);  //呼叫 *.exe

            //用預設的程式開啟檔案
            string filename = @"D:\_git\vcs\_1.data\______test_files1\aaaaaaa.txt";

            if (File.Exists(filename) == false)
            {
                MessageBox.Show("檔案: " + filename + "不存在，無法開啟。\n");
                return;
            }
            else
            {
                Process.Start(filename);
            }

            //用預設的程式開啟檔案
            filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_gif\sky.gif";

            Process.Start("explorer.exe", filename);
            //Process.Start(filename);    //same

            //開啟一個程式
            //Process newprocess = Process.Start(filename);

 */

namespace vcs_Process_Start
{
    public partial class Form1 : Form
    {
        //c#調用系統資源
        //引入API函數
        [DllImportAttribute("user32.dll")]
        public static extern int FindWindow(string ClassName, string WindowName);
        [DllImport("user32.dll")]
        public static extern int ShowWindow(int handle, int cmdShow);

        private const int SW_HIDE = 0;//API參數表示隱藏窗口
        private const int SW_SHOW = 5;//API參數表示用當前的大小和位置顯示窗口

        Panel panel1 = new Panel();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int W = 200;
            int H = 580;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;
            groupBox1.Size = new Size(W, H);
            groupBox2.Size = new Size(W, H);
            groupBox5.Size = new Size(W, H);
            groupBox3.Size = new Size(W, 200 - 40);
            groupBox4.Size = new Size(W, 300);
            groupBox6.Size = new Size(W, 200 - 40);
            groupBox1.Location = new Point(x_st, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox5.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            groupBox4.Location = new Point(x_st + dx * 3, y_st + dy * 0 + 170);
            groupBox6.Location = new Point(x_st + dx * 3, y_st + dy * 0 + 170 + 310);

            richTextBox1.Size = new Size(500, 300);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0 + 380);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            y_st = 20;
            dx = 180 + 10;
            dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button40.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            button42.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button43.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button44.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button45.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            button8.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            this.Size = new Size(1400, 750);
            this.Text = "vcs_Process_Start";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //開啟Windows小程式
            //開啟小算盤應用程式
            //Process.Start(@"C:\WINDOWS\system32\calc.exe");   same
            Process.Start("calc");  //打開計算機

            /*
            //開啟記事本程式
            //Process.Start("notepad.exe"); //same
            Process.Start("notepad");   //打開記事本

            //小畫家
            Process.Start("mspaint.exe");

            //小作家(WordPad)
            Process.Start("write.exe");

            //啟動Windows Media Player
            Process.Start("dvdplay.exe");

            //打開Windows版本信息
            Process.Start("winver.exe ");

            //cmd命令列
            Process.Start("cmd.exe");

            //打開D槽
            Process.Start("d:");
            */
        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            //開啟Office程式   (偽)
            Process.Start("EXCEL.exe");  //啟動Excel

            //打開Word
            Process.Start(@"C:\Program Files\Microsoft Office\OFFICE15\winword.exe");

            //打開Excel
            Process.Start(@"C:\Program Files\Microsoft Office\OFFICE15\excel.exe");

            //打開Access fail
            //Process.Start(@"C:\Program Files\Microsoft Office\OFFICE15\msaccess.exe");

            //打開PowerPoint
            Process.Start(@"C:\Program Files\Microsoft Office\OFFICE15\powerpnt.exe");

            //打開OutLook
            Process.Start(@"C:\Program Files\Microsoft Office\OFFICE15\outlook.exe");
            */
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //開啟各種程式
            Process.Start("Firefox.exe");

            //開啟特定程式 1
            Process.Start(@"C:\___small\imagesweeper5.1影像清潔工.exe");

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //開啟imsLink
            //Process.Start(@"D:\_git\ims1\iMS_Link\iMS_Link\bin\Debug\iMS_Link.exe");

            //or

            //開啟imsLink
            Process process = new Process();    //創建一個進程用於調用外部程序
            process = Process.Start(@"D:\_git\ims1\iMS_Link\iMS_Link\bin\Debug\iMS_Link.exe");

            richTextBox1.Text += "ProcessName : " + process.ProcessName + "\n";
            richTextBox1.Text += "SessionId : " + process.SessionId.ToString() + "\n";
            richTextBox1.Text += "StartTime : " + process.StartTime + "\n";
            richTextBox1.Text += "Id : " + process.Id.ToString() + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //開啟IE, 指名網址
            //Process.Start("IExplore.exe", "www.google.com.tw");   //same
            Process.Start("iexplore.exe", "www.google.com.tw");
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //開啟FireFox, 指名網址
            Process.Start("Firefox.exe", "www.google.com.tw");
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //用Adobe開啟pdf檔案
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_pdf\note_Linux_workstation.pdf";
            Process process = new Process();    //創建一個進程用於調用外部程序
            process = Process.Start(filename);
            process.WaitForExit();  //需等開啟的程式結束後才可以回到表單
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //檔案總管 C槽
            //開啟檔案總管
            String pathname = "C:\\";
            Process.Start(pathname);
            /*
            if (Directory.Exists(this.FolderPath))
            {
                Process.Start(this.FolderPath);
                return true;
            }
            else
                return false;
             */
        }

        private void button14_Click(object sender, EventArgs e)
        {
            string exe_filename = "notepad.exe";
            Process process = new Process();    //創建一個進程用於調用外部程序
            try
            {
                process.StartInfo.FileName = exe_filename;
                process.StartInfo.UseShellExecute = false;
                process.StartInfo.CreateNoWindow = true;
                process.Start();    //啟動程式
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button20_Click(object sender, EventArgs e)
        {
            //開啟記事本, 指名檔案

            //ProcessStartInfo 0

            //啟動一個外部程序

            ////////////聲明一個程序信息類，指定啟動進程是的參數信息     
            ProcessStartInfo processStartInfo = new ProcessStartInfo();

            //設置外部程序名
            processStartInfo.FileName = "notepad.exe";
            //設置外部程序的啟動參數（命令行參數）為test.txt
            processStartInfo.Arguments = "file_to_save.txt";
            //設置外部程序工作目錄為  C:\
            processStartInfo.WorkingDirectory = @"D:\_git\vcs\_1.data\______test_files1";

            ///////////聲明一個程序類,也就是創建一個進程
            Process Proc;
            try
            {
                //     //啟動外部程序
                Proc = Process.Start(processStartInfo);
            }
            catch (System.ComponentModel.Win32Exception ex)
            {
                Console.WriteLine("系統找不到指定的程序文件。\r{0}", ex);
                return;
            }
            //打印出外部程序的開始執行時間
            Console.WriteLine("外部程序的開始執行時間：{0}", Proc.StartTime);
            //等待3秒鐘
            Proc.WaitForExit(3000);

            //如果這個外部程序沒有結束運行則對其強行終止
            if (Proc.HasExited == false)
            {
                Console.WriteLine("由主程序強行終止外部程序的運行！");
                Proc.Kill();
            }
            else
            {
                Console.WriteLine("由外部程序正常退出！");
            }
            Console.WriteLine("外部程序的結束運行時間：{0}", Proc.ExitTime);
            Console.WriteLine("外部程序在結束運行時的返回值：{0}", Proc.ExitCode);
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //ProcessStartInfo 1

            //檔案總管 C槽
            string exe_filename = "explorer.exe";   //檔案總管
            ProcessStartInfo processStartInfo = new ProcessStartInfo();
            processStartInfo.FileName = exe_filename;
            processStartInfo.Arguments = @"C:\";
            Process.Start(processStartInfo);
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //ProcessStartInfo 2
            //啟動一個外部程序
            ProcessStartInfo processStartInfo = new ProcessStartInfo();
            processStartInfo.FileName = "notepad.exe";  //設置外部程序名
            processStartInfo.Arguments = "article.txt"; //設置外部程序的啟動參數（命令行參數）為test.txt
            processStartInfo.WorkingDirectory = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt";   //設置外部程序工作目錄

            Process process = new Process();    //創建一個進程用於調用外部程序
            try
            {
                process = Process.Start(processStartInfo);
            }
            catch (Win32Exception ex)
            {
                Console.WriteLine("系統找不到指定的程序文件。\r{0}", ex);
                return;
            }   //打印出外部程序的開始執行時間
            Console.WriteLine("外部程序的開始執行時間：{0}", process.StartTime);

            //等待3秒鐘
            process.WaitForExit(3000);

            //如果這個外部程序沒有結束運行則對其強行終止
            if (process.HasExited == false)
            {
                Console.WriteLine("由主程序強行終止外部程序的運行！");
                process.Kill();
            }
            else
            {
                Console.WriteLine("由外部程序正常退出！");
            }
            Console.WriteLine("外部程序的結束運行時間：{0}", process.ExitTime);
            Console.WriteLine("外部程序在結束運行時的返回值：{0}", process.ExitCode);
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //ProcessStartInfo 3
            //使用預設程式打開指定文件

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\poem.txt";
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";

            ProcessStartInfo psi = new ProcessStartInfo(filename);
            Process process = new Process();    //創建一個進程用於調用外部程序
            process.StartInfo = psi;
            process.Start();    //啟動程式
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //ProcessStartInfo 4
            //調用外部程序

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";

            //聲明一個程序信息類
            ProcessStartInfo processStartInfo = new ProcessStartInfo();

            //設置外部程序名
            processStartInfo.FileName = "notepad.exe";

            //設置外部程序的啟動參數（命令行參數）為test.txt
            processStartInfo.Arguments = filename;

            //設置外部程序工作目錄為  C:
            processStartInfo.WorkingDirectory = "C:\\";

            Process process = new Process();   //創建一個進程用於調用外部程序

            try
            {
                //啟動外部程序
                process = Process.Start(processStartInfo);
            }
            catch (Win32Exception ex)
            {
                Console.WriteLine("系統找不到指定的程序文件。{0}", ex);
                return;
            }

            //打印出外部程序的開始執行時間
            Console.WriteLine("外部程序的開始執行時間：{0}", process.StartTime);

            //等待3秒鐘
            process.WaitForExit(3000);

            //如果這個外部程序沒有結束運行則對其強行終止
            if (process.HasExited == false)
            {
                Console.WriteLine("由主程序強行終止外部程序的運行！");
                process.Kill();
            }
            else
            {
                Console.WriteLine("由外部程序正常退出！");
            }
            Console.WriteLine("外部程序的結束運行時間：{0}", process.ExitTime);
            Console.WriteLine("外部程序在結束運行時的返回值：{0}", process.ExitCode);


        }

        private void button25_Click(object sender, EventArgs e)
        {
            //ProcessStartInfo 5
            try
            {
                using (Process process = new Process())
                {
                    string exe_filename = @"D:\_git\ims1\iMS_Link\iMS_Link\bin\Debug\iMS_Link.exe"; //要執行的程序名稱
                    process.StartInfo.FileName = exe_filename;  //設定要啟動的程式
                    process.StartInfo.UseShellExecute = false;
                    process.StartInfo.CreateNoWindow = true;
                    process.Start();    //啟動程式
                    // This code assumes the process you are starting will terminate itself. 
                    // Given that is is started without a window so you cannot terminate it 
                    // on the desktop, it must terminate itself or you can do it programmatically
                    // from this application using the Kill method.
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }

        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button40_Click(object sender, EventArgs e)
        {
            //開啟Notepad程序
            process1.StartInfo.FileName = "notepad.exe";
            process1.Start();
        }

        private void button41_Click(object sender, EventArgs e)
        {
            //關閉Notepad程序
            Process[] processes = Process.GetProcessesByName("Notepad");
            foreach (Process process in processes)
            {
                process.CloseMainWindow();
                process.WaitForExit(3000);
                process.Close();
            }
        }

        private void button42_Click(object sender, EventArgs e)
        {
            //打開註冊表
            Process.Start("regedit.exe");
        }

        private void button43_Click(object sender, EventArgs e)
        {
            //打開控制面板1
            //打開播放器() 
            Process.Start("mplayer2.exe");

            //打開資源管理器() 
            Process.Start("explorer.exe");

            //打開任務管理器() 
            Process.Start("taskmgr.exe");

            //打開事件檢視器() 
            Process.Start("eventvwr.exe");

            //打開系統信息() fail
            //Process.Start("winmsd.exe");

            //打開備份還原() fail
            //Process.Start("ntbackup.exe");

            //打開Windows版本() 
            Process.Start("winver.exe");
        }

        private void button44_Click(object sender, EventArgs e)
        {
            //打開控制面板2
            //打開控制面板() 
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL");

            //打開控制面板輔助選項鍵盤() 
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL access.cpl,,1");

            //打開控制面板輔助選項聲音() 
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL access.cpl,,2");

            //打開控制面板輔助選項顯示() 
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL access.cpl,,3");

            //打開控制面板輔助選項鼠標() 
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL access.cpl,,4");

            //打開控制面板輔助選項常規() 
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL access.cpl,,5");

            //打開控制面板添加新硬件向導() 
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL sysdm.cpl @1");

            //打開控制面板添加新打印機向導() 
            Process.Start("rundll32.exe", "shell32.dll,SHHelpShortcuts_RunDLL AddPrinter");
        }

        private void button45_Click(object sender, EventArgs e)
        {
            //打開控制面板3
            //打開控制面板添加刪除程序安裝卸載面板() 
            Process.Start("rundll32.exe", "shell32.dll,shell32.dll,Control_RunDLL appwiz.cpl,,1");

            //打開控制面板添加刪除程序安裝Windows面板() 
            Process.Start("rundll32.exe", "shell32.dll,shell32.dll,Control_RunDLL appwiz.cpl,,2");

            //打開控制面板添加刪除程序啟動盤面板() 
            Process.Start("rundll32.exe", "shell32.dll,shell32.dll,Control_RunDLL appwiz.cpl,,3");

            //打開建立快捷方式對話框() 
            Process.Start("rundll32.exe", " appwiz.cpl,NewLinkHere %1");

            //打開日期時間選項() 
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL timedate.cpl,,0");

            //打開時區選項() 
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL timedate.cpl,,1");

            //建立公文包() 
            Process.Start("rundll32.exe", " syncui.dll,Briefcase_Create");

            //打開復制軟碟窗口() 
            Process.Start("rundll32.exe", " diskcopy.dll,DiskCopyRunDll");

            //打開新建撥號連接() 
            Process.Start("rundll32.exe", " rnaui.dll,RnaWizard");

            //打開顯示屬性背景() 
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL desk.cpl,,0");

            //打開顯示屬性屏幕保護() 
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL desk.cpl,,1");

            //打開顯示屬性外觀() 
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL desk.cpl,,2");

            //打開顯示屬性屬性() 
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL desk.cpl,,3");
        }

        //------------------------------------------------------------  # 60個

        private void button8_Click(object sender, EventArgs e)
        {
            //開啟外部程式並內嵌至表單中
            //將程序窗口嵌入到任務欄中
            panel1.Location = new Point(900, 10);
            panel1.Size = new Size(400, 400);
            //panel1.Dock = System.Windows.Forms.DockStyle.Fill;
            Controls.Add(this.panel1);

            //通過 WIN32 API 實現嵌入程序窗體，win32api

            //string sPath = Environment.GetEnvironmentVariable("windir");//獲取系統變量 windir(windows)    
            const string exe_filename = "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe";
            InsertWindow insertwin = new InsertWindow(panel1, exe_filename);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //開啟外部程式並內嵌至表單中
            //想做一個開啟pdf的, 目前無法指名檔案
            const string exe_filename = @"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_pdf\note_Linux_workstation.pdf";

            panel1.Location = new Point(900, 10);
            panel1.Size = new Size(400, 400);
            //panel1.Dock = System.Windows.Forms.DockStyle.Fill;
            Controls.Add(this.panel1);

            //通過 WIN32 API 實現嵌入程序窗體，win32api

            //string sPath = Environment.GetEnvironmentVariable("windir");//獲取系統變量 windir(windows)    
            //InsertWindow insertwin = new InsertWindow(panel1, exe_filename + " " + filename);
            InsertWindow insertwin = new InsertWindow(panel1, exe_filename);
        }

        //------------------------------------------------------------  # 60個
    }

    //------------------------------------------------------------  # 60個

    class InsertWindow
    {
        /// <summary>  
        /// 將程序嵌入窗體  
        /// </summary>  
        /// <param name="pW">容器</param>  
        /// <param name="appname">程序名</param>  
        public InsertWindow(Panel pW, string exe_filename)
        {
            this.pan = pW;
            this.LoadEvent(exe_filename);
            pane();
        }

        ~InsertWindow()
        {
            if (process != null)
            {
                process.Dispose();
            }
        }

        //#region  函數和變量聲明
        //聲明 Win32 API 
        [DllImport("user32.dll")]
        static extern IntPtr SetParent(IntPtr hWndChild, IntPtr hWndNewParent);

        [DllImport("user32.dll")]
        static extern Int32 GetWindowLong(IntPtr hWnd, Int32 nIndex);

        [DllImport("user32.dll")]
        static extern Int32 SetWindowLong(IntPtr hWnd, Int32 nIndex, Int32 dwNewLong);

        [DllImport("user32.dll")]
        static extern Int32 SetWindowPos(IntPtr hWnd,
            IntPtr hWndInsertAfter,
            Int32 X,
            Int32 Y,
            Int32 cx,
            Int32 cy,
            UInt32 uFlags
        );

        // 定義 Win32 常數 

        const Int32 GWL_STYLE = -16;
        const Int32 WS_BORDER = (Int32)0x00800000L;
        const Int32 WS_THICKFRAME = (Int32)0x00040000L;

        const Int32 SWP_NOMOVE = 0x0002;
        const Int32 SWP_NOSIZE = 0x0001;
        const Int32 SWP_NOZORDER = 0x0004;
        const Int32 SWP_FRAMECHANGED = 0x0020;

        const Int32 SW_MAXIMIZE = 3;
        IntPtr HWND_NOTOPMOST = new IntPtr(-2);

        // 目標應用程序的進程.  
        Process process = null;
        //#endregion

        //#region  容器
        private Panel pan = null;
        public Panel panel1
        {
            set { pan = value; }
            get { return pan; }
        }
        private void pane()
        {
            panel1.Anchor = AnchorStyles.Left | AnchorStyles.Top | AnchorStyles.Right | AnchorStyles.Bottom;
            panel1.Resize += new EventHandler(panel1_Resize);
        }
        private void panel1_Resize(object sender, EventArgs e)
        {
            // 設置目標應用程序的窗體樣式.  

            IntPtr innerWnd = process.MainWindowHandle;
            SetWindowPos(innerWnd, IntPtr.Zero, 0, 0, panel1.ClientSize.Width, panel1.ClientSize.Height, SWP_NOZORDER);
        }
        //#endregion

        //#region  相應事件
        private void LoadEvent(string exe_filename)
        {
            // 啟動目標應用程序.  
            process = Process.Start(exe_filename);
            process.StartInfo.WindowStyle = ProcessWindowStyle.Hidden; //隱藏  
            // 等待, 直到那個程序已經完全啟動.   
            process.WaitForInputIdle();

            // 目標應用程序的主窗體.  
            IntPtr innerWnd = process.MainWindowHandle;

            // 設置目標應用程序的主窗體的父親(為我們的窗體).  
            SetParent(innerWnd, panel1.Handle);

            // 除去窗體邊框.  
            Int32 wndStyle = GetWindowLong(innerWnd, GWL_STYLE);
            wndStyle &= ~WS_BORDER;
            wndStyle &= ~WS_THICKFRAME;
            SetWindowLong(innerWnd, GWL_STYLE, wndStyle);
            SetWindowPos(innerWnd, IntPtr.Zero, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOZORDER | SWP_FRAMECHANGED);

            // 在Resize事件中更新目標應用程序的窗體尺寸.  
            panel1_Resize(panel1, null);
        }
        //#endregion
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


/*
ProcessStartInfo psi = new ProcessStartInfo();
psi.FileName = @"cmd.exe";
psi.Arguments = @"/c net use " + Name + " " + Path + "";
psi.WindowStyle = ProcessWindowStyle.Hidden;
Process.Start(psi);

//------------------------------------------------------------  # 60個

//開啟檔案總管到指定的目錄
string Path = @"C:\dddddddddd";
Process.Start("explorer.exe", Path);

Process.Start(textBox1.Text);//打开文件夹进行查看

//------------------------------------------------------------  # 60個

//C#啟動另外一個C#程序，並傳遞參數
string filename = @"C:\______test_files\aaaaa4.txt";
Process.Start("notepad.exe", filename);

//------------------------------------------------------------  # 60個

Windows Task Scheduler). I am currently using Process.Start() to launch the file (or exe) required by th

Process myProcess = Process.Start("param1", "param2");
if (myProcess != null && !myProcess.HasExited)
    newProcess.Kill();
  
if ((myProcess != null) && (!myProcess.HasExited))
    myProcess.Kill();

process.start加參數
  
proc = Process.Start("C:\Program Files\Windows Media Player\wmplayer.exe", filename)

Then you can kill it normally.

proc.Kill()
  
//------------------------------------------------------------  # 60個

[C#]開啟EXE檔並輸入EXE檔的參數

在程式裡放入下列程式
Process.Start("路徑", "參數"); 

//------------------------------------------------------------  # 60個

*/

