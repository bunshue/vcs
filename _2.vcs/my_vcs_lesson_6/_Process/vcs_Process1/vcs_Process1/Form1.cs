using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;       //for Process
using System.Threading;
using System.IO;    //for File
using System.Runtime.InteropServices;   //for DllImport
using System.Drawing.Imaging;           //for PixelFormat

namespace vcs_Process1
{
    public partial class Form1 : Form
    {
        Process myProcess;
        int cnt = 0;

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
            int x_st;
            int y_st;
            int dx;
            int dy;
            //button
            x_st = 12;
            y_st = 12;
            dx = 170;
            dy = 55;

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

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            button30.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            string pdf_path = "C:\\______test_files\\note_Linux_workstation.pdf";
            Process process;
            process = Process.Start(pdf_path);
            process.WaitForExit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Process process = new Process();
            process = Process.Start(@"C:\_git\vcs\_2.vcs\ims\imsLink\bin\Debug\imsLink.exe");
            richTextBox1.Text += "ProcessName : " + process.ProcessName + "\n";
            richTextBox1.Text += "SessionId : " + process.SessionId.ToString() + "\n";
            richTextBox1.Text += "StartTime : " + process.StartTime + "\n";
            richTextBox1.Text += "Id : " + process.Id.ToString() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if ((myProcess != null) && (!myProcess.HasExited))
                myProcess.Kill();
            else
                richTextBox1.Text += " already killed ";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (timer1.Enabled == false)
            {
                timer1.Enabled = true;
                button3.Text = "停止";
            }
            else
            {
                timer1.Enabled = false;
                button3.Text = "自動開關程式";
            }
            cnt = 0;

        }

