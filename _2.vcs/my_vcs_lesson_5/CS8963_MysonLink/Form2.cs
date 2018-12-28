using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace myson_link
{
    public partial class Form2 : Form
    {
        int isStart = 0;
        DateTime start_time = DateTime.Now;
        bool flag_topmost = false;
        int stop_count = 0;

        public Form2()
        {
            InitializeComponent();
            timer1.Enabled = false;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            DateTime now = DateTime.Now;
            TimeSpan ts = now - start_time;
            //labelTimer.Text = ts.Hour + ":" + ts.Minute + ":" + ts.Second;
            labelTimer.Text = ts.ToString("T");
        }

        private void buttonStart_Click(object sender, EventArgs e)
        {
            if (isStart == 0)
            {
                isStart = 1;
                start_time = DateTime.Now;
                timer1.Enabled = true;
                //buttonStart.Text = "停止計時";
                stop_count = 0;
            }
            else
            {
                //buttonStart.Text = "開始計時";
            }
        }

        private void buttonReset_Click(object sender, EventArgs e)
        {
            if (stop_count == 0)
            {
                stop_count = 1;
                timer1.Enabled = false;
                isStart = 0;
            }
            else if (stop_count == 1)
            {
                labelTimer.Text = "-.--";
            }
        }

        private void buttonTop_Click(object sender, EventArgs e)
        {
            if (flag_topmost == false)
            {
                this.TopMost = true;
                buttonTop.Text = "下";
            }
            else
            {
                this.TopMost = false;
                buttonTop.Text = "上";
            }
        }

        private void buttonExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
