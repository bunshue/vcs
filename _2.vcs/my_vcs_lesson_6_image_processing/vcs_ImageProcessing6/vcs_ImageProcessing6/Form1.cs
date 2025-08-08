using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ImageProcessing6
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            pictureBox0.Image = Image.FromFile(filename);
            pictureBox1.Image = Image.FromFile(filename);
            pictureBox2.Image = Image.FromFile(filename);
            pictureBox3.Image = Image.FromFile(filename);
        }

        void show_item_location()
        {
            int W = 500;
            int H = 400;
            int x_st = 20;
            int y_st = 20;
            int dx = W + 50;
            int dy = H + 100;
            int dd1 = 40;
            int dd2 = 85;

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            label3.Location = new Point(x_st + dx * 1, y_st + dy * 1);

            label0.Text = "原圖";
            label1.Text = "Gamma";
            label2.Text = "Gamma";
            label3.Text = "亮度";

            pictureBox0.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox3.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd2);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0 + dd2);
            pictureBox2.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd2);
            pictureBox3.Location = new Point(x_st + dx * 1, y_st + dy * 1 + dd2);

            richTextBox1.Size = new Size(W, H);
            richTextBox1.Location = new Point(x_st + dx * 2 + 150, y_st + dy * 0 + dd2);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

        }


    }
}
