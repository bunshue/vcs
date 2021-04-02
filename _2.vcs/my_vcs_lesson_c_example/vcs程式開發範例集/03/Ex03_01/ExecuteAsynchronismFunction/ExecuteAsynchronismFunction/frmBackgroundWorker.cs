using System;
using System.Collections;
using System.ComponentModel;
using System.Drawing;
using System.Threading;
using System.Windows.Forms;

namespace ExecuteAsynchronismFunction
{
    public partial class frmBackgroundWorker : Form
    {
        public frmBackgroundWorker()
        {
            InitializeComponent();
        }
        private int numberToCompute = 0;
        private int highestPercentageReached = 0;

        // 操作開在另一個線程上運行事件處理和序
        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            e.Result = ComputeFibonacci((int)e.Argument, this.backgroundWorker1, e);
        }
    
        private void backgroundWorker1_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            this.progressBar1.Value = e.ProgressPercentage;

        }
        //
        private void backgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            if (e.Error != null)
            {
                MessageBox.Show(e.Error.Message);
            }
            else if (e.Cancelled)
            {
              
                resultLabel.Text = "Canceled";
            }
            else
            {
                resultLabel.Text = e.Result.ToString();
            }
            this.numericUpDown1.Enabled = true;

            startAsyncButton.Enabled = true;
            cancelAsyncButton.Enabled = false;
        }
        //
        private void startAsyncButton_Click(object sender, EventArgs e)
        {
           
            resultLabel.Text = String.Empty;
            this.numericUpDown1.Enabled = false;
            this.startAsyncButton.Enabled = false;
            this.cancelAsyncButton.Enabled = true;
            numberToCompute = (int)numericUpDown1.Value;
            highestPercentageReached = 0;
            backgroundWorker1.RunWorkerAsync(numberToCompute);

        }//
        long ComputeFibonacci(int n, BackgroundWorker worker, DoWorkEventArgs e)
        {
            if ((n < 0) || (n > 91))
            {
                throw new ArgumentException(
                    "value must be >= 0 and <= 91", "n");
            }
            long result = 0;
            if (worker.CancellationPending)
            {
                e.Cancel = true;
            }
            else
            {
                if (n < 2)
                {
                    result = 1;
                }
                else
                {
                    result = ComputeFibonacci(n - 1, worker, e) +
                             ComputeFibonacci(n - 2, worker, e);
                }

                // Report progress as a percentage of the total task.
                int percentComplete =
                    (int)((float)n / (float)numberToCompute * 100);
                if (percentComplete > highestPercentageReached)
                {
                    highestPercentageReached = percentComplete;
                    worker.ReportProgress(percentComplete);
                }
            }

            return result;
        }

        private void cancelAsyncButton_Click(object sender, EventArgs e)
        {
            this.backgroundWorker1.CancelAsync();
            cancelAsyncButton.Enabled = false;

        }

        private void frmBackgroundWorker_Load_1(object sender, EventArgs e)
        {

        }

        
     
        
    }
}