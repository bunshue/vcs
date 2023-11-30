using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for Process

namespace vcs_Process5
{
    public partial class Form1 : Form
    {
        bool flag_keep_program_running = true;

        string program_name = "AMCAP";
        string program_path = @"C:\Program Files (x86)\Noel Danjou\AMCap\AMCap.exe";

        //string program_name = "MegaDownloader";
        //string program_path = @"C:\____backup\MegaDownloaderNoinstall_1.8_azo\MegaDownloaderNoinstall\MegaDownloader.exe";

        bool flag_program_running = false;

        private Process[] processes;
        bool flag_EnableRaisingEvents = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //C# 跨 Thread 存取 UI
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效

            if (flag_keep_program_running == true)
                richTextBox1.Text += "維持程式運行模式\n";
            else
                richTextBox1.Text += "監控模式\n";

            label1.Text = "偵測程式 : " + program_name;
            richTextBox1.Text += "偵測程式 : " + program_name + " 開始, 時間 : " + DateTime.Now.ToString() + "\n";
        }

        private void process_exited(object sender, EventArgs e)//被觸發的程序
        {
            richTextBox1.Text += "偵測到程式 " + program_name + " 被關閉, 時間 : " + DateTime.Now.ToString() + "\n";

            flag_EnableRaisingEvents = false;
            flag_program_running = false;
        }

        int program_executed_time = 1;
        int count = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            if (flag_keep_program_running == true)
            {
                if (flag_program_running == true)
                {
                    //richTextBox1.Text += "O";
                }
                else
                {
                    //richTextBox1.Text += "X";
                    count++;
                    if (count == 120)
                    {
                        count = 0;
                        richTextBox1.Text += "\n已100秒 開啟\n";

                        //開啟imsLink
                        Process process = new Process();    //創建一個進程用於調用外部程序
                        process = Process.Start(program_path);
                    }
                }
            }

            processes = Process.GetProcessesByName(program_name);//需要監控的程序名，該方法帶出該程序所有用到的進程
            foreach (Process process in processes)
            {
                //richTextBox1.Text += process.ProcessName + "\r\n";
                if (flag_EnableRaisingEvents == false)
                {
                    if (process.ProcessName.ToLower() == program_name.ToLower())
                    {
                        flag_EnableRaisingEvents = true;
                        richTextBox1.Text += "\n第 " + (program_executed_time++).ToString() + " 次偵測到程式 " + program_name + " 被開啟, 時間 : " + DateTime.Now.ToString() + "\n";
                        process.EnableRaisingEvents = true;//設置進程終止時觸發的時間
                        process.Exited += new EventHandler(process_exited);//發現外部程序關閉即觸發方法process_exited
                        flag_program_running = true;
                    }
                }
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
