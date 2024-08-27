using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for Process
using System.Threading;   //匯入多執行緒功能函數

using System.Timers;    //for ElapsedEventHandler

namespace vcs_Thread_Example3
{
    //創建SetValue的委托
    public delegate void SetValueDel(string str, object obj);

    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            Thread.CurrentThread.Name = "MainThread";
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (timechange != null)
            {
                //把thread停掉
                timechange.stop();
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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
        private void button1_Click(object sender, EventArgs e)
        {
            //啟動時鐘
            //產生一個類別，專門來管理時間運作
            timechange = new ChangeTime(this);
            //timechange.change();

            //使用一個thread來增加時間的秒數
            System.Threading.Thread thread = new System.Threading.Thread(new System.Threading.ThreadStart(timechange.run));
            thread.Start();

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //關閉時鐘
            if (timechange != null)
                timechange.stop();
        }


        //開啟一個線程
        int aaaa = 0;

        //給文本框賦值
        private void SetValue(string str, object obj)
        {
            //lock裡面的代碼同一個時刻，只能被一個線程使用。其它的後面排隊。這樣防止數據混亂。
            lock (obj)
            {
                richTextBox1.Text += "Thread名稱 : " + str + " 做事 " + DateTime.Now.ToString() + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "第2種Thread使用\n";
            //將委托的方法和主窗體傳過去
            NEWThreadClass threadOneClass = new NEWThreadClass(SetValue, this);

            aaaa++;
            string thread_name = "Thread測試_" + aaaa.ToString();

            Thread TheThreadOne = new Thread(threadOneClass.threadOne);//不需要ThreadStart()也可以
            TheThreadOne.Name = thread_name;

            richTextBox1.Text += "開啟thread, 名稱 : " + TheThreadOne.Name + "\n";

            //讓線程變為後台線程（默認是前台的），這樣主線程結束了，這個線程也會結束。要不然，任何前台線程在運行都會保持程序存活。
            TheThreadOne.IsBackground = true;
            TheThreadOne.Start();

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
