using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Diagnostics;
using System.Timers;    //for ElapsedEventHandler

namespace vcs_Thread_Example2
{
    public partial class Form1 : Form
    {
        private Thread thread_ex1;
        private bool flag_thread_running = false;

        // This value is incremented by the thread.
        public int Value = 0;
        // Make and start a new counter object.
        private int thread_num = 0;

        static Thread thread_ex2a;
        static Thread thread_ex2b;
        static Thread thread_ex3 = null;
        Thread thread_ex4;                                  //宣告監聽用執行續

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            thread_ex2a = new Thread(ThreadProc_ex2);
            thread_ex2a.Name = "Thread_ex1";

            thread_ex2b = new Thread(ThreadProc_ex2);
            thread_ex2b.Name = "Thread_ex2";
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //關閉監聽執行續(如果有的話)
            try
            {
                thread_ex4.Abort(); //關閉監聽執行續
                //U.Close();  //關閉監聽器
            }
            catch
            {
                //忽略錯誤，程式繼續執行
            }

            //C# 強制關閉 Process
            Process.GetCurrentProcess().Kill();

            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (flag_thread_running == false)
            {
                flag_thread_running = true;
                button1.Text = "停止";
                thread_ex1 = new Thread(new ThreadStart(this.ThreadProc_ex1));
                thread_ex1.Start();
            }
            else
            {
                button1.Text = "啟動";
                flag_thread_running = false;
                richTextBox1.Text += "\n";
            }
        }

