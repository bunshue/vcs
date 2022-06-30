using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_BackgroundWorker6
{
    public partial class Form1 : Form
    {
        //多線程顯示運行狀態
        BackgroundWorker work = new BackgroundWorker();
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            work.WorkerReportsProgress = true;
            work.DoWork += DoSomethingBusy1;
            work.RunWorkerCompleted += completeRun;
            Control.CheckForIllegalCrossThreadCalls = false;
        }

        private void DoSomethingBusy1(object sender, DoWorkEventArgs e)
        {
            double aa = 0;
            double bb = 0;
            double cc = 0;
            double num = 0;
            while (num < 10000)
            {
                aa = num;
                bb = 5000 - num;
                cc = Math.Sqrt(Math.Sqrt(aa) * Math.Sqrt(bb));
                num++;
                label1.Text = "使用BackgroundWorker " + cc.ToString();
                Application.DoEvents();
            }
        }

        private void DoSomethingBusy2()
        {
            double aa = 0;
            double bb = 0;
            double cc = 0;
            double num = 0;
            while (num < 10000)
            {
                aa = num;
                bb = 5000 - num;
                cc = Math.Sqrt(Math.Sqrt(aa) * Math.Sqrt(bb));
                num++;
                label1.Text = "不使用BackgroundWorker " + cc.ToString();
                Application.DoEvents();
            }
        }

        private void completeRun(object sender, RunWorkerCompletedEventArgs e)
        {
            this.progressBar1.Style = ProgressBarStyle.Blocks;
            label1.Text = "使用BackgroundWorker 完成";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            label1.Text = "使用BackgroundWorker";
            this.progressBar1.Style = ProgressBarStyle.Marquee;
            work.RunWorkerAsync();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label1.Text = "不使用BackgroundWorker";
            this.progressBar1.Style = ProgressBarStyle.Marquee;
            DoSomethingBusy2();
            this.progressBar1.Style = ProgressBarStyle.Blocks;
            label1.Text = "不使用BackgroundWorker 完成";
        }
    }
}
