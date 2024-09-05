using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;   //匯入多執行緒功能函數
using System.Diagnostics;   //for Process

using System.Timers;    //for ElapsedEventHandler

namespace vcs_Thread
{
    //創建SetValue的委托
    public delegate void SetValueDel(string str, object obj);

    public partial class Form1 : Form
    {
        private const int BORDER = 10;

        private Thread thread_ex0;
        static Thread thread_ex2a = null;
        static Thread thread_ex2b = null;
        private Thread thread_ex8a;
        private Thread thread_ex8b;
        private Thread thread_ex10;

        private bool flag_thread_running0 = false;
        private bool flag_thread_running2a = false;
        private bool flag_thread_running2b = false;
        private bool flag_thread_running8a = false;
        private bool flag_thread_running8b = false;
        private bool flag_thread_running7 = false;
        private bool flag_thread_running9 = false;
        private bool flag_thread_running10 = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            //CheckForIllegalCrossThreadCalls = false; 另法
            myUser();


            Thread.CurrentThread.Name = "MainThread";

            show_item_location();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (timechange != null)
            {
                //把thread停掉
                timechange.stop();
            }

            //關閉監聽執行續(如果有的話)
            try
            {
                thread_ex0.Abort(); //關閉監聽執行續
                //U.Close();  //關閉監聽器
            }
            catch
            {
                //忽略錯誤，程式繼續執行
            }

            //殺死一個線程
            if (thread_ex8a != null)
            {
                if (thread_ex8a.IsAlive)//線程類的 Abort() 方法可以永久的殺死一個線程。在殺死一個線程起前應該判斷線程是否在生存期間。
                {
                    thread_ex8a.Abort();
                }
                thread_ex8a = null;
            }

            //殺死一個線程
            if (thread_ex8b != null)
            {
                if (thread_ex8b.IsAlive)//線程類的 Abort() 方法可以永久的殺死一個線程。在殺死一個線程起前應該判斷線程是否在生存期間。
                {
                    thread_ex8b.Abort();
                }
                thread_ex8b = null;
            }

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

        void show_item_location()
        {
            int W = 640;
            int H = 480;
            int x_st = BORDER;
            int y_st = BORDER;
            int dx = 140 + 50;
            int dy = 50 + 15;


            W = 150;
            H = 150;
            dx = W + BORDER;
            dy = H + BORDER;

            groupBox0.Size = new Size(W, H);
            groupBox1.Size = new Size(W, H);
            groupBox2.Size = new Size(W, H);
            groupBox3.Size = new Size(W, H);
            groupBox4.Size = new Size(W, H);
            groupBox5.Size = new Size(W, H);
            groupBox6.Size = new Size(W, H);
            groupBox7.Size = new Size(W, H);
            groupBox8.Size = new Size(W, H);
            groupBox9.Size = new Size(W, H);
            groupBox11.Size = new Size(W * 2 / 3, H + 50);

            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            groupBox11.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            groupBox4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox5.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox6.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            groupBox7.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            groupBox8.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            groupBox9.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            groupBox10.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            richTextBox1.Size = new Size(220, 540);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = BORDER * 2;
            y_st = BORDER * 2;
            W = 90;
            H = 30;
            dx = W + BORDER;
            dy = H + BORDER;
            button00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button30.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button40.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button42.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button50.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button51.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button52.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button60.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button61.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button62.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button70.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button71.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button72.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button80a.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button81a.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button80b.Location = new Point(x_st + dx * 0 + 50 + 10, y_st + dy * 0);
            button81b.Location = new Point(x_st + dx * 0 + 50 + 10, y_st + dy * 1);
            button82.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button90.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button91.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button92.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            this.Size = new Size(1000, 600);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //Thread使用範例0 ST

        private void ThreadProc_ex0()
        {
            richTextBox1.Text += "啟動一個thread0 ";
            while (flag_thread_running0 == true)
            {
                //無限迴圈
                richTextBox1.Text += "0 ";
                Thread.Sleep(500);
            }
            richTextBox1.Text += "\n結束 ThreadProc_ex0\n";
        }

        private void button00_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "啟動 thread 0\n";

            flag_thread_running0 = true;
            //thread_ex0 = new Thread(new ThreadStart(ThreadProc_ex0)); same
            thread_ex0 = new Thread(ThreadProc_ex0);

            thread_ex0.Name = "Thread_ex0";
            //thread_ex0.IsBackground = true;  //設定為背景執行緒
            richTextBox1.Text += "啟動 thread 0, 名稱 : " + thread_ex0.Name + "\n";

            thread_ex0.Start();
        }

