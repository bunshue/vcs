using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace MoveWindows
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            label1.Left -= 2;
            if (label1.Right < 0)
            {
                label1.Left = this.Width;
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
            this.Close();
        }
    }
}