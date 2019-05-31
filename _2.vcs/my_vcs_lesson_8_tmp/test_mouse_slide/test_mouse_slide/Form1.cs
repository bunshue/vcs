using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace test_mouse_slide
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        bool flag_mouse_down = false;
        int mouse_down_position_x = 0;
        int mouse_down_position_y = 0;
        int mouse_up_position_x = 0;
        int mouse_up_position_y = 0;

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "Down ";
            flag_mouse_down = true;
            mouse_down_position_x = e.X;
            mouse_down_position_y = e.Y;

        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "Move ";

        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "Up ";
            flag_mouse_down = false;
            mouse_up_position_x = e.X;
            mouse_up_position_y = e.Y;
            if (mouse_up_position_x > mouse_down_position_x)
                richTextBox1.Text += "Right ";
            else
                richTextBox1.Text += "Left ";

        }

        private void pictureBox1_MouseWheel(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += e.Delta.ToString() + " ";

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.pictureBox1.MouseWheel += new MouseEventHandler(pictureBox1_MouseWheel);
        }
    }
}
