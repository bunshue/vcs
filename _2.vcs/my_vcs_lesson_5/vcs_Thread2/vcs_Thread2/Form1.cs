using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_Thread2
{
    public partial class Form1 : Form
    {
        private Thread MyThread;
        int cnt = 0;

        public Form1()
        {
            InitializeComponent();

            //C# 跨 Thread 存取 UI
            Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效
        }

        private void button1_Click(object sender, EventArgs e)
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

        private void button2_Click(object sender, EventArgs e)
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

                label1.Text = (cnt++).ToString();

                Application.DoEvents();
                Thread.Sleep(200);
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (MyThread != null)
            {
                // The thread is running. Stop it.
                MyThread.Abort();
                MyThread = null;
            }
        }

    }
}
