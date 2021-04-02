using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace ButtonNavigation
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            button5.Visible = true;
            button6.Visible = true;
            button7.Visible = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            button8.Visible = true;
            button9.Visible = true;
            button10.Visible = true;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            button11.Visible = true;
            button12.Visible = true;
            button13.Visible = true;
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void 日誌管理ToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void panel2_Paint(object sender, PaintEventArgs e)
        {

        }
    }
}