        int start_cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            richTextBox1.Text += "s";
            cnt++;
            if ((cnt) == 3)
            {
                start_cnt++;
                richTextBox1.Text += " " + start_cnt.ToString() + " ";
                button1_Click(sender, e);
            }
            else if ((cnt) == 10)
            {
                button2_Click(sender, e);
                cnt = 0;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //此範例會啟動記事本的實例。
            //以2秒的間隔來抓取相關進程的實體記憶體使用量，最多10秒。
            //此範例會偵測進程是否會在10秒之前結束。
            //此範例會關閉進程（如果它仍然在10秒後執行）。

            try
            {   //可能會產生錯誤的程式區段
                using (Process process = Process.Start("Notepad.exe"))
                {
                    // Display physical memory usage 5 times at intervals of 2 seconds.
                    for (int i = 0; i < 10; i++)
                    {
                        if (!process.HasExited)
                        {
                            // Discard cached information about the process.
                            process.Refresh();
                            // Print working set to console.
                            //Console.WriteLine($"Physical Memory Usage: {process.WorkingSet}");
                            richTextBox1.Text += "Physical Memory Usage: " + process.WorkingSet64.ToString() + "\n";
                            //label1.Text = process.WorkingSet64.ToString();
                            // Wait 2 seconds.
                            Thread.Sleep(2000);
                        }
                        else
                        {
                            break;
                        }
                    }

                    // Close process by sending a close message to its main window.
                    process.CloseMainWindow();
                    // Free resources associated with process.
                    process.Close();
                }
            }
            catch (Exception ex)
            {
                //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "The following exception was raised: \n";
                richTextBox1.Text += "xxx錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //使用IE
            //Process.Start("IExplore.exe", "www.google.com.tw");   //same
            Process.Start("iexplore.exe", "www.google.com.tw");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Process.Start("Firefox.exe", "www.google.com.tw");
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Process.Start("Firefox.exe");
        }

        private void button8_Click(object sender, EventArgs e)
        {
            try
            {
                using (Process process = new Process())
                {
                    process.StartInfo.UseShellExecute = false;
                    // You can start any process, HelloWorld is a do-nothing example.
                    process.StartInfo.FileName = @"C:\_git\vcs\_2.vcs\ims\imsLink\bin\Debug\imsLink.exe";
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

        private void button9_Click(object sender, EventArgs e)
        {
            //呼叫系統內建小鍵盤     fail
            //Process.Start("" + Environment.SystemDirectory + "/osk.exe");

            //開啟特定程式
            //Process.Start(@"C:\___small\imagesweeper5.1影像清潔工.exe");

            //開啟小算盤應用程式
            //Process.Start(@"C:\WINDOWS\system32\calc.exe");

            //開啟檔案 由預設程式開啟
            //Process.Start("C:\\______test_files\\my_text_file.txt");

            //開啟記事本程式
            //Process.Start("notepad.exe");

            //開啟程式
            //Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL");
            Process.Start("winver.exe ");              //--打開Windows版本信息

            //開啟imsLink
            //Process.Start(@"C:\_git\vcs\_2.vcs\ims\imsLink\bin\Debug\imsLink.exe");

            //呼叫外部的Exe文件
            //Process.Start(textBox1.Text);  //呼叫 *.exe
        }

        private void button10_Click(object sender, EventArgs e)
        {
            ProcessStartInfo processStartInfo = new ProcessStartInfo();
            processStartInfo.FileName = "explorer.exe";  //資源管理器
            processStartInfo.Arguments = @"C:\";
            Process.Start(processStartInfo);

        }

        private void button11_Click(object sender, EventArgs e)
        {
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

        private void button12_Click(object sender, EventArgs e)
        {
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
            filename = @"C:\______test_files\__RW\_gif\sky.gif";

            Process.Start("explorer.exe", filename);
            //Process.Start(filename);    //same

            //開啟一個程式
            //Process newprocess = Process.Start(filename);



        }

        private void button13_Click(object sender, EventArgs e)
        {
            //列出正在執行的任務
            richTextBox1.Text = string.Empty;
            Process[] processes = Process.GetProcesses();
            foreach (Process process in processes)
            {
                if (process.MainWindowTitle.Length > 0)
                    richTextBox1.Text += "任務名： " + process.MainWindowTitle + "\n";
            }

        }

        private void button14_Click(object sender, EventArgs e)
        {
            //取得本機端上執行中的應用程式
            //[C#]取得本機端上，執行中有 GUI 介面的應用程式
            //Environment.MachineName 屬性 : 取得這個本機電腦的 NetBIOS 名稱。
            //Process.GetProcesses 方法 (String) : 為指定電腦上的每個處理序資源建立新的 Process 元件。
            //Process.MainWindowHandle 屬性 : 取得相關處理序主視窗的視窗控制代碼。
            richTextBox1.Text = string.Empty;
            foreach (Process p in Process.GetProcesses(Environment.MachineName))
            {
                if (p.MainWindowHandle != IntPtr.Zero)  // 判斷 MainWindowHandle 為非零值的應用程式，表示有主視窗
                {
                    //listBox1.Items.Add(p.ToString());
                    richTextBox1.Text += p.ToString() + "\n";
                }
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            richTextBox1.Text = string.Empty;

            // 列出系統中所有的程序
            //Process[] processes = Process.GetProcesses(Environment.MachineName);   //相同
            Process[] processes = Process.GetProcesses();

            richTextBox1.Text += "系統中共有： " + processes.Length.ToString() + " 個程序\n";

            foreach (Process p in processes)
            {
                /*
                // 因為使用 Idle 的 StartTime 會造成錯誤，因此先排除。對其他程序取時間也會造成錯誤，故不用。
                if (!p.ProcessName.Equals("Idle"))
                {
                    // 顯示程序的名稱及啟動時間
                    richTextBox1.Text += p.ProcessName + "\t\t" + p.StartTime.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
                }
                else
                {
                    richTextBox1.Text += p.ProcessName + "\t\t" + "xxxxxxxxxxxxxxxx\n";
                }
                */

                richTextBox1.Text += p.ProcessName + "\n";
            }

        }

        private void button16_Click(object sender, EventArgs e)
        {
            //C# 指定程序還原與置於前景視窗 
            // 取得目前電腦的處理程序
            richTextBox1.Text += "找到 " + Process.GetProcesses().Length + " 個程序\n\n";
            foreach (Process pTarget in Process.GetProcesses())
            {
                richTextBox1.Text += "找到 " + pTarget.ProcessName + "\n";
                if (pTarget.ProcessName == "ACDSee32")  // 取得處理序名稱並與指定程序名稱比較
                {
                    richTextBox1.Text += "\t你開啟了ACDSee32，移到前台。\n";
                    //listBox1.Items.Add(pTarget.ProcessName + "\n");
                    HandleRunningInstance(pTarget);
                }
            }

        }

        //範圍
        public struct Rect
        {
            public int Left;
            public int Top;
            public int Right;
            public int Bottom;
        }
        [DllImport("user32.dll")]
        //取得應用程式畫面
        public static extern Boolean GetWindowRect(IntPtr hWnd, ref Rect rect);
        [DllImport("User32.dll")]
        private static extern bool ShowWindowAsync(IntPtr hWnd, int cmdShow);
        [DllImport("User32.dll")]
        //將程式置於前景
        private static extern bool SetForegroundWindow(IntPtr hWnd);
        [DllImport("user32.dll")]
        //顯示視窗
        private static extern IntPtr ShowWindow(IntPtr hWnd, int nCmdShow);

        private const int WS_SHOWNORMAL = 1;
        public static void HandleRunningInstance(Process instance)
        {
            // 相同時透過ShowWindowAsync還原，以及SetForegroundWindow將程式至於前景
            ShowWindowAsync(instance.MainWindowHandle, WS_SHOWNORMAL);
            SetForegroundWindow(instance.MainWindowHandle);
            //Environment.SpecialFolder.
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //在c#中，如果启动了外部程序，一般也可以通过退出码来确认程序的运行状态：

            Process p = Process.Start(@"C:\_git\vcs\_2.vcs\ims\imsLink\bin\Debug\imsLink.exe");

            p.WaitForExit();
            if (p.ExitCode == 0)
            {
                //richTextBox1.Text += "11111111111111111111\n";
            }
            else
            {
                //richTextBox1.Text += "222222222222222222222\n";
            }
            richTextBox1.Text += "退出碼 : " + p.ExitCode.ToString() + "\n";
            richTextBox1.Text += "退出時間 : " + p.ExitTime + "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            richTextBox1.Text = string.Empty;

            // 列出系統中所有的程序
            //Process[] processes = Process.GetProcesses(Environment.MachineName);   //相同
            Process[] processes = Process.GetProcesses();

            richTextBox1.Text += "系統中共有： " + processes.Length.ToString() + " 個程序\n";

            foreach (Process p in processes)
            {
                /*
                // 因為使用 Idle 的 StartTime 會造成錯誤，因此先排除。對其他程序取時間也會造成錯誤，故不用。
                if (!p.ProcessName.Equals("Idle"))
                {
                    // 顯示程序的名稱及啟動時間
                    richTextBox1.Text += p.ProcessName + "\t\t" + p.StartTime.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
                }
                else
                {
                    richTextBox1.Text += p.ProcessName + "\t\t" + "xxxxxxxxxxxxxxxx\n";
                }
                */

                //取得特定應用程式的資訊
                //richTextBox1.Text += p.ProcessName + "\n";
                if (p.ProcessName == "putty")
                {
                    richTextBox1.Text += p.ProcessName + "\n";
                    SetForegroundWindow(p.MainWindowHandle);
                    ShowWindow(p.MainWindowHandle, 1);
                    richTextBox1.Text += "time = " + p.StartTime.ToString() + "\n";
                    Rect rect = new Rect();
                    GetWindowRect(p.MainWindowHandle, ref rect);
                    richTextBox1.Text += "Left = " + rect.Left.ToString() + "\n";
                    richTextBox1.Text += "Right = " + rect.Right.ToString() + "\n";
                    richTextBox1.Text += "Top = " + rect.Top.ToString() + "\n";
                    richTextBox1.Text += "Bottom = " + rect.Bottom.ToString() + "\n";
                    richTextBox1.Text += "Width = " + (rect.Right - rect.Left).ToString() + "\n";
                    richTextBox1.Text += "Height = " + (rect.Bottom - rect.Top).ToString() + "\n";

                    richTextBox1.Text += "擷取此應用程式的畫面\n";

                    int width = rect.Right - rect.Left;
                    int height = rect.Bottom - rect.Top;
                    Bitmap bmp = new Bitmap(width, height, PixelFormat.Format32bppArgb);

                    Graphics.FromImage(bmp).CopyFromScreen(rect.Left,
                                                           rect.Top,
                                                           0,
                                                           0,
                                                           new Size(width, height),
                                                           CopyPixelOperation.SourceCopy);
                    string filename = Application.StartupPath + "\\capture_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                    //string path = DateTime.Now.ToString("yyyyMMdd HHmmss") + ".jpg";
                    //bmp.Save(path);
                    bmp.Save(filename, ImageFormat.Jpeg);
                }
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button19_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開啟檔案總管 給定參數";
            richTextBox1.Text += "開啟檔案總管 開啟路徑在D槽";
            //  C:\Windows\explorer.exe /n,/e,D:\

            //呼叫外部程式 並帶有參數的用法
            Process process = new Process();
            process.StartInfo.FileName = @"C:\Windows\explorer.exe";
            process.StartInfo.Arguments = @"/n,/e,D:\";
            process.Start();
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //列出所有的Process
            Process[] all = Process.GetProcesses();
            int length = all.Length;
            for (int index = 0; index < length; index++)
            {
                richTextBox1.Text += String.Format("{0} \tID:{1}", all[index].ProcessName, all[index].Id) + "\n";
            }

        }

        private void button21_Click(object sender, EventArgs e)
        {
            //列出firefox的Process
            Process[] ps = Process.GetProcessesByName("firefox");
            foreach (Process p in ps)
            {
                richTextBox1.Text += String.Format("{0} \tID:{1}", p.ProcessName, p.Id) + "\n";
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //啟動一個外部程序

            ProcessStartInfo Info = new ProcessStartInfo();
            Info.FileName = "notepad.exe";  //設置外部程序名
            Info.Arguments = "article.txt"; //設置外部程序的啟動參數（命令行參數）為test.txt
            Info.WorkingDirectory = @"C:\______test_files\__RW\_txt";   //設置外部程序工作目錄

            //創建一個進程
            Process Proc;
            try
            {////啟動外部程序//
                Proc = Process.Start(Info);
            }
            catch (System.ComponentModel.Win32Exception ex)
            {
                Console.WriteLine("系統找不到指定的程序文件。\r{0}", ex);
                return;
            }   //打印出外部程序的開始執行時間
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

        private void button23_Click(object sender, EventArgs e)
        {
            //Process 測試

            //取出名字裡有特定字樣的process
            Process[] processes = Process.GetProcessesByName("firefox");

            //取出所有的process
            //Process[] processes = Process.GetProcesses();
            foreach (Process p in processes)
            {
                //p.Kill(); 指名刪除這個process
                richTextBox1.Text += p.ProcessName + "\n";
            }


        }

        private void button24_Click(object sender, EventArgs e)
        {
            //啟動一個外部程序

            ////////////聲明一個程序信息類，指定啟動進程是的參數信息     
            ProcessStartInfo Info = new ProcessStartInfo();

            //設置外部程序名
            Info.FileName = "notepad.exe";
            //設置外部程序的啟動參數（命令行參數）為test.txt
            Info.Arguments = "file_to_save.txt";
            //設置外部程序工作目錄為  C:\
            Info.WorkingDirectory = @"C:\______test_files";
            ///////////聲明一個程序類,也就是創建一個進程
            Process Proc;
            try
            {
                //     //啟動外部程序
                Proc = Process.Start(Info);
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

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "(偽)關機\n";
            //Process.Start("shutdown","-s -t 0");//關機程序
        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {
            //尋找並殺死process
            string process_name = "acdsee";
            KillProcess(process_name);
        }

        //C#殺死進程
        private void KillProcess(string processName)
        {
            Process myproc = new Process();
            //得到所有打開的進程
            try
            {
                //foreach (Process thisproc in Process.GetProcessesByName("WINPROJ"))
                foreach (Process thisproc in Process.GetProcesses())
                {
                    richTextBox1.Text += "get process : " + thisproc.ProcessName + "\n";

                    /*
                    if (!thisproc.CloseMainWindow())
                    {
                        //thisproc.Kill();
                        richTextBox1.Text += "殺死進程 : " + processName + "\n";
                    }
                    */
                }
            }
            catch (System.Exception ex)
            {
                //ScriptManager.RegisterStartupScript(this.btnUpload, GetType(), "dis", "alert(進程殺死失敗);", true);
            }
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //使用Process類調用外部exe程序

            Process p = Process.Start("notepad.exe");
            p.WaitForExit();//關鍵，等待外部程序退出後才能往下執行
        }

        private void button30_Click(object sender, EventArgs e)
        {
        }


    }
}



/*
c# 執行外部程式(.exe，.bat…)

Process p = new Process();
//Process類有一個StartInfo屬性，這個是ProcessStartInfo類，包括了一些屬性和方法，下面用到了幾個屬性：
p.StartInfo.FileName = "cmd.exe"; //設定程序名
p.StartInfo.Arguments = "/c" + FullBatPath; //設定程式執行參數" /c " 執行完以下命令後停止
p.StartInfo.UseShellExecute = false; //關閉Shell的使用
p.StartInfo.RedirectStandardInput = true; //重定向標準輸入
p.StartInfo.RedirectStandardOutput = true; //重定向標準輸出
p.StartInfo.RedirectStandardError = true; //重定向錯誤輸出
p.StartInfo.CreateNoWindow = false; //true設置不顯示窗口
p.StartInfo.RedirectStandardError = true;
p.Start(); //啟動
while (!p.HasExited)
{
p.WaitForExit(2000); //等待20秒
}
p.Dispose();
*/


