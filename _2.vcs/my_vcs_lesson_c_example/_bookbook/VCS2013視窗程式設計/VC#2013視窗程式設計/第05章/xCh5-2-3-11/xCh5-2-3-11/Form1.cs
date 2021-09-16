using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_2_3_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 設定進度列的最大值與最小值
            progressBar1.Maximum = 100;
            progressBar1.Minimum = 0;

            // 設定Timer每一秒鐘會執行Tick事件一次
            timer1.Interval = 1000;

            // 跑馬燈式的進度列會一直有動畫，
            // 為避免誤解，當進度為0時，將其樣式更改為Block
            if (progressBar1.Minimum == 0)
                progressBar1.Style = ProgressBarStyle.Blocks;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            progressBar1.Style = ProgressBarStyle.Marquee;
            timer1.Start();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (progressBar1.Value >= progressBar1.Maximum)
            {
                timer1.Stop();
                textBox1.Text = "完成";
                progressBar1.Value = 0;
                progressBar1.Style = ProgressBarStyle.Blocks;
            }
            else
            {
                progressBar1.Value += 10;
                textBox1.Text = progressBar1.Value.ToString() + "%";
            }
        }
    }
}
