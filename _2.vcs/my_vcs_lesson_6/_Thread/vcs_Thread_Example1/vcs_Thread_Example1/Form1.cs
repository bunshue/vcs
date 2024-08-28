using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Diagnostics;   //for Process

namespace vcs_Thread_Example1
{
    public partial class Form1 : Form
    {
        private const int BORDER = 10;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            show_item_location();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //關閉監聽執行續(如果有的話)
            try
            {
                thread_ex1.Abort(); //關閉監聽執行續
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
            groupBox10.Size = new Size(W, H);
            groupBox11.Size = new Size(W, H);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            groupBox4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox5.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox6.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            groupBox7.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            groupBox8.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            groupBox9.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            groupBox10.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            groupBox11.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            richTextBox1.Size = new Size(320, 540);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
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
            button100.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button101.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button102.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button110.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button111.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button112.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            this.Size = new Size(1000, 600);

            groupBox4.Enabled = false;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //Thread使用範例0 ST

        private Thread thread_ex0;
        private bool flag_thread_running0 = false;

        private void ThreadProc_ex0()
        {
            richTextBox1.Text += "啟動一個thread ";
            while (flag_thread_running0 == true)
            {
                //無限迴圈
                richTextBox1.Text += "0";
                Thread.Sleep(500);
            }
            richTextBox1.Text += "\n結束 ThreadProc_ex0\n";
        }

        private void button00_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "啟動 thread 0\n";

            flag_thread_running0 = true;
            //thread_ex0 = new Thread(new ThreadStart(this.ThreadProc_ex0)); same
            thread_ex0 = new Thread(ThreadProc_ex0);
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

        }
        //Thread使用範例0 SP


        //Thread使用範例1 ST

        Thread thread_ex1;                                  //宣告監聽用執行續
        private bool flag_thread_running1 = false;

        private void ThreadProc_ex1()
        {
            while (flag_thread_running1 == true)
            {
                //無限迴圈
                richTextBox1.Text += "1";
                Thread.Sleep(500);
            }
            richTextBox1.Text += "\n結束 ThreadProc_ex1\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            flag_thread_running1 = true;
            thread_ex1 = new Thread(ThreadProc_ex1); //建立監聽網路訊息的新執行緒
            thread_ex1.Name = "Thread_ex1";
            //thread_ex1.IsBackground = true;  //設定為背景執行緒
            thread_ex1.Start();             //啟動監聽執行緒
            richTextBox1.Text += "啟動 thread 1, 名稱 : " + thread_ex1.Name + "\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            if (thread_ex1 != null)
            {
                richTextBox1.Text += "停止 thread 1\n";
                thread_ex1.Abort();
            }
            
            //same
            flag_thread_running1 = false;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Info\n";
            if (thread_ex1 == null)
            {
                richTextBox1.Text += "Main Thread 尚未啟動\n";
            }
            else
            {
                richTextBox1.Text += "Main Thread\t" + thread_ex1.ToString() + "\n";
                richTextBox1.Text += "ThreadState\t" + thread_ex1.ThreadState.ToString() + "\n";
                richTextBox1.Text += "Name\t" + thread_ex1.Name + "\n";
                richTextBox1.Text += "IsAlive\t" + thread_ex1.IsAlive.ToString() + "\n";

                if (thread_ex1.IsAlive == true)
                {
                    richTextBox1.Text += "IsBackground\t" + thread_ex1.IsBackground.ToString() + "\n";
                }
            }
        }
        //Thread使用範例1 SP


        //Thread使用範例2 ST

        static Thread thread_ex2a;
        static Thread thread_ex2b;

        private bool flag_thread_running2a = false;
        private bool flag_thread_running2b = false;

        private void ThreadProc_ex2()
        {
            while (true)
            {
                if (Thread.CurrentThread.Name == "Thread_ex1")
                {
                    //richTextBox1.Text += "AA ";
                    Console.Write("AA ");
                }
                else if (Thread.CurrentThread.Name == "Thread_ex2")
                {
                    //richTextBox1.Text += "BB ";
                    Console.Write("BB ");
                }
                else
                {
                    //richTextBox1.Text += "XX ";
                    Console.Write("XX ");
                }


                richTextBox1.Text += Thread.CurrentThread.Name + "  ";
                Thread.Sleep(1000);
            }
            /*
            richTextBox1.Text += "建立 thread : " + Thread.CurrentThread.Name + "\n";

            if (Thread.CurrentThread.Name == "Thread_ex1" && Thread_ex2.ThreadState != ThreadState.Unstarted)
            {
                if (thread_ex2b.Join(2000))
                {
                    richTextBox1.Text += "Thread_ex2 has termminated.\n";
                }
                else
                {
                    richTextBox1.Text += "The timeout has elapsed and Thread_ex1 will resume.\n";
                }
            }

            //Thread.Sleep(4000);
            richTextBox1.Text += "\nCurrent thread : " + Thread.CurrentThread.Name + "\n";
            richTextBox1.Text += "Thread_ex1 狀態 : " + thread_ex2a.ThreadState + "\n";
            richTextBox1.Text += "Thread_ex2 狀態 : " + thread_ex2b.ThreadState + "\n";
            */
        }

