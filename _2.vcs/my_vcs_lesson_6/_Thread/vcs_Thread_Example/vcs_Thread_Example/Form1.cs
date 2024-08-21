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
        //色塊 ST
        private Thread ThreadA;
        private Thread ThreadB;
        int cnt1 = 0;
        int cnt2 = 0;
        //色塊 SP

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

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //殺死一個線程
            if (ThreadA != null)
            {
                if (ThreadA.IsAlive)//線程類的 Abort() 方法可以永久的殺死一個線程。在殺死一個線程起前應該判斷線程是否在生存期間。
                {
                    ThreadA.Abort();
                }
                ThreadA = null;
            }

            //殺死一個線程
            if (ThreadB != null)
            {
                if (ThreadB.IsAlive)//線程類的 Abort() 方法可以永久的殺死一個線程。在殺死一個線程起前應該判斷線程是否在生存期間。
                {
                    ThreadB.Abort();
                }
                ThreadB = null;
            }

            if (timechange != null)
            {
                timechange.stop();
            }
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

        // 色塊 ST
        private void button4_Click(object sender, EventArgs e)
        {
            if (ThreadA == null)
            {
                // The thread isn't running. Start it.
                cnt1 = 0;
                ThreadA = new Thread(DoThreadA);
                ThreadA.Priority = ThreadPriority.BelowNormal;
                ThreadA.IsBackground = true;
                ThreadA.Start();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //殺死一個線程
            if (ThreadA != null)
            {
                if (ThreadA.IsAlive)//線程類的 Abort() 方法可以永久的殺死一個線程。在殺死一個線程起前應該判斷線程是否在生存期間。
                {
                    ThreadA.Abort();
                }
                ThreadA = null;
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //停止


        }

        private void button10_Click(object sender, EventArgs e)
        {
            //掛起


        }

        private void button11_Click(object sender, EventArgs e)
        {
            //繼續
        }


        private void DoThreadA()
        {
            while (true)
            {
                if (this.pictureBox1.BackColor == Color.White)
                    this.pictureBox1.BackColor = Color.Red;
                else
                    this.pictureBox1.BackColor = Color.White;

                label6.Text = (cnt1++).ToString();

                Application.DoEvents();
                Thread.Sleep(200);
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (ThreadB == null)
            {
                richTextBox1.Text += "等ThreadA 執行完，ThreadB 再繼續執行\n";
                // The thread isn't running. Start it.
                cnt2 = 0;
                ThreadB = new Thread(DoThreadB);
                ThreadB.Priority = ThreadPriority.BelowNormal;
                ThreadB.IsBackground = true;
                ThreadB.Start();
            }

        }

        private void button8_Click(object sender, EventArgs e)
        {
            //殺死一個線程
            if (ThreadB != null)
            {
                if (ThreadB.IsAlive)//線程類的 Abort() 方法可以永久的殺死一個線程。在殺死一個線程起前應該判斷線程是否在生存期間。
                {
                    ThreadB.Abort();
                }
                ThreadB = null;
            }
        }

        private void DoThreadB()
        {
            if (ThreadA != null)
            {
                //等待執行
                ThreadA.Join();//ThreadB 要先讓線程 ThreadA 執行完，然後線程 ThreadB 再繼續執行
            }

            while (true)
            {
                if (this.pictureBox2.BackColor == Color.White)
                    this.pictureBox2.BackColor = Color.Red;
                else
                    this.pictureBox2.BackColor = Color.White;

                label7.Text = (cnt2++).ToString();

                Application.DoEvents();
                Thread.Sleep(200);
            }
        }

        // 色塊 SP

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


        Thread th = null;
        private void button12_Click(object sender, EventArgs e)
        {
            //啟動一個Thread
            th = new Thread(new ThreadStart(SayHello));
            th.Name = "SayHelloThread";
            th.Start();

        }

        public void SayHello()
        {
            while (true)
            {
                Console.WriteLine("Hello from a single thread.");
                Thread.Sleep(1000);
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //停止一個Thread
            if (th != null)
            {
                th.Abort();

            }
        }
    }
}
