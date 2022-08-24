using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
//using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.Sockets; //ServerSocket = new Socket(...)時使用
using System.Threading;  //Thread時使用
using System.Text;       //Encoding.Unicode.GetString(...) 時使用
using System.IO;         //使用FileInfo類別，來建立一個檔案實體物件
using System.Diagnostics;

namespace vcs_Client
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            this.Location = new Point(1100, 300);
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            /*
            richTextBox1.Text += "關閉程式\n";
            //Application.Exit();
            try
            {
                System.Environment.Exit(0);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息e41 : " + ex.Message + "\n";
            }
            */

            //C# 強制關閉 Process
            Process.GetCurrentProcess().Kill();

            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

    }
}
