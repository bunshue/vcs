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

namespace vcs_Process
{
    public partial class Form1 : Form
    {
        Process myProcess;
        int cnt = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            myProcess = Process.Start(@"D:\___source_code\_git\part1\vcs\_2.vcs\ims\imsLink\bin\Debug\imsLink.exe");
            richTextBox1.Text += "ProcessName : " + myProcess.ProcessName + "\n";
            richTextBox1.Text += "SessionId : " + myProcess.SessionId.ToString() + "\n";
            richTextBox1.Text += "StartTime : " + myProcess.StartTime + "\n";
            richTextBox1.Text += "Id : " + myProcess.Id.ToString() + "\n";

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
                using (Process myProcess = Process.Start("Notepad.exe"))
                {
                    // Display physical memory usage 5 times at intervals of 2 seconds.
                    for (int i = 0; i < 10; i++)
                    {
                        if (!myProcess.HasExited)
                        {
                            // Discard cached information about the process.
                            myProcess.Refresh();
                            // Print working set to console.
                            //Console.WriteLine($"Physical Memory Usage: {myProcess.WorkingSet}");
                            richTextBox1.Text += "Physical Memory Usage: " + myProcess.WorkingSet64.ToString() + "\n";
                            //label1.Text = myProcess.WorkingSet64.ToString();
                            // Wait 2 seconds.
                            Thread.Sleep(2000);
                        }
                        else
                        {
                            break;
                        }
                    }

                    // Close process by sending a close message to its main window.
                    myProcess.CloseMainWindow();
                    // Free resources associated with process.
                    myProcess.Close();
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
            Process.Start("IExplore.exe", "www.google.com.tw");
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
                using (Process myProcess = new Process())
                {
                    myProcess.StartInfo.UseShellExecute = false;
                    // You can start any process, HelloWorld is a do-nothing example.
                    myProcess.StartInfo.FileName = @"D:\___source_code\_git\part1\vcs\_2.vcs\ims\imsLink\bin\Debug\imsLink.exe";
                    myProcess.StartInfo.CreateNoWindow = true;
                    myProcess.Start();
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
            //System.Diagnostics.Process.Start("" + System.Environment.SystemDirectory + "/osk.exe");

            //開啟特定程式
            //Process.Start(@"C:\___small\imagesweeper5.1影像清潔工.exe");

            //開啟計算機程式
            //Process.Start(@"C:\WINDOWS\system32\calc.exe");

            //開啟檔案 由預設程式開啟
            //System.Diagnostics.Process.Start("C:\\______test_files\\my_text_file.txt");

            //開啟記事本程式
            //System.Diagnostics.Process.Start("notepad.exe");

            //開啟程式
            //System.Diagnostics.Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL");
            System.Diagnostics.Process.Start("winver.exe ");              //--打开Windows版本信息

            //開啟imsLink
            //System.Diagnostics.Process.Start(@"D:\___source_code\_git\part1\vcs\_2.vcs\ims\imsLink\bin\Debug\imsLink.exe");

        }

        private void button10_Click(object sender, EventArgs e)
        {
            System.Diagnostics.ProcessStartInfo processStartInfo = new System.Diagnostics.ProcessStartInfo();
            processStartInfo.FileName = "explorer.exe";  //资源管理器
            processStartInfo.Arguments = @"C:\";
            System.Diagnostics.Process.Start(processStartInfo);

        }

        private void button11_Click(object sender, EventArgs e)
        {
            //開啟檔案總管
            String pathname = "C:\\";
            System.Diagnostics.Process.Start(pathname);
            /*
            if (Directory.Exists(this.FolderPath))
            {
                System.Diagnostics.Process.Start(this.FolderPath);
                return true;
            }
            else
                return false;
             */

        }

        private void button12_Click(object sender, EventArgs e)
        {
            //用預設的程式開啟檔案
            String pathname = "C:\\______test_files\\aaaaaaa.txt";

            if (File.Exists(pathname) == false)
            {
                MessageBox.Show("檔案: " + pathname + "不存在，無法開啟。\n");
                return;
            }
            else
                System.Diagnostics.Process.Start(pathname);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //列出正在執行的任務
            richTextBox1.Text = string.Empty;
            Process[] myProcesses = Process.GetProcesses();
            foreach (Process myProcess in myProcesses)
            {
                if (myProcess.MainWindowTitle.Length > 0)
                    richTextBox1.Text += "任務名： " + myProcess.MainWindowTitle + "\n";
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
            foreach (Process p in Process.GetProcesses(System.Environment.MachineName))
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
            //Process[] processes = Process.GetProcesses(System.Environment.MachineName);   //相同
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
        [DllImport("User32.dll")]
        private static extern bool ShowWindowAsync(IntPtr hWnd, int cmdShow);
        [DllImport("User32.dll")]
        private static extern bool SetForegroundWindow(IntPtr hWnd);
        private const int WS_SHOWNORMAL = 1;
        public static void HandleRunningInstance(Process instance)
        {
            // 相同時透過ShowWindowAsync還原，以及SetForegroundWindow將程式至於前景
            ShowWindowAsync(instance.MainWindowHandle, WS_SHOWNORMAL);
            SetForegroundWindow(instance.MainWindowHandle);
            //Environment.SpecialFolder.
        }




    }
}
