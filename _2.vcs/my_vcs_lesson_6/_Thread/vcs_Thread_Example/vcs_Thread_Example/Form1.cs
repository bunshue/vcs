using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;     //for Thread

namespace vcs_Thread_Example
{
    public partial class Form1 : Form
    {
        private ChangeTime timechange;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效
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

        private void button2_Click(object sender, EventArgs e)
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

        // 色塊 ST
        private Thread MyThread;
        int cnt = 0;

        private void button4_Click(object sender, EventArgs e)
        {
            if (MyThread == null)
            {
                // The thread isn't running. Start it.
                cnt = 0;
                MyThread = new Thread(DoThread);
                MyThread.Priority = ThreadPriority.BelowNormal;
                MyThread.IsBackground = true;
                MyThread.Start();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (MyThread != null)
            {
                // The thread is running. Stop it.
                MyThread.Abort();
                MyThread = null;
            }
        }

        private void DoThread()
        {
            while (true)
            {
                if (this.pictureBox1.BackColor == Color.White)
                    this.pictureBox1.BackColor = Color.Red;
                else
                    this.pictureBox1.BackColor = Color.White;

                label6.Text = (cnt++).ToString();

                Application.DoEvents();
                Thread.Sleep(200);
            }
        }
        // 色塊 SP

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (MyThread != null)
            {
                // The thread is running. Stop it.
                MyThread.Abort();
                MyThread = null;
            }

            if (timechange != null)
                timechange.stop();
        }

        //啟動時鐘
        private void button5_Click(object sender, EventArgs e)
        {
            //產生一個類別，專門來管理時間運作
            timechange = new ChangeTime(this);
            //timechange.change();

            //使用一個thread來增加時間的秒數
            System.Threading.Thread thread = new System.Threading.Thread(new System.Threading.ThreadStart(timechange.run));
            thread.Start();
        }

        //關閉時鐘
        private void button6_Click(object sender, EventArgs e)
        {
            if (timechange != null)
                timechange.stop();
        }
    }
}

