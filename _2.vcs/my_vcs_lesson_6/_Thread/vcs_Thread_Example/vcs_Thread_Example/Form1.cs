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
        private Thread thread_ex8a;
        private Thread thread_ex8b;
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
        }


        // 色塊 ST
        private void button4_Click(object sender, EventArgs e)
        {
            if (thread_ex8a == null)
            {
                // The thread isn't running. Start it.
                cnt1 = 0;
                thread_ex8a = new Thread(ThreadProc_ex8a);
                thread_ex8a.Priority = ThreadPriority.BelowNormal;
                thread_ex8a.IsBackground = true;
                thread_ex8a.Start();
            }
        }

        private void button1_Click(object sender, EventArgs e)
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


        private void ThreadProc_ex8a()
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
            if (thread_ex8b == null)
            {
                richTextBox1.Text += "等thread_ex8a 執行完，thread_ex8b 再繼續執行\n";
                // The thread isn't running. Start it.
                cnt2 = 0;
                thread_ex8b = new Thread(ThreadProc_ex8b);
                thread_ex8b.Priority = ThreadPriority.BelowNormal;
                thread_ex8b.IsBackground = true;
                thread_ex8b.Start();
            }

        }

        private void button8_Click(object sender, EventArgs e)
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
