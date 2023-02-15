using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File
using System.Diagnostics;       //for Process
using System.Threading;
using System.Management;    //for ManagementObjectSearcher
using System.Runtime.InteropServices;   //for DllImport
using System.Text.RegularExpressions;
using System.Drawing.Imaging;           //for PixelFormat

/*
Start 啟動進程資源將其與process類關聯

Kill立即關閉進程

waitforExit 在等待關聯進程的退出

Close 釋放與此關聯的所有進程 
*/

namespace vcs_Process1
{
    public partial class Form1 : Form
    {
        Process myProcess = new Process();
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
            x_st = 10;
            y_st = 10;
            dx = 150 + 10;
            dy = 60 + 10;

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

            groupBox1.Size = new Size(180, 200);
            dy = 60;
            groupBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_system0.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 10);
            bt_system1.Location = new Point(x_st + dx * 0, y_st + dy * 1 + 10);
            bt_system2.Location = new Point(x_st + dx * 0, y_st + dy * 2 + 10);

            richTextBox1.Size = new Size(360, 700);
            richTextBox1.Location = new Point(x_st + dx * 5 + 30, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1230, 760);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得所有程序\n";
            Process[] processes = Process.GetProcesses(); //取得所有程序
            richTextBox1.Text += "系統中有： " + processes.Length.ToString() + " 個程序\n\n";

            richTextBox1.Text += "僅列出 有視窗 的Process\n\n";

            foreach (Process process in processes)
            {
                //richTextBox1.Text += "A\t" + process.ProcessName + "\t";
                if (process.MainWindowTitle.Length > 0)
                {
                    //僅列出 有視窗 的Process
                    richTextBox1.Text += "處理序的名稱 :\t" + process.ProcessName.ToString().Trim() + "\n";//取得處理序的名稱
                    richTextBox1.Text += "主視窗標題 :\t" + process.MainWindowTitle + "\n";   //取得處理序的主視窗標題
                    richTextBox1.Text += "處理序啟動的時間 :\t" + process.StartTime.ToString() + "\n";   //取得處理序的主視窗標題
                    richTextBox1.Text += "這個處理序的總處理器時間 :\t" + process.TotalProcessorTime.ToString() + "\n";   //取得處理序的主視窗標題

                    richTextBox1.Text += "\n";
                }
                else
                {
                    //richTextBox1.Text += "取得 無視窗 的Process : " + process.ProcessName.ToString().Trim() + "\n";
                }
            }

            richTextBox1.Text += "\n\n\n";

            int length = processes.Length;
            for (int index = 0; index < length; index++)
            {
                if (processes[index].MainWindowTitle.Length > 0)
                {
                    richTextBox1.Text += String.Format("Name: {0} \tID: {1}", processes[index].ProcessName, processes[index].Id) + "\n\n";
                }
            }

            richTextBox1.Text += "\n\n\n";
            richTextBox1.Text += "獲取系統進程的用戶名\n";
            foreach (Process p in Process.GetProcesses())
            {
                //Console.Write(p.ProcessName);
                //Console.Write("----");
                //Console.WriteLine(GetProcessUserName(p.Id));

                richTextBox1.Text += p.ProcessName + "\t" + GetProcessUserName(p.Id) + "\n";
            }

            richTextBox1.Text += "\n\n\n";
            richTextBox1.Text += "取得所有程序\n";

            //取得本機端上執行中的應用程式
            //[C#]取得本機端上，執行中有 GUI 介面的應用程式
            //Environment.MachineName 屬性 : 取得這個本機電腦的 NetBIOS 名稱。
            //Process.GetProcesses 方法 (String) : 為指定電腦上的每個處理序資源建立新的 Process 元件。
            //Process.MainWindowHandle 屬性 : 取得相關處理序主視窗的視窗控制代碼。
            foreach (Process process in Process.GetProcesses(Environment.MachineName))
            {
                if (process.MainWindowHandle != IntPtr.Zero)  // 判斷 MainWindowHandle 為非零值的應用程式，表示有主視窗
                {
                    //listBox1.Items.Add(process.ToString());
                    richTextBox1.Text += process.ToString() + "\n";
                }
            }

            richTextBox1.Text += "取得所有程序\n";

            // 列出系統中所有的程序
            //Process[] processes2 = Process.GetProcesses(Environment.MachineName);   //相同
            Process[] processes2 = Process.GetProcesses();   //取得所有程序
            richTextBox1.Text += "系統中有： " + processes2.Length.ToString() + " 個程序\n";

