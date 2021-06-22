using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;   //匯入多執行緒功能函數

namespace vcs_Thread3
{
    //創建SetValue的委托
    public delegate void SetValueDel(string str, object obj);

    public partial class Form1 : Form
    {
        // This value is incremented by the thread.
        public int Value = 0;

        // Make and start a new counter object.
        private int thread_num = 0;

        Thread Th;                                  //宣告監聽用執行續

        public Form1()
        {
            InitializeComponent();
            Thread.CurrentThread.Name = "MainThread";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Control.CheckForIllegalCrossThreadCalls = false; //忽略跨執行緒操作的錯誤
        }

        //第1種Thread使用
        private void button1_Click(object sender, EventArgs e)
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



        //第2種Thread使用

        //開啟一個線程
        int a = 0;
        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "第2種Thread使用\n";
            //將委托的方法和主窗體傳過去
            NEWThreadClass threadOneClass = new NEWThreadClass(SetValue, this);

            a++;
            string thread_name = "Thread測試_" + a.ToString();

            Thread TheThreadOne = new Thread(threadOneClass.threadOne);//不需要ThreadStart()也可以
            TheThreadOne.Name = thread_name;

            richTextBox1.Text += "開啟thread, 名稱 : " + TheThreadOne.Name + "\n";

            //讓線程變為後台線程（默認是前台的），這樣主線程結束了，這個線程也會結束。要不然，任何前台線程在運行都會保持程序存活。
            TheThreadOne.IsBackground = true;
            TheThreadOne.Start();
        }

        //給文本框賦值
        private void SetValue(string str, object obj)
        {
            //lock裡面的代碼同一個時刻，只能被一個線程使用。其它的後面排隊。這樣防止數據混亂。
            lock (obj)
            {
                richTextBox1.Text += "Thread名稱 : " + str + " 做事 " + DateTime.Now.ToString() + "\n";
            }
        }


        //第3種Thread使用

        // Start threads with different priorities.
        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "第3種Thread使用\n";
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

        //監聽副程式
        int i;
        private void Listen()
        {
            while (true)
            {
                i++;
                this.Text = i.ToString();

                //一秒執行一次
                Thread.Sleep(1000); //停一秒
            }
        }

        //關閉監聽執行續(如果有的話)
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            try
            {
                Th.Abort(); //關閉監聽執行續
                //U.Close();  //關閉監聽器
            }
            catch
            {
                //忽略錯誤，程式繼續執行
            }
        }

        int cnt = 0;
        private void bt_th1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "啟動Thread\n";
            Th = new Thread(Listen); //建立監聽網路訊息的新執行緒
            //Th.IsBackground = true;  //設定為背景執行緒
            Th.Name = "my_thread" + cnt.ToString();
            cnt++;

            Th.Start();             //啟動監聽執行緒
        }

        private void bt_th2_Click(object sender, EventArgs e)
        {
            if (Th != null)
            {
                richTextBox1.Text += "關閉Thread\n";
                Th.Abort();
            }
            else
            {
                richTextBox1.Text += "無Thread\n";
            }
        }

        private void bt_th3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Info\n";
            if (Th == null)
            {
                richTextBox1.Text += "XXXXXX\n";
            }
            else
            {
                richTextBox1.Text += "Th\t" + Th.ToString() + "\n";
                richTextBox1.Text += "ThreadState\t" + Th.ThreadState.ToString() + "\n";

                richTextBox1.Text += "Name\t" + Th.Name + "\n";
                richTextBox1.Text += "IsAlive\t" + Th.IsAlive.ToString() + "\n";
                if (Th.IsAlive == true)
                    richTextBox1.Text += "IsBackground\t" + Th.IsBackground.ToString() + "\n";
            }
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
                // An unexpected error.
                Console.WriteLine("Unexpected error in thread " + Number + "\r\n" + ex.Message);
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
            { }
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

