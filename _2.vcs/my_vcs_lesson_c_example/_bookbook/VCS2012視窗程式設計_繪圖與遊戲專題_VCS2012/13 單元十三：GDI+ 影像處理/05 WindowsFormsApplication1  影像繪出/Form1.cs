using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Bitmap bitmap1; // Bitmap 影像
        string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

        public Form1()
        {
            InitializeComponent();
            bitmap1 = new Bitmap(filename);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            if (comboBox1.SelectedIndex == 0)
            {
                richTextBox1.Text += "第0項 Form\n";
                Rectangle rectDest = new Rectangle(0, 0, bitmap1.Width, bitmap1.Height);
                Rectangle rectSrc = new Rectangle(0, 0, bitmap1.Width, bitmap1.Height);
                e.Graphics.DrawImage(bitmap1, rectDest, rectSrc, GraphicsUnit.Pixel); // 呈現原圖
            }
            else if (comboBox1.SelectedIndex == 1)
            {
                richTextBox1.Text += "第1項 Form\n";
                Rectangle rectDest = new Rectangle(0, 0, bitmap1.Width, bitmap1.Height);
                e.Graphics.DrawImage(bitmap1, rectDest); // 呈現原圖
            }
            else if (comboBox1.SelectedIndex == 2)
            {
                richTextBox1.Text += "第2項 Form\n";
                Rectangle rectDest = new Rectangle(0, 0, bitmap1.Width * 2, bitmap1.Height / 2);
                e.Graphics.DrawImage(bitmap1, rectDest); // 呈現原圖
            }
            else if (comboBox1.SelectedIndex == 3)
            {
                richTextBox1.Text += "第3項 Form\n";
                Point dest = new Point(0, 0); // 目的地左上角座標
                e.Graphics.DrawImage(bitmap1, dest); // 呈現原圖
            }
            else if (comboBox1.SelectedIndex == 4)
            {
                richTextBox1.Text += "第4項 Form\n";
                e.Graphics.DrawImage(bitmap1, 0, 0); // 呈現原圖
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            radioButton1.Text = "rectDest <- rectDest";
            radioButton2.Text = "rectDest";
            radioButton3.Text = "rectDest (縮放)";
            radioButton4.Text = "Point";
            radioButton5.Text = "X, Y";
        }

        private void rb_check(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            if (radioButton1.Checked == true)
            {
                richTextBox1.Text += "第1項 PictureBox\n";
                Rectangle rectDest = new Rectangle(0, 0, bitmap1.Width, bitmap1.Height);
                Rectangle rectSrc = new Rectangle(0, 0, bitmap1.Width, bitmap1.Height);
                e.Graphics.DrawImage(bitmap1, rectDest, rectSrc, GraphicsUnit.Pixel); // 呈現原圖
            }
            else if (radioButton2.Checked == true)
            {
                richTextBox1.Text += "第2項 PictureBox\n";
                Rectangle rectDest = new Rectangle(0, 0, bitmap1.Width, bitmap1.Height);
                e.Graphics.DrawImage(bitmap1, rectDest); // 呈現原圖
            }
            else if (radioButton3.Checked == true)
            {
                richTextBox1.Text += "第3項 PictureBox\n";
                Rectangle rectDest = new Rectangle(0, 0, bitmap1.Width * 2, bitmap1.Height / 2);
                e.Graphics.DrawImage(bitmap1, rectDest); // 呈現原圖
            }
            else if (radioButton4.Checked == true)
            {
                richTextBox1.Text += "第4項 PictureBox\n";
                Point dest = new Point(0, 0); // 目的地左上角座標
                e.Graphics.DrawImage(bitmap1, dest); // 呈現原圖
            }
            else if (radioButton5.Checked == true)
            {
                richTextBox1.Text += "第5項 PictureBox\n";
                e.Graphics.DrawImage(bitmap1, 0, 0); // 呈現原圖
            }
        }
    }
}