            foreach (Process process in processes2)
            {
                /*
                // 因為使用 Idle 的 StartTime 會造成錯誤，因此先排除。對其他程序取時間也會造成錯誤，故不用。
                if (!process.ProcessName.Equals("Idle"))
                {
                    // 顯示程序的名稱及啟動時間
                    richTextBox1.Text += process.ProcessName + "\t\t" + process.StartTime.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
                }
                else
                {
                    richTextBox1.Text += process.ProcessName + "\t\t" + "xxxxxxxxxxxxxxxx\n";
                }
                */

                richTextBox1.Text += process.ProcessName + "\n";
            }


        }

        private void button1_Click(object sender, EventArgs e)
        {
            //偵測程式執行時的記憶體用量

            // Define variables to track the peak memory usage of the process. 
            long peakPagedMem = 0;
            long peakWorkingSet = 0;
            long peakVirtualMem = 0;

            Process myProcess = null;

            try
            {
                // Start the process.
                myProcess = Process.Start("NotePad.exe");

                // Display the process statistics until the user closes the program. 
                do
                {
                    if (!myProcess.HasExited)
                    {
                        // Refresh the current process property values.
                        myProcess.Refresh();

                        Console.WriteLine();

                        // Display current process statistics.

                        Console.WriteLine("{0} -", myProcess.ToString());
                        Console.WriteLine("-------------------------------------");
                        Console.WriteLine("  physical memory usage: {0}", myProcess.WorkingSet64);
                        Console.WriteLine("  base priority: {0}", myProcess.BasePriority);
                        Console.WriteLine("  priority class: {0}", myProcess.PriorityClass);
                        Console.WriteLine("  user processor time: {0}", myProcess.UserProcessorTime);
                        Console.WriteLine("  privileged processor time: {0}", myProcess.PrivilegedProcessorTime);
                        Console.WriteLine("  total processor time: {0}", myProcess.TotalProcessorTime);
                        Console.WriteLine("  PagedSystemMemorySize64: {0}", myProcess.PagedSystemMemorySize64);
                        Console.WriteLine("  PagedMemorySize64: {0}", myProcess.PagedMemorySize64);

                        // Update the values for the overall peak memory statistics.
                        peakPagedMem = myProcess.PeakPagedMemorySize64;
                        peakVirtualMem = myProcess.PeakVirtualMemorySize64;
                        peakWorkingSet = myProcess.PeakWorkingSet64;

                        if (myProcess.Responding)
                        {
                            Console.WriteLine("Status = Running");
                        }
                        else
                        {
                            Console.WriteLine("Status = Not Responding");
                        }
                    }
                }
                while (!myProcess.WaitForExit(1000));

                Console.WriteLine();
                Console.WriteLine("Process exit code: {0}", myProcess.ExitCode);

                // Display peak memory statistics for the process.
                Console.WriteLine("Peak physical memory usage of the process: {0}", peakWorkingSet);
                Console.WriteLine("Peak paged memory usage of the process: {0}", peakPagedMem);
                Console.WriteLine("Peak virtual memory usage of the process: {0}", peakVirtualMem);
            }
            finally
            {
                if (myProcess != null)
                {
                    myProcess.Close();
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            return;

            //應該是要指名關閉哪個程式
            if ((myProcess != null) && (!myProcess.HasExited))
            {
                myProcess.Kill();
            }
            else
            {
                richTextBox1.Text += " already killed ";
            }
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
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //當前進程資料

            uint uiPid = (uint)Process.GetCurrentProcess().Id;  // 當前進程 ID
            richTextBox1.Text += "aaaaa0 :" + uiPid.ToString() + "\n";
            richTextBox1.Text += "aaaaa3 :" + Process.GetCurrentProcess().MainWindowTitle + "\n";   //取得處理序的主視窗標題
            richTextBox1.Text += "aaaaa6 :" + Process.GetCurrentProcess().SessionId + "\n";
            richTextBox1.Text += "aaaaa9 :" + Process.GetCurrentProcess().StartTime.ToString() + "\n";
        }

        private static string GetProcessUserName(int pID)
        {
            string text1 = null;
            SelectQuery query1 = new SelectQuery("Select * from Win32_Process WHERE processID=" + pID);
            ManagementObjectSearcher searcher1 = new ManagementObjectSearcher(query1);
            try
            {
                foreach (ManagementObject disk in searcher1.Get())
                {
                    ManagementBaseObject inPar = null;
                    ManagementBaseObject outPar = null;
                    inPar = disk.GetMethodParameters("GetOwner");
                    outPar = disk.InvokeMethod("GetOwner", inPar, null);
                    text1 = outPar["User"].ToString();
                    break;
                }
            }
            catch
            {
                text1 = "SYSTEM";
            }
            return text1;
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得所有程序\n";
            //C# 指定程序還原與置於前景視窗 
            // 取得目前電腦的處理程序
            richTextBox1.Text += "找到 " + Process.GetProcesses().Length + " 個程序\n\n";
            foreach (Process pTarget in Process.GetProcesses()) //取得所有程序
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
            //在c#中，如果啟動了外部程序，一般也可以通過退出碼來確認程序的運行狀態：

            Process process = Process.Start(@"C:\_git\vcs\_2.vcs\ims\imsLink\bin\Debug\imsLink.exe");

            process.WaitForExit();
            if (process.ExitCode == 0)
            {
                //richTextBox1.Text += "11111111111111111111\n";
            }
            else
            {
                //richTextBox1.Text += "222222222222222222222\n";
            }
            richTextBox1.Text += "退出碼 : " + process.ExitCode.ToString() + "\n";
            richTextBox1.Text += "退出時間 : " + process.ExitTime + "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得所有程序\n";
            //Process[] processes = Process.GetProcesses(Environment.MachineName);   //相同
            Process[] processes = Process.GetProcesses();   //取得所有程序
            richTextBox1.Text += "系統中有： " + processes.Length.ToString() + " 個程序\n";

            foreach (Process process in processes)
            {
                /*
                // 因為使用 Idle 的 StartTime 會造成錯誤，因此先排除。對其他程序取時間也會造成錯誤，故不用。
                if (!process.ProcessName.Equals("Idle"))
                {
                    // 顯示程序的名稱及啟動時間
                    richTextBox1.Text += process.ProcessName + "\t\t" + process.StartTime.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
                }
                else
                {
                    richTextBox1.Text += process.ProcessName + "\t\t" + "xxxxxxxxxxxxxxxx\n";
                }
                */

                //取得特定應用程式的資訊
                //richTextBox1.Text += process.ProcessName + "\n";
                if (process.ProcessName == "putty")
                {
                    richTextBox1.Text += process.ProcessName + "\n";
                    SetForegroundWindow(process.MainWindowHandle);
                    ShowWindow(process.MainWindowHandle, 1);
                    richTextBox1.Text += "time = " + process.StartTime.ToString() + "\n";
                    Rect rect = new Rect();
                    GetWindowRect(process.MainWindowHandle, ref rect);
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

        private void button19_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開啟檔案總管 給定參數";
            richTextBox1.Text += "開啟檔案總管 開啟路徑在D槽";
            //  C:\Windows\explorer.exe /n,/e,D:\

            //呼叫外部程式 並帶有參數的用法
            Process process = new Process();
            process.StartInfo.FileName = @"C:\Windows\explorer.exe";    //設定要啟動的程式
            process.StartInfo.Arguments = @"/n,/e,D:\";
            process.Start();
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
            richTextBox1.Text += "取得所有程序\n";
            //Process 測試

            //取出名字裡有特定字樣的process
            Process[] processes = Process.GetProcessesByName("firefox");
            richTextBox1.Text += "系統中有： " + processes.Length.ToString() + " 個程序\n";

            //取出所有的process
            //Process[] processes = Process.GetProcesses(); //取得所有程序
            foreach (Process process in processes)
            {
                //process.Kill(); 指名刪除這個process
                richTextBox1.Text += process.ProcessName + "\n";
            }

            /*
            //列出firefox的Process
            Process[] processes = Process.GetProcessesByName("firefox");
            foreach (Process process in processes)
            {
                richTextBox1.Text += String.Format("{0} \tID:{1}", process.ProcessName, process.Id) + "\n";
            }
            */
        }

        private void button24_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得所有程序\n";
            Process[] processes = Process.GetProcesses();    //取得所有程序
            richTextBox1.Text += "系統中有： " + processes.Length.ToString() + " 個程序\n";

            foreach (Process process in processes)
            {
                //process.Kill(); //關閉所有進程.
                //process.ProcessName; //進程名
                Console.Write(process.ToString());
            }
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
            string process_name = "ACDSee32";

            richTextBox1.Text += "尋找並殺死process : " + process_name + "\n";
            //string process_name = "TabTip";
            KillProcess(process_name);
        }

        //C#殺死進程
        private void KillProcess(string processName)
        {
            //得到所有打開的進程
            try
            {
                //foreach (Process processes in Process.GetProcesses())  //取得所有程序
                foreach (Process process in Process.GetProcessesByName(processName))   //指明特定名稱的程序
                {
                    richTextBox1.Text += "get process : " + process.ProcessName + "\n";
                    if (!process.CloseMainWindow())
                    {
                        //process.Kill();
                        richTextBox1.Text += "殺死進程 : " + processName + "\n";
                    }
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //使用Process類調用外部exe程序

            Process process = Process.Start("notepad.exe");
            process.WaitForExit();//關鍵，等待外部程序退出後才能往下執行
        }

        private void button30_Click(object sender, EventArgs e)
        {
            //Process 測試 from M$
            // Get the current process.
            Process currentProcess = Process.GetCurrentProcess();

            // Get all processes running on the local computer.
            richTextBox1.Text += "取得所有程序\n";
            Process[] localAll = Process.GetProcesses();    //取得所有程序

            // Get all instances of Notepad running on the local computer.
            // This will return an empty array if notepad isn't running.
            Process[] localByName = Process.GetProcessesByName("notepad");

            // Get a process on the local computer, using the process id.
            // This will throw an exception if there is no such process.
            //Process localById = Process.GetProcessById(5);

            // Get processes running on a remote computer. Note that this
            // and all the following calls will timeout and throw an exception
            // if "myComputer" and 169.0.0.0 do not exist on your local network.

            // Get all processes on a remote computer.
            //Process[] remoteAll = Process.GetProcesses("myComputer");

            // Get all instances of Notepad running on the specific computer, using machine name.
            //Process[] remoteByName = Process.GetProcessesByName("notepad", "myComputer");

            // Get all instances of Notepad running on the specific computer, using IP address.
            //Process[] ipByName = Process.GetProcessesByName("notepad", "169.0.0.0");

            // Get a process on a remote computer, using the process id and machine name.
            //Process remoteById = Process.GetProcessById(2345, "myComputer");

        }

        private void button31_Click(object sender, EventArgs e)
        {
            //Process 測試

            //進程, 我們可以把計算機中每一個運行的應用程序當作是一個進程

            ///獲得當前程序中正在運行的進程
            richTextBox1.Text += "取得所有程序\n";
            Process[] processes = Process.GetProcesses();    //取得所有程序
            richTextBox1.Text += "系統中有： " + processes.Length.ToString() + " 個程序\n";

            foreach (Process process in processes)
            {
                //item.Kill(); //關閉所有進程.　　　　//item.ProcessName; //進程名
                //Console.Write(item.ToString());
                richTextBox1.Text += "取得目前Process : " + process.ToString() + "\n";
            }
        }

        private void button32_Click(object sender, EventArgs e)
        {
            //檢查本程式是否已在執行中
            Process[] processes = Process.GetProcessesByName(Application.CompanyName);
            richTextBox1.Text += "系統中有： " + processes.Length.ToString() + " 個程序\n";

            if (processes.Length > 1)
            {
                richTextBox1.Text += "本程式已在執行中\n";
                MessageBox.Show("應用程序已經在運行中。");
                //Thread.Sleep(1000);
                //System.Environment.Exit(1);
            }
            else
            {
                richTextBox1.Text += "本程式尚未被其他執行\n";
                //Application.EnableVisualStyles();
                //Application.SetCompatibleTextRenderingDefault(false);
                //Application.Run(new Form1());
            }
        }

        private void button33_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
        {
        }

        private void button35_Click(object sender, EventArgs e)
        {
            //取得系統處理器數目
            int cnt = Environment.ProcessorCount;
            richTextBox1.Text += "cnt = " + cnt.ToString() + "\n";

            //通過C#還可以指定當前線程的運行在哪個CPU上。

            Process process = Process.GetCurrentProcess();
            process.ProcessorAffinity = (IntPtr)0x0001;

            //Process.ProcessorAffinity 設置當前CPU的屏蔽字，0x0001表示選用一號CPU，0x0002表示選用2號CPU。


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

        }

        private void bt_system0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "(偽)關機\n";
            //Process.Start("shutdown", "-s -t 0");
        }

        private void bt_system1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "(偽)註銷\n";
            //Process.Start("shutdown", "-l ");
        }

        private void bt_system2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "(偽)重啟\n";
            //Process.Start("shutdown", "-r -t 0");
        }
    }
}
