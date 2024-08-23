using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Diagnostics;   //for Process
namespace vcs_Thread_Example1
{
    public partial class Form1 : Form
    {
        private const int BORDER = 10;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            show_item_location();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //關閉監聽執行續(如果有的話)
            try
            {
                thread_ex1.Abort(); //關閉監聽執行續
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


        void show_item_location()
        {
            int W = 640;
            int H = 480;
            int x_st = BORDER;
            int y_st = BORDER;
            int dx = 140 + 50;
            int dy = 50 + 15;


            W = 150;
            H = 150;
            dx = W + BORDER;
            dy = H + BORDER;

            groupBox0.Size = new Size(W, H);
            groupBox1.Size = new Size(W, H);
            groupBox2.Size = new Size(W, H);
            groupBox3.Size = new Size(W, H);
            groupBox4.Size = new Size(W, H);
            groupBox5.Size = new Size(W, H);
            groupBox6.Size = new Size(W, H);
            groupBox7.Size = new Size(W, H);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            groupBox4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox5.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox6.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            groupBox7.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            richTextBox1.Size = new Size(320, 540);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = BORDER * 2;
            y_st = BORDER * 2;
            W = 90;
            H = 30;
            dx = W + BORDER;
            dy = H + BORDER;
            button00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button30.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button40.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button42.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button50.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button51.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button52.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button60.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button61.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button62.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button70.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button71.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button72.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            this.Size = new Size(1000, 600);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //Thread使用範例0 ST

        private bool flag_ThreadProc_ex0 = false;

        private void ThreadProc_ex0()
        {
            while (flag_ThreadProc_ex0 == true)
            {
                Console.WriteLine("無限迴圈");
                richTextBox1.Text += "無限迴圈 ";

                Thread.Sleep(1000);
            }
            Console.WriteLine("結束 ThreadProc_ex0");
            richTextBox1.Text += "\n結束 ThreadProc_ex0\n";
        }

        private void button00_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "啟動 thread 7\n";

            flag_ThreadProc_ex0 = true;
            Thread thread_ex0 = new Thread(ThreadProc_ex0);
            thread_ex0.Start();
        }

        private void button01_Click(object sender, EventArgs e)
        {
            flag_ThreadProc_ex0 = false;
        }

        private void button02_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例0 SP


        //Thread使用範例1 ST

        Thread thread_ex1;                                  //宣告監聽用執行續

        //監聽副程式
        int i;
        private void ThreadProc_ex1()
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

        private void button10_Click(object sender, EventArgs e)
        {
            thread_ex1 = new Thread(ThreadProc_ex1); //建立監聽網路訊息的新執行緒
            thread_ex1.Name = "Thread_ex1_" + cnt.ToString();
            //thread_ex1.IsBackground = true;  //設定為背景執行緒
            thread_ex1.Start();             //啟動監聽執行緒
            richTextBox1.Text += "啟動 thread 4, 名稱 : " + thread_ex1.Name + "\n";
            cnt++;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            if (thread_ex1 != null)
            {
                richTextBox1.Text += "關閉 Main Thread\n";
                thread_ex1.Abort();
            }
            else
            {
                richTextBox1.Text += "無Thread\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Info\n";
            if (thread_ex1 == null)
            {
                richTextBox1.Text += "Main Thread 尚未啟動\n";
            }
            else
            {
                richTextBox1.Text += "Main Thread\t" + thread_ex1.ToString() + "\n";
                richTextBox1.Text += "ThreadState\t" + thread_ex1.ThreadState.ToString() + "\n";
                richTextBox1.Text += "Name\t" + thread_ex1.Name + "\n";
                richTextBox1.Text += "IsAlive\t" + thread_ex1.IsAlive.ToString() + "\n";

                if (thread_ex1.IsAlive == true)
                {
                    richTextBox1.Text += "IsBackground\t" + thread_ex1.IsBackground.ToString() + "\n";
                }
            }

        }
        //Thread使用範例1 SP


        //Thread使用範例2 ST

        static Thread thread_ex2a;
        static Thread thread_ex2b;

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

        private void button20_Click(object sender, EventArgs e)
        {
            thread_ex2a = new Thread(ThreadProc_ex2);
            thread_ex2a.Name = "Thread_ex1";

            thread_ex2b = new Thread(ThreadProc_ex2);
            thread_ex2b.Name = "Thread_ex2";

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

        private void button21_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "停止 thread 2a\n";
            thread_ex2a.Abort();

            richTextBox1.Text += "停止 thread 2b\n";
            thread_ex2b.Abort();
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //狀態
            richTextBox1.Text += "Thread_ex1 狀態 : " + thread_ex2a.ThreadState + "\n";
            richTextBox1.Text += "Thread_ex2 狀態 : " + thread_ex2b.ThreadState + "\n";
        }
        //Thread使用範例2 SP


        //Thread使用範例3 ST
        static Thread thread_ex3 = null;
        public void ThreadProc_ex3()
        {
            while (true)
            {
                Console.WriteLine("Hello from a single thread.");
                Thread.Sleep(1000);
            }
        }

        private void button30_Click(object sender, EventArgs e)
        {
            thread_ex3 = new Thread(new ThreadStart(ThreadProc_ex3));
            thread_ex3.Name = "Thread_ex3";
            thread_ex3.Start();
            richTextBox1.Text += "啟動 thread 3, 名稱 : " + thread_ex3.Name + "\n";
        }

        private void button31_Click(object sender, EventArgs e)
        {
            //停止一個Thread
            if (thread_ex3 != null)
            {
                thread_ex3.Abort();
            }
        }

        private void button32_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例3 SP

        //Thread使用範例4 ST
        private void button40_Click(object sender, EventArgs e)
        {

        }

        private void button41_Click(object sender, EventArgs e)
        {

        }

        private void button42_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例4 SP


        //Thread使用範例5 ST
        private void button50_Click(object sender, EventArgs e)
        {

        }

        private void button51_Click(object sender, EventArgs e)
        {

        }

        private void button52_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例5 SP


        //Thread使用範例6 ST
        private void button60_Click(object sender, EventArgs e)
        {

        }

        private void button61_Click(object sender, EventArgs e)
        {

        }

        private void button62_Click(object sender, EventArgs e)
        {

        }
        //Thread使用範例6 SP

        //Thread使用範例7 ST
        private void button70_Click(object sender, EventArgs e)
        {

        }

        private void button71_Click(object sender, EventArgs e)
        {

        }

        private void button72_Click(object sender, EventArgs e)
        {

        }

        //Thread使用範例7 SP

    }
}
