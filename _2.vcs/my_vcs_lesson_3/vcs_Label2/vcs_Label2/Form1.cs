using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Label2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void toggleButton_Click(object sender, EventArgs e)
        {
            if (timer1.Enabled == false) {
                timer1.Enabled = true;
                toggleButton.Text = "暫停";
            }
            else {
                timer1.Enabled = false;
                toggleButton.Text = "繼續";
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (northOption.Checked == true)
                carLabel.Top -= 1;
            else if (westOption.Checked == true)
                carLabel.Left -= 1;
            else if (eastOption.Checked == true)
                carLabel.Left += 1;
            else if (southOption.Checked == true)
                carLabel.Top += 1;
        }

        private void slowOption_Click(object sender, EventArgs e)
        {
            timer1.Interval = 200;
        }
        private void mediumOption_Click(object sender, EventArgs e)
        {
            timer1.Interval = 100;
        }
        private void fastOption_Click(object sender, EventArgs e)
        {
            timer1.Interval = 50;
        }


    }
}
