using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsXP
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void pictureBox5_Click(object sender, EventArgs e)
        {
            int i ;
            i=80;
            pictureBox5.Visible = false;
            pictureBox4.Visible = false;
            label2.Visible = false;
            label3.Visible = false;
            pictureBox6.Top -= i;
            pictureBox8.Top -= i;
            label4.Top -= i;
            label5.Top -= i;
            label6.Top -= i;
            label10.Top -= i;
            label7.Top -= i;
            label8.Top -= i;
            label9.Top -= i;
            pictureBox9.Top -= i;
            pictureBox11.Top -= i;
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            if (pictureBox5.Visible == false)
            {
                int i;
                i = 80;
                pictureBox5.Visible = true;
                pictureBox4.Visible = true;
                label2.Visible = true;
                label3.Visible = true;
                pictureBox6.Top += i;
                pictureBox8.Top += i;
                label4.Top += i;
                label5.Top += i;
                label6.Top += i;
                label10.Top += i;
                label7.Top += i;
                label8.Top += i;
                label9.Top += i;
                pictureBox9.Top += i;
                pictureBox11.Top += i;
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SetStyle(ControlStyles.SupportsTransparentBackColor,true);
        }
    }
}