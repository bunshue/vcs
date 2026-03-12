using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs__common
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int W = 360;
            int H = 200;
            int x_st;
            int y_st;
            int dx;
            int dy;

            //groupBox
            x_st = 10;
            y_st = 10;
            dx = W + 10;
            dy = H + 10;

            groupBox0.Size = new Size(600, 600);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            //button
            x_st = 380;
            y_st = 30;
            dx = 200 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            x_st = 10;
            y_st = 30;
            dx = 200 + 10;
            dy = 40;

            label1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            linkLabel1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            comboBox1.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            checkBox1.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            radioButton1.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            trackBar1.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            hScrollBar1.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            vScrollBar1.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            textBox1.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 8);

            this.Size = new Size(650, 670);
            this.Text = "vcs__common";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void LinkLabel_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
        }

        private void linkLabel2_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
        }

        private void linkLabel3_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }
    }
}
