using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

// BackgroundWorker 非同步背景執行緒

namespace vcs_BackgroundWorker1
{
    public partial class Form1 : Form
    {
        private BackgroundWorker backgroundWorker0 = new BackgroundWorker();
        private BackgroundWorker backgroundWorker1 = new BackgroundWorker();
        private BackgroundWorker backgroundWorker2 = new BackgroundWorker();
        private BackgroundWorker backgroundWorker4 = new BackgroundWorker();
        private BackgroundWorker backgroundWorker6 = new BackgroundWorker();//多線程顯示運行狀態

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //C# 跨 Thread 存取 UI
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            //------------------------------------------------------------  # 60個

            backgroundWorker0.DoWork += backgroundWorker0_DoWork;
            backgroundWorker0.RunWorkerCompleted += backgroundWorker0_RunWorkerCompleted;
            backgroundWorker0.ProgressChanged += backgroundWorker0_ProgressChanged;

            backgroundWorker0.WorkerSupportsCancellation = true;  // 是否支援非同步取消
            backgroundWorker0.WorkerReportsProgress = true;  // 是否報告進度

            //------------------------------------------------------------  # 60個

            //繫結事件
            backgroundWorker1.DoWork += new DoWorkEventHandler(backgroundWorker1_DoWork);
            backgroundWorker1.ProgressChanged += new ProgressChangedEventHandler(backgroundWorker1_ProgressChanged);
            backgroundWorker1.RunWorkerCompleted += new RunWorkerCompletedEventHandler(backgroundWorker1_RunWorkerCompleted);

            backgroundWorker1.WorkerSupportsCancellation = true;  // 是否支援非同步取消
            backgroundWorker1.WorkerReportsProgress = true;  // 是否報告進度

            //------------------------------------------------------------  # 60個

            backgroundWorker2.DoWork += backgroundWorker2_DoWork;
            backgroundWorker2.RunWorkerCompleted += backgroundWorker2_RunWorkerCompleted;
            backgroundWorker2.ProgressChanged += backgroundWorker2_ProgressChanged;

            backgroundWorker2.WorkerSupportsCancellation = true;  // 是否支援非同步取消
            backgroundWorker2.WorkerReportsProgress = true;  // 是否報告進度

            //------------------------------------------------------------  # 60個

            backgroundWorker6.DoWork += DoSomethingBusy1;
            backgroundWorker6.RunWorkerCompleted += backgroundWorker6_RunWorkerCompleted;
            backgroundWorker6.WorkerReportsProgress = true;  // 是否報告進度

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
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            progressBar0.Size = new Size(410, 40);
            progressBar0.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            label0.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            label6.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            pictureBox1.Size = new Size(620, 550);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 2);

