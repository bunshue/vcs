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

        static Thread thread_ex3 = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
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
