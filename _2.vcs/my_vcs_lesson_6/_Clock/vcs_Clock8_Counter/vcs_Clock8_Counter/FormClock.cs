using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Clock8_Counter
{
    public partial class FormClock : Form
    {
        int counter = 0;

        public FormClock()
        {
            InitializeComponent();
            timer.Enabled = true;
        }

        private void timer_Tick(object sender, EventArgs e)
        {
            DateTime now = DateTime.Now;
            labelTime.Text = now.Hour + ":" + now.Minute + ":" + now.Second;

            if (isStart) {
                counter++;
                labelCounter.Text = (counter / 100.0) + "";
            }
        }

        bool isStart = false;

        private void buttonStart_Click(object sender, EventArgs e)
        {
            isStart = !isStart;

            if (isStart)
            {
                buttonStart.Text = "停止計時";
            }
            else
            {
                buttonStart.Text = "開始計時";
            }

        }
    }
}
