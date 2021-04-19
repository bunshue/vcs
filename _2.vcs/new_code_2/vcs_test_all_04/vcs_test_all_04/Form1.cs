using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;

using System.Management;    //for ManagementObjectSearcher

using System.Diagnostics;
using System.IO;

using System.Runtime.InteropServices;   //for DllImport

using System.Text.RegularExpressions;   //for Regex

using Microsoft.VisualBasic.Devices;

using System.Collections;       //for DictionaryEntry
using System.Drawing.Imaging;   //for ImageFormat


namespace vcs_test_all_04
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            Image myImage = System.Drawing.Image.FromFile(filename);
            pictureBox1.Image = myImage;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 140;
            dy = 60;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //圖片轉向
            string filename = @"C:\______test_files\picture1.jpg";
            //pictureBox1.Image = Image.FromFile(filename);


            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            pictureBox1.Image = bitmap1;


            Bitmap bitmap2 = (Bitmap)Bitmap.FromFile(filename);
            bitmap2.RotateFlip(RotateFlipType.Rotate90FlipX);
            pictureBox2.Image = bitmap2;


        }

        private void button11_Click(object sender, EventArgs e)
        {
            Image myImage = pictureBox1.Image;
            myImage.RotateFlip(RotateFlipType.Rotate90FlipXY);
            pictureBox1.Image = myImage;
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }
    }
}

