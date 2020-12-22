using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_BackgroundWorker
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "";
            label2.Text = "";
        }

        // Use the BackgroundWorker to perform a long task.
        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text == "Go")
            {
                // Start the process.
                label1.Text = "Working...";
                button1.Text = "Stop";
                progressBar1.Value = 0;
                progressBar1.Visible = true;

                // Start the BackgroundWorker.
                backgroundWorker1.RunWorkerAsync();
            }
            else
            {
                // Stop the process.
                backgroundWorker1.CancelAsync();
            }
        }

        // Perform the long task.
        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            // Spend 10 seconds doing nothing.
            for (int i = 1; i <= 10; i++)
            {
                // If we should stop, do so.
                if (backgroundWorker1.CancellationPending)
                {
                    // Indicate that the task was canceled.
                    e.Cancel = true;
                    break;
                }

                // Sleep.
                System.Threading.Thread.Sleep(1000);

                // Notify the UI thread of our progress.
                //backgroundWorker1.ReportProgress(i * 10);
                backgroundWorker1.ReportProgress(i * 10);
            }
        }

        // Update the progress bar.
        private void backgroundWorker1_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            progressBar1.Value = e.ProgressPercentage;
        }

        // The long task is done.
        private void backgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            if (e.Cancelled)
            {
                label1.Text = "Canceled";
            }
            else
            {
                label1.Text = "Finished";
            }
            button1.Text = "Go";
            progressBar1.Visible = false;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            label2.Text = DateTime.Now.ToString("T");
        }

    }
}
