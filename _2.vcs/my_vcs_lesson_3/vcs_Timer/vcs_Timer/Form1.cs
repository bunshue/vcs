using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Timer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.DoubleBuffered = true;

            ShowResult.BackColor = Color.Red;
            pictureBox1.Image = vcs_Timer.Properties.Resources.red_ball_icon;
            label1.Text = "Interval : " + timer1.Interval.ToString() + " ms";

            //for countdown timer ST
            label2.Text = "";
            label3.Text = "";
            button1.Enabled = true;
            button2.Enabled = false;
            this.TopMost = false;
            //for countdown timer SP

            toolStripStatusLabel1.Text = DateTime.Now.ToString();
        }

        int toggle = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            if (toggle == 0)
            {
                toggle = 1;
                ShowResult.BackColor = Color.Red;
                pictureBox1.Image = vcs_Timer.Properties.Resources.red_ball_icon;
            }
            else
            {
                toggle = 0;
                ShowResult.BackColor = Color.Green;
                pictureBox1.Image = vcs_Timer.Properties.Resources.green_ball_icon;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            timer1.Interval += 50;
            label1.Text = "Interval : " + timer1.Interval.ToString() + " ms";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (timer1.Interval > 50)
                timer1.Interval -= 50;
            label1.Text = "Interval : " + timer1.Interval.ToString() + " ms";
        }


        //for countdown timer ST
        int total_second = 0;
        private void button6_Click(object sender, EventArgs e)
        {
            total_second = (int)numericUpDown1.Value * 60 + (int)numericUpDown2.Value;
            timer2_cnt = 0;
            timer2.Enabled = true;
            button1.Enabled = false;
            button2.Enabled = true;
            label2.Text = "計數中";
            label2.ForeColor = Color.Black;
            label3.Text = "時間經過： " + timer2_cnt.ToString() + " 秒";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            label2.Text = "";
            label3.Text = "";
            timer2.Enabled = false;
            button1.Enabled = true;
            button2.Enabled = false;
            this.TopMost = false;
        }

        int timer2_cnt = 0;
        private void timer2_Tick(object sender, EventArgs e)
        {
            timer2_cnt++;
            label3.Text = "時間經過： " + timer2_cnt.ToString() + " 秒";
            if (timer2_cnt == total_second)
            {
                this.TopMost = true;
                label2.Text = "時間到";
                label2.ForeColor = Color.Red;
            }
        }
        //for countdown timer SP

        //progress bar ST
        int progress = 0;
        private void timer3_Tick(object sender, EventArgs e)
        {
            progress++;
            label13.Text = "讀取進度： " + progress + "%";
            progressBar1.Value = progress;
            if (progress >= 100)
            {
                timer3.Enabled = false;
                label13.Text += "   讀取完成";
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            progress = 0;
            timer3.Enabled = false;
            progressBar1.Value = progress;
            label13.Text = "讀取進度： ";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            for (int i = 0; i <= 100; i++)
            {
                label13.Text = "讀取進度： " + i + "%";
                progressBar1.Value = i;
                Application.DoEvents();         //執行某一事件，以達到延遲效果。
                for (int j = 0; j < 100; j++)
                    System.Threading.Thread.Sleep(1);
            }
            label13.Text += "   讀取完成";
        }

        private void button15_Click(object sender, EventArgs e)
        {
            timer3.Enabled = true;
            progress = 0;
        }

        private void timer_status_strip_Tick(object sender, EventArgs e)
        {
            toolStripStatusLabel1.Text = DateTime.Now.ToString();
        }
        //progress bar SP


    }
}
