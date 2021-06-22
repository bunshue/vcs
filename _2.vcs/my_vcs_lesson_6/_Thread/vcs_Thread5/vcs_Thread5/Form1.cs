using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Timers;    //for ElapsedEventHandler

namespace vcs_Thread5
{
    public partial class Form1 : Form
    {
        int a = 0;

        thread1 obj;
        Thread t;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        //第2種 啟動Thread 方法
        //建立一個Thread 到 偵錯/視窗/即時運算 看結果
        private void button1_Click(object sender, EventArgs e)
        {
            a++;
            string thread_name = "Thread測試_" + a.ToString();
            richTextBox1.Text += "開啟thread, 名稱 : " + thread_name + "\n";
            obj = new thread1(thread_name);
            t = new Thread(obj.runMe);
            t.Start();
        }

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

        private void button2_Click(object sender, EventArgs e)
        {
            t.Abort();

        }

        //第2種 啟動Thread 方法
        //開啟關閉thread    ST
        System.Timers.Timer tt = new System.Timers.Timer(1234);
        int number = 0;

        private void button4_Click(object sender, EventArgs e)
        {
            tt.Elapsed += new ElapsedEventHandler(run);
            tt.Enabled = true;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            tt.Enabled = false;
            number = 0;
        }

        public void run(object source, System.Timers.ElapsedEventArgs e)
        {
            number++;
            System.Diagnostics.Debug.Print("即時運算視窗輸出除錯訊息 測試訊息！！！Form1！！！ " + number.ToString());
            Console.Write(number.ToString() + "\r\n");

            //MessageBox.Show("number = " + number);
        }

        //開啟關閉thread    SP
    }
}
