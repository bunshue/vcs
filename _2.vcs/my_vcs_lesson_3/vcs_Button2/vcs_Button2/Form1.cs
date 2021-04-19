using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_Button2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_MouseMove(object sender, MouseEventArgs e)
        {
            button1.ImageAlign = ContentAlignment.MiddleLeft;
        }

        private void button2_MouseMove(object sender, MouseEventArgs e)
        {
            button2.ImageAlign = ContentAlignment.MiddleLeft;
        }

        private void button3_MouseMove(object sender, MouseEventArgs e)
        {
            button3.ImageAlign = ContentAlignment.MiddleLeft;
        }

        private void button4_MouseMove(object sender, MouseEventArgs e)
        {
            button4.ImageAlign = ContentAlignment.MiddleLeft;
        }

        private void button5_MouseMove(object sender, MouseEventArgs e)
        {
            button5.ImageAlign = ContentAlignment.MiddleLeft;
        }

        private void button6_Click(object sender, EventArgs e)
        {
           
        }

        private void button1_MouseLeave(object sender, EventArgs e)
        {
            button1.ImageAlign = ContentAlignment.MiddleCenter;
        }

        private void button2_MouseLeave(object sender, EventArgs e)
        {
            button2.ImageAlign = ContentAlignment.MiddleCenter;
        }

        private void button3_MouseLeave(object sender, EventArgs e)
        {
            button3.ImageAlign = ContentAlignment.MiddleCenter;
        }

        private void button4_MouseLeave(object sender, EventArgs e)
        {
            button4.ImageAlign = ContentAlignment.MiddleCenter;
        }

        private void button5_MouseLeave(object sender, EventArgs e)
        {
            button5.ImageAlign = ContentAlignment.MiddleCenter;
        }

        private void button6_MouseMove(object sender, MouseEventArgs e)
        {
            button6.ImageAlign = ContentAlignment.MiddleLeft;
        }

        private void button6_MouseLeave(object sender, EventArgs e)
        {
            button6.ImageAlign = ContentAlignment.MiddleCenter;
        }
    }
}