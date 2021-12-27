using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_BackgroundWorker3
{
    public partial class Form1 : Form
    {
        BackgroundWorker work = new BackgroundWorker();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "";
            label2.Text = "";
            label3.Text = "";

            work.WorkerReportsProgress = true;
            work.DoWork += Count;
            work.RunWorkerCompleted += completeRun;
            Control.CheckForIllegalCrossThreadCalls = false;
        }

        int ccc = 0;
        private void Count(object sender, DoWorkEventArgs e)
        {
            ccc++;
            this.Text = ccc.ToString();
        }

        private void completeRun(object sender, RunWorkerCompletedEventArgs e)
        {
            this.progressBar1.Style = ProgressBarStyle.Blocks;

            delay(1234);

            label1.Text = "";
            label3.Text = "完成";
        }

        int new_work = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            new_work++;
            label1.Text = "新增工作 " + new_work.ToString();
            label3.Text = "";
            this.progressBar1.Style = ProgressBarStyle.Marquee;
            work.RunWorkerAsync();

        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }
    }
}
