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
        private Thread my_thread;

        private void run_my_threaed()
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
            my_thread = new Thread(run_my_threaed);

            if (my_thread.IsAlive == false)
            {
                my_thread.Start();
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            my_thread.Abort();
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
            richTextBox1.Text += "第1種Thread使用\n";
            // Make a new counter object.
            Counter new_counter = new Counter(this, thread_num);
            richTextBox1.Text += "開啟thread, 編號 " + thread_num.ToString() + "\n";
            thread_num++;

            // Make a thread to run the object's Run method.
            Thread counter_thread = new Thread(new_counter.Run);

            // Make this a background thread so it automatically
            // aborts when the main program stops.
            counter_thread.IsBackground = true;

            // Start the thread.
            counter_thread.Start();

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
            }
            if (thread_ex2b.ThreadState == System.Threading.ThreadState.Aborted)
            {
                thread_ex2b = new Thread(ThreadProc_ex2);
                thread_ex2b.Name = "Thread_ex2";
                thread_ex2b.Start();
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //停止
            thread_ex2a.Abort();
            thread_ex2b.Abort();

        }

        private void button8_Click(object sender, EventArgs e)
        {
            //狀態
            richTextBox1.Text += "Thread_ex1 狀態 : " + thread_ex2a.ThreadState + "\n";
            richTextBox1.Text += "Thread_ex2 狀態 : " + thread_ex2b.ThreadState + "\n";
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
