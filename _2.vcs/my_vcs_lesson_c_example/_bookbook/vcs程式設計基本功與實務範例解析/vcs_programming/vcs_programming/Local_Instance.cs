using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class Local_Instance : Form
    {
        public Local_Instance()
        {
            InitializeComponent();
        }

        int y = 0;

        private void button2_Click(object sender, EventArgs e)
        {
            y = y + 1;
            label1.Text = "y = " + y;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int x = 0;
            x = x + 1;
            label1.Text = "x = " + x;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            y = y + 1;
            label1.Text = "y = " + y;
        }
    }
}
