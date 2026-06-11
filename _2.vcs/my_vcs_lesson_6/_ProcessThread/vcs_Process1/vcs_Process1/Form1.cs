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
waitforExit 在等待關聯進程的退出   // 會等到這個程式結束為止
Close 釋放與此關聯的所有進程 
*/

/*
Process 的方法
Process.Start()  // 啟動程式
Process.GetCurrentProcess()  // 取得目前的process
Process.GetProcesses()  // 取得所有程序
Process.GetProcessesByName()  // 根據[process名稱]取得process
Process.GetProcessById()  // 根據[process id]取得process
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

            process = Process.Start("NotePad.exe");  // 啟動程式

            //------------------------------------------------------------  # 60個

            //監控外部程序運行狀態 ST
            //C# 跨 Thread 存取 UI
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效

            if (flag_keep_program_running == true)
            {
                richTextBox2.Text += "\n維持程式運行模式\n";
            }
            else
            {
                richTextBox2.Text += "\n監控模式\n";
            }
            lb_monitor_process.Text = "偵測程式 : " + program_name;
            richTextBox2.Text += "偵測程式 : " + program_name + " 開始, 時間 : " + DateTime.Now.ToString() + "\n";
            //監控外部程序運行狀態 SP

            //------------------------------------------------------------  # 60個

            listView2.View = View.Details;  //定義列表顯示的方式
            listView2.FullRowSelect = true; //整行一起選取
            listView2.GridLines = true;  // 顯示格線
            listView2.Columns.Add("PID", 150, HorizontalAlignment.Left);
            listView2.Columns.Add("名稱", 250, HorizontalAlignment.Left);

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

            label1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_list_process.Location = new Point(x_st + dx * 5 - 80 - 80 - 80, y_st + dy * 0 - 10);
            bt_open_process.Location = new Point(x_st + dx * 5 - 80 - 80, y_st + dy * 0 - 10);
            bt_kill_process.Location = new Point(x_st + dx * 5 - 80, y_st + dy * 0 - 10);
            listView2.Size = new Size(410, 300);
            listView2.Location = new Point(x_st + dx * 3, y_st + dy * 0 + 40);

            listView1.Size = new Size(560, 290);
            listView1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            richTextBox1.Size = new Size(560, 690 - 300);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0 + 300);
            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear1.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear1.Size.Height);

            lb_monitor_process.Text = "監控外部程序運行狀態";
            lb_monitor_process.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            richTextBox2.Size = new Size(410, 310);
            richTextBox2.Location = new Point(x_st + dx * 3, y_st + dy * 5 + 30);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear2.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear2.Size.Height);

            this.Size = new Size(1650, 750);
            this.Text = "vcs_Process1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得所有程序\n";

            Process[] processes = Process.GetProcesses();  // 取得所有程序
            foreach (Process process in processes)
            {
                // 取得處理序的主視窗標題
                if (process.MainWindowTitle.Length > 0)
                {
                    //僅列出 有視窗 的Process
                    richTextBox1.Text += "處理序的名稱 :\t" + process.ProcessName.ToString().Trim() + "\n";//取得處理序的名稱
                    richTextBox1.Text += "主視窗標題 :\t" + process.MainWindowTitle + "\n";  // 取得處理序的主視窗標題
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

            //Process[]
            processes = Process.GetProcesses(Environment.MachineName);  // 取得所有程序
            foreach (Process process in processes)
            {
                if (process.MainWindowHandle != IntPtr.Zero)  // 判斷 MainWindowHandle 為非零值的應用程式，表示有主視窗
                {
                    richTextBox1.Text += process.ToString() + "\n";
                }
            }

            richTextBox1.Text += "取得所有程序\n";

            // 列出系統中所有的程序
            //Process[] processes = Process.GetProcesses(Environment.MachineName);   //相同
            //Process[]
            processes = Process.GetProcesses();  // 取得所有程序
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

                richTextBox1.Text += process.ProcessName + "\n";
            }

            //------------------------------------------------------------  # 60個

            //取得目前的進程數
            // 取得目前電腦的處理程序
            // 進程, 我們可以把計算機中每一個運行的應用程序當作是一個進程
            // 獲得當前程序中正在運行的進程

            richTextBox1.Text += "取得所有程序\n";
            //Process[]
            processes = Process.GetProcesses();  // 取得所有程序
            richTextBox1.Text += "系統中有 : " + processes.Length.ToString() + " 個程序\n";

            //比對電腦的處理程序, 指定程序還原與置於前景視窗 
            foreach (Process process in processes)  // 取得所有程序
            {
                //richTextBox1.Text += "找到 " + process.ProcessName + "\n";  // 進程名
                if (process.ProcessName == "ACDSee32")  // 取得處理序名稱並與指定程序名稱比較
                {
                    richTextBox1.Text += "\t你開啟了ACDSee32，移到前台。\n";
                    HandleRunningInstance(process);
                }
                //process.Kill();  // 指名刪除這個process
            }

            //------------------------------------------------------------  # 60個

            //取得特定應用程式的資訊
            richTextBox1.Text += "取得所有程序\n";
            //Process[] processes = Process.GetProcesses(Environment.MachineName);   //相同
            //Process[]
            processes = Process.GetProcesses();  // 取得所有程序
            richTextBox1.Text += "系統中有 : " + processes.Length.ToString() + " 個程序\n";

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

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {

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
            {
                using (Process process = Process.Start("Notepad.exe"))  // 啟動程式
                {
                    // Display physical memory usage 5 times at intervals of 2 seconds.
                    for (int i = 0; i < 10; i++)
                    {
                        if (!process.HasExited)
                        {
                            // Discard cached information about the process.
                            process.Refresh();
                            richTextBox1.Text += "Physical Memory Usage : " + process.WorkingSet64.ToString() + "\n";
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
            //使用Process的StartInfo

            //開啟記事本
            Process process = new Process();
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.FileName = "notepad";
            process.StartInfo.CreateNoWindow = true;  // 是否顯示程序視窗, true:不顯示, false:顯示
            process.Start();  // 啟動程式

            int process_id = process.Id;  // 進程ID
            richTextBox1.Text += process_id.ToString() + "\n";

            //Process
            process = Process.GetProcessById(process_id);  // 根據[process id]取得process
            richTextBox1.Text += "處理序名稱 : " + process.ProcessName + "\n";

            //6060

            string exe_filename = "notepad.exe";
            //Process
            process = new Process();    //創建一個進程用於調用外部程序
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

        private void button6_Click(object sender, EventArgs e)
        {
            //Process.Start()  // 啟動程式

            //開啟檔案總管 給定參數

            richTextBox1.Text += "開啟檔案總管 給定參數";
            richTextBox1.Text += "開啟檔案總管 開啟路徑在D槽";
            //  C:\Windows\explorer.exe /n,/e,D:\

            //呼叫外部程式 並帶有參數的用法
            Process process = new Process();
            process.StartInfo.FileName = @"C:\Windows\explorer.exe";    //設定要啟動的程式
            process.StartInfo.Arguments = @"/n,/e,D:\";
            process.Start();  // 啟動程式

            //------------------------------------------------------------  # 60個

            //使用Process類調用外部exe程序

            //Process process = Process.Start("notepad.exe");  // 啟動程式
            //process.WaitForExit();  // 會等到這個程式結束為止

            //------------------------------------------------------------  # 60個

            /*
            richTextBox1.Text += "開啟 Chrome 指定網頁\n";
            //filename = @"D:\_git\vcs\_1.data\_html\朱冶蕙老師的電腦教室.html";
            //Process.Start("chrome.exe", filename);

            //------------------------------------------------------------  # 60個

            //開啟各種程式
            Process.Start("Firefox.exe");

            //開啟特定程式 1
            Process.Start(@"C:\___small\imagesweeper5.1影像清潔工.exe");

            //Process.Start()  // 啟動程式

            /*
            //C# 呼叫檔案總管開啟某個資料夾，並讓某個檔案或資料夾呈現反白的樣子
            string file = @"C:\Windows\explorer.exe";
            string argument = @"/select, " + foldername;
            Process.Start(file, argument);
            */

            Process.Start("IExplore.exe", "tw.yahoo.com");  // 啟動程式 + 參數
            Process.Start("chrome.exe", "C:\\Read_Cht.htm");  // 啟動程式 + 參數

            //開啟IE, 指名網址
            //Process.Start("IExplore.exe", "www.google.com.tw");   //same
            Process.Start("iexplore.exe", "www.google.com.tw");

            //開啟FireFox, 指名網址
            Process.Start("Firefox.exe", "www.google.com.tw");

            //用Adobe開啟pdf檔案
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_pdf\note_Linux_workstation.pdf";
            //Process
            process = new Process();    //創建一個進程用於調用外部程序
            process = Process.Start(filename);
            process.WaitForExit();  //需等開啟的程式結束後才可以回到表單

            //開啟檔案總管, C槽
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

        private void button7_Click(object sender, EventArgs e)
        {
            //Process

            //test Process()
            //在cmd控制台輸入命令
            Process process = new Process();    //創建一個進程用於調用外部程序
            process.StartInfo.FileName = "cmd.exe";//設定要啟動的程式
            process.StartInfo.UseShellExecute = false;  // 是否指定操作系統外殼進程啟動程序
            process.StartInfo.RedirectStandardInput = true;  // 重定向標準輸入, 可能接受來自調用程序的輸入信息
            process.StartInfo.RedirectStandardOutput = true;  // 重定向標準輸出, 由調用程序獲取輸出信息
            process.StartInfo.RedirectStandardError = true;  // 重定向錯誤輸出
            process.StartInfo.CreateNoWindow = true;  // 是否顯示程序視窗, true:不顯示, false:顯示
            process.Start();  // 啟動程式
            //process.StandardInput.WriteLine("net start mssqlserver");//輸入命令
            //process.StandardInput.WriteLine("exit");//一定要關閉。

            //------------------------------------------------------------  # 60個

            //取得系統處理器數目
            int cnt = Environment.ProcessorCount;
            richTextBox1.Text += "cnt = " + cnt.ToString() + "\n";

            //通過C#還可以指定當前線程的運行在哪個CPU上。
            //Process process = Process.GetCurrentProcess();  // 取得目前的process
            //process.ProcessorAffinity = (IntPtr)0x0001;
            //Process.ProcessorAffinity 設置當前CPU的屏蔽字，0x0001表示選用一號CPU，0x0002表示選用2號CPU。

            //------------------------------------------------------------  # 60個

        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
        {
            //打開Windows小程式/註冊表/控制面板

            //calc

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

            richTextBox1.Text += "開啟 系統資訊 設定\n";
            Process.Start("MSINFO32.EXE");

            richTextBox1.Text += "開啟 顯示器 設定\n";
            Process.Start("desk.cpl");

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

            //------------------------------------------------------------  # 60個

            //關機/註銷/重啟

            richTextBox1.Text += "(偽)關機\n";
            //Process.Start("shutdown", "-s -t 0");

            richTextBox1.Text += "(偽)註銷\n";
            //Process.Start("shutdown", "-l ");

            richTextBox1.Text += "(偽)重啟\n";
            //Process.Start("shutdown", "-r -t 0");

            //------------------------------------------------------------  # 60個

            //打開註冊表
            Process.Start("regedit.exe");

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

        private void button10_Click(object sender, EventArgs e)
        {
            //取得Process資訊
            //1. 當前進程資料, 取得目前的Process
            //Process process = Process.GetCurrentProcess();  // 取得目前的process
            //show_process_info(process);

            //------------------------------  # 30個

            /*
            //2. 單一程式的記憶體資訊, 記事本
            Process[] processes = Process.GetProcessesByName("NotePad");  // 根據[process名稱]取得process
            foreach (Process process in processes)
            {
                show_process_info(process);
            }

            //------------------------------  # 30個

            //3. 所有的Process
            Process[] processes = Process.GetProcesses();  // 取得所有程序
            foreach (Process process in processes)
            {
                show_process_info(process);
            }
            */

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "偵測程式執行時的記憶體用量\n";

            // Define variables to track the peak memory usage of the process. 
            long peakPagedMem = 0;
            long peakWorkingSet = 0;
            long peakVirtualMem = 0;

            if (!process.HasExited)
            {
                richTextBox1.Text += "此程式的PID : " + process.Id.ToString() + "\n";

                // Refresh the current process property values.
                process.Refresh();

                // Display current process statistics.

                richTextBox1.Text += process.ToString() + "\n";

                //------------------------------  # 30個

                richTextBox1.Text += "physical memory usage : " + process.WorkingSet64 + "\n";
                richTextBox1.Text += "base priority : " + process.BasePriority + "\n";
                richTextBox1.Text += "priority class : " + process.PriorityClass + "\n";
                richTextBox1.Text += "user processor time : " + process.UserProcessorTime + "\n";
                richTextBox1.Text += "privileged processor time : " + process.PrivilegedProcessorTime + "\n";
                richTextBox1.Text += "total processor time : " + process.TotalProcessorTime + "\n";
                richTextBox1.Text += "PagedSystemMemorySize64 : " + process.PagedSystemMemorySize64 + "\n";
                richTextBox1.Text += "PagedMemorySize64 : " + process.PagedMemorySize64 + "\n";

                // Update the values for the overall peak memory statistics.
                peakPagedMem = process.PeakPagedMemorySize64;
                peakVirtualMem = process.PeakVirtualMemorySize64;
                peakWorkingSet = process.PeakWorkingSet64;

                if (process.Responding)  // 使用者介面是否正在回應
                {
                    richTextBox1.Text += "Status = Running\n";
                }
                else
                {
                    richTextBox1.Text += "Status = Not Responding\n";
                }
            }
            else
            {

                richTextBox1.Text += "程式已結束, 退出碼 : " + process.ExitCode + "\n";
                richTextBox1.Text += "退出時間 : " + process.ExitTime + "\n";
            }

            // Display peak memory statistics for the process.
            richTextBox1.Text += "Peak physical memory usage of the process : " + peakWorkingSet + "\n";
            richTextBox1.Text += "Peak paged memory usage of the process : " + peakPagedMem + "\n";
            richTextBox1.Text += "Peak virtual memory usage of the process : " + peakVirtualMem + "\n";
        }

        void show_process_info(Process process)
        {
            richTextBox1.Text += "MainModule : " + process.MainModule + "\n";
            richTextBox1.Text += "ProcessorAffinity : " + process.ProcessorAffinity + "\n";
            richTextBox1.Text += "處理序名稱 : " + process.ProcessName + "\n";
            richTextBox1.Text += "處理序名稱 : " + process.ProcessName.ToString().Trim() + "\n";//取得處理序的名稱
            richTextBox1.Text += "這個處理序的總處理器時間 : " + process.TotalProcessorTime.ToString() + "\n";
            richTextBox1.Text += "當前進程 ID : " + process.Id.ToString() + "\n";
            richTextBox1.Text += "當前進程 主視窗標題 : " + process.MainWindowTitle + "\n";  // 取得處理序的主視窗標題
            richTextBox1.Text += "當前進程 SessionId : " + process.SessionId + "\n";
            richTextBox1.Text += "當前進程 啟動時間 : " + process.StartTime.ToString() + "\n";
            richTextBox1.Text += "電腦名稱 : " + process.MachineName + "\n";

            richTextBox1.Text += "取得記憶體使用狀態\n";
            richTextBox1.Text += "Min Working Set : " + ((double)process.MinWorkingSet).ToFileSize() + "\n";
            richTextBox1.Text += "Max Working Set : " + ((double)process.MaxWorkingSet).ToFileSize() + "\n";
            richTextBox1.Text += "Non-paged Memory Size : " + ((double)process.NonpagedSystemMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Paged Memory Size : " + ((double)process.PagedMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Paged System Memory Size : " + ((double)process.PagedSystemMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Peak Paged Memory Size : " + ((double)process.PeakPagedMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Peak Virtual Memory Size : " + ((double)process.PeakVirtualMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Peak Working Set : " + ((double)process.PeakWorkingSet64).ToFileSize() + "\n";
            richTextBox1.Text += "Virtual Memory Size : " + ((double)process.VirtualMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Working Set : " + ((double)process.WorkingSet64).ToFileSize() + "\n";

            // 記憶體部分
            // 取得工作集 (Working Set) 記憶體大小，單位是位元組
            //WorkingSet64 → 目前占用的實體記憶體 (RAM)。
            //PrivateMemorySize64 → 只屬於此程式的記憶體大小。
            //PagedMemorySize64 → 已分頁到虛擬記憶體的大小。
            //PrivateMemorySize64	程式獨佔的記憶體，不含共用 DLL	Private Working Set	工作管理員「記憶體」欄位通常顯示這個數字。

            richTextBox1.Text += "名稱 : " + process.ProcessName + "\n";
            richTextBox1.Text += "識別項 : " + process.Id.ToString() + "\n";
            richTextBox1.Text += "私有記憶體 : " + (process.PrivateMemorySize64 / 1024) + " Kbyte\n";
            richTextBox1.Text += "虛擬記憶體 : " + (process.VirtualMemorySize64 / 1024) + " Kbyte\n";

            richTextBox1.Text += "程式目前使用記憶體 WorkingSet64 : " + (process.WorkingSet64 / 1024.0 / 1024.0).ToString("F2") + " MB\n";
            richTextBox1.Text += "程式目前使用記憶體 PrivateMemorySize64 : " + (process.PrivateMemorySize64 / 1024.0 / 1024.0).ToString("F2") + " MB\n";
            richTextBox1.Text += "程式目前使用記憶體 PagedMemorySize64 : " + (process.PagedMemorySize64 / 1024.0 / 1024.0).ToString("F2") + " MB\n";
        }

        //------------------------------------------------------------  # 60個

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
            Process process = Process.Start("Notepad.exe");  // 啟動程式

            for (int i = 0; i < 5; i++)
            {
                if (!process.HasExited)
                {
                    process.Refresh();
                    richTextBox1.Text += "實體記憶體的耗用 : " + process.WorkingSet64.ToString() + "\n";
                    process.WaitForExit(3000);  // 等待3秒鐘
                }
                else
                {
                    break;
                }
            }
            process.CloseMainWindow();
            richTextBox1.Text += "執行了CloseMainWindow()方法\n";

            process.Close();
            richTextBox1.Text += "執行了Close()方法\n";

            //------------------------------------------------------------  # 60個

            /*
            //開啟Notepad程序
            Process process1 = new Process();
            process1.StartInfo.FileName = "notepad.exe";
            process1.Start();

            //關閉Notepad程序
            Process[] processes = Process.GetProcessesByName("Notepad");
            foreach (Process process in processes)
            {
                process.CloseMainWindow();
                process.WaitForExit(3000);
                process.Close();
            }
            */
        }

        //------------------------------------------------------------  # 60個

        private void button14_Click(object sender, EventArgs e)
        {
            //取得Process資訊

            //當前進程資料, 取得目前的Process
            Process current_process = Process.GetCurrentProcess();  // 取得目前的process

            //------------------------------------------------------------  # 60個

            //獲取窗體的進程標識ID
            string windowTitle = "Google";
            int rs = 0;
            Process[] processes = Process.GetProcesses();  // 取得所有程序
            foreach (Process process in processes)
            {
                // 取得處理序的主視窗標題
                if (process.MainWindowTitle.Length > 0)
                {
                    //richTextBox1.Text += "\n有窗體程序 : " + process.ProcessName + ", 窗體名稱 : " + process.MainWindowTitle + "\n";
                }
                else
                {
                    //richTextBox1.Text += "X ";

                }

                // 取得處理序的主視窗標題
                if (process.MainWindowTitle.IndexOf(windowTitle) != -1)
                {
                    richTextBox1.Text += "aaaaaaaaaaaaaaaaaaaaaaaaaaa\n";
                    rs = process.Id;

                    richTextBox1.Text += "取得 name : " + process.ProcessName + "\n";
                    richTextBox1.Text += "取得 id : " + process.Id + "\n";

                    break;
                }
            }
            richTextBox1.Text += "取得 process ID : " + rs.ToString() + "\n";

            //------------------------------------------------------------  # 60個

            //取出所有的process
            //Process[] processes = Process.GetProcesses();  // 取得所有程序

            //取出名字裡有特定字樣的process, "VCSExpress"
            //Process[]
            processes = Process.GetProcessesByName("VCSExpress");  // 根據[process名稱]取得process
            richTextBox1.Text += "系統中有 : " + processes.Length.ToString() + " 個程序\n";

            foreach (Process process in processes)
            {
                richTextBox1.Text += "ProcessName : " + process.ProcessName + "\n";
                richTextBox1.Text += "Id : " + process.Id + "\n";

                IntPtr baseAddress = process.MainModule.BaseAddress;
                richTextBox1.Text += "BaseAddress : " + baseAddress.ToString() + "\n";
            }

            //------------------------------------------------------------  # 60個

            //準備加入

            //程序的退出
            //process.Kill();  // 指名刪除這個process

            /*
            //關閉程式
            //應該是要指名關閉哪個程式
            if ((process != null) && (!process.HasExited))
            {
                process.Kill();  // 指名刪除這個process
            }
            else
            {
                richTextBox1.Text += " already killed ";
            }
            */

            //------------------------------------------------------------  # 60個

            string process_name = "ACDSee32";
            richTextBox1.Text += "尋找並殺死process : " + process_name + "\n";
            //string process_name = "TabTip";
            //KillProcess(process_name);
        }

        //尋找並殺死進程
        private void KillProcess(string processName)
        {
            //得到所有打開的進程
            try
            {
                Process[] processes = Process.GetProcessesByName(processName);  // 根據[process名稱]取得process
                foreach (Process process in processes)
                {
                    richTextBox1.Text += "get process : " + process.ProcessName + "\n";
                    if (!process.CloseMainWindow())
                    {
                        //process.Kill();  // 指名刪除這個process
                        richTextBox1.Text += "殺死進程 : " + processName + "\n";
                    }
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {
            //如果啟動了外部程序，一般也可以通過退出碼來確認程序的運行狀態

            Process process = Process.Start(@"C:\_git\ims1\iMS_Link\iMS_Link\bin\Debug\iMS_Link.exe");

            process.WaitForExit();  // 會等到這個程式結束為止

            richTextBox1.Text += "退出碼 : " + process.ExitCode.ToString() + "\n";
            richTextBox1.Text += "退出時間 : " + process.ExitTime + "\n";

            //------------------------------------------------------------  # 60個

            //開啟imsLink
            //Process.Start(@"C:\_git\ims1\iMS_Link\iMS_Link\bin\Debug\iMS_Link.exe");

            //開啟imsLink
            //Process
            process = new Process();    //創建一個進程用於調用外部程序
            process = Process.Start(@"C:\_git\ims1\iMS_Link\iMS_Link\bin\Debug\iMS_Link.exe");

            richTextBox1.Text += "ProcessName : " + process.ProcessName + "\n";
            richTextBox1.Text += "SessionId : " + process.SessionId.ToString() + "\n";
            richTextBox1.Text += "StartTime : " + process.StartTime + "\n";
            richTextBox1.Text += "Id : " + process.Id.ToString() + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //ProcessStartInfo
            //Process

            /* 創建一個進程，並為進程傳入需要的參數
             * 或者說是啟動一個外部程序，並為其傳入參數
             * 等待退出或者強制關閉
             */

            //啟動一個外部程序
            //聲明一個程序信息類，指定啟動進程是的參數信息

            ProcessStartInfo psi1 = new ProcessStartInfo();
            //設置外部程序名
            psi1.FileName = "notepad.exe";
            //設置外部程序的啟動參數（命令行參數）為test.txt                   
            psi1.Arguments = "test.txt";
            //設置外部程序工作目錄為  D:\                   
            psi1.WorkingDirectory = "D:\\";
            //聲明一個程序類,也就是創建一個進程

            Process process;
            try
            {
                process = Process.Start(psi1);  // 啟動外部程序
            }
            catch (System.ComponentModel.Win32Exception ex)
            {
                richTextBox1.Text += "系統找不到指定的程序文件。\t" + ex + "\n";
                return;
            }

            richTextBox1.Text += "外部程序的開始執行時間 : " + process.StartTime + "\n";

            process.WaitForExit(3000);  // 等待3秒鐘

            //如果這個外部程序沒有結束運行則對其強行終止                   
            if (process.HasExited == false)
            {
                richTextBox1.Text += "由主程序強行終止外部程序的運行！\n";
                process.Kill();  // 指名刪除這個process
            }
            else
            {
                richTextBox1.Text += "由外部程序正常退出！\n";
            }
            richTextBox1.Text += "外部程序的結束運行時間 : " + process.ExitTime + "\n";
            richTextBox1.Text += "外部程序在結束運行時的返回值 : " + process.ExitCode + "\n";

            richTextBox1.Text += "退出碼 : " + process.ExitCode.ToString() + "\n";
            richTextBox1.Text += "退出時間 : " + process.ExitTime + "\n";

            //------------------------------------------------------------  # 60個

            //用WordPad編輯rtf檔
            // Allow the user to edit the file with WordPad.

            string rtf_filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_rtf\text.rtf";

            // Hide.
            this.ShowInTaskbar = false;
            this.Hide();

            // We will open rtf_filename with wordpad.exe.
            ProcessStartInfo psi2 = new ProcessStartInfo("wordpad.exe", rtf_filename);
            psi2.WindowStyle = ProcessWindowStyle.Maximized;

            // Open wordpad.
            process = new Process();
            process.StartInfo = psi2;
            process.Start();  // 啟動程式

            // Wait for wordpad to finish.
            process.WaitForExit();  // 會等到這個程式結束為止

            // Unhide.
            this.ShowInTaskbar = true;
            this.Show();

            //------------------------------------------------------------  # 60個

            string fileName = @"D:\_git\vcs\_1.data\______test_files1\__RW\_word\bmp_format.docx";
            ProcessStartInfo psi3 = new ProcessStartInfo(fileName);

            if (File.Exists(fileName))
            {
                foreach (String verb in psi3.Verbs)
                {
                    richTextBox1.Text += "取得 Verb : " + verb + "\n";
                }
            }
            else
            {
                richTextBox1.Text += "檔案不存在\n";
            }

            //------------------------------------------------------------  # 60個

            //在局域網內發送訊息
            //NG
            // send message to another computer
            // 在局域網內發送訊息
            // NG

            string strIP = "192.168.1.106";
            string strInfo = "send message to another computer";

            ProcessStartInfo psi4 = new ProcessStartInfo();
            psi4.FileName = @"cmd.exe";
            psi4.Arguments = @"/c net send " + strIP + " " + strInfo + "";
            psi4.WindowStyle = ProcessWindowStyle.Hidden;
            Process.Start(psi4);  // 啟動外部程序

            richTextBox1.Text += "done\n";

            //------------------------------------------------------------  # 60個

            //指定應用程式路徑
            string target = @"C:\Program Files\DAUM\PotPlayer\PotPlayerMini.exe";
            string all_filename = "aaaaaaaaaaaaaaa";
            ProcessStartInfo psi5 = new ProcessStartInfo(target);
            psi5.Arguments = all_filename;

            richTextBox1.Text += "target : " + target + "\n";
            richTextBox1.Text += "all_filename : " + all_filename + "\n";
            /*
            Process process = new Process();
            process.StartInfo = psi5;
            process.Start();  // 啟動程式
            */
            //------------------------------------------------------------  # 60個
        }

        private void button21_Click(object sender, EventArgs e)
        {
            // 不允許重複執行本程式 的作法
            // 在 Program.cs 裡面先檢查, 若 processes.Length > 1 , 即重複執行, 警示完離開程式

            string MName = Process.GetCurrentProcess().MainModule.ModuleName;
            string PName = Path.GetFileNameWithoutExtension(MName);

            richTextBox1.Text += "MName : " + MName + "\n";
            richTextBox1.Text += "PName : " + PName + "\n";

            Process[] processes = Process.GetProcessesByName(PName);

            richTextBox1.Text += "本程式執行次數 : " + processes.Length.ToString() + "\n";

            if (processes.Length > 1)
            {
                MessageBox.Show("不允許重複執行本程式", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
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

        //------------------------------------------------------------  # 60個

        private void button29_Click(object sender, EventArgs e)
        {
            //關閉所有記事本

        }

        //------------------------------------------------------------  # 60個

        void list_all_processes()
        {
            listView2.Items.Clear();

            richTextBox1.Text += "取得所有程序\n";
            Process[] processes = Process.GetProcesses();  // 取得所有程序
            richTextBox1.Text += "系統中有 : " + processes.Length.ToString() + " 個程序\n";

            foreach (Process process in processes)
            {
                // 取得處理序的主視窗標題
                if (process.MainWindowTitle.Length > 0)
                {
                    //僅列出 有視窗 的Process

                    //richTextBox1.Text += "取得 有視窗 的Process : " + process.Id.ToString() + "\n";
                    //richTextBox1.Text += "取得 有視窗 的Process : " + process.ProcessName.ToString().Trim() + "\n";

                    ListViewItem processItem = new ListViewItem(process.Id.ToString());//定義一個listView選擇項的實例
                    processItem.SubItems.Add(process.ProcessName.ToString().Trim());
                    listView2.Items.Add(processItem);//執行添加操作
                }
                else
                {
                    //richTextBox1.Text += "取得 無視窗 的Process : " + process.ProcessName.ToString().Trim() + "\n";
                }
            }
        }

        private void bt_list_process_Click(object sender, EventArgs e)
        {
            list_all_processes();

            //------------------------------------------------------------  # 60個

            getProcessInfo();
        }

        private void bt_open_process_Click(object sender, EventArgs e)
        {
            Process.Start("NotePad.exe");  // 啟動程式
        }

        private void bt_kill_process_Click(object sender, EventArgs e)
        {
            //關閉外部已開啟的程序

            //刪除資料
            int len = listView2.SelectedIndices.Count;
            if (len <= 0)  //總共選擇的個數
            {
                richTextBox1.Text += "未選擇要刪除的項目\n";
                return;
            }
            richTextBox1.Text += "共選擇 " + len.ToString() + " 個項目, 分別是\n";
            for (int i = (len - 1); i >= 0; i--)
            {
                int index = listView2.SelectedItems[i].Index;  // 取得欲刪除項目號

                richTextBox1.Text += "欲刪除項目號 : " + index.ToString() + "\n";
                richTextBox1.Text += "欲關閉程序ID : " + listView2.SelectedItems[i].SubItems[0].Text + "\n";
                richTextBox1.Text += "欲關閉程序名 : " + listView2.SelectedItems[i].SubItems[1].Text + "\n";

                /*
                //根據名稱刪除程序, 如果名稱相同就會一併被刪除
                Process[] processes = Process.GetProcessesByName(listView2.SelectedItems[i].SubItems[1].Text);  // 根據[process名稱]取得process
                foreach (Process process in processes)
                {
                    richTextBox1.Text += "取得程序名 : " + process.ProcessName + "\n";
                    richTextBox1.Text += "取得程序ID : " + process.Id + "\n";
                    process.CloseMainWindow();
                }
                */

                //------------------------------  # 30個

                //根據process id刪除程序, 就可以分開處理
                Process process = Process.GetProcessById(int.Parse(listView2.SelectedItems[i].SubItems[0].Text));  // 根據[process id]取得process
                richTextBox1.Text += "取得程序名 : " + process.ProcessName + "\n";
                richTextBox1.Text += "取得程序ID : " + process.Id + "\n";
                process.CloseMainWindow();

                //------------------------------  # 30個

                listView2.Items.RemoveAt(index);
                richTextBox1.Text += "程序已關閉\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void getProcessInfo()
        {
            richTextBox1.Text += "取得進程資訊\n";

            try
            {
                listView1.Items.Clear();
                Process[] processes = Process.GetProcesses(); //取得所有程序
                richTextBox1.Text += "系統中有： " + processes.Length.ToString() + " 個程序\n";

                string[] Minfo = new string[6];
                foreach (Process process in processes)
                {
                    Minfo[0] = process.ProcessName;
                    Minfo[1] = process.Id.ToString();
                    Minfo[2] = process.Threads.Count.ToString();
                    Minfo[3] = process.BasePriority.ToString();
                    Minfo[4] = Convert.ToString(process.WorkingSet64 / 1024) + "K";
                    Minfo[5] = Convert.ToString(process.VirtualMemorySize64 / 1024) + "K";
                    ListViewItem lvi = new ListViewItem(Minfo, "process");
                    listView1.Items.Add(lvi);
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息e01 : " + ex.Message + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        //監控外部程序運行狀態 ST

        bool flag_keep_program_running = true;
        //string program_name = "AMCAP";
        //string program_path = @"C:\Program Files (x86)\Noel Danjou\AMCap\AMCap.exe";
        //string program_name = "MegaDownloader";
        //string program_path = @"C:\____backup\MegaDownloaderNoinstall_1.8_azo\MegaDownloaderNoinstall\MegaDownloader.exe";
        string program_name = "notepad";
        string program_path = @"NotePad.exe";

        bool flag_program_running = false;

        private Process[] processes;
        bool flag_EnableRaisingEvents = false;

        int program_executed_time = 1;
        int count = 0;
        private void timer_monitor_process_Tick(object sender, EventArgs e)
        {
            richTextBox2.Text += ".";
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

                        // 啟動程式
                        Process process = new Process();  // 創建一個進程用於調用外部程序
                        process = Process.Start(program_path);  // 啟動程式
                    }
                }
            }

            processes = Process.GetProcessesByName(program_name);//需要監控的程序名，該方法帶出該程序所有用到的進程  // 根據[process名稱]取得process
            foreach (Process process in processes)
            {
                //richTextBox2.Text += process.ProcessName + "\r\n";
                if (flag_EnableRaisingEvents == false)
                {
                    if (process.ProcessName.ToLower() == program_name.ToLower())
                    {
                        flag_EnableRaisingEvents = true;
                        richTextBox2.Text += "\n第 " + (program_executed_time++).ToString() + " 次偵測到程式 : " + program_name + " 被開啟, 時間 : " + DateTime.Now.ToString() + "\n";
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

        //------------------------------------------------------------  # 60個

        private void 刷新ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "右鍵選單/刷新\n";
            getProcessInfo();
        }

        private void 結束進程ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "右鍵選單/結束進程\n";

            return;

            try
            {
                if (MessageBox.Show("警告:終止進程會導致不希望發生的結果，\r包括數據丟失和系統不穩定。在被終止前，\r進程將沒有機會保存其狀態和數據。確實\r想終止該進程嗎?", "任務管理器警告", MessageBoxButtons.YesNo, MessageBoxIcon.Exclamation) == DialogResult.Yes)
                {
                    string ProcessName = listView1.SelectedItems[0].Text;
                    Process[] processes = Process.GetProcessesByName(ProcessName);
                    processes[0].Kill();
                    getProcessInfo();
                }
                else
                { }
            }
            catch
            {
                string ProcessName = listView1.SelectedItems[0].Text;
                Process[] processes = Process.GetProcessesByName(ProcessName);

                Process process = new Process();
                //設定程序名
                process.StartInfo.FileName = "cmd.exe";
                //關閉Shell的使用
                process.StartInfo.UseShellExecute = false;
                //重定向標準輸入
                process.StartInfo.RedirectStandardInput = true;
                //重定向標準輸出
                process.StartInfo.RedirectStandardOutput = true;
                //重定向錯誤輸出
                process.StartInfo.RedirectStandardError = true;
                //設置不顯示窗口
                process.StartInfo.CreateNoWindow = true;
                //執行強制結束命令

                process.Start();
                process.StandardInput.WriteLine("ntsd -c q -p " + (processes[0].Id).ToString());
                process.StandardInput.WriteLine("Exit");
                getProcessInfo();
            }
        }

        private void SetBasePriority(int i)
        {
            richTextBox1.Text += "設定優先序 i = " + i.ToString() + "\n";

            return;

            string ProcessName = listView1.SelectedItems[0].Text;
            Process[] processes = Process.GetProcessesByName(ProcessName);
            switch (i)
            {
                case 0: processes[0].PriorityClass = ProcessPriorityClass.Idle; break;//低
                case 1: processes[0].PriorityClass = ProcessPriorityClass.Normal; break;//標準
                case 2: processes[0].PriorityClass = ProcessPriorityClass.High; break;//高
                case 3: processes[0].PriorityClass = ProcessPriorityClass.RealTime; break;//實時
                case 4: processes[0].PriorityClass = ProcessPriorityClass.AboveNormal; break;//高于標準
                case 5: processes[0].PriorityClass = ProcessPriorityClass.BelowNormal; break;//低于標準
            }
            getProcessInfo();
        }
        private void 實時ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "右鍵選單/設置優先級/實時\n";
            SetBasePriority(3);
        }

        private void 高ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "右鍵選單/設置優先級/高\n";
            SetBasePriority(2);
        }

        private void 高于標準ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "右鍵選單/設置優先級/高於標準\n";
            SetBasePriority(4);
        }

        private void 標準ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "右鍵選單/設置優先級/標準\n";
            SetBasePriority(1);
        }

        private void 低于標準ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "右鍵選單/設置優先級/低於標準\n";
            SetBasePriority(5);
        }

        private void 低ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "右鍵選單/設置優先級/低\n";
            SetBasePriority(0);
        }

        //------------------------------------------------------------  # 60個
    }

    //------------------------------------------------------------  # 60個

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

            return ThreeNonZeroDigits(value / Math.Pow(1024, suffixes.Length - 1)) + " " + suffixes[suffixes.Length - 1];
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

C#調用默認浏覽器打開網頁的幾種方法

方法一 : 從注冊表中讀取默認浏覽器可執行文件路徑

        private void button1_Click(object sender, EventArgs e)
        {
            //從注冊表中讀取默認浏覽器可執行文件路徑
            RegistryKey key = Registry.ClassesRoot.OpenSubKey(@httpshellopencommand);
            string s = key.GetValue().ToString();

            //s就是你的默認浏覽器，不過後面帶了參數，把它截去，不過需要注意的是 : 不同的浏覽器後面的參數不一樣！
            //D:Program Files (x86)GoogleChromeApplicationchrome.exe -- %1
            Process.Start(s.Substring(0, s.Length - 8), http://blog.csdn.net/testcs_dn);
        }
方法二 :
        private void button2_Click(object sender, EventArgs e)
        {
            //調用系統默認的浏覽器 
            Process.Start(explorer.exe, http://blog.csdn.net/testcs_dn);
        }
方法三 :
        private void button3_Click(object sender, EventArgs e)
        {
            //調用系統默認的浏覽器 
            Process.Start(http://blog.csdn.net/testcs_dn);
        }

方法四 : 調用IE浏覽器

從原理上來講，方法二和方法三應該是一樣的，不過方法三的代碼更短一點。 

//------------------------------------------------------------  # 60個

//打开注册表
string regeditstr = Environment.GetEnvironmentVariable("WinDir");//WinDir系统环境变量的名称
Process.Start(regeditstr + "\\regedit.exe");//打开注册表

//------------------------------------------------------------  # 60個

*/

//richTextBox1.Text += "本程式名稱 : " + Application.CompanyName + "\n";

            //Thread.Sleep(1000);
            //System.Environment.Exit(1);
            //Application.EnableVisualStyles();
            //Application.SetCompatibleTextRenderingDefault(false);
            //Application.Run(new Form1());