        private void button20_Click(object sender, EventArgs e)
        {
            thread_ex2a = new Thread(ThreadProc_ex2);
            thread_ex2a.Name = "Thread_ex1";

            thread_ex2b = new Thread(ThreadProc_ex2);
            thread_ex2b.Name = "Thread_ex2";

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
                thread_ex2a.Name = "Thread_ex1";
                thread_ex2a.Start();
                richTextBox1.Text += "啟動 thread 2a, 名稱 : " + thread_ex2a.Name + "\n";
            }
            if (thread_ex2b.ThreadState == System.Threading.ThreadState.Aborted)
            {
                thread_ex2b = new Thread(ThreadProc_ex2);
                thread_ex2b.Name = "Thread_ex2";
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
            richTextBox1.Text += "Thread_ex1 狀態 : " + thread_ex2a.ThreadState + "\n";
            richTextBox1.Text += "Thread_ex2 狀態 : " + thread_ex2b.ThreadState + "\n";
        }
        //Thread使用範例2 SP


        //Thread使用範例3 ST
        static Thread thread_ex3 = null;
        private bool flag_thread_running3 = false;

        public void ThreadProc_ex3()
        {
            while (flag_thread_running3 == true)
            {
                //無限迴圈
                richTextBox1.Text += "3";
                Thread.Sleep(500);
            }
            richTextBox1.Text += "\n結束 ThreadProc_ex3\n";
        }

        private void button30_Click(object sender, EventArgs e)
        {
            flag_thread_running3 = true;
            thread_ex3 = new Thread(new ThreadStart(ThreadProc_ex3));
            thread_ex3.Name = "Thread_ex3";
            thread_ex3.Start();
            richTextBox1.Text += "啟動 thread 3, 名稱 : " + thread_ex3.Name + "\n";
        }

        private void button31_Click(object sender, EventArgs e)
        {
            if (thread_ex3 != null)
            {
                richTextBox1.Text += "停止 thread 3\n";
                thread_ex3.Abort();
            }

            //same
            flag_thread_running3 = false;
        }

        private void button32_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例3 SP

        //Thread使用範例4 ST

        private void button40_Click(object sender, EventArgs e)
        {
        }

        private void button41_Click(object sender, EventArgs e)
        {
        }

        private void button42_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例4 SP


        //Thread使用範例5 ST
        //建立一個Thread 到 偵錯/視窗/即時運算 看結果

        thread1 obj;
        Thread thread_ex5;
        private bool flag_thread_running5 = false;

        class thread1
        {
            private String title;
            public thread1(String title)
            {
                this.title = title;
            }
            int aa = 0;
            public void runMe()
            {
                while (true)
                {
                    aa++;
                    System.Diagnostics.Debug.Print("即時運算視窗輸出除錯訊息 測試訊息！！！Form1！！！ title = " + title + "  " + aa.ToString());
                    Console.Write(title + "\r\n");
                    System.Threading.Thread.Sleep(1000);
                }
            }
        }

        private void button50_Click(object sender, EventArgs e)
        {
            flag_thread_running5 = true;
            string thread_name = "Thread測試_5";
            richTextBox1.Text += "開啟thread, 名稱 : " + thread_name + "\n";
            richTextBox1.Text += "啟動 thread 5\n";
            obj = new thread1(thread_name);
            thread_ex5 = new Thread(obj.runMe);
            thread_ex5.Start();
        }

        private void button51_Click(object sender, EventArgs e)
        {
            if (thread_ex5 != null)
            {
                richTextBox1.Text += "停止 thread 5\n";
                thread_ex5.Abort();
            }

            //same
            flag_thread_running5 = false;
        }

        private void button52_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例5 SP


        //Thread使用範例6 ST

        private bool flag_thread_running6a = false;
        private bool flag_thread_running6b = false;

        private void ThreadProc_ex6a()
        {
            while (flag_thread_running6a == true)
            {
                //無限迴圈
                richTextBox1.Text += "6a";
                Thread.Sleep(500);
            }
        }

        private void ThreadProc_ex6b()
        {
            while (flag_thread_running6b == true)
            {
                //無限迴圈
                richTextBox1.Text += "6b";
                Thread.Sleep(500);
            }
        }

