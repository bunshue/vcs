using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace TrackBarStraightForwardUtility
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //控制進度條
        private void timer1_Tick(object sender, EventArgs e)
        {
            if (progressBar1.Value == progressBar1.Maximum)
            {
                progressBar1.Value = progressBar1.Minimum;
            }
            else
            {
                progressBar1.PerformStep();//增加進度
            }// end 
            int intBar;
            intBar = 100 * (progressBar1.Value - progressBar1.Minimum) / (progressBar1.Maximum - progressBar1.Minimum);
            label2.Text = intBar.ToString() + "%";
        }
        //設置Timer控件Interval屬性
        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            timer1.Interval = Convert.ToInt16(10000 / trackBar1.Value);
        }
        //起動Timer控件
        private void button1_Click(object sender, EventArgs e)
        {
            if (timer1.Enabled == true)
            {
                timer1.Enabled = false;
                button1.Text = "開始";
            }
            else
            {
                timer1.Enabled = true;
                button1.Text = "停止";

            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}