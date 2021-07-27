using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1ffffff
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
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
                richTextBox1.Text += trackBar1.Value.ToString() + " ";
            }


        }

        private void trackBar1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
            richTextBox1.Text += trackBar1.Value.ToString() + " ";

            trackBar1.Value = 1;

        }
    }
}

