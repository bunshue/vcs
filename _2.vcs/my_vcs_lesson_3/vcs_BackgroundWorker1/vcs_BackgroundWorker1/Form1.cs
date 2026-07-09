using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_BackgroundWorker1
{
    public partial class Form1 : Form
    {
        private BackgroundWorker backgroundWorker0;
        BackgroundWorker backgroundWorker4 = new BackgroundWorker();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            label1.Text = "";
            label2.Text = "";

            //------------------------------------------------------------  # 60個

            //C# 跨 Thread 存取 UI
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            //------------------------------------------------------------  # 60個

            backgroundWorker0 = new BackgroundWorker();
            backgroundWorker0.DoWork += Worker0_DoWork;
            backgroundWorker0.RunWorkerCompleted += Worker0_RunWorkerCompleted;

            //------------------------------------------------------------  # 60個

            label4a.Text = "";
            label4b.Text = "";
            label4c.Text = "";

            backgroundWorker4.WorkerReportsProgress = true;
            backgroundWorker4.DoWork += Worker4_Count;
            backgroundWorker4.RunWorkerCompleted += Worker4_completeRun;
            Control.CheckForIllegalCrossThreadCalls = false;

            //------------------------------------------------------------  # 60個

        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            richTextBox1.Size = new Size(640, 690 - 300);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0 + 300);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(890, 750);
            this.Text = "vcs_BackgroundWorker1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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

        //------------------------------------------------------------  # 60個

        private void Worker0_DoWork(object sender, DoWorkEventArgs e)
        {
            // 模擬耗時工作
            long sum = 0;
            for (int i = 0; i < 100000000; i++)
            {
                sum += i;
            }
            e.Result = sum;
        }

        private void Worker0_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            MessageBox.Show("完成! 結果 = " + e.Result.ToString());
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //使用 BackgroundWorker

            if (!backgroundWorker0.IsBusy)
            {
                backgroundWorker0.RunWorkerAsync(); // 在背景執行緒開始工作
            }
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //啟動BackgroundWorker1
            // Use the BackgroundWorker to perform a long task.
            if (button1.Text == "啟動BackgroundWorker")
            {
                // Start the process.
                label1.Text = "Working...";
                button1.Text = "停止BackgroundWorker";
                progressBar1.Value = 0;
                progressBar1.Visible = true;

                // 啟動BackgroundWorker
                backgroundWorker1.RunWorkerAsync();
            }
            else
            {
                button1.Text = "啟動BackgroundWorker";

                // 停止BackgroundWorker
                backgroundWorker1.CancelAsync();
            }
        }

        //------------------------------------------------------------  # 60個

        int cnt = 0;
        private void button2_Click(object sender, EventArgs e)
        {
            //啟動BackgroundWorker2
            string message = "message " + cnt.ToString();
            backgroundWorker2.RunWorkerAsync(new string[1] { message });
            cnt++;
        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
            //啟動BackgroundWorker3
            BackgroundWorkerInit.BackgroundWorker1_Init();
        }

        //------------------------------------------------------------  # 60個

        int ccc4 = 0;
        private void Worker4_Count(object sender, DoWorkEventArgs e)
        {
            ccc4++;
            this.Text = ccc4.ToString();
        }

        private void Worker4_completeRun(object sender, RunWorkerCompletedEventArgs e)
        {
            this.progressBar4.Style = ProgressBarStyle.Blocks;

            delay(1234);

            label4a.Text = "";
            label4c.Text = "完成";
        }

        int new_work = 0;
        private void button4_Click(object sender, EventArgs e)
        {
            //啟動BackgroundWorker4
            new_work++;
            label4a.Text = "新增工作 " + new_work.ToString();
            label4c.Text = "";
            this.progressBar4.Style = ProgressBarStyle.Marquee;
            backgroundWorker4.RunWorkerAsync();
        }

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void timer1_Tick(object sender, EventArgs e)
        {
            label2.Text = DateTime.Now.ToString("T");


        }

        //------------------------------------------------------------  # 60個

        // Perform the long task.
        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            richTextBox1.Text += "BGW 執行 DoWork()\n";

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
                backgroundWorker1.ReportProgress(i * 10);
            }
        }

        // Update the progress bar.
        private void backgroundWorker1_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            richTextBox1.Text += "BGW 執行 ProgressChanged()\n";
            progressBar1.Value = e.ProgressPercentage;
        }

        // The long task is done.
        private void backgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            richTextBox1.Text += "BGW 執行 RunWorkerCompleted()\t完成\n";

            if (e.Cancelled)
            {
                label1.Text = "Canceled";
            }
            else
            {
                label1.Text = "Finished";
            }
            button1.Text = "啟動BackgroundWorker";
            progressBar1.Visible = false;
        }

        //------------------------------------------------------------  # 60個

        private void backgroundWorker2_DoWork(object sender, DoWorkEventArgs e)
        {
            richTextBox1.Text += "BGW2 執行 DoWork()\n";
            string mesg = (e.Argument as string[])[0];
            richTextBox1.Text += "取得訊息 " + mesg + "\n";
        }

        private void backgroundWorker2_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            richTextBox1.Text += "BGW2 執行 RunWorkerCompleted()\t完成\n";
        }

        //------------------------------------------------------------  # 60個
    }


    public class BackgroundWorkerInit
    {
        public static void BackgroundWorker1_Init()
        {
            BackgroundWorker backgroundWorker1 = new BackgroundWorker();
            backgroundWorker1.WorkerReportsProgress = true;//能否報告進度更新。
            backgroundWorker1.WorkerSupportsCancellation = true;//是否支援非同步取消
            //繫結事件
            backgroundWorker1.DoWork += new DoWorkEventHandler(BackgroundWorker1_DoWork);
            backgroundWorker1.ProgressChanged += new ProgressChangedEventHandler(BackgroundWorker1_ProgressChanged);
            backgroundWorker1.RunWorkerCompleted += new RunWorkerCompletedEventHandler(BackgroundWorker1_RunWorkerCompleted);

            //啟動BackgroundWorker
            if (backgroundWorker1.IsBusy != true)//判斷BackgroundWorker 是否正在執行非同步操作。
            {
                backgroundWorker1.RunWorkerAsync("object argument");//啟動非同步操作，有兩種過載（有參和無參）,將觸發BackgroundWorker.DoWork事件
            }
        }

        /// <summary>
        /// 控制代碼sender指向的就是該BackgroundWorker。
        /// e.Argument 獲取非同步操作引數的值  
        /// e.Cancel 是否應該取消事件
        /// e.Result  獲取或設定非同步操作結果的值(在RunWorkerCompleted事件可能會使用到)
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private static void BackgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            object value = e.Argument;//獲取RunWorkerAsync(object argument)傳入的值
            BackgroundWorker worker = sender as BackgroundWorker;

            for (int i = 1; i <= 10; i++)
            {
                if (worker.CancellationPending == true)//在耗時操作中判斷CancellationPending屬性，如果為true則退出
                {
                    e.Cancel = true;
                    break;
                }
                else
                {
                    // 執行耗時操作
                    System.Threading.Thread.Sleep(1000);
                    worker.ReportProgress(i * 10, "Object userState");// 將觸發BackgroundWorker.ProgressChanged事件，向ProgressChanged報告進度
                }
            }
            e.Result = "結束";
        }


        /// <summary>
        /// e.Cancelled指示非同步操作是否已被取消
        /// e.Error 指示非同步操作期間發生的錯誤
        /// e.Result 獲取非同步操作結果的值,即DoWork事件中，Result設定的值。    
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private static void BackgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            //判斷是否使用者手動取消，若程式要支援此處功能，需要程式中有cancel的動作，並在該動作中將e.cancel置為true
            if (e.Cancelled == true)
            {
                //新增使用者手動取消的動作，並在標籤控制元件中進行提示  
                Console.WriteLine("操作已經被取消！");
            }
            //判斷是否由錯誤造成意外中止
            else if (e.Error != null)
            {
                //若發生錯誤，在標籤控制元件中顯示錯誤資訊
                Console.WriteLine("操作發生錯誤！");
            }
            //判斷是否正常結束
            else
            {
                //新增正常結束之後的收尾動作，並在標籤控制元件中進行提示
                Console.WriteLine("執行結果：{e.Result.ToString()}！");
            }
        }

        /// <summary>
        /// 進度重新整理
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private static void BackgroundWorker1_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            //接收ReportProgress方法傳遞過來的userState
            string state = (string)e.UserState;

            //e.ProgressPercentage  獲取非同步操作進度的百分比
            Console.WriteLine("進度 : " + e.ProgressPercentage.ToString() + " %");
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


