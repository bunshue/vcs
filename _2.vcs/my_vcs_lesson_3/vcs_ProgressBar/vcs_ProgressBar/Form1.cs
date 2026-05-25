using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ProgressBar
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
            progressBar0.Maximum = 100;
            progressBar0.Minimum = 0;

            // 設定Timer每一秒鐘會執行Tick事件一次
            timer1.Interval = 1000;

            // 跑馬燈式的進度列會一直有動畫，
            // 為避免誤解，當進度為0時，將其樣式更改為Block
            if (progressBar0.Minimum == 0)
            {
                progressBar0.Style = ProgressBarStyle.Blocks;
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_start_Click(object sender, EventArgs e)
        {
            progressBar0.Style = ProgressBarStyle.Marquee;
            timer1.Start();
        }

        private void bt_stop_Click(object sender, EventArgs e)
        {
            timer1.Stop();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (progressBar0.Value >= progressBar0.Maximum)
            {
                timer1.Stop();
                lb_status0.Text = "完成";
                progressBar0.Value = 0;
                progressBar0.Style = ProgressBarStyle.Blocks;
            }
            else
            {
                progressBar0.Value += 10;
                lb_status0.Text = progressBar0.Value.ToString() + "%";
            }
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