            richTextBox1.Size = new Size(500, 690);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1400, 750);
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

        long do_heavy_work()
        {
            // 模擬耗時工作
            long sum = 0;
            for (int i = 0; i < 1000000000; i++)
            {
                sum += i;
                progressBar0.Value = i / 10000000;
                label0.Text = progressBar0.Value.ToString() + " %";
                Application.DoEvents();
            }
            return sum;
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int r = 50;
            int cx = 770;
            int cy = 80;

            e.Graphics.DrawEllipse(Pens.Red, cx - r, cy - r, r * 2, r * 2);
        }

        //------------------------------------------------------------  # 60個

        private void backgroundWorker0_DoWork(object sender, DoWorkEventArgs e)
        {
            richTextBox1.Text += "backgroundWorker0_DoWork\n";

            BackgroundWorker worker = sender as BackgroundWorker;

            // 模擬耗時工作
            long sum = 0;
            for (int i = 0; i < 1000000000; i++)
            {
                sum += i;
                if ((i % 100000000) == 0)
                {
                    progressBar0.Value = i / 10000000;
                    label0.Text = progressBar0.Value.ToString() + " %";
                    Application.DoEvents();
                    if (worker.CancellationPending == true)  // 檢查是否有收到取消命令
                    {
                        // 回傳取消
                        e.Cancel = true;
                        break;
                    }
                    worker.ReportProgress(i / 10000000);  // 向ProgressChanged報告進度
                }
            }
            e.Result = sum;  // e.Result是個Object, 表示非同步作業的結果。
        }

        private void backgroundWorker0_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            richTextBox1.Text += "BGW0 執行 ProgressChanged() " + e.ProgressPercentage.ToString() + " %\n";

            //e.ProgressPercentage  獲取非同步作業進度的百分比
            progressBar0.Value = e.ProgressPercentage;
            Application.DoEvents();
        }

        private void backgroundWorker0_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            richTextBox1.Text += "BGW0 執行 RunWorkerCompleted()\t完成\n";

            string result = string.Empty;
            if (e.Cancelled == true)
            {
                result = "取消";
            }
            else
            {
                result = "完成\n";
                progressBar0.Value = 100;
                label0.Text = progressBar0.Value.ToString() + " %";
                Application.DoEvents();
            }
            if (e.Error != null)
            {
                richTextBox1.Text += "錯誤： " + e.Error.Message + "\n";
            }
            richTextBox1.Text += "BGW0 結束, 結果 : " + result + "\n";
            flag_bgw0_RunWorkerAsync = false;
            button0.Text = "使用 BackgroundWorker0";
        }

        bool flag_bgw0_RunWorkerAsync = false;
        private void button0_Click(object sender, EventArgs e)
        {
            if (flag_bgw0_RunWorkerAsync == false)
            {
                flag_bgw0_RunWorkerAsync = true;
                button0.Text = "停止BackgroundWorker0";

                progressBar0.Value = 0;
                label0.Text = progressBar0.Value.ToString() + " %";
                Application.DoEvents();
                if (backgroundWorker0.IsBusy == false)
                {
                    // 啟動BackgroundWorker
                    richTextBox1.Text += "啟動BackgroundWorker0\n";
                    backgroundWorker0.RunWorkerAsync();  // 啟動非同步背景執行緒, 將觸發BackgroundWorker.DoWork事件
                }
            }
            else
            {
                flag_bgw0_RunWorkerAsync = false;
                button0.Text = "啟動BackgroundWorker0";

                // 停止BackgroundWorker
                richTextBox1.Text += "停止BackgroundWorker0\n";
                backgroundWorker0.CancelAsync();  // 取消非同步背景執行緒
            }
        }

        //------------------------------------------------------------  # 60個

        /// 控制代碼sender指向的就是該BackgroundWorker。
        /// e.Cancel 是否應該取消事件
        /// e.Result  獲取或設定非同步作業結果的值(在RunWorkerCompleted事件可能會使用到)
        /// e.Result是個Object, 表示非同步作業的結果。
        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            BackgroundWorker worker = sender as BackgroundWorker;

            // 模擬耗時工作
            for (int i = 1; i <= 10; i++)
            {
                if (worker.CancellationPending == true)  // 檢查是否有收到取消命令
                {
                    // 回傳取消
                    e.Cancel = true;
                    break;
                }
                else
                {
                    Thread.Sleep(1000);  // 執行耗時作業
                    string userState = "進行中";  // 狀態物件
                    worker.ReportProgress(i * 10, userState);  // 向ProgressChanged報告進度
                }
            }
            e.Result = "結束";  // e.Result是個Object, 表示非同步作業的結果。
        }

        // 進度重新整理
        private void backgroundWorker1_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            //接收ReportProgress方法傳遞過來的userState
            string state = (string)e.UserState;
            Console.WriteLine("狀態 : " + state);

            //e.ProgressPercentage  獲取非同步作業進度的百分比
            Console.WriteLine("進度 : " + e.ProgressPercentage.ToString() + " %");
        }

        /// e.Cancelled指示非同步作業是否已被取消
        /// e.Error 指示非同步作業期間發生的錯誤
        /// e.Result 獲取非同步作業結果的值,即DoWork事件中，Result設定的值。    
        /// e.Result是個Object, 表示非同步作業的結果。
        private void backgroundWorker1_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            //判斷是否使用者手動取消，若程式要支援此處功能，需要程式中有cancel的動作，並在該動作中將e.cancel置為true
            if (e.Cancelled == true)
            {
                //新增使用者手動取消的動作，並在標籤控制元件中進行提示  
                Console.WriteLine("作業已經被取消！");
            }
            //判斷是否由錯誤造成意外中止
            else if (e.Error != null)
            {
                //若發生錯誤，在標籤控制元件中顯示錯誤資訊
                Console.WriteLine("作業發生錯誤！");
            }
            //判斷是否正常結束
            else
            {
                //新增正常結束之後的收尾動作，並在標籤控制元件中進行提示
                // e.Result是個Object, 表示非同步作業的結果。
                Console.WriteLine("執行結果：{e.Result.ToString()}！");
            }
            //richTextBox1.Text += "BGW0 結束, 結果 : " + result + "\n";
            //flag_bgw1_RunWorkerAsync = false;
            button1.Text = "使用 BackgroundWorker1";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (backgroundWorker1.IsBusy == false)  // 判斷BackgroundWorker 是否正在執行非同步作業。
            {
                richTextBox1.Text += "啟動BackgroundWorker1\n";
                backgroundWorker1.RunWorkerAsync("object argument");  // 啟動非同步背景執行緒, 將觸發BackgroundWorker.DoWork事件, 有參數
            }
        }

        //------------------------------------------------------------  # 60個

        private void backgroundWorker2_DoWork(object sender, DoWorkEventArgs e)
        {
            richTextBox1.Text += "backgroundWorker2_DoWork\n";

            BackgroundWorker worker = sender as BackgroundWorker;

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_哆啦A夢\doraemon1.jpg";

            Bitmap bmp = new Bitmap(filename);
            int W = bmp.Width;
            int H = bmp.Height;

            Color pixel;
            byte r = 0;
            byte g = 0;
            byte b = 0;
            byte gray = 0;
            for (int y = 0; y < H; y++)
            {
                for (int x = 0; x < W; x++)
                {
                    //取值
                    pixel = bmp.GetPixel(x, y);//提取像素值
                    r = pixel.R;
                    g = pixel.G;
                    b = pixel.B;

                    //灰階
                    gray = (byte)(r * 0.299 + g * 0.587 + b * 0.114);
                    bmp.SetPixel(x, y, Color.FromArgb(gray, gray, gray));//設定像素值
                }
                if (worker.CancellationPending == true)  // 檢查是否有收到取消命令
                {
                    // 回傳取消
                    e.Cancel = true;
                    break;
                }
                //worker.ReportProgress((int)(y * 100 / H) + 1);  // 向ProgressChanged報告進度
                progressBar0.Value = (int)(y * 100 / H) + 1;
                label0.Text = progressBar0.Value.ToString() + " %";
                Application.DoEvents();
            }
            pictureBox1.Image = bmp;
        }

        private void backgroundWorker2_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            richTextBox1.Text += "BGW0 執行 ProgressChanged() " + e.ProgressPercentage.ToString() + " %\n";

            //e.ProgressPercentage  獲取非同步作業進度的百分比
            progressBar0.Value = e.ProgressPercentage;
            label0.Text = progressBar0.Value.ToString() + " %";
            Application.DoEvents();
        }

        private void backgroundWorker2_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            richTextBox1.Text += "BGW0 執行 RunWorkerCompleted()\t完成\n";

            string result = string.Empty;
            if (e.Cancelled == true)
            {
                result = "取消";
            }
            else
            {
                result = "完成\n";
            }
            if (e.Error != null)
            {
                richTextBox1.Text += "錯誤： " + e.Error.Message + "\n";
            }
            richTextBox1.Text += "BGW2 結束, 結果 : " + result + "\n";
            flag_bgw2_RunWorkerAsync = false;
            button2.Text = "使用 BackgroundWorker0";
        }

        bool flag_bgw2_RunWorkerAsync = false;
        private void button2_Click(object sender, EventArgs e)
        {
            //不使用BackgroundWorker
            /*
            richTextBox1.Text += "像素法\n";
            
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_哆啦A夢\doraemon1.jpg";
            Bitmap bmp = image_process_pixel1(filename);
            pictureBox1.Image = bmp;
            */

            if (flag_bgw2_RunWorkerAsync == false)
            {
                flag_bgw2_RunWorkerAsync = true;
                button0.Text = "停止BackgroundWorker0";

                progressBar0.Value = 0;
                label0.Text = progressBar0.Value.ToString() + " %";
                Application.DoEvents();
                if (backgroundWorker2.IsBusy == false)
                {
                    // 啟動BackgroundWorker
                    richTextBox1.Text += "啟動BackgroundWorker2\n";
                    backgroundWorker2.RunWorkerAsync();  // 啟動非同步背景執行緒, 將觸發BackgroundWorker.DoWork事件
                }
            }
            else
            {
                flag_bgw2_RunWorkerAsync = false;
                button0.Text = "啟動BackgroundWorker2";

                // 停止BackgroundWorker
                richTextBox1.Text += "停止BackgroundWorker2\n";
                backgroundWorker2.CancelAsync();  // 取消非同步背景執行緒
            }

        }

        Bitmap image_process_pixel1(string filename)
        {
            Bitmap bmp = new Bitmap(filename);
            int W = bmp.Width;
            int H = bmp.Height;

            Color pixel;
            byte r = 0;
            byte g = 0;
            byte b = 0;
            byte gray = 0;
            for (int x = 0; x < W; x++)
            {
                for (int y = 0; y < H; y++)
                {
                    //取值
                    pixel = bmp.GetPixel(x, y);//提取像素值
                    r = pixel.R;
                    g = pixel.G;
                    b = pixel.B;

                    //灰階
                    gray = (byte)(r * 0.299 + g * 0.587 + b * 0.114);
                    bmp.SetPixel(x, y, Color.FromArgb(gray, gray, gray));//設定像素值
                }
            }
            return bmp;
        }

        //------------------------------------------------------------  # 60個

        private void backgroundWorker3_DoWork(object sender, DoWorkEventArgs e)
        {
            richTextBox1.Text += "backgroundWorker3_DoWork\n";

            //object value = e.Argument;  // 獲取非同步作業引數的值
            string[] parameters = e.Argument as string[];
            int len = parameters.Length;
            richTextBox1.Text += "參數長度 : " + len.ToString() + "\n";

            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += "取得參數 : " + (e.Argument as string[])[i] + "\n";
                //richTextBox1.Text += "取得參數 : " + parameters[i] + "\n";
            }
        }

        private void backgroundWorker3_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
        }

        private void backgroundWorker3_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            richTextBox1.Text += "轉換完成\n";
        }

        int cnt3 = 0;
        private void button3_Click(object sender, EventArgs e)
        {
            //有參數 啟動BackgroundWorker

            string message0 = "BackgroundWorker3訊息" + (cnt3++).ToString();
            string message1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string message2 = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

            richTextBox1.Text += "啟動BackgroundWorker3\n";
            backgroundWorker3.RunWorkerAsync(new string[1] { message0 });

            delay(100);

            richTextBox1.Text += "啟動BackgroundWorker3\n";
            backgroundWorker3.RunWorkerAsync(new string[3] { message0, message1, message2 });

        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void DoSomethingBusy1(object sender, DoWorkEventArgs e)
        {
            // 模擬耗時工作
            long sum = 0;
            for (int i = 0; i < 1000000; i++)
            {
                sum += i;
                //progressBar0.Value = i / 10000000;
                //label6.Text = "使用BackgroundWorker " + (i / 10000000).ToString();
                Application.DoEvents();
            }
        }

        private void DoSomethingBusy2()
        {
            // 模擬耗時工作
            long sum = 0;
            for (int i = 0; i < 1000000; i++)
            {
                sum += i;
                //progressBar0.Value = i / 10000000;
                //label6.Text = "不使用BackgroundWorker " + (i / 10000000).ToString();
                Application.DoEvents();
            }
        }

        private void backgroundWorker6_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
        {
            richTextBox1.Text += "BGW6 執行 RunWorkerCompleted()\t完成\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //不使用BackgroundWorker
            label6.Text = "不使用BackgroundWorker6";
            richTextBox1.Text += "不使用BackgroundWorker 開始\n";
            DoSomethingBusy2();
            label6.Text = "不使用BackgroundWorker 完成";
            richTextBox1.Text += "不使用BackgroundWorker 完成\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            label6.Text = "使用BackgroundWorker6";

            if (backgroundWorker6.IsBusy == false)
            {
                richTextBox1.Text += "啟動BackgroundWorker6\n";
                backgroundWorker6.RunWorkerAsync();  // 啟動非同步背景執行緒, 將觸發BackgroundWorker.DoWork事件
            }
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button8_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "打印文字\n";
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

//label6.Text = "使用BackgroundWorker 完成";
//richTextBox1.Text += "BG6 完成! 結果 = " + e.Result.ToString() + "\n";
// e.Result是個Object, 表示非同步作業的結果。
// e.Result = sum;  // e.Result是個Object, 表示非同步作業的結果。

