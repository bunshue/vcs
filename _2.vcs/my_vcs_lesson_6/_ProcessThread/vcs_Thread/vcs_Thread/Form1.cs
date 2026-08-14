using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;  // 匯入多執行緒功能函數
using System.Diagnostics;  // for Process
using System.Timers;  // for ElapsedEventHandler

namespace vcs_Thread
{
    public partial class Form1 : Form
    {
        private Thread thread_ex0;
        static Thread thread_ex2a = null;
        static Thread thread_ex2b = null;
        private Thread thread_ex8a;
        private Thread thread_ex8b;
        private Thread thread_ex10;
        private Thread thread_ex11;

        private bool flag_thread_running8a = false;
        private bool flag_thread_running8b = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            //CheckForIllegalCrossThreadCalls = false; 另法
            get_cpu_useage();

            Thread.CurrentThread.Name = "MainThread";  // 設置這個線程的名字
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

            if (thread_ex11 != null)
            {
                thread_ex11.Abort();
            }

            //C# 強制關閉 Process
            Process.GetCurrentProcess().Kill();

            Application.Exit();
        }

        void show_item_location()
        {
            int W = 200;
            int H = 240;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;
            groupBox0.Size = new Size(W, H);
            groupBox1.Size = new Size(W, H);
            groupBox2.Size = new Size(W, H);
            groupBox3.Size = new Size(W, H);
            groupBox4.Size = new Size(W, H);
            groupBox8.Size = new Size(W, H);
            groupBox13.Size = new Size(W, H);
            groupBox12.Size = new Size(W, H);
            groupBox14.Size = new Size(W * 2 + 10, H);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            groupBox4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox8.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox13.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            groupBox12.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            groupBox14.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            groupBox11.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            richTextBox1.Size = new Size(500, 690 + 50);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 10;
            y_st = 20;
            W = 180;
            H = 60;
            dx = W + 10;
            dy = H + 10;
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
            button80a.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button81a.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button80b.Location = new Point(x_st + dx * 0 + 90, y_st + dy * 0);
            button81b.Location = new Point(x_st + dx * 0 + 90, y_st + dy * 1);
            button82.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_R.Location = new Point(x_st + dx * 0 + 130, y_st + dy * 0);
            lb_G.Location = new Point(x_st + dx * 0 + 130, y_st + dy * 1);
            lb_B.Location = new Point(x_st + dx * 0 + 130, y_st + dy * 2);

            this.Size = new Size(1380, 750 + 50);
            this.Text = "vcs_Thread";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        //Thread使用範例0 ST

        int count0 = 0;
        private void ThreadProc_ex0()
        {
            richTextBox1.Text += "啟動一個thread0 ";
            for (int i = 0; i < 10; i++)
            {

                richTextBox1.Text += count0.ToString() + " ";
                Thread.Sleep(500);
                count0++;
            }
            richTextBox1.Text += "\n結束 ThreadProc_ex0\n";
        }

        private void button00_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "啟動 thread 0\n";

            //thread_ex0 = new Thread(ThreadProc_ex0);//same
            thread_ex0 = new Thread(new ThreadStart(ThreadProc_ex0));
            thread_ex0.Name = "Thread_ex0";  // 設置這個線程的名字
            //thread_ex0.IsBackground = true;  //設定為背景執行緒, 這樣能隨主程序一起結束
            thread_ex0.Start();

            richTextBox1.Text += "啟動 thread 0, 名稱 : " + thread_ex0.Name + "\n";
        }

