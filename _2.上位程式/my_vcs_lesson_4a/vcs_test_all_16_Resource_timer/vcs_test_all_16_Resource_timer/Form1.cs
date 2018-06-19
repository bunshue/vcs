using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_16_Resource_timer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;
            textBox1.Text = timer1.Interval.ToString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;
            textBox1.Text = timer1.Interval.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            timer1.Interval += 100;
            textBox1.Text = timer1.Interval.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if(timer1.Interval>100)
                timer1.Interval -= 100;
            textBox1.Text = timer1.Interval.ToString();
        }

        int toggle = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            if (toggle == 0)
            {
                toggle = 1;
                pictureBox1.Image = Resource1.red_ball_icon;
            }
            else
            {
                toggle = 0;
                pictureBox1.Image = Resource1.green_ball_icon;
            }
        }
    }
}