        private void ThreadProc_ex1()
        {
            richTextBox1.Text += "啟動一個thread ";
            while (flag_thread_running)
            {
                //無限迴圈
                richTextBox1.Text += "A";

                Thread.Sleep(500);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Thread t = new Thread(new ParameterizedThreadStart(delegate(object obj)
            {
                while (true)
                {
                    Thread.Sleep(400);
                    if (this.BackColor == Color.Green)
                    {
                        this.BackColor = Color.Pink;
                    }
                    else
                    {
                        this.BackColor = Color.Green;
                    }
                }
            }));
            t.Name = " --start tray thread";
            t.IsBackground = true;
            t.Priority = ThreadPriority.Lowest;
            t.Start(null);

        }

        //螢幕畫素讀取 ST

        Random r = new Random(Guid.NewGuid().GetHashCode());
        private int _R = 0, _G = 0, _B = 0;
        private Thread thread_ex8;

        private void ThreadProc_ex8()
        {
            while (true)
            {
                _R = r.Next(256);
                _G = r.Next(256);
                _B = r.Next(256);
                Thread.Sleep(100);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            thread_ex8 = new Thread(ThreadProc_ex8);

            if (thread_ex8.IsAlive == false)
            {
                thread_ex8.Start();
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "停止 thread thread_ex8\n";
            thread_ex8.Abort();
        }

        private void timer_rgb_Tick(object sender, EventArgs e)
        {
            lb_R.Text = _R.ToString();
            lb_G.Text = _G.ToString();
            lb_B.Text = _B.ToString();
        }
        //螢幕畫素讀取 SP

        //第1種Thread使用
        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "啟動 thread 9\n";

            richTextBox1.Text += "第1種Thread使用\n";
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
        // Add the text to the results.
        // The form provides this service because the
        // thread cannot access the form's controls directly.
        public void DisplayValue(string txt)
        {
            richTextBox1.AppendText(txt + "\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

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

        private void button6_Click(object sender, EventArgs e)
        {
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

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "停止 thread 2a\n";
            thread_ex2a.Abort();

            richTextBox1.Text += "停止 thread 2b\n";
            thread_ex2b.Abort();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //狀態
            richTextBox1.Text += "Thread_ex1 狀態 : " + thread_ex2a.ThreadState + "\n";
            richTextBox1.Text += "Thread_ex2 狀態 : " + thread_ex2b.ThreadState + "\n";
        }

        public void ThreadProc_ex3()
        {
            while (true)
            {
                Console.WriteLine("Hello from a single thread.");
                Thread.Sleep(1000);
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            thread_ex3 = new Thread(new ThreadStart(ThreadProc_ex3));
            thread_ex3.Name = "Thread_ex3";
            thread_ex3.Start();
            richTextBox1.Text += "啟動 thread 3, 名稱 : " + thread_ex3.Name + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //停止一個Thread
            if (thread_ex3 != null)
            {
                thread_ex3.Abort();
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {

        }


        //監聽副程式
        int i;
        private void ThreadProc_ex4()
        {
            while (true)
            {
                i++;
                this.Text = i.ToString();
                richTextBox1.Text += "m";

                //一秒執行一次
                Thread.Sleep(1000); //停一秒
            }
        }
        int cnt = 0;
        private void button14_Click(object sender, EventArgs e)
        {
            thread_ex4 = new Thread(ThreadProc_ex4); //建立監聽網路訊息的新執行緒
            thread_ex4.Name = "Thread_ex4_" + cnt.ToString();
            //thread_ex4.IsBackground = true;  //設定為背景執行緒
            thread_ex4.Start();             //啟動監聽執行緒
            richTextBox1.Text += "啟動 thread 4, 名稱 : " + thread_ex4.Name + "\n";
            cnt++;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            if (thread_ex4 != null)
            {
                richTextBox1.Text += "關閉 Main Thread\n";
                thread_ex4.Abort();
            }
            else
            {
                richTextBox1.Text += "無Thread\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Info\n";
            if (thread_ex4 == null)
            {
                richTextBox1.Text += "Main Thread 尚未啟動\n";
            }
            else
            {
                richTextBox1.Text += "Main Thread\t" + thread_ex4.ToString() + "\n";
                richTextBox1.Text += "ThreadState\t" + thread_ex4.ThreadState.ToString() + "\n";
                richTextBox1.Text += "Name\t" + thread_ex4.Name + "\n";
                richTextBox1.Text += "IsAlive\t" + thread_ex4.IsAlive.ToString() + "\n";

                if (thread_ex4.IsAlive == true)
                {
                    richTextBox1.Text += "IsBackground\t" + thread_ex4.IsBackground.ToString() + "\n";
                }
            }
        }

        thread1 obj;
        Thread thread_ex5;

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

        int a = 0;
        //建立一個Thread 到 偵錯/視窗/即時運算 看結果
        private void button17_Click(object sender, EventArgs e)
        {
            a++;
            string thread_name = "Thread測試_" + a.ToString();
            richTextBox1.Text += "開啟thread, 名稱 : " + thread_name + "\n";
            richTextBox1.Text += "啟動 thread 5\n";
            obj = new thread1(thread_name);
            thread_ex5 = new Thread(obj.runMe);
            thread_ex5.Start();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            thread_ex5.Abort();
        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        //開啟關閉thread    ST
        System.Timers.Timer tt = new System.Timers.Timer(1234);
        int number = 0;

        public void run(object source, System.Timers.ElapsedEventArgs e)
        {
            number++;
            System.Diagnostics.Debug.Print("即時運算視窗輸出除錯訊息 測試訊息！！！Form1！！！ " + number.ToString());
            Console.Write(number.ToString() + "\r\n");

            //MessageBox.Show("number = " + number);
        }

        private void button20_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "啟動 thread 6\n";

            tt.Elapsed += new ElapsedEventHandler(run);
            tt.Enabled = true;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            tt.Enabled = false;
            number = 0;

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void ThreadProc_ex6a()
        {
            while (true)
            {
                Console.Write("A");
                richTextBox1.Text += "A";

                Thread.Sleep(300);
            }
        }

        private void ThreadProc_ex6b()
        {
            while (true)
            {
                Console.Write("B");
                richTextBox1.Text += "B";

                Thread.Sleep(1000);
            }
        }

        private void button26_Click(object sender, EventArgs e)
        {
            Thread thread_ex6a = new Thread(new ThreadStart(ThreadProc_ex6a));
            thread_ex6a.IsBackground = true;
            thread_ex6a.Start();

            Thread thread_ex6b = new Thread(new ThreadStart(ThreadProc_ex6b));
            thread_ex6b.IsBackground = true;
            thread_ex6b.Start();

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }
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
}