        private void button01_Click(object sender, EventArgs e)
        {
            if (thread_ex0 != null)
            {
                richTextBox1.Text += "停止 thread 0\n";
                thread_ex0.Abort();
            }
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
                    //是否為 背景執行緒
                    richTextBox1.Text += "IsBackground\t" + thread_ex0.IsBackground.ToString() + "\n";
                }
            }
        }
        //Thread使用範例0 SP

        //------------------------------------------------------------  # 60個

        //Thread使用範例1 ST

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例1 SP

        //------------------------------------------------------------  # 60個

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
            thread_ex2a.Name = "Thread_ex2a";  // 設置這個線程的名字

            thread_ex2b = new Thread(ThreadProc_ex2);
            thread_ex2b.Name = "Thread_ex2b";  // 設置這個線程的名字

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
                thread_ex2a.Name = "Thread_ex2a";  // 設置這個線程的名字
                thread_ex2a.Start();
                richTextBox1.Text += "啟動 thread 2a, 名稱 : " + thread_ex2a.Name + "\n";
            }
            if (thread_ex2b.ThreadState == System.Threading.ThreadState.Aborted)
            {
                thread_ex2b = new Thread(ThreadProc_ex2);
                thread_ex2b.Name = "Thread_ex2b";  // 設置這個線程的名字
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
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //狀態
            richTextBox1.Text += "Thread_ex2a 狀態 : " + thread_ex2a.ThreadState + "\n";
            richTextBox1.Text += "Thread_ex2b 狀態 : " + thread_ex2b.ThreadState + "\n";
        }
        //Thread使用範例2 SP

        //------------------------------------------------------------  # 60個

        //Thread使用範例3 ST

        private void button30_Click(object sender, EventArgs e)
        {
        }

        private void button31_Click(object sender, EventArgs e)
        {
        }

        private void button32_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例3 SP

        //------------------------------------------------------------  # 60個

        //Thread使用範例4 ST

        Random rand = new Random();

        private int _R = 0, _G = 0, _B = 0;

        private void ThreadProc_ex10()
        {
            richTextBox1.Text += "啟動一個thread10 ";
            while (true)
            {
                _R = rand.Next(256);
                _G = rand.Next(256);
                _B = rand.Next(256);
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

        //------------------------------------------------------------  # 60個

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
                thread_ex8a.IsBackground = true;  //設定為背景執行緒, 這樣能隨主程序一起結束
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
                thread_ex8b.IsBackground = true;  //設定為背景執行緒, 這樣能隨主程序一起結束
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

        //------------------------------------------------------------  # 60個

        //Thread使用範例 時鐘 ST

        public void setResult(int value)
        {
            lb_thread.Text = "結果 : " + value.ToString();
        }

        //委派function
        public delegate void InvokeFunction(int value);

        private ChangeTime timechange;

        private void bt_start_Click(object sender, EventArgs e)
        {
            //啟動時鐘
            //產生一個類別，專門來管理時間運作
            timechange = new ChangeTime(this);

            Thread th = new Thread(new ThreadStart(timechange.run));
            th.Start();
        }

        private void bt_stop_Click(object sender, EventArgs e)
        {
            if (timechange != null)
            {
                timechange.stop();
            }
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {

        }

        //Thread使用範例 時鐘 SP

        //------------------------------------------------------------  # 60個

        //Thread使用範例 CPU使用率 ST
        Thread thread_cpu;
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
        private void get_cpu_useage()
        {
            lb_cpu1.Text = cpu_count.ToString() + " %";
            lb_cpu2.Text = "CPU使用率：" + lb_cpu1.Text;
            mheight = Convert.ToInt32(cpu_count.ToString());
            if (mheight == 100)
            {
                panel3.Height = 100;
            }
            CreateImage();
            cpu_count += 3;
            if (cpu_count > 100)
            {
                cpu_count -= 100;
            }
        }

        private void timer11_Tick(object sender, EventArgs e)
        {
            thread_cpu = new Thread(new ThreadStart(get_cpu_useage));
            thread_cpu.Start();
        }
        //Thread使用範例 CPU使用率 SP

        //------------------------------------------------------------  # 60個

        private void button110_Click(object sender, EventArgs e)
        {
            thread_ex11 = new Thread(new ThreadStart(ThreadProc_ex11));
            thread_ex11.Start();

            /*
            //看 thread的狀態
            while (thread_ex11.ThreadState != ThreadState.Stopped)
            {
                richTextBox1.Text += "忙碌中\n";
                richTextBox1.Text += thread_ex11.IsBackground + "\n";//看是否為後台/前台線程
                Application.DoEvents();
                Thread.Sleep(500);//當前執行緒 休息100ms
            }
            richTextBox1.Text += "完成\n";
            */

            /*
            //執行緒等待
            thread_ex11.Join(500);//最多等待500ms
            Console.WriteLine("最多等待500ms");
            thread_ex11.Join();//主執行緒等待thread_ex11完成, 主執行緒會卡在這裡, 等thread_ex11做完
            */
        }

        private void ThreadProc_ex11()
        {
            richTextBox1.Text += "要做很久的事 ST\t";
            delay(5000);
            richTextBox1.Text += "要做很久的事 SP\t";
        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(double delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        private void button111_Click(object sender, EventArgs e)
        {

        }

        private void button112_Click(object sender, EventArgs e)
        {
            //狀態

        }

        //------------------------------------------------------------  # 60個

        static void f1()
        {
            System.Threading.Thread y = new System.Threading.Thread(new System.Threading.ThreadStart(f2));
            y.Start();
            y.Join();
            Console.WriteLine("This is F1.{0}", 1);
        }

        static void f2()
        {
            Console.WriteLine("This is F2.{0}", 1);
        }

        private void button140_Click(object sender, EventArgs e)
        {
            //新進 0

            //Thread.Join()用法的理解
            //指在一線程裡面調用另一線程join方法時，表示將本線程阻塞直至另一線程終止時再執行

            System.Threading.Thread x = new System.Threading.Thread(new System.Threading.ThreadStart(f1));
            x.Start();
            Console.WriteLine("This is Main.{0}", 1);

            x.Join();  // 比較這行有無的狀況

            Console.WriteLine("This is Main.{0}", 2);
            Console.ReadLine();
        }

        //------------------------------------------------------------  # 60個

        private void button141_Click(object sender, EventArgs e)
        {
            //新進 1
            //使用 ThreadPool

            Console.WriteLine("主執行緒開始工作...");

            // 把耗時工作丟到 ThreadPool
            ThreadPool.QueueUserWorkItem(HeavyWork);

            Console.WriteLine("主執行緒繼續執行，不會被阻塞。");
        }

        static void HeavyWork(object state)
        {
            long sum = 0;
            for (int i = 0; i < 100000000; i++)
            {
                sum += i;
            }
            Console.WriteLine("背景工作完成! 結果 = " + sum);
        }

        //------------------------------------------------------------  # 60個

        private void button142_Click(object sender, EventArgs e)
        {
            //新進 2

        }

        //------------------------------------------------------------  # 60個

        private void MotionReaction()
        {
            richTextBox1.Text += "建立一個Thread : " + Thread.CurrentThread.Name + "\n";

            for (int i = 0; i < 5; i++)
            {
                richTextBox1.Text += Thread.CurrentThread.Name + " ";
                Thread.Sleep(1000);
            }

            richTextBox1.Text += "Thread : " + Thread.CurrentThread.Name + ", 完成\n";
        }

        int thread_index = 0;
        private void button143_Click(object sender, EventArgs e)
        {
            //新進 3

            // 累計建立多個thread

            Thread th = new Thread(MotionReaction);
            th.Name = thread_index.ToString();  // 設置這個線程的名字
            th.Start();

            thread_index++;
        }

        //------------------------------------------------------------  # 60個

        private void button144_Click(object sender, EventArgs e)
        {
            //新進 4

        }

        //------------------------------------------------------------  # 60個

        private void button145_Click(object sender, EventArgs e)
        {
            //新進 5

        }
        //------------------------------------------------------------  # 60個
    }

    //------------------------------------------------------------  # 60個

    class ChangeTime
    {
        private Form1 form;

        private Boolean state = true;

        private int value;

        public ChangeTime(Form1 form1)
        {
            this.form = form1;

            //設定數值
            DateTime date = DateTime.Now;
            value = date.Second;
        }

        //停止thread,在form Dispose時要把thread也設定關掉
        public void stop()
        {
            state = false;
        }

        public void run()
        {
            while (state == true)
            {
                value++;

                //一定要使用form裡的thread才可以變動form上的元件內容，其它thread更動時會有問題
                //利用invoke來執行form的thread
                if (state)//如果已經Dispose掉了就不再invoke了
                {
                    form.Invoke(new Form1.InvokeFunction(form.setResult), new object[] { value });
                }
                //一秒執行一次
                Thread.Sleep(1000);//停一秒
            }
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*

//一秒執行一次
Thread.Sleep(1000); //停一秒

//richTextBox1.Text += "XX ";
Console.Write("XX ");

//------------------------------------------------------------  # 60個

程式只能同時運行一個  在Form1_Load加入:

        private void Form1_Load(object sender, EventArgs e)
        {
            bool Exist;//定義一個bool變量 用來表示是否已經運行
            //創建Mutex互斥對象
            System.Threading.Mutex newMutex = new System.Threading.Mutex(true, "僅一次", out Exist);
            if (Exist)//如果沒有運行
            {
                newMutex.ReleaseMutex();//運行新窗体
            }
            else
            {
                MessageBox.Show("本程式一次只能運行一個實例！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);//彈出提示信息
                this.Close();//關閉當前窗体
            }
        }

//------------------------------------------------------------  # 60個

主程式持續進行，開啟thread做一些事，thread做事時，主程式依舊不耽擱

thread工作型態
1. 建立一個thread，讓他無限迴圈地等待做一件事，直到外面叫他停止		印表機、
2. 建立一個thread，只做一件事，做完即結束				去搬便當、

停止 thread 的3個方法
1. 強制停止 .Abort()
2. 使用 flag 讓 thread 中斷運行
3. 事情做完 thread即停止

//無限迴圈
richTextBox1.Text += "0";
Thread.Sleep(500);

//------------------------------------------------------------  # 60個

利用线程的方法 做延时 不卡界面

Thread thread_ex5 = new Thread(o => Thread.Sleep(500));
thread_ex5.Start(this);
while (thread_ex5.IsAlive)
{
    Application.DoEvents();
}

不用线程 也可以这样不卡界面 
public static void Delay(int mm)
{
    DateTime current = DateTime.Now;
    while (current.AddMilliseconds(mm) > DateTime.Now)
    {
        Application.DoEvents();
    }
    return;
} 

//------------------------------------------------------------  # 60個

//线程常用的方法

/// <summary>
/// 一个示例方法 - 无参数
/// </summary>
private void TestMethod()
{
    Console.WriteLine("我是测试线程");
}
//无参数线程的创建
Thread thread_ex8a = new Thread(TestMethod);

/// <summary>
/// 一个示例方法 - 有参数
/// </summary>
private void TestMethod(int Obj)
{
    Console.WriteLine("我是测试线程");
}
//有参数线程的创建
int Obj = 0;
Thread thread_ex8b = new Thread(() => TestMethod(Obj));

//如果要设置线程为MTA模型
thread_ex8b.SetApartmentState(ApartmentState.MTA);

//线程挂起（类似线程暂停）
thread_ex8b.Suspend();

//线程恢复（将挂起线程恢复运行状态）
thread_ex8b.Resume();

//线程强制终止（强制退出）
thread_ex8b.Abort();
//为了保证线程被终止，要加入一句Join
thread_ex8b.Join();

//得到当前线程的名字
string MyThreadName = Thread.CurrentThread.Name;

//判断线程是否存活
if (thread_ex8b.IsAlive)
{
    //如果存活，则执行....
}

//------------------------------------------------------------  # 60個

Thread.Sleep()方法用於將當前線程休眠一定時間,時間單位是毫秒。
在阻塞時線程狀態是 ThreadState.WaitSleepJoin， 在休眠的時間裡讓其他等待線程先執行，可以減少CPU的占用時間。

c# Delay 1秒鐘寫法
using System.Threading;
Thread.Sleep(1000); //Delay 1秒，不好用，因為這段時間會卡住
System.Threading.Thread.Sleep(2000);當前休眠2秒，
System.Threading.Thread.Sleep(5000);當前休眠5秒，
System.Threading.Thread.Sleep(5000); // wait 5 seconds (5000 milliseconds)

//------------------------------------------------------------  # 60個

進程 :
我們可以把計算機中每一個運行的應用程序當作是一個進程

線程 :
每一個進程是由多個線程組成的。
單線程：讓程序做多件事時，會引發卡死 假死狀態。
多線程：讓一個程序同時處理多個事情，後台運行程序，提高程序的運行效率。
前台線程：只有所有的前台線程都關閉才能完成程序關閉。(winform多窗口時)
後台線程：只要所有的前台線程結束，後台線程自動結束。

 1 //實例化Thread類，並傳入一個指向線程所要運行的方法。（這時線程已經產生，但還沒有運行）
 2 //調用Thread類的Start方法，標記線程可以被CPU執行了，但具體執行事件由CPU決定。
 3 Thread thread_ex6 = new Thread(Test); //創建一個線程去執行這個方法。
 6 //在.net下是不允許跨線程訪問的。
 7 //有時候需要手動釋放線程 關閉時 判斷線程是否關閉 
 8 if (thread_ex6 != null)
 9 {
10     thread_ex6.Abort(); //結束這個線程 不能再Start()
11 }
12 Thread.Sleep(3000); //睡眠3秒後執行
13 //線程執行帶參數方法
14 Thread.Start("123")； object類型參數 在start後括號寫參數

//多用於大量數據時，多分一個線程去搜索數據，然後存儲到緩存裡，頁面再用異步獲取緩存中的數據。

//------------------------------------------------------------  # 60個

停止一個線程

Thread.Sleep 方法能夠在一個固定周期類停止一個線程

thread.Sleep(); 
 
設定線程優先級
線程類中的ThreadPriority 屬性是用來設定一個ThreadPriority的優先級別。
線程優先級別包括Normal, AboveNormal, BelowNormal, Highest, and Lowest幾種。
	
thread.Priority = ThreadPriority.Highest; 
thread.Priority = ThreadPriority.Lowest;
                  ThreadPriority.BelowNormal
                  ThreadPriority.Normal
                  ThreadPriority.AboveNormal

掛起一個線程
調用線程類的Suspend()方法將掛起一個線程直到使用Resume()方法喚起她。在掛起一個線程起前應該判斷線程是否在活動期間。

if (thread.ThreadState = ThreadState.Running )
{
	thread.Suspend();
} 

喚起一個線程

通過使用Resume()方法可以喚起一個被掛起線程。在掛起一個線程起前應該判斷線程是否在掛起期間，如果
線程未被掛起則方法不起作用。

if (thread.ThreadState = ThreadState.Suspended )
{
	thread.Resume();
} 

//------------------------------------------------------------  # 60個

//這裡獲取線程的名字
//string threadName = Thread.CurrentThread.Name;

//讓線程變為後台線程（默認是前台的），這樣主線程結束了，這個線程也會結束。要不然，任何前台線程在運行都會保持程序存活。
thread_ex9b.IsBackground = true;  //設定為背景執行緒, 這樣能隨主程序一起結束

*/

