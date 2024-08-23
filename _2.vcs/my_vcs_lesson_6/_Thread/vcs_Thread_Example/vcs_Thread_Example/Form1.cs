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

    }
}

