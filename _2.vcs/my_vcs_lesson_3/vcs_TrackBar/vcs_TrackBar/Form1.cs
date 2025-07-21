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
            trackBar1.Value = 50;
        }

        bool flag_mouse_down = false;
        private void trackBar1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;
            richTextBox1.Text += "MouseDown :"+trackBar1.Value.ToString() + "\n";
        }

        private void trackBar1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                label1.Text = "取得 : " + trackBar1.Value.ToString();
            }
        }

        private void trackBar1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
            richTextBox1.Text += "MouseUp :" + trackBar1.Value.ToString() + "\n";
        }
    }
}