        private void button60_Click(object sender, EventArgs e)
        {
            flag_thread_running6a = true;
            Thread thread_ex6a = new Thread(new ThreadStart(ThreadProc_ex6a));
            thread_ex6a.IsBackground = true;
            thread_ex6a.Start();

            flag_thread_running6b = true;
            Thread thread_ex6b = new Thread(new ThreadStart(ThreadProc_ex6b));
            thread_ex6b.IsBackground = true;
            thread_ex6b.Start();
        }

        private void button61_Click(object sender, EventArgs e)
        {
            flag_thread_running6a = false;
            flag_thread_running6b = false;
        }

        private void button62_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例6 SP

        //Thread使用範例7 ST

        // Make a thread with the indicated priority.
        private void MakeThread(string thread_name, ThreadPriority thread_priority)
        {
            richTextBox1.Text += "開啟thread, 名稱 : " + thread_name + ", 優先序 : " + thread_priority.ToString() + "\n";
            Application.DoEvents();

            // Initialize the thread.
            Counter2 new_counter = new Counter2(thread_name);
            Thread thread = new Thread(new_counter.Run);
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
        private Thread thread_ex8a;
        private Thread thread_ex8b;
        int cnt8a = 0;
        int cnt8b = 0;

        private bool flag_thread_running8a = false;
        private bool flag_thread_running8b = false;


        private void ThreadProc_ex8a()
        {
            while (true)
            {
                richTextBox1.Text += "8a " + (cnt8a++).ToString() + " ";
                Thread.Sleep(500);
            }
        }

        private void ThreadProc_ex8b()
        {
            if (thread_ex8a != null)
            {
                //等待執行
                thread_ex8a.Join();//thread_ex8b 要先讓線程 thread_ex8a 執行完，然後線程 thread_ex8b 再繼續執行
            }

            while (true)
            {
                richTextBox1.Text += "8b " + (cnt8b++).ToString() + " ";
                Thread.Sleep(500);
            }
        }

        private void button80a_Click(object sender, EventArgs e)
        {
            if (thread_ex8a == null)
            {
                flag_thread_running8a = true;
                // The thread isn't running. Start it.
                cnt8a = 0;
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
                // The thread isn't running. Start it.
                cnt8b = 0;
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

        // This value is incremented by the thread.
        public int Value = 0;
        // Make and start a new counter object.
        private int thread_num = 0;

        private bool flag_thread_running9 = false;

        // Add the text to the results.
        // The form provides this service because the
        // thread cannot access the form's controls directly.
        public void DisplayValue(string txt)
        {
            richTextBox1.AppendText(txt + "\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button90_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "啟動 thread 9\n";

            // Make a new counter object.
            Counter new_counter = new Counter(this, thread_num);
            richTextBox1.Text += "開啟thread, 編號 " + thread_num.ToString() + "\n";
            thread_num++;

            // Make a thread to run the object's Run method.
            Thread thread_ex9 = new Thread(new_counter.Run);

            // Make this a background thread so it automatically
            // aborts when the main program stops.
            thread_ex9.IsBackground = true;

            // Start the thread.
            thread_ex9.Start();
        }

        private void button91_Click(object sender, EventArgs e)
        {
            //same
            flag_thread_running9 = false;
        }

        private void button92_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例9 SP


        //Thread使用範例10 ST

        Random r = new Random(Guid.NewGuid().GetHashCode());
        private int _R = 0, _G = 0, _B = 0;
        private Thread thread_ex10;
        private bool flag_thread_running10 = false;

        private void ThreadProc_ex10()
        {
            while (true)
            {
                _R = r.Next(256);
                _G = r.Next(256);
                _B = r.Next(256);
                Thread.Sleep(100);
            }
        }

        private void button100_Click(object sender, EventArgs e)
        {
            thread_ex10 = new Thread(ThreadProc_ex10);

            if (thread_ex10.IsAlive == false)
            {
                thread_ex10.Start();
            }
        }

        private void button101_Click(object sender, EventArgs e)
        {
            if (thread_ex10 != null)
            {
                richTextBox1.Text += "停止 thread 10\n";
                thread_ex10.Abort();
            }

            //same
            flag_thread_running10 = false;
        }

        private void button102_Click(object sender, EventArgs e)
        {

        }

        private void timer_rgb_Tick(object sender, EventArgs e)
        {
            lb_R.Text = _R.ToString();
            lb_G.Text = _G.ToString();
            lb_B.Text = _B.ToString();
        }

        //Thread使用範例10 SP


        //Thread使用範例11 ST

        private void button110_Click(object sender, EventArgs e)
        {

        }

        private void button111_Click(object sender, EventArgs e)
        {

        }

        private void button112_Click(object sender, EventArgs e)
        {

        }

        //Thread使用範例11 SP
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
        public void Run()
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
        public void Run()
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
        }
    }
}


/*

                //一秒執行一次
                Thread.Sleep(1000); //停一秒

 
*/