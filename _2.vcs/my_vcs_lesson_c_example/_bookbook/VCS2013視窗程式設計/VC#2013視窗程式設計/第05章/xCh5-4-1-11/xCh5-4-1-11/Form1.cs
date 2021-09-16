using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_4_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            backgroundWorker1.WorkerReportsProgress = true;
            backgroundWorker1.WorkerSupportsCancellation = true;

            label1.Text = "目前進度";
            button1.Text = "同步作業";
            button2.Text = "取消同步";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (backgroundWorker1.IsBusy != true)
            {
                backgroundWorker1.RunWorkerAsync();
            }
        }

        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            BackgroundWorker worker = sender as BackgroundWorker;

            for (int i = 1; i <= 10; i++)
            {
                if (worker.CancellationPending == true)
                {
                    e.Cancel = true;
                    break;
                }
                else
                {
                    System.Threading.Thread.Sleep(2000);
                    worker.ReportProgress(i * 10);
                }
            }
        }

        private void backgroundWorker1_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            label1.Text = ("目前進度是：" + e.ProgressPercentage.ToString() + "%");
        }

        private void backgroundWorker1_RunWorkerCompleted(
            object sender, RunWorkerCompletedEventArgs e)
        {
            if (e.Cancelled == true)
            {
               label1.Text = "非同步作業被取消了！";
            }
            else if (e.Error != null)
            {
               label1.Text = "錯誤： " + e.Error.Message;
            }
            else
            {
               label1.Text = "Done!";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (backgroundWorker1.WorkerSupportsCancellation == true)
            {
                backgroundWorker1.CancelAsync();
            }
        }
    }
}
