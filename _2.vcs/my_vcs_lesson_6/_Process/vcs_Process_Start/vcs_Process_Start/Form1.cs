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
//Process.Start("C:\\______test_files\\my_text_file.txt");

//開啟程式
//Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL");

//呼叫外部的Exe文件
//Process.Start(textBox1.Text);  //呼叫 *.exe

            //用預設的程式開啟檔案
            string filename = "C:\\______test_files\\aaaaaaa.txt";

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
            filename = @"C:\______test_files\__pic\_gif\sky.gif";

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
            int BORDER = 20;
            int x_st = BORDER;
            int y_st = BORDER;
            int w = 150;
            int h = 50;
            int dx = w + 10;
            int dy = h + 10;

            int W = BORDER + w + BORDER;
            int H = BORDER + h * 10 + 10 * 9 + BORDER;

            groupBox1.Size = new Size(W, H);
            groupBox2.Size = new Size(W, H);

            W = BORDER + w * 2 + BORDER;
            groupBox5.Size = new Size(W, H);

            W = BORDER + w + BORDER;
            groupBox3.Size = new Size(W, 160);
            groupBox4.Size = new Size(W, 300);

            groupBox1.Location = new Point(x_st, y_st);
            dx = W;
            groupBox2.Location = new Point(x_st + dx * 1 + BORDER, y_st);
            groupBox5.Location = new Point(x_st + dx * 2 + BORDER + BORDER, y_st);
            groupBox3.Location = new Point(x_st + dx * 4 + BORDER, y_st);
            groupBox4.Location = new Point(x_st + dx * 4 + BORDER, 210);
            richTextBox1.Location = new Point(x_st + dx * 5 + BORDER + BORDER, y_st);

            dx = w + 10;
            dy = h + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button30.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button40.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            button42.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button43.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button44.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button45.Location = new Point(x_st + dx * 0, y_st + dy * 3);
        }

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
            //Process.Start(@"C:\_git\ims1\iMS_Link\iMS_Link\bin\Debug\iMS_Link.exe");

            //or

            //開啟imsLink
            Process process = new Process();    //創建一個進程用於調用外部程序
            process = Process.Start(@"C:\_git\ims1\iMS_Link\iMS_Link\bin\Debug\iMS_Link.exe");

            richTextBox1.Text += "ProcessName : " + process.ProcessName + "\n";
            richTextBox1.Text += "SessionId : " + process.SessionId.ToString() + "\n";
            richTextBox1.Text += "StartTime : " + process.StartTime + "\n";
            richTextBox1.Text += "Id : " + process.Id.ToString() + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {

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
            string filename = "C:\\______test_files\\__RW\\_pdf\\note_Linux_workstation.pdf";
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
                process.Start();
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

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }

        private void button30_Click(object sender, EventArgs e)
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
            processStartInfo.WorkingDirectory = @"C:\______test_files";

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

        private void button31_Click(object sender, EventArgs e)
        {
            //ProcessStartInfo 1

            //檔案總管 C槽
            string exe_filename = "explorer.exe";   //檔案總管
            ProcessStartInfo processStartInfo = new ProcessStartInfo();
            processStartInfo.FileName = exe_filename;
            processStartInfo.Arguments = @"C:\";
            Process.Start(processStartInfo);

        }

        private void button32_Click(object sender, EventArgs e)
        {
            //ProcessStartInfo 2
            //啟動一個外部程序
            ProcessStartInfo processStartInfo = new ProcessStartInfo();
            processStartInfo.FileName = "notepad.exe";  //設置外部程序名
            processStartInfo.Arguments = "article.txt"; //設置外部程序的啟動參數（命令行參數）為test.txt
            processStartInfo.WorkingDirectory = @"C:\______test_files\__RW\_txt";   //設置外部程序工作目錄

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

        private void button33_Click(object sender, EventArgs e)
        {
            //ProcessStartInfo 3
            //使用預設程式打開指定文件

            string filename = @"C:\______test_files\__RW\_txt\poem.txt";
            //string filename = @"C:\______test_files\__RW\_txt\琵琶行.txt";

            ProcessStartInfo pro = new ProcessStartInfo(filename);
            Process process = new Process();    //創建一個進程用於調用外部程序
            process.StartInfo = pro;
            process.Start();
        }

        private void button34_Click(object sender, EventArgs e)
        {

            //調用外部程序

            string filename = @"C:\______test_files\__RW\_txt\琵琶行.txt";

            //聲明一個程序信息類
            ProcessStartInfo processStartInfo = new ProcessStartInfo();

            //設置外部程序名
            processStartInfo.FileName = "notepad.exe";

            //設置外部程序的啟動參數（命令行參數）為test.txt
            processStartInfo.Arguments = filename;

            //設置外部程序工作目錄為  C:
            processStartInfo.WorkingDirectory = "C:\\";

            Process Proc = new Process();   //創建一個進程用於調用外部程序

            try
            {
                //啟動外部程序
                Proc = Process.Start(processStartInfo);
            }
            catch (Win32Exception ex)
            {
                Console.WriteLine("系統找不到指定的程序文件。{0}", ex);
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

        private void button35_Click(object sender, EventArgs e)
        {
        }

        private void button36_Click(object sender, EventArgs e)
        {
            
        }

        private void button37_Click(object sender, EventArgs e)
        {
            
        }

        private void button38_Click(object sender, EventArgs e)
        {
        }

        private void button39_Click(object sender, EventArgs e)
        {
            try
            {
                using (Process process = new Process())
                {
                    string exe_filename = @"C:\_git\ims1\iMS_Link\iMS_Link\bin\Debug\iMS_Link.exe"; //要執行的程序名稱
                    process.StartInfo.FileName = exe_filename;  //設定要啟動的程式
                    process.StartInfo.UseShellExecute = false;
                    process.StartInfo.CreateNoWindow = true;
                    process.Start();
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
    }
}