        private void button01_Click(object sender, EventArgs e)
        {
            if (thread_ex0 != null)
            {
                richTextBox1.Text += "停止 thread 0\n";
                thread_ex0.Abort();
            }

            //same
            flag_thread_running0 = false;
        }

        private void button02_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Info\n";
            if (thread_ex0 == null)
            {
                richTextBox1.Text += "Main Thread 尚未啟動\n";
            }
            else
            {
                richTextBox1.Text += "Main Thread\t" + thread_ex0.ToString() + "\n";
                richTextBox1.Text += "ThreadState\t" + thread_ex0.ThreadState.ToString() + "\n";
                richTextBox1.Text += "Name\t" + thread_ex0.Name + "\n";
                richTextBox1.Text += "IsAlive\t" + thread_ex0.IsAlive.ToString() + "\n";

                if (thread_ex0.IsAlive == true)
                {
                    richTextBox1.Text += "IsBackground\t" + thread_ex0.IsBackground.ToString() + "\n";
                }
            }
        }
        //Thread使用範例0 SP


        //Thread使用範例1 ST

        // This value is incremented by the thread.
        public int Value = 0;
        // Make and start a new counter object.
        private int thread_num = 0;


        // Add the text to the results.
        // The form provides this service because the
        // thread cannot access the form's controls directly.
        public void DisplayValue(string txt)
        {
            richTextBox1.AppendText(txt + "\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void ThreadProc_ex9()
        {
            richTextBox1.Text += "啟動一個thread9 ";
            while (flag_thread_running9 == true)
            {
                //無限迴圈
                richTextBox1.Text += "9 ";
                Thread.Sleep(500);
            }
            richTextBox1.Text += "\n結束 ThreadProc_ex9\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "啟動 thread 9\n";

            // Make a new counter object.
            Counter new_counter = new Counter(this, thread_num);
            richTextBox1.Text += "開啟thread, 編號 " + thread_num.ToString() + "\n";
            thread_num++;

            // Make a thread to run the object's Run method.
            Thread thread_ex9 = new Thread(new_counter.ThreadProc_ex9);

            // Make this a background thread so it automatically
            // aborts when the main program stops.
            thread_ex9.IsBackground = true;

            // Start the thread.
            thread_ex9.Start();

        }

        private void button11_Click(object sender, EventArgs e)
        {
            //same
            flag_thread_running9 = false;

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例1 SP


        //Thread使用範例2 ST

        private void ThreadProc_ex2()
        {
            richTextBox1.Text += "啟動一個thread2 ";

            //無限迴圈
            while (true)
            {
                if (Thread.CurrentThread.Name == "Thread_ex2a")
                {
                    richTextBox1.Text += "2A ";
                }
                else if (Thread.CurrentThread.Name == "Thread_ex2b")
                {
                    richTextBox1.Text += "2B ";
                }
                else
                {
                    richTextBox1.Text += "2X ";
                }
                //richTextBox1.Text += Thread.CurrentThread.Name + "  ";
                Thread.Sleep(500);
            }

            richTextBox1.Text += "\n結束 ThreadProc_ex2\n";
            /*
            richTextBox1.Text += "建立 thread : " + Thread.CurrentThread.Name + "\n";

            if (Thread.CurrentThread.Name == "Thread_ex2a" && Thread_ex2b.ThreadState != ThreadState.Unstarted)
            {
                if (thread_ex2b.Join(2000))
                {
                    richTextBox1.Text += "Thread_ex2b has termminated.\n";
                }
                else
                {
                    richTextBox1.Text += "The timeout has elapsed and Thread_ex2a will resume.\n";
                }
            }

            //Thread.Sleep(4000);
            richTextBox1.Text += "\nCurrent thread : " + Thread.CurrentThread.Name + "\n";
            richTextBox1.Text += "Thread_ex2a 狀態 : " + thread_ex2a.ThreadState + "\n";
            richTextBox1.Text += "Thread_ex2b 狀態 : " + thread_ex2b.ThreadState + "\n";
            */
        }

        private void button20_Click(object sender, EventArgs e)
        {
            thread_ex2a = new Thread(ThreadProc_ex2);
            thread_ex2a.Name = "Thread_ex2a";

            thread_ex2b = new Thread(ThreadProc_ex2);
            thread_ex2b.Name = "Thread_ex2b";

            richTextBox1.Text += "啟動 thread 2\n";
            //啟動
            if (thread_ex2a.ThreadState == System.Threading.ThreadState.Unstarted)
            {
                thread_ex2a.Start();
            }

            if (thread_ex2b.ThreadState == System.Threading.ThreadState.Unstarted)
            {
                thread_ex2b.Start();
            }

            if (thread_ex2a.ThreadState == System.Threading.ThreadState.Aborted)
            {
                thread_ex2a = new Thread(ThreadProc_ex2);
                thread_ex2a.Name = "Thread_ex2a";
                thread_ex2a.Start();
                richTextBox1.Text += "啟動 thread 2a, 名稱 : " + thread_ex2a.Name + "\n";
            }
            if (thread_ex2b.ThreadState == System.Threading.ThreadState.Aborted)
            {
                thread_ex2b = new Thread(ThreadProc_ex2);
                thread_ex2b.Name = "Thread_ex2b";
                thread_ex2b.Start();
                richTextBox1.Text += "啟動 thread 2b, 名稱 : " + thread_ex2b.Name + "\n";
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            if (thread_ex2a != null)
            {
                richTextBox1.Text += "停止 thread 2a\n";
                thread_ex2a.Abort();
            }

            if (thread_ex2b != null)
            {
                richTextBox1.Text += "停止 thread 2b\n";
                thread_ex2b.Abort();
            }

            //same
            flag_thread_running2a = false;
            flag_thread_running2b = false;
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //狀態
            richTextBox1.Text += "Thread_ex2a 狀態 : " + thread_ex2a.ThreadState + "\n";
            richTextBox1.Text += "Thread_ex2b 狀態 : " + thread_ex2b.ThreadState + "\n";
        }
        //Thread使用範例2 SP


        //Thread使用範例3 ST

        private void button30_Click(object sender, EventArgs e)
        {
            Thread thread_ex3 = new Thread(new ParameterizedThreadStart(delegate(object obj)
            {
                while (true)
                {
                    richTextBox1.Text += "3 ";
                    Thread.Sleep(500);
                }
            }));
            thread_ex3.Name = " --start tray thread";
            thread_ex3.IsBackground = true;
            thread_ex3.Priority = ThreadPriority.Lowest;
            thread_ex3.Start(null);
        }

        private void button31_Click(object sender, EventArgs e)
        {
        }

        private void button32_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例3 SP

        //Thread使用範例4 ST

        Random r = new Random(Guid.NewGuid().GetHashCode());
        private int _R = 0, _G = 0, _B = 0;

        private void ThreadProc_ex10()
        {
            richTextBox1.Text += "啟動一個thread10 ";
            while (true)
            {
                _R = r.Next(256);
                _G = r.Next(256);
                _B = r.Next(256);
                Thread.Sleep(100);
            }
            richTextBox1.Text += "\n結束 ThreadProc_ex10\n";
        }



        private void button40_Click(object sender, EventArgs e)
        {
            thread_ex10 = new Thread(ThreadProc_ex10);

            if (thread_ex10.IsAlive == false)
            {
                thread_ex10.Start();
            }
        }

        private void button41_Click(object sender, EventArgs e)
        {
            if (thread_ex10 != null)
            {
                richTextBox1.Text += "停止 thread 10\n";
                thread_ex10.Abort();
            }

            //same
            flag_thread_running10 = false;
        }

        private void button42_Click(object sender, EventArgs e)
        {

        }

        private void timer_rgb_Tick(object sender, EventArgs e)
        {
            lb_R.Text = _R.ToString();
            lb_G.Text = _G.ToString();
            lb_B.Text = _B.ToString();
        }


        //Thread使用範例4 SP


        //Thread使用範例5 ST

        private void ThreadProc_ex5()
        {
        }

        private void button50_Click(object sender, EventArgs e)
        {
        }

        private void button51_Click(object sender, EventArgs e)
        {
        }

        private void button52_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例5 SP


        //Thread使用範例6 ST

        System.Timers.Timer timer6 = new System.Timers.Timer(1234);
        int number = 0;

        public void ThreadProc_ex6(object source, System.Timers.ElapsedEventArgs e)
        {
            number++;
            System.Diagnostics.Debug.Print("即時運算視窗輸出除錯訊息 測試訊息！！！Form1！！！ " + number.ToString());
            Console.Write(number.ToString() + "\r\n");

            //MessageBox.Show("number = " + number);
        }

        private void button60_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "啟動 thread 6\n";

            timer6.Elapsed += new ElapsedEventHandler(ThreadProc_ex6);
            timer6.Enabled = true;
        }

        private void button61_Click(object sender, EventArgs e)
        {
            timer6.Enabled = false;
            number = 0;

        }

        private void button62_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例6 SP

        //Thread使用範例7 ST

        private void ThreadProc_ex7()
        {
            richTextBox1.Text += "啟動一個thread7 ";
            while (flag_thread_running7 == true)
            {
                //無限迴圈
                richTextBox1.Text += "7 ";
                Thread.Sleep(500);
            }
            richTextBox1.Text += "\n結束 ThreadProc_ex7\n";
        }

        // Make a thread with the indicated priority.
        private void MakeThread(string thread_name, ThreadPriority thread_priority)
        {
            richTextBox1.Text += "開啟thread, 名稱 : " + thread_name + ", 優先序 : " + thread_priority.ToString() + "\n";
            Application.DoEvents();

            // Initialize the thread.
            Counter2 new_counter = new Counter2(thread_name);
            Thread thread = new Thread(new_counter.ThreadProc_ex7);
            thread.Priority = thread_priority;
            thread.IsBackground = true;
            thread.Name = thread_name;

            // Start the thread.
            thread.Start();
        }

        private void button70_Click(object sender, EventArgs e)
        {
            //啟動thread, 不同優先序
            int i;
            int num_low = 4;
            for (i = 0; i < num_low; i++)
            {
                MakeThread("低_" + i.ToString(), ThreadPriority.BelowNormal);
            }

            int num_normal = 4;
            for (i = 0; i < num_normal; i++)
            {
                MakeThread("中_" + i.ToString(), ThreadPriority.Normal);
            }

            int num_high = 4;
            for (i = 0; i < num_high; i++)
            {
                MakeThread("高_" + i.ToString(), ThreadPriority.AboveNormal);
            }
        }

        private void button71_Click(object sender, EventArgs e)
        {

        }

        private void button72_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例7 SP

        //Thread使用範例8 ST

        private void ThreadProc_ex8a()
        {
            richTextBox1.Text += "啟動一個thread8a ";
            while (flag_thread_running8a == true)
            {
                richTextBox1.Text += "8a ";
                Thread.Sleep(500);
            }
            richTextBox1.Text += "\n結束 ThreadProc_ex8a\n";
        }

        private void ThreadProc_ex8b()
        {
            if (thread_ex8a != null)
            {
                //等待執行
                thread_ex8a.Join();//thread_ex8b 要先讓線程 thread_ex8a 執行完，然後線程 thread_ex8b 再繼續執行
            }

            richTextBox1.Text += "啟動一個thread8b ";
            while (flag_thread_running8b == true)
            {
                richTextBox1.Text += "8b ";
                Thread.Sleep(500);
            }
            richTextBox1.Text += "\n結束 ThreadProc_ex8b\n";
        }

        private void button80a_Click(object sender, EventArgs e)
        {
            if (thread_ex8a == null)
            {
                flag_thread_running8a = true;
                thread_ex8a = new Thread(ThreadProc_ex8a);
                thread_ex8a.Priority = ThreadPriority.BelowNormal;
                thread_ex8a.IsBackground = true;
                thread_ex8a.Start();
            }
        }

        private void button81a_Click(object sender, EventArgs e)
        {
            //殺死一個線程
            if (thread_ex8a != null)
            {
                if (thread_ex8a.IsAlive)//線程類的 Abort() 方法可以永久的殺死一個線程。在殺死一個線程起前應該判斷線程是否在生存期間。
                {
                    thread_ex8a.Abort();
                }
                thread_ex8a = null;
            }

            //same
            flag_thread_running8a = false;
        }

        private void button80b_Click(object sender, EventArgs e)
        {
            if (thread_ex8b == null)
            {
                richTextBox1.Text += "等thread_ex8a 執行完，thread_ex8b 再繼續執行\n";
                thread_ex8b = new Thread(ThreadProc_ex8b);
                thread_ex8b.Priority = ThreadPriority.BelowNormal;
                thread_ex8b.IsBackground = true;
                thread_ex8b.Start();
                flag_thread_running8b = true;
            }
        }

        private void button81b_Click(object sender, EventArgs e)
        {
            //殺死一個線程
            if (thread_ex8b != null)
            {
                if (thread_ex8b.IsAlive)//線程類的 Abort() 方法可以永久的殺死一個線程。在殺死一個線程起前應該判斷線程是否在生存期間。
                {
                    thread_ex8b.Abort();
                }
                thread_ex8b = null;
            }

            //same
            flag_thread_running8b = false;
        }

        private void button82_Click(object sender, EventArgs e)
        {

        }

        //Thread使用範例8 SP


        //Thread使用範例9 ST

        //開啟一個線程
        int thread_ex9_count = 0;

        //給文本框賦值
        private void SetValue(string str, object obj)
        {
            //lock裡面的代碼同一個時刻，只能被一個線程使用。其它的後面排隊。這樣防止數據混亂。
            lock (obj)
            {
                richTextBox1.Text += "Thread名稱 : " + str + " 做事 " + DateTime.Now.ToString() + "\n";
            }
        }

        private void button90_Click(object sender, EventArgs e)
        {
            //將委托的方法和主窗體傳過去
            NEWThreadClass threadOneClass = new NEWThreadClass(SetValue, this);

            thread_ex9_count++;
            string thread_name = "Thread測試_" + thread_ex9_count.ToString();

            Thread TheThreadOne = new Thread(threadOneClass.threadOne);//不需要ThreadStart()也可以
            TheThreadOne.Name = thread_name;

            richTextBox1.Text += "開啟thread, 名稱 : " + TheThreadOne.Name + "\n";

            //讓線程變為後台線程（默認是前台的），這樣主線程結束了，這個線程也會結束。要不然，任何前台線程在運行都會保持程序存活。
            TheThreadOne.IsBackground = true;
            TheThreadOne.Start();
        }

        private void button91_Click(object sender, EventArgs e)
        {

        }

        private void button92_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例9 SP

        //Thread使用範例 時鐘 ST

        //委派function
        public delegate void InvokeFunction(int h, int m, int s);
        //設定時間
        public void setTime(int h, int m, int s)
        {
            setHH(h);
            setMM(m);
            setSS(s);
        }

        public void setHH(int h)
        {
            this.label1.Text = h.ToString();
        }
        public void setMM(int m)
        {
            this.label2.Text = m.ToString();
        }
        public void setSS(int s)
        {
            this.label3.Text = s.ToString();
        }

        private ChangeTime timechange;

        private void bt_clock_st_Click(object sender, EventArgs e)
        {
            //啟動時鐘
            //產生一個類別，專門來管理時間運作
            timechange = new ChangeTime(this);
            //timechange.change();

            //使用一個thread來增加時間的秒數
            Thread thread_clock = new Thread(new ThreadStart(timechange.run));
            thread_clock.Start();
        }

        private void bt_clock_sp_Click(object sender, EventArgs e)
        {
            //關閉時鐘
            if (timechange != null)
                timechange.stop();
        }

        //Thread使用範例 時鐘 SP


        //Thread使用範例 CPU使用率 ST

        Thread td;
        int mheight = 0;


        private void CreateImage()
        {
            int i = panel3.Height / 100;
            Bitmap image = new Bitmap(panel3.Width, panel3.Height);
            //建立Graphics類對像
            Graphics g = Graphics.FromImage(image);
            g.Clear(Color.Green);
            SolidBrush mybrush = new SolidBrush(Color.Lime);
            g.FillRectangle(mybrush, 0, panel3.Height - mheight * i, 26, mheight * i);
            panel3.BackgroundImage = image;
        }




        int cpu_count = 0;
        private void myUser()
        {
            lb_cpu1.Text = cpu_count.ToString() + " %";
            lb_cpu2.Text = "CPU使用率：" + lb_cpu1.Text;
            mheight = Convert.ToInt32(cpu_count.ToString());
            if (mheight == 100)
                panel3.Height = 100;
            CreateImage();
            cpu_count += 3;
            if (cpu_count > 100)
                cpu_count -= 100;
        }


        private void timer11_Tick(object sender, EventArgs e)
        {
            td = new Thread(new ThreadStart(myUser));
            td.Start();
        }



        //Thread使用範例 CPU使用率 SP
    }

    // This class's Run method displays a count in the Output window.
    class Counter
    {
        // The form that owns the Value variable.
        private Form1 MyForm;

        // This counter's number.
        private int Number;

        // Define a delegate type for the form's DisplayValue method.
        private delegate void DisplayValueDelegateType(string txt);

        // Declare a delegate variable to point to the form's DisplayValue method.
        private DisplayValueDelegateType DisplayValueDelegate;

        public Counter(Form1 form1, int number)
        {
            MyForm = form1;
            Number = number;

            // Initialize the delegate variable to point
            // to the form's DisplayValue method.
            DisplayValueDelegate = MyForm.DisplayValue;
        }

        // Count off seconds in the Output window.
        public void ThreadProc_ex9()
        {
            try
            {
                while (true)
                {
                    // Wait 1 second.
                    Thread.Sleep(1000);

                    // Lock the form object. This doesn't do anything
                    // to the form, it just means no other thread can
                    // lock the form object until we release the lock.
                    // That means a thread can update MyForm.Value
                    // and then display its value without interference.
                    lock (MyForm)
                    {
                        // Increment the form's Value.
                        MyForm.Value++;

                        // Display the value on the form.
                        // The call to InvokeRequired returns true
                        // if this code is not running on the same
                        // thread as the object MyForm. In this
                        // example, we know that is true so the call
                        // isn't necessary, but in other cases it
                        // might not be so clear.
                        if (MyForm.InvokeRequired)
                        {
                            // Make an array containing the parameters
                            // to pass to the method.
                            string[] args = new string[] { "Thread : " + Number + ", 數字 : " + MyForm.Value };

                            // Invoke the delegate.
                            MyForm.Invoke(DisplayValueDelegate, args);
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Unexpected error in thread " + Number + "\r\n" + ex.Message);
            }
        }
    }

    class Counter2
    {
        // This counter's number.
        public string Name;

        // Initializing constructor.
        public Counter2(string name)
        {
            Name = name;
        }

        // Count off 10 half second intervals in the Output window.
        public void ThreadProc_ex7()
        {
            for (int i = 1; i <= 10; i++)
            {
                // Display the next message.
                Console.WriteLine(Name + " " + i);

                // See when we should display the next message.
                DateTime next_time = DateTime.Now.AddSeconds(0.5);

                // Waste half a second. We don't sleep or call
                // DoEvents so we don't give up control of the CPU.
                while (DateTime.Now < next_time)
                {
                    // Wait a bit.
                }
            }
            Console.WriteLine(Name + "  done");
        }
    }

    class ChangeTime
    {
        private Form1 form;

        private Boolean state = true;

        private int h;
        private int m;
        private int s;

        public ChangeTime(Form1 form1)
        {
            this.form = form1;
            //設定預設的起始時間
            DateTime date = DateTime.Now;
            h = date.Hour;
            m = date.Minute;
            s = date.Second;
        }

        //停止thread,在fomr Dispose時要把thread也設定關掉
        public void stop()
        {
            state = false;
        }

        public void run()
        {
            while (state)
            {
                s++;
                if (s / 60 == 1)
                {
                    s = s - 60;
                    m++;
                    if (m / 60 == 1)
                    {
                        m = m - 60;
                        h++;
                        if (h / 24 == 1)
                        {
                            h = h - 24;
                        }
                    }
                }

                //一定要使用form裡的thread才可以變動form上的元件內容，其它thread更動時會有問題
                //利用invoke來執行form的thread
                if (state)//如果已經Dispose掉了就不再invoke了
                {
                    form.Invoke(new Form1.InvokeFunction(form.setTime), new object[] { h, m, s });
                }
                //一秒執行一次
                System.Threading.Thread.Sleep(1000);//停一秒
            }
        }
    }

    //建一個類，模擬實際使用情況
    public class NEWThreadClass
    {
        //接收主窗體傳過來的委托方法。
        public SetValueDel setValueDel;

        //接收主窗體
        public Form form;

        //用於告訴主線程中鎖，是哪一個線程調用的。
        static object locker = new object();

        public NEWThreadClass(SetValueDel del, Form fom)
        {
            this.setValueDel = del;
            this.form = fom;
        }
        //第一個線程,給主線程創建的控件傳值。
        public void threadOne()
        {
            //這裡獲取線程的名字
            string threadName = Thread.CurrentThread.Name;
            try
            {
                while (true)
                {
                    //告訴主線程，我要更改你的控件了。
                    this.form.Invoke((EventHandler)(delegate
                    {
                        //如果在這裡使用Thread.CurrentThread.Name 獲取到的是主線程的名字。
                        setValueDel(threadName + " :Hello!", locker);//給文本框傳值，“自己的名字：Hello!”。
                    }));
                    Thread.Sleep(3 * 1000);//太累了 ，休息三秒。。。。
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Unexpected error in thread : " + ex.Message);
            }
        }
    }
}


/*

                //一秒執行一次
                Thread.Sleep(1000); //停一秒

                    //richTextBox1.Text += "XX ";
                    Console.Write("XX ");

 
*/