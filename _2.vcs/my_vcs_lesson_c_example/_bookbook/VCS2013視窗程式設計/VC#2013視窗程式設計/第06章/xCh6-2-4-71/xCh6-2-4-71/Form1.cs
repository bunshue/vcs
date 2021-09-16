using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_2_4_71
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            toolStripButton1.Image = Image.FromFile(@"c:\user_red32x32.png");

            // 設定進度列的最大值與最小值
            toolStripProgressBar1.Maximum = 100;
            toolStripProgressBar1.Minimum = 0;

            // 設定Timer每一秒鐘會執行Tick事件一次
            timer1.Interval = 1000;
            timer1.Tick += new EventHandler(timer1_Tick);

            // 跑馬燈式的進度列會一直有動畫，
            // 為避免誤解，當進度為0時，將其樣式更改為Block
            if (toolStripProgressBar1.Minimum == 0)
                toolStripProgressBar1.Style = ProgressBarStyle.Blocks;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            // 如果進度已達上限，停止Timer、秀出「完成」
            // 並將進度列的值重設為0
            // 如果進度未達上限，則每次增10，並將進度
            // 顯示在TextBox中
            if (toolStripProgressBar1.Value >= toolStripProgressBar1.Maximum)
            {
                timer1.Stop();
                toolStripButton1.Enabled = true;
                toolStripTextBox1.Text = "完成";
                toolStripProgressBar1.Value = 0;
                toolStripProgressBar1.Style = ProgressBarStyle.Blocks;
            }
            else
            {
                toolStripProgressBar1.Value += 10;
                toolStripTextBox1.Text = "目前進度：" +
                    toolStripProgressBar1.Value.ToString() + 
                    "%";
            }
        }

        private void toolStripButton1_Click(object sender, EventArgs e)
        {
            toolStripProgressBar1.Style = ProgressBarStyle.Marquee;
            toolStripButton1.Enabled = false;
            timer1.Start();
        }
    }
}
