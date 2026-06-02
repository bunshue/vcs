using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for File
using System.Diagnostics;  // for Process
using System.Threading;
using System.Runtime.InteropServices;  // for DllImport
using System.Text.RegularExpressions;
using System.Drawing.Imaging;  // for PixelFormat

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
        Process process = new Process();    //創建一個進程用於調用外部程序
        int cnt = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //監控外部程序運行狀態 ST
            //C# 跨 Thread 存取 UI
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效

            if (flag_keep_program_running == true)
            {
                richTextBox2.Text += "維持程式運行模式\n";
            }
            else
            {
                richTextBox2.Text += "監控模式\n";
            }
            lb_monitor_process.Text = "偵測程式 : " + program_name;
            richTextBox2.Text += "偵測程式 : " + program_name + " 開始, 時間 : " + DateTime.Now.ToString() + "\n";
            //監控外部程序運行狀態 SP

            //------------------------------------------------------------  # 60個

            list_all_processes();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
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

            label1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_kill_process.Location = new Point(x_st + dx * 6 - 80, y_st + dy * 0 - 10);
            listBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0 + 40);
            listBox1.Size = new Size(410, 360);

            richTextBox1.Size = new Size(360, 690);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            lb_monitor_process.Text = "監控外部程序運行狀態";
            lb_monitor_process.Location = new Point(x_st + dx * 4, y_st + dy * 7 - 26);
            richTextBox2.Size = new Size(190, 200);
            richTextBox2.Location = new Point(x_st + dx * 4, y_st + dy * 7);

            this.Size = new Size(1650, 750);
            this.Text = "vcs_Process1";

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

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            int length = processes.Length;
            for (int index = 0; index < length; index++)
            {
                if (processes[index].MainWindowTitle.Length > 0)
                {
                    richTextBox1.Text += String.Format("Name: {0} \tID: {1}", processes[index].ProcessName, processes[index].Id) + "\n\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
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

            Process process = new Process();    //創建一個進程用於調用外部程序

            try
            {
                //啟動程式
                process = Process.Start("NotePad.exe");

                // Display the process statistics until the user closes the program. 
                do
                {
                    if (!process.HasExited)
                    {
                        // Refresh the current process property values.
                        process.Refresh();

                        Console.WriteLine();

                        // Display current process statistics.

                        Console.WriteLine("{0} -", process.ToString());
                        Console.WriteLine("-------------------------------------");
                        Console.WriteLine("  physical memory usage: {0}", process.WorkingSet64);
                        Console.WriteLine("  base priority: {0}", process.BasePriority);
                        Console.WriteLine("  priority class: {0}", process.PriorityClass);
                        Console.WriteLine("  user processor time: {0}", process.UserProcessorTime);
                        Console.WriteLine("  privileged processor time: {0}", process.PrivilegedProcessorTime);
                        Console.WriteLine("  total processor time: {0}", process.TotalProcessorTime);
                        Console.WriteLine("  PagedSystemMemorySize64: {0}", process.PagedSystemMemorySize64);
                        Console.WriteLine("  PagedMemorySize64: {0}", process.PagedMemorySize64);

                        // Update the values for the overall peak memory statistics.
                        peakPagedMem = process.PeakPagedMemorySize64;
                        peakVirtualMem = process.PeakVirtualMemorySize64;
                        peakWorkingSet = process.PeakWorkingSet64;

                        if (process.Responding)
                        {
                            Console.WriteLine("Status = Running");
                        }
                        else
                        {
                            Console.WriteLine("Status = Not Responding");
                        }
                    }
                }
                while (!process.WaitForExit(1000));

                Console.WriteLine();
                Console.WriteLine("Process exit code: {0}", process.ExitCode);

                // Display peak memory statistics for the process.
                Console.WriteLine("Peak physical memory usage of the process: {0}", peakWorkingSet);
                Console.WriteLine("Peak paged memory usage of the process: {0}", peakPagedMem);
                Console.WriteLine("Peak virtual memory usage of the process: {0}", peakVirtualMem);
            }
            finally
            {
                if (process != null)
                {
                    process.Close();
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            return;

            //應該是要指名關閉哪個程式
            if ((process != null) && (!process.HasExited))
            {
                process.Kill();
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
            // 取得目前電腦的處理程序
            // 進程, 我們可以把計算機中每一個運行的應用程序當作是一個進程
            // 獲得當前程序中正在運行的進程

            richTextBox1.Text += "取得所有程序\n";
            Process[] AllProcesses = Process.GetProcesses();  // 取得所有程序
            richTextBox1.Text += "進程數 : " + AllProcesses.Length.ToString() + "\n";

            //比對電腦的處理程序, 指定程序還原與置於前景視窗 
            foreach (Process p in AllProcesses)  // 取得所有程序
            {
                //richTextBox1.Text += "找到 " + p.ProcessName + "\n";  // 進程名
                if (p.ProcessName == "ACDSee32")  // 取得處理序名稱並與指定程序名稱比較
                {
                    richTextBox1.Text += "\t你開啟了ACDSee32，移到前台。\n";
                    HandleRunningInstance(p);
                }
                //p.Kill(); //關閉所有進程.
            }

            //------------------------------------------------------------  # 60個

            //列出firefox的Process
            //取出名字裡有特定字樣的process
            Process[] processes = Process.GetProcessesByName("firefox");
            richTextBox1.Text += "系統中有： " + processes.Length.ToString() + " 個程序\n";

            //取出所有的process
            //Process[] processes = Process.GetProcesses(); //取得所有程序
            foreach (Process process in processes)
            {
                //process.Kill(); 指名刪除這個process
                richTextBox1.Text += process.ProcessName + "\n";
                richTextBox1.Text += String.Format("{0} \tID:{1}", process.ProcessName, process.Id) + "\n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //Process.Start()

            //開啟檔案總管 給定參數

            richTextBox1.Text += "開啟檔案總管 給定參數";
            richTextBox1.Text += "開啟檔案總管 開啟路徑在D槽";
            //  C:\Windows\explorer.exe /n,/e,D:\

            //呼叫外部程式 並帶有參數的用法
            Process process = new Process();
            process.StartInfo.FileName = @"C:\Windows\explorer.exe";    //設定要啟動的程式
            process.StartInfo.Arguments = @"/n,/e,D:\";
            process.Start();

            //------------------------------------------------------------  # 60個

            //使用Process類調用外部exe程序

            //Process process = Process.Start("notepad.exe");
            //process.WaitForExit();//關鍵，等待外部程序退出後才能往下執行


            //------------------------------------------------------------  # 60個

            /*
richTextBox1.Text += "開啟 系統資訊 設定\n";
Process.Start("MSINFO32.EXE");

richTextBox1.Text += "開啟 顯示器 設定\n";
Process.Start("desk.cpl");
*/
            richTextBox1.Text += "開啟 滑鼠 設定\n";
            //Process.Start("main.cpl");

            richTextBox1.Text += "開啟 網路連線 設定\n";
            //Process.Start("ncpa.cpl");

            richTextBox1.Text += "開啟 聲音 設定\n";
            //Process.Start("mmsys.cpl");

            richTextBox1.Text += "開啟 寄信程式\n";
            //Process.Start("mailto:david@insighteyes.com");

            //NG
            //Process.Start(Environment.SystemDirectory + "/osk.exe");
            //NG
            //Process.Start("osk.exe");

            richTextBox1.Text += "開啟 控制台\n";
            //Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL");

            richTextBox1.Text += "用預設程式開啟檔案\n";
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            //Process.Start("explorer.exe", filename);

            richTextBox1.Text += "開啟 小畫家\n";
            //Process.Start("mspaint.exe");

            richTextBox1.Text += "開啟 WordPad\n";
            //Process.Start("write.exe");

            richTextBox1.Text += "開啟 Windows Media Player\n";
            //Process.Start("dvdplay.exe");

            richTextBox1.Text += "開啟 Windows 版本宣告\n";
            //Process.Start("winver.exe");

            richTextBox1.Text += "開啟 CMD\n";
            //Process.Start("cmd.exe");

            richTextBox1.Text += "開啟 檔案總管 D槽\n";
            //Process.Start("d:");

            richTextBox1.Text += "開啟 登錄編輯程式 regedit\n";
            //Process.Start("regedit.exe");

            richTextBox1.Text += "開啟 Windows Media Player\n";
            //Process.Start("mplayer2.exe");

            richTextBox1.Text += "開啟 檔案總管\n";
            //Process.Start("explorer.exe");

            richTextBox1.Text += "開啟 工作管理員\n";
            //Process.Start("taskmgr.exe");

            richTextBox1.Text += "開啟 事件檢視器\n";
            //Process.Start("eventvwr.exe");

            //NG
            //Process.Start("winmsd.exe");

            //NG
            //Process.Start("ntbackup.exe");

            richTextBox1.Text += "開啟 Chrome 指定網頁\n";
            //filename = @"D:\_git\vcs\_1.data\_html\朱冶蕙老師的電腦教室.html";
            //Process.Start("chrome.exe", filename);

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //Process

            //test Process()
            //在cmd控制台輸入命令
            Process process = new Process();    //創建一個進程用於調用外部程序
            process.StartInfo.FileName = "cmd.exe";//設定要啟動的程式
            process.StartInfo.UseShellExecute = false;  // 是否指定操作系統外殼進程啟動程序
            process.StartInfo.RedirectStandardInput = true;//可能接受來自調用程序的輸入信息, 重定向標准輸入
            process.StartInfo.RedirectStandardOutput = true;//重定向標准輸出
            process.StartInfo.RedirectStandardError = true;//重定向錯誤輸出
            process.StartInfo.CreateNoWindow = true;  // 是否顯示程序視窗, true:不顯示, false:顯示
            process.Start();//啟動程序
            //process.StandardInput.WriteLine("net start mssqlserver");//輸入命令
            //process.StandardInput.WriteLine("exit");//一定要關閉。

            //------------------------------------------------------------  # 60個

            //取得系統處理器數目
            int cnt = Environment.ProcessorCount;
            richTextBox1.Text += "cnt = " + cnt.ToString() + "\n";

            //通過C#還可以指定當前線程的運行在哪個CPU上。

            //Process process = Process.GetCurrentProcess();
            //process.ProcessorAffinity = (IntPtr)0x0001;

            //Process.ProcessorAffinity 設置當前CPU的屏蔽字，0x0001表示選用一號CPU，0x0002表示選用2號CPU。

            //------------------------------------------------------------  # 60個

        }

        private void button8_Click(object sender, EventArgs e)
        {
            /*
            //C# 呼叫檔案總管開啟某個資料夾，並讓某個檔案或資料夾呈現反白的樣子
            string file = @"C:\Windows\explorer.exe";
            string argument = @"/select, " + foldername;
            Process.Start(file, argument);
            */

            Process.Start("IExplore.exe", "tw.yahoo.com");
            Process.Start("chrome.exe", "C:\\Read_Cht.htm");
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

        private void button11_Click(object sender, EventArgs e)
        {
            //取得目前的Process
            using (Process curProcess = Process.GetCurrentProcess())
            {
                richTextBox1.Text += "aaaa = " + curProcess.ProcessName + "\n";
                richTextBox1.Text += "aaaa = " + curProcess.MainModule + "\n";
                richTextBox1.Text += "aaaa = " + curProcess.MainWindowTitle + "\n";
                richTextBox1.Text += "aaaa = " + curProcess.ProcessorAffinity + "\n";
                richTextBox1.Text += "處理序的名稱 :\t" + curProcess.ProcessName.ToString().Trim() + "\n";//取得處理序的名稱
                richTextBox1.Text += "主視窗標題 :\t" + curProcess.MainWindowTitle + "\n";   //取得處理序的主視窗標題
                richTextBox1.Text += "處理序啟動的時間 :\t" + curProcess.StartTime.ToString() + "\n";   //取得處理序的主視窗標題
                richTextBox1.Text += "這個處理序的總處理器時間 :\t" + curProcess.TotalProcessorTime.ToString() + "\n";   //取得處理序的主視窗標題

                //程序的退出
                //Process.GetCurrentProcess().Kill();
            }

            Process proc = Process.GetCurrentProcess();

            richTextBox1.Text += "aaa : " + proc.MinWorkingSet + " 拜\n";
            richTextBox1.Text += "bbb : " + proc.MaxWorkingSet + " 拜\n";
            richTextBox1.Text += "ccc : " + proc.NonpagedSystemMemorySize64 + " 拜\n";
            richTextBox1.Text += "ddd : " + proc.PagedMemorySize64 + " 拜\n";
            richTextBox1.Text += "eee : " + proc.PagedSystemMemorySize64 + " 拜\n";

            richTextBox1.Text += "aaa : " + proc.PeakPagedMemorySize64 + " 拜\n";
            richTextBox1.Text += "bbb : " + proc.PeakVirtualMemorySize64 + " 拜\n";
            richTextBox1.Text += "ccc : " + proc.PeakWorkingSet64 + " 拜\n";
            richTextBox1.Text += "ddd : " + proc.VirtualMemorySize64 + " 拜\n";
            richTextBox1.Text += "eee : " + proc.WorkingSet64 + " 拜\n";

            //取得記憶體使用狀態

            richTextBox1.Text += "Property\t\t\tValue\n";
            richTextBox1.Text += "Min Working Set" + "\t" + ((double)proc.MinWorkingSet).ToFileSize() + "\n";
            richTextBox1.Text += "Max Working Set" + "\t" + ((double)proc.MaxWorkingSet).ToFileSize() + "\n";
            richTextBox1.Text += "Non-paged Memory Size" + "\t" + ((double)proc.NonpagedSystemMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Paged Memory Size" + "\t" + ((double)proc.PagedMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Paged System Memory Size" + "\t" + ((double)proc.PagedSystemMemorySize64).ToFileSize() + "\n";

            richTextBox1.Text += "Peak Paged Memory Size" + "\t" + ((double)proc.PeakPagedMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Peak Virtual Memory Size" + "\t" + ((double)proc.PeakVirtualMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Peak Working Set" + "\t" + ((double)proc.PeakWorkingSet64).ToFileSize() + "\n";
            richTextBox1.Text += "Virtual Memory Size" + "\t" + ((double)proc.VirtualMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Working Set" + "\t" + ((double)proc.WorkingSet64).ToFileSize() + "\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //關機/註銷/重啟

            richTextBox1.Text += "(偽)關機\n";
            //Process.Start("shutdown", "-s -t 0");

            richTextBox1.Text += "(偽)註銷\n";
            //Process.Start("shutdown", "-l ");

            richTextBox1.Text += "(偽)重啟\n";
            //Process.Start("shutdown", "-r -t 0");
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

            Process process = Process.Start(@"D:\_git\ims1\iMS_Link\iMS_Link\bin\Debug\iMS_Link.exe");

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
            //用WordPad編輯rtf檔
            // Allow the user to edit the file with WordPad.

            string rtf_filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_rtf\text.rtf";

            // Hide.
            this.ShowInTaskbar = false;
            this.Hide();

            // We will open rtf_filename with wordpad.exe.
            ProcessStartInfo start_info = new ProcessStartInfo("wordpad.exe", rtf_filename);
            start_info.WindowStyle = ProcessWindowStyle.Maximized;

            // Open wordpad.
            Process process = new Process();
            process.StartInfo = start_info;
            process.Start();

            // Wait for wordpad to finish.
            process.WaitForExit();

            // Unhide.
            this.ShowInTaskbar = true;
            this.Show();
        }

        private void button34_Click(object sender, EventArgs e)
        {
            //開啟記事本
            Process process1 = new Process();
            process1.StartInfo.UseShellExecute = false;
            process1.StartInfo.FileName = "notepad";
            process1.StartInfo.CreateNoWindow = true;
            process1.Start();

            int process_id = process1.Id;
            richTextBox1.Text += process_id.ToString() + "\n";

            //3030

            Process localById = Process.GetProcessById(process_id);
            richTextBox1.Text += "電腦名稱：" + localById.MachineName + Environment.NewLine + "處理序名稱：" + localById.ProcessName + "\n";

            Process currentProcess = Process.GetCurrentProcess();
            MessageBox.Show("電腦名稱：" + currentProcess.MachineName + Environment.NewLine + "處理序名稱：" + currentProcess.ProcessName);
        }

        private void button35_Click(object sender, EventArgs e)
        {
            Process process1 = Process.Start("Notepad.exe");
            for (int i = 0; i < 5; i++)
            {
                if (!process1.HasExited)
                {
                    process1.Refresh();
                    richTextBox1.Text += "實體記憶體的耗用： " + process1.WorkingSet64.ToString() + "\n";
                    process1.WaitForExit(3000);
                }
                else
                {
                    break;
                }
            }
            process1.CloseMainWindow();
            richTextBox1.Text += "執行了CloseMainWindow()方法\n";

            process1.Close();
            richTextBox1.Text += "執行了Close()方法\n";
        }

        private void button36_Click(object sender, EventArgs e)
        {
            // 先執行 記事本，這樣才看得到效果

            //單一程式的記憶體資訊
            Process[] localByName = Process.GetProcessesByName("notepad");
            foreach (Process p in localByName)
            {
                richTextBox1.Text += "名稱 : " + p.ProcessName + "\n";
                richTextBox1.Text += "識別項 : " + p.Id.ToString() + "\n";
                richTextBox1.Text += "私有記憶體 : " + (p.PrivateMemorySize64 / 1024) + "Kbyte\n";
                richTextBox1.Text += "虛擬記憶體 : " + (p.VirtualMemorySize64 / 1024) + "byte\n";
            }

            //所有程式的記憶體資訊
            foreach (Process p in Process.GetProcesses())
            {
                richTextBox1.Text += "名稱 : " + p.ProcessName + "\n";
                richTextBox1.Text += "識別項 : " + p.Id.ToString() + "\n";
                richTextBox1.Text += "私有記憶體 : " + (p.PrivateMemorySize64 / 1024) + "Kbyte\n";
                richTextBox1.Text += "虛擬記憶體 : " + (p.VirtualMemorySize64 / 1024) + "byte\n";
            }
        }

        private void button37_Click(object sender, EventArgs e)
        {
            //test
            string fileName = @"D:\_git\vcs\_1.data\______test_files1\__RW\_word\bmp_format.docx";
            ProcessStartInfo startInfo = new ProcessStartInfo(fileName);

            if (File.Exists(fileName))
            {
                int i = 0;
                foreach (String verb in startInfo.Verbs)
                {
                    listBox1.Items.Add(string.Format("  {0}. {1}", i.ToString(), verb));
                    i++;
                }
            }
            else
            {
            }
        }

        private void button38_Click(object sender, EventArgs e)
        {

        }

        private void button39_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        void list_all_processes()
        {
            listBox1.Items.Clear();

            richTextBox1.Text += "取得所有程序\n";
            Process[] processes = Process.GetProcesses(); //取得所有程序
            richTextBox1.Text += "系統中有： " + processes.Length.ToString() + " 個程序\n";

            foreach (Process process in processes)
            {
                //richTextBox1.Text += "A\t" + process.ProcessName + "\t";
                if (process.MainWindowTitle.Length > 0)
                {
                    //僅列出 有視窗 的Process
                    listBox1.Items.Add(process.ProcessName.ToString().Trim());
                    richTextBox1.Text += "取得 有視窗 的Process : " + process.ProcessName.ToString().Trim() + "\n";
                }
                else
                {
                    //richTextBox1.Text += "取得 無視窗 的Process : " + process.ProcessName.ToString().Trim() + "\n";
                }
            }
        }

        private void bt_kill_process_Click(object sender, EventArgs e)
        {
            //關閉外部已開啟的程序

            if (listBox1.SelectedItem == null)
                return;
            richTextBox1.Text += "欲關閉程序名稱 : " + listBox1.SelectedItem.ToString().Trim() + "\n";
            Process[] processes = Process.GetProcessesByName(listBox1.SelectedItem.ToString().Trim());
            foreach (Process process in processes)
            {
                process.CloseMainWindow();
            }
            listBox1.Items.Remove(listBox1.SelectedItem);//從listBox1中移除listBox1中選定的項

            richTextBox1.Text += "程序已關閉\n";
        }

        //------------------------------------------------------------  # 60個

        //監控外部程序運行狀態 ST

        bool flag_keep_program_running = true;
        string program_name = "AMCAP";
        string program_path = @"C:\Program Files (x86)\Noel Danjou\AMCap\AMCap.exe";

        //string program_name = "MegaDownloader";
        //string program_path = @"C:\____backup\MegaDownloaderNoinstall_1.8_azo\MegaDownloaderNoinstall\MegaDownloader.exe";

        bool flag_program_running = false;

        private Process[] processes;
        bool flag_EnableRaisingEvents = false;

        int program_executed_time = 1;
        int count = 0;
        private void timer_monitor_process_Tick(object sender, EventArgs e)
        {
            richTextBox2.Text += "A ";
            if (flag_keep_program_running == true)
            {
                if (flag_program_running == true)
                {
                    //richTextBox2.Text += "O";
                }
                else
                {
                    //richTextBox2.Text += "X";
                    count++;
                    if (count == 120)
                    {
                        count = 0;
                        richTextBox2.Text += "\n已100秒 開啟\n";

                        //開啟imsLink
                        Process process = new Process();    //創建一個進程用於調用外部程序
                        process = Process.Start(program_path);
                    }
                }
            }

            processes = Process.GetProcessesByName(program_name);//需要監控的程序名，該方法帶出該程序所有用到的進程
            foreach (Process process in processes)
            {
                //richTextBox2.Text += process.ProcessName + "\r\n";
                if (flag_EnableRaisingEvents == false)
                {
                    if (process.ProcessName.ToLower() == program_name.ToLower())
                    {
                        flag_EnableRaisingEvents = true;
                        richTextBox2.Text += "\n第 " + (program_executed_time++).ToString() + " 次偵測到程式 " + program_name + " 被開啟, 時間 : " + DateTime.Now.ToString() + "\n";
                        process.EnableRaisingEvents = true;//設置進程終止時觸發的時間
                        process.Exited += new EventHandler(process_exited);//發現外部程序關閉即觸發方法process_exited
                        flag_program_running = true;
                    }
                }
            }
        }

        private void process_exited(object sender, EventArgs e)//被觸發的程序
        {
            richTextBox2.Text += "偵測到程式 " + program_name + " 被關閉, 時間 : " + DateTime.Now.ToString() + "\n";

            flag_EnableRaisingEvents = false;
            flag_program_running = false;
        }
        //監控外部程序運行狀態 SP
    }

    public static class MyExtensions
    {
        [DllImport("Shlwapi.dll", CharSet = CharSet.Auto)]
        public static extern Int32 StrFormatByteSize(
            long fileSize,
            [MarshalAs(UnmanagedType.LPTStr)] StringBuilder buffer,
            int bufferSize);

        // Return a file size created by the StrFormatByteSize API function.
        public static string ToFileSizeApi(this long file_size)
        {
            StringBuilder sb = new StringBuilder(20);
            StrFormatByteSize(file_size, sb, 20);
            return sb.ToString();
        }

        // Return a string describing the value as a file size.
        // For example, 1.23 MB.
        public static string ToFileSize(this double value)
        {
            string[] suffixes = { "bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB" };
            for (int i = 0; i < suffixes.Length; i++)
            {
                if (value <= (Math.Pow(1024, i + 1)))
                {
                    return ThreeNonZeroDigits(value / Math.Pow(1024, i)) + " " + suffixes[i];
                }
            }

            return ThreeNonZeroDigits(value / Math.Pow(1024, suffixes.Length - 1)) +
                " " + suffixes[suffixes.Length - 1];
        }

        // Return the value formatted to include at most three
        // non-zero digits and at most two digits after the
        // decimal point. Examples:
        //         1
        //       123
        //        12.3
        //         1.23
        //         0.12
        private static string ThreeNonZeroDigits(double value)
        {
            if (value >= 100)
            {
                // No digits after the decimal.
                return value.ToString("0,0");
            }
            else if (value >= 10)
            {
                // One digit after the decimal.
                return value.ToString("0.0");
            }
            else
            {
                // Two digits after the decimal.
                return value.ToString("0.00");
            }
        }
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

        //獲取窗體的進程標識ID
        public static int GetPid(string windowTitle)
        {
            int rs = 0;
            Process[] arrayProcess = Process.GetProcesses();
            foreach (Process p in arrayProcess)
            {
                if (p.MainWindowTitle.IndexOf(windowTitle) != -1)
                {
                    rs = p.Id;
                    break;
                }
            }
            return rs;
        }

//------------------------------------------------------------  # 60個

        //根據進程名獲取PID
        public static int GetPidByProcessName(string processName, ref IntPtr baseAddress)
        {
            Process[] arrayProcess = Process.GetProcessesByName(processName);
            foreach (Process p in arrayProcess)
            {
                baseAddress = p.MainModule.BaseAddress;
                return p.Id;
            }

            return 0;
        }

        //根據進程名獲取PID
        public static int GetPidByProcessName(string processName)
        {
            Process[] arrayProcess = Process.GetProcessesByName(processName);
            foreach (Process p in arrayProcess)
            {
                return p.Id;
            }

            return 0;
        }
*/






/*
C#調用默認浏覽器打開網頁的幾種方法

方法一：從注冊表中讀取默認浏覽器可執行文件路徑

        private void button1_Click(object sender, EventArgs e)
        {
            //從注冊表中讀取默認浏覽器可執行文件路徑
            RegistryKey key = Registry.ClassesRoot.OpenSubKey(@httpshellopencommand);
            string s = key.GetValue().ToString();

            //s就是你的默認浏覽器，不過後面帶了參數，把它截去，不過需要注意的是：不同的浏覽器後面的參數不一樣！
            //D:Program Files (x86)GoogleChromeApplicationchrome.exe -- %1
            Process.Start(s.Substring(0, s.Length - 8), http://blog.csdn.net/testcs_dn);
        }
方法二：
        private void button2_Click(object sender, EventArgs e)
        {
            //調用系統默認的浏覽器 
            Process.Start(explorer.exe, http://blog.csdn.net/testcs_dn);
        }
方法三：
        private void button3_Click(object sender, EventArgs e)
        {
            //調用系統默認的浏覽器 
            Process.Start(http://blog.csdn.net/testcs_dn);
        }

方法四：調用IE浏覽器

從原理上來講，方法二和方法三應該是一樣的，不過方法三的代碼更短一點。 

//------------------------------------------------------------  # 60個

//打开注册表
string regeditstr = Environment.GetEnvironmentVariable("WinDir");//WinDir系统环境变量的名称
Process.Start(regeditstr + "\\regedit.exe");//打开注册表

//------------------------------------------------------------  # 60個


*/



