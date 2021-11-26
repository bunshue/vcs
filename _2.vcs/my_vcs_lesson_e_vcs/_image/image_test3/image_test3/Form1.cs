using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
//using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;

namespace image_test3
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
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            Bitmap bitmap;
            string filename1 = @"C:\______test_files\bear.bmp";
            bitmap = new Bitmap(filename1);
            pictureBox1.Image = bitmap;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            FileInfo f1 = new FileInfo(filename1);

            string filename2 = Application.StartupPath + "\\jpg_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            //string fileName = saveFileDialog.FileName;
            bitmap.Save(filename2, ImageFormat.Jpeg);
            FileInfo f2 = new FileInfo(filename2);

            richTextBox1.Text += "圖像轉換 : " + f1.Name + " 轉換成 " + f2.Name + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bitmap;
            string filename1 = @"C:\______test_files\picture1.jpg";
            bitmap = new Bitmap(filename1);
            pictureBox1.Image = bitmap;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            FileInfo f1 = new FileInfo(filename1);

            string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            //string fileName = saveFileDialog.FileName;
            bitmap.Save(filename2, ImageFormat.Bmp);
            FileInfo f2 = new FileInfo(filename2);

            richTextBox1.Text += "圖像轉換 : " + f1.Name + " 轉換成 " + f2.Name + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //ico2bmp
            Bitmap bitmap;
            string filename1 = @"C:\______test_files\_icon\唐.ico";
            bitmap = new Bitmap(filename1);
            pictureBox1.Image = bitmap;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            FileInfo f1 = new FileInfo(filename1);

            string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            //string fileName = saveFileDialog.FileName;
            bitmap.Save(filename2, ImageFormat.Bmp);
            FileInfo f2 = new FileInfo(filename2);

            richTextBox1.Text += "圖像轉換 : " + f1.Name + " 轉換成 " + f2.Name + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }
    }
}
