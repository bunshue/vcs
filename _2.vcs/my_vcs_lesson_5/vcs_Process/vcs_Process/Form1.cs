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
    }
}
