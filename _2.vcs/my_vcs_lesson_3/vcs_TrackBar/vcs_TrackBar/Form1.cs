using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_TrackBar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        bool flag_mouse_down = false;
        private void trackBar1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;
            richTextBox1.Text += trackBar1.Value.ToString() + " ";
        }

        private void trackBar1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                //richTextBox1.Text += trackBar1.Value.ToString() + " ";

                int x = trackBar1.Value;

                int k = 100;
                label1.Text = "ES = k * x * x / 2 = " + (k * x * x / 2).ToString();
            }
        }

        private void trackBar1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
            richTextBox1.Text += trackBar1.Value.ToString() + " ";

            trackBar1.Value = 0;
        }
    }
}


