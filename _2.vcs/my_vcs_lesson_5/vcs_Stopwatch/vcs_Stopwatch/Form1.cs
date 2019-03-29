using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for Stopwatch

namespace vcs_Stopwatch
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Stopwatch sw = new Stopwatch();

        private void button1_Click(object sender, EventArgs e)
        {
            sw.Start();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            sw.Stop();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            double ms = sw.ElapsedMilliseconds;

            TimeSpan ts = sw.Elapsed;

            string elapsedTime = String.Format("{0:00}:{1:00}:{2:00}.{3:00}",
                        ts.Hours, ts.Minutes, ts.Seconds,
                        ts.Milliseconds / 10);
            //digitalDisplayControl1.DigitText = elapsedTime;
            label1.Text = elapsedTime;

        }

        DateTime LoginTime;
        DateTime LogoffTime;
        TimeSpan StayTime = new TimeSpan();
        private void button4_Click(object sender, EventArgs e)
        {
            LoginTime = DateTime.Now; //取得目前登入的時間
            richTextBox1.Text += "登入時間： " + LoginTime + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            LogoffTime = DateTime.Now;
            richTextBox1.Text += "登入時間： " + LogoffTime + "\n";
            StayTime = LogoffTime.Subtract(LoginTime);
            richTextBox1.Text += "您在此停留了" + StayTime.Hours + "小時" + StayTime.Minutes + "分鐘" + StayTime.Seconds + "秒\n";

        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開始計時\n";
            // Create stopwatch
            Stopwatch stopwatch = new Stopwatch();
            // Begin timing
            stopwatch.Start();

            // Do something
            Application.DoEvents();         //執行某一事件，以達到延遲效果。
            for (int j = 0; j < 123; j++)
                System.Threading.Thread.Sleep(1);

            // Stop timing
            stopwatch.Stop();

            // Write result
            richTextBox1.Text += "停止計時\n";
            richTextBox1.Text += "總時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";

        }
    }
}
