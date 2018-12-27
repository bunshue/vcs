using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_vcs_15_timer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int result = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (result == 0)
            {
                ShowResult.BackColor = Color.Red;
                result = 1;
            }
            else
            {
                ShowResult.BackColor = Color.Green;
                result = 0;
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ShowResult.BackColor = Color.Red;
            label1.Text = "Interval : " + timer1.Interval.ToString() + " ms";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            timer1.Interval += 50;
            label1.Text = "Interval : " + timer1.Interval.ToString() + " ms";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (timer1.Interval >50)
                timer1.Interval -= 50;
            label1.Text = "Interval : " + timer1.Interval.ToString() + " ms";
        }
    }
}
