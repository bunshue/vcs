using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Draw_Example3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Size = new Size(1600, 800);

            show_item_location();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int BORDER = 20;
            int W = this.ClientSize.Width;
            int H = this.ClientSize.Height;

            int ww = (W - BORDER * 4) / 9;
            int hh = (H - BORDER * 3) / 4;
            richTextBox1.Text += "ww = " + ww.ToString() + "\n";
            richTextBox1.Text += "hh = " + hh.ToString() + "\n";
            int block = (ww < hh) ? ww : hh;
            richTextBox1.Text += "block = " + block.ToString() + "\n";

            int w = block * 3;
            int h = block * 2;
            pictureBox0.Size = new Size(w, h);
            pictureBox1.Size = new Size(w, h);
            pictureBox2.Size = new Size(w, h);
            pictureBox3.Size = new Size(w, h);
            pictureBox4.Size = new Size(w, h);
            pictureBox5.Size = new Size(w, h);

            int x_st = BORDER;
            int y_st = BORDER;
            int dx = w + BORDER;
            int dy = h + BORDER;

            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
        }

    }
}
