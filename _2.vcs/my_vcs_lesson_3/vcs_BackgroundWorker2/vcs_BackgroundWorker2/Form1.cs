using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Diagnostics;

namespace vcs_BackgroundWorker2
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
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤
        }

        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            string mesg = (e.Argument as string[])[0];
            richTextBox1.Text += "取得訊息 " + mesg + "\n";

        }

        private void backgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            richTextBox1.Text += "完成\n";

        }

        int cnt = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            string message = "message " + cnt.ToString();
            backgroundWorker1.RunWorkerAsync(new string[1] { message });
            cnt++;
        }

    }
}
