using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_17_SetupTimer_TopMost
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            label2.Text = "";
            label3.Text = "";
            button1.Enabled = true;
            button2.Enabled = false;
            this.TopMost = false;
        }

        int total_second = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            total_second = (int)numericUpDown1.Value * 60 + (int)numericUpDown2.Value;
            timer1_cnt = 0;
            timer1.Enabled = true;
            button1.Enabled = false;
            button2.Enabled = true;
            label2.Text = "計數中";
            label2.ForeColor = Color.Black;
            label3.Text = "時間經過： " + timer1_cnt.ToString() + " 秒";
        }

        int timer1_cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            timer1_cnt++;
            label3.Text = "時間經過： " + timer1_cnt.ToString() + " 秒";
            if (timer1_cnt == total_second)
            {
                this.TopMost = true;
                label2.Text = "時間到";
                label2.ForeColor = Color.Red;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label2.Text = "";
            label3.Text = "";
            timer1.Enabled = false;
            button1.Enabled = true;
            button2.Enabled = false;
            this.TopMost = false;
        }
    }
}
