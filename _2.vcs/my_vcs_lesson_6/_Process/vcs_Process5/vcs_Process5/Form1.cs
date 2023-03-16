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
        bool falg_keep_program_running = true;

        string program_name = "AMCAP";
        string program_path = @"C:\Program Files (x86)\Noel Danjou\AMCap\AMCap.exe";

        bool falg_program_running = false;

        private Process[] processes;
        bool flag_EnableRaisingEvents = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效

            richTextBox1.Text += "偵測程式 : " + program_name + "\n";
        }

        private void process_exited(object sender, EventArgs e)//被觸發的程序
        {
            richTextBox1.Text += "偵測到程式 " + program_name + " 被關閉, 時間 : " + DateTime.Now.ToString() + "\n";

            flag_EnableRaisingEvents = false;
            falg_program_running = false;
        }

        int count = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            if (falg_keep_program_running == true)
            {
                if (falg_program_running == true)
                {
                    //richTextBox1.Text += "O";
                }
                else
                {
                    //richTextBox1.Text += "X";
                    count++;
                    if (count == 100)
                    {
                        count = 0;
                        richTextBox1.Text += "已100秒 開啟\n";

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
                        richTextBox1.Text += "偵測到程式 " + program_name + " 被開啟, 時間 : " + DateTime.Now.ToString() + "\n";
                        process.EnableRaisingEvents = true;//設置進程終止時觸發的時間
                        process.Exited += new EventHandler(process_exited);//發現外部程序關閉即觸發方法process_exited
                        falg_program_running = true;
                    }
                }
            }
        }
    }
}